# Strobes GraphQL Client Wiki

The **Strobes GraphQL Client** is a Python wrapper around the Strobes **public
GraphQL API**. It turns raw GraphQL operations into simple method calls so you
can automate everything you'd normally do in the Strobes UI — manage assets and
findings, run engagements, post comments, generate reports, and export data in
bulk.

This wiki is the complete, user-friendly manual. If you just want to get
running, jump to the [Quickstart](Quickstart).

## New here? Read in this order

1. **[Installation](Installation)** — get the package onto your machine.
2. **[Configuration & Authentication](Configuration-and-Authentication)** — find your host, API token, and organization ID.
3. **[Quickstart](Quickstart)** — your first query in under a minute.
4. **[Core Concepts](Core-Concepts)** — how the client is structured, how responses look, and how pagination and errors work. **Read this once and everything else clicks.**

## Guides by topic

| Guide | What it covers |
|---|---|
| [Search Query Language](Search-Query-Language) | The filter syntax (`severity = 5 and state = 1`) used everywhere, plus field references per object |
| [Assets](Assets) | List, search, create (web/mobile/network/cloud/code), custom fields, bulk updates |
| [Findings](Findings) | List, search, create, bulk-update state/severity, CSV updates |
| [Engagements](Engagements) | List, search, create, update state (single & bulk) |
| [Comments](Comments) | Read and post comments on findings and engagements |
| [Vault Documents](Vault-Documents) | Upload and list engagement/vault documents |
| [Reports](Reports) | Templates, preview, generate PDF reports, attachments |
| [Exporting Data](Exporting-Data) | Async CSV exports of all bugs/assets, plus streaming helpers |
| [Connectors & Scan Logs](Connectors-and-Scan-Logs) | List connector configurations and scan history |
| [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports) | Workspace files, sheet CSV imports, finding CSV updates |

## Reference

| Reference | What it is |
|---|---|
| [Python API Reference](Python-API-Reference) | Every method on `StrobesGQLClient`, with signatures and return shapes |
| [GraphQL API Reference](GraphQL-API-Reference) | The public queries and mutations the client supports |
| [Troubleshooting](Troubleshooting) | Common errors and how to fix them |

## A taste of the client

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Read: critical, still-open findings
resp = client.execute_query(
    "all_bugs",
    organization_id=enums.ORGANIZATION_ID,
    search_query="severity = 5 and state = 1",
)
print(len(resp["data"]["allBugs"]["objects"]), "critical open findings")

# Write: create a web asset
client.execute_mutation(
    "create_asset",
    organization_id=enums.ORGANIZATION_ID,
    name="Production Web App",
    type=1,                       # 1 = Web
    url="https://app.example.com",
    sensitivity=3, exposed=2,
)

# Export: every asset to a CSV, the server does the heavy lifting
report = client.export_assets_and_wait(enums.ORGANIZATION_ID)
print(report["file"])            # signed download URL
```

## Runnable examples

Every feature in this wiki has a matching script in the repo's
[`examples/`](https://github.com/strobes-co/strobes-gql-client/tree/main/examples)
directory. Set `STROBES_API_TOKEN` and `STROBES_ORGANIZATION_ID`, then run any
of them — e.g. `python examples/test-fetchassets-example.py`.

> **Note on scope.** This client targets the Strobes **public** GraphQL
> endpoint (`/api/public/graphql/`). The bundled `schema.py` is generated from
> the full internal schema, so it describes many more types than the public
> endpoint exposes. This wiki documents only what the public endpoint actually
> supports — those are the operations the client is built around.
