# Engagements

An engagement is a security assessment — a scoped piece of work (a pentest, a
scan campaign) against a set of assets, with a schedule, services, and
prerequisites. This guide covers listing, searching, creating, and updating
engagement state.

> **Example scripts:** `test-fetchengagement-example.py`,
> `test-createengagement-example.py`,
> `test-create-engagement-custom-fields-example.py`,
> `test-update-engagement-state-example.py`,
> plus `execute_create_engagement_with_multiple_services` in `example.py`.

## List engagements

`all_engagements` is **offset-paginated** (see [Core Concepts](Core-Concepts#pagination)).

```python
resp = client.execute_query("all_engagements", organization_id=ORG)
engagements = resp["data"]["allEngagements"]["objects"]

for e in engagements[:5]:
    print(f"- {e['name']} (id={e['id']}, state={e['state']})")
```

### Search

```python
client.execute_query(
    "all_engagements",
    organization_id=ORG,
    search_query='name ~ "pentest"',
)
```

### Arguments

| Argument | Type | Description |
|---|---|---|
| `organization_id` | UUID! | Required |
| `search_query` | String | RQL filter |
| `order_by` | [String] | Sort fields |
| `asset_id` | Int | Only engagements covering this asset |
| `page` / `page_size` | Int | Offset pagination |

## Create an engagement

Uses the `create_engagement` mutation. The two fiddly arguments are
`assessment_data` and `prerequisites_data`, both **JSON strings**.

```python
import json

engagement = {
    "organization_id": ORG,
    "name": "Q3 2025 Security Assessment",
    "scheduled_date": "2025-08-06",
    "delivery_date": "2025-08-22",
    "subscribed_services": ["service 1"],
    "plans": 1,
    "state": 1,                              # 1 = active
    "is_self_managed": True,
    "include_related_assets": False,
    "vendor_code": "",
    "document_ids": [],
    "fields": "{}",                          # custom fields (JSON string)

    # Which assets each service covers:
    "assessment_data": json.dumps({
        "service 1": [
            {"search_query": "id in (38069,38070)"},
            {
                "asset_id": "38069", "asset_type": 1,
                "scheduled_date": "2025-08-06", "delivery_date": "2025-08-22",
                "vpn_accounts": "", "test_accounts": "",
                "instructions": "", "scope": "",
            },
            {
                "asset_id": "38070", "asset_type": 1,
                "scheduled_date": "2025-08-06", "delivery_date": "2025-08-22",
                "vpn_accounts": "", "test_accounts": "",
                "instructions": "", "scope": "",
            },
        ]
    }),

    # Pre-engagement tasks:
    "prerequisites_data": json.dumps([
        {
            "id": None,
            "title": "Provide VPN access",
            "description": "Share VPN credentials with the testing team.",
            "assigned_to": "security_team",
            "due_date": "2025-08-04",
            "attachments": [],
            "order_index": 1,
            "is_completed": True,
        }
    ]),
}

result = client.execute_mutation("create_engagement", **engagement)
print("Engagement created:", result)
```

### Required vs. optional fields

**Required:** `organization_id`, `name`, `scheduled_date`, `delivery_date`,
`subscribed_services`, `plans`, `assessment_data`, `state`.

**Optional:** `fields` (custom fields), `document_ids`, `prerequisites_data`,
`vendor_code`, `is_self_managed`, `include_related_assets`, `credential_ids`,
`executive_summary`, `custom_status`.

### Custom fields

As with assets, create the custom field in the UI first
(**Settings → Custom Fields → Engagement Custom Fields**) and reference it by
**slug**. Pass values as a JSON string in `fields`:

```python
"fields": json.dumps({"notes": "High-priority client", "custom_text": "ACME-42"})
```

> **Example:** `test-create-engagement-custom-fields-example.py`

## Update engagement state

`create_engagement` sets the state once at creation. To change it afterwards,
use one of two mutations.

### Single engagement — `update_engagement`

```python
result = client.execute_mutation(
    "update_engagement",
    organization_id=ORG,
    engagement_id="0c5c2d61-4a3a-4a58-9b4b-4a1b9f0f2f11",
    state=2,
)
print(result["engagement"]["state"])
```

### Many engagements — `bulk_update_engagements`

```python
result = client.execute_mutation(
    "bulk_update_engagements",
    organization_id=ORG,
    engagement_ids=[
        "0c5c2d61-4a3a-4a58-9b4b-4a1b9f0f2f11",
        "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    ],
    state=2,
)
for e in result["engagements"]:
    print(e["id"], e["state"])
```

> **State values vary by organization.** Check which numeric state values your
> org uses (via the UI or by reading `state` / `custom_status` on an existing
> engagement) before setting them. You can look up current states first with
> `all_engagements`.

> **Example:** `test-update-engagement-state-example.py`

## Response fields

Each engagement object includes (non-exhaustive):

**Core** — `id`, `engagement_custom_id`, `name`, `state`, `state_id`,
`parent_state`, `custom_status`
**Schedule** — `scheduled_date`, `delivery_date`, `created`, `updated`
**Scope / services** — `subscribed_services`, `plans`, `is_self_managed_engagement`,
`is_agentic_assessment`
**Metrics** — `security_posture`, `credits`, `credits_estimated`,
`assessments_count`, `engagement_completion`, `assessments_per_service`,
`total_hours_spent`, `prerequisites_completion`
**Other** — `executive_summary`, `fields` (custom fields),
`checked_terms_and_conditions`, `is_active`

For the complete list see the [GraphQL API Reference](GraphQL-API-Reference) and
`ENGAGEMENT_FULL_FIELDS` in
[`client.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/client.py).

## Related

- [Comments](Comments) — post engagement comments
- [Vault Documents](Vault-Documents) — attach documents to engagements
- [Reports](Reports)
