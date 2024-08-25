from strobes_gql_client.base_client import BaseClient
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.types import Type, Field, list_of
from sgqlc.types.relay import Connection, connection_args
from sgqlc.operation import Operation
from strobes_gql_client import schema
import requests

class StrobesGQLClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        session = requests.Session()
        session.verify = kwargs.get('verify', True)
        self.grapqhl_url = f'{self.app_url}api/graphql/'
        self.endpoint = RequestsEndpoint(self.grapqhl_url, self.headers, session=session)
    
    def get_op(self):
        self.op = Operation(schema.Query)
        return self.op
    
    def get_mutation_op(self):
        self.op = Operation(schema.Mutation)
        return self.op
