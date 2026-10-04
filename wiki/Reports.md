# Reports

The reporting API lets you manage HTML **templates**, preview a report, generate
a PDF, attach files, and download the finished file — all with a public API
token (no JWT needed).

> **Example scripts:** `test-reports-example.py`,
> `test-add-report-attachment-example.py`

## The report lifecycle

1. **Create or find a template** (`add_report_template` / `all_templates`).
2. **Preview** the rendered HTML (`preview_report`) — optional sanity check.
3. **Generate** the report (`generate_report`) — runs asynchronously on the server.
4. **Download** the finished file (`download_report`).

## 1. Templates

### Create a template

```python
template = client.execute_mutation(
    "add_report_template",
    organization_id=ORG,
    template_name="Executive Summary",
    html_data="<h1>{{ report_name }}</h1><p>Generated via strobes-gql-client.</p>",
    mode=0,          # 0 = portrait, 1 = landscape
    type=2,          # 2 = findings report
)
print(template["templates"]["id"])
```

### List / find templates

`all_templates` is offset-paginated.

```python
resp = client.execute_query(
    "all_templates",
    organization_id=ORG,
    search_query='template_name ~ "Executive"',
    page_size=1,
)
templates = resp["data"]["allTemplates"]["objects"]
```

A common pattern is "reuse if it exists, else create":

```python
def find_or_create_template(client, org, name, html, mode=0, type=2):
    resp = client.execute_query(
        "all_templates", organization_id=org,
        search_query=f'template_name ~ "{name}"', page_size=1,
    )
    objs = resp.get("data", {}).get("allTemplates", {}).get("objects", [])
    if objs:
        return objs[0]
    created = client.execute_mutation(
        "add_report_template", organization_id=org,
        template_name=name, html_data=html, mode=mode, type=type,
    )
    return created["templates"]
```

### Template fields

`TemplateType` returns `id`, `template_name`, `mode`, `type`, `is_active`,
`is_editable`, `created`, `updated`, `custom_fields`, `html`, and `created_by`
(`id`, `email`, `first_name`, `last_name`).

## 2. Preview a report

Renders the template against live data and returns the HTML as a string —
without generating a file:

```python
resp = client.execute_query(
    "preview_report",
    organization_id=ORG,
    template_id=int(template_id),
    report_name="Monthly Findings",
    search_query=None,                 # or an RQL filter to scope the findings
)
html = resp["data"]["previewReport"]
print(html[:500])
```

## 3. Generate a report

```python
result = client.execute_mutation(
    "generate_report",
    organization_id=ORG,
    template_id=int(template_id),
    report_name="Monthly Findings",
    search_query=None,                 # RQL filter, or None for everything
)
print(result["reports"])
if result["password_required"]:
    print("This org requires a report password — pass password=... too.")
```

Generation is **asynchronous** — the server builds the file in the background.
Once it finishes, fetch it by its export id (visible in the UI, or by polling
`all_bug_reports` internally):

```python
resp = client.execute_query(
    "download_report", organization_id=ORG, export_id="<exportId>"
)
report = resp["data"]["downloadReport"]
print(report["file"])       # signed download URL once status == "2"
```

### `download_report` / `ReportType` fields

| Field | Description |
|---|---|
| `id` | Report identifier |
| `report_name` | Generated report name |
| `status` | Raw status code: `"0"`=Pending · `"1"`=In-Progress · `"2"`=Finished · `"3"`=Failed |
| `created` | When generation started |
| `export_id` | The id used to poll `download_report` |
| `file` | Signed download URL (present once `status == "2"`) |
| `has_password` | Whether the file is password protected |
| `template` | `id`, `template_name` |

> `download_report` briefly returns an *"Invalid export details."* error in the
> split second between an export starting and the backend creating the report
> row. The client treats that as "not ready yet" and logs it at DEBUG — see
> [Exporting Data](Exporting-Data), which automates this polling for CSV exports.

## 4. Report attachments

Attach a file (e.g. an appendix or evidence bundle) to a report:

```python
result = client.add_report_attachment("appendix.pdf", ORG)
print(result["attachment"]["url"])
```

Returns the attachment's `id`, `attachment`, `attachment_name`, `created`,
`updated`, `url`, and `attached_by` (`id`, `email`, `first_name`, `last_name`).

> **Example:** `test-add-report-attachment-example.py`

## Related

- [Exporting Data](Exporting-Data) — fully-automated async CSV exports of bugs/assets
- [Search Query Language](Search-Query-Language) — scope reports to specific findings
- [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports)
