# Search Query Language

Almost every list endpoint in this client accepts a `search_query` argument.
It's written in the **Strobes Query Language** (also called RQL) — the same
syntax the Strobes UI search bar uses. This page is your reference for the
operators, how to combine them, and which fields and codes you can filter on per
object.

> Omit `search_query` (or pass `None`) to match everything the token can see.

## Operators

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `severity = 5` |
| `!=` | Not equal to | `state != 2` |
| `>` | Greater than | `cvss > 7` |
| `>=` | Greater than or equal | `risk_score >= 80` |
| `<` | Less than | `cvss < 4` |
| `<=` | Less than or equal | `risk_score <= 30` |
| `~` | Contains (substring) | `title ~ "SQL"` |
| `!~` | Does not contain | `title !~ "test"` |
| `in` | In a list | `severity in (4, 5)` |
| `not in` | Not in a list | `type not in (2, 3)` |
| `^` | Regex match | `name ^ "prod-.*"` |

Combine conditions with **`and`** / **`or`**:

```text
severity in (4, 5) and state = 1 and bug_level = 2
cloud_type = 2 and region = "us-east-1"
created >= "2024-01-01" and created <= "2024-06-30"
```

Quote string values; leave numbers unquoted. Dates are ISO-8601 strings
(`"2024-01-01"`).

## Using it in code

```python
client.execute_query(
    "all_bugs",
    organization_id=ORG,
    search_query='severity = 5 and state = 1',
)
```

String interpolation is fine for dynamic values — just mind the quoting:

```python
finding_id = 12345
search_query = f"id = {finding_id}"                 # numeric: no quotes
name = "production"
search_query = f'name ~ "{name}"'                   # string: quotes
```

---

## Asset fields

Filter `all_assets` / `export_assets` on these.

### Enum codes

| Field | Codes |
|---|---|
| `type` | `1`=Web · `2`=Mobile · `3`=Network · `4`=Cloud · `7`=Code repo |
| `cloud_type` | `1`=Other · `2`=AWS · `3`=Azure · `4`=GCP |
| `sensitivity` | `1`=Low · `2`=Medium · `3`=High · `4`=Critical |
| `exposed` | `1`=Private · `2`=Public |

### Common patterns

```python
# By type
'type = 1'                  # web assets
'type in (1, 3, 4)'         # web, network, cloud

# By sensitivity / exposure
'sensitivity in (3, 4)'     # high + critical
'exposed = 2'               # public

# By risk score
'risk_score >= 80'
'risk_score > 50 and risk_score < 80'

# By name / target / host
'name ~ "production"'
'target ~ "api"'
'hostname ~ "server"'

# By network info
'ipaddress = "192.168.1.1"'
'ipaddress ~ "192.168.1"'
'os ~ "Linux"'

# By cloud
'cloud_type = 2 and region = "us-east-1"'
'account_id = "123456789012"'

# By date
'created >= "2024-01-01"'

# Combined
'type = 1 and risk_score >= 80 and exposed = 2'
'type = 4 and sensitivity >= 3 and exposed = 2'
```

Full field list: [Assets](Assets#response-fields). Official reference:
[StrobesQL — Assets](https://github.com/strobes-co/ql-documentation?tab=readme-ov-file#assets).

---

## Finding (bug) fields

Filter `all_bugs` / `export_bugs` on these.

### Enum codes

| Field | Codes |
|---|---|
| `severity` | `1`=Info · `2`=Low · `3`=Medium · `4`=High · `5`=Critical |
| `state` | `1`=Open · `2`=Closed · `3`=In&nbsp;Progress · `4`=Resolved |
| `bug_level` | `1`=Code · `2`=Web · `3`=Mobile · `4`=Network · `5`=Cloud · `6`=Package |

### Common patterns

```python
# By severity
'severity = 5'              # critical
'severity in (4, 5)'        # high + critical
'severity >= 3'

# By state
'state = 1'                 # open
'state in (1, 3)'           # open + in-progress
'state != 2'                # everything except closed

# By level
'bug_level = 2'             # web findings
'bug_level in (1, 2)'       # code + web

# By CVSS
'cvss >= 9.0'
'cvss >= 7.0 and cvss < 9.0'

# By text
'title ~ "SQL"'
'description ~ "authentication"'

# By CVE / CWE
'cve ~ "CVE-2023"'
'cwe ~ "CWE-79"'            # XSS
'cwe ~ "CWE-89"'            # SQL injection

# By exploit / patch
'exploit_available = true'
'exploit_available = true and patch_available = false'

# By related asset
'asset.name ~ "production"'
'asset.type = 1'
'asset.exposed = 2 and severity >= 4'

# Combined
'severity in (4, 5) and state = 1 and bug_level = 2'
'cvss >= 8.0 and exploit_available = true'
'created >= "2024-01-01" and state = 1 and cvss >= 7.0'
```

Full field list: [Findings](Findings#response-fields). Official reference:
[StrobesQL — Bugs](https://github.com/strobes-co/ql-documentation?tab=readme-ov-file#bugs).

---

## Engagement fields

Filter `all_engagements` on these.

```python
'name ~ "pentest"'
'state = 1'
'scheduled_date >= "2025-01-01"'
```

See [Engagements](Engagements) and the official
[StrobesQL — Engagements](https://github.com/strobes-co/ql-documentation)
section.

---

## Comment fields

Filter `all_comments` on these (in addition to the structured `bug_id` /
`engagement_id` / `internal` arguments — see [Comments](Comments)).

```python
'comment ~ "credentials"'
```

---

## Other objects

- **Vault documents** (`all_vault_attachments`): `document_name ~ "test"`
- **Report templates** (`all_templates`): `template_name ~ "Executive"`
- **Connector configurations** (`all_configurations`) and **scan logs**
  (`all_logs`) accept `search_query` too.

---

## Full language reference

For the complete grammar, every available field, and advanced constructs, see
the official **[Strobes QL Documentation](https://github.com/strobes-co/ql-documentation)**.
