"""Connector configurations + scan logs: list an org's connector
configurations and their scan history via the public API token.

Edit ORGANIZATION_ID below (or export STROBES_ORGANIZATION_ID), then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-configurations-scanlogs-example.py

Covers:
    Query allConfigurations(organizationId, orderBy, searchQuery, page, pageSize)
    Query allLogs(organizationId, searchQuery, orderBy, page, pageSize)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID


def get_client():
    return StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)


def list_configurations(client, org_id):
    payload = client.all_configurations(org_id, page=1, page_size=10) or {}
    objects = payload.get("objects", [])
    print(f"Found {payload.get('totalCount', 0)} configuration(s), showing {len(objects)}:")
    for config in objects:
        connector = (config.get("connector") or {}).get("name")
        print(f"  [{config['id']}] {config['name']} — connector: {connector}")
    return objects


def list_scan_logs(client, org_id):
    payload = client.all_logs(org_id, page=1, page_size=10) or {}
    objects = payload.get("objects", [])
    print(f"Found {payload.get('totalCount', 0)} scan log(s), showing {len(objects)}:")
    for log in objects:
        status_map = {0: "queued", 1: "running", 2: "success", 3: "failed"}
        status = status_map.get(log.get("status"), log.get("status"))
        print(
            f"  [{log['id']}] task {log['taskId']} — connector: "
            f"{log.get('connectorName')} — status: {status}"
        )
    return objects


def main():
    if not API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        sys.exit(1)
    if not ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        sys.exit(1)

    client = get_client()

    print("=== Listing connector configurations ===")
    list_configurations(client, ORGANIZATION_ID)

    print("\n=== Listing scan logs ===")
    list_scan_logs(client, ORGANIZATION_ID)


if __name__ == "__main__":
    main()
