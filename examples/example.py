from strobes_gql_client.client import StrobesGQLClient


def fetch_assets():
    s = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    s.get_op().all_assets(organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6")
    return s.endpoint(s.op)


def fetch_bugs():
    s = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    s.get_op().all_bugs(organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6")
    return s.endpoint(s.op)


# Define a function to execute the mutation
def execute_web_bug_create_mutation():
    """Creates a new web bug in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    bug_create_fields = {
        "title": "Cross-Site Request Forgery (CSRF)",
        "description": "A CSRF vulnerability in the product update form allows attackers to change product details without authorization.",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",  # Replace with your organization ID
        "bug_level": 2,  # Web
        "mitigation": "Implement anti-CSRF tokens or use the HTTP Strict-Transport-Security (HSTS) header.",
        "steps_to_reproduce": """1. Log into the application as a regular user.
                                 2. Access a malicious website hosting a crafted CSRF payload that targets the product update form.
                                 3. The payload will be submitted without your knowledge, changing product details.""",
        "web": """{
            "affected_endpoints": ["/product/update"], 
            "request": "POST /product/update HTTP/1.1\\r\\nHost: vulnerable-website.com\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\n\\r\\nproduct_id=123&name=NewProductName&description=NewDescription",
            "response": "HTTP/1.1 302 Found\\r\\nLocation: /product/123"
        }""",
        "selected_team": 123,
        "cwe_list": ["352"],  # CWE-352: Cross-Site Request Forgery (CSRF)
        "cve_list": [],
        "cvss": 6.5,  # High
        "severity": 3,  # Medium
        "attack_vector": "Network",
        "engagement_id": "8c48af59-cdc7-44d7-924a-c6e044840288",
        "tags": ["csrf", "web"],
        "bug_attachment_list": [],
        "selected_assets": [12, 34],
        "cloud_asset_type": 1,  # Others (not applicable for web bugs)
        "engagement_ids": [],
    }

    bug_create = op.bug_create(**bug_create_fields)
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_code_bug_create_mutation():
    """Creates a new code bug in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "xxxxxxxxxxxxxxxx"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    bug_create_fields = {
        "title": "SQL Injection Vulnerability in User Input Sanitization",
        "description": "Unsanitized user input in the 'process_query' function allows SQL injection attacks.",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "bug_level": 1,  # Code
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
        "cwe_list": [
            "89"
        ],  # CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
        "cve_list": [],  # No associated CVEs yet
        "cvss": 7.5,
        "severity": 4,  # High
        "tags": ["sql-injection", "code-vulnerability"],
        "selected_assets": [123],  # Replace with the relevant asset ID
        "cloud_asset_type": 1,  # Others (not applicable for code bugs)
    }

    bug_create = op.bug_create(**bug_create_fields)  # Create the bug object
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_package_bug_create_mutation():
    """Creates a new package bug in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    bug_create_fields = {
        "title": "Log4Shell Vulnerability in log4j Library",
        "description": """A critical remote code execution vulnerability (CVE-2021-44228) exists in the Apache Log4j logging library. 
        Exploitation allows attackers to gain control of affected systems.""",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",
        "bug_level": 6,  # Package
        "mitigation": """Upgrade Log4j to version 2.17.0 or later. If upgrading is not possible, follow mitigation guidelines provided by Apache.""",
        "steps_to_reproduce": """1. Send a specially crafted log message to a vulnerable application.
                                 2. The message triggers the Log4j vulnerability, allowing remote code execution.""",
        "package": """{
            "fixed_version":"2.17.0",
            "installed_version":"2.14.1",
            "package_name":"Apache Log4j",
            "affected_versions":"2.0-beta9 to 2.14.1"
        }""",
        "cwe_list": ["502"],  # Deserialization of Untrusted Data
        "cve_list": ["CVE-2021-44228"],
        "cvss": 10.0,
        "severity": 5,  # Critical
        "tags": ["log4shell", "rce"],
        "selected_assets": [123],  # Replace with the relevant asset ID
        "cloud_asset_type": 1,  # Others (not applicable for package bugs)
        "custom_fields": """{
            "exploitability": "Easy",
            "impact": "Critical"
        }""",  # Example of additional custom fields (JSON string)
    }

    bug_create = op.bug_create(**bug_create_fields)
    try:
        result = client.endpoint(op)
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_cloud_aws_bug_create_mutation():
    """Creates a new cloud bug in Strobes."""
    # aws_account_id: Replace with the account ID
    # aws_resource_id: Replace with the bucket ARN

    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    bug_create_fields = {
        "title": "Unrestricted Access to S3 Bucket",
        "description": "An Amazon S3 bucket is configured to allow public access, potentially exposing sensitive data.",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",  # Replace with your organization ID
        "bug_level": 5,  # Cloud
        "mitigation": "Disable public access and enforce appropriate access controls on the S3 bucket.",
        "steps_to_reproduce": """1. Attempt to access the S3 bucket URL directly from a web browser.
                                 2. If the contents of the bucket are accessible without authentication, the vulnerability is confirmed.""",
        "cloud": '{"region": "us-west-2", "aws_account_id": "123456789012", "aws_resource_id": "arn:aws:s3:::example-bucket", "aws_category": "Compute", "aws_type": 2}',
        "cwe_list": ["528"],  # CWE-528: Improper Access Control
        "cve_list": [],  # No associated CVEs yet
        "cvss": 7.5,
        "severity": 4,  # High
        "tags": ["s3", "aws", "misconfiguration"],
        "selected_assets": [669],  # Replace with the relevant asset ID
        "cloud_asset_type": 2,  # AWS
    }

    bug_create = op.bug_create(**bug_create_fields)  # Create the bug object
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_cloud_gcp_bug_create_mutation():
    """Creates a new cloud bug in Strobes."""

    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    gcp_bug_create_fields = {
        "title": "Exposed Google Cloud Storage Bucket",
        "description": "A Google Cloud Storage bucket is misconfigured and publicly accessible, potentially exposing sensitive data.",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",  # Replace with your organization ID
        "bug_level": 5,  # Cloud
        "mitigation": "Restrict access to the Google Cloud Storage bucket and enforce appropriate permissions.",
        "steps_to_reproduce": """1. Attempt to access the GCS bucket URL directly from a web browser.
                                2. If the contents of the bucket are accessible without authentication, the vulnerability is confirmed.""",
        "cloud": '{"gcp_project_id": "your-project-id", "gcp_resource_id": "your-bucket-id", "gcp_type": 1}',  # GCP type 1 for storage
        "cwe_list": ["284"],  # CWE-284: Improper Access Control
        "cve_list": [],  # No associated CVEs yet
        "cvss": 8.0,  # Example CVSS score
        "severity": 4,  # High
        "tags": ["gcs", "google-cloud", "misconfiguration"],
        "selected_assets": [671],  # Replace with the relevant asset ID
        "cloud_asset_type": 4,  # GCP
    }

    bug_create = op.bug_create(**gcp_bug_create_fields)  # Create the bug object
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_cloud_azure_bug_create_mutation():
    """Creates a new cloud bug in Strobes."""

    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    azure_bug_create_fields = {
        "title": "Exposed Azure Blob Storage Container",
        "description": "An Azure Blob Storage container is misconfigured and publicly accessible, potentially exposing sensitive data.",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",  # Replace with your organization ID
        "bug_level": 5,  # Cloud
        "mitigation": "Restrict access to the Azure Blob Storage container and enforce appropriate permissions.",
        "steps_to_reproduce": """1. Attempt to access the Azure Blob Storage container URL directly from a web browser.
                                2. If the contents of the container are accessible without authentication, the vulnerability is confirmed.""",
        "cloud": '{"azure_resource": "your-container-name", "azure_category": "Storage"}',  # Azure category "Storage"
        "cwe_list": ["284"],  # CWE-284: Improper Access Control
        "cve_list": [],  # No associated CVEs yet
        "cvss": 7.5,  # Example CVSS score
        "severity": 4,  # High
        "tags": ["azure", "blob-storage", "misconfiguration"],
        "selected_assets": [670],  # Replace with the relevant asset ID
        "cloud_asset_type": 3,  # Azure
    }

    bug_create = op.bug_create(**azure_bug_create_fields)  # Create the bug object
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_web_asset_create_mutation():
    """Creates a new web asset in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    asset_create_fields = {
        "name": "E-commerce Storefront",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",  # Replace with your organization ID
        "sensitivity": 4,  # Moderately sensitive (1-5 scale)
        "exposed": 1,  # Exposed to the internet
        "type": 1,  # Web asset
        "tags": ["ecommerce", "frontend"],
        "url": "https://shop.example.com",
    }
    create_asset = op.create_asset(**asset_create_fields)
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_mobile_asset_create_mutation():
    """Creates a new mobile asset in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    asset_create_fields = {
        "name": "Mobile Banking App (v1.2.3)",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",  # Replace with your organization ID
        "sensitivity": 5,  # Highly sensitive (financial data)
        "exposed": 1,  # Exposed to the internet
        "type": 2,  # Mobile asset
        "tags": ["banking", "android"],
        "package": "com.example.mobilebanking",  # Example bundle ID
    }
    create_asset = op.create_asset(**asset_create_fields)
    try:
        result = client.endpoint(op)
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_network_asset_with_single_ip_create_mutation():
    """Creates a new network asset with a single IP in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    asset_create_fields = {
        "name": "Office Firewall (HQ)",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",  # Replace with your organization ID
        "sensitivity": 4,  # Moderately sensitive
        "exposed": 1,  # Exposed to the internet
        "type": 3,  # Network asset
        "os": "Cisco IOS XE",
        "cpe": "cpe:/o:cisco:ios_xe:16.9.1",  # Example CPE
        "hostname": "fw-hq",
        "mac_address": "00:1A:2B:3C:4D:5E",
        "tags": ["firewall", "network"],
        "ipaddress": "192.168.1.1",
    }

    create_asset = op.create_asset(**asset_create_fields)

    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_network_asset_with_multiple_ip_create_mutation():
    """Creates a new network asset with multiple IPs in Strobes."""

    client = StrobesGQLClient(
        "tata.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()

    asset_create_fields = {
        "name": "Web Server Cluster",
        "organization_id": "d3d2a591-944b-47dc-b8d6-eee7c8f6ed02",  # Replace with your organization ID
        "sensitivity": 4,  # Moderately sensitive
        "exposed": 1,  # Exposed to the internet
        "type": 3,  # Network asset
        "os": "Linux",
        "cpe": "cpe:/o:linux:linux_kernel",  # Example CPE
        "hostname": "web-cluster",
        "mac_address": "00:25:90:67:89:AB",
        "tags": ["webserver", "load-balancer"],
        "ipaddress_list": [
            "192.168.1.10",
            "192.168.1.11",
            "192.168.1.12",
        ],  # Multiple IP addresses
        "excluded_ipaddress_list": ["192.168.1.123"],  # Example of excluded IP
    }

    create_asset = op.create_asset(**asset_create_fields)

    try:
        result = client.endpoint(op)
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_aws_cloud_asset_create_mutation():
    """Creates a new aws cloud asset in Strobes."""

    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()
    asset_create_fields = {
        "name": "Production Database (RDS Instance)",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",  # Replace with your organization ID
        "sensitivity": 5,  # Highly sensitive (contains customer data)
        "exposed": 0,  # Not directly exposed to the internet
        "type": 4,  # Cloud asset
        "tags": ["database", "rds", "production"],
        "cloud_type": 2,  # AWS
    }
    create_asset = op.create_asset(**asset_create_fields)
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_azure_cloud_asset_create_mutation():
    """Creates a new azure cloud asset in Strobes."""

    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()
    asset_create_fields = {
        "name": "my-azure-vm",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",  # Replace with your organization ID
        "sensitivity": 5,  # Highly sensitive (contains customer data)
        "exposed": 0,  # Not directly exposed to the internet
        "type": 4,  # Cloud asset
        "tags": ["database", "rds", "production"],
        "cloud_type": 3,  # AZURE
    }
    create_asset = op.create_asset(**asset_create_fields)
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)


def execute_gcp_cloud_asset_create_mutation():
    """Creates a new gcp cloud asset in Strobes."""

    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )  # Replace placeholders with your credentials
    op = client.get_mutation_op()
    asset_create_fields = {
        "name": "my-gcp-instance",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",  # Replace with your organization ID
        "sensitivity": 5,  # Highly sensitive (contains customer data)
        "exposed": 0,  # Not directly exposed to the internet
        "type": 4,  # Cloud asset
        "tags": ["database", "rds", "production"],
        "cloud_type": 4,  # GCP
    }
    create_asset = op.create_asset(**asset_create_fields)
    try:
        result = client.endpoint(op)  # Execute the mutation directly
        print("Mutation Result:", result)
        return result
    except Exception as e:
        print("Error:", e)
