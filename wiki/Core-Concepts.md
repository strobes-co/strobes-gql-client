# Core Concepts

Understand this page once and the rest of the wiki reads easily. It explains how
the client is put together, the two ways to call the API, what responses look
like, how pagination works, and how errors surface.

## The client object

Everything hangs off a single `StrobesGQLClient` instance:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)
```

Under the hood it:

- Builds the endpoint URL `https://<host>/api/public/graphql/`.
- Attaches your `Authorization: token <api_token>` header to every request.
- Uses [`sgqlc`](https://github.com/profusion/sgqlc) to build and validate each
  GraphQL operation against the bundled `schema.py` before sending it.

You typically create one client and reuse it.

## Two ways to call the API

### 1. The generic dispatchers: `execute_query` / `execute_mutation`

Most operations go through one of two methods:

```python
client.execute_query(query_name, **arguments)       # reads
client.execute_mutation(mutation_name, **arguments)  # writes
```

- `query_name` / `mutation_name` is the operation in **snake_case**
  (`all_bugs`, `create_asset`, `add_bug_comment`). The client maps it to the
  GraphQL camelCase name for you.
- `**arguments` are the operation's arguments, also in snake_case
  (`organization_id`, `search_query`, `page_size`).

The client already knows which fields to request for each supported operation,
so you never write a GraphQL selection set by hand.

### 2. Dedicated helper methods

Some operations have a purpose-built method because they need special handling
(file uploads, GraphQL variables, retry loops, or polling). You call these
directly:

| Method | Why it's special |
|---|---|
| `all_configurations(...)`, `all_logs(...)` | Convenience list wrappers |
| `bulk_update_asset_custom_fields(...)` | Sends `fields` as a GraphQL variable |
| `export_bugs_and_wait(...)`, `export_assets_and_wait(...)` | Start an export and poll until done |
| `export_all_bugs(...)`, `export_all_assets(...)` | Stream every page with adaptive retries |
| `upload_workspace_file(...)`, `import_csv(...)`, `update_bugs_fields_with_csv(...)`, `add_report_attachment(...)` | Multipart file uploads |

See the [Python API Reference](Python-API-Reference) for the full list.

## Response shapes (important)

This trips people up, so read carefully — the two dispatchers unwrap results
differently.

### `execute_query` returns the full GraphQL envelope

Your data is nested under `["data"][<camelCaseFieldName>]`:

```python
resp = client.execute_query("all_assets", organization_id=ORG)
# resp == {"data": {"allAssets": {"objects": [...], "hasNext": ..., ...}}}

assets = resp["data"]["allAssets"]["objects"]
```

Use `.get(...)` defensively if you want to avoid `KeyError`:

```python
assets = resp.get("data", {}).get("allAssets", {}).get("objects", [])
```

### `execute_mutation` returns the payload directly

It unwraps `["data"][<mutationName>]` for you and returns just that payload:

```python
result = client.execute_mutation("add_bug_comment", organization_id=ORG,
                                  bug_id=123, comment="Looks fixed.")
# result == {"comment": {"id": "...", "comment": "...", ...}}
comment_id = result["comment"]["id"]
```

### Dedicated methods return the useful part

The list wrappers return the paginated object (e.g. `{"objects": [...],
"totalCount": N, ...}`); the export helpers return the report dict; the
generators yield lists of objects. Each method's return shape is documented on
its guide page and in the [Python API Reference](Python-API-Reference).

## Pagination

Strobes uses **two** pagination styles, and which one applies depends on the
endpoint.

### Cursor pagination — `allBugs`, `allAssets`

These return a cursor envelope:

```python
{
  "objects":      [...],
  "hasNext":      true,
  "hasPrevious":  false,
  "lastCursor":   "cmVkYWN0ZWQ=",   # pass as `after` to get the next page
  "beforeCursor": "..."
}
```

Walk pages with the `after` argument:

```python
after = None
while True:
    resp = client.execute_query(
        "all_bugs", organization_id=ORG, page_size=200, after=after
    )
    page = resp["data"]["allBugs"]
    for bug in page["objects"]:
        ...
    if not page["hasNext"]:
        break
    after = page["lastCursor"]
```

> **You usually shouldn't do this by hand.** For "give me everything", use
> `export_all_bugs` / `export_all_assets` (which handle retries and adaptive
> batch sizing) or the async CSV export. See [Exporting Data](Exporting-Data).

### Offset pagination — `allEngagements`, `allComments`, `allConfigurations`, `allLogs`, `allTemplates`, `allVaultAttachments`

These return a page envelope:

```python
{
  "objects":    [...],
  "page":       1,
  "pageSize":   10,
  "totalPages": 5,
  "totalCount": 48,
  "hasNext":    true,
  "hasPrev":    false
}
```

Walk pages with `page` / `page_size`:

```python
page = 1
while True:
    resp = client.execute_query(
        "all_comments", organization_id=ORG, bug_id=123, page=page, page_size=50
    )
    data = resp["data"]["allComments"]
    for c in data["objects"]:
        ...
    if not data["hasNext"]:
        break
    page += 1
```

## Filtering with search queries

Nearly every list endpoint accepts `search_query` — a filter written in the
**Strobes Query Language** (sometimes called RQL), e.g.
`severity in (4,5) and state = 1`. It's the same language the UI search bar
uses. Operators and per-object field references are in
[Search Query Language](Search-Query-Language).

Omitting `search_query` returns everything the token can see.

## Sorting

List endpoints that support ordering accept `order_by` as a list of field names.
Prefix a field with `-` for descending:

```python
client.execute_query("all_comments", organization_id=ORG,
                     bug_id=123, order_by=["-created"])   # newest first
```

## Error handling

The client raises rather than returning silent failures.

### `GraphQLRequestError`

Raised when the server responds with a GraphQL `errors` array — including the
case where a gateway timeout or 5xx is converted into
`{"data": null, "errors": [...]}`. This matters: without it, a timed-out export
page would look like an empty-but-successful page. Catch it to distinguish
"request failed" from "no results":

```python
from strobes_gql_client.exceptions import GraphQLRequestError

try:
    resp = client.execute_query("all_bugs", organization_id=ORG)
except GraphQLRequestError as e:
    print("Operation:", e.operation_name)
    print("Errors:", e.errors)
```

### Other exceptions

| Exception | When |
|---|---|
| `GraphQLRequestError` | Server returned GraphQL `errors` (incl. timeouts/5xx) |
| `AttributeError` | The `query_name`/`mutation_name` isn't in the schema (usually a typo) |
| `ValueError` | A dedicated method got invalid arguments (e.g. an empty `search_query` for `bulk_update_asset_custom_fields`) |
| `RuntimeError` | An export failed (`status == "3"`) or returned no data (check permissions) |
| `TimeoutError` | An `_and_wait` export didn't finish within `timeout` |
| `requests` exceptions | Network/TLS problems before a response was received |

Full list and messages: [exceptions.py](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/exceptions.py).

## Logging

The client logs through the standard `logging` module under the logger name
`StrobesGQLClient`. Turn on debug logging to see each operation as it runs:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Expected-and-transient conditions (like a report row not existing yet in the
split second after an export starts) are logged at `DEBUG`, not `ERROR`, so your
logs stay clean.

## File uploads

GraphQL file uploads can't ride the normal JSON transport. Methods that take a
file (`upload_workspace_file`, `import_csv`, `update_bugs_fields_with_csv`,
`add_report_attachment`, and vault uploads) use the
[GraphQL multipart request spec](https://github.com/jaydenseric/graphql-multipart-request-spec)
internally. You just pass a path — see
[File Uploads & CSV Imports](File-Uploads-and-CSV-Imports).

## Next steps

- [Search Query Language](Search-Query-Language)
- Pick a topic guide: [Assets](Assets), [Findings](Findings), [Engagements](Engagements)
- [Python API Reference](Python-API-Reference)
