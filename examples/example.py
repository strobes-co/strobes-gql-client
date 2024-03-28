from strobes_gql_client.client import StrobesGQLClient


gql_client = StrobesGQLClient("a@wesecureapp.com", "a", "qa1.strobes.wsa-apps.com", 80, "http", verify=True|False)
list_bugs = gql_client.get_op().all_bugs(organization_id="727f30bc-05fc-4d3e-aacb-e1fcd8ed65fc", search_query="ipaddress ~ \"1\"", page_size=10)
data = gql_client.endpoint(gql_client.op)

list_all_bugs = [data]

has_next = data.get("data", {}).get("allBugs", {}).get("hasNext", False)
while has_next:
    if not data.get("data", {}).get("allBugs", {}).get("hasNext"):
        has_next = False
        break
    list_bugs = gql_client.get_op().all_bugs(organization_id="727f30bc-05fc-4d3e-aacb-e1fcd8ed65fc", search_query="ipaddress ~ \"1\"", page_size=10, after=data.get("data", {}).get("allBugs", {}).get("beforeCursor", ""))
    data = gql_client.endpoint(gql_client.op)
    list_all_bugs.append(data)

print(list_all_bugs)
