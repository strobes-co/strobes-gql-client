"""
Async asset metadata export: kick off a background CSV export of every
asset in an org (or every asset matching a search query), poll until it
finishes, and download the result — all via the public API token (no JWT
needed).

Each row in the CSV covers the asset's full metadata
(scanner_raw_response, dns_info, whois_info, custom fields) plus every
source (connector) that contributed to it (columns "Imported Using" for the
primary source, "Other Sources" for every additional one). Note: the
underlying platform merges/overwrites metadata in place when multiple
sources report the same asset, so a field's value can't be attributed to
one specific source — only which sources contributed is tracked. This is
the most complete "metadata from each source" view currently available.

Edit the variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-export-assets-example.py [--out assets-export.csv]

Covers:
    Mutation exportAssets(organizationId, searchQuery)
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

# Restrict the export to assets matching this RQL query. Leave as None to
# export every asset the token can see.
SEARCH_QUERY = None

# =============================================================================


def get_client():
    return StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)


def download_file(url, output_path):
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)
    print(f"Wrote {len(resp.content)} bytes to {output_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="assets-export.csv")
    args = parser.parse_args()

    if not API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        sys.exit(1)
    if not ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        sys.exit(1)

    client = get_client()

    print("=== Exporting asset metadata (export_assets_and_wait) ===")
    report = client.export_assets_and_wait(ORGANIZATION_ID, search_query=SEARCH_QUERY)

    print(f"\nExport finished: {report}")
    if report.get("file"):
        download_file(report["file"], args.out)
    else:
        print("No file on the finished report — nothing to download.")


if __name__ == "__main__":
    main()
