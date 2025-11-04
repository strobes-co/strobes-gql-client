from strobes_gql_client.client import StrobesGQLClient


def get_client():
    return StrobesGQLClient(
        host="auto.in.strobes.co",
        api_token="<token>",
        verify=True,
    )


def fetch_assets():
    client = get_client()
    return client.execute_query(
        "all_assets", organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6"
    )


def fetch_bugs():
    client = get_client()
    return client.execute_query(
        "all_bugs", organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6"
    )


def execute_web_bug_create_mutation():
    client = get_client()
    bug_create_fields = {
        "title": "Cross-Site Request Forgery (CSRF)",
        "description": "A CSRF vulnerability in the product update form allows attackers to change product details without authorization.",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "bug_level": 2,
        "mitigation": "Implement anti-CSRF tokens or use the HTTP Strict-Transport-Security (HSTS) header.",
        "steps_to_reproduce": """1. Log into the application as a regular user.
                                 2. Access a malicious website hosting a crafted CSRF payload that targets the product update form.
                                 3. The payload will be submitted without your knowledge, changing product details.""",
        "web": """{
            "affected_endpoints": ["/product/update"], 
            "request_responses": [
                {
                    "request": "POST /product/update HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nproduct_id=123&name=NewProductName&description=NewDescription",
                    "response": "HTTP/1.1 302 Found\\r\\nLocation: /product/123"
                },
                {
                    "request": "GET /product/123 HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\n\\r\\n",
                    "response": "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n<html>Product Updated</html>"
                }
            ],
            "request": "POST /product/update HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nproduct_id=123&name=NewProductName&description=NewDescription",
            "response": "HTTP/1.1 302 Found\\r\\nLocation: /product/123"
        }""",
        "selected_team": 123,
        "cwe_list": ["352"],
        "cve_list": [],
        "cvss": 6.5,
        "severity": 3,
        "attack_vector": "Network",
        "engagement_id": "8c48af59-cdc7-44d7-924a-c6e044840288",
        "tags": ["csrf", "web"],
        "bug_attachment_list": [],
        "selected_assets": [12, 34],
        "cloud_asset_type": 1,
        "engagement_ids": [],
    }
    return client.execute_mutation("bug_create", **bug_create_fields)


def execute_code_bug_create_mutation():
    client = get_client()
    bug_create_fields = {
        "title": "SQL Injection Vulnerability in User Input Sanitization",
        "description": "Unsanitized user input in the 'process_query' function allows SQL injection attacks.",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "bug_level": 1,
        "mitigation": "Use parameterized queries or properly escape user input.",
        "steps_to_reproduce": """
            1. Navigate to the vulnerable endpoint (e.g., /search?q=test)
            2. Append a single quote (') to the query parameter value
            3. Observe error messages indicating SQL syntax errors
            """,
        "code": """
            {
                "vulnerable_code": "query = \\"SELECT * FROM users WHERE name = '{}'\\".format(user_input)",
                "start_line_number": 25,
                "end_line_number": 25,
                "file_name": "app.py" 
            }
            """,
        "cwe_list": ["89"],
        "cve_list": [],
        "cvss": 7.5,
        "severity": 4,
        "tags": ["sql-injection", "code-vulnerability"],
        "selected_assets": [123],
        "cloud_asset_type": 1,
    }
    return client.execute_mutation("bug_create", **bug_create_fields)


def execute_package_bug_create_mutation():
    client = get_client()
    bug_create_fields = {
        "title": "Log4Shell Vulnerability in log4j Library",
        "description": """A critical remote code execution vulnerability (CVE-2021-44228) exists in the Apache Log4j logging library. 
        Exploitation allows attackers to gain control of affected systems.""",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "bug_level": 6,
        "mitigation": """Upgrade Log4j to version 2.17.0 or later. If upgrading is not possible, follow mitigation guidelines provided by Apache.""",
        "steps_to_reproduce": """1. Send a specially crafted log message to a vulnerable application.
                                 2. The message triggers the Log4j vulnerability, allowing remote code execution.""",
        "package": """{
            "fixed_version":"2.17.0",
            "installed_version":"2.14.1",
            "package_name":"Apache Log4j",
            "affected_versions":"2.0-beta9 to 2.14.1"
        }""",
        "cwe_list": ["502"],
        "cve_list": ["CVE-2021-44228"],
        "cvss": 10.0,
        "severity": 5,
        "tags": ["log4shell", "rce"],
        "selected_assets": [123],
        "cloud_asset_type": 1,
        "custom_fields": """{
            "exploitability": "Easy",
            "impact": "Critical"
        }""",
    }
    return client.execute_mutation("bug_create", **bug_create_fields)


def execute_cloud_aws_bug_create_mutation():
    client = get_client()
    bug_create_fields = {
        "title": "Unrestricted Access to S3 Bucket",
        "description": "An Amazon S3 bucket is configured to allow public access, potentially exposing sensitive data.",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 5,
        "mitigation": "Disable public access and enforce appropriate access controls on the S3 bucket.",
        "steps_to_reproduce": """1. Attempt to access the S3 bucket URL directly from a web browser.
                                 2. If the contents of the bucket are accessible without authentication, the vulnerability is confirmed.""",
        "cloud": '{"region": "us-west-2", "aws_account_id": "123456789012", "aws_resource_id": "arn:aws:s3:::example-bucket", "aws_category": "Compute", "aws_type": 2}',
        "cwe_list": ["528"],
        "cve_list": [],
        "cvss": 7.5,
        "severity": 4,
        "tags": ["s3", "aws", "misconfiguration"],
        "selected_assets": [669],
        "cloud_asset_type": 2,
    }
    return client.execute_mutation("bug_create", **bug_create_fields)


def execute_cloud_gcp_bug_create_mutation():
    client = get_client()
    gcp_bug_create_fields = {
        "title": "Exposed Google Cloud Storage Bucket",
        "description": "A Google Cloud Storage bucket is misconfigured and publicly accessible, potentially exposing sensitive data.",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 5,
        "mitigation": "Restrict access to the Google Cloud Storage bucket and enforce appropriate permissions.",
        "steps_to_reproduce": """1. Attempt to access the GCS bucket URL directly from a web browser.
                                2. If the contents of the bucket are accessible without authentication, the vulnerability is confirmed.""",
        "cloud": '{"gcp_project_id": "your-project-id", "gcp_resource_id": "your-bucket-id", "gcp_type": 1}',
        "cwe_list": ["284"],
        "cve_list": [],
        "cvss": 8.0,
        "severity": 4,
        "tags": ["gcs", "google-cloud", "misconfiguration"],
        "selected_assets": [671],
        "cloud_asset_type": 4,
    }
    return client.execute_mutation("bug_create", **gcp_bug_create_fields)


def execute_cloud_azure_bug_create_mutation():
    client = get_client()
    azure_bug_create_fields = {
        "title": "Exposed Azure Blob Storage Container",
        "description": "An Azure Blob Storage container is misconfigured and publicly accessible, potentially exposing sensitive data.",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 5,
        "mitigation": "Restrict access to the Azure Blob Storage container and enforce appropriate permissions.",
        "steps_to_reproduce": """1. Attempt to access the Azure Blob Storage container URL directly from a web browser.
                                2. If the contents of the container are accessible without authentication, the vulnerability is confirmed.""",
        "cloud": '{"azure_resource": "your-container-name", "azure_category": "Storage"}',
        "cwe_list": ["284"],
        "cve_list": [],
        "cvss": 7.5,
        "severity": 4,
        "tags": ["azure", "blob-storage", "misconfiguration"],
        "selected_assets": [670],
        "cloud_asset_type": 3,
    }
    return client.execute_mutation("bug_create", **azure_bug_create_fields)


def execute_web_asset_create_mutation():
    client = get_client()
    asset_create_fields = {
        "name": "E-commerce Storefront",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "sensitivity": 4,
        "exposed": 1,
        "type": 1,
        "tags": ["ecommerce", "frontend"],
        "url": "https://shop.example.com",
    }
    return client.execute_mutation("create_asset", **asset_create_fields)


def execute_mobile_asset_create_mutation():
    client = get_client()
    asset_create_fields = {
        "name": "Mobile Banking App (v1.2.3)",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "sensitivity": 5,
        "exposed": 1,
        "type": 2,
        "tags": ["banking", "android"],
        "package": "com.example.mobilebanking",
    }
    return client.execute_mutation("create_asset", **asset_create_fields)


def execute_network_asset_with_single_ip_create_mutation():
    client = get_client()
    asset_create_fields = {
        "name": "Office Firewall (HQ)",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "sensitivity": 4,
        "exposed": 1,
        "type": 3,
        "os": "Cisco IOS XE",
        "cpe": "cpe:/o:cisco:ios_xe:16.9.1",
        "hostname": "fw-hq",
        "mac_address": "00:1A:2B:3C:4D:5E",
        "tags": ["firewall", "network"],
        "ipaddress": "192.168.1.1",
    }
    return client.execute_mutation("create_asset", **asset_create_fields)


def execute_network_asset_with_multiple_ip_create_mutation():
    client = get_client()
    asset_create_fields = {
        "name": "Web Server Cluster",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "sensitivity": 4,
        "exposed": 1,
        "type": 3,
        "os": "Linux",
        "cpe": "cpe:/o:linux:linux_kernel",
        "hostname": "web-cluster",
        "mac_address": "00:25:90:67:89:AB",
        "tags": ["webserver", "load-balancer"],
        "ipaddress_list": [
            "192.168.1.10",
            "192.168.1.11",
            "192.168.1.12",
        ],
        "excluded_ipaddress_list": ["192.168.1.123"],
    }
    return client.execute_mutation("create_asset", **asset_create_fields)


def execute_create_engagement_with_multiple_services():
    client = get_client()
    engagement_create_fields = {
        "name": "testeng001",
        "organization_id": "2f1a818a-7426-4cdb-b52c-efac1d81bba6",
        "vendor_code": "wes-9637708",
        "scheduled_date": "2025-07-01",
        "delivery_date": "2025-07-16",
        "plans": 1,
        "document_ids": [],
        "subscribed_services": [
            "Cloud Security",
            "Secure Code Review",
            "Web Application Penetration Test",
            "Mobile Application Pentesting",
            "Network VAPT",
        ],
        "assessment_data": '{"Cloud Security":[{"search_query":"id in (35663,35664,35665,35666,35667)"},{"asset_id":"35663","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35664","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35665","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35666","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35667","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""}],"Secure Code Review":[{"search_query":"id in (35658,35659,35660,35661,35662)"},{"asset_id":"35658","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35659","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35660","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35661","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""},{"asset_id":"35662","asset_type":3,"scheduled_date":"2025-07-01","delivery_date":"2025-07-16","vpn_accounts":"","test_accounts":"","instructions":"","scope":""}]}',
        "prerequisites_data": '[{"id":null,"title":"preqtest1","description":"desc 1","assigned_to":[533759],"due_date":"2025-07-02","attachments":[],"order_index":1,"is_completed":false}]',
        "fields": '{"internal_info":"testint","f":"f","custom_text":"cut text","custom_number":1,"custom_date":"2025-07-16","custom_boolean":"true","custom_select":"multiselct","custom_multiselect":["five"],"custom_email":"test@gmail.com","custom_user":["533759"],"custom_url":"https://auto.in.strobes.co/"}',
        # "is_self_managed": False,
        # "include_related_assets": False,
    }

    return client.execute_mutation("create_engagement", **engagement_create_fields)


execute_create_engagement_with_multiple_services()
