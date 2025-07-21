from strobes_gql_client.client import StrobesGQLClient


def get_client():
    return StrobesGQLClient(
        host="auto.in.strobes.co",
        api_token="api-key",
        verify=False,
        scheme="https",
        port=443,
    )


def fetch_bugs_with_search():
    """Example function showing how to fetch bugs with a search query"""
    client = get_client()
    return client.execute_query(
        "all_bugs", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='  severity in (1) and is_active in ("true") and alert_category not in (-1)'
    )


def fetch_bugs_by_severity():
    """Example: Fetch bugs by severity level"""
    client = get_client()
    return client.execute_query(
        "all_bugs", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='severity in (2, 3) and is_active in ("true")'
    )


def fetch_bugs_by_state():
    """Example: Fetch bugs by state (0=Open, 1=Closed, 2=In Progress)"""
    client = get_client()
    return client.execute_query(
        "all_bugs", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='state in (0) and is_active in ("true")'
    )


def fetch_bugs_by_id_range():
    """Example: Fetch bugs by ID range"""
    client = get_client()
    return client.execute_query(
        "all_bugs", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='id in ("109950", "109951", "109952") and is_active in ("true")'
    )


def fetch_bugs_by_created_date():
    """Example: Fetch bugs created in the last 7 days"""
    client = get_client()
    return client.execute_query(
        "all_bugs", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='created >= "2025-07-11" and is_active in ("true")'
    )


def fetch_bugs_complex_query():
    """Example: Complex query combining multiple criteria"""
    client = get_client()
    return client.execute_query(
        "all_bugs", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='severity in (1, 2) and state in (0) and created >= "2025-07-15" and is_active in ("true")'
    )


def fetch_assets_by_id():
    """Example: Fetch assets by specific ID"""
    client = get_client()
    return client.execute_query(
        "all_assets", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='id in (1, 2, 3)'
    )


def fetch_assets_by_sensitivity():
    """Example: Fetch assets by sensitivity level"""
    client = get_client()
    return client.execute_query(
        "all_assets", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='sensitivity in (1, 2)'
    )


def fetch_assets_by_name():
    """Example: Fetch assets by name pattern"""
    client = get_client()
    return client.execute_query(
        "all_assets", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='name contains "web" or name contains "server"'
    )


def fetch_assets_complex_query():
    """Example: Complex asset query combining multiple criteria"""
    client = get_client()
    return client.execute_query(
        "all_assets", 
        organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        search_query='sensitivity in (1) and name contains "web"'
    )


def test_function(function_name, function, search_query):
    """Test a specific function and print results"""
    print(f"🔍 {function_name}")
    print(f"Query: {search_query}")
    print("-" * 80)

    try:
        result = function()

        # Handle bugs
        if result and 'data' in result and 'allBugs' in result['data']:
            bugs = result['data']['allBugs']['objects']

            if len(bugs) > 0:
                print("\n📋 Bug Details:")
                for i, bug in enumerate(bugs, 1):
                    print(f"\n{i}. Bug ID: {bug['id']}")
                    print(f"   Title: {bug['title']}")
                    print(f"   Severity: {bug['severity']}")
                    print(f"   State: {bug['state']}")
                    print(f"   Created: {bug['created']}")
                    if bug.get('description'):
                        print(f"   Description: {bug['description']}")
                    if bug.get('cvss'):
                        print(f"   CVSS: {bug['cvss']}")
                    if bug.get('cve'):
                        print(f"   CVE: {bug['cve']}")
                    if bug.get('cwe'):
                        print(f"   CWE: {bug['cwe']}")
                    if bug.get('asset'):
                        print(f"   Asset: {bug['asset']}")
                    if bug.get('assigned_to'):
                        print(f"   Assigned To: {bug['assigned_to']}")
                    if bug.get('reported_by'):
                        print(f"   Reported By: {bug['reported_by']}")
                    if bug.get('bug_tags'):
                        print(f"   Tags: {bug['bug_tags']}")
                    if bug.get('links'):
                        print(f"   Links: {bug['links']}")
                    if bug.get('exploit_available'):
                        print(f"   Exploit Available: {bug['exploit_available']}")
                    if bug.get('patch_available'):
                        print(f"   Patch Available: {bug['patch_available']}")
                    if bug.get('sla_violated'):
                        print(f"   SLA Violated: {bug['sla_violated']}")
                    if bug.get('prioritization_score'):
                        print(f"   Prioritization Score: {bug['prioritization_score']}")
                    if bug.get('trend'):
                        print(f"   Trend: {bug['trend']}")
                    if bug.get('is_wormable'):
                        print(f"   Is Wormable: {bug['is_wormable']}")
                    if bug.get('zero_day_available'):
                        print(f"   Zero Day Available: {bug['zero_day_available']}")
                    if bug.get('cisa_due_date'):
                        print(f"   CISA Due Date: {bug['cisa_due_date']}")
                    if bug.get('epss_score'):
                        print(f"   EPSS Score: {bug['epss_score']}")
                    if bug.get('port'):
                        print(f"   Port: {bug['port']}")
                    if bug.get('engagements'):
                        print(f"   Engagements: {bug['engagements']}")
                    if bug.get('connector'):
                        print(f"   Connector: {bug['connector']}")
                    if bug.get('tracker'):
                        print(f"   Tracker: {bug['tracker']}")
                    print("-" * 60)
            else:
                print("❌ No bugs found")

        # Handle assets
        elif result and 'data' in result and 'allAssets' in result['data']:
            assets = result['data']['allAssets']['objects']

            if len(assets) > 0:
                print("\n📋 Asset Details:")
                for i, asset in enumerate(assets, 1):
                    print(f"\n{i}. Asset ID: {asset['id']}")
                    print(f"   Name: {asset['name']}")
                    if asset.get('sensitivity'):
                        print(f"   Sensitivity: {asset['sensitivity']}")
                    if asset.get('type'):
                        print(f"   Type: {asset['type']}")
                    if asset.get('exposed'):
                        print(f"   Exposed: {asset['exposed']}")
                    if asset.get('target'):
                        print(f"   Target: {asset['target']}")
                    if asset.get('ipaddress'):
                        print(f"   IP Address: {asset['ipaddress']}")
                    if asset.get('mac_address'):
                        print(f"   MAC Address: {asset['mac_address']}")
                    if asset.get('hostname'):
                        print(f"   Hostname: {asset['hostname']}")
                    if asset.get('cpe'):
                        print(f"   CPE: {asset['cpe']}")
                    if asset.get('os'):
                        print(f"   OS: {asset['os']}")
                    if asset.get('cloud_type'):
                        print(f"   Cloud Type: {asset['cloud_type']}")
                    print("-" * 60)
            else:
                print("❌ No assets found")
        else:
            print("❌ No data returned or unexpected response format")

    except Exception as e:
        print(f"❌ Error: {e}")

    print("\n" + "="*100 + "\n")


if __name__ == "__main__":
    print("🚀 Running All Search Query Examples\n")

    # Test essential search query functions
    functions_to_test = [
        # ("fetch_bugs_with_search", fetch_bugs_with_search,
        #  'severity in (1) and is_active in ("true") and alert_category not in (-1)'),

        # ("fetch_bugs_by_severity", fetch_bugs_by_severity,
        #  'severity in (2, 3) and is_active in ("true")'),

        # ("fetch_bugs_by_state", fetch_bugs_by_state,
        #  'state in (0) and is_active in ("true")'),

        # ("fetch_bugs_by_id_range", fetch_bugs_by_id_range,
        #  'id in ("109950", "109951", "109952") and is_active in ("true")'),

        # ("fetch_bugs_by_created_date", fetch_bugs_by_created_date,
        #  'created >= "2025-07-11" and is_active in ("true")'),

        # ("fetch_bugs_complex_query", fetch_bugs_complex_query,
        #  'severity in (1, 2) and state in (0) and created >= "2025-07-15" and is_active in ("true")'),

        # ("fetch_assets_by_id", fetch_assets_by_id,
        #  'id in (1, 2, 3)'),

        # ("fetch_assets_by_sensitivity", fetch_assets_by_sensitivity,
        #  'sensitivity in (1, 2)'),

        # ("fetch_assets_by_name", fetch_assets_by_name,
        #  'name contains "web" or name contains "server"'),

        # ("fetch_assets_complex_query", fetch_assets_complex_query,
        #  'sensitivity in (1) and name contains "web"')
    ]

    for function_name, function, search_query in functions_to_test:
        test_function(function_name, function, search_query) 