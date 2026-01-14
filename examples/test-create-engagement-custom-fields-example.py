"""
Example: Create Engagement with Custom Fields

This script demonstrates how to create a new engagement (security assessment) 
with custom fields using the Strobes GraphQL client.

⚠️  IMPORTANT: CREATE CUSTOM FIELDS FIRST ⚠️
Before using custom fields in this script, you MUST create them in the Strobes UI:
1. Log into your Strobes account
2. Go to Settings > Custom Fields > Engagement Custom Fields
3. Create the custom fields you want to use (e.g., "notes", "custom_text")
4. Note the field slug (lowercase name) - this is what you'll use in the code
5. For dropdown fields, note the exact option values

Only after creating custom fields in the UI can you use them in this script.

CUSTOM FIELDS:
- Custom fields are passed in the "fields" parameter as a JSON string
- Use the field slug (lowercase) as the key, not the display name
- Example: If you have a custom field named "Notes", use "notes" (lowercase)
- The custom fields MUST exist in your Strobes organization before using them

REQUIRED FIELDS:
- organization_id: Your organization UUID
- name: Engagement name
- scheduled_date: Start date (YYYY-MM-DD format)
- delivery_date: End date (YYYY-MM-DD format)
- subscribed_services: List of service names (e.g., ["tri", "service 1"])
- plans: Number of plans (usually 1)
- assessment_data: JSON string with asset search queries
- state: Engagement state (1 = active)

OPTIONAL FIELDS:
- fields: JSON string with custom field values
- document_ids: List of document IDs
- prerequisites_data: JSON string with prerequisites
- vendor_code: Vendor code string
- is_self_managed: Boolean (True/False)
- include_related_assets: Boolean (True/False)

Run this file:
    python examples/test-create-engagement-custom-fields-example.py
"""

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
from sgqlc.operation import Operation
from strobes_gql_client import schema
import json

# ============================================
# STEP 1: Initialize the client
# ============================================
# The client uses your API token and organization ID from enums.py
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# ============================================
# STEP 2: Configure your engagement
# ============================================

# REQUIRED: Engagement basic information
ENGAGEMENT_NAME = "Security Assessment Q1 2025"  # Change this to your engagement name
SCHEDULED_DATE = "2025-02-01"                     # Start date (YYYY-MM-DD format)
DELIVERY_DATE = "2025-02-28"                     # End date (YYYY-MM-DD format)

# REQUIRED: Service configuration
# Replace "tri" with your actual service name(s)
# You can add multiple services: ["tri", "service 1", "service 2"]
SUBSCRIBED_SERVICES = ["tri"]

# REQUIRED: Asset selection for assessment
# Replace the asset IDs (47, 46) with your actual asset IDs
# Format: "id in (asset_id1, asset_id2, asset_id3)"
ASSET_SEARCH_QUERY = "id in (47,46)"  # Change these IDs to your asset IDs

# OPTIONAL: Custom fields
# ⚠️  IMPORTANT: You MUST create these custom fields in Strobes UI first!
# Steps:
#   1. Go to Strobes UI > Settings > Custom Fields > Engagement Custom Fields
#   2. Create your custom fields (e.g., "notes", "custom_text")
#   3. Note the field slug (lowercase name) - use that as the key below
#   4. For dropdown fields, note the exact option values
#
# Add your custom fields here using the field slug (lowercase)
# Example custom fields (only use fields that exist in Strobes UI):
CUSTOM_FIELDS = {
    "notes": "Initial security assessment for Q1 2025",  # Text field example (must exist in Strobes UI)
    # "custom_text": "Some text value",                  # Another text field
    # "custom_number": 123,                             # Number field
    # "custom_date": "2025-07-16",                      # Date field
    # "custom_boolean": "true",                          # Boolean field (use "true"/"false" as strings)
    # "custom_select": "option_value",                   # Dropdown field (single value)
    # "custom_multiselect": ["option1", "option2"],      # Multi-select field (list)
}

# OPTIONAL: Prerequisites (leave empty list [] if none)
PREREQUISITES = []  # Or add prerequisites like:
# PREREQUISITES = [
#     {
#         "id": None,
#         "title": "Prerequisite title",
#         "description": "Prerequisite description",
#         "assigned_to": "team_name",
#         "due_date": "2025-02-04",
#         "attachments": [],
#         "order_index": 1,
#         "is_completed": False
#     }
# ]

# ============================================
# STEP 3: Build engagement fields
# ============================================
# You usually don't need to modify this section

engagement_fields = {
    # Required fields
    "organization_id": enums.ORGANIZATION_ID,     # Your organization ID
    "name": ENGAGEMENT_NAME,                       # Engagement name
    "scheduled_date": SCHEDULED_DATE,             # Start date
    "delivery_date": DELIVERY_DATE,               # End date
    "subscribed_services": SUBSCRIBED_SERVICES,    # List of services
    "plans": 1,                                   # Number of plans (usually 1)
    "state": 1,                                   # Engagement state (1 = active)
    
    # Custom fields (JSON string format)
    "fields": json.dumps(CUSTOM_FIELDS) if CUSTOM_FIELDS else "{}",
    
    # Assessment data (which assets to assess)
    "assessment_data": json.dumps({
        SUBSCRIBED_SERVICES[0]: [  # Use first service name
            {"search_query": ASSET_SEARCH_QUERY}
        ]
    }),
    
    # Optional fields
    "document_ids": [],                            # List of document IDs (empty if none)
    "prerequisites_data": json.dumps(PREREQUISITES),  # Prerequisites (empty list if none)
    "include_related_assets": False,               # Include related assets (True/False)
    "vendor_code": "",                            # Vendor code (empty string if none)
    "is_self_managed": True,                       # Self-managed engagement (True/False)
}

# ============================================
# STEP 4: Create the engagement
# ============================================
# This section executes the creation - usually no changes needed

def create_engagement():
    """Create the engagement with the configured fields"""
    try:
        print("🚀 Creating engagement...")
        print(f"   Name: {ENGAGEMENT_NAME}")
        print(f"   Scheduled: {SCHEDULED_DATE} to {DELIVERY_DATE}")
        print(f"   Services: {', '.join(SUBSCRIBED_SERVICES)}")
        print(f"   Custom fields: {CUSTOM_FIELDS}")
        
        op = Operation(schema.Mutation)
        mutation = op.create_engagement(**engagement_fields)
        mutation.engagement.id()
        mutation.engagement.name()
        
        response = client.endpoint(op)
        
        if response.get("errors"):
            print(f"\n❌ Error creating engagement:")
            print(f"   {response['errors']}")
            print("\n💡 Common issues:")
            print("   - Check that asset IDs exist in your organization")
            print("   - Verify service names match your configured services")
            print("   - ⚠️  IMPORTANT: Custom fields must be created in Strobes UI first!")
            print("      Go to Settings > Custom Fields > Engagement Custom Fields")
            print("   - Ensure custom field slugs are correct (use lowercase)")
            print("   - Check date format is YYYY-MM-DD")
        elif response.get("data", {}).get("createEngagement"):
            engagement = response["data"]["createEngagement"]["engagement"]
            print("\n✅ Engagement created successfully!")
            print(f"   ID: {engagement.get('id')}")
            print(f"   Name: {engagement.get('name')}")
        else:
            print("\n❌ No data returned from API")
            print(f"   Response: {response}")
            
    except Exception as exc:
        print(f"\n❌ Exception occurred: {exc}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("=" * 60)
    print("Strobes Engagement Creation with Custom Fields")
    print("=" * 60)
    create_engagement()