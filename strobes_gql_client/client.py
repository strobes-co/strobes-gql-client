import json
import logging
import mimetypes
from strobes_gql_client.base_client import BaseClient
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation
from sgqlc.types import Variable, non_null
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


# Scalar fields the public ConfigurationsFieldType exposes. The locally
# generated schema.py carries the *internal* ConfigurationsFieldType, which
# also has reverse-relation sets (configurationsSet, scanlogSet, bugSet,
# ...) that need their own subselection — pin to scalars here and select
# connector/organization/createdBy separately.
CONFIGURATION_FIELDS = (
    "id",
    "name",
    "object_id",
    "key",
    "remote_access_id",
    "remote_access_url",
    "is_default",
    "created",
    "updated",
    "extra",
    "is_automated",
    "auto_close_findings",
    "auto_smart_merge_assets",
    "send_csv_report_with_summary",
    "enable_github_webhook",
    "github_webhook_triggers",
)

# Scalar fields the public AllScanLogType exposes. Excludes the internal
# type's reverse-relation/list fields (childTasks, assetSet, bugSet, ...)
# and JSON blobs not needed for polling scan status — select config/
# createdBy separately.
SCAN_LOG_FIELDS = (
    "id",
    "task_id",
    "finished",
    "type",
    "is_triangulum_scanner",
    "task_retry_count",
    "triangulum_task_finished",
    "scanner_task_id",
    "build_status",
    "is_scheduled",
    "external_scheduled_task",
    "error_code",
    "status",
    "is_child_task",
    "started",
    "status_last_updated",
    "error_info",
    "asset",
    "organization_id",
    "connector_name",
    "connector_slug",
    "scan_arguments",
    "events",
)


def _select_configuration(result):
    """Apply the public ConfigurationsFieldType selection to a node."""
    result.__fields__(*CONFIGURATION_FIELDS)
    result.connector.__fields__("id", "name", "slug")
    result.organization.__fields__("id", "name")
    result.created_by.__fields__("id", "email", "first_name", "last_name")


def _select_scan_log(result):
    """Apply the public AllScanLogType selection to a node."""
    result.__fields__(*SCAN_LOG_FIELDS)
    result.config.__fields__("id", "name")
    result.created_by.__fields__("id", "email", "first_name", "last_name")


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

    def all_configurations(
        self, organization_id, order_by=None, search_query=None, page=1, page_size=10
    ):
        """List an organization's connector configurations via the
        `allConfigurations` query."""
        op = Operation(schema.Query)
        result = op.all_configurations(
            organization_id=str(organization_id),
            order_by=order_by,
            search_query=search_query,
            page=page,
            page_size=page_size,
        )
        result.page()
        result.total_pages()
        result.page_size()
        result.total_count()
        result.has_next()
        result.has_prev()
        _select_configuration(result.objects)

        data = self.endpoint(op)
        return (data.get("data") or {}).get("allConfigurations") if data else None

    def all_logs(
        self, organization_id, search_query=None, order_by=None, page=1, page_size=10
    ):
        """List an organization's scan logs via the `allLogs` query.

        Note: the public API's `allLogs` doesn't accept a `log_type` filter
        (unlike the internal schema) — only organization_id/search_query/
        order_by/page/page_size are supported.
        """
        op = Operation(schema.Query)
        result = op.all_logs(
            organization_id=str(organization_id),
            search_query=search_query,
            order_by=order_by,
            page=page,
            page_size=page_size,
        )
        result.page()
        result.total_pages()
        result.page_size()
        result.total_count()
        result.has_next()
        result.has_prev()
        _select_scan_log(result.objects)

        data = self.endpoint(op)
        return (data.get("data") or {}).get("allLogs") if data else None

    def _execute_multipart_operation(
        self, op, graphql_field, file_path, file_variable="file"
    ):
        """Send an sgqlc-built Operation containing an `Upload!` variable.

        sgqlc's RequestsEndpoint (used by execute_mutation/execute_query) only
        ever sends plain application/json, so an Operation with a file
        argument can't go through it. This serializes `op`'s schema-checked
        query text and sends it as a GraphQL multipart request
        (https://github.com/jaydenseric/graphql-multipart-request-spec)
        directly, attaching the file as its own part.
        """
        operations = {
            "query": bytes(op).decode("utf-8"),
            "variables": {file_variable: None},
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
        op = Operation(
            schema.Mutation,
            name="UploadWorkspaceFile",
            variables={"file": non_null(schema.Upload)},
        )
        result = op.upload_workspace_file(
            workspace_id=str(workspace_id), file=Variable("file"), path=path
        )
        result.success()
        result.file.__fields__(
            "name", "path", "is_folder", "size", "last_modified", "content_type"
        )
        return self._execute_multipart_operation(op, "uploadWorkspaceFile", file_path)

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
        op = Operation(
            schema.Mutation,
            name="ImportSheetCSV",
            variables={"file": non_null(schema.Upload)},
        )
        result = op.import_csv(
            file=Variable("file"),
            organization_id=str(organization_id),
            sheet_id=sheet_id,
            work_book_id=work_book_id,
            import_override=import_override,
            merge_with=merge_with,
            name=name,
        )
        result.success()
        result.message()
        return self._execute_multipart_operation(op, "importCsv", file_path)

    def update_bugs_fields_with_csv(self, file_path, organization_id):
        """Bulk-update finding custom fields from a CSV via the
        `updateBugsFieldsWithCsv` mutation."""
        op = Operation(
            schema.Mutation,
            name="UpdateBugsFieldsWithCsv",
            variables={"file": non_null(schema.Upload)},
        )
        result = op.update_bugs_fields_with_csv(
            organization_id=str(organization_id), file=Variable("file")
        )
        result.bug.__fields__("id")
        return self._execute_multipart_operation(
            op, "updateBugsFieldsWithCsv", file_path
        )

    def add_report_attachment(self, file_path, organization_id):
        """Upload a file as a report attachment via the `addReportAttachment` mutation."""
        op = Operation(
            schema.Mutation,
            name="AddReportAttachment",
            variables={"file": non_null(schema.Upload)},
        )
        result = op.add_report_attachment(
            organization_id=str(organization_id), file=Variable("file")
        )
        result.attachment.__fields__(
            "id", "attachment", "attachment_name", "created", "updated", "url"
        )
        result.attachment.attached_by.__fields__(
            "id", "email", "first_name", "last_name"
        )
        return self._execute_multipart_operation(op, "addReportAttachment", file_path)
