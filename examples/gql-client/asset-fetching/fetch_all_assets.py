from strobes_gql_client.client import StrobesGQLClient
import json
from datetime import datetime
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CONNECTION_CONFIG, QUERY_CONFIG

def get_client():
    return StrobesGQLClient(**CONNECTION_CONFIG)

def fetch_assets(organization_id=None, search_query=None, page_size=50):
    """Fetch assets with detailed fields including created_by"""
    # Use default organization_id from config if not provided
    if organization_id is None:
        organization_id = QUERY_CONFIG["organization_id"]
    try:
        client = get_client()
        print(f"Querying with detailed fields, search: {search_query}")
        
        # Build parameters dict, filtering out None values
        params = {"organization_id": organization_id}
        if search_query:
            params["search_query"] = search_query
        if page_size:
            params["page_size"] = page_size
            
        # Add selected_fields to include created_by and other fields
        # Use the exact field names from the GraphQL schema (camelCase)
        params["selected_fields"] = [
            "id", "name", "updated", "target", "type", "data", "fields", 
            "sensitivity", "exposed", "created", "isActive", "ipaddress", 
            "os", "riskScore", "macAddress", "hostname", "cloudType", 
            "resourceId", "accountId", "region", "cdn", "asmLastAlive",
            "createdBy", "tags", "assessmentsSet", "connector", "lastSeen", "scan"
        ]
        
        result = client.execute_query("all_assets", **params)
        return result
    except Exception as e:
        print(f"Error fetching assets: {e}")
        return None

def analyze_assets(assets_data):
    """Analyze assets and show type breakdown, creators, and organizations"""
    if not assets_data or not assets_data.get('data') or not assets_data['data'].get('allAssets') or not assets_data['data']['allAssets'].get('objects'):
        print("No assets data to analyze")
        return
    
    assets = assets_data['data']['allAssets']['objects']
    print(f"\n=== Asset Analysis ===")
    print(f"Total assets: {len(assets)}")
    
    # Type breakdown
    type_counts = {}
    creator_counts = {}
    organization_counts = {}
    
    for asset in assets:
        # Count by type
        asset_type = asset.get('type', 'Unknown')
        type_counts[asset_type] = type_counts.get(asset_type, 0) + 1
        
        # Count by creator
        created_by = asset.get('createdBy')
        if created_by:
            creator_name = f"{created_by.get('firstName', 'Unknown')} {created_by.get('lastName', '')}"
            creator_counts[creator_name] = creator_counts.get(creator_name, 0) + 1
        else:
            creator_counts['Unknown'] = creator_counts.get('Unknown', 0) + 1
        
        # Count by organization
        organization = asset.get('organization')
        if organization:
            org_name = organization.get('name', 'Unknown Organization')
            organization_counts[org_name] = organization_counts.get(org_name, 0) + 1
        else:
            organization_counts['Unknown'] = organization_counts.get('Unknown', 0) + 1
    
    print(f"\nAsset types:")
    for asset_type, count in sorted(type_counts.items()):
        type_name = {1: "Web", 2: "Mobile", 3: "Network", 4: "Cloud", 7: "Code"}.get(asset_type, f"Type {asset_type}")
        print(f"  {type_name}: {count} assets")
    
    print(f"\nAsset creators:")
    for creator, count in sorted(creator_counts.items()):
        print(f"  {creator}: {count} assets")
    
    print(f"\nOrganizations:")
    for org, count in sorted(organization_counts.items()):
        print(f"  {org}: {count} assets")
    
    # Show sample asset data with detailed foreign key information
    if assets:
        print(f"\nSample asset data:")
        sample_asset = assets[0]
        print(f"  ID: {sample_asset.get('id')}")
        print(f"  Name: {sample_asset.get('name')}")
        print(f"  Type: {sample_asset.get('type')}")
        print(f"  Created: {sample_asset.get('created')}")
        
        # Display created_by information
        created_by = sample_asset.get('createdBy')
        if created_by:
            print(f"  Created By: {created_by.get('firstName', '')} {created_by.get('lastName', '')} (ID: {created_by.get('id', 'N/A')})")
            print(f"    Email: {created_by.get('email', 'N/A')}")
        else:
            print(f"  Created By: Not available")
        
        # Display organization information
        organization = sample_asset.get('organization')
        if organization:
            print(f"  Organization: {organization.get('name', 'N/A')} (ID: {organization.get('id', 'N/A')})")
            print(f"    Domain: {organization.get('domain', 'N/A')}")
        else:
            print(f"  Organization: Not available")

def fetch_assets_by_type(asset_type, organization_id=None):
    """Fetch assets by specific type"""
    search_query = f'type in ("{asset_type}")'
    return fetch_assets(organization_id, search_query)

def fetch_assets_by_sensitivity(sensitivity, organization_id=None):
    """Fetch assets by sensitivity level"""
    search_query = f'sensitivity in ("{sensitivity}")'
    return fetch_assets(organization_id, search_query)

def fetch_assets_by_exposure(exposure, organization_id=None):
    """Fetch assets by exposure level"""
    search_query = f'exposed in ("{exposure}")'
    return fetch_assets(organization_id, search_query)

def fetch_assets_by_name_pattern(pattern, organization_id=None):
    """Fetch assets by name pattern"""
    search_query = f'name contains "{pattern}"'
    return fetch_assets(organization_id, search_query)

def export_to_json(assets_data, filename=None):
    """Export assets data to JSON file"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"assets_export_{timestamp}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(assets_data, f, indent=2, default=str)
        print(f"Assets exported to {filename}")
    except Exception as e:
        print(f"Error exporting to JSON: {e}")

def fetch_assets_with_search_query(search_query, organization_id=None):
    """Fetch assets with custom search query"""
    return fetch_assets(organization_id, search_query)



if __name__ == "__main__":
    # Fetch all assets with generic query
    all_assets = fetch_assets()
    analyze_assets(all_assets)
    
    # Export to JSON
    export_to_json(all_assets)
    

    
    # Example: Fetch assets by type
    # web_assets = fetch_assets_by_type("web")
    # analyze_assets(web_assets)
    
    # Example: Fetch assets by sensitivity
    # high_sensitivity_assets = fetch_assets_by_sensitivity("high")
    # analyze_assets(high_sensitivity_assets)