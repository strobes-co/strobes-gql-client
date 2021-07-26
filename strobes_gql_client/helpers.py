import requests
from strobes_gql_client.exceptions import LoginFailure


def get_jwt_token(url: str, email: str, password: str) -> str:
    r = requests.post(f"{url}api/v1/login/",
                      json={"email": email, "password": password})
    resp = r.json()
    if 'access' in resp:
        return resp['access']
    raise LoginFailure
