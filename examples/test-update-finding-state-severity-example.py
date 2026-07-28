"""
Update one or more findings' state and/or severity.

Edit the three variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-update-finding-state-severity-example.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID

# =============================================================================
# EDIT THESE — the only three things you should need to change
# =============================================================================

# Finding IDs to update. Add/remove IDs as needed.
FINDING_IDS = [1]

# State to set. Leave as None to skip updating state.
#   1 = Active/New
#   2 = Resolved
#   3 = Not Applicable
#   4 = Duplicate
#   5 = Accepted Risk
#   6 = Won't Fix
STATE = 1

# Severity to set. Leave as None to skip updating severity.
#   1 = Info
#   2 = Low
#   3 = Medium
#   4 = High
#   5 = Critical
SEVERITY = 5

# =============================================================================

STATE_LABELS = {
    1: "Active/New",
    2: "Resolved",
    3: "Not Applicable",
    4: "Duplicate",
    5: "Accepted Risk",
    6: "Won't Fix",
}
SEVERITY_LABELS = {
    1: "Info",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Critical",
}


def describe_state(value):
    return f"{STATE_LABELS.get(value, 'Unknown')} ({value})"


def describe_severity(value):
    return f"{SEVERITY_LABELS.get(value, 'Unknown')} ({value})"


def update_finding(client, org_id, finding_id, state, severity):
    result = client.execute_mutation(
        "bug_bulk_update",
        organization_id=org_id,
        search_query=f"id = {finding_id}",
        state=state,
        severity=severity,
    )
    bugs = (result or {}).get("bugs") or []
    return bugs[0] if bugs else None


def main():
    if not API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        sys.exit(1)
    if not ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        sys.exit(1)
    if not FINDING_IDS:
        print("Error: FINDING_IDS is empty — add at least one finding ID to update.")
        sys.exit(1)
    if STATE is None and SEVERITY is None:
        print("Error: set STATE and/or SEVERITY at the top of this file.")
        sys.exit(1)

    client = StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)

    print("Strobes Finding Updater")
    print("-" * 40)
    if STATE is not None:
        print(f"New state:    {describe_state(STATE)}")
    if SEVERITY is not None:
        print(f"New severity: {describe_severity(SEVERITY)}")
    print(f"Findings:     {', '.join(str(fid) for fid in FINDING_IDS)}")
    print("-" * 40)

    succeeded, failed = [], []
    for finding_id in FINDING_IDS:
        updated = update_finding(client, ORGANIZATION_ID, finding_id, STATE, SEVERITY)
        if updated:
            succeeded.append(finding_id)
            print(f"\nFinding {updated['id']}: updated successfully")
            print(f"  State:    {describe_state(updated['state'])}")
            print(f"  Severity: {describe_severity(updated['severity'])}")
        else:
            failed.append(finding_id)
            print(f"\nFinding {finding_id}: FAILED — no matching finding found (check the ID and your permissions)")

    print("\n" + "-" * 40)
    print(f"Done: {len(succeeded)} succeeded, {len(failed)} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
