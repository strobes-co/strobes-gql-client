# Strobes GraphQL Client

## Introduction

The Strobes GraphQL Client is a Python-based interface that enables programmatic interaction with the Strobes platform. This client provides comprehensive functionality for managing assets, security vulnerabilities, and security assessments through GraphQL API calls.

This documentation will guide you through the setup process and demonstrate how to effectively utilize the client to integrate with your Strobes platform instance.

## Prerequisites

### Python Installation

Ensure Python 3.7 or higher is installed on your system.

**Verify Python Installation:**
```bash
python3 --version
```

**Installation Methods:**

- **Windows:** Download from [python.org](https://python.org) and follow the installation wizard
- **macOS:** Use Homebrew: `brew install python3` or download from python.org
- **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install python3 python3-pip`
- **Linux (RHEL/CentOS):** `sudo yum install python3 python3-pip`

## Installation

### Clone the Repository

Clone the Strobes GraphQL Client repository from GitHub:

```bash
git clone https://github.com/strobes-co/strobes-gql-client.git
cd strobes-gql-client
```

### Virtual Environment Setup

Create and activate an isolated Python environment to manage dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

When activated, your terminal prompt will display `(venv)` prefix.

### Install Dependencies

Install the required packages using the provided requirements file:

```bash
pip install -r requirements.txt
```

This installs all necessary dependencies including the GraphQL client libraries and authentication modules required for Strobes platform integration.

## Configuration

### Collecting Required Information

Before establishing a connection, gather the following information from your Strobes platform:

- **Host**: Your Strobes platform domain (e.g., "mycorp.strobes.co", "mycorp.in.strobes.co", "mycorp.us.strobes.co")
- **API Token**: Authentication token for API access
- **Organization ID**: Your organization's unique identifier

### Obtaining API Token and Organization ID

1. Navigate to your Strobes platform in a web browser
2. Log in with your credentials
3. Access the **Settings** menu (typically located in the top-right corner)
4. Select **"API Access"** from the settings menu
5. Click **"Generate Token"** to create a new API token
6. Copy the generated token (alphanumeric string)
7. Note your **Organization ID** displayed on the same page

<!-- VIDEO PLACEHOLDER: Insert API Token and Organization ID tutorial video here -->

**Security Note**: Treat your API token as a credential. Store it securely and avoid sharing it publicly.

### Configuring Connection Settings

Edit the `strobes_gql_client/enums.py` file to configure your connection settings:

```python
# strobes_gql_client/enums.py
USER_AGENT = "strobes-python-gql-client"
APP_PORT   = 443
APP_SCHEME = "https"
APP_HOST   = "mycorp.strobes.co"            # Update with your domain
API_TOKEN  = "your_api_token_here"          # Add your API token
ORGANIZATION_ID = "your_organisation_uuid"  # Add your organization ID
```

Leave `APP_SCHEME` and `APP_PORT` unchanged unless using a non-standard configuration.

### Testing Connectivity

Verify your connection using either method:

**Option 1: Run the test script**
```bash
python examples/test-connectivity-example.py
```

**Option 2: Use the function directly**
```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import json

# Initialize client using configuration from enums
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Test connection
resp = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
assets = resp.get("data", {}).get("allAssets", {}).get("objects", [])
print(f"Total assets: {len(assets)}")
```

If the asset count displays without error, your connection is successfully configured.

**Video Tutorial**: A step-by-step video demonstration of this process is available below.

[Watch the Video](https://app.arcade.software/share/h36MBeei7wJP7vf1diYs)

## Assets Fetching

### Fetch All Assets

Retrieve all assets from your organization:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch all assets
response = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
assets = response.get("data", {}).get("allAssets", {}).get("objects", [])

print(f"Total assets: {len(assets)}")
for asset in assets[:5]:  # Show first 5 assets
    print(f"- {asset.get('name')} (Type: {asset.get('type')}, Risk: {asset.get('risk_score')})")
```

**Example File**: `examples/test-fetchassets-example.py`

[Watch the Video](https://app.arcade.software/share/OgmRxuL5eFFOK0cCMBRk)

### Fetch Assets with Search Query

Filter assets using search queries:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch web assets only
response = client.execute_query(
    "all_assets", 
    organization_id=enums.ORGANIZATION_ID,
    search_query="type = 1"  # Web assets
)
assets = response.get("data", {}).get("allAssets", {}).get("objects", [])

print(f"Total web assets: {len(assets)}")
for asset in assets[:3]:  # Show first 3 assets
    print(f"- {asset.get('name')} ({asset.get('target')})")
```

**Example File**: `examples/test-fetchassets-example.py`


### Available Response Fields

Each asset response contains the following fields based on the official GraphQL schema:

**Core Identifiers:**
- `id` (ID!) - Unique asset identifier (required)
- `tempId` (UUID) - Temporary UUID for processing
- `name` (String!) - Asset name (required)
- `target` (String) - Asset URL or target identifier

**Asset Classification:**
- `type` (Int!) - Asset type (1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code repo asset)
- `cloudType` (Int!) - Cloud provider type (AWS=2, Azure=3, GCP=4, others=1)
- `sensitivity` (Int!) - Sensitivity level (1=Low, 2=Medium, 3=High, 4=Critical)
- `exposed` (Int!) - Exposure level (1=Private, 2=Public)

**Security & Risk:**
- `risk_score` (Int) - Risk score (0-100, computed field)
- `disabled` (Boolean!) - Whether asset is disabled
- `keys` (String!) - Security keys or identifiers

**Technical Details:**
- `ipaddress` (String) - IP address
- `hostname` (String) - Hostname
- `macAddress` (String) - MAC address
- `os` (String) - Operating system
- `location` (String) - Physical or logical location

**Data & Configuration:**
- `data` (JSONString) - Additional asset data in JSON format
- `additionalInfo` (JSONString) - Extra information in JSON format

**Timestamps:**
- `created` (DateTime!) - Creation timestamp (required, ISO8601 format)
- `updated` (DateTime!) - Last updated timestamp (required, ISO8601 format)

**Relationships:**
- `organization` (TenantOrganizationType) - Organization details
- `createdBy` (UserType) - User who created the asset
- `tags` ([TagType]!) - Associated tags (array)
- `linkedAssets` ([AssetType]!) - Linked assets (array)
- `scan` (ScanLog) - Associated scan information

**Asset Associations:**
- `groupAssets` ([GroupsType]!) - Groups containing this asset
- `engagementAssets` ([EngagementType]!) - Security engagements
- `configurationAsset` ([ConfigurationType]!) - Configurations
- `bugSet` ([BugType]!) - Associated vulnerabilities

**Data Types Reference:**
- `String` - UTF-8 text data
- `Int` - Signed whole numbers  
- `Boolean` - True/false values
- `DateTime` - ISO8601 timestamp
- `ID` - Unique identifier (returned as String)
- `UUID` - Universal unique identifier
- `JSONString` - JSON formatted data
- `!` - Required field (non-nullable)
- `[]` - Array of values

### Common Search Patterns

**Available Operators:**
- `=` Equal to | `!=` Not equal to | `>` Greater than | `>=` Greater than or equal
- `<` Less than | `<=` Less than or equal | `~` Contains | `!~` Doesn't contain  
- `in` In list | `not in` Not in list | `^` Regex match
- `and` `or` for combining conditions

**By Asset Type:**
```python
search_query='type = 1'         # Web assets
search_query='type = 3'         # Network assets  
search_query='type = 4'         # Cloud assets
search_query='type = 7'         # Code repo assets
search_query='type in (1, 3, 4)'  # Multiple types
```

**By Sensitivity Level:**
```python
search_query='sensitivity = 1'     # Low sensitivity
search_query='sensitivity = 2'     # Medium sensitivity
search_query='sensitivity = 3'     # High sensitivity
search_query='sensitivity = 4'     # Critical sensitivity
search_query='sensitivity in (3, 4)'  # High and Critical
```

**By Exposure:**
```python
search_query='exposed = 1'  # Private assets
search_query='exposed = 2'  # Public assets
```

**By Risk Score:**
```python
search_query='risk_score >= 80'     # High-risk assets
search_query='risk_score <= 30'     # Low-risk assets
search_query='risk_score > 50 and risk_score < 80'  # Medium risk range
```

**By Name and Target:**
```python
search_query='name ~ "production"'  # Assets containing "production"
search_query='target ~ "api"'       # Targets containing "api"
search_query='hostname ~ "server"'  # Hostnames containing "server"
```

**By Network Information:**
```python
search_query='ipaddress = "192.168.1.1"'      # Specific IP
search_query='ipaddress ~ "192.168.1"'        # IP range
search_query='os ~ "Linux"'                   # Operating system
search_query='port_number = 80'               # Specific port
```

**By Cloud Assets:**
```python
search_query='cloud_type = "AWS"'             # AWS assets
search_query='region = "us-east-1"'           # Specific region
search_query='account_id = "123456789"'       # Cloud account
```

**By Date Range:**
```python
search_query='created >= "2024-01-01"'        # Created after date
search_query='created < "2024-12-31"'         # Created before date
search_query='created >= "2024-01-01" and created <= "2024-06-30"'  # Date range
```

**By Tags and Metadata:**
```python
search_query='tags in ("critical", "external")'  # Tagged assets
search_query='created_by.id = 123'              # Created by specific user
search_query='connector = "Nessus"'             # Imported via connector
```

**Combined Complex Queries:**
```python
search_query='type = 1 and risk_score >= 80 and exposed = 2'   # High-risk public web assets
search_query='cloud_type = "AWS" and region = "us-east-1" and tags in ("production")'  # Production AWS assets in US East
search_query='os ~ "Linux" and port_number in (80, 443, 8080)'  # Linux servers with web ports
search_query='type = 4 and sensitivity >= 3 and exposed = 2'    # High-sensitivity public cloud assets
```

### Advanced Search Documentation

For comprehensive search query syntax and additional field options, refer to the **[Strobes QL Documentation](https://github.com/strobes-co/ql-documentation)**, specifically the **[Assets section](https://github.com/strobes-co/ql-documentation?tab=readme-ov-file#assets)**.

## Asset Creation

### Create Web Asset

Create a new web application asset:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create web asset
asset_fields = {
    "name": "Production Web App",                    # Required: Asset name
    "organization_id": enums.ORGANIZATION_ID,        # Required: Organization ID
    "type": 1,                                       # Required: Asset type (1=Web)
    "url": "https://app.example.com",               # Required: Web asset URL
    "sensitivity": 3,                                # Required: Sensitivity (1=Low, 2=Medium, 3=High, 4=Critical)
    "exposed": 2,                                    # Required: Exposure (1=Private, 2=Public)
    "tags": ["production", "web", "critical"]        # Optional: Tags for categorization
}

result = client.execute_mutation("create_asset", **asset_fields)
print("Web asset created successfully!")
```

**Example File**: `examples/test-create-assets-example.py`

[Watch the Video](https://app.arcade.software/share/GGWpd2Pl4SdZ5vMfiXrh)

### Create Network Asset

Create a new network device or server asset:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create network asset
asset_fields = {
    "name": "Production Server",                     # Required: Asset name
    "organization_id": enums.ORGANIZATION_ID,        # Required: Organization ID
    "type": 3,                                       # Required: Asset type (3=Network)
    "ipaddress": "192.168.1.100",                   # Required: IP address (or ipaddress_list for multiple)
    "sensitivity": 4,                                # Required: Sensitivity level
    "exposed": 1,                                    # Required: Exposure (1=Private, 2=Public)
    "hostname": "prod-server-01",                    # Optional: Hostname
    "os": "Ubuntu 20.04",                           # Optional: Operating system
    "tags": ["server", "production", "ubuntu"]      # Optional: Tags
}

result = client.execute_mutation("create_asset", **asset_fields)
print("Network asset created successfully!")
```

**Example File**: `examples/test-create-assets-example.py`

[Watch the Video](https://app.arcade.software/share/XuIU3E90EFufAYrAypWy)

### Create Cloud Asset

Create a new cloud resource asset:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create cloud asset
asset_fields = {
    "name": "AWS EC2 Instance",                      # Required: Asset name
    "organization_id": enums.ORGANIZATION_ID,        # Required: Organization ID
    "type": 4,                                       # Required: Asset type (4=Cloud)
    "cloud_type": 2,                                # Required: Cloud provider (2=AWS, 3=Azure, 4=GCP, 1=Other)
    "sensitivity": 3,                                # Required: Sensitivity level
    "exposed": 2,                                    # Required: Exposure level
    "region": "us-east-1",                          # Optional: Cloud region
    "account_id": "123456789012",                   # Optional: Cloud account ID
    "resource_id": "i-0123456789abcdef0",           # Optional: Cloud resource ID
    "tags": ["aws", "ec2", "production"]            # Optional: Tags
}

result = client.execute_mutation("create_asset", **asset_fields)
print("Cloud asset created successfully!")
```

**Example File**: `examples/test-create-assets-example.py`

[Watch the Video](https://app.arcade.software/share/n0RJ8MfToJR3vNi3FyA5)


### Create Mobile Asset

Create a new mobile application asset:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create mobile asset
asset_fields = {
    "name": "Mobile Banking App",                    # Required: Asset name
    "organization_id": enums.ORGANIZATION_ID,        # Required: Organization ID
    "type": 2,                                       # Required: Asset type (2=Mobile)
    "package": "com.company.banking",               # Required: Package name or bundle ID
    "sensitivity": 4,                                # Required: Sensitivity level
    "exposed": 2,                                    # Required: Exposure level
    "tags": ["mobile", "banking", "ios", "android"] # Optional: Tags
}

result = client.execute_mutation("create_asset", **asset_fields)
print("Mobile asset created successfully!")
```

**Example File**: `examples/test-create-assets-example.py`

[Watch the Video](https://app.arcade.software/share/f31EgZ04ZXdPAzR0jPwb)

### Required Fields by Asset Type

**All Asset Types (Common Requirements):**
- `name` (String) - Descriptive asset name
- `organization_id` (UUID) - Your organization identifier
- `type` (Int) - Asset type (1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code repo)
- `sensitivity` (Int) - Sensitivity level (1=Low, 2=Medium, 3=High, 4=Critical)
- `exposed` (Int) - Exposure level (1=Private, 2=Public)

**Asset Type Specific Requirements:**

**Web Assets (type=1):**
- `url` (String) - Web application URL

**Mobile Assets (type=2):**
- `package` (String) - Package name or bundle identifier

**Network Assets (type=3):**
- `ipaddress` (String) OR `ipaddress_list` (Array) - IP address(es)

**Cloud Assets (type=4):**
- `cloud_type` (Int) - Cloud provider (1=Other, 2=AWS, 3=Azure, 4=GCP)

**Code Repository Assets (type=7):**
- `url` (String) - Repository URL

### Optional Fields

**Network Assets:**
- `hostname` (String) - Server hostname
- `os` (String) - Operating system
- `mac_address` (String) - MAC address
- `cpe` (String) - Common Platform Enumeration

**Cloud Assets:**
- `region` (String) - Cloud region
- `account_id` (String) - Cloud account identifier
- `resource_id` (String) - Cloud resource identifier

**All Assets:**
- `tags` (Array) - Tags for categorization and search

## Findings Fetching

### Fetch All Findings

Retrieve all security findings (vulnerabilities) from your organization:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch all findings
response = client.execute_query("all_bugs", organization_id=enums.ORGANIZATION_ID)
findings = response.get("data", {}).get("allBugs", {}).get("objects", [])

print(f"Total findings: {len(findings)}")
for finding in findings[:5]:  # Show first 5 findings
    print(f"- {finding.get('title')} (Severity: {finding.get('severity')}, CVSS: {finding.get('cvss')})")
```

**Example File**: `examples/test-fetch-findings-example.py`

[Watch the Video](https://app.arcade.software/share/jka4PEc74QgEbsgEEjiJ)

### Fetch Findings with Search Query

Filter findings using search queries:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch critical severity findings only
response = client.execute_query(
    "all_bugs", 
    organization_id=enums.ORGANIZATION_ID,
    search_query="severity = 4"  # Critical findings
)
findings = response.get("data", {}).get("allBugs", {}).get("objects", [])

print(f"Critical findings: {len(findings)}")
for finding in findings[:3]:  # Show first 3 findings
    print(f"- {finding.get('title')} (CVSS: {finding.get('cvss')})")
```

**Example File**: `examples/test-fetch-findings-example.py`



### Available Response Fields

Each finding response contains the following fields based on the official GraphQL schema:

**Core Identifiers:**
- `id` (ID!) - Unique finding identifier (required)
- `title` (String!) - Finding title (required)
- `description` (String!) - Detailed description (required)
- `hash` (String) - Unique hash for deduplication

**Severity & Risk:**
- `severity` (Int!) - Severity level (1=Info, 2=Low, 3=Medium, 4=High, 5=Critical)
- `cvss` (Float!) - CVSS score (0.0-10.0)
- `state` (Int!) - Finding state (1=Open, 2=Closed, 3=In Progress, 4=Resolved)
- `bugLevel` (Int!) - Finding level (1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code)

**Vulnerability Details:**
- `mitigation` (String!) - Remediation steps (required)
- `stepsToReproduce` (String!) - Reproduction steps (required)
- `attackVector` (String) - Attack vector description
- `exploitAvailable` (Boolean!) - Whether exploit is available
- `patchAvailable` (Boolean!) - Whether patch is available

**Classification:**
- `cwe` ([CWEType]!) - CWE (Common Weakness Enumeration) classifications
- `cve` ([CVEType]!) - CVE (Common Vulnerabilities and Exposures) identifiers
- `bugTags` ([TagType]!) - Associated tags

**Timestamps:**
- `created` (DateTime!) - Creation timestamp (required, ISO8601 format)
- `updated` (DateTime!) - Last updated timestamp (required, ISO8601 format)
- `dueDate` (DateTime) - Due date for remediation
- `vulnerableSince` (DateTime) - When vulnerability was introduced

**Relationships:**
- `organization` (TenantOrganizationType) - Organization details
- `asset` (AssetType) - Associated asset
- `reportedBy` (UserType) - User who reported the finding
- `assignedTo` ([UserType]!) - Users assigned to fix the finding
- `team` (TeamType) - Assigned team

**Assessment Context:**
- `engagement` (EngagementType) - Security engagement/assessment
- `connector` (ConnectorType) - Tool/scanner that found the vulnerability
- `scan` (ScanLog) - Scan information
- `scannerRawResponse` (JSONString) - Raw scanner output

**Additional Details:**
- `objectId` (Int) - Object reference ID
- `duplicate` (BugType) - Reference to duplicate finding
- `slaViolated` (Boolean!) - Whether SLA was violated
- `prioritizationScore` (Float!) - Prioritization score
- `exploitInfo` (JSONString) - Exploit information
- `patchInfo` (JSONString) - Patch information

### Common Search Patterns

**Available Operators:**
- `=` Equal to | `!=` Not equal to | `>` Greater than | `>=` Greater than or equal
- `<` Less than | `<=` Less than or equal | `~` Contains | `!~` Doesn't contain  
- `in` In list | `not in` Not in list | `^` Regex match
- `and` `or` for combining conditions

**By Severity Level:**
```python
search_query='severity = 4'            # Critical findings
search_query='severity = 3'            # High severity findings
search_query='severity in (3, 4)'      # High and Critical findings
search_query='severity >= 3'           # High severity and above
```

**By Finding State:**
```python
search_query='state = 1'               # Open findings
search_query='state = 4'               # Resolved findings
search_query='state in (1, 3)'         # Open and In Progress findings
search_query='state != 2'              # All except closed findings
```

**By Finding Level (Asset Type):**
```python
search_query='bug_level = 1'           # Web findings
search_query='bug_level = 3'           # Network findings
search_query='bug_level = 4'           # Cloud findings
search_query='bug_level in (1, 2)'     # Web and Mobile findings
```

**By CVSS Score:**
```python
search_query='cvss >= 9.0'             # Critical CVSS scores
search_query='cvss >= 7.0 and cvss < 9.0'  # High CVSS range
search_query='cvss <= 4.0'             # Low CVSS scores
```

**By Title and Description:**
```python
search_query='title ~ "SQL"'           # SQL injection findings
search_query='title ~ "XSS"'           # Cross-site scripting findings
search_query='description ~ "authentication"'  # Authentication issues
search_query='title ~ "Remote Code"'   # Remote code execution
```

**By CVE and CWE:**
```python
search_query='cve ~ "CVE-2023"'        # Findings with 2023 CVEs
search_query='cve ~ "CVE-2023-1234"'   # Specific CVE
search_query='cwe ~ "CWE-79"'          # Cross-site scripting (CWE-79)
search_query='cwe ~ "CWE-89"'          # SQL injection (CWE-89)
```

**By Date Range:**
```python
search_query='created >= "2024-01-01"'     # Created after date
search_query='dueDate <= "2024-12-31"'     # Due before date
search_query='vulnerableSince >= "2024-06-01"'  # Vulnerable since date
```

**By Assignment and Team:**
```python
search_query='assignedTo.firstName ~ "John"'      # Assigned to John
search_query='reportedBy.email ~ "security"'      # Reported by security team
search_query='team.name ~ "DevOps"'               # Assigned to DevOps team
```

**By Asset Information:**
```python
search_query='asset.name ~ "production"'          # Findings in production assets
search_query='asset.type = 1'                     # Findings in web assets
search_query='asset.risk_score >= 80'             # Findings in high-risk assets
```

**By Exploit and Patch Status:**
```python
search_query='exploitAvailable = true'            # Findings with available exploits
search_query='patchAvailable = true'              # Findings with available patches
search_query='exploitAvailable = true and patchAvailable = false'  # Exploitable but no patch
```

**Combined Complex Queries:**
```python
search_query='severity in (3, 4) and state = 1 and bug_level = 1'  # Critical/High open web findings
search_query='cvss >= 8.0 and exploitAvailable = true'             # High CVSS with exploits
search_query='asset.exposed = 2 and severity >= 3'                 # High severity in public assets
search_query='created >= "2024-01-01" and state = 1 and cvss >= 7.0'  # Recent high-severity open findings
```

### Advanced Search Documentation

For comprehensive search query syntax and additional field options, refer to the **[Strobes QL Documentation](https://github.com/strobes-co/ql-documentation)**, specifically the **[Bugs section](https://github.com/strobes-co/ql-documentation?tab=readme-ov-file#bugs)**.

## Finding Creation

### Create Web Finding

Create a new web application security finding:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create web finding
finding_fields = {
    "title": "Cross-Site Scripting (XSS) in Search Function",           # Required: Finding title
    "description": "Reflected XSS vulnerability in the search functionality allows attackers to inject malicious scripts.",  # Required: Detailed description
    "organization_id": enums.ORGANIZATION_ID,                          # Required: Organization ID
    "bug_level": 2,                                                    # Required: Finding level (2=Web)
    "mitigation": "Sanitize user input and implement proper output encoding.",  # Required: Remediation steps
    "steps_to_reproduce": "1. Navigate to search page. 2. Enter script payload. 3. Observe execution.",  # Required: Reproduction steps
    "cwe_list": [79],                                                  # Optional: CWE classifications
    "cve_list": [],                                                    # Optional: CVE identifiers
    "cvss": 6.1,                                                       # Optional: CVSS score (0.0-10.0)
    "severity": 3,                                                     # Required: Severity (1=Info, 2=Low, 3=Medium, 4=High, 5=Critical)
    "tags": ["xss", "web", "reflected"],                              # Optional: Tags
    "selected_assets": [123, 456],                                     # Required: Associated asset IDs
    "web": '{"affected_endpoints": ["http://example.com/search"], "request": "GET /search?q=<script>alert(1)</script>", "response": "HTTP/1.1 200 OK"}',  # Required for web findings
    "custom_fields": "{}"                                              # Optional: Additional custom data
}

result = client.execute_mutation("bug_create", **finding_fields)
print("Web finding created successfully!")
```

**Example File**: `examples/test-create-findings-example.py`

[Watch the Video](https://app.arcade.software/share/f3YO1ztvkgVnDNaFSosS)


### Create Network Finding

Create a new network security finding:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create network finding
finding_fields = {
    "title": "Open SSH Port (22) Exposed to Internet",                 # Required: Finding title
    "description": "SSH port 22 is open and accessible from the internet, increasing attack surface.",  # Required: Detailed description
    "organization_id": enums.ORGANIZATION_ID,                          # Required: Organization ID
    "bug_level": 4,                                                    # Required: Finding level (4=Network)
    "mitigation": "Implement firewall rules to restrict SSH access to specific IP ranges.",  # Required: Remediation steps
    "steps_to_reproduce": "1. Use nmap to scan target IP. 2. Verify SSH service running. 3. Confirm external access.",  # Required: Reproduction steps
    "cwe_list": [200],                                                 # Optional: CWE classifications
    "cve_list": [],                                                    # Optional: CVE identifiers
    "cvss": 5.3,                                                       # Optional: CVSS score
    "severity": 3,                                                     # Required: Severity level
    "tags": ["network", "ssh", "exposed-services"],                   # Optional: Tags
    "selected_assets": [789],                                          # Required: Associated asset IDs
    "network": '{"port": "22", "cpe": ["cpe:/a:openssh:openssh:8.2p1"]}',  # Required for network findings
    "custom_fields": "{}"                                              # Optional: Additional custom data
}

result = client.execute_mutation("bug_create", **finding_fields)
print("Network finding created successfully!")
```

**Example File**: `examples/test-create-findings-example.py`

[Watch the Video](https://app.arcade.software/share/EA86C2IGqwNwzBRrYnl0)


### Create Code Finding

Create a new code security finding:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Create code finding
finding_fields = {
    "title": "Command Injection Vulnerability in File Upload Handler",   # Required: Finding title
    "description": "User input in filename parameter is directly concatenated into shell command.",  # Required: Detailed description
    "organization_id": enums.ORGANIZATION_ID,                          # Required: Organization ID
    "bug_level": 1,                                                    # Required: Finding level (1=Code)
    "mitigation": "Use secure libraries like subprocess with argument lists instead of raw command strings.",  # Required: Remediation steps
    "steps_to_reproduce": "1. Intercept file upload request. 2. Modify filename parameter. 3. Observe command execution.",  # Required: Reproduction steps
    "cwe_list": [78],                                                  # Optional: CWE classifications
    "cve_list": [],                                                    # Optional: CVE identifiers
    "cvss": 8.6,                                                       # Optional: CVSS score
    "severity": 4,                                                     # Required: Severity level
    "tags": ["command-injection", "code-vulnerability"],              # Optional: Tags
    "selected_assets": [101],                                          # Required: Associated asset IDs
    "code": '{"vulnerable_code": "os.system(\\"mv uploads/\\" + filename + \\" /archive/\\")", "start_line_number": "78", "end_line_number": "78", "file_name": "utils/upload_handler.py"}',  # Required for code findings
    "custom_fields": "{}"                                              # Optional: Additional custom data
}

result = client.execute_mutation("bug_create", **finding_fields)
print("Code finding created successfully!")
```

**Example File**: `examples/test-create-findings-example.py`

[Watch the Video](https://app.arcade.software/share/wGZRCyMKJ70Pfi7mUpQx)


### Required Fields by Finding Type

**All Finding Types (Common Requirements):**
- `title` (String) - Concise finding title
- `description` (String) - Detailed vulnerability description
- `organization_id` (UUID) - Your organization identifier
- `bug_level` (Int) - Finding level (1=Code, 2=Web, 3=Mobile, 4=Network, 5=Cloud, 6=Package)
- `mitigation` (String) - Recommended remediation steps
- `steps_to_reproduce` (String) - Instructions to replicate the issue
- `severity` (Int) - Severity level (1=Info, 2=Low, 3=Medium, 4=High, 5=Critical)
- `selected_assets` (Array) - Asset IDs affected by the finding

**Finding Type Specific Requirements:**

**Web Findings (bug_level=2):**
- `web` (JSON String) - Web-specific details:
  - `affected_endpoints` - Array of affected URLs
  - `request` - HTTP request demonstrating the issue
  - `response` - HTTP response showing the vulnerability

**Network Findings (bug_level=4):**
- `network` (JSON String) - Network-specific details:
  - `port` - Port number involved
  - `cpe` - Common Platform Enumeration identifiers

**Code Findings (bug_level=1):**
- `code` (JSON String) - Code-specific details:
  - `vulnerable_code` - The vulnerable code snippet
  - `start_line_number` - Starting line number
  - `end_line_number` - Ending line number (can be same as start)
  - `file_name` - Path to the vulnerable file

### Optional Fields

**Classification:**
- `cwe_list` (Array) - CWE (Common Weakness Enumeration) numbers
- `cve_list` (Array) - CVE (Common Vulnerabilities and Exposures) identifiers
- `cvss` (Float) - CVSS score (0.0-10.0)

**Additional Information:**
- `tags` (Array) - Tags for categorization and search
- `custom_fields` (JSON String) - Additional custom metadata
- `bug_attachment_list` (Array) - File attachments
- `engagement_ids` (Array) - Associated engagement/assessment IDs

### Severity Levels

**Severity Values:**
- `1` = Info (Informational finding)
- `2` = Low (Low impact vulnerability)
- `3` = Medium (Medium impact vulnerability)
- `4` = High (High impact vulnerability)
- `5` = Critical (Critical impact vulnerability)

### Bug Level Types

**Bug Level Values:**
- `1` = Code (Source code vulnerabilities)
- `2` = Web (Web application vulnerabilities)
- `3` = Mobile (Mobile application vulnerabilities)
- `4` = Network (Network/infrastructure vulnerabilities)
- `5` = Cloud (Cloud configuration issues)
- `6` = Package (Third-party package vulnerabilities)

## Engagements Fetching

### Fetch All Engagements

Retrieve all engagements for your organization:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch all engagements
response = client.execute_query(
    "all_engagements",
    organization_id=enums.ORGANIZATION_ID
)
engagements = response.get("data", {}).get("allEngagements", {}).get("objects", [])

print(f"Total engagements: {len(engagements)}")
for eng in engagements[:5]:  # Show first 5 engagements
    print(f"- {eng.get('name')} (ID: {eng.get('id')}, Scheduled: {eng.get('scheduled_date')})")
```

### Fetch Engagements with Search Query

Filter engagements using powerful search queries:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Fetch engagements matching a search query (e.g., name contains "pentest")
response = client.execute_query(
    "all_engagements",
    organization_id=enums.ORGANIZATION_ID,
    search_query='name ~ "pentest"'
)
engagements = response.get("data", {}).get("allEngagements", {}).get("objects", [])

print(f"Pentest engagements: {len(engagements)}")
for eng in engagements[:3]:
    print(f"- {eng.get('name')} (State: {eng.get('state')})")
```

**Example File**: `examples/test-fetchengagement-example.py`

[Watch the Video](https://app.arcade.software/share/D8fXmSOGMDDzshHHNUd6)

### Available Response Fields

Each engagement response contains the following fields based on the official GraphQL schema:

**Core Identifiers:**
- `id` (ID!) – Unique engagement identifier (required)
- `engagement_custom_id` (Int) – Custom numerical ID
- `name` (String!) – Engagement name (required)

**Scheduling & Dates:**
- `scheduled_date` (Date) – Scheduled start date
- `delivery_date` (Date) – Planned delivery / due date
- `created` (DateTime!) – Creation timestamp
- `updated` (DateTime!) – Last updated timestamp

**Associations & Context:**
- `organization` (TenantOrganizationType) – Organization details
- `vendor` (VendorType) – Vendor assigned to the engagement
- `subscribed_services` (JSONString) – Services included in the engagement
- `documents` ([VaultType]!) – Attached documents
- `created_by` (UserType) – User who created the engagement
- `engagement_assessment` ([AssessmentType]!) – Assessments linked to this engagement
- `prerequisites_engagement` ([PreRequisitesType]!) – Engagement prerequisites / tasks

**Metrics & State:**
- `security_posture` (Int!) – Security posture score
- `credits_estimated` (Boolean!) – Whether credit usage is estimated
- `credits` (Int!) – Allocated credits
- `plans` (Int!) – Plan type / tier
- `assessments_count` (Int) – Total assessment count
- `engagement_completion` (Int) – Completion percentage
- `state` (String) – Current engagement state (e.g., "Active")

**Custom & Additional Data:**
- `fields` (JSONString) – Custom field data
- `checked_terms_and_conditions` (Boolean!) – Terms acceptance flag
- `is_active` (Boolean!) – Whether the engagement is active

For a complete list of fields, consult the **[Strobes QL Documentation](https://github.com/strobes-co/ql-documentation)** under the **Engagements section**.

## Engagement Creation

### Create Engagement

Create a new engagement (security assessment) for your organization:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

engagement_fields = {
    "name": "Q3 2025 Security Assessment",                 # Required: Engagement name
    "organization_id": enums.ORGANIZATION_ID,               # Required: Organization ID
    "vendor_code": "sec-12345",                           # Optional: Vendor code
    "scheduled_date": "2025-07-01",                       # Optional: Scheduled start date (YYYY-MM-DD)
    "delivery_date": "2025-07-16",                        # Optional: Planned delivery date (YYYY-MM-DD)
    "plans": 1,                                             # Required: Plan type / tier
    "document_ids": [],                                     # Optional: Attachments (Vault IDs)
    "subscribed_services": [                                # Required: Services included
        "Web Application Penetration Test",
        "Cloud Security"
    ],
    "assessment_data": "{\"Web Application Penetration Test\":[{\"search_query\":\"type = 1 and risk_score >= 80\"}]}",
    "prerequisites_data": "[]",                           # Optional: Prerequisite tasks
    "fields": "{\"internal_info\":\"Quarterly engagement\"}" # Optional: Custom fields JSON
}

result = client.execute_mutation("create_engagement", **engagement_fields)
print("Engagement created successfully!")
```

**Example Reference**: See `examples/test-createengagement-example.py` for a complete engagement creation script, or refer to `execute_create_engagement_with_multiple_services` in `examples/example.py` for an advanced multi-service example.

[Watch the Video](https://app.arcade.software/share/SJbGASd5s9Puyoflo7Tw)

## Vault Document Creation

### Create and Upload Vault Document

Create and upload documents to the Strobes vault:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import requests
import json

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def upload_file(filepath, engagement_id=None, is_prerequisite=False):
    """Upload a file to the vault"""
    try:
        operations = {
            'query': 'mutation AddVaultAttachment($file: Upload!, $organizationId: UUID!) { addVaultAttachment(file: $file, organizationId: $organizationId) { vault { id documentName documentSize } } }',
            'variables': {
                'file': None,
                'organizationId': enums.ORGANIZATION_ID
            }
        }
        map = {'0': ['variables.file']}
        
        with open(filepath, "rb") as f:
            files = {'0': (filepath, f, 'application/octet-stream')}
            response = requests.post(
                f"{client.app_url}api/graphql/",
                headers={
                    'Authorization': f"token {enums.API_TOKEN}",
                    'user-agent': enums.USER_AGENT
                },
                data={
                    'operations': json.dumps(operations),
                    'map': json.dumps(map)
                },
                files=files
            )
        result = response.json()
        vault_data = result.get('data', {}).get('addVaultAttachment', {}).get('vault', {})
        print(f"\nUploaded {filepath}:")
        print(f"Vault ID: {vault_data.get('id')}")
        print(f"Name: {vault_data.get('documentName')}")
        print(f"Size: {vault_data.get('documentSize')} bytes")
        return result
    except Exception as e:
        print(f"Error uploading {filepath}: {str(e)}")
        return None

# Example usage
upload_file("path/to/your/document.pdf")
```

**Example File**: `examples/test-create-vault-example.py`

### Required Fields
* `file`: The file to upload
* `organization_id`: Your organization's unique identifier

### Optional Fields
* `engagement_id`: UUID of the engagement to attach the document to (can be empty string or None)
* `is_prerequisite`: Boolean indicating if this is a prerequisite document

### Features
* Upload any type of file to the Strobes vault
* Attach documents to engagements
* Mark documents as prerequisites
* Track document metadata like name and size

### Example Response
```json
{
  "data": {
    "addVaultAttachment": {
      "vault": {
        "id": "123",
        "documentName": "requirements.txt",
        "documentSize": 49
      }
    }
  }
}
```
[Watch the Video](https://app.arcade.software/flows/F98XvHFDjmyEZMW8Z6xN/view)

### Fetch Vault Documents

#### Fetch All Vault Documents

Retrieve all documents from the vault:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Get all vault documents
print("\n=== All Vault Documents ===")
response = client.execute_query(
    "all_vault_attachments",
    organization_id=enums.ORGANIZATION_ID
)
attachments = response.get("data", {}).get("allVaultAttachments", {}).get("objects", [])
print(f"Total documents: {len(attachments)}")
for doc in attachments:
    name = doc.get('document_name', 'Unknown')
    who = doc.get('attachedBy', {}).get('firstName', '') + ' ' + doc.get('attachedBy', {}).get('lastName', '')
    when = doc.get('created', 'N/A')
    print(f"- {name} (Added by: {who.strip()}, On: {when})")
```
[Watch the Video](https://app.arcade.software/share/5O3FR2cQV1X6Sb4gmOFv)

#### Fetch Vault Documents with Search Query

Search for specific documents in the vault:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

# Initialize client
client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

# Search for documents with "test" in name
print("\n=== Search for 'test' documents ===")
response = client.execute_query(
    "all_vault_attachments",
    organization_id=enums.ORGANIZATION_ID,
    search_query='document_name ~ "test"'
)
attachments = response.get("data", {}).get("allVaultAttachments", {}).get("objects", [])
print(f"Found {len(attachments)} documents matching 'test'")
for doc in attachments:
    name = doc.get('document_name', 'Unknown')
    who = doc.get('attachedBy', {}).get('firstName', '') + ' ' + doc.get('attachedBy', {}).get('lastName', '')
    when = doc.get('created', 'N/A')
    print(f"- {name} (Added by: {who.strip()}, On: {when})")
```

**Example File**: `examples/test-fetch-vaults-example.py`

[Watch the Video](https://app.arcade.software/share/0atq1gLJ1ttmIAtUXts9)

### Complete collection of videos

Watch the complete video walkthrough covering configuration, examples, and usage:
[View Collection](https://app.arcade.software/share/collections/UNqMoy5jy0JnoMslxR5X)


