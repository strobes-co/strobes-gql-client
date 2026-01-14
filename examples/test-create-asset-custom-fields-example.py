"""
Example: Create Asset with Custom Fields

This script demonstrates how to create a new asset with custom fields 
using the Strobes GraphQL client.

⚠️  IMPORTANT: CREATE CUSTOM FIELDS FIRST ⚠️
Before using custom fields in this script, you MUST create them in the Strobes UI:
1. Log into your Strobes account
2. Go to Settings > Custom Fields > Asset Custom Fields
3. Create the custom fields you want to use (e.g., "developer", "priority")
4. Note the field slug (lowercase name) - this is what you'll use in the code
5. For dropdown fields, note the exact option values (usually lowercase)

Only after creating custom fields in the UI can you use them in this script.

CUSTOM FIELDS:
- Custom fields are passed in the "custom_fields" parameter as a JSON string
- Use the field slug (lowercase) as the key, not the display name
- Example: If you have a custom field named "Developer", use "developer" (lowercase)
- For dropdown fields, use lowercase values (e.g., "p1" not "P1")
- The custom fields MUST exist in your Strobes organization before using them

ASSET TYPES:
- 1 = Web Asset (requires: url)
- 2 = Mobile Asset (requires: package)
- 3 = Network Asset (requires: ipaddress or ipaddress_list)
- 4 = Cloud Asset (requires: cloud_type)
- 7 = Code Repository Asset (requires: url)

REQUIRED FIELDS (All Asset Types):
- name: Asset name
- organization_id: Your organization UUID
- type: Asset type (1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code)
- sensitivity: Sensitivity level (1=Low, 2=Medium, 3=High, 4=Critical)
- exposed: Exposure level (1=Private, 2=Public)

REQUIRED FIELDS (Type-Specific):
- Web (type=1): url
- Mobile (type=2): package
- Network (type=3): ipaddress or ipaddress_list
- Cloud (type=4): cloud_type (1=Other, 2=AWS, 3=Azure, 4=GCP)
- Code (type=7): url

OPTIONAL FIELDS:
- custom_fields: JSON string with custom field values
- tags: List of tags (e.g., ["production", "web"])
- hostname: Hostname (for Network assets)
- os: Operating system (for Network assets)
- mac_address: MAC address (for Network assets)
- region: Cloud region (for Cloud assets)
- account_id: Cloud account ID (for Cloud assets)
- resource_id: Cloud resource ID (for Cloud assets)

Run this file:
    python examples/test-create-asset-custom-fields-example.py
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
# STEP 2: Configure your asset
# ============================================

# REQUIRED: Asset basic information
ASSET_NAME = "My Web Application"              # Change this to your asset name
ASSET_TYPE = 1                                 # 1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code
SENSITIVITY = 3                                # 1=Low, 2=Medium, 3=High, 4=Critical
EXPOSED = 2                                    # 1=Private, 2=Public

# REQUIRED: Type-specific fields (choose based on ASSET_TYPE)
# For Web Assets (type=1):
ASSET_URL = "https://app.example.com"         # Web application URL

# For Mobile Assets (type=2):
# ASSET_PACKAGE = "com.company.app"            # Package name or bundle ID

# For Network Assets (type=3):
# ASSET_IPADDRESS = "192.168.1.100"           # IP address
# ASSET_HOSTNAME = "server-01"                 # Optional: Hostname
# ASSET_OS = "Ubuntu 20.04"                    # Optional: Operating system

# For Cloud Assets (type=4):
# CLOUD_TYPE = 2                               # 1=Other, 2=AWS, 3=Azure, 4=GCP
# CLOUD_REGION = "us-east-1"                    # Optional: Cloud region

# For Code Repository Assets (type=7):
# REPO_URL = "https://github.com/company/repo" # Repository URL

# OPTIONAL: Tags for categorization
ASSET_TAGS = ["production", "web"]             # List of tags (can be empty [])

# OPTIONAL: Custom fields
# ⚠️  IMPORTANT: You MUST create these custom fields in Strobes UI first!
# Steps:
#   1. Go to Strobes UI > Settings > Custom Fields > Asset Custom Fields
#   2. Create your custom fields (e.g., "developer", "priority")
#   3. Note the field slug (lowercase name) - use that as the key below
#   4. For dropdown fields, note the exact option values (usually lowercase)
#
# Add your custom fields here using the field slug (lowercase)
# IMPORTANT: For dropdown fields, use lowercase values (e.g., "p1" not "P1")
CUSTOM_FIELDS = {
    "developer": "John Doe",                  # Text field example (must exist in Strobes UI)
    "priority": "p1",                          # Dropdown field (use lowercase: p0, p1, p2, p3)
    # Add more custom fields here (only if they exist in Strobes UI):
    # "department": "Engineering",             # Another text field
    # "environment": "production",              # Dropdown field (use lowercase value)
    # "owner_email": "owner@example.com",      # Email/text field
}

# ============================================
# STEP 3: Build asset fields based on type
# ============================================

# Base fields (required for all asset types)
asset_fields = {
    "name": ASSET_NAME,
    "organization_id": enums.ORGANIZATION_ID,
    "type": ASSET_TYPE,
    "sensitivity": SENSITIVITY,
    "exposed": EXPOSED,
    "tags": ASSET_TAGS,
    "custom_fields": json.dumps(CUSTOM_FIELDS) if CUSTOM_FIELDS else None,
}

# Add type-specific required fields
if ASSET_TYPE == 1:  # Web Asset
    asset_fields["url"] = ASSET_URL
elif ASSET_TYPE == 2:  # Mobile Asset
    # Uncomment and set ASSET_PACKAGE above
    # asset_fields["package"] = ASSET_PACKAGE
    print("❌ Error: Mobile asset type selected. Please set ASSET_PACKAGE in configuration.")
    exit(1)
elif ASSET_TYPE == 3:  # Network Asset
    # Uncomment and set ASSET_IPADDRESS above
    # asset_fields["ipaddress"] = ASSET_IPADDRESS
    # asset_fields["hostname"] = ASSET_HOSTNAME  # Optional
    # asset_fields["os"] = ASSET_OS  # Optional
    print("❌ Error: Network asset type selected. Please set ASSET_IPADDRESS in configuration.")
    exit(1)
elif ASSET_TYPE == 4:  # Cloud Asset
    # Uncomment and set CLOUD_TYPE above
    # asset_fields["cloud_type"] = CLOUD_TYPE
    # asset_fields["region"] = CLOUD_REGION  # Optional
    print("❌ Error: Cloud asset type selected. Please set CLOUD_TYPE in configuration.")
    exit(1)
elif ASSET_TYPE == 7:  # Code Repository Asset
    # Uncomment and set REPO_URL above
    # asset_fields["url"] = REPO_URL
    print("❌ Error: Code repository asset type selected. Please set REPO_URL in configuration.")
    exit(1)
else:
    print(f"❌ Error: Invalid asset type {ASSET_TYPE}. Use 1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code")
    exit(1)

# Remove None values
asset_fields = {k: v for k, v in asset_fields.items() if v is not None}

# ============================================
# STEP 4: Create the asset
# ============================================
# This section executes the creation - usually no changes needed

def create_asset():
    """Create the asset with the configured fields"""
    try:
        print("🚀 Creating asset...")
        print(f"   Name: {ASSET_NAME}")
        print(f"   Type: {ASSET_TYPE} ({'Web' if ASSET_TYPE == 1 else 'Mobile' if ASSET_TYPE == 2 else 'Network' if ASSET_TYPE == 3 else 'Cloud' if ASSET_TYPE == 4 else 'Code'})")
        print(f"   Sensitivity: {SENSITIVITY} ({'Low' if SENSITIVITY == 1 else 'Medium' if SENSITIVITY == 2 else 'High' if SENSITIVITY == 3 else 'Critical'})")
        print(f"   Exposed: {EXPOSED} ({'Private' if EXPOSED == 1 else 'Public'})")
        print(f"   Tags: {', '.join(ASSET_TAGS) if ASSET_TAGS else 'None'}")
        print(f"   Custom fields: {CUSTOM_FIELDS}")
        
        op = Operation(schema.Mutation)
        mutation = op.create_asset(**asset_fields)
        mutation.asset.id()
        mutation.asset.name()
        
        response = client.endpoint(op)
        
        if response.get("errors"):
            print(f"\n❌ Error creating asset:")
            print(f"   {response['errors']}")
            print("\n💡 Common issues:")
            print("   - Check that all required fields are set for your asset type")
            print("   - ⚠️  IMPORTANT: Custom fields must be created in Strobes UI first!")
            print("      Go to Settings > Custom Fields > Asset Custom Fields")
            print("   - Verify custom field slugs are correct (use lowercase)")
            print("   - For dropdown fields, use lowercase values (e.g., 'p1' not 'P1')")
            print("   - Ensure URL format is correct (starts with http:// or https://)")
            print("   - Check that asset name is unique")
        elif response.get("data", {}).get("createAsset"):
            asset = response["data"]["createAsset"]["asset"]
            print("\n✅ Asset created successfully!")
            print(f"   ID: {asset.get('id')}")
            print(f"   Name: {asset.get('name')}")
        else:
            print("\n❌ No data returned from API")
            print(f"   Response: {response}")
            
    except Exception as exc:
        print(f"\n❌ Exception occurred: {exc}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("=" * 60)
    print("Strobes Asset Creation with Custom Fields")
    print("=" * 60)
    create_asset()
