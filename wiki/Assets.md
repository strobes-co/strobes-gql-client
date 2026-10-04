# Assets

Assets are the things you secure — web apps, mobile apps, network hosts, cloud
resources, and code repositories. This guide covers listing, searching,
fetching one, creating each type, working with custom fields, and bulk updates.

> **Example scripts:** `test-fetchassets-example.py`,
> `test-create-assets-example.py`,
> `test-create-asset-custom-fields-example.py`,
> `test-update-asset-custom-fields-example.py`,
> `test-export-assets-example.py`, `dump-assets-example.py`.

## Asset type codes

| `type` | Asset | Required extra field |
|---|---|---|
| `1` | Web | `url` |
| `2` | Mobile | `package` |
| `3` | Network | `ipaddress` or `ipaddress_list` |
| `4` | Cloud | `cloud_type` (`1`=Other, `2`=AWS, `3`=Azure, `4`=GCP) |
| `7` | Code repository | `url` |

Other shared enums: `sensitivity` (`1`=Low → `4`=Critical), `exposed`
(`1`=Private, `2`=Public).

## List assets

`all_assets` is **cursor-paginated** (see [Core Concepts](Core-Concepts#pagination)).

```python
resp = client.execute_query("all_assets", organization_id=ORG)
assets = resp["data"]["allAssets"]["objects"]

for a in assets[:5]:
    print(f"- {a['name']} (type={a['type']}, risk={a['risk_score']})")
```

### Arguments

| Argument | Type | Description |
|---|---|---|
| `organization_id` | UUID! | Required |
| `search_query` | String | RQL filter — see [Search Query Language](Search-Query-Language#asset-fields) |
| `order_by` | [String] | Sort fields, prefix `-` for descending |
| `page_size` | Int | Objects per page (cursor) |
| `after` | String | Cursor for the next page (`lastCursor` from the previous page) |

### Search examples

```python
client.execute_query("all_assets", organization_id=ORG, search_query="type = 1")
client.execute_query("all_assets", organization_id=ORG,
                     search_query="type = 4 and sensitivity >= 3 and exposed = 2")
```

See [Search Query Language → Asset fields](Search-Query-Language#asset-fields)
for the full pattern library.

## Fetch a single asset

```python
resp = client.execute_query("asset", id=12345)
asset = resp["data"]["asset"]
```

This returns the full asset metadata plus every connector that reported it
(`connector` and `other_connectors`).

## Create an asset

Creation uses the `create_asset` mutation. The required fields depend on the
asset type.

### Web (type 1)

```python
client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="Production Web App",
    type=1,
    url="https://app.example.com",
    sensitivity=3,
    exposed=2,
    tags=["production", "web", "critical"],   # optional
)
```

### Network (type 3)

```python
client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="Production Server",
    type=3,
    ipaddress="192.168.1.100",                # or ipaddress_list=[...]
    sensitivity=4,
    exposed=1,
    hostname="prod-server-01",                # optional
    os="Ubuntu 20.04",                        # optional
    tags=["server", "production"],
)
```

### Cloud (type 4)

```python
client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="AWS EC2 Instance",
    type=4,
    cloud_type=2,                             # 2 = AWS
    sensitivity=3,
    exposed=2,
    region="us-east-1",                       # optional
    account_id="123456789012",                # optional
    resource_id="i-0123456789abcdef0",        # optional
    tags=["aws", "ec2"],
)
```

### Mobile (type 2)

```python
client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="Mobile Banking App",
    type=2,
    package="com.company.banking",
    sensitivity=4,
    exposed=2,
    tags=["mobile", "ios", "android"],
)
```

### Required vs. optional fields

**Required for every type:** `name`, `organization_id`, `type`, `sensitivity`,
`exposed`, plus the type-specific field from the table above.

**Optional (all types):** `tags`, `custom_fields`.
**Optional (network):** `hostname`, `os`, `mac_address`, `cpe`.
**Optional (cloud):** `region`, `account_id`, `resource_id`.

## Custom fields on an asset

Custom fields let you attach your own metadata (e.g. `developer`, `priority`).

> ⚠️ **Create the custom field in the UI first.** Go to **Settings → Custom
> Fields → Asset Custom Fields**, create the field, and note its **slug**
> (lowercase, underscores). The slug — not the display name — is the key you
> use in code. For dropdown fields, use the exact lowercase option value.

### At creation time

Pass `custom_fields` as a JSON string keyed by slug:

```python
import json

client.execute_mutation(
    "create_asset",
    organization_id=ORG,
    name="My Web Application",
    type=1,
    url="https://app.example.com",
    sensitivity=3,
    exposed=2,
    custom_fields=json.dumps({"developer": "jane", "priority": "p1"}),
)
```

### Updating custom fields on existing assets

Use the dedicated `bulk_update_asset_custom_fields` method. It sets custom-field
values on **every asset matching an RQL query** in one call.

```python
result = client.bulk_update_asset_custom_fields(
    organization_id=ORG,
    search_query='type = 1 and name ~ "prod"',       # must be non-empty
    fields={"last_hotfix_release": "2026-09-18", "hotfix_released_by": "jane"},
)
updated = result["asset"]      # list of {id, name, type, fields}
```

Notes:
- `search_query` **must be non-empty** — an empty query would otherwise match
  every asset in the org. The method raises `ValueError` if it's blank.
- `fields` maps slug → value; unknown slugs are ignored, values are validated
  server-side.
- Up to **100** matching assets are updated inline and returned. Above that, the
  backend queues a background task and `asset` comes back as an empty list.

> **Example:** `test-update-asset-custom-fields-example.py`

## Export all assets

For bulk extraction, don't paginate by hand — use the async CSV export or the
streaming generator. Each asset row includes full metadata plus every source
(connector) that contributed to it.

```python
# Async CSV (recommended for large orgs)
report = client.export_assets_and_wait(ORG, search_query="type = 1")
print(report["file"])          # signed download URL

# Or stream every page as Python objects
for page in client.export_all_assets(ORG):
    for asset in page:
        ...
```

Details and tuning: [Exporting Data](Exporting-Data).

## Response fields

Each asset object includes (non-exhaustive):

**Identifiers** — `id`, `name`, `target`, `temp_id`
**Classification** — `type`, `cloud_type`, `sensitivity`, `exposed`
**Risk** — `risk_score`, `disabled`
**Network** — `ipaddress`, `hostname`, `mac_address`, `os`, `cpe`, `location`,
`port_addresses`
**Cloud / domain** — `region`, `account_id`, `resource_id`, `asn`, `waf`, `cdn`,
`dns_info`, `whois_info`, and the `domain_*` fields
**Data** — `data`, `additional_info`, `fields` (custom fields),
`scanner_raw_response`, `technology_used`, `webserver`, `package_count`
**Timestamps** — `created`, `updated`
**Sources** — `connector`, `other_connectors`, `last_seen`

For the authoritative, complete field list see the
[GraphQL API Reference](GraphQL-API-Reference) and the exact selection in
[`client.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/client.py)
(`ASSET_FULL_FIELDS`).

## Related

- [Search Query Language → Asset fields](Search-Query-Language#asset-fields)
- [Exporting Data](Exporting-Data)
- [Findings](Findings) — vulnerabilities attached to assets
