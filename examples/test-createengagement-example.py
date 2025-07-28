# examples/test-createengagement-example.py
"""Example script demonstrating how to create an engagement (security assessment)
using the Strobes GraphQL client.

Run this file directly to create a sample engagement:

    python examples/test-createengagement-example.py

IMPORTANT: Update the required fields (especially `name`, `organization_id`,
`subscribed_services`, and any custom JSON strings) to values valid in your
Strobes tenant before execution.
"""

import json
from datetime import date, timedelta
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums


def get_client():
    """Instantiate a GraphQL client using credentials from enums.py"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def create_sample_engagement():
    """Create a simple engagement with two subscribed services"""
    client = get_client()

    # Build dynamic dates (today + offsets) for the demo
    scheduled_date = date.today() + timedelta(days=7)
    delivery_date = scheduled_date + timedelta(days=14)

    engagement_fields = {
        "name": "Demo Security Engagement",               # Required: Engagement name
        "organization_id": enums.ORGANIZATION_ID,          # Required: Organization UUID
        "vendor_code": "demo-001",                       # Optional: Vendor code / reference
        "scheduled_date": scheduled_date.isoformat(),      # Optional: YYYY-MM-DD
        "delivery_date": delivery_date.isoformat(),        # Optional: YYYY-MM-DD
        "plans": 1,                                        # Required: Plan / tier (1 = Basic)
        "document_ids": [],                                # Optional: Attachments (Vault IDs)
        "subscribed_services": [                           # Required: Services included
            "Web Application Penetration Test",
            "Cloud Security"
        ],
        # Assessment & prerequisite data may need to be formatted as JSON strings.
        # Provide minimal data for the example. Adjust as per your workflow.
        "assessment_data": json.dumps({
            "Web Application Penetration Test": [
                {"search_query": "type = 1"}
            ]
        }),
        "prerequisites_data": "[]",
        "fields": json.dumps({"internal_info": "Created via API demo"})
    }

    try:
        result = client.execute_mutation("create_engagement", **engagement_fields)
        engagement_id = (
            result.get("data", {})
            .get("createEngagement", {})
            .get("engagement", [{}])[0]
            .get("id")
        )
        print(f"✅ Engagement created successfully! ID: {engagement_id}")
    except Exception as exc:
        print(f"❌ Error creating engagement: {exc}")


def main():
    print("🚀 Strobes Engagement Creation Example")
    print("=" * 50)
    create_sample_engagement()


if __name__ == "__main__":
    main() 