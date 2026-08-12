import json
import logging
import mimetypes
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

# Scalar fields the public CommentType exposes. The locally generated
# schema.py carries the *internal* CommentType, which is a superset — the
# public backend rejects the extra relation fields (bug, team, approval,
# connector, connectorConfig, activity, automationWorkflow, ...), so pin the
# selection to what the public surface actually returns.
COMMENT_FIELDS = (
    "id",
    "comment",
    "internal",
    "bug_id",
    "engagement_id",
    "created",
    "updated",
)


def _select_comment(result):
    """Apply the public CommentType selection to a CommentType node."""
    result.__fields__(*COMMENT_FIELDS)
    result.commented_by.__fields__("id", "email", "first_name", "last_name")
    result.attachments.__fields__(
        "id", "attachment_name", "attachment_size", "caption", "url"
    )


# Scalar fields the public TemplateType exposes. The locally generated
# schema.py carries the *internal* TemplateType, which is a superset (org,
# lock/co-editor/version-history relations) — pin the selection to what the
# public surface actually returns.
TEMPLATE_FIELDS = (
    "id",
    "template_name",
    "mode",
    "type",
    "is_active",
    "is_editable",
    "created",
    "updated",
    "custom_fields",
    "html",
)

# Scalar fields the public ReportType exposes. Same story as TEMPLATE_FIELDS
# — the internal ReportType carries report_type/scan/bug_ids/organization/etc,
# none of which the public surface exposes.
REPORT_FIELDS = (
    "id",
    "report_name",
    "status",
    "created",
    "export_id",
    "file",
    "has_password",
)


def _select_template(result):
    """Apply the public TemplateType selection to a TemplateType node."""
    result.__fields__(*TEMPLATE_FIELDS)
    result.created_by.__fields__("id", "email", "first_name", "last_name")


def _select_report(result):
    """Apply the public ReportType selection to a ReportType node."""
    result.__fields__(*REPORT_FIELDS)
    result.template.__fields__("id", "template_name")


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

            if query_name == "all_comments":
                # Pagination/meta fields
                result.page()
                result.total_pages()
                result.page_size()
                result.total_count()
                result.has_next()
                result.has_prev()
                _select_comment(result.objects)

            if query_name == "all_templates":
                # Pagination/meta fields
                result.page()
                result.total_pages()
                result.page_size()
                result.total_count()
                result.has_next()
                result.has_prev()
                _select_template(result.objects)

            if query_name == "download_report":
                _select_report(result)

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

            if mutation_name in ("add_bug_comment", "add_engagement_comment"):
                _select_comment(result.comment)

            if mutation_name == "add_report_template":
                _select_template(result.templates)

            if mutation_name == "generate_report":
                result.reports()
                result.password_required()

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

    def _execute_multipart_mutation(
        self, query, variables, graphql_field, file_path, file_variable="file"
    ):
        """Execute a GraphQL mutation that takes an `Upload!` argument.

        sgqlc's RequestsEndpoint (used by execute_mutation/execute_query) only
        ever sends plain application/json, so mutations with a file argument
        can't go through it. This sends a GraphQL multipart request
        (https://github.com/jaydenseric/graphql-multipart-request-spec)
        directly, the same way examples/test-create-vault-example.py does.
        """
        operations = {
            "query": query,
            "variables": {**variables, file_variable: None},
        }
        map_ = {"0": [f"variables.{file_variable}"]}

        with open(file_path, "rb") as fh:
            files = {
                "0": (
                    fh.name.split("/")[-1],
                    fh,
                    mimetypes.guess_type(file_path)[0] or "application/octet-stream",
                )
            }
            response = requests.post(
                self.graphql_url,
                headers=self.headers,
                data={"operations": json.dumps(operations), "map": json.dumps(map_)},
                files=files,
            )

        response.raise_for_status()
        result = response.json()
        if result.get("errors"):
            self.logger.error(f"GraphQL errors: {result['errors']}")
            raise Exception(f"GraphQL errors: {result['errors']}")

        return (result.get("data") or {}).get(graphql_field)

    def upload_workspace_file(self, workspace_id, file_path, path=None):
        """Upload a file to a workspace's S3 storage via the `uploadWorkspaceFile` mutation."""
        query = """
            mutation UploadWorkspaceFile($workspaceId: UUID!, $file: Upload!, $path: String) {
                uploadWorkspaceFile(workspaceId: $workspaceId, file: $file, path: $path) {
                    success
                    file {
                        name
                        path
                        isFolder
                        size
                        lastModified
                        contentType
                    }
                }
            }
        """
        variables = {"workspaceId": str(workspace_id), "path": path}
        return self._execute_multipart_mutation(
            query, variables, "uploadWorkspaceFile", file_path
        )

    def import_csv(
        self,
        file_path,
        organization_id,
        sheet_id=None,
        work_book_id=None,
        import_override=None,
        merge_with=None,
        name=None,
    ):
        """Import a CSV into a sheet/workbook via the `importCsv` mutation."""
        query = """
            mutation ImportSheetCSV(
                $file: Upload!
                $organizationId: UUID!
                $sheetId: Int
                $workBookId: Int
                $importOverride: Boolean
                $mergeWith: Boolean
                $name: String
            ) {
                importCsv(
                    file: $file
                    organizationId: $organizationId
                    sheetId: $sheetId
                    workBookId: $workBookId
                    importOverride: $importOverride
                    mergeWith: $mergeWith
                    name: $name
                ) {
                    success
                    message
                }
            }
        """
        variables = {
            "organizationId": str(organization_id),
            "sheetId": sheet_id,
            "workBookId": work_book_id,
            "importOverride": import_override,
            "mergeWith": merge_with,
            "name": name,
        }
        return self._execute_multipart_mutation(
            query, variables, "importCsv", file_path
        )

    def update_bugs_fields_with_csv(self, file_path, organization_id):
        """Bulk-update finding custom fields from a CSV via the
        `updateBugsFieldsWithCsv` mutation."""
        query = """
            mutation UpdateBugsFieldsWithCsv($organizationId: UUID!, $file: Upload!) {
                updateBugsFieldsWithCsv(organizationId: $organizationId, file: $file) {
                    bug {
                        id
                    }
                }
            }
        """
        variables = {"organizationId": str(organization_id)}
        return self._execute_multipart_mutation(
            query, variables, "updateBugsFieldsWithCsv", file_path
        )
