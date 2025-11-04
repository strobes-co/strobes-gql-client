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


def fetch_code_assets():
    """Fetch code assets (type 7) from the organization"""
    try:
        client = get_client()
        logger.info("Fetching code assets from organization...")
        
        result = client.execute_query(
            "all_assets",
            organization_id=QUERY_CONFIG["organization_id"],
            search_query="type in (7)",
        )
        
        if result and "data" in result and "allAssets" in result["data"]:
            assets = result["data"]["allAssets"]["objects"]
            
            if len(assets) > 0:
                # Filter for code assets (type 7)
                code_asset_ids = []
                for asset in assets:
                    if 'id' in asset and 'type' in asset and asset['type'] == 7:
                        code_asset_ids.append(int(asset['id']))  # Convert to integer
                
                logger.info(f"Found {len(code_asset_ids)} code assets: {code_asset_ids}")
                return code_asset_ids
            else:
                logger.warning("No code assets found in the organization")
                return []
        else:
            logger.warning("No code assets found in the organization")
            return []
            
    except Exception as e:
        logger.error(f"Error fetching code assets: {str(e)}")
        return []


def create_all_code_bugs():
    """
    Create all code bugs in a single function
    """
    try:
        client = get_client()
        logger.info("Starting code bug creation for all types...")
        
        # Fetch code assets first
        code_asset_ids = fetch_code_assets()
        
        if not code_asset_ids:
            logger.error("No code assets found. Cannot create code bugs without assets.")
            return
        
        logger.info(f"Using code assets: {code_asset_ids}")
        
        # Define all bug configurations
        bugs_config = [
    {
        "title": "Command Injection Vulnerability in File Upload Handler",
        "description": "User input in the 'filename' parameter is directly concatenated into a shell command, allowing arbitrary command execution.",
        "organization_id": QUERY_CONFIG["organization_id"],
        "bug_level": 1,
        "mitigation": "Use secure libraries like Python’s `subprocess` with argument lists instead of raw command strings.",
        "steps_to_reproduce": """
            1. Intercept a file upload request.
            2. Modify the 'filename' parameter to include `; whoami`.
            3. Observe the server response or logs showing the command execution result.
        """,
        "code": '{ "vulnerable_code": "os.system(\\"mv uploads/\\" + filename + \\" /archive/\\")", "start_line_number": "78", "end_line_number": "78", "file_name": "utils/upload_handler.py" }',
        "cwe_list": [78],
        "cve_list": [],
        "cvss": 8.6,
        "severity": 4,
        "tags": ["command-injection", "code-vulnerability"],
        "bug_attachment_list": [],
        "selected_assets": code_asset_ids,
        "engagement_ids": [],
        "custom_fields": "{}"
    },
    {
        "title": "Reflected XSS in Search Query Parameter",
        "description": "Improper input sanitization in the search page leads to reflected XSS.",
        "organization_id": QUERY_CONFIG["organization_id"],
        "bug_level": 1,
        "mitigation": "Sanitize and encode user input before reflecting it back in the HTML response.",
        "steps_to_reproduce": """
            1. Go to /search?q=<script>alert(1)</script>
            2. Observe that the script executes in the browser
        """,
        "code": '{ "vulnerable_code": "<div>Search Results for: \\" + user_input + \\"</div>", "start_line_number": "45", "end_line_number": "45", "file_name": "views/search.py" }',
        "cwe_list": [79],
        "cve_list": [],
        "cvss": 6.1,
        "severity": 4,
        "tags": ["xss", "reflected", "unsanitized-input"],
        "bug_attachment_list": [],
        "selected_assets": code_asset_ids,
        "engagement_ids": [],
        "custom_fields": "{}"
    },
    {
        "title": "Insecure Direct Object Reference in User Profile Access",
        "description": "User ID can be changed in the URL to access other users' profiles without authorization.",
        "organization_id": QUERY_CONFIG["organization_id"],
        "bug_level": 1,
        "mitigation": "Implement proper authorization checks before serving user-specific data.",
        "steps_to_reproduce": """
            1. Login as user A and go to /profile/101
            2. Change the URL to /profile/102
            3. Observe that user B's profile is visible
        """,
        "code": '{ "vulnerable_code": "user = db.get_user_by_id(request.params[\\"user_id\\"])", "start_line_number": "88", "end_line_number": "88", "file_name": "controllers/profile.py" }',
        "cwe_list": [639],
        "cve_list": [],
        "cvss": 5.3,
        "severity": 4,
        "tags": ["idor", "authorization", "insecure-access"],
        "bug_attachment_list": [],
        "selected_assets": code_asset_ids,
        "engagement_ids": [],
        "custom_fields": "{}"
    }
]

        
        # Create each bug for each asset
        bug_count = 0
        total_bugs = len(bugs_config) * len(code_asset_ids)
        
        for asset_id in code_asset_ids:
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
        
        logger.info("🎉 All code bugs creation process completed!")
        
    except Exception as e:
        logger.error(f"Error in create_all_code_bugs: {str(e)}")
        raise


if __name__ == "__main__":
    # Execute all code bug creation in a single function
    create_all_code_bugs() 