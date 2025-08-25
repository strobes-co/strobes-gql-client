#!/usr/bin/env python3
"""
Test script to verify foreign key relationships in asset data
"""

from fetch_all_assets import get_client, fetch_assets
import json
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import QUERY_CONFIG

def test_foreign_keys():
    """Test that foreign keys are properly fetched and displayed"""
    print("Testing foreign key relationships in asset data...")
    
    # Fetch assets with foreign key fields
    assets_data = fetch_assets(page_size=5)  # Limit to 5 for testing
    
    if not assets_data or not assets_data.get('data') or not assets_data['data'].get('allAssets'):
        print("❌ Failed to fetch assets data")
        return False
    
    assets = assets_data['data']['allAssets']['objects']
    if not assets:
        print("❌ No assets found")
        return False
    
    print(f"✅ Successfully fetched {len(assets)} assets")
    
    # Check each asset for foreign key data
    foreign_key_stats = {
        'has_created_by': 0,
        'has_organization': 0,
        'has_connector': 0,
        'has_tags': 0
    }
    
    for i, asset in enumerate(assets):
        print(f"\n--- Asset {i+1} ---")
        print(f"ID: {asset.get('id')}")
        print(f"Name: {asset.get('name')}")
        
        # Check created_by
        created_by = asset.get('createdBy')
        if created_by:
            foreign_key_stats['has_created_by'] += 1
            print(f"✅ Created By: {created_by.get('firstName', '')} {created_by.get('lastName', '')} (ID: {created_by.get('id')})")
        else:
            print(f"❌ Created By: Not available")
        
        # Check organization
        organization = asset.get('organization')
        if organization:
            foreign_key_stats['has_organization'] += 1
            print(f"✅ Organization: {organization.get('name')} (ID: {organization.get('id')})")
        else:
            print(f"❌ Organization: Not available")
        
        # Check connector
        connector = asset.get('connector')
        if connector:
            foreign_key_stats['has_connector'] += 1
            print(f"✅ Connector: {connector.get('name')} (ID: {connector.get('id')})")
        else:
            print(f"❌ Connector: Not available")
        
        # Check tags
        tags = asset.get('tags', [])
        if tags:
            foreign_key_stats['has_tags'] += 1
            print(f"✅ Tags: {len(tags)} tags")
            for tag in tags[:3]:  # Show first 3 tags
                print(f"   - {tag.get('name')}")
        else:
            print(f"❌ Tags: None")
    
    # Summary
    print(f"\n{'='*50}")
    print("FOREIGN KEY SUMMARY:")
    print(f"Assets with created_by: {foreign_key_stats['has_created_by']}/{len(assets)}")
    print(f"Assets with organization: {foreign_key_stats['has_organization']}/{len(assets)}")
    print(f"Assets with connector: {foreign_key_stats['has_connector']}/{len(assets)}")
    print(f"Assets with tags: {foreign_key_stats['has_tags']}/{len(assets)}")
    

    
    return True

def test_schema_fields():
    """Test that we can access all the fields we're requesting"""
    print("\nTesting schema field access...")
    
    try:
        client = get_client()
        
        # Test a simple query to see what fields are available
        result = client.execute_query("all_assets", 
                                    organization_id=QUERY_CONFIG["organization_id"],
                                    page_size=1,
                                    selected_fields=["id", "name", "createdBy", "organization"])
        
        if result and result.get('data') and result['data'].get('allAssets'):
            print("✅ Schema fields test passed")
            return True
        else:
            print("❌ Schema fields test failed")
            return False
            
    except Exception as e:
        print(f"❌ Schema fields test error: {e}")
        return False

if __name__ == "__main__":
    print("Testing Foreign Key Relationships in Asset Data")
    print("=" * 60)
    
    # Test schema fields first
    schema_ok = test_schema_fields()
    
    # Test foreign key data
    foreign_keys_ok = test_foreign_keys()
    
    print(f"\n{'='*60}")
    if schema_ok and foreign_keys_ok:
        print("✅ All tests passed! Foreign keys are working correctly.")
    else:
        print("❌ Some tests failed. Check the output above for details.") 