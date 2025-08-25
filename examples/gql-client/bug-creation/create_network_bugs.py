from strobes_gql_client.client import StrobesGQLClient
import logging
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CONNECTION_CONFIG, QUERY_CONFIG

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_client():
    return StrobesGQLClient(**CONNECTION_CONFIG)


def fetch_network_assets():
    """Fetch network assets (type 3) from the organization"""
    try:
        client = get_client()
        logger.info("Fetching network assets from organization...")
        
        result = client.execute_query(
            "all_assets",
            organization_id=QUERY_CONFIG["organization_id"],
            search_query="type in (3)",
        )
        
        if result and "data" in result and "allAssets" in result["data"]:
            assets = result["data"]["allAssets"]["objects"]
            
            if len(assets) > 0:
                # Filter for network assets (type 3)
                network_asset_ids = []
                for asset in assets:
                    if 'id' in asset and 'type' in asset and asset['type'] == 3:
                        network_asset_ids.append(int(asset['id']))  # Convert to integer
                
                logger.info(f"Found {len(network_asset_ids)} network assets: {network_asset_ids}")
                return network_asset_ids
            else:
                logger.warning("No network assets found in the organization")
                return []
        else:
            logger.warning("No network assets found in the organization")
            return []
            
    except Exception as e:
        logger.error(f"Error fetching network assets: {str(e)}")
        return []


def create_all_network_bugs():
    """
    Create all network bugs in a single function
    """
    try:
        client = get_client()
        logger.info("Starting network bug creation for all types...")
        
        # Fetch network assets first
        network_asset_ids = fetch_network_assets()
        
        if not network_asset_ids:
            logger.error("No network assets found. Cannot create network bugs without assets.")
            return
        
        logger.info(f"Using network assets: {network_asset_ids}")
        
        # Define all bug configurations
        bugs_config = [
            {
                "title": "Open SSH Port (22) Exposed to Internet",
                "description": "SSH port 22 is open and accessible from the internet, which increases the attack surface and risk of brute force attacks.",
                "bug_level": 4,
                "mitigation": "Implement firewall rules to restrict SSH access to specific IP ranges, use SSH key-based authentication, and consider using non-standard ports.",
                "steps_to_reproduce": "1. Use nmap to scan the target IP address: nmap -p 22 target_ip. 2. Verify SSH service is running: telnet target_ip 22. 3. Confirm the port is accessible from external networks.",
                "cwe_list": [200],
                "cve_list": [],
                "cvss": 5.3,
                "severity": 3,
                "tags": ["network", "ssh", "port-scanning", "exposed-services"],
                "bug_attachment_list": [],
                "selected_assets": network_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "network": '{ "port": "22", "cpe": ["cpe:/a:openssh:openssh:8.2p1"] }',
                "organization_id": QUERY_CONFIG["organization_id"],
            },
            {
                "title": "Weak SNMP Community String",
                "description": "SNMP is configured with default or weak community strings, allowing unauthorized access to network device information.",
                "bug_level": 4,
                "mitigation": "Change default community strings to strong, unique values. Implement SNMPv3 with authentication and encryption. Restrict SNMP access to specific IP addresses.",
                "steps_to_reproduce": "1. Use snmpwalk to test default community strings: snmpwalk -v2c -c public target_ip. 2. Try common community strings like 'private', 'community', 'cisco'. 3. Verify successful information retrieval.",
                "cwe_list": [1188],
                "cve_list": [],
                "cvss": 6.5,
                "severity": 3,
                "tags": ["network", "snmp", "weak-authentication", "default-credentials"],
                "bug_attachment_list": [],
                "selected_assets": network_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "network": '{ "port": "161", "cpe": ["cpe:/a:ietf:snmp:2.0"] }',
                "organization_id": QUERY_CONFIG["organization_id"],
            },
            {
                "title": "Telnet Service Enabled",
                "description": "Telnet service is enabled and accessible, which transmits data in cleartext and is considered insecure for network administration.",
                "bug_level": 4,
                "mitigation": "Disable Telnet service and replace with SSH for secure remote access. If Telnet is required, restrict access to specific IP addresses and implement network segmentation.",
                "steps_to_reproduce": "1. Scan for Telnet port: nmap -p 23 target_ip. 2. Attempt Telnet connection: telnet target_ip 23. 3. Verify service responds and accepts connections.",
                "cwe_list": [319],
                "cve_list": [],
                "cvss": 7.5,
                "severity": 4,
                "tags": ["network", "telnet", "cleartext-transmission", "insecure-protocol"],
                "bug_attachment_list": [],
                "selected_assets": network_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "network": '{ "port": "23", "cpe": ["cpe:/a:ietf:telnet:1.0"] }',
                "organization_id": QUERY_CONFIG["organization_id"],
            },
            {
                "title": "FTP Anonymous Access Enabled",
                "description": "FTP server allows anonymous access, potentially exposing sensitive files and directory structures to unauthorized users.",
                "bug_level": 4,
                "mitigation": "Disable anonymous FTP access. Implement proper user authentication. Consider using SFTP or FTPS for secure file transfers. Restrict access to specific IP addresses.",
                "steps_to_reproduce": "1. Connect to FTP server: ftp target_ip. 2. Use 'anonymous' as username and any email as password. 3. Verify successful login and directory listing access.",
                "cwe_list": [552],
                "cve_list": [],
                "cvss": 5.0,
                "severity": 3,
                "tags": ["network", "ftp", "anonymous-access", "file-exposure"],
                "bug_attachment_list": [],
                "selected_assets": network_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "network": '{ "port": "21", "cpe": ["cpe:/a:ietf:ftp:1.0"] }',
                "organization_id": QUERY_CONFIG["organization_id"],
            },
            {
                "title": "Outdated Network Device Firmware",
                "description": "Network device is running outdated firmware version that contains known security vulnerabilities and lacks recent security patches.",
                "bug_level": 4,
                "mitigation": "Update device firmware to the latest stable version. Implement a regular firmware update schedule. Monitor vendor security advisories for critical patches.",
                "steps_to_reproduce": "1. Access device management interface. 2. Check current firmware version in system information. 3. Compare with latest available version from vendor.",
                "cwe_list": [754],
                "cve_list": [],
                "cvss": 6.8,
                "severity": 3,
                "tags": ["network", "firmware", "outdated-software", "security-patches"],
                "bug_attachment_list": [],
                "selected_assets": network_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "network": '{ "port": "80", "cpe": ["cpe:/h:cisco:router:ios:15.0"] }',
                "organization_id": QUERY_CONFIG["organization_id"],
            }
        ]
        
        # Create each bug for each asset
        bug_count = 0
        total_bugs = len(bugs_config) * len(network_asset_ids)
        
        for asset_id in network_asset_ids:
            for i, bug_config in enumerate(bugs_config, 1):
                bug_count += 1
                logger.info(f"Creating bug {bug_count}/{total_bugs}: {bug_config['title']} for asset {asset_id}")
                
                # Create a copy of the bug config with single asset ID
                single_asset_bug_config = bug_config.copy()
                single_asset_bug_config['selected_assets'] = [asset_id]
                
                try:
                    result = client.execute_mutation("bug_create", **single_asset_bug_config)
                    logger.info(f"✅ Bug {bug_count} created successfully for asset {asset_id}!")
                    logger.info(f"Result: {result}")
                except Exception as e:
                    logger.error(f"❌ Error creating bug {bug_count} for asset {asset_id}: {str(e)}")
                    # Continue with next bug even if one fails
                    continue
        
        logger.info("🎉 All network bugs creation process completed!")
        
    except Exception as e:
        logger.error(f"Error in create_all_network_bugs: {str(e)}")
        raise


if __name__ == "__main__":
    # Execute all network bug creation in a single function
    create_all_network_bugs() 