import requests
from strobes_gql_client import enums

class BaseClient:
    def __init__(
        self,
        host: str = enums.APP_HOST,
        port: int = enums.APP_PORT,
        scheme: str = enums.APP_SCHEME,
        api_token: str = None,
        verify: bool = True,
    ):
        self.app_url = f"{scheme}://{host}:" f"{str(port)}/"
        self.headers = {
                    "Authorization": f"token {api_token}",
                    "user-agent": enums.USER_AGENT,
                }
