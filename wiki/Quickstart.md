# Quickstart

This page gets you from zero to a working read, write, and export in a few
minutes. It assumes you've already done [Installation](Installation) and
[Configuration & Authentication](Configuration-and-Authentication).

## 1. Create a client

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)
ORG = enums.ORGANIZATION_ID
```

## 2. Read some data

Queries go through `execute_query(query_name, **arguments)`. The response is the
raw GraphQL envelope — your data is under `["data"][<graphqlFieldName>]`.

```python
resp = client.execute_query("all_assets", organization_id=ORG)
assets = resp["data"]["allAssets"]["objects"]

print(f"{len(assets)} assets")
for a in assets[:5]:
    print(f"- {a['name']} (type={a['type']}, risk={a['risk_score']})")
```

## 3. Filter with a search query

Almost every list endpoint accepts a `search_query` written in the
[Search Query Language](Search-Query-Language):

```python
resp = client.execute_query(
    "all_bugs",
    organization_id=ORG,
    search_query="severity = 5 and state = 1",   # critical + open
)
for bug in resp["data"]["allBugs"]["objects"]:
    print(bug["title"], bug["cvss"])
```

## 4. Write some data

Mutations go through `execute_mutation(mutation_name, **arguments)`. Unlike
queries, this returns the mutation's **payload directly** (no `["data"]`
wrapper).

```python
result = client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="Production Web App",
    type=1,                         # 1 = Web
    url="https://app.example.com",
    sensitivity=3,                  # High
    exposed=2,                      # Public
    tags=["production", "web"],
)
print("Created:", result)
```

## 5. Export everything (the easy way)

For large organizations, don't paginate by hand — kick off a server-side CSV
export and let the client poll until it's done:

```python
report = client.export_bugs_and_wait(ORG)      # or export_assets_and_wait(ORG)
print("Download URL:", report["file"])
```

See [Exporting Data](Exporting-Data) for the full story.

## Full script

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)
ORG = enums.ORGANIZATION_ID

# Read
resp = client.execute_query(
    "all_assets", organization_id=ORG, search_query="type = 1"
)
web_assets = resp["data"]["allAssets"]["objects"]
print(f"{len(web_assets)} web assets")

# Write
client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="API Gateway",
    type=1,
    url="https://api.example.com",
    sensitivity=4,
    exposed=2,
)

# Export
report = client.export_assets_and_wait(ORG, search_query="type = 1")
print("CSV:", report["file"])
```

## Where to go next

- **[Core Concepts](Core-Concepts)** — understand queries vs. mutations, response shapes, pagination, and error handling. Highly recommended before you build anything real.
- **[Search Query Language](Search-Query-Language)** — master the filter syntax.
- Topic guides: [Assets](Assets), [Findings](Findings), [Engagements](Engagements), [Comments](Comments), [Reports](Reports), [Exporting Data](Exporting-Data).
