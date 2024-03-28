from strobes_gql_client.client import StrobesGQLClient


s = StrobesGQLClient("test.in.strobes.co", 80, "http", "xxxxxxxxxxxxxxxxxxxxx")
list_bugs = s.get_op().all_bugs(organization_id="d973bf5f-f922-4759-9247-2437e2af7bbb")
data = s.endpoint(s.op)
print(data)