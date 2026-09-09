"""
Update one or more engagements' state.

Edit the variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-update-engagement-state-example.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID

# =============================================================================
# EDIT THESE — the only things you should need to change
# =============================================================================

# Engagement IDs to update (UUIDs). Add/remove IDs as needed.
ENGAGEMENT_IDS = ["914db797-f6e7-439b-8af0-54da5f96d609"]

# State to set. Check with your organization for the state values in use —
# this client doesn't hardcode a mapping since it varies per deployment.
STATE = 6

# =============================================================================


def get_current_states(client, org_id, engagement_ids):
    """Look up each engagement's state before updating, via allEngagements."""
    ids_clause = ", ".join(f'"{eid}"' for eid in engagement_ids)
    result = client.execute_query(
        "all_engagements",
        organization_id=org_id,
        search_query=f"id in ({ids_clause})",
    )
    objects = (result or {}).get("objects") or []
    return {e["id"]: e["state"] for e in objects}


def update_single_engagement(client, org_id, engagement_id, state):
    """Update one engagement via updateEngagement (also accepts name, dates,
    assignees, executive summary, etc. — pass any other updateEngagement
    argument as an extra keyword here)."""
    result = client.execute_mutation(
        "update_engagement",
        organization_id=org_id,
        engagement_id=engagement_id,
        state=state,
    )
    engagements = (result or {}).get("engagement") or []
    return engagements[0] if engagements else None


def update_engagements_in_bulk(client, org_id, engagement_ids, state):
    """Update many engagements at once via bulkUpdateEngagements."""
    result = client.execute_mutation(
        "bulk_update_engagements",
        organization_id=org_id,
        engagement_ids=engagement_ids,
        state=state,
    )
    return (result or {}).get("engagements") or []


def main():
    if not API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        sys.exit(1)
    if not ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        sys.exit(1)
    if not ENGAGEMENT_IDS:
        print("Error: ENGAGEMENT_IDS is empty — add at least one engagement ID to update.")
        sys.exit(1)

    client = StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)

    print("Strobes Engagement State Updater")
    print("-" * 40)
    print(f"New state:   {STATE}")
    print(f"Engagements: {', '.join(ENGAGEMENT_IDS)}")
    print("-" * 40)

    current_states = get_current_states(client, ORGANIZATION_ID, ENGAGEMENT_IDS)
    for engagement_id in ENGAGEMENT_IDS:
        if engagement_id in current_states:
            print(f"Engagement {engagement_id}: current state = {current_states[engagement_id]}")
        else:
            print(f"Engagement {engagement_id}: NOT FOUND (check the ID and your permissions)")
    print("-" * 40)

    updated = update_engagements_in_bulk(client, ORGANIZATION_ID, ENGAGEMENT_IDS, STATE)
    updated_ids = {e["id"]: e["state"] for e in updated}

    for engagement_id in ENGAGEMENT_IDS:
        if engagement_id in updated_ids:
            before = current_states.get(engagement_id, "?")
            after = updated_ids[engagement_id]
            print(f"\nEngagement {engagement_id}: updated successfully ({before} -> {after})")
        else:
            print(f"\nEngagement {engagement_id}: FAILED — no matching engagement found (check the ID and your permissions)")

    failed = [eid for eid in ENGAGEMENT_IDS if eid not in updated_ids]
    print("\n" + "-" * 40)
    print(f"Done: {len(updated_ids)} succeeded, {len(failed)} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
