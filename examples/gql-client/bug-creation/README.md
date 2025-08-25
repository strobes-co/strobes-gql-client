# Bug Creation Scripts

This folder contains scripts for creating different types of security findings/bugs in the Strobes GraphQL API.

## Files

### 1. `create_web_bugs.py`
- **Purpose**: Creates web application security findings (bug_level: 2)
- **Features**:
  - Dynamically fetches web assets (type 1) from the organization
  - Creates multiple web vulnerability types:
    - SQL Injection
    - Cross-Site Scripting (XSS)
    - Path Traversal
    - Cross-Site Request Forgery (CSRF)
  - Links bugs to existing web assets
  - Includes detailed vulnerability descriptions and mitigation steps
- **Usage**: `python3 create_web_bugs.py`

### 2. `create_code_bugs.py`
- **Purpose**: Creates code security findings (bug_level: 1)
- **Features**:
  - Dynamically fetches code assets (type 7) from the organization
  - Creates multiple code vulnerability types:
    - Command Injection
    - Reflected XSS
    - Insecure Direct Object Reference (IDOR)
  - Links bugs to existing code assets
  - Includes code snippets and line numbers in findings
- **Usage**: `python3 create_code_bugs.py`

### 3. `create_network_bugs.py`
- **Purpose**: Creates network security findings (bug_level: 4)
- **Features**:
  - Dynamically fetches network assets (type 3) from the organization
  - Creates multiple network vulnerability types:
    - Open SSH Port (22) Exposed to Internet
    - Weak SNMP Community String
    - Telnet Service Enabled
    - FTP Anonymous Access Enabled
    - Outdated Network Device Firmware
  - Links bugs to existing network assets
  - Includes port information and CPE data
- **Usage**: `python3 create_network_bugs.py`

## Bug Types and Levels

- **Code Bugs (bug_level: 1)**: Source code vulnerabilities
- **Web Bugs (bug_level: 2)**: Web application vulnerabilities
- **Network Bugs (bug_level: 4)**: Network device and protocol vulnerabilities

## Common Features

All scripts include:
- Dynamic asset fetching from the organization
- Multiple vulnerability types per script
- Detailed vulnerability descriptions
- Step-by-step reproduction instructions
- Mitigation recommendations
- CWE and CVE references
- CVSS scoring
- Severity classification
- Tagging for categorization
- Error handling and logging

## Vulnerability Types Covered

### Web Vulnerabilities
- SQL Injection (CWE-89)
- Cross-Site Scripting (CWE-79)
- Path Traversal (CWE-22)
- Cross-Site Request Forgery (CWE-352)

### Code Vulnerabilities
- Command Injection (CWE-78)
- Reflected XSS (CWE-79)
- Insecure Direct Object Reference (CWE-639)

### Network Vulnerabilities
- Information Exposure (CWE-200)
- Weak Authentication (CWE-1188)
- Cleartext Transmission (CWE-319)
- Insecure File Permissions (CWE-552)
- Outdated Software (CWE-754)

## Prerequisites

- Strobes GraphQL API access
- Valid API token
- Existing assets in the organization
- Python 3.x with required dependencies
- Network connectivity to the Strobes server

## Usage Workflow

1. **Create Assets First**: Use scripts from the `asset-creation` folder
2. **Create Bugs**: Use scripts from this `bug-creation` folder
3. **Verify Results**: Check the Strobes dashboard for created findings 