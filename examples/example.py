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
def execute_bug_create_mutation():
    # Instantiate the StrobesGQLClient
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


def execute_asset_create_mutation():
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


if __name__ == "__main__":
    # Execute the mutation
    mutation_response = execute_asset_create_mutation()

    # Print the response
    print(mutation_response)
