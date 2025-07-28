# examples/test-fetch-findings-example.py
"""
Strobes Findings Fetching Examples

This example demonstrates comprehensive security findings (vulnerabilities) fetching
from the Strobes platform with robust error handling and data validation.

Key Features:
- Robust GraphQL error handling (handles None responses, malformed data)
- Alternative query strategies for unsupported fields
- Comprehensive data validation and safety checks
- Fallback approaches for CVE/CWE/exploit queries that may fail
- Professional logging and error reporting

Data Handling Improvements:
- All GraphQL responses are checked for None values before processing
- Functions return empty lists instead of crashing on errors
- Field existence is validated before accessing nested data
- Alternative queries provided when direct field searches fail
- Graceful degradation for unsupported GraphQL schema features

Usage:
    python examples/test-fetch-findings-example.py

Note: Some advanced fields like 'cve', 'cwe', 'exploitAvailable', 'patchAvailable' 
may not be directly searchable in all GraphQL implementations. This code includes 
intelligent fallbacks and alternative approaches.
"""

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import json
from datetime import datetime
import logging

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def fetch_findings_with_query(search_query, query_description=""):
    """
    Helper function to fetch findings with proper error handling
    
    Args:
        search_query (str): The search query to execute
        query_description (str): Description for logging purposes
    
    Returns:
        list: List of findings or empty list if query fails
    """
    try:
        client = get_client()
        response = client.execute_query(
            "all_bugs",
            organization_id=enums.ORGANIZATION_ID,
            search_query=search_query
        )
        
        # Check if response is None (common GraphQL error)
        if response is None:
            print(f"  Warning: No response received for {query_description}")
            return []
        
        # Check if response has the expected structure
        if not isinstance(response, dict) or 'data' not in response:
            print(f"  Warning: Invalid response structure for {query_description}")
            return []
        
        # Extract findings with additional safety checks
        data = response.get('data')
        if data is None:
            print(f"  Warning: No data in response for {query_description}")
            return []
        
        all_bugs = data.get('allBugs')
        if all_bugs is None:
            print(f"  Warning: No allBugs in response for {query_description}")
            return []
        
        objects = all_bugs.get('objects')
        if objects is None:
            print(f"  Warning: No objects in allBugs for {query_description}")
            return []
        
        return objects
        
    except Exception as e:
        print(f"  Error fetching {query_description}: {e}")
        return []

def fetch_all_findings():
    """Fetch all security findings from organization"""
    print("=== Fetching All Findings ===")
    try:
        client = get_client()
        response = client.execute_query("all_bugs", organization_id=enums.ORGANIZATION_ID)
        findings = response.get("data", {}).get("allBugs", {}).get("objects", [])
        
        print(f"Total findings: {len(findings)}")
        
        # Show first 5 findings
        for finding in findings[:5]:
            title = finding.get('title', 'Unknown')
            severity = finding.get('severity', 'Unknown')
            cvss = finding.get('cvss', 'N/A')
            state = finding.get('state', 'Unknown')
            print(f"- {title} (Severity: {severity}, CVSS: {cvss}, State: {state})")
            
        return findings
        
    except Exception as e:
        print(f"Error fetching findings: {e}")
        return []

def fetch_findings_by_severity():
    """Fetch findings by different severity levels"""
    print("\n=== Fetching Findings by Severity ===")
    
    # Severity levels: 1=Info, 2=Low, 3=Medium, 4=High, 5=Critical
    severity_levels = {
        1: "Info",
        2: "Low", 
        3: "Medium",
        4: "High",
        5: "Critical"
    }
    
    for level_id, level_name in severity_levels.items():
        search_query = f"severity = {level_id}"
        findings = fetch_findings_with_query(search_query, f"{level_name} severity findings")
        print(f"{level_name} severity findings: {len(findings)}")

def fetch_findings_by_state():
    """Fetch findings by different states"""
    print("\n=== Fetching Findings by State ===")
    
    # Finding states: 1=Open, 2=Closed, 3=In Progress, 4=Resolved
    finding_states = {
        1: "Open",
        2: "Closed",
        3: "In Progress", 
        4: "Resolved"
    }
    
    for state_id, state_name in finding_states.items():
        search_query = f"state = {state_id}"
        findings = fetch_findings_with_query(search_query, f"{state_name} findings")
        print(f"{state_name} findings: {len(findings)}")

def fetch_findings_by_bug_level():
    """Fetch findings by bug level (asset type)"""
    print("\n=== Fetching Findings by Bug Level ===")
    
    # Bug levels: 1=Web, 2=Mobile, 3=Network, 4=Cloud, 7=Code
    bug_levels = {
        1: "Web",
        2: "Mobile",
        3: "Network",
        4: "Cloud", 
        7: "Code"
    }
    
    for level_id, level_name in bug_levels.items():
        search_query = f"bug_level = {level_id}"
        findings = fetch_findings_with_query(search_query, f"{level_name} findings")
        print(f"{level_name} findings: {len(findings)}")

def fetch_findings_by_cvss_score():
    """Fetch findings by CVSS score ranges"""
    print("\n=== Fetching Findings by CVSS Score ===")
    
    cvss_ranges = [
        ("Critical (9.0+)", "cvss >= 9.0"),
        ("High (7.0-8.9)", "cvss >= 7.0 and cvss < 9.0"),
        ("Medium (4.0-6.9)", "cvss >= 4.0 and cvss < 7.0"),
        ("Low (<4.0)", "cvss < 4.0")
    ]
    
    for range_name, search_query in cvss_ranges:
        findings = fetch_findings_with_query(search_query, range_name)
        print(f"{range_name}: {len(findings)}")

def fetch_findings_by_patterns():
    """Fetch findings using title and description patterns"""
    print("\n=== Fetching Findings by Patterns ===")
    
    patterns = [
        ("SQL Injection", 'title ~ "SQL"'),
        ("Cross-Site Scripting", 'title ~ "XSS"'),
        ("Authentication Issues", 'title ~ "Authentication"'),
        ("Authorization Issues", 'title ~ "Authorization"'),
        ("Remote Code Execution", 'title ~ "Remote Code"'),
        ("Command Injection", 'title ~ "Command"')
    ]
    
    for pattern_name, search_query in patterns:
        findings = fetch_findings_with_query(search_query, pattern_name)
        print(f"{pattern_name}: {len(findings)}")
        
        # Show first few matching findings with better error handling
        for finding in findings[:2]:
            title = finding.get('title', 'Unknown') if finding else 'Unknown'
            severity = finding.get('severity', 'N/A') if finding else 'N/A'
            print(f"  - {title} (Severity: {severity})")

def fetch_findings_by_cve_cwe():
    """
    Fetch findings by CVE and CWE identifiers
    Note: CVE and CWE fields might not be directly searchable in all GraphQL implementations
    This function includes fallback handling for unsupported queries
    """
    print("\n=== Fetching Findings by CVE/CWE ===")
    
    # Note: Some CVE/CWE queries might not be supported depending on the GraphQL schema implementation
    # We'll try these queries but handle failures gracefully
    cve_cwe_queries = [
        ("Recent 2024 CVEs", 'title ~ "CVE-2024"'),  # Search in title instead of dedicated CVE field
        ("Recent 2023 CVEs", 'title ~ "CVE-2023"'),  # Search in title instead of dedicated CVE field
        ("XSS related findings", 'title ~ "XSS"'),   # Search for XSS in title rather than CWE field
        ("SQL related findings", 'title ~ "SQL"'),   # Search for SQL in title rather than CWE field
        ("Path Traversal findings", 'title ~ "Path"'), # Search for Path in title
        ("Buffer related findings", 'title ~ "Buffer"') # Search for Buffer in title
    ]
    
    for query_name, search_query in cve_cwe_queries:
        findings = fetch_findings_with_query(search_query, query_name)
        print(f"{query_name}: {len(findings)}")
        
        # Show first finding as example if available
        if findings:
            finding = findings[0]
            title = finding.get('title', 'Unknown')
            severity = finding.get('severity', 'N/A')
            print(f"  Example: {title} (Severity: {severity})")

def fetch_findings_by_exploit_status():
    """
    Fetch findings by exploit and patch availability
    Note: These boolean fields might not be directly searchable in all implementations
    """
    print("\n=== Fetching Findings by Exploit Status ===")
    
    # Note: exploitAvailable and patchAvailable fields might not be directly searchable
    # We'll try these queries but provide fallbacks
    exploit_queries = [
        ("High CVSS (potential exploits)", "cvss >= 7.0"),  # Use CVSS as proxy for exploit potential
        ("Critical Severity (urgent patches)", "severity = 5"), # Use severity as proxy for patch priority
        ("Recently discovered (potential new exploits)", 'created >= "2024-01-01"'), # Recent findings
        ("High severity open findings", "severity >= 4 and state = 1") # High severity open issues
    ]
    
    print("Note: Using alternative queries as exploit/patch fields may not be directly searchable")
    
    for query_name, search_query in exploit_queries:
        findings = fetch_findings_with_query(search_query, query_name)
        print(f"{query_name}: {len(findings)}")

def fetch_findings_by_date():
    """Fetch findings by date ranges with improved field handling"""
    print("\n=== Fetching Findings by Date ===")
    
    # Use more reliable date fields that are commonly available
    date_queries = [
        ("Created in 2024", 'created >= "2024-01-01"'),
        ("Created in last 6 months", 'created >= "2024-07-01"'),
        ("Created in last month", 'created >= "2024-12-01"'),  # More reliable than updated field
        ("Created this year", f'created >= "{datetime.now().year}-01-01"')  # Dynamic year query
    ]
    
    for query_name, search_query in date_queries:
        findings = fetch_findings_with_query(search_query, query_name)
        print(f"{query_name}: {len(findings)}")

def fetch_findings_complex_queries():
    """Fetch findings using complex combined queries with improved error handling"""
    print("\n=== Complex Combined Queries ===")
    
    complex_queries = [
        ("Critical/High Open Web Findings", 'severity in (4, 5) and state = 1 and bug_level = 1'),
        ("High CVSS with Recent Creation", 'cvss >= 8.0 and created >= "2024-01-01"'),
        ("Open High-Severity Findings", 'state = 1 and severity >= 4'),
        ("Recent High-Severity Open Findings", 'created >= "2024-01-01" and state = 1 and severity >= 4'),
        ("SQL Injection in Any Asset", 'title ~ "SQL"'),
        ("Critical Findings", 'severity = 5')
    ]
    
    for query_name, search_query in complex_queries:
        findings = fetch_findings_with_query(search_query, query_name)
        print(f"{query_name}: {len(findings)}")
        
        # Show details for first finding if available with better error handling
        if findings and len(findings) > 0:
            finding = findings[0]
            if finding:  # Additional safety check
                title = finding.get('title', 'Unknown')
                severity = finding.get('severity', 'N/A')
                cvss = finding.get('cvss', 'N/A')
                state = finding.get('state', 'N/A')
                print(f"  Example: {title} (Severity: {severity}, CVSS: {cvss}, State: {state})")

def analyze_findings(findings):
    """Analyze findings and provide summary statistics"""
    print("\n=== Findings Analysis ===")
    
    if not findings:
        print("No findings to analyze")
        return
    
    print(f"Total findings analyzed: {len(findings)}")
    
    # Severity breakdown
    severities = {}
    for finding in findings:
        severity = finding.get('severity', 'unknown')
        severities[severity] = severities.get(severity, 0) + 1
    
    print("\nSeverity breakdown:")
    severity_names = {1: "Info", 2: "Low", 3: "Medium", 4: "High", 5: "Critical"}
    for severity, count in sorted(severities.items()):
        severity_name = severity_names.get(severity, f"Level {severity}")
        print(f"  {severity_name}: {count}")
    
    # State breakdown
    states = {}
    for finding in findings:
        state = finding.get('state', 'unknown')
        states[state] = states.get(state, 0) + 1
    
    print("\nState breakdown:")
    state_names = {1: "Open", 2: "Closed", 3: "In Progress", 4: "Resolved"}
    for state, count in sorted(states.items()):
        state_name = state_names.get(state, f"State {state}")
        print(f"  {state_name}: {count}")
    
    # Bug level breakdown
    levels = {}
    for finding in findings:
        level = finding.get('bug_level', 'unknown')
        levels[level] = levels.get(level, 0) + 1
    
    print("\nBug level breakdown:")
    level_names = {1: "Web", 2: "Mobile", 3: "Network", 4: "Cloud", 7: "Code"}
    for level, count in sorted(levels.items()):
        level_name = level_names.get(level, f"Level {level}")
        print(f"  {level_name}: {count}")
    
    # CVSS statistics
    cvss_scores = [finding.get('cvss', 0) for finding in findings if finding.get('cvss') is not None]
    if cvss_scores:
        avg_cvss = sum(cvss_scores) / len(cvss_scores)
        max_cvss = max(cvss_scores)
        min_cvss = min(cvss_scores)
        print(f"\nCVSS Statistics:")
        print(f"  Average CVSS: {avg_cvss:.2f}")
        print(f"  Highest CVSS: {max_cvss}")
        print(f"  Lowest CVSS: {min_cvss}")

def export_findings_to_json(findings, filename=None):
    """Export findings to JSON file"""
    if not findings:
        print("No findings to export")
        return None
        
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"findings_export_{timestamp}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(findings, f, indent=2, default=str)
        print(f"Exported {len(findings)} findings to {filename}")
        return filename
    except Exception as e:
        print(f"Error exporting findings: {e}")
        return None

def demonstrate_finding_details():
    """Show detailed information from finding response"""
    print("\n=== Finding Response Details ===")
    try:
        client = get_client()
        response = client.execute_query(
            "all_bugs",
            organization_id=enums.ORGANIZATION_ID,
            page_size=1  # Get just one finding for demo
        )
        findings = response.get("data", {}).get("allBugs", {}).get("objects", [])
        
        if findings:
            finding = findings[0]
            print("Sample finding fields:")
            
            # Core identifiers
            print(f"  ID: {finding.get('id')}")
            print(f"  Title: {finding.get('title')}")
            print(f"  Hash: {finding.get('hash')}")
            
            # Severity & risk
            print(f"  Severity: {finding.get('severity')}")
            print(f"  CVSS Score: {finding.get('cvss')}")
            print(f"  State: {finding.get('state')}")
            print(f"  Bug Level: {finding.get('bug_level')}")
            
            # Vulnerability details
            print(f"  Exploit Available: {finding.get('exploitAvailable')}")
            print(f"  Patch Available: {finding.get('patchAvailable')}")
            
            # Timestamps
            print(f"  Created: {finding.get('created')}")
            print(f"  Updated: {finding.get('updated')}")
            print(f"  Due Date: {finding.get('dueDate')}")
            
        else:
            print("No findings found to demonstrate")
            
    except Exception as e:
        print(f"Error demonstrating finding details: {e}")

def main():
    """
    Main function to run all finding fetching examples
    
    This function demonstrates various ways to fetch and analyze security findings.
    All functions now use improved error handling to gracefully handle GraphQL query failures.
    
    Note: Some fields like 'cve', 'cwe', 'exploitAvailable', 'patchAvailable' may not be 
    directly searchable in all GraphQL implementations. The code includes fallback strategies
    and alternative queries for such cases.
    """
    print("🔍 Strobes Findings Fetching Examples")
    print("=" * 50)
    
    # Uncomment the functions you want to test:
    
    # Basic fetching with improved error handling
    findings = fetch_all_findings()
    
    # Analyze findings (works with any findings list, even if empty)
    analyze_findings(findings)
    
    # Fetching by different criteria (all functions now have proper error handling)
    fetch_findings_by_severity()
    fetch_findings_by_state()
    fetch_findings_by_bug_level()
    fetch_findings_by_cvss_score()
    
    # Pattern-based fetching (most reliable queries)
    fetch_findings_by_patterns()
    
    # CVE/CWE fetching (with fallback strategies for unsupported fields)
    fetch_findings_by_cve_cwe()
    
    # Exploit status (with alternative queries when direct fields aren't searchable)
    fetch_findings_by_exploit_status()
    
    # Date-based queries (using reliable date fields)
    fetch_findings_by_date()
    
    # Advanced queries (simplified to avoid unsupported field combinations)
    fetch_findings_complex_queries()
    
    # Show finding details (with comprehensive error handling)
    # demonstrate_finding_details()
    
    # Export findings (only if findings exist)
    # if findings:
    #     export_findings_to_json(findings)
    
    print("\n✅ Findings fetching examples completed!")
    print("\n💡 Tips:")  
    print("  - All functions now include robust error handling for GraphQL failures")
    print("  - Some queries use alternative approaches when direct field searches aren't supported")
    print("  - Functions return empty lists instead of crashing on errors")
    print("  - Uncomment specific functions in main() to test individual scenarios")
    print("📚 For more search options, visit: https://github.com/strobes-co/ql-documentation")

if __name__ == "__main__":
    main()
