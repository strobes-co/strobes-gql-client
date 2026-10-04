# Strobes GraphQL Client

A small, batteries-included Python wrapper around the **Strobes public GraphQL API**.

It hides the GraphQL plumbing (query building, field selection, pagination,
retries, file uploads) behind simple Python methods, so you can read and manage
your **assets**, **findings**, **engagements**, **comments**, **reports**, and
**exports** in a few lines of code.

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

resp = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
assets = resp["data"]["allAssets"]["objects"]
print(f"{len(assets)} assets")
```

---

## Installation

```bash
git clone https://github.com/strobes-co/strobes-gql-client.git
cd strobes-gql-client

python3 -m venv venv && source venv/bin/activate   # recommended
pip install -r requirements.txt
python setup.py install
```

Working on the client itself? Install it in editable mode so your edits take
effect immediately:

```bash
pip install -e .
```

Requires **Python 3.6+**. See **[Installation](../../wiki/Installation)** for
platform notes and troubleshooting.

## Configuration

You need three things from your Strobes platform:

| Value | Where to find it |
|---|---|
| **Host** | Your Strobes domain, e.g. `mycorp.strobes.co` |
| **API Token** | Settings → API Access → *Generate Token* |
| **Organization ID** | Shown on the same API Access page (a UUID) |

Provide them either via environment variables:

```bash
export STROBES_API_TOKEN="<your-api-token>"
export STROBES_ORGANIZATION_ID="<your-org-uuid>"
```

…or by editing `strobes_gql_client/enums.py`. Full walkthrough (with
screenshots and a video) in **[Configuration & Authentication](../../wiki/Configuration-and-Authentication)**.

## Quick example

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch the critical, still-open findings
resp = client.execute_query(
    "all_bugs",
    organization_id=enums.ORGANIZATION_ID,
    search_query="severity = 5 and state = 1",
)
for bug in resp["data"]["allBugs"]["objects"]:
    print(bug["title"], bug["cvss"])
```

## What you can do

| Area | Read | Write |
|---|---|---|
| **Assets** | list, search, get one, export all | create, bulk-update custom fields |
| **Findings** (bugs) | list, search, export all | create, bulk-update state/severity, update via CSV |
| **Engagements** | list, search | create, update state (single & bulk) |
| **Comments** | list (on a finding or engagement) | add to a finding, add to an engagement |
| **Vault documents** | list, search | upload |
| **Reports** | list/preview templates, download | create template, generate report, attach files |
| **Connectors** | list configurations, list scan logs | — |
| **Workspaces / Sheets** | — | upload file, import CSV |

## Documentation (Wiki)

The full, user-friendly documentation lives in the **[Wiki](../../wiki)**:

- **[Home](../../wiki)** — start here
- **[Installation](../../wiki/Installation)**
- **[Configuration & Authentication](../../wiki/Configuration-and-Authentication)**
- **[Quickstart](../../wiki/Quickstart)**
- **[Core Concepts](../../wiki/Core-Concepts)** — client, queries vs. mutations, responses, pagination, errors
- **[Search Query Language](../../wiki/Search-Query-Language)** — filter syntax & field reference
- **[Assets](../../wiki/Assets)** · **[Findings](../../wiki/Findings)** · **[Engagements](../../wiki/Engagements)**
- **[Comments](../../wiki/Comments)** · **[Vault Documents](../../wiki/Vault-Documents)** · **[Reports](../../wiki/Reports)**
- **[Exporting Data](../../wiki/Exporting-Data)** — async CSV exports
- **[Connectors & Scan Logs](../../wiki/Connectors-and-Scan-Logs)**
- **[File Uploads & CSV Imports](../../wiki/File-Uploads-and-CSV-Imports)**
- **[Python API Reference](../../wiki/Python-API-Reference)** — every client method
- **[GraphQL API Reference](../../wiki/GraphQL-API-Reference)** — public queries & mutations
- **[Troubleshooting](../../wiki/Troubleshooting)**

> The Markdown sources for these pages are also in the [`wiki/`](wiki/) folder
> of this repo.

## Runnable examples

The [`examples/`](examples/) directory has a self-contained script for every
feature (fetch/create assets, findings, engagements, comments, vault uploads,
reports, exports, CSV imports). Set your credentials and run any of them:

```bash
export STROBES_API_TOKEN="<token>"
export STROBES_ORGANIZATION_ID="<org-id>"
python examples/test-fetchassets-example.py
```

Run them all at once with `python test.py`.

## License

GPLv3. See [`setup.py`](setup.py).
