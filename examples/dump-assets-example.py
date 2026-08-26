"""
Dump every asset in an organization to a local JSON file.

Pages through allAssets (cursor pagination via `after`/`hasNext`) and writes
the full list of asset objects (including lastSeen, connector, and
otherConnectors, per _select_asset in client.py) to disk.

Usage:
    python examples/dump-assets-example.py [-o assets.json] [-q 'type = 1'] [-p 200]

Covers:
    Query allAssets(organizationId, searchQuery, pageSize, after)
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID


def get_client():
    return StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)


def fetch_all_assets(client, organization_id, search_query=None, page_size=100):
    """Page through allAssets via cursor pagination, returning every asset."""
    assets = []
    after = None

    while True:
        response = client.execute_query(
            "all_assets",
            organization_id=organization_id,
            search_query=search_query,
            page_size=page_size,
            after=after,
        )
        payload = (response or {}).get("data", {}).get("allAssets") or {}
        objects = payload.get("objects", [])
        assets.extend(objects)
        print(f"  fetched {len(objects)} assets (total so far: {len(assets)})")

        if not payload.get("hasNext") or not objects:
            break
        after = payload.get("lastCursor")
        if not after:
            break

    return assets


def dump_assets(output_path, search_query=None, page_size=100):
    print("=== Dumping All Assets ===")
    client = get_client()
    assets = fetch_all_assets(
        client, ORGANIZATION_ID, search_query=search_query, page_size=page_size
    )

    with open(output_path, "w") as f:
        json.dump(assets, f, indent=2, default=str)

    print(f"\nWrote {len(assets)} assets to {output_path}")
    return assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o", "--output", default="assets.json", help="Output JSON file path"
    )
    parser.add_argument(
        "-q", "--search-query", default=None, help="Optional RQL search query filter"
    )
    parser.add_argument(
        "-p", "--page-size", type=int, default=100, help="Assets per page"
    )
    args = parser.parse_args()

    dump_assets(args.output, search_query=args.search_query, page_size=args.page_size)


if __name__ == "__main__":
    main()
