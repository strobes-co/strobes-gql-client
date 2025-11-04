from strobes_gql_client.client import StrobesGQLClient
from config import CONNECTION_CONFIG, QUERY_CONFIG

def get_client():
    """Create and return a Strobes GraphQL client"""
    return StrobesGQLClient(**CONNECTION_CONFIG)

def test_connectivity():
    """Test connectivity and basic functionality"""
    try:
        print("🔌 Testing Strobes GraphQL API connectivity...")
        
        client = get_client()
        print(f"✅ Client created - URL: {client.graphql_url}")
        
        # Test basic query
        result = client.execute_query(
            "all_assets",
            organization_id=QUERY_CONFIG["organization_id"],
        )
        
        if result and "data" in result and "allAssets" in result["data"]:
            assets = result["data"]["allAssets"]["objects"]
            print(f"✅ Query successful - Found {len(assets)} assets")
            
            # Quick asset breakdown
            types = {}
            for asset in assets:
                asset_type = asset.get('type', 'unknown')
                types[asset_type] = types.get(asset_type, 0) + 1
            
            print("Asset types:")
            for asset_type, count in types.items():
                type_name = {1: "Web", 2: "Mobile", 3: "Network", 4: "Cloud", 7: "Code"}.get(asset_type, f"Type {asset_type}")
                print(f"  {type_name}: {count}")
            
            return True
        else:
            print(f"❌ Query failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def main():
    """Run connectivity test"""
    print("🚀 Strobes GraphQL API Test")
    print("=" * 40)
    
    success = test_connectivity()
    
    print("=" * 40)
    if success:
        print("🎉 All tests passed! API is working correctly.")
    else:
        print("❌ Tests failed. Check connection details.")
    print("=" * 40)

if __name__ == "__main__":
    main() 