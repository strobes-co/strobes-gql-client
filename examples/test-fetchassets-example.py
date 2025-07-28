# examples/test-fetchassets-example.py
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def fetch_all_assets():
    """Fetch all assets from organization"""
    print("=== Fetching All Assets ===")
    try:
        client = get_client()
        response = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
        assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
        
        print(f"Total assets: {len(assets)}")
        
        # Show first 5 assets
        for asset in assets[:5]:
            name = asset.get('name', 'Unknown')
            asset_type = asset.get('type', 'Unknown')
            risk_score = asset.get('risk_score', 'N/A')
            print(f"- {name} (Type: {asset_type}, Risk: {risk_score})")
            
        return assets
        
    except Exception as e:
        print(f"Error fetching assets: {e}")
        return []

def fetch_assets_by_type():
    """Fetch assets by different types"""
    print("\n=== Fetching Assets by Type ===")
    client = get_client()
    
    # Asset types: 1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code repo
    asset_types = {
        1: "Web",
        2: "Mobile", 
        3: "Network",
        4: "Cloud",
        7: "Code repo"
    }
    
    for type_id, type_name in asset_types.items():
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=f"type = {type_id}"
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{type_name} assets: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {type_name} assets: {e}")

def fetch_assets_by_sensitivity():
    """Fetch assets by sensitivity levels"""
    print("\n=== Fetching Assets by Sensitivity ===")
    client = get_client()
    
    # Sensitivity levels: 1=Low, 2=Medium, 3=High, 4=Critical
    sensitivity_levels = {
        1: "Low",
        2: "Medium",
        3: "High", 
        4: "Critical"
    }
    
    for level_id, level_name in sensitivity_levels.items():
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=f"sensitivity = {level_id}"
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{level_name} sensitivity assets: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {level_name} sensitivity assets: {e}")

def fetch_assets_by_exposure():
    """Fetch assets by exposure levels"""
    print("\n=== Fetching Assets by Exposure ===")
    client = get_client()
    
    # Exposure levels: 1=Private, 2=Public
    exposure_levels = {
        1: "Private",
        2: "Public"
    }
    
    for exposure_id, exposure_name in exposure_levels.items():
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=f"exposed = {exposure_id}"
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{exposure_name} assets: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {exposure_name} assets: {e}")

def fetch_assets_by_risk_score():
    """Fetch assets by risk score ranges"""
    print("\n=== Fetching Assets by Risk Score ===")
    client = get_client()
    
    risk_ranges = [
        ("High Risk (80+)", "risk_score >= 80"),
        ("Medium Risk (40-79)", "risk_score >= 40 and risk_score < 80"),
        ("Low Risk (<40)", "risk_score < 40")
    ]
    
    for range_name, search_query in risk_ranges:
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=search_query
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{range_name}: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {range_name}: {e}")

def fetch_assets_by_patterns():
    """Fetch assets using name and target patterns"""
    print("\n=== Fetching Assets by Patterns ===")
    client = get_client()
    
    patterns = [
        ("Production assets", 'name ~ "production"'),
        ("API assets", 'target ~ "api"'),
        ("Server assets", 'hostname ~ "server"'),
        ("Test assets", 'name ~ "test"')
    ]
    
    for pattern_name, search_query in patterns:
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=search_query
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{pattern_name}: {len(assets)}")
            
            # Show first few matching assets
            for asset in assets[:2]:
                name = asset.get('name', 'Unknown')
                target = asset.get('target', 'N/A')
                print(f"  - {name} ({target})")
                
        except Exception as e:
            print(f"Error fetching {pattern_name}: {e}")

def fetch_assets_by_network_info():
    """Fetch assets by network-related information"""
    print("\n=== Fetching Assets by Network Info ===")
    client = get_client()
    
    network_queries = [
        ("Linux servers", 'os ~ "Linux"'),
        ("Windows servers", 'os ~ "Windows"'),
        ("Internal IP range", 'ipaddress ~ "192.168"'),
        ("Web ports (80, 443)", 'port_number in (80, 443)')
    ]
    
    for query_name, search_query in network_queries:
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=search_query
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{query_name}: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {query_name}: {e}")

def fetch_cloud_assets():
    """Fetch cloud-specific assets"""
    print("\n=== Fetching Cloud Assets ===")
    client = get_client()
    
    cloud_queries = [
        ("AWS assets", 'cloud_type = "AWS"'),
        ("Azure assets", 'cloud_type = "Azure"'),
        ("GCP assets", 'cloud_type = "GCP"'),
        ("US East region", 'region = "us-east-1"'),
        ("US West region", 'region = "us-west-2"')
    ]
    
    for query_name, search_query in cloud_queries:
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=search_query
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{query_name}: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {query_name}: {e}")

def fetch_assets_by_date():
    """Fetch assets by date ranges"""
    print("\n=== Fetching Assets by Date ===")
    client = get_client()
    
    date_queries = [
        ("Created in 2024", 'created >= "2024-01-01"'),
        ("Created in last 6 months", 'created >= "2024-07-01"'),
        ("Recently updated", 'updated >= "2024-11-01"')
    ]
    
    for query_name, search_query in date_queries:
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=search_query
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{query_name}: {len(assets)}")
            
        except Exception as e:
            print(f"Error fetching {query_name}: {e}")

def fetch_assets_complex_queries():
    """Fetch assets using complex combined queries"""
    print("\n=== Complex Combined Queries ===")
    client = get_client()
    
    complex_queries = [
        ("High-risk public web assets", 'type = 1 and risk_score >= 80 and exposed = 2'),
        ("Critical cloud assets", 'type = 4 and sensitivity = 4'),
        ("Production AWS assets", 'cloud_type = "AWS" and name ~ "production"'),
        ("High-risk Linux servers", 'type = 3 and os ~ "Linux" and risk_score >= 70'),
        ("Public assets with high sensitivity", 'exposed = 2 and sensitivity >= 3')
    ]
    
    for query_name, search_query in complex_queries:
        try:
            response = client.execute_query(
                "all_assets",
                organization_id=enums.ORGANIZATION_ID,
                search_query=search_query
            )
            assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
            print(f"{query_name}: {len(assets)}")
            
            # Show details for first asset if available
            if assets:
                asset = assets[0]
                name = asset.get('name', 'Unknown')
                risk = asset.get('risk_score', 'N/A')
                sensitivity = asset.get('sensitivity', 'N/A')
                exposed = asset.get('exposed', 'N/A')
                print(f"  Example: {name} (Risk: {risk}, Sensitivity: {sensitivity}, Exposed: {exposed})")
                
        except Exception as e:
            print(f"Error fetching {query_name}: {e}")

def demonstrate_asset_details():
    """Show detailed information from asset response"""
    print("\n=== Asset Response Details ===")
    try:
        client = get_client()
        response = client.execute_query(
            "all_assets",
            organization_id=enums.ORGANIZATION_ID,
            page_size=1  # Get just one asset for demo
        )
        assets = response.get("data", {}).get("allAssets", {}).get("objects", [])
        
        if assets:
            asset = assets[0]
            print("Sample asset fields:")
            
            # Basic info
            print(f"  ID: {asset.get('id')}")
            print(f"  Name: {asset.get('name')}")
            print(f"  Target: {asset.get('target')}")
            print(f"  Type: {asset.get('type')}")
            
            # Risk & security
            print(f"  Risk Score: {asset.get('risk_score')}")
            print(f"  Sensitivity: {asset.get('sensitivity')}")
            print(f"  Exposed: {asset.get('exposed')}")
            print(f"  Active: {asset.get('isActive')}")
            
            # Technical details
            print(f"  IP Address: {asset.get('ipaddress')}")
            print(f"  Hostname: {asset.get('hostname')}")
            print(f"  OS: {asset.get('os')}")
            
            # Cloud info (if applicable)
            print(f"  Cloud Type: {asset.get('cloud_type')}")
            print(f"  Region: {asset.get('region')}")
            
            # Timestamps
            print(f"  Created: {asset.get('created')}")
            print(f"  Updated: {asset.get('updated')}")
            
        else:
            print("No assets found to demonstrate")
            
    except Exception as e:
        print(f"Error demonstrating asset details: {e}")

def main():
    """Main function to run all asset fetching examples"""
    print("🔍 Strobes Asset Fetching Examples")
    print("=" * 50)
    
    # Uncomment the functions you want to test:
    
    # Basic fetching
    fetch_all_assets()
    
    # Fetching by different criteria
    # fetch_assets_by_type()
    # fetch_assets_by_sensitivity()
    # fetch_assets_by_exposure()
    # fetch_assets_by_risk_score()
    
    # Pattern-based fetching
    # fetch_assets_by_patterns()
    # fetch_assets_by_network_info()
    # fetch_cloud_assets()
    # fetch_assets_by_date()
    
    # Advanced queries
    # fetch_assets_complex_queries()
    
    # Show asset details
    # demonstrate_asset_details()
    
    print("\n✅ Asset fetching examples completed!")
    print("\n💡 Tip: Uncomment different functions in main() to test various scenarios")
    print("📚 For more search options, visit: https://github.com/strobes-co/ql-documentation")

if __name__ == "__main__":
    main()
