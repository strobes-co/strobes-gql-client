import logging
from strobes_gql_client.base_client import BaseClient
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation
from strobes_gql_client import schema
import requests

# All scalar (leaf, no-subselection-needed) fields on the public BugType.
# Deliberately excludes relation fields (asset, connector, connectorConfig,
# scan, otherScans, engagements, originalBug, bugTags, assignedTo, reportedBy,
# duplicate) since those need their own subselection, and `cwe`/`cve` since
# the client's locally generated schema.py (built from the internal schema)
# types them as object lists, while the public API actually returns them as
# a scalar GenericScalar — selecting them here would emit a subselection the
# public backend rejects. `branch_history`/`branches` aren't in this
# generated schema.py at all yet.
BUG_FULL_FIELDS = (
    "id",
    "title",
    "description",
    "mitigation",
    "steps_to_reproduce",
    "evidence",
    "object_id",
    "hash",
    "state",
    "severity",
    "bug_level",
    "alert_category",
    "cvss",
    "attack_vector",
    "cvss_v3",
    "cvss_v3_attack_vector",
    "cvss_v4",
    "cvss_v4_attack_vector",
    "due_date",
    "risk_acceptance_due_date",
    "sla_violated",
    "has_user_defined_due_date",
    "exploit_available",
    "exploit_info",
    "patch_available",
    "patch_info",
    "prioritization_score",
    "prioritization_score_calculated",
    "drill_down_score",
    "nuclie_template",
    "nuclie_rule_set",
    "nuclie_target",
    "configuration_name",
    "scanner_raw_response",
    "scan_raw_response",
    "batch_id",
    "temp_id",
    "recently_rediscovered_batch_id",
    "vulnerable_since",
    "priority_last_updated",
    "zero_day_available",
    "is_wormable",
    "trend",
    "advisories_seen",
    "epss_score",
    "cisa_due_date",
    "records_at_risk",
    "records_type",
    "fields",
    "links",
    "metadata",
    "asm_last_updated",
    "is_misconfiguration",
    "sla_rule_search_query",
    "created",
    "updated",
    "is_active",
    "is_alert",
    "smart_close",
    "is_reopened",
    "last_smart_closed_on",
    "last_reopened_on",
    "is_automated_patched",
    "patch_data",
    "maintf",
    "tf_prev_state",
    "last_data_enriched",
    "is_data_enriched",
    "ai_title",
    "ai_description",
    "ai_mitigation",
    "priority_rule_data",
    "cost_of_risk",
    "last_resolved_on",
    "port",
    "content_object",
)


class StrobesGQLClient(BaseClient):
    def __init__(self, host, api_token, verify=True):
        super().__init__(host=host, api_token=api_token)
        self.logger = logging.getLogger(self.__class__.__name__)
        session = requests.Session()
        session.verify = verify
        self.graphql_url = f"{self.app_url}api/public/graphql/"
        self.endpoint = RequestsEndpoint(
            self.graphql_url, self.headers, session=session
        )

    def execute_query(self, query_name, **variables):
        try:
            op = Operation(schema.Query)
            query = getattr(op, query_name)
            result = query(**variables)

            # NOTE:
            # Your backend error:
            #   "Field Bug.connector cannot be both deferred and traversed using select_related at the same time."
            # is typically raised by Django ORM when a queryset contains BOTH:
            #   - select_related('connector')
            #   - defer('connector') / only(...) that implicitly defers it
            #
            # GraphQL optimizers (graphene-django-optimizer / custom get_queryset) commonly
            # defer relations that are NOT requested in the GraphQL selection set.
            #
            # Workaround on the client: explicitly request a minimal connector selection
            # for allBugs so the backend won't "defer" it.
            if query_name == "all_bugs":
                # Pagination/meta fields
                result.has_next()
                result.has_previous()
                result.last_cursor()
                result.before_cursor()

                # Full scalar bug field set + a minimal connector selection
                result.objects.__fields__(*BUG_FULL_FIELDS)
                result.objects.connector.__fields__("id", "name", "slug")

            data = self.endpoint(op)
            if data:
                self.logger.debug(f"{query_name} executed successfully.")
                return data
            else:
                self.logger.error(
                    f"No data returned for {query_name} or an error occurred."
                )
                return None
        except AttributeError:
            self.logger.error(f"Query '{query_name}' not found in schema.")
            raise
        except Exception as e:
            self.logger.exception(
                f"An error occurred while executing {query_name}: {str(e)}"
            )
            raise

    def execute_mutation(self, mutation_name, **variables):
        try:
            op = Operation(schema.Mutation)
            mutation = getattr(op, mutation_name)
            result = mutation(**variables)

            if mutation_name == "bug_create":
                result.bug.__fields__(*BUG_FULL_FIELDS)

            if mutation_name == "bug_bulk_update":
                result.bugs.__fields__("id", "state", "severity")

            data = self.endpoint(op)
            graphql_name = getattr(schema.Mutation, mutation_name).graphql_name
            payload = (data.get("data") or {}).get(graphql_name) if data else None
            if payload is not None:
                self.logger.debug(f"{mutation_name} executed successfully.")
                return payload
            else:
                self.logger.error(
                    f"No data returned for {mutation_name} or an error occurred."
                )
                return None
        except AttributeError:
            self.logger.error(f"Mutation '{mutation_name}' not found in schema.")
            raise
        except Exception as e:
            self.logger.exception(
                f"An error occurred while executing {mutation_name}: {str(e)}"
            )
            raise
