# examples/test-createengagement-example.py
"""Example script demonstrating how to create an engagement (security assessment)
using the Strobes GraphQL client.

Run this file directly to create a sample engagement:

    python examples/test-createengagement-example.py
"""

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
from sgqlc.operation import Operation
from strobes_gql_client import schema
import json

def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def create_sample_engagement():
    """Create a simple engagement"""
    client = get_client()

    # Prepare engagement fields exactly as in the working mutation
    engagement_fields = {
        "document_ids": [],
        "organization_id": enums.ORGANIZATION_ID,
        "name": "Demo Engagement 1234555",
        "scheduled_date": "2025-08-06",
        "delivery_date": "2025-08-22",
        "fields": "{}",
        "subscribed_services": ["service 1"],
        "plans": 1,
        "assessment_data": json.dumps({
            "service 1": [
                {"search_query": "id in (38069,38070)"},
                {
                    "asset_id": "38069",
                    "asset_type": 1,
                    "scheduled_date": "2025-08-06",
                    "delivery_date": "2025-08-22",
                    "vpn_accounts": "",
                    "test_accounts": "",
                    "instructions": "",
                    "scope": ""
                },
                {
                    "asset_id": "38070",
                    "asset_type": 1,
                    "scheduled_date": "2025-08-06",
                    "delivery_date": "2025-08-22",
                    "vpn_accounts": "",
                    "test_accounts": "",
                    "instructions": "",
                    "scope": ""
                }
            ]
        }),
        "prerequisites_data": json.dumps([
            {
                "id": None,
                "title": "for testing prerequisites data",
                "description": "test description for prerequisites data",
                "assigned_to": "security_team",
                "due_date": "2025-08-04",
                "attachments": [],
                "order_index": 1,
                "is_completed": True
            }
        ]),
        "include_related_assets": False,
        "vendor_code": "",
        "is_self_managed": True
    }

    try:
        # Execute the mutation
        op = Operation(schema.Mutation)
        mutation = op.create_engagement(**engagement_fields)
        mutation.engagement.id()
        mutation.engagement.name()
        mutation.engagement.prerequisites_engagement()
        
        response = client.endpoint(op)
        
        if response.get("errors"):
            print(f"❌ GraphQL Errors: {response['errors']}")
            return

        engagement = (
            response.get("data", {})
            .get("createEngagement", {})
            .get("engagement", {})
        )
        
        if engagement:
            print(f"✅ Engagement created successfully!")
            print(f"ID: {engagement.get('id')}")
            print(f"Name: {engagement.get('name')}")
            if engagement.get('prerequisitesEngagement'):
                print("Prerequisites:")
                for prereq in engagement.get('prerequisitesEngagement', []):
                    print(f"- {prereq.get('title')}: {prereq.get('description')}")
        else:
            print("❌ No engagement data returned")
            
    except Exception as exc:
        print(f"❌ Error creating engagement: {exc}")


if __name__ == "__main__":
    print("🚀 Strobes Engagement Creation Example")
    print("=" * 50)
    create_sample_engagement() 