import contextlib
import json
import logging
import mimetypes
import time
from strobes_gql_client.base_client import BaseClient
from strobes_gql_client.exceptions import GraphQLRequestError
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


# Scalar fields on AssetType. Deliberately excludes relation fields
# (organization, created_by, connector, other_connectors, workspace,
# linked_assets, linked_to, group_assets, asset_port, assessments_set,
# asset_package, asset_apis, configuration_asset, bug_set, activity_set,
# trackers_set, patch_set, source_relationships, target_relationships,
# tags, apis, outgoing_relationships, incoming_relationships,
# all_relationships) since those need their own subselection, and `scan`/
# `last_seen`, which are selected separately in `_select_asset` below.
ASSET_FULL_FIELDS = (
    "id",
    "name",
    "target",
    "exposed",
    "type",
    "cloud_type",
    "disabled",
    "sensitivity",
    "keys",
    "data",
    "additional_info",
    "sensitivity_reasoning",
    "exposure_reasoning",
    "temp_id",
    "is_active",
    "created",
    "updated",
    "location",
    "scanner_raw_response",
    "region",
    "resource_id",
    "account_id",
    "fields",
    "asset_region",
    "dns_info",
    "whois_info",
    "asn",
    "waf",
    "cdn",
    "asm_last_alive",
    "ipaddress",
    "hostname",
    "mac_address",
    "os",
    "cpe",
    "risk_score",
    "dns_a",
    "dns_ns",
    "dns_soa",
    "dns_aaaa",
    "dns_axfr",
    "dns_cname",
    "domain_org",
    "domain_city",
    "domain_state",
    "domain_dnssec",
    "domain_emails",
    "domain_status",
    "domain_address",
    "domain_country",
    "domain_registrar",
    "domain_name",
    "domain_name_servers",
    "domain_referral_url",
    "domain_updated_date",
    "domain_server",
    "domain_expiration_date",
    "domain_creation_date",
    "domain_registrant_postal_code",
    "port_addresses",
    "package_count",
    "webserver",
    "technology_used",
)

# Scalar fields on ScanLogType, the type AssetType.lastSeen resolves to.
ASSET_LAST_SEEN_FIELDS = (
    "id",
    "task_id",
    "config",
    "finished",
    "connector_name",
    "connector_slug",
)

# Scalar fields on ConnectorType, the type AssetType.connector /
# otherConnectors resolve to.
ASSET_CONNECTOR_FIELDS = (
    "id",
    "slug",
    "name",
    "type",
    "scanner_type",
    "is_internal",
    "is_active",
)


def _select_asset(result):
    """Apply the AssetType selection to a node, including lastSeen,
    connector, and otherConnectors.

    sgqlc's default auto-select depth doesn't reach far enough to pick up
    these nested relation objects (several levels below the query root),
    so they silently drop out of the response unless selected here.

    `otherConnectors` is every additional source (beyond the primary
    `connector`) that has also reported this asset — selecting it is what
    makes an asset export carry metadata "from each one of the sources"
    for assets discovered by more than one connector.
    """
    result.__fields__(*ASSET_FULL_FIELDS)
    result.last_seen.__fields__(*ASSET_LAST_SEEN_FIELDS)
    result.connector.__fields__(*ASSET_CONNECTOR_FIELDS)
    result.other_connectors.__fields__(*ASSET_CONNECTOR_FIELDS)


@contextlib.contextmanager
def _quiet_transient_report_lookup():
    """Silence sgqlc's own `logger.error('GraphQL query failed with %s
    errors', ...)` (sgqlc.endpoint.base) around a `download_report` poll.

    That log comes from sgqlc itself, before our code ever sees the
    response, so our own quieter handling of the expected "row not created
    yet" race in `execute_query` (see there) can't reach it. Callers here
    already treat every `download_report` error during polling as
    "not ready yet" and retry, so there's nothing this would be hiding.
    """
    sgqlc_logger = logging.getLogger("sgqlc.endpoint.base")
    previous_level = sgqlc_logger.level
    sgqlc_logger.setLevel(logging.CRITICAL)
    try:
        yield
    finally:
        sgqlc_logger.setLevel(previous_level)


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

            if query_name == "all_assets":
                # Pagination/meta fields
                result.has_next()
                result.has_previous()
                result.last_cursor()
                result.before_cursor()
                _select_asset(result.objects)

            if query_name == "asset":
                _select_asset(result)

            if query_name == "download_report":
                _select_report(result)

            data = self.endpoint(op)
            if data and data.get("errors"):
                # A gateway timeout or 5xx doesn't raise here — sgqlc's
                # RequestsEndpoint converts it into {"data": None,
                # "errors": [...]} and returns it like any other response.
                # Raise so a caller (or _fetch_page_with_retry) can tell
                # "this page failed" apart from "this page was empty".
                #
                # download_report briefly returns "Invalid export details."
                # in the window between exportBugs/exportAssets returning an
                # exportId and the backend task creating the row — callers
                # (e.g. export_bugs_and_wait) treat that as "not ready yet"
                # and retry, so log it quietly instead of as an error.
                is_transient_report_lookup = query_name == "download_report" and any(
                    "Invalid export details" in error.get("message", "")
                    for error in data["errors"]
                )
                if is_transient_report_lookup:
                    self.logger.debug(
                        f"{query_name}: report not created yet ({data['errors']})"
                    )
                else:
                    self.logger.error(
                        f"GraphQL errors for {query_name}: {data['errors']}"
                    )
                raise GraphQLRequestError(query_name, data["errors"])
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
        except GraphQLRequestError:
            # Already logged above at the appropriate level — avoid
            # double-logging a full traceback for an error we've already
            # reported (and, for download_report, may be expected/transient).
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

            if mutation_name == "bug_bulk_update_mitigation_description":
                result.bugs.__fields__(
                    "id", "description", "mitigation", "evidence", "steps_to_reproduce"
                )

            if mutation_name in ("add_bug_comment", "add_engagement_comment"):
                _select_comment(result.comment)

            if mutation_name == "add_report_template":
                _select_template(result.templates)

            if mutation_name == "generate_report":
                result.reports()
                result.password_required()

            data = self.endpoint(op)
            if data and data.get("errors"):
                self.logger.error(
                    f"GraphQL errors for {mutation_name}: {data['errors']}"
                )
                raise GraphQLRequestError(mutation_name, data["errors"])
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

    def _fetch_page_with_retry(
        self,
        query_name,
        graphql_key,
        variables,
        page_size,
        min_page_size,
        max_retries,
        initial_backoff,
        max_backoff,
    ):
        """Run one page of a cursor-paginated query, retrying transient
        failures (gateway timeouts, 5xx) with exponential backoff.

        If a page still fails after `max_retries` attempts, halve
        `page_size` (down to `min_page_size`) and start the retry count
        over — a batch that's too large to complete inside the gateway's
        timeout window will keep failing at a fixed size no matter how
        many times it's retried, so shrinking it is what actually
        resolves it, not more retries alone.

        Returns `(payload, page_size)` — the page's data and the page
        size that ended up succeeding, so the caller can keep using it for
        the next page.
        """
        attempt = 0
        while True:
            try:
                response = self.execute_query(
                    query_name, page_size=page_size, **variables
                )
                payload = (response.get("data") or {}).get(graphql_key) or {}
                return payload, page_size
            except Exception as exc:
                attempt += 1
                if page_size <= min_page_size and attempt > max_retries:
                    raise
                if attempt > max_retries:
                    page_size = max(min_page_size, page_size // 2)
                    attempt = 0
                    self.logger.warning(
                        f"{query_name}: repeated failures ({exc}); "
                        f"shrinking page_size to {page_size}"
                    )
                    continue
                backoff = min(max_backoff, initial_backoff * (2 ** (attempt - 1)))
                self.logger.warning(
                    f"{query_name}: attempt {attempt} failed ({exc}); "
                    f"retrying in {backoff:.1f}s"
                )
                time.sleep(backoff)

    def _export_cursor_paginated(
        self,
        query_name,
        graphql_key,
        page_size,
        min_page_size,
        max_retries,
        initial_backoff,
        max_backoff,
        **variables,
    ):
        """Page through a cursor-paginated query end to end, yielding each
        page's `objects` list.

        This is the recommended way to pull "everything" out of a
        cursor-paginated endpoint like `allBugs`/`allAssets`: instead of
        hand-rolling retry logic around `execute_query(...)` and guessing
        at a batch size that won't hit the gateway timeout, start with
        whatever `page_size` you'd like and let this shrink it on repeated
        failures and grow it back up once a run of pages succeeds cleanly.
        """
        after = None
        current_page_size = page_size
        consecutive_successes = 0

        while True:
            payload, current_page_size = self._fetch_page_with_retry(
                query_name,
                graphql_key,
                {**variables, "after": after},
                current_page_size,
                min_page_size,
                max_retries,
                initial_backoff,
                max_backoff,
            )
            objects = payload.get("objects") or []
            if objects:
                yield objects

            if current_page_size < page_size:
                consecutive_successes += 1
                if consecutive_successes >= 3:
                    current_page_size = min(page_size, current_page_size * 2)
                    consecutive_successes = 0

            if not payload.get("hasNext") or not objects:
                return
            after = payload.get("lastCursor")
            if not after:
                return

    def export_all_bugs(
        self,
        organization_id,
        search_query=None,
        order_by=None,
        page_size=200,
        min_page_size=25,
        max_retries=5,
        initial_backoff=2.0,
        max_backoff=30.0,
    ):
        """Export every bug in an organization via `allBugs` cursor
        pagination, yielding one list of bug objects per page.

        Handles the batch-size-vs-gateway-timeout tradeoff for you:
        transient failures are retried with backoff, and a batch that
        keeps timing out gets progressively smaller instead of failing the
        whole export (then grows back toward `page_size` once things
        settle). Use this instead of driving `execute_query("all_bugs",
        ...)` in a loop by hand.
        """
        yield from self._export_cursor_paginated(
            "all_bugs",
            "allBugs",
            page_size,
            min_page_size,
            max_retries,
            initial_backoff,
            max_backoff,
            organization_id=organization_id,
            search_query=search_query,
            order_by=order_by,
        )

    def export_all_assets(
        self,
        organization_id,
        search_query=None,
        page_size=200,
        min_page_size=25,
        max_retries=5,
        initial_backoff=2.0,
        max_backoff=30.0,
    ):
        """Export every asset in an organization via `allAssets` cursor
        pagination, yielding one list of asset objects per page.

        Each asset includes full metadata plus every source that reported
        it (`connector` and `otherConnectors`, via `_select_asset`). Same
        retry/backoff/adaptive-batching behavior as `export_all_bugs`.
        """
        yield from self._export_cursor_paginated(
            "all_assets",
            "allAssets",
            page_size,
            min_page_size,
            max_retries,
            initial_backoff,
            max_backoff,
            organization_id=organization_id,
            search_query=search_query,
        )

    def export_bugs(self, organization_id, search_query=None):
        """Kick off an async CSV export of every bug matching `search_query`
        (or every bug the token can see, if omitted) and return immediately.

        This is the recommended way to pull "everything" out of a large org
        instead of paginating `allBugs` yourself: the export runs as a
        background job on the server, so nothing about it can hit a gateway
        timeout the way a large synchronous `allBugs` batch can.

        Returns a dict with `exportId` (pass to `download_report` / to
        `export_bugs_and_wait` to poll) and `status` (a raw ExportReport
        status code: "0"=Pending, "1"=In-Progress, "2"=Finished, "3"=Failed).
        """
        result = self.execute_mutation(
            "export_bugs",
            organization_id=organization_id,
            search_query=search_query,
        )
        if not result:
            raise RuntimeError("exportBugs returned no data — check permissions.")
        return result

    def export_bugs_and_wait(
        self,
        organization_id,
        search_query=None,
        poll_interval=3.0,
        timeout=1800,
    ):
        """`export_bugs`, then poll `downloadReport` until it finishes.

        Returns the finished report dict (with a `file` URL) once
        `status == "2"`. Raises `RuntimeError` if the export reaches
        `status == "3"` (Failed), or `TimeoutError` if it doesn't finish
        within `timeout` seconds.
        """
        export = self.export_bugs(organization_id, search_query=search_query)
        export_id = export["exportId"]
        deadline = time.monotonic() + timeout

        while True:
            try:
                with _quiet_transient_report_lookup():
                    response = self.execute_query(
                        "download_report",
                        organization_id=organization_id,
                        export_id=export_id,
                    )
                report = (
                    (response.get("data") or {}).get("downloadReport")
                    if response
                    else None
                )
            except GraphQLRequestError:
                # downloadReport raises "Invalid export details." for the brief
                # window between this call returning exportId and the backend
                # task actually creating the row — expected and transient, not
                # a real failure. Treat exactly like "not ready yet" below.
                report = None

            if not report:
                if time.monotonic() >= deadline:
                    raise TimeoutError(
                        f"Bug export {export_id} did not finish within {timeout}s "
                        f"(export not found yet)."
                    )
                time.sleep(poll_interval)
                continue

            status = report.get("status")
            if status == "2":
                return report
            if status == "3":
                raise RuntimeError(f"Bug export {export_id} failed (status=3).")

            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"Bug export {export_id} did not finish within {timeout}s "
                    f"(last status={status})."
                )
            time.sleep(poll_interval)

    def export_assets(self, organization_id, search_query=None):
        """Kick off an async CSV export of every asset matching
        `search_query` (or every asset the token can see, if omitted) and
        return immediately.

        Each row covers the asset's full metadata (scanner_raw_response,
        dns_info, whois_info, custom fields) plus every source (connector)
        that contributed to it. Note: metadata itself is merged/overwritten
        on ingestion when multiple sources report the same asset — there is
        no way to attribute a specific field's value to a specific source,
        only to see which sources contributed. This is the most complete
        "metadata from each source" view the platform currently supports.

        Returns a dict with `exportId` (pass to `download_report` / to
        `export_assets_and_wait` to poll) and `status` (a raw ExportReport
        status code: "0"=Pending, "1"=In-Progress, "2"=Finished, "3"=Failed).
        """
        result = self.execute_mutation(
            "export_assets",
            organization_id=organization_id,
            search_query=search_query,
        )
        if not result:
            raise RuntimeError("exportAssets returned no data — check permissions.")
        return result

    def export_assets_and_wait(
        self,
        organization_id,
        search_query=None,
        poll_interval=3.0,
        timeout=1800,
    ):
        """`export_assets`, then poll `downloadReport` until it finishes.

        Returns the finished report dict (with a `file` URL) once
        `status == "2"`. Raises `RuntimeError` if the export reaches
        `status == "3"` (Failed), or `TimeoutError` if it doesn't finish
        within `timeout` seconds.
        """
        export = self.export_assets(organization_id, search_query=search_query)
        export_id = export["exportId"]
        deadline = time.monotonic() + timeout

        while True:
            try:
                with _quiet_transient_report_lookup():
                    response = self.execute_query(
                        "download_report",
                        organization_id=organization_id,
                        export_id=export_id,
                    )
                report = (
                    (response.get("data") or {}).get("downloadReport")
                    if response
                    else None
                )
            except GraphQLRequestError:
                # See export_bugs_and_wait — same transient "row not created
                # yet" race, not a real failure.
                report = None

            if not report:
                if time.monotonic() >= deadline:
                    raise TimeoutError(
                        f"Asset export {export_id} did not finish within {timeout}s "
                        f"(export not found yet)."
                    )
                time.sleep(poll_interval)
                continue

            status = report.get("status")
            if status == "2":
                return report
            if status == "3":
                raise RuntimeError(f"Asset export {export_id} failed (status=3).")

            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"Asset export {export_id} did not finish within {timeout}s "
                    f"(last status={status})."
                )
            time.sleep(poll_interval)

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

    def update_bug_mitigation_description(
        self,
        organization_id,
        search_query,
        description=None,
        mitigation=None,
        evidence=None,
        steps_to_reproduce=None,
        group_by_field=None,
        group_by_value=None,
    ):
        """Bulk-update findings' description/mitigation/evidence/steps-to-reproduce
        via the `bugBulkUpdateMitigationDescription` mutation.

        Findings are targeted with `search_query` (or `group_by_field`/
        `group_by_value`), not by ID directly — scope `search_query` tightly
        enough to match a single bug if that's the intent. Returns the list
        of updated bugs.
        """
        return self.execute_mutation(
            "bug_bulk_update_mitigation_description",
            organization_id=str(organization_id),
            search_query=search_query,
            description=description,
            mitigation=mitigation,
            evidence=evidence,
            steps_to_reproduce=steps_to_reproduce,
            group_by_field=group_by_field,
            group_by_value=group_by_value,
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
