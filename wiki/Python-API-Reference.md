# Python API Reference

Every public method on `StrobesGQLClient`, grouped by purpose. Snake_case
operation names are used throughout. For the response-shape rules (queries
return the full envelope; `execute_mutation` returns the payload directly), see
[Core Concepts](Core-Concepts#response-shapes-important).

## Construction

```python
StrobesGQLClient(host, api_token, verify=True)
```

| Argument | Default | Description |
|---|---|---|
| `host` | — | Platform domain, e.g. `mycorp.strobes.co` |
| `api_token` | — | API token from Settings → API Access |
| `verify` | `True` | TLS certificate verification |

See [Configuration & Authentication](Configuration-and-Authentication).

---

## Generic dispatchers

### `execute_query(query_name, **variables)`

Runs a supported query and returns the full GraphQL envelope
(`{"data": {...}}`) or raises [`GraphQLRequestError`](Core-Concepts#error-handling).

Supported `query_name` values and their key arguments:

| `query_name` | Key arguments | Guide |
|---|---|---|
| `all_assets` | `organization_id`, `search_query`, `order_by`, `page_size`, `after` | [Assets](Assets) |
| `asset` | `id` | [Assets](Assets#fetch-a-single-asset) |
| `all_bugs` | `organization_id`, `search_query`, `order_by`, `page_size`, `after` | [Findings](Findings) |
| `all_engagements` | `organization_id`, `search_query`, `order_by`, `asset_id`, `page`, `page_size` | [Engagements](Engagements) |
| `all_comments` | `organization_id`, `bug_id`, `engagement_id`, `internal`, `search_query`, `order_by`, `page`, `page_size` | [Comments](Comments) |
| `all_vault_attachments` | `organization_id`, `search_query`, `page`, `page_size` | [Vault Documents](Vault-Documents) |
| `all_templates` | `organization_id`, `template_id`, `search_query`, `page`, `page_size` | [Reports](Reports) |
| `preview_report` | `organization_id`, `template_id`, `report_name`, `search_query`, `asset_search_query` | [Reports](Reports#2-preview-a-report) |
| `download_report` | `organization_id`, `export_id` | [Reports](Reports) · [Exporting Data](Exporting-Data) |

> Other queries exist in the schema, but the ones above are what the client
> wires up field selections for on the public endpoint.

### `execute_mutation(mutation_name, **variables)`

Runs a supported mutation and returns its **payload directly**, or raises
`GraphQLRequestError`.

| `mutation_name` | Key arguments | Returns | Guide |
|---|---|---|---|
| `create_asset` | `organization_id`, `name`, `type`, type-specific field, `sensitivity`, `exposed`, `tags`, `custom_fields` | asset payload | [Assets](Assets#create-an-asset) |
| `bug_create` | `organization_id`, `title`, `description`, `bug_level`, `severity`, `mitigation`, `steps_to_reproduce`, `selected_assets`, type JSON | `{bug}` | [Findings](Findings#create-a-finding) |
| `bug_bulk_update` | `organization_id`, `search_query`, `state`, `severity` | `{bugs: [...]}` | [Findings](Findings#update-state-andor-severity) |
| `add_bug_comment` | `organization_id`, `bug_id`, `comment`, `internal`, `attachments` | `{comment}` | [Comments](Comments) |
| `add_engagement_comment` | `organization_id`, `engagement_id`, `comment`, `attachments` | `{comment}` | [Comments](Comments) |
| `create_engagement` | see [Engagements](Engagements#create-an-engagement) | engagement payload | [Engagements](Engagements) |
| `update_engagement` | `organization_id`, `engagement_id`, `state`, … | `{engagement}` | [Engagements](Engagements#single-engagement--update_engagement) |
| `bulk_update_engagements` | `organization_id`, `engagement_ids`, `state`, … | `{engagements: [...]}` | [Engagements](Engagements#many-engagements--bulk_update_engagements) |
| `add_report_template` | `organization_id`, `template_name`, `html_data`, `mode`, `type` | `{templates}` | [Reports](Reports#create-a-template) |
| `generate_report` | `organization_id`, `template_id`, `report_name`, `search_query`, `asset_search_query`, `password` | `{reports, password_required}` | [Reports](Reports#3-generate-a-report) |
| `export_bugs` | `organization_id`, `search_query` | `{exportId, status}` | [Exporting Data](Exporting-Data) |
| `export_assets` | `organization_id`, `search_query` | `{exportId, status}` | [Exporting Data](Exporting-Data) |

---

## Dedicated list methods

### `all_configurations(organization_id, order_by=None, search_query=None, page=1, page_size=10)`

Lists connector configurations. Returns the offset-paginated payload.
→ [Connectors & Scan Logs](Connectors-and-Scan-Logs#list-connector-configurations)

### `all_logs(organization_id, search_query=None, order_by=None, page=1, page_size=10)`

Lists scan logs. Returns the offset-paginated payload.
→ [Connectors & Scan Logs](Connectors-and-Scan-Logs#list-scan-logs)

---

## Asset custom fields

### `bulk_update_asset_custom_fields(organization_id, search_query, fields)`

Sets custom-field values on every asset matching `search_query` (RQL, **must be
non-empty**). `fields` is a `{slug: value}` dict. Returns `{"asset": [...]}`;
≤100 assets are updated inline, more are queued as a background task (empty
list). Raises `ValueError` on a blank query or empty `fields`.
→ [Assets](Assets#updating-custom-fields-on-existing-assets)

---

## Exports

### `export_bugs(organization_id, search_query=None)`
### `export_assets(organization_id, search_query=None)`

Start an async CSV export; return immediately with `{exportId, status}`.

### `export_bugs_and_wait(organization_id, search_query=None, poll_interval=3.0, timeout=1800)`
### `export_assets_and_wait(organization_id, search_query=None, poll_interval=3.0, timeout=1800)`

Start an export and poll `download_report` until it finishes. Return the
finished report dict (with a `file` URL). Raise `RuntimeError` on a failed
export (`status == "3"`) or `TimeoutError` if it doesn't finish in time.

### `export_all_bugs(organization_id, search_query=None, order_by=None, page_size=200, min_page_size=25, max_retries=5, initial_backoff=2.0, max_backoff=30.0)`
### `export_all_assets(organization_id, search_query=None, page_size=200, min_page_size=25, max_retries=5, initial_backoff=2.0, max_backoff=30.0)`

Generators that page through everything, **yielding one list of objects per
page**, with automatic retries and adaptive batch sizing.

→ Full guide: [Exporting Data](Exporting-Data)

---

## File uploads

### `upload_workspace_file(workspace_id, file_path, path=None)`

Upload a file into a workspace. Returns `{success, file{...}}`.

### `import_csv(file_path, organization_id, sheet_id=None, work_book_id=None, import_override=None, merge_with=None, name=None)`

Import a CSV into a sheet/workbook. Returns `{success, message}`.

### `update_bugs_fields_with_csv(file_path, organization_id)`

Bulk-update finding custom fields from a CSV. Returns `{bug: [{id}, ...]}`.

### `add_report_attachment(file_path, organization_id)`

Upload a report attachment. Returns `{attachment{...}}`.

→ Full guide: [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports)

---

## Attributes

| Attribute | Description |
|---|---|
| `client.app_url` | `https://<host>:<port>/` |
| `client.graphql_url` | `https://<host>:<port>/api/public/graphql/` |
| `client.headers` | Request headers (incl. `Authorization`) |
| `client.endpoint` | The underlying `sgqlc` `RequestsEndpoint` |
| `client.logger` | `logging.Logger` named `StrobesGQLClient` |

## Exceptions

See [Core Concepts → Error handling](Core-Concepts#error-handling) for the full
table. The key one is `GraphQLRequestError` (from
`strobes_gql_client.exceptions`), which exposes `.operation_name` and `.errors`.
