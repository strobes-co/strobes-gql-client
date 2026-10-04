# Troubleshooting

Common problems and how to fix them. If you're just getting set up, re-check
[Configuration & Authentication](Configuration-and-Authentication) first.

## Authentication & connection

### `GraphQLRequestError: ... permission` / 403

**"You do not have permission to perform this action."**

- The API token is wrong, revoked, or belongs to a user without access to that
  organization. Regenerate it under **Settings → API Access**.
- You're calling an operation the public endpoint doesn't allow-list, or the
  backend hasn't been updated to expose it yet. Stick to the operations in the
  [GraphQL API Reference](GraphQL-API-Reference).
- The `organization_id` doesn't match the token's org.

### Connection refused / timeout / name resolution error

- Check `host` — it should be the bare domain (`mycorp.strobes.co`), no
  `https://`, no trailing slash, no path.
- Confirm you can reach the host from your network (VPN? firewall?).

### `SSLError` / certificate verification failed

The host uses a certificate your system doesn't trust. For a known self-signed
host you can disable verification:

```python
client = StrobesGQLClient(host=HOST, api_token=TOKEN, verify=False)
```

Only do this for trusted internal hosts — it disables TLS validation.

### Empty / missing credentials

`enums.API_TOKEN` / `enums.ORGANIZATION_ID` are `None` because the environment
variables aren't set. Export them, or edit `enums.py`:

```bash
export STROBES_API_TOKEN="<token>"
export STROBES_ORGANIZATION_ID="<org-id>"
```

## Operation errors

### `AttributeError` / "Query not found in schema"

The `query_name` / `mutation_name` is misspelled or isn't in the schema. Use the
exact snake_case name from the [Python API Reference](Python-API-Reference)
(e.g. `all_bugs`, not `allBugs` or `all_bug`).

### "Field X cannot be both deferred and traversed…" / subselection errors

You're selecting a field the **public** endpoint doesn't return as an object
(the generated schema describes the richer internal type). Use the client's
built-in methods/dispatchers, which pin the correct public field selection —
don't hand-build selections against the public endpoint. See the notes in
[`client.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/client.py)
and the [GraphQL API Reference](GraphQL-API-Reference#public-vs-internal-schema).

### "Expected Name, found String" on a custom-fields update

Don't inline a Python dict into a query string — the keys render as JSON strings
and the parser rejects them. Use the dedicated
`bulk_update_asset_custom_fields(...)` method, which sends `fields` as a GraphQL
variable. → [Assets](Assets#updating-custom-fields-on-existing-assets)

### `ValueError: search_query must be a non-empty RQL string`

`bulk_update_asset_custom_fields` refuses a blank `search_query` on purpose — an
empty query would match **every** asset in the org. Pass a real filter.

### My search query returns nothing (or everything)

- Numbers aren't quoted, strings are: `severity = 5`, `name ~ "prod"`.
- Check the enum codes — e.g. finding `severity` is `1`–`5` and `state` is
  `1`–`4`. See [Search Query Language](Search-Query-Language).
- An empty/omitted `search_query` returns everything the token can see.

## Pagination

### I only get the first page

That's expected — you have to walk pages. Use the right style for the endpoint
(cursor `after` vs. offset `page`), or better, use the export helpers. See
[Core Concepts → Pagination](Core-Concepts#pagination) and
[Exporting Data](Exporting-Data).

### Large exports time out at the gateway

Don't paginate `allBugs` / `allAssets` by hand for huge orgs. Use the async CSV
export (`export_bugs_and_wait` / `export_assets_and_wait`) or the streaming
generators (`export_all_bugs` / `export_all_assets`), which retry and shrink the
batch automatically. → [Exporting Data](Exporting-Data)

## Exports & reports

### `TimeoutError: ... did not finish within Ns`

The server export ran past `timeout`. Raise it (`timeout=3600`) for very large
orgs, or scope the export with a `search_query`.

### `RuntimeError: export ... failed (status=3)`

The server-side export job failed. Retry; if it persists, check the export in
the UI and contact support.

### `download_report` says "Invalid export details."

Transient — the report row isn't created yet in the moment just after an export
starts. The `_and_wait` helpers handle this for you (treating it as "not ready,
retry"). If polling yourself, treat it the same way.

### "This org requires a report password"

`generate_report` returned `password_required: true`. Pass `password="..."`.

## File uploads

### Upload does nothing / wrong content type

Pass a real path to a readable file. The client guesses the MIME type and falls
back to `application/octet-stream`. For vault uploads specifically, see the
inline snippet in [Vault Documents](Vault-Documents#upload-a-document).

## Logging & debugging

Turn on debug logging to see each operation and the raw errors:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

The client logs under the `StrobesGQLClient` logger. Expected-transient
conditions are logged at DEBUG, real failures at ERROR.

## Still stuck?

- Re-read [Core Concepts](Core-Concepts) — most issues are response-shape or
  pagination misunderstandings.
- Compare against the matching script in
  [`examples/`](https://github.com/strobes-co/strobes-gql-client/tree/main/examples).
- Open an issue on the
  [repository](https://github.com/strobes-co/strobes-gql-client/issues).
