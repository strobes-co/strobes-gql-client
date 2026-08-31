"""
Async bug export: kick off a background CSV export of every bug in an org
(or every bug matching a search query), poll until it finishes, and
download the result — all via the public API token (no JWT needed).

This is the recommended way to pull "everything" out of a large org instead
of paginating `allBugs` yourself: the export runs as a background job on
the server, so nothing about it can hit a gateway timeout the way a large
synchronous `allBugs` batch can.

Edit the variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-export-bugs-example.py [--out bugs-export.csv]

Covers:
    Mutation exportBugs(organizationId, searchQuery)
    Query    downloadReport(organizationId, exportId)
"""

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID

# =============================================================================
# EDIT THIS
# =============================================================================

# Restrict the export to bugs matching this RQL query. Leave as None to
# export every bug the token can see.
SEARCH_QUERY = None

# =============================================================================


def get_client():
    return StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)


def export_via_manual_poll(client, org_id):
    """Equivalent to export_bugs_and_wait, spelled out step by step —
    useful if you want your own polling cadence/backoff instead of the
    built-in one, or want to show a progress indicator between polls."""
    export = client.export_bugs(org_id, search_query=SEARCH_QUERY)
    export_id = export["exportId"]
    print(f"Export started: exportId={export_id} status={export['status']}")

    import time

    while True:
        response = client.execute_query(
            "download_report", organization_id=org_id, export_id=export_id
        )
        report = (response.get("data") or {}).get("downloadReport") if response else None
        if not report:
            raise RuntimeError(f"downloadReport returned no data for {export_id}")

        status = report["status"]
        print(f"  polling... status={status}")
        if status == "2":
            return report
        if status == "3":
            raise RuntimeError(f"Export {export_id} failed.")
        time.sleep(3)


def download_file(url, output_path):
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)
    print(f"Wrote {len(resp.content)} bytes to {output_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="bugs-export.csv")
    parser.add_argument(
        "--manual-poll",
        action="store_true",
        help="Poll step by step instead of using export_bugs_and_wait.",
    )
    args = parser.parse_args()

    if not API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        sys.exit(1)
    if not ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        sys.exit(1)

    client = get_client()

    if args.manual_poll:
        print("=== Exporting bugs (manual poll loop) ===")
        report = export_via_manual_poll(client, ORGANIZATION_ID)
    else:
        print("=== Exporting bugs (export_bugs_and_wait) ===")
        report = client.export_bugs_and_wait(
            ORGANIZATION_ID, search_query=SEARCH_QUERY
        )

    print(f"\nExport finished: {report}")
    if report.get("file"):
        download_file(report["file"], args.out)
    else:
        print("No file on the finished report — nothing to download.")


if __name__ == "__main__":
    main()
