from strobes_gql_client.base_client import BaseClient
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.types import Type, Field, list_of
from sgqlc.types.relay import Connection, connection_args
from sgqlc.operation import Operation
from strobes_gql_client.schema import schema

class StrobesGQLClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grapqhl_url = f'{self.app_url}api/graphql/'
        self.endpoint = RequestsEndpoint(self.grapqhl_url, self.headers)
    
    def get_op(self):
        self.op = Operation(schema.Query)
        return self.op
