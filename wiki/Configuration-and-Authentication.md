# Configuration & Authentication

Before you can make a call, the client needs three pieces of information.

| Value | What it is | Example |
|---|---|---|
| **Host** | Your Strobes platform domain | `mycorp.strobes.co`, `mycorp.in.strobes.co`, `mycorp.us.strobes.co` |
| **API Token** | A per-user token that authenticates every request | `9f3c…` (long alphanumeric string) |
| **Organization ID** | The UUID of the organization you're working in | `0c5c2d61-4a3a-4a58-9b4b-4a1b9f0f2f11` |

## Get your API token and organization ID

1. Open your Strobes platform in a browser and log in.
2. Go to **Settings** (top-right).
3. Select **API Access**.
4. Click **Generate Token** and copy the token.
5. Note the **Organization ID** shown on the same page.

> 🎥 **Video:** [Getting your API token and org ID](https://app.arcade.software/share/h36MBeei7wJP7vf1diYs)

> **Treat the token like a password.** It grants API access to your
> organization's data. Don't commit it to source control or paste it into
> shared channels. Prefer environment variables (below) over hard-coding.

## How the client reads credentials

The client is constructed explicitly with a host and token:

```python
StrobesGQLClient(host="mycorp.strobes.co", api_token="<token>")
```

Every request is sent to `https://<host>/api/public/graphql/` with the header
`Authorization: token <api_token>`.

`strobes_gql_client/enums.py` provides convenient defaults so you don't have to
repeat these values. There are two common ways to supply them.

### Option A — Environment variables (recommended)

`enums.py` reads two environment variables:

```python
# strobes_gql_client/enums.py (excerpt)
API_TOKEN       = os.getenv('STROBES_API_TOKEN')
ORGANIZATION_ID = os.getenv('STROBES_ORGANIZATION_ID')
APP_HOST        = "automate.in.strobes.co"   # change to your host
```

Set them in your shell:

```bash
export STROBES_API_TOKEN="<your-api-token>"
export STROBES_ORGANIZATION_ID="<your-org-uuid>"
```

Then in code:

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)
```

> Set `APP_HOST` in `enums.py` to your own domain, or pass `host=` explicitly
> when you construct the client.

### Option B — Edit `enums.py` directly

```python
# strobes_gql_client/enums.py
USER_AGENT      = "strobes-python-gql-client"
APP_PORT        = 443
APP_SCHEME      = "https"
APP_HOST        = "mycorp.strobes.co"          # your domain
API_TOKEN       = "your_api_token_here"        # your token
ORGANIZATION_ID = "your_organization_uuid"     # your org id
```

Leave `APP_SCHEME` and `APP_PORT` as-is unless you're on a non-standard setup.

## Constructor options

```python
StrobesGQLClient(host, api_token, verify=True)
```

| Argument | Default | Description |
|---|---|---|
| `host` | — | Your platform domain (no scheme, no trailing slash). |
| `api_token` | — | The API token from Settings → API Access. |
| `verify` | `True` | TLS certificate verification. Set `False` only for a host with a self-signed cert (not recommended in production). |

The scheme (`https`) and port (`443`) come from `enums.py` and rarely need
changing.

## Test connectivity

**Run the bundled script:**

```bash
python examples/test-connectivity-example.py
```

**Or do it inline:**

```python
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

resp = client.execute_query("all_assets", organization_id=enums.ORGANIZATION_ID)
assets = resp.get("data", {}).get("allAssets", {}).get("objects", [])
print(f"Connected — {len(assets)} assets visible")
```

If an asset count prints without error, you're ready. If not, see
[Troubleshooting](Troubleshooting).

## Next steps

- [Quickstart](Quickstart)
- [Core Concepts](Core-Concepts)
