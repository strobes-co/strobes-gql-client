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


def asset_exists(asset_name, ip_address, existing_assets):
    """Check if an asset with the same name or IP already exists"""
    for asset in existing_assets:
        # Check by name
        if asset.get('name') == asset_name:
            return True, asset['id']
        # Check by IP address
        if asset.get('ipaddress') == ip_address:
            return True, asset['id']
    return False, None


def create_network_asset_with_single_ip():
    """Create a network asset with a single IP address (avoid duplicates)"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    asset_name = "Network Asset - Single IP"
    ip_address = "192.168.1.100"
    
    # Check if asset already exists
    exists, asset_id = asset_exists(asset_name, ip_address, existing_assets)
    if exists:
        print(f"Asset '{asset_name}' (IP: {ip_address}) already exists with ID: {asset_id}")
        return None
    
    asset_create_fields = {
        "name": asset_name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": 3,  # Medium sensitivity
        "exposed": 1,  # Exposed to internet
        "type": 3,  # Network asset type
        "os": "Linux Ubuntu 20.04",
        "cpe": "cpe:/o:canonical:ubuntu_linux:20.04",
        "hostname": "network-server-01",
        "mac_address": "00:1A:2B:3C:4D:5E",
        "tags": ["network", "server", "ubuntu"],
        "ipaddress": ip_address,
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Network asset '{asset_name}' created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating network asset: {e}")
        return None


def create_network_asset_with_multiple_ips():
    """Create a network asset with multiple IP addresses (avoid duplicates)"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    asset_name = "Network Asset - Multiple IPs"
    ip_addresses = ["192.168.1.200", "192.168.1.201", "192.168.1.202"]
    excluded_ips = ["192.168.1.250"]
    
    # Check which IPs already exist
    existing_ips = []
    new_ips = []
    
    for ip in ip_addresses:
        exists, asset_id = asset_exists(f"IP: {ip}", ip, existing_assets)
        if exists:
            existing_ips.append(ip)
            logger.info(f"Asset with IP {ip} already exists with ID: {asset_id}")
        else:
            new_ips.append(ip)
    
    if not new_ips:
        logger.info(f"All IPs for '{asset_name}' already exist. Skipping creation.")
        return None
    
    logger.info(f"Creating assets for new IPs: {new_ips}")
    
    asset_create_fields = {
        "name": asset_name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": 4,  # High sensitivity
        "exposed": 1,  # Exposed to internet
        "type": 3,  # Network asset type
        "os": "Windows Server 2019",
        "cpe": "cpe:/o:microsoft:windows_server:2019",
        "hostname": "network-cluster-01",
        "mac_address": "00:25:90:67:89:AB",
        "tags": ["network", "cluster", "windows"],
        "ipaddress_list": new_ips,
        "excluded_ipaddress_list": excluded_ips,
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Network asset with multiple IPs created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating network asset with multiple IPs: {e}")
        return None


def create_firewall_asset():
    """Create a firewall network asset (avoid duplicates)"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    asset_name = "Office Firewall"
    ip_address = "10.0.0.1"
    
    # Check if asset already exists
    exists, asset_id = asset_exists(asset_name, ip_address, existing_assets)
    if exists:
        print(f"Asset '{asset_name}' (IP: {ip_address}) already exists with ID: {asset_id}")
        return None
    
    asset_create_fields = {
        "name": asset_name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": 5,  # Critical sensitivity
        "exposed": 1,  # Exposed to internet
        "type": 3,  # Network asset type
        "os": "Cisco ASA",
        "cpe": "cpe:/o:cisco:asa",
        "hostname": "fw-office-main",
        "mac_address": "00:1C:58:29:3A:4B",
        "tags": ["firewall", "network", "security"],
        "ipaddress": ip_address,
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Firewall asset '{asset_name}' created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating firewall asset: {e}")
        return None


def create_custom_network_asset(name, ip_address, os="Linux", hostname=None, sensitivity=3):
    """Create a custom network asset with duplicate checking"""
    client = get_client()
    existing_assets = get_existing_assets()
    
    # Check if asset already exists
    exists, asset_id = asset_exists(name, ip_address, existing_assets)
    if exists:
        logger.info(f"Asset '{name}' (IP: {ip_address}) already exists with ID: {asset_id}")
        return None
    
    asset_create_fields = {
        "name": name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "sensitivity": sensitivity,
        "exposed": 1,  # Exposed to internet
        "type": 3,  # Network asset type
        "os": os,
        "hostname": hostname or f"host-{ip_address.replace('.', '-')}",
        "tags": ["network", "custom"],
        "ipaddress": ip_address,
    }
    
    try:
        result = client.execute_mutation("create_asset", **asset_create_fields)
        logger.info(f"Custom network asset '{name}' created successfully!")
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating custom network asset: {e}")
        return None


if __name__ == "__main__":
    logger.info("Creating network assets (with duplicate checking)...")
    
    
    logger.info("1. Creating network asset with single IP...")
    create_network_asset_with_single_ip()

    logger.info("2. Creating network asset with multiple IPs...")
    create_network_asset_with_multiple_ips()
    
    logger.info("3. Creating firewall asset...")
    create_firewall_asset()
    
    logger.info("Network asset creation completed!") 