# examples/test-fetchengagement-example.py
"""Example script demonstrating how to fetch engagements using the Strobes GraphQL client.

Run this file directly to see sample outputs:

    python examples/test-fetchengagement-example.py

Update the connection details in `strobes_gql_client/enums.py` (APP_HOST, API_TOKEN,
ORGANIZATION_ID) before running.
"""

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums


def get_client():
    """Initialize and return a configured GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def fetch_all_engagements():
    """Fetch all engagements for the configured organization"""
    print("=== Fetching All Engagements ===")
    client = get_client()
    try:
        resp = client.execute_query(
            "all_engagements", organization_id=enums.ORGANIZATION_ID
        )
        engagements = resp.get("data", {}).get("allEngagements", {}).get("objects", [])
        print(f"Total engagements: {len(engagements)}")

        # Show a preview of the first few engagements
        for eng in engagements[:5]:
            print(
                f"- {eng.get('name')} (ID: {eng.get('id')}, State: {eng.get('state')})"
            )
        return engagements
    except Exception as exc:
        print(f"Error while fetching engagements: {exc}")
        return []


def fetch_engagements_with_query():
    """Fetch engagements using a search query (update the query as needed)"""
    print("\n=== Fetching Engagements Using Search Query ===")
    client = get_client()
    search_query = 'name ~ "Security" and state = "Active"'  # Example query
    try:
        resp = client.execute_query(
            "all_engagements",
            organization_id=enums.ORGANIZATION_ID,
            search_query=search_query,
        )
        engagements = resp.get("data", {}).get("allEngagements", {}).get("objects", [])
        print(f"Matching engagements: {len(engagements)}")
        for eng in engagements[:3]:
            print(
                f"- {eng.get('name')} | Scheduled: {eng.get('scheduled_date')} | Services: {eng.get('subscribed_services')}"
            )
    except Exception as exc:
        print(f"Error while searching engagements: {exc}")


def demonstrate_engagement_details():
    """Retrieve a single engagement and print a selection of useful fields"""
    print("\n=== Engagement Response Field Demonstration ===")
    engagements = fetch_all_engagements()
    if not engagements:
        print("No engagements found to demonstrate")
        return

    eng = engagements[0]
    print("Sample engagement fields:")
    print(f"  ID: {eng.get('id')}")
    print(f"  Name: {eng.get('name')}")
    print(f"  Scheduled Date: {eng.get('scheduled_date')}")
    print(f"  Delivery Date: {eng.get('delivery_date')}")
    print(f"  State: {eng.get('state')}")
    print(f"  Subscribed Services: {eng.get('subscribed_services')}")
    print(f"  Created: {eng.get('created')}")
    print(f"  Updated: {eng.get('updated')}")


def main():
    """Run the fetch engagement examples"""
    print("🔍 Strobes Engagement Fetching Examples")
    print("=" * 50)

    # Basic fetch
    fetch_all_engagements()

    # Uncomment to test search query example
    # fetch_engagements_with_query()

    # Uncomment to show detailed field demonstration
    # demonstrate_engagement_details()

    print("\n✅ Engagement fetching examples completed!")


if __name__ == "__main__":
    main() 