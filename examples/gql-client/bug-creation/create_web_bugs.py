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


def fetch_web_assets():
    """Fetch web assets (type 1) from the organization"""
    try:
        client = get_client()
        logger.info("Fetching web assets from organization...")
        
        result = client.execute_query(
            "all_assets",
            organization_id=QUERY_CONFIG["organization_id"],
            search_query="type in (1)",
        )
        
        if result and "data" in result and "allAssets" in result["data"]:
            assets = result["data"]["allAssets"]["objects"]
            
            if len(assets) > 0:
                # Filter for web assets (type 1)
                web_asset_ids = []
                for asset in assets:
                    if 'id' in asset and 'type' in asset and asset['type'] == 1:
                        web_asset_ids.append(int(asset['id']))  # Convert to integer
                
                logger.info(f"Found {len(web_asset_ids)} web assets: {web_asset_ids}")
                return web_asset_ids
            else:
                logger.warning("No web assets found in the organization")
                return []
        else:
            logger.warning("No web assets found in the organization")
            return []
            
    except Exception as e:
        logger.error(f"Error fetching web assets: {str(e)}")
        return []


def create_all_web_bugs():
    """
    Create all web bugs in a single function
    """
    try:
        client = get_client()
        logger.info("Starting web bug creation for all types...")
        
        # Fetch web assets first
        web_asset_ids = fetch_web_assets()
        
        if not web_asset_ids:
            logger.error("No web assets found. Cannot create web bugs without assets.")
            return
        
        logger.info(f"Using web assets: {web_asset_ids}")
        
        # Define all bug configurations
        bugs_config = [
            {
                "title": "Cross-Site Request Forgery (CSRF)",
                "description": "A CSRF vulnerability in the product update form allows attackers to change product details without authorization.",
                "bug_level": 2,
                "mitigation": "Implement anti-CSRF tokens or use the HTTP Strict-Transport-Security (HSTS) header.",
                "steps_to_reproduce": "1. Log into the application as a regular user. 2. Access a malicious website hosting a crafted CSRF payload that targets the product update form. 3. The payload will be submitted without your knowledge, changing product details.",
                "cwe_list": [352],
                "cve_list": [],
                "cvss": 6.5,
                "severity": 2,
                "tags": ["csrf", "web"],
                "bug_attachment_list": [],
                "selected_assets": web_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "web": '{ "affected_endpoints": ["http://vulnerable-website.com/product/update"], "request": "POST /product/update HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nproduct_id=123&name=NewProductName&description=NewDescription", "response": "HTTP/1.1 302 Found\\r\\nLocation: /product/123" }',
                "organization_id": QUERY_CONFIG["organization_id"],
            },
            {
                "title": "Cross-Site Scripting (XSS) in Search Function",
                "description": "Reflected XSS vulnerability in the search functionality allows attackers to inject malicious scripts.",
                "bug_level": 2,
                "mitigation": "Sanitize user input and implement proper output encoding.",
                "steps_to_reproduce": "1. Navigate to the search page. 2. Enter a script payload: <script>alert('XSS')</script>. 3. Submit the search and observe the script execution in the response.",
                "cwe_list": [79],
                "cve_list": [],
                "cvss": 6.1,
                "severity": 2,
                "tags": ["xss", "web", "reflected"],
                "bug_attachment_list": [],
                "selected_assets": web_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "web": '{ "affected_endpoints": ["http://vulnerable-website.com/search"], "request": "GET /search?q=<script>alert(\\"XSS\\")</script> HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\nUser-Agent: Mozilla/5.0", "response": "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n<html><body>Search results for: <script>alert(\\"XSS\\")</script></body></html>" }',
                "organization_id": QUERY_CONFIG["organization_id"],
            },
            {
                "title": "SQL Injection in Login Form",
                "description": "SQL injection vulnerability in the login form allows attackers to bypass authentication.",
                "bug_level": 2,
                "mitigation": "Use parameterized queries and input validation.",
                "steps_to_reproduce": "1. Navigate to the login page. 2. Enter username: admin OR 1=1. 3. Enter any password. 4. Submit the form and observe successful login.",
                "cwe_list": [89],
                "cve_list": [],
                "cvss": 8.5,
                "severity": 3,
                "tags": ["sql-injection", "web", "authentication-bypass"],
                "bug_attachment_list": [],
                "selected_assets": web_asset_ids,
                "engagement_ids": [],
                "custom_fields": "{}",
                "web": '{ "affected_endpoints": ["http://vulnerable-website.com/login"], "request": "POST /login HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nusername=admin OR 1=1&password=test", "response": "HTTP/1.1 302 Found\\r\\nLocation: /dashboard\\r\\nSet-Cookie: session=abc123" }',
                "organization_id": QUERY_CONFIG["organization_id"],
            }
        ]
        
        # Create each bug for each asset
        bug_count = 0
        total_bugs = len(bugs_config) * len(web_asset_ids)
        
        for asset_id in web_asset_ids:
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
        
        logger.info("🎉 All web bugs creation process completed!")
        
    except Exception as e:
        logger.error(f"Error in create_all_web_bugs: {str(e)}")
        raise


if __name__ == "__main__":
    # Execute all web bug creation in a single function
    create_all_web_bugs() 