# examples/test-create-assets-example.py
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def get_existing_assets():
    """Get all existing assets to check for duplicates"""
    client = get_client()
    try:
        result = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
        if result and 'data' in result and 'allAssets' in result['data']:
            return result['data']['allAssets']['objects']
        return []
    except Exception as e:
        logger.error(f"Error fetching existing assets: {e}")
        return []

def asset_exists(asset_name, existing_assets):
    """Check if an asset with the same name already exists"""
    for asset in existing_assets:
        if asset.get('name') == asset_name:
            return True, asset['id']
    return False, None

def create_web_asset():
    """Create web application assets"""
    print("\n=== Creating Web Assets ===")
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Web asset examples
    web_assets = [
        {
            "name": "Production Web Application",
            "url": "https://app.example.com",
            "sensitivity": 4,  # Critical
            "exposed": 2,      # Public
            "tags": ["production", "web", "critical"]
        },
        {
            "name": "Staging Web Portal",
            "url": "https://staging.example.com", 
            "sensitivity": 2,  # Medium
            "exposed": 1,      # Private
            "tags": ["staging", "web", "portal"]
        },
        {
            "name": "Company Website",
            "url": "https://www.example.com",
            "sensitivity": 1,  # Low
            "exposed": 2,      # Public
            "tags": ["website", "marketing", "public"]
        }
    ]
    
    for web_asset in web_assets:
        try:
            # Check for duplicates
            exists, asset_id = asset_exists(web_asset["name"], existing_assets)
            if exists:
                logger.info(f"Web asset '{web_asset['name']}' already exists with ID: {asset_id}")
                continue
            
            # Required fields for web assets
            asset_fields = {
                "name": web_asset["name"],                    # Required: Asset name
                "organization_id": enums.ORGANIZATION_ID,     # Required: Organization ID
                "type": 1,                                    # Required: Asset type (1=Web)
                "url": web_asset["url"],                     # Required: Web asset URL
                "sensitivity": web_asset["sensitivity"],      # Required: Sensitivity (1=Low, 2=Medium, 3=High, 4=Critical)
                "exposed": web_asset["exposed"],              # Required: Exposure (1=Private, 2=Public)
                "tags": web_asset["tags"]                     # Optional: Tags for categorization
            }
            
            result = client.execute_mutation("create_asset", **asset_fields)
            logger.info(f"Web asset '{web_asset['name']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating web asset '{web_asset['name']}': {e}")

def create_network_assets():
    """Create network device and server assets"""
    print("\n=== Creating Network Assets ===")
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Network asset examples
    network_assets = [
        {
            "name": "Production Database Server",
            "ipaddress": "192.168.1.100",
            "hostname": "prod-db-01",
            "os": "Ubuntu 20.04 LTS",
            "sensitivity": 4,  # Critical
            "exposed": 1,      # Private
            "tags": ["database", "production", "mysql"]
        },
        {
            "name": "Web Server Cluster",
            "ipaddress": "10.0.1.50",
            "hostname": "web-cluster-01",
            "os": "CentOS 8",
            "sensitivity": 3,  # High
            "exposed": 2,      # Public
            "tags": ["webserver", "nginx", "cluster"]
        },
        {
            "name": "Network Router",
            "ipaddress": "192.168.1.1",
            "hostname": "core-router-01",
            "sensitivity": 3,  # High
            "exposed": 1,      # Private
            "tags": ["router", "network", "infrastructure"]
        }
    ]
    
    for network_asset in network_assets:
        try:
            # Check for duplicates
            exists, asset_id = asset_exists(network_asset["name"], existing_assets)
            if exists:
                logger.info(f"Network asset '{network_asset['name']}' already exists with ID: {asset_id}")
                continue
            
            # Required fields for network assets
            asset_fields = {
                "name": network_asset["name"],                # Required: Asset name
                "organization_id": enums.ORGANIZATION_ID,     # Required: Organization ID
                "type": 3,                                    # Required: Asset type (3=Network)
                "ipaddress": network_asset["ipaddress"],     # Required: IP address (or ipaddress_list for multiple)
                "sensitivity": network_asset["sensitivity"],  # Required: Sensitivity level
                "exposed": network_asset["exposed"],          # Required: Exposure level
                "hostname": network_asset.get("hostname"),    # Optional: Hostname
                "os": network_asset.get("os"),               # Optional: Operating system
                "tags": network_asset["tags"]                # Optional: Tags
            }
            
            # Remove None values
            asset_fields = {k: v for k, v in asset_fields.items() if v is not None}
            
            result = client.execute_mutation("create_asset", **asset_fields)
            logger.info(f"Network asset '{network_asset['name']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating network asset '{network_asset['name']}': {e}")

def create_cloud_assets():
    """Create cloud resource assets"""
    print("\n=== Creating Cloud Assets ===")
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Cloud asset examples
    cloud_assets = [
        {
            "name": "AWS Production EC2 Instance",
            "cloud_type": 2,       # AWS
            "sensitivity": 4,      # Critical
            "exposed": 2,          # Public
            "tags": ["aws", "ec2", "production"]
        },
        {
            "name": "Azure Storage Account",
            "cloud_type": 3,       # Azure
            "sensitivity": 3,      # High
            "exposed": 1,          # Private
            "tags": ["azure", "storage", "data"]
        },
        {
            "name": "GCP Kubernetes Cluster",
            "cloud_type": 4,       # GCP
            "sensitivity": 4,      # Critical
            "exposed": 2,          # Public
            "tags": ["gcp", "kubernetes", "cluster"]
        }
    ]
    
    for cloud_asset in cloud_assets:
        try:
            # Check for duplicates
            exists, asset_id = asset_exists(cloud_asset["name"], existing_assets)
            if exists:
                logger.info(f"Cloud asset '{cloud_asset['name']}' already exists with ID: {asset_id}")
                continue
            
            # Required fields for cloud assets
            asset_fields = {
                "name": cloud_asset["name"],                  # Required: Asset name
                "organization_id": enums.ORGANIZATION_ID,     # Required: Organization ID
                "type": 4,                                    # Required: Asset type (4=Cloud)
                "cloud_type": cloud_asset["cloud_type"],     # Required: Cloud provider (1=Other, 2=AWS, 3=Azure, 4=GCP)
                "sensitivity": cloud_asset["sensitivity"],    # Required: Sensitivity level
                "exposed": cloud_asset["exposed"],            # Required: Exposure level
                "tags": cloud_asset["tags"]                  # Optional: Tags
            }
            
            result = client.execute_mutation("create_asset", **asset_fields)
            logger.info(f"Cloud asset '{cloud_asset['name']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating cloud asset '{cloud_asset['name']}': {e}")

def create_mobile_assets():
    """Create mobile application assets"""
    print("\n=== Creating Mobile Assets ===")
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Mobile asset examples
    mobile_assets = [
        {
            "name": "Banking Mobile App (iOS)",
            "package": "com.company.banking.ios",
            "sensitivity": 4,  # Critical
            "exposed": 2,      # Public
            "tags": ["mobile", "banking", "ios", "finance"]
        },
        {
            "name": "Banking Mobile App (Android)",
            "package": "com.company.banking.android",
            "sensitivity": 4,  # Critical
            "exposed": 2,      # Public
            "tags": ["mobile", "banking", "android", "finance"]
        },
        {
            "name": "Internal HR Mobile App",
            "package": "com.company.hr.internal",
            "sensitivity": 3,  # High
            "exposed": 1,      # Private
            "tags": ["mobile", "hr", "internal", "employee"]
        }
    ]
    
    for mobile_asset in mobile_assets:
        try:
            # Check for duplicates
            exists, asset_id = asset_exists(mobile_asset["name"], existing_assets)
            if exists:
                logger.info(f"Mobile asset '{mobile_asset['name']}' already exists with ID: {asset_id}")
                continue
            
            # Required fields for mobile assets
            asset_fields = {
                "name": mobile_asset["name"],                 # Required: Asset name
                "organization_id": enums.ORGANIZATION_ID,     # Required: Organization ID
                "type": 2,                                    # Required: Asset type (2=Mobile)
                "package": mobile_asset["package"],          # Required: Package name or bundle ID
                "sensitivity": mobile_asset["sensitivity"],   # Required: Sensitivity level
                "exposed": mobile_asset["exposed"],           # Required: Exposure level
                "tags": mobile_asset["tags"]                 # Optional: Tags
            }
            
            result = client.execute_mutation("create_asset", **asset_fields)
            logger.info(f"Mobile asset '{mobile_asset['name']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating mobile asset '{mobile_asset['name']}': {e}")

def create_code_repository_assets():
    """Create code repository assets"""
    print("\n=== Creating Code Repository Assets ===")
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Code repository asset examples
    code_assets = [
        {
            "name": "Main Web Application Repository",
            "url": "https://github.com/company/web-app",
            "sensitivity": 4,  # Critical
            "exposed": 1,      # Private
            "tags": ["code", "repository", "web", "production"]
        },
        {
            "name": "Mobile App Codebase",
            "url": "https://github.com/company/mobile-app",
            "sensitivity": 3,  # High
            "exposed": 1,      # Private
            "tags": ["code", "mobile", "react-native"]
        },
        {
            "name": "Microservices Repository",
            "url": "https://github.com/company/microservices",
            "sensitivity": 4,  # Critical
            "exposed": 1,      # Private
            "tags": ["code", "microservices", "golang", "api"]
        }
    ]
    
    for code_asset in code_assets:
        try:
            # Check for duplicates
            exists, asset_id = asset_exists(code_asset["name"], existing_assets)
            if exists:
                logger.info(f"Code asset '{code_asset['name']}' already exists with ID: {asset_id}")
                continue
            
            # Required fields for code repository assets
            asset_fields = {
                "name": code_asset["name"],                   # Required: Asset name
                "organization_id": enums.ORGANIZATION_ID,     # Required: Organization ID
                "type": 7,                                    # Required: Asset type (7=Code repository)
                "url": code_asset["url"],                    # Required: Repository URL
                "sensitivity": code_asset["sensitivity"],     # Required: Sensitivity level
                "exposed": code_asset["exposed"],             # Required: Exposure level
                "tags": code_asset["tags"]                   # Optional: Tags
            }
            
            result = client.execute_mutation("create_asset", **asset_fields)
            logger.info(f"Code repository asset '{code_asset['name']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating code asset '{code_asset['name']}': {e}")

def demonstrate_field_requirements():
    """Show examples of required and optional fields for each asset type"""
    print("\n=== Field Requirements by Asset Type ===")
    
    print("\n** All Asset Types (Common Requirements) **")
    print("- name (String): Descriptive asset name")
    print("- organization_id (UUID): Your organization identifier")
    print("- type (Int): Asset type (1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code)")
    print("- sensitivity (Int): Sensitivity level (1=Low, 2=Medium, 3=High, 4=Critical)")
    print("- exposed (Int): Exposure level (1=Private, 2=Public)")
    
    print("\n** Web Assets (type=1) **")
    print("Required: url (String) - Web application URL")
    print("Example: 'https://app.example.com'")
    
    print("\n** Mobile Assets (type=2) **")
    print("Required: package (String) - Package name or bundle identifier")
    print("Example: 'com.company.banking' or 'com.company.banking.ios'")
    
    print("\n** Network Assets (type=3) **")
    print("Required: ipaddress (String) OR ipaddress_list (Array) - IP address(es)")
    print("Optional: hostname, os, mac_address, cpe")
    print("Example: ipaddress='192.168.1.100', hostname='server-01'")
    
    print("\n** Cloud Assets (type=4) **")
    print("Required: cloud_type (Int) - Cloud provider (1=Other, 2=AWS, 3=Azure, 4=GCP)")
    print("Optional: region, account_id, resource_id")
    print("Example: cloud_type=2 (AWS), region='us-east-1'")
    
    print("\n** Code Repository Assets (type=7) **")
    print("Required: url (String) - Repository URL")
    print("Example: 'https://github.com/company/repository'")
    
    print("\n** Sensitivity Levels **")
    print("1 = Low sensitivity")
    print("2 = Medium sensitivity") 
    print("3 = High sensitivity")
    print("4 = Critical sensitivity")
    
    print("\n** Exposure Levels **")
    print("1 = Private (internal access only)")
    print("2 = Public (accessible from internet)")

def main():
    """Main function to demonstrate asset creation"""
    print("🔧 Strobes Asset Creation Examples")
    print("=" * 50)
    
    # Uncomment the functions you want to test:
    
    # Show field requirements
    demonstrate_field_requirements()
    
    # Create different types of assets
    # create_web_asset()
    # create_network_assets()
    create_cloud_assets()
    # create_mobile_assets()
    # create_code_repository_assets()
    
    print("\n✅ Asset creation examples completed!")
    print("\n💡 Tip: Uncomment different functions in main() to test various asset types")
    print("📚 For more field options, visit: https://github.com/strobes-co/ql-documentation")

if __name__ == "__main__":
    main()
