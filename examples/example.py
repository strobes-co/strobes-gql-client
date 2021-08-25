from strobes_gql_client.client import StrobesGQLClient


s = StrobesGQLClient("a@wesecureapp.com", "a", "qa1.strobes.wsa-apps.com", 80, "http")

list_bugs = s.get_op().all_bugs(organization_id="727f30bc-05fc-4d3e-aacb-e1fcd8ed65fc", search_query="ipaddress ~ \"1\"")

data = s.endpoint(s.op)

print(data)
