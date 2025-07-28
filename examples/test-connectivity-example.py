# examples/test-connectivity-example.py
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import json

def test_connectivity():
    """Test connectivity to Strobes platform"""
    try:
        # Initialize client using configuration from enums
        client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)
        
        # Test connection
        resp = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
        assets = resp.get("data", {}).get("allAssets", {}).get("objects", [])
        
        print(f"Connection successful!")
        print(f"Total assets: {len(assets)}")
        return True
        
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_connectivity()
