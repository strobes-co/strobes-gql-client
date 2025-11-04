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


def web_asset_exists(asset_name, url, existing_assets):
    """Check if a web asset with the same name or URL already exists"""
    for asset in existing_assets:
        # Check by name
        if asset.get('name') == asset_name:
            return True, asset['id']
        # Check by URL (target field for web assets)
        if asset.get('target') == url:
            return True, asset['id']
    return False, None


def create_web_application_asset():
    """Create a web application asset (avoid duplicates)"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    asset_name = "E-commerce Web Application"
    url = "https://shop.example.com"
    
    # Check if asset already exists
    exists, asset_id = web_asset_exists(asset_name, url, existing_assets)
    if exists:
        logger.info(f"Web asset '{asset_name}' (URL: {url}) already exists with ID: {asset_id}")
        return None
    
    asset_create_fields = {
        "name": asset_name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": 3,  # Medium sensitivity (default)
        "exposed": 1,  # Exposed to internet
        "type": 1,  # Web asset type
        "url": url,
        "tags": ["web", "ecommerce", "production"],
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Web application asset '{asset_name}' created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating web application asset: {e}")
        return None


def create_api_endpoint_asset():
    """Create an API endpoint asset (avoid duplicates)"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    asset_name = "REST API Service"
    url = "https://api.example.com"
    
    # Check if asset already exists
    exists, asset_id = web_asset_exists(asset_name, url, existing_assets)
    if exists:
        logger.info(f"API asset '{asset_name}' (URL: {url}) already exists with ID: {asset_id}")
        return None
    
    asset_create_fields = {
        "name": asset_name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": 3,  # Medium sensitivity (default)
        "exposed": 1,  # Exposed to internet
        "type": 1,  # Web asset type
        "url": url,
        "tags": ["api", "rest", "backend"],
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"API endpoint asset '{asset_name}' created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating API endpoint asset: {e}")
        return None


def create_custom_web_asset(name, url, sensitivity=3, tags=None):
    """Create a custom web asset with duplicate checking"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Check if asset already exists
    exists, asset_id = web_asset_exists(name, url, existing_assets)
    if exists:
        logger.info(f"Web asset '{name}' (URL: {url}) already exists with ID: {asset_id}")
        return None
    
    if tags is None:
        tags = ["web", "custom"]
    
    asset_create_fields = {
        "name": name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": sensitivity,
        "exposed": 1,  # Exposed to internet
        "type": 1,  # Web asset type
        "url": url,
        "tags": tags,
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Custom web asset '{name}' created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating custom web asset: {e}")
        return None


if __name__ == "__main__":
    logger.info("Creating web assets (with duplicate checking)...")
    
    # Create just two web assets
    logger.info("1. Creating web application asset...")
    create_web_application_asset()
    
    logger.info("2. Creating API endpoint asset...")
    create_api_endpoint_asset()
    
    logger.info("Web asset creation completed!") 