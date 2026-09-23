"""
Set custom-field values on existing assets.

Edit the variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-update-asset-custom-fields-example.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID

# =============================================================================
# EDIT THESE — the only things you should need to change
# =============================================================================

# RQL selecting the assets to update. Keep it narrow: `id = 1234` for one
# asset, or e.g. `type = 7 and name ~ 'my-repo'` for a group. Asset `id` is
# an integer in RQL, so do not quote it.
SEARCH_QUERY = "id = 1234"

# Custom-field slug -> value. Slugs are lowercase with underscores (the slug
# Strobes generated when the field was created, e.g. "Last Hotfix Release"
# -> "last_hotfix_release"). Dates as YYYY-MM-DD, numbers as ints.
FIELDS = {
    "last_hotfix_release": "2026-09-18",
    "hotfix_released_by": "jane.doe",
}

# =============================================================================


def main():
    client = StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)

    result = client.bulk_update_asset_custom_fields(
        organization_id=ORGANIZATION_ID,
        search_query=SEARCH_QUERY,
        fields=FIELDS,
    )
    assets = (result or {}).get("asset") or []
    if not assets:
        print("Update accepted; >100 assets matched so it runs in the background.")
        return
    for asset in assets:
        print(f"{asset['name']} ({asset['id']}) -> {asset.get('fields')}")


if __name__ == "__main__":
    main()
