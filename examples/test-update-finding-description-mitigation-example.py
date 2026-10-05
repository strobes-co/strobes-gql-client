"""
Update one or more findings' description and/or mitigation (and, optionally,
evidence / steps to reproduce).

Edit the variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-update-finding-description-mitigation-example.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID

# =============================================================================
# EDIT THESE — the only things you should need to change
# =============================================================================

# Finding IDs to update. Add/remove IDs as needed.
FINDING_IDS = [1]

# New description. Leave as None to skip updating it.
DESCRIPTION = "Updated description text for this finding."

# New mitigation. Leave as None to skip updating it.
MITIGATION = "Updated remediation guidance for this finding."

# New evidence / steps to reproduce. Leave as None to skip updating them.
EVIDENCE = None
STEPS_TO_REPRODUCE = None

# =============================================================================


def update_finding(client, org_id, finding_id):
    result = client.update_bug_mitigation_description(
        organization_id=org_id,
        search_query=f"id = {finding_id}",
        description=DESCRIPTION,
        mitigation=MITIGATION,
        evidence=EVIDENCE,
        steps_to_reproduce=STEPS_TO_REPRODUCE,
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
    if (
        DESCRIPTION is None
        and MITIGATION is None
        and EVIDENCE is None
        and STEPS_TO_REPRODUCE is None
    ):
        print(
            "Error: set at least one of DESCRIPTION/MITIGATION/EVIDENCE/STEPS_TO_REPRODUCE."
        )
        sys.exit(1)

    client = StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)

    print("Strobes Finding Description/Mitigation Updater")
    print("-" * 40)
    if DESCRIPTION is not None:
        print(f"New description:         {DESCRIPTION}")
    if MITIGATION is not None:
        print(f"New mitigation:          {MITIGATION}")
    if EVIDENCE is not None:
        print(f"New evidence:            {EVIDENCE}")
    if STEPS_TO_REPRODUCE is not None:
        print(f"New steps to reproduce:  {STEPS_TO_REPRODUCE}")
    print(f"Findings:     {', '.join(str(fid) for fid in FINDING_IDS)}")
    print("-" * 40)

    succeeded, failed = [], []
    for finding_id in FINDING_IDS:
        updated = update_finding(client, ORGANIZATION_ID, finding_id)
        if updated:
            succeeded.append(finding_id)
            print(f"\nFinding {updated['id']}: updated successfully")
            print(f"  Description:        {updated.get('description')}")
            print(f"  Mitigation:          {updated.get('mitigation')}")
            print(f"  Evidence:            {updated.get('evidence')}")
            print(f"  Steps to reproduce:  {updated.get('stepsToReproduce')}")
        else:
            failed.append(finding_id)
            print(
                f"\nFinding {finding_id}: FAILED — no matching finding found (check the ID and your permissions)"
            )

    print("\n" + "-" * 40)
    print(f"Done: {len(succeeded)} succeeded, {len(failed)} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
