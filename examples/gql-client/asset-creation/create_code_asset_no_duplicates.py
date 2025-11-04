import logging
import sys
import os
from strobes_gql_client.client import StrobesGQLClient

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CONNECTION_CONFIG, QUERY_CONFIG

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def get_client():
    return StrobesGQLClient(**CONNECTION_CONFIG)


def get_existing_assets():
    """Get all existing assets to check for duplicates"""
    client = get_client()
    try:
        result = client.execute_query("all_assets", organization_id=QUERY_CONFIG["organization_id"])
        if result and 'data' in result and 'allAssets' in result['data']:
            return result['data']['allAssets']['objects']
        return []
    except Exception as e:
        logger.error(f"Error fetching existing assets: {e}")
        return []


def code_asset_exists(asset_name, repository_url, existing_assets):
    """Check if a code asset with the same name or repository URL already exists"""
    for asset in existing_assets:
        # Check by name
        if asset.get('name') == asset_name:
            return True, asset['id']
        # Check by repository URL (target field for code assets)
        if asset.get('target') == repository_url:
            return True, asset['id']
    return False, None


def create_custom_code_asset(name, repository_url, language="Python", sensitivity=3, tags=None):
    """Create a custom code asset with duplicate checking"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Check if asset already exists
    exists, asset_id = code_asset_exists(name, repository_url, existing_assets)
    if exists:
        logger.info(f"Code asset '{name}' (Repo: {repository_url}) already exists with ID: {asset_id}")
        return None
    
    if tags is None:
        tags = ["code", "custom", language.lower()]
    
    asset_create_fields = {
        "name": name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": sensitivity,
        "exposed": 1,  # Exposed to internet
        "type": 7,  # Code asset type
        "url": repository_url,
        "tags": tags,
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Custom code asset '{name}' created successfully with type 7 and sensitivity {sensitivity}!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating custom code asset: {e}")
        return None


if __name__ == "__main__":
    logger.info("Creating new code assets with type 7...")
    
    # Create new code assets with type 7
    logger.info("1. Creating mobile app code asset...")
    create_custom_code_asset("Mobile App Codebase", "https://github.com/company/mobile-app", "React Native", tags=["code", "mobile", "react-native"])
    
    logger.info("2. Creating microservice code asset...")
    create_custom_code_asset("Microservice Codebase", "https://github.com/company/microservice", "Go", sensitivity=4, tags=["code", "microservice", "go"])
    
    logger.info("Code asset creation completed!") 