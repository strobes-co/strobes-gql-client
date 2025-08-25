from strobes_gql_client.client import StrobesGQLClient
import json
from datetime import datetime
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CONNECTION_CONFIG, QUERY_CONFIG

def get_client():
    return StrobesGQLClient(**CONNECTION_CONFIG)

def fetch_bugs(organization_id=None, search_query=None):
    """Fetch bugs with optional search query"""
    if organization_id is None:
        organization_id = QUERY_CONFIG["organization_id"]
    try:
        client = get_client()
        
        # Only pass search_query if it's not None
        if search_query:
            result = client.execute_query("all_bugs", organization_id=organization_id, search_query=search_query)
        else:
            result = client.execute_query("all_bugs", organization_id=organization_id)
        
        if result and "data" in result and "allBugs" in result["data"]:
            return result["data"]["allBugs"]["objects"]
        return []
    except Exception as e:
        print(f"Error fetching bugs: {e}")
        return []

def fetch_by_severity(severity_levels):
    """Fetch bugs by severity levels"""
    levels_str = ", ".join(map(str, severity_levels))
    return fetch_bugs(search_query=f"severity in ({levels_str})")

def fetch_by_state(states):
    """Fetch bugs by state(s)"""
    states_str = ", ".join(map(str, states))
    return fetch_bugs(search_query=f"state in ({states_str})")

def fetch_by_bug_level(bug_levels):
    """Fetch bugs by bug level(s)"""
    levels_str = ", ".join(map(str, bug_levels))
    return fetch_bugs(search_query=f"bug_level in ({levels_str})")

def fetch_by_cvss_score(min_score=None, max_score=None):
    """Fetch bugs by CVSS score range"""
    if min_score is not None and max_score is not None:
        return fetch_bugs(search_query=f"cvss >= {min_score} and cvss <= {max_score}")
    elif min_score is not None:
        return fetch_bugs(search_query=f"cvss >= {min_score}")
    elif max_score is not None:
        return fetch_bugs(search_query=f"cvss <= {max_score}")
    return []

def fetch_by_title_pattern(pattern):
    """Fetch bugs by title pattern"""
    return fetch_bugs(search_query=f'title ~ "{pattern}"')

def fetch_by_cve(cve_id):
    """Fetch bugs by CVE ID"""
    return fetch_bugs(search_query=f'cve ~ "{cve_id}"')

def fetch_by_cwe(cwe_id):
    """Fetch bugs by CWE ID"""
    return fetch_bugs(search_query=f'cwe ~ "{cwe_id}"')

def analyze_bugs(bugs):
    """Quick bug analysis"""
    if not bugs:
        print("No bugs found")
        return
    
    print(f"\n🐛 Found {len(bugs)} bugs")
    
    # Severity breakdown
    severities = {}
    for bug in bugs:
        severity = bug.get('severity', 'unknown')
        severities[severity] = severities.get(severity, 0) + 1
    
    print("Bug severities:")
    for severity, count in severities.items():
        severity_name = {1: "Low", 2: "Medium", 3: "High", 4: "Critical"}.get(severity, f"Level {severity}")
        print(f"  {severity_name}: {count}")
    
    # State breakdown
    states = {}
    for bug in bugs:
        state = bug.get('state', 'unknown')
        states[state] = states.get(state, 0) + 1
    
    print("Bug states:")
    for state, count in states.items():
        state_name = {1: "Open", 2: "Closed", 3: "In Progress", 4: "Resolved"}.get(state, f"State {state}")
        print(f"  {state_name}: {count}")
    
    # Bug level breakdown
    levels = {}
    for bug in bugs:
        level = bug.get('bug_level', 'unknown')
        levels[level] = levels.get(level, 0) + 1
    
    print("Bug levels:")
    for level, count in levels.items():
        level_name = {1: "Web", 2: "Mobile", 3: "Network", 4: "Cloud", 7: "Code"}.get(level, f"Level {level}")
        print(f"  {level_name}: {count}")

def export_to_json(bugs, filename=None):
    """Export bugs to JSON"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bugs_export_{timestamp}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(bugs, f, indent=2, default=str)
        print(f"✅ Exported to {filename}")
        return filename
    except Exception as e:
        print(f"Error exporting: {e}")
        return None

def main():
    """Main function"""
    print("🐛 Bug Fetching Examples")
    
    # Fetch all bugs
    all_bugs = fetch_bugs()
    analyze_bugs(all_bugs)
    
    # Examples
    high_severity = fetch_by_severity([3, 4])
    open_bugs = fetch_by_state([1])
    web_bugs = fetch_by_bug_level([1])
    critical_cvss = fetch_by_cvss_score(min_score=9.0)
    sql_bugs = fetch_by_title_pattern("SQL")
    
    print(f"\nHigh severity bugs: {len(high_severity)}")
    print(f"Open bugs: {len(open_bugs)}")
    print(f"Web bugs: {len(web_bugs)}")
    print(f"Critical CVSS bugs: {len(critical_cvss)}")
    print(f"SQL-related bugs: {len(sql_bugs)}")
    
    # Export
    export_to_json(all_bugs)

if __name__ == "__main__":
    main() 