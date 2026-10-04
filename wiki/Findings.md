# Findings

Findings (called **bugs** in the API) are the vulnerabilities on your assets.
This guide covers listing, searching, creating each type, updating state and
severity, and CSV-based bulk updates.

> **Example scripts:** `test-fetch-findings-example.py`,
> `test-create-findings-example.py`,
> `test-update-finding-state-severity-example.py`,
> `test-update-bugs-fields-csv-example.py`, `test-export-bugs-example.py`.

## Finding enums

| Field | Codes |
|---|---|
| `severity` | `1`=Info · `2`=Low · `3`=Medium · `4`=High · `5`=Critical |
| `state` | `1`=Open · `2`=Closed · `3`=In&nbsp;Progress · `4`=Resolved |
| `bug_level` | `1`=Code · `2`=Web · `3`=Mobile · `4`=Network · `5`=Cloud · `6`=Package |

## List findings

`all_bugs` is **cursor-paginated** (see [Core Concepts](Core-Concepts#pagination)).

```python
resp = client.execute_query("all_bugs", organization_id=ORG)
findings = resp["data"]["allBugs"]["objects"]

for f in findings[:5]:
    print(f"- {f['title']} (severity={f['severity']}, cvss={f['cvss']})")
```

### Arguments

| Argument | Type | Description |
|---|---|---|
| `organization_id` | UUID! | Required |
| `search_query` | String | RQL filter — see [Search Query Language](Search-Query-Language#finding-bug-fields) |
| `order_by` | [String] | Sort fields, prefix `-` for descending |
| `page_size` | Int | Objects per page (cursor) |
| `after` | String | Cursor for the next page |

### Search examples

```python
client.execute_query("all_bugs", organization_id=ORG, search_query="severity = 5")
client.execute_query("all_bugs", organization_id=ORG,
                     search_query="severity in (4,5) and state = 1 and bug_level = 2")
```

See [Search Query Language → Finding fields](Search-Query-Language#finding-bug-fields).

## Create a finding

Creation uses the `bug_create` mutation. The type-specific detail field
(`web` / `network` / `code`) is a **JSON string**.

### Web finding (bug_level 2)

```python
client.execute_mutation(
    "bug_create",
    organization_id=ORG,
    title="Reflected XSS in Search",
    description="Reflected XSS in the search box allows script injection.",
    bug_level=2,                        # 2 = Web
    severity=3,
    mitigation="Sanitize input and encode output.",
    steps_to_reproduce="1. Open /search  2. Enter payload  3. Observe execution",
    selected_assets=[123, 456],         # affected asset IDs
    cwe_list=[79],                      # optional
    cve_list=[],                        # optional
    cvss=6.1,                           # optional
    tags=["xss", "web"],                # optional
    web='{"affected_endpoints": ["https://example.com/search"], '
        '"request": "GET /search?q=<script>alert(1)</script>", '
        '"response": "HTTP/1.1 200 OK"}',
    custom_fields="{}",
)
```

### Network finding (bug_level 4)

```python
client.execute_mutation(
    "bug_create",
    organization_id=ORG,
    title="SSH (22) exposed to the internet",
    description="SSH is reachable from any source address.",
    bug_level=4,                        # 4 = Network
    severity=3,
    mitigation="Restrict SSH to a bastion / allow-list.",
    steps_to_reproduce="1. nmap target  2. confirm 22/tcp open externally",
    selected_assets=[789],
    cwe_list=[200],
    cvss=5.3,
    network='{"port": "22", "cpe": ["cpe:/a:openssh:openssh:8.2p1"]}',
)
```

### Code finding (bug_level 1)

```python
client.execute_mutation(
    "bug_create",
    organization_id=ORG,
    title="Command injection in upload handler",
    description="User-controlled filename is concatenated into a shell command.",
    bug_level=1,                        # 1 = Code
    severity=4,
    mitigation="Use subprocess with an argument list, never a shell string.",
    steps_to_reproduce="1. Intercept upload  2. Edit filename  3. Observe RCE",
    selected_assets=[101],
    cwe_list=[78],
    cvss=8.6,
    code='{"vulnerable_code": "os.system(\\"mv \\" + filename)", '
         '"start_line_number": "78", "end_line_number": "78", '
         '"file_name": "utils/upload_handler.py"}',
)
```

### Required vs. optional fields

**Required for every finding:** `title`, `description`, `organization_id`,
`bug_level`, `severity`, `mitigation`, `steps_to_reproduce`, `selected_assets`,
plus the type-specific JSON field.

**Type-specific JSON:**
- Web (2): `web` → `affected_endpoints`, `request`, `response`
- Network (4): `network` → `port`, `cpe`
- Code (1): `code` → `vulnerable_code`, `start_line_number`, `end_line_number`, `file_name`

**Optional (all):** `cwe_list`, `cve_list`, `cvss`, `tags`, `custom_fields`,
`bug_attachment_list`, `engagement_ids`.

## Update state and/or severity

Use the `bug_bulk_update` mutation. Despite the "bulk" name, you target findings
with an RQL `search_query`, so it works for one finding or many.

```python
# Update a single finding by id
result = client.execute_mutation(
    "bug_bulk_update",
    organization_id=ORG,
    search_query="id = 12345",
    state=4,            # Resolved; pass None to leave unchanged
    severity=5,         # Critical; pass None to leave unchanged
)
for bug in result["bugs"]:
    print(bug["id"], bug["state"], bug["severity"])
```

```python
# Update many findings at once
client.execute_mutation(
    "bug_bulk_update",
    organization_id=ORG,
    search_query="severity = 4 and state = 1",
    state=3,            # move all matching to In Progress
)
```

The mutation returns `{"bugs": [{"id", "state", "severity"}, ...]}`.

> **Example:** `test-update-finding-state-severity-example.py`

## Bulk-update custom fields from a CSV

To update finding custom fields in bulk from a spreadsheet, upload a CSV:

```python
client.update_bugs_fields_with_csv("findings-fields.csv", ORG)
```

See [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports#update-finding-fields-from-a-csv).

## Export all findings

```python
# Async CSV (recommended for large orgs)
report = client.export_bugs_and_wait(ORG, search_query="severity = 5")
print(report["file"])

# Or stream every page as Python objects
for page in client.export_all_bugs(ORG):
    for bug in page:
        ...
```

Details: [Exporting Data](Exporting-Data).

## Response fields

Each finding object includes (non-exhaustive):

**Core** — `id`, `title`, `description`, `hash`, `object_id`
**Risk** — `severity`, `state`, `bug_level`, `cvss`, `cvss_v3`, `cvss_v4`,
`attack_vector`, `prioritization_score`, `epss_score`, `sla_violated`,
`due_date`, `cisa_due_date`
**Remediation** — `mitigation`, `steps_to_reproduce`, `evidence`,
`exploit_available`, `exploit_info`, `patch_available`, `patch_info`
**Lifecycle** — `is_active`, `is_reopened`, `smart_close`, `vulnerable_since`,
`last_resolved_on`, `created`, `updated`
**AI/enrichment** — `ai_title`, `ai_description`, `ai_mitigation`,
`is_data_enriched`
**Data** — `fields` (custom fields), `links`, `metadata`,
`scanner_raw_response`, `port`, `connector`

For the authoritative, complete list see the
[GraphQL API Reference](GraphQL-API-Reference) and `BUG_FULL_FIELDS` in
[`client.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/client.py).

> **Note:** On the public API, `cwe` and `cve` come back as scalar data on the
> finding, not as nested objects. Filter on them with `cwe ~ "CWE-79"` /
> `cve ~ "CVE-2023-1234"`.

## Related

- [Search Query Language → Finding fields](Search-Query-Language#finding-bug-fields)
- [Comments](Comments) — discuss a finding
- [Exporting Data](Exporting-Data)
