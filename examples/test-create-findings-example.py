# examples/test-create-findings-example.py
"""
Strobes Finding Creation Examples

This example demonstrates comprehensive security finding (vulnerability) creation
for the Strobes platform with robust error handling and comprehensive examples.

Key Features:
- Web, Network, and Code finding creation examples
- Asset fetching to associate findings with appropriate assets
- Comprehensive field documentation and validation
- Duplicate checking to prevent redundant findings
- Professional logging and error handling

Finding Types Supported:
- Web findings (bug_level=2): XSS, SQL injection, CSRF, etc.
- Network findings (bug_level=4): Open ports, weak protocols, misconfigurations
- Code findings (bug_level=1): Command injection, insecure code patterns

Usage:
    python examples/test-create-findings-example.py

Note: Findings require existing assets to be associated with. The script will
automatically fetch appropriate assets for each finding type.
"""

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def fetch_assets_by_type(asset_type):
    """
    Fetch assets of a specific type for associating with findings
    
    Args:
        asset_type (int): Asset type (1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code)
    
    Returns:
        list: List of asset IDs
    """
    try:
        client = get_client()
        logger.info(f"Fetching assets of type {asset_type}...")
        
        result = client.execute_query(
            "all_assets",
            organization_id=enums.ORGANIZATION_ID,
            search_query=f"type = {asset_type}"
        )
        
        if result and "data" in result and "allAssets" in result["data"]:
            assets = result["data"]["allAssets"]["objects"]
            
            asset_ids = []
            for asset in assets:
                if 'id' in asset and 'type' in asset and asset['type'] == asset_type:
                    asset_ids.append(int(asset['id']))
            
            logger.info(f"Found {len(asset_ids)} assets of type {asset_type}: {asset_ids}")
            return asset_ids
        else:
            logger.warning(f"No assets of type {asset_type} found")
            return []
            
    except Exception as e:
        logger.error(f"Error fetching assets of type {asset_type}: {str(e)}")
        return []

def get_existing_findings():
    """Get all existing findings to check for duplicates"""
    try:
        client = get_client()
        result = client.execute_query("all_bugs", organization_id=enums.ORGANIZATION_ID)
        if result and 'data' in result and 'allBugs' in result['data']:
            return result['data']['allBugs']['objects']
        return []
    except Exception as e:
        logger.error(f"Error fetching existing findings: {e}")
        return []

def finding_exists(finding_title, existing_findings):
    """Check if a finding with the same title already exists"""
    for finding in existing_findings:
        if finding.get('title') == finding_title:
            return True, finding['id']
    return False, None

def create_web_findings():
    """Create web application security findings"""
    print("\n=== Creating Web Findings ===")
    client = get_client()
    existing_findings = get_existing_findings()
    
    # Get web assets (type 1)
    web_asset_ids = fetch_assets_by_type(1)
    if not web_asset_ids:
        logger.error("No web assets found. Cannot create web findings without assets.")
        return
    
    # Web finding examples
    web_findings = [
        {
            "title": "Cross-Site Scripting (XSS) in Search Function",
            "description": "Reflected XSS vulnerability in the search functionality allows attackers to inject malicious scripts that execute in users' browsers.",
            "bug_level": 2,  # Web finding
            "mitigation": "Sanitize user input and implement proper output encoding. Use Content Security Policy (CSP) headers.",
            "steps_to_reproduce": "1. Navigate to the search page. 2. Enter script payload: <script>alert('XSS')</script>. 3. Submit the search and observe script execution in the response.",
            "cwe_list": [79],  # CWE-79: Cross-site Scripting
            "cve_list": [],
            "cvss": 6.1,
            "severity": 3,  # Medium
            "tags": ["xss", "web", "reflected", "input-validation"],
            "web": '{"affected_endpoints": ["http://example.com/search"], "request": "GET /search?q=<script>alert(\\"XSS\\")</script> HTTP/1.1\\r\\nHost: example.com", "response": "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n<html><body>Search results for: <script>alert(\\"XSS\\")</script></body></html>"}',
            "custom_fields": "{}"
        },
        {
            "title": "SQL Injection in Login Form",
            "description": "SQL injection vulnerability in the login form allows attackers to bypass authentication and potentially access sensitive database information.",
            "bug_level": 2,  # Web finding
            "mitigation": "Use parameterized queries/prepared statements and implement proper input validation. Apply principle of least privilege to database accounts.",
            "steps_to_reproduce": "1. Navigate to the login page. 2. Enter username: admin' OR '1'='1. 3. Enter any password. 4. Submit the form and observe successful authentication bypass.",
            "cwe_list": [89],  # CWE-89: SQL Injection
            "cve_list": [],
            "cvss": 8.5,
            "severity": 4,  # High
            "tags": ["sql-injection", "web", "authentication-bypass", "database"],
            "web": '{"affected_endpoints": ["http://example.com/login"], "request": "POST /login HTTP/1.1\\r\\nHost: example.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nusername=admin\' OR \'1\'=\'1&password=test", "response": "HTTP/1.1 302 Found\\r\\nLocation: /dashboard\\r\\nSet-Cookie: session=abc123"}',
            "custom_fields": "{}"
        },
        {
            "title": "Cross-Site Request Forgery (CSRF) in Profile Update",
            "description": "CSRF vulnerability in the profile update functionality allows attackers to modify user profiles without proper authorization.",
            "bug_level": 2,  # Web finding
            "mitigation": "Implement anti-CSRF tokens, verify HTTP Referer header, and use SameSite cookie attributes.",
            "steps_to_reproduce": "1. Log into the application as a user. 2. Visit a malicious website with a crafted CSRF payload targeting the profile update form. 3. Observe unauthorized profile changes.",
            "cwe_list": [352],  # CWE-352: Cross-Site Request Forgery
            "cve_list": [],
            "cvss": 6.5,
            "severity": 3,  # Medium
            "tags": ["csrf", "web", "authorization", "state-changing"],
            "web": '{"affected_endpoints": ["http://example.com/profile/update"], "request": "POST /profile/update HTTP/1.1\\r\\nHost: example.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nname=AttackerName&email=attacker@evil.com", "response": "HTTP/1.1 302 Found\\r\\nLocation: /profile"}',
            "custom_fields": "{}"
        }
    ]
    
    for web_finding in web_findings:
        try:
            # Check for duplicates
            exists, finding_id = finding_exists(web_finding["title"], existing_findings)
            if exists:
                logger.info(f"Web finding '{web_finding['title']}' already exists with ID: {finding_id}")
                continue
            
            # Add required common fields
            finding_fields = {
                "title": web_finding["title"],                      # Required
                "description": web_finding["description"],          # Required
                "organization_id": enums.ORGANIZATION_ID,           # Required
                "bug_level": web_finding["bug_level"],             # Required
                "mitigation": web_finding["mitigation"],            # Required
                "steps_to_reproduce": web_finding["steps_to_reproduce"],  # Required
                "cwe_list": web_finding["cwe_list"],               # Optional
                "cve_list": web_finding["cve_list"],               # Optional
                "cvss": web_finding["cvss"],                       # Optional
                "severity": web_finding["severity"],               # Required
                "tags": web_finding["tags"],                       # Optional
                "selected_assets": web_asset_ids,                  # Required
                "web": web_finding["web"],                         # Required for web findings
                "bug_attachment_list": [],                         # Optional
                "engagement_ids": [],                              # Optional
                "custom_fields": web_finding["custom_fields"]     # Optional
            }
            
            result = client.execute_mutation("bug_create", **finding_fields)
            logger.info(f"Web finding '{web_finding['title']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating web finding '{web_finding['title']}': {e}")

def create_network_findings():
    """Create network security findings"""
    print("\n=== Creating Network Findings ===")
    client = get_client()
    existing_findings = get_existing_findings()
    
    # Get network assets (type 3)
    network_asset_ids = fetch_assets_by_type(3)
    if not network_asset_ids:
        logger.error("No network assets found. Cannot create network findings without assets.")
        return
    
    # Network finding examples
    network_findings = [
        {
            "title": "Open SSH Port (22) Exposed to Internet",
            "description": "SSH port 22 is open and accessible from the internet, which increases the attack surface and risk of brute force attacks.",
            "bug_level": 4,  # Network finding
            "mitigation": "Implement firewall rules to restrict SSH access to specific IP ranges, use SSH key-based authentication, and consider using non-standard ports.",
            "steps_to_reproduce": "1. Use nmap to scan the target IP address: nmap -p 22 target_ip. 2. Verify SSH service is running: telnet target_ip 22. 3. Confirm the port is accessible from external networks.",
            "cwe_list": [200],  # CWE-200: Information Exposure
            "cve_list": [],
            "cvss": 5.3,
            "severity": 3,  # Medium
            "tags": ["network", "ssh", "port-scanning", "exposed-services"],
            "network": '{"port": "22", "cpe": ["cpe:/a:openssh:openssh:8.2p1"]}',
            "custom_fields": "{}"
        },
        {
            "title": "Weak SNMP Community String",
            "description": "SNMP is configured with default or weak community strings, allowing unauthorized access to network device information.",
            "bug_level": 4,  # Network finding
            "mitigation": "Change default community strings to strong, unique values. Implement SNMPv3 with authentication and encryption. Restrict SNMP access to specific IP addresses.",
            "steps_to_reproduce": "1. Use snmpwalk to test default community strings: snmpwalk -v2c -c public target_ip. 2. Try common community strings like 'private', 'community', 'cisco'. 3. Verify successful information retrieval.",
            "cwe_list": [1188],  # CWE-1188: Insecure Default Initialization
            "cve_list": [],
            "cvss": 6.5,
            "severity": 3,  # Medium
            "tags": ["network", "snmp", "weak-authentication", "default-credentials"],
            "network": '{"port": "161", "cpe": ["cpe:/a:ietf:snmp:2.0"]}',
            "custom_fields": "{}"
        },
        {
            "title": "Telnet Service Enabled",
            "description": "Telnet service is enabled and accessible, which transmits data in cleartext and is considered insecure for network administration.",
            "bug_level": 4,  # Network finding
            "mitigation": "Disable Telnet service and replace with SSH for secure remote access. If Telnet is required, restrict access to specific IP addresses and implement network segmentation.",
            "steps_to_reproduce": "1. Scan for Telnet port: nmap -p 23 target_ip. 2. Attempt Telnet connection: telnet target_ip 23. 3. Verify service responds and accepts connections.",
            "cwe_list": [319],  # CWE-319: Cleartext Transmission
            "cve_list": [],
            "cvss": 7.5,
            "severity": 4,  # High
            "tags": ["network", "telnet", "cleartext-transmission", "insecure-protocol"],
            "network": '{"port": "23", "cpe": ["cpe:/a:ietf:telnet:1.0"]}',
            "custom_fields": "{}"
        }
    ]
    
    for network_finding in network_findings:
        try:
            # Check for duplicates
            exists, finding_id = finding_exists(network_finding["title"], existing_findings)
            if exists:
                logger.info(f"Network finding '{network_finding['title']}' already exists with ID: {finding_id}")
                continue
            
            # Add required common fields
            finding_fields = {
                "title": network_finding["title"],                  # Required
                "description": network_finding["description"],      # Required
                "organization_id": enums.ORGANIZATION_ID,           # Required
                "bug_level": network_finding["bug_level"],         # Required
                "mitigation": network_finding["mitigation"],        # Required
                "steps_to_reproduce": network_finding["steps_to_reproduce"],  # Required
                "cwe_list": network_finding["cwe_list"],           # Optional
                "cve_list": network_finding["cve_list"],           # Optional
                "cvss": network_finding["cvss"],                   # Optional
                "severity": network_finding["severity"],           # Required
                "tags": network_finding["tags"],                   # Optional
                "selected_assets": network_asset_ids,              # Required
                "network": network_finding["network"],             # Required for network findings
                "bug_attachment_list": [],                         # Optional
                "engagement_ids": [],                              # Optional
                "custom_fields": network_finding["custom_fields"] # Optional
            }
            
            result = client.execute_mutation("bug_create", **finding_fields)
            logger.info(f"Network finding '{network_finding['title']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating network finding '{network_finding['title']}': {e}")

def create_code_findings():
    """Create code security findings"""
    print("\n=== Creating Code Findings ===")
    client = get_client()
    existing_findings = get_existing_findings()
    
    # Get code assets (type 7)
    code_asset_ids = fetch_assets_by_type(7)
    if not code_asset_ids:
        logger.error("No code assets found. Cannot create code findings without assets.")
        return
    
    # Code finding examples
    code_findings = [
        {
            "title": "Command Injection Vulnerability in File Upload Handler",
            "description": "User input in the 'filename' parameter is directly concatenated into a shell command, allowing arbitrary command execution on the server.",
            "bug_level": 1,  # Code finding
            "mitigation": "Use secure libraries like Python's subprocess with argument lists instead of raw command strings. Implement proper input validation and sanitization.",
            "steps_to_reproduce": "1. Intercept a file upload request. 2. Modify the 'filename' parameter to include `; whoami`. 3. Observe the server response or logs showing the command execution result.",
            "cwe_list": [78],  # CWE-78: OS Command Injection
            "cve_list": [],
            "cvss": 8.6,
            "severity": 4,  # High
            "tags": ["command-injection", "code-vulnerability", "file-upload", "rce"],
            "code": '{"vulnerable_code": "os.system(\\"mv uploads/\\" + filename + \\" /archive/\\")", "start_line_number": "78", "end_line_number": "78", "file_name": "utils/upload_handler.py"}',
            "custom_fields": "{}"
        },
        {
            "title": "Reflected XSS in Search Query Parameter",
            "description": "Improper input sanitization in the search page leads to reflected XSS vulnerability, allowing attackers to inject malicious scripts.",
            "bug_level": 1,  # Code finding
            "mitigation": "Sanitize and encode user input before reflecting it back in the HTML response. Use template engines with auto-escaping enabled.",
            "steps_to_reproduce": "1. Go to /search?q=<script>alert(1)</script>. 2. Observe that the script executes in the browser.",
            "cwe_list": [79],  # CWE-79: Cross-site Scripting
            "cve_list": [],
            "cvss": 6.1,
            "severity": 3,  # Medium
            "tags": ["xss", "reflected", "unsanitized-input", "code-vulnerability"],
            "code": '{"vulnerable_code": "<div>Search Results for: \\" + user_input + \\"</div>", "start_line_number": "45", "end_line_number": "45", "file_name": "views/search.py"}',
            "custom_fields": "{}"
        },
        {
            "title": "Insecure Direct Object Reference in User Profile Access",
            "description": "User ID can be changed in the URL to access other users' profiles without proper authorization checks.",
            "bug_level": 1,  # Code finding
            "mitigation": "Implement proper authorization checks before serving user-specific data. Use session-based access control and validate user permissions.",
            "steps_to_reproduce": "1. Login as user A and go to /profile/101. 2. Change the URL to /profile/102. 3. Observe that user B's profile is visible without authorization.",
            "cwe_list": [639],  # CWE-639: Authorization Bypass Through User-Controlled Key
            "cve_list": [],
            "cvss": 5.3,
            "severity": 3,  # Medium
            "tags": ["idor", "authorization", "insecure-access", "access-control"],
            "code": '{"vulnerable_code": "user = db.get_user_by_id(request.params[\\"user_id\\"])", "start_line_number": "88", "end_line_number": "88", "file_name": "controllers/profile.py"}',
            "custom_fields": "{}"
        }
    ]
    
    for code_finding in code_findings:
        try:
            # Check for duplicates
            exists, finding_id = finding_exists(code_finding["title"], existing_findings)
            if exists:
                logger.info(f"Code finding '{code_finding['title']}' already exists with ID: {finding_id}")
                continue
            
            # Add required common fields
            finding_fields = {
                "title": code_finding["title"],                     # Required
                "description": code_finding["description"],         # Required
                "organization_id": enums.ORGANIZATION_ID,           # Required
                "bug_level": code_finding["bug_level"],            # Required
                "mitigation": code_finding["mitigation"],           # Required
                "steps_to_reproduce": code_finding["steps_to_reproduce"],  # Required
                "cwe_list": code_finding["cwe_list"],              # Optional
                "cve_list": code_finding["cve_list"],              # Optional
                "cvss": code_finding["cvss"],                      # Optional
                "severity": code_finding["severity"],              # Required
                "tags": code_finding["tags"],                      # Optional
                "selected_assets": code_asset_ids,                 # Required
                "code": code_finding["code"],                      # Required for code findings
                "bug_attachment_list": [],                         # Optional
                "engagement_ids": [],                              # Optional
                "custom_fields": code_finding["custom_fields"]    # Optional
            }
            
            result = client.execute_mutation("bug_create", **finding_fields)
            logger.info(f"Code finding '{code_finding['title']}' created successfully!")
            
        except Exception as e:
            logger.error(f"Error creating code finding '{code_finding['title']}': {e}")

def demonstrate_field_requirements():
    """Show examples of required and optional fields for each finding type"""
    print("\n=== Field Requirements by Finding Type ===")
    
    print("\n** All Finding Types (Common Requirements) **")
    print("- title (String): Concise finding title")
    print("- description (String): Detailed vulnerability description")
    print("- organization_id (UUID): Your organization identifier")
    print("- bug_level (Int): Finding level (1=Code, 2=Web, 3=Mobile, 4=Network, 5=Cloud, 6=Package)")
    print("- mitigation (String): Recommended remediation steps")
    print("- steps_to_reproduce (String): Instructions to replicate the issue")
    print("- severity (Int): Severity level (1=Info, 2=Low, 3=Medium, 4=High, 5=Critical)")
    print("- selected_assets (Array): Asset IDs affected by the finding")
    
    print("\n** Web Findings (bug_level=2) **")
    print("Required: web (JSON String) - Web-specific details")
    print("  - affected_endpoints: Array of affected URLs")
    print("  - request: HTTP request demonstrating the issue")
    print("  - response: HTTP response showing the vulnerability")
    
    print("\n** Network Findings (bug_level=4) **")
    print("Required: network (JSON String) - Network-specific details")
    print("  - port: Port number involved")
    print("  - cpe: Common Platform Enumeration identifiers")
    
    print("\n** Code Findings (bug_level=1) **")
    print("Required: code (JSON String) - Code-specific details")
    print("  - vulnerable_code: The vulnerable code snippet")
    print("  - start_line_number: Starting line number")
    print("  - end_line_number: Ending line number")
    print("  - file_name: Path to the vulnerable file")
    
    print("\n** Optional Fields (All Types) **")
    print("- cwe_list (Array): CWE classifications")
    print("- cve_list (Array): CVE identifiers")
    print("- cvss (Float): CVSS score (0.0-10.0)")
    print("- tags (Array): Tags for categorization")
    print("- custom_fields (JSON String): Additional metadata")
    print("- bug_attachment_list (Array): File attachments")
    print("- engagement_ids (Array): Associated engagement IDs")
    
    print("\n** Severity Levels **")
    print("1 = Info (Informational)")
    print("2 = Low (Low impact)") 
    print("3 = Medium (Medium impact)")
    print("4 = High (High impact)")
    print("5 = Critical (Critical impact)")
    
    print("\n** Bug Level Types **")
    print("1 = Code (Source code vulnerabilities)")
    print("2 = Web (Web application vulnerabilities)")
    print("3 = Mobile (Mobile application vulnerabilities)")
    print("4 = Network (Network/infrastructure vulnerabilities)")
    print("5 = Cloud (Cloud configuration issues)")
    print("6 = Package (Third-party package vulnerabilities)")

def main():
    """Main function to demonstrate finding creation"""
    print("🔧 Strobes Finding Creation Examples")
    print("=" * 50)
    
    # Uncomment the functions you want to test:
    
    # Show field requirements
    demonstrate_field_requirements()
    
    # Create different types of findings
    create_web_findings()
    create_network_findings()
    create_code_findings()
    
    print("\n✅ Finding creation examples completed!")
    print("\n💡 Tips:")
    print("  - Findings require existing assets to be associated with")
    print("  - Each finding type has specific required fields (web, network, code)")
    print("  - Duplicate checking prevents creating identical findings")
    print("  - Uncomment different functions in main() to test various finding types")
    print("📚 For more field options, visit: https://github.com/strobes-co/ql-documentation")

if __name__ == "__main__":
    main()
