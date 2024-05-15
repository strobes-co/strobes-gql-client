from strobes_gql_client.client import StrobesGQLClient


# s = StrobesGQLClient(
#     "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
# )
# print(s.endpoint(s.get_mutation_op()))
# print(dir(s.get_mutation_op()))
# list_bugs = s.get_op().all_bugs(organization_id="d15a82e7-2be0-40ab-ab18-44983d46ffe6")
# data = s.endpoint(s.op)
# print(data)


# Define a function to execute the mutation
def execute_web_bug_create_mutation():
    # Instantiate the StrobesGQLClient
    # You can add custom fields in bug by adding kwarg in bug_create_fields e.g "custom_fields": '{"test": "hellotest"}',
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    bug_create_fields = {
        "title": "hello1",
        "description": "hegfe ehfie ",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 4,
        "mitigation": "iwheuiw wihwifhw wihdiwh",
        "steps_to_reproduce": "jeuw wkhdiwhfiwh",
        "web": '{"affected_endpoints": [""], "request": "", "response": ""}',
        "selected_team": 1,
        "cwe_list": [],
        "cve_list": ["CVE-2024-23842", "CVE-2024-26234"],
        "cvss": 7.5,
        "severity": 2,
        "attack_vector": "jwdbjw",
        "engagement_id": "8c48af59-cdc7-44d7-924a-c6e044840288",
        "tags": ["abs", "tvs"],
        "bug_attachment_list": [2, 3],
        "network": '{"port_address":"3000","cpe":["mlmd","vdvd"], "port": ""}',
        "selected_assets": [648, 647, 646],
        "cloud_asset_type": 1,
        "engagement_ids": [],
    }

    # Execute the mutation
    bug_create = op.bug_create(**bug_create_fields)

    prepared_mutation = "mutation {\n" + str(bug_create) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_code_bug_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    bug_create_fields = {
        "title": "codebug001",
        "description": "hegfe ehfie ",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 1,
        "mitigation": "iwheuiw wihwifhw wihdiwh",
        "steps_to_reproduce": "jeuw wkhdiwhfiwh",
        "code": '{"vulnerable_code":"wodowj\\nwodjwod\\nwodwodkwodk","start_line_number":12,"end_line_number":14,"file_name":"test.py","commit":""}',
        "cwe_list": [],
        "cve_list": ["CVE-2024-29745", "CVE-2024-29748"],
        "cvss": 7.5,
        "severity": 2,
        "tags": ["abs", "tvs"],
        "selected_assets": [651],
        "cloud_asset_type": 1,
    }

    # Execute the mutation
    bug_create = op.bug_create(**bug_create_fields)

    prepared_mutation = "mutation {\n" + str(bug_create) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_package_bug_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    bug_create_fields = {
        "title": "packagebug001",
        "description": "hegfe ehfie ",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 6,
        "mitigation": "iwheuiw wihwifhw wihdiwh",
        "steps_to_reproduce": "jeuw wkhdiwhfiwh",
        "package": '{"fixed_version":"2.25.0","installed_version":"2.23.0","package_name":"Requests (Python HTTP library)","affected_versions":"2.20.0, 2.24.0, 2.21.0, 2.22.0, 2.23.0"}',
        "cwe_list": [],
        "cve_list": ["CVE-2024-29745", "CVE-2024-29748"],
        "cvss": 7.5,
        "severity": 2,
        "tags": ["abs", "tvs"],
        "selected_assets": [651],
        "cloud_asset_type": 1,
        "custom_fields": "{}",
    }

    # Execute the mutation
    bug_create = op.bug_create(**bug_create_fields)

    prepared_mutation = "mutation {\n" + str(bug_create) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_cloud_bug_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    bug_create_fields = {
        "title": "cloudbug001",
        "description": "hegfe ehfie ",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "bug_level": 5,
        "mitigation": "iwheuiw wihwifhw wihdiwh",
        "steps_to_reproduce": "jeuw wkhdiwhfiwh",
        "cloud": '{"region":"asia-east1-a","gcp_resource_id":"test-resource","gcp_project_id":"xyz"}',
        "cwe_list": ["1041", "1048"],
        "cve_list": ["CVE-2024-29745", "CVE-2024-29748"],
        "cvss": 7.5,
        "severity": 2,
        "tags": ["abs", "tvs"],
        "selected_assets": [667],
        "cloud_asset_type": 4, 
    }

    # Execute the mutation
    bug_create = op.bug_create(**bug_create_fields)

    prepared_mutation = "mutation {\n" + str(bug_create) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_web_asset_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    asset_create_fields = {
        "name": "hello1",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "sensitivity": 4,
        "exposed": 1,
        "type": 1,
        "tags": ["abs", "tvs"],
        "url": "http://test1.in.strobes.local/organizations/d15a82e7-2be0-40ab-ab18-44983d46ffe6/apps/ptaas/assets?query=",
    }

    # Execute the mutation
    create_asset = op.create_asset(**asset_create_fields)

    prepared_mutation = "mutation {\n" + str(create_asset) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_mobile_asset_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    asset_create_fields = {
        "name": "hello1",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "sensitivity": 3,
        "exposed": 1,
        "type": 2,
        "tags": ["dw", "wd"],
        "package": "http://test1.in.strobes.local/organizations/d15a82e7-2be0-40ab-ab18-44983d46ffe6/apps/ptaas/assets?query=",
    }

    # Execute the mutation
    create_asset = op.create_asset(**asset_create_fields)

    prepared_mutation = "mutation {\n" + str(create_asset) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_network_asset_with_single_ip_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    asset_create_fields = {
        "name": "networkasset001",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "sensitivity": 3,
        "exposed": 1,
        "type": 3,
        "os": "Ubuntu",
        "cpe": "cpe:/o:microsoft:windows_vista:6.0:sp1:~-~home_premium~-~x64~-",
        "hostname": "strobes.local",
        "mac_address": "00:B0:D0:63:C2:26",
        "tags": ["multiip", "network"],
        "ipaddress": "192.158.1.38",
    }

    # Execute the mutation
    create_asset = op.create_asset(**asset_create_fields)

    prepared_mutation = "mutation {\n" + str(create_asset) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_network_asset_with_multiple_ip_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    asset_create_fields = {
        "name": "networkasset002",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "sensitivity": 3,
        "exposed": 1,
        "type": 3,
        "tags": ["asset", "cloud"],
        "ipaddress_list": ["192.168.1.1", "10.0.0.1", "203.0.113.42", "66.220.144.0"],
        "excluded_ipaddress_list": ["198.51.100.42", "8.8.8.8"],
    }

    # Execute the mutation
    create_asset = op.create_asset(**asset_create_fields)

    prepared_mutation = "mutation {\n" + str(create_asset) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


def execute_cloud_asset_create_mutation():
    # Instantiate the StrobesGQLClient
    client = StrobesGQLClient(
        "test1.in.strobes.local", 80, "http", "f2f83a24a660ce1a2df03dd64f5b88fb020bb66b"
    )

    # Get the mutation operation
    op = client.get_mutation_op()

    # Define the mutation fields
    asset_create_fields = {
        "name": "cloudasset001",
        "organization_id": "d15a82e7-2be0-40ab-ab18-44983d46ffe6",
        "sensitivity": 3,
        "exposed": 1,
        "type": 4,
        "tags": ["asset", "cloud"],
        "cloud_type": 4,
    }

    # Execute the mutation
    create_asset = op.create_asset(**asset_create_fields)

    prepared_mutation = "mutation {\n" + str(create_asset) + "\n}"

    result = client.endpoint(prepared_mutation)

    return result


if __name__ == "__main__":
    # Execute the mutation
    mutation_response = execute_cloud_bug_create_mutation()

    # Print the response
    print(mutation_response)
