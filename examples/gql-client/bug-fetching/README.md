# Bug Fetching Examples

This directory contains optimized scripts for fetching bugs (vulnerabilities) from the Strobes platform using the GraphQL API.

## Features

- **Fetch all bugs** from an organization
- **Filter by severity** (Low, Medium, High, Critical)
- **Filter by state** (Open, Closed, In Progress, Resolved)
- **Filter by bug level** (Web, Mobile, Network, Cloud, Code)
- **Filter by CVSS score** (range queries)
- **Search by title pattern** (regex matching)
- **Search by CVE/CWE IDs**
- **Export to JSON** with timestamps
- **Quick analysis** with breakdowns

## Usage

### Basic Usage

```python
from fetch_all_bugs import fetch_bugs, analyze_bugs, export_to_json

# Fetch all bugs
all_bugs = fetch_bugs()
analyze_bugs(all_bugs)

# Export to JSON
export_to_json(all_bugs)
```

### Filtering Examples

```python
# Fetch high and critical severity bugs
high_critical = fetch_by_severity([3, 4])

# Fetch open bugs only
open_bugs = fetch_by_state([1])

# Fetch web application bugs
web_bugs = fetch_by_bug_level([1])

# Fetch bugs with CVSS score >= 9.0
critical_cvss = fetch_by_cvss_score(min_score=9.0)

# Fetch bugs with CVSS score between 7.0 and 8.9
medium_high = fetch_by_cvss_score(min_score=7.0, max_score=8.9)

# Search bugs by title pattern
xss_bugs = fetch_by_title_pattern("XSS")

# Search by CVE ID
cve_bugs = fetch_by_cve("CVE-2023-1234")

# Search by CWE ID
cwe_bugs = fetch_by_cwe("CWE-79")
```

## Available Functions

```python
# Main function
fetch_bugs(organization_id="uuid", search_query="string")

# Filtering functions
fetch_by_severity(severity_levels)           # [1,2,3,4]
fetch_by_state(states)                       # [0,1,2,3,4]
fetch_by_bug_level(bug_levels)               # [1,2,3,4,7]
fetch_by_cvss_score(min_score=None, max_score=None)
fetch_by_title_pattern(pattern)              # regex pattern
fetch_by_cve(cve_id)                         # CVE ID
fetch_by_cwe(cwe_id)                         # CWE ID

# Utility functions
analyze_bugs(bugs)                           # Print analysis
export_to_json(bugs, filename=None)          # Export to JSON
```

## Bug Severity Levels

- **1**: Low
- **2**: Medium  
- **3**: High
- **4**: Critical

## Bug States

- **0**: Unknown/Default
- **1**: Open
- **2**: Closed
- **3**: In Progress
- **4**: Resolved

## Bug Levels

- **1**: Web
- **2**: Mobile
- **3**: Network
- **4**: Cloud
- **7**: Code

## Output Format

The script provides:

1. **Console output** with bug counts and breakdowns
2. **JSON export** with full bug details including:
   - Basic info (title, description, severity, state)
   - Technical details (CVSS, CVE, CWE, attack vector)
   - Metadata (created, updated, assigned to)
   - Related data (asset, scan, attachments)

## Example Output

```
🐛 Bug Fetching Examples

🐛 Found 10 bugs
Bug severities:
  Critical: 3
  High: 7
Bug states:
  Open: 10
Bug levels:
  Web: 6
  Code: 4

High severity bugs: 10
Open bugs: 10
Web bugs: 6
Critical CVSS bugs: 3
SQL-related bugs: 2
✅ Exported to bugs_export_20250724_132741.json
```

## Configuration

Update the connection details in `get_client()` function:

```python
def get_client():
    return StrobesGQLClient(
        host="your-strobes-host",
        api_token="your-api-token",
        scheme="https",  # or "http"
        port=443,        # or your port
        verify=True,
    )
```

## Dependencies

- `strobes_gql_client`
- `json`
- `datetime`

## Notes

- **Separate functions** - Each filtering type has its own function
- **Consistent pattern** - Follows the same structure as asset fetching
- **Simple API** - Easy to understand and use
- **Handles null queries** - Automatically handles GraphQL null search query issues
- **Error handling** - Robust operation with proper exception handling
- **JSON exports** - Include timestamps for easy file management 