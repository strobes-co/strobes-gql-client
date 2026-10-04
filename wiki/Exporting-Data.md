# Exporting Data

When you need **everything** out of an organization — every bug or every asset —
paginating `allBugs` / `allAssets` by hand is fragile: a large synchronous batch
can hit the API gateway's timeout. The client gives you two robust alternatives:

1. **Async CSV export** — the server builds a CSV in the background; you poll
   until it's done, then download. *Recommended for large orgs.*
2. **Streaming generators** — page through everything as Python objects, with
   automatic retries and adaptive batch sizing.

> **Example scripts:** `test-export-bugs-example.py`,
> `test-export-assets-example.py`, `dump-assets-example.py`

---

## Option 1: Async CSV export (recommended)

Three steps: start the export, poll until finished, download the file. The
`_and_wait` helpers do the polling and give you a finished report with a `file`
URL.

### Export bugs

```python
report = client.export_bugs_and_wait(
    ORG,
    search_query=None,       # or an RQL filter, e.g. 'severity = 5'
    poll_interval=3.0,       # seconds between status polls
    timeout=1800,            # give up after 30 minutes
)
print(report["file"])        # signed URL to the finished CSV
```

### Export assets

```python
report = client.export_assets_and_wait(ORG, search_query="type = 1")
print(report["file"])
```

### Download the file

```python
import requests

resp = requests.get(report["file"], timeout=60)
resp.raise_for_status()
with open("export.csv", "wb") as f:
    f.write(resp.content)
```

### Run the example scripts

```bash
export STROBES_API_TOKEN="<token>"
export STROBES_ORGANIZATION_ID="<org-id>"

python examples/test-export-bugs-example.py   --out bugs-export.csv
python examples/test-export-assets-example.py --out assets-export.csv
```

Edit the `SEARCH_QUERY` variable near the top of each script to scope the
export, or leave it `None` to export everything the token can see.

### Driving the poll loop yourself

If you want your own cadence or a progress indicator, call the non-waiting
`export_bugs` / `export_assets` (which return immediately with an `exportId`)
and poll `download_report` yourself:

```python
import time

export = client.export_bugs(ORG, search_query=None)
export_id = export["exportId"]
print(f"Started: exportId={export_id} status={export['status']}")

while True:
    resp = client.execute_query(
        "download_report", organization_id=ORG, export_id=export_id
    )
    report = resp["data"]["downloadReport"]
    print("  status =", report["status"])
    if report["status"] == "2":       # Finished
        break
    if report["status"] == "3":       # Failed
        raise RuntimeError(f"Export {export_id} failed.")
    time.sleep(3)
```

(The example scripts expose this path via a `--manual-poll` flag.)

### Status codes

| `status` | Meaning |
|---|---|
| `"0"` | Pending |
| `"1"` | In-Progress |
| `"2"` | Finished (`file` URL now present) |
| `"3"` | Failed |

### Arguments

| Argument | Applies to | Description |
|---|---|---|
| `organization_id` | all | Required |
| `search_query` | all | RQL filter; omit/`None` to export everything |
| `poll_interval` | `_and_wait` | Seconds between polls (default `3.0`) |
| `timeout` | `_and_wait` | Seconds before raising `TimeoutError` (default `1800`) |

### What's in the asset CSV

Each asset row carries the asset's full metadata (`scanner_raw_response`,
`dns_info`, `whois_info`, custom fields) plus every **source (connector)** that
contributed to it — the primary source in the "Imported Using" column and each
additional one in "Other Sources".

> The platform merges/overwrites metadata in place when multiple sources report
> the same asset, so a specific field's value can't be attributed to one
> specific source — only *which* sources contributed is tracked. This is the
> most complete "metadata from each source" view currently available.

---

## Option 2: Streaming generators

If you'd rather work with Python objects than a CSV, `export_all_bugs` and
`export_all_assets` page through everything for you and **yield one list of
objects per page**:

```python
total = 0
for page in client.export_all_bugs(ORG, search_query="severity in (4,5)"):
    for bug in page:
        total += 1
print(total, "findings")

for page in client.export_all_assets(ORG):
    for asset in page:
        ...                 # includes connector + other_connectors metadata
```

These are the right tool for "pull everything and process it in code" — they
handle the batch-size-vs-timeout tradeoff automatically:

- Transient failures (gateway timeouts, 5xx) are **retried with exponential
  backoff**.
- A batch that keeps timing out is **progressively halved** (down to
  `min_page_size`) instead of failing the whole export…
- …then **grows back toward `page_size`** once a run of pages succeeds cleanly.

### Tuning parameters

| Argument | Default | Description |
|---|---|---|
| `page_size` | `200` | Starting objects per page |
| `min_page_size` | `25` | Floor the adaptive shrink won't go below |
| `max_retries` | `5` | Retries at a given size before shrinking |
| `initial_backoff` | `2.0` | First backoff in seconds |
| `max_backoff` | `30.0` | Backoff ceiling in seconds |

```python
for page in client.export_all_assets(ORG, page_size=100, min_page_size=10):
    ...
```

---

## Which should I use?

| Situation | Use |
|---|---|
| You want a CSV file (for a spreadsheet, a data warehouse, a share) | `export_bugs_and_wait` / `export_assets_and_wait` |
| Very large org; avoid any client-side timeout risk | Async CSV export |
| You want to process records in Python as you go | `export_all_bugs` / `export_all_assets` |
| You need fine-grained control of the poll loop | `export_bugs` + `download_report` |

## Related

- [Findings](Findings) · [Assets](Assets)
- [Reports](Reports) — PDF reports (different from CSV exports)
- [Core Concepts → Pagination](Core-Concepts#pagination)
