# Vault Documents

The vault stores documents for your organization — reports, scope letters,
credentials files, and engagement attachments. This guide covers uploading and
listing them.

> **Example scripts:** `test-create-vault-example.py`,
> `test-fetch-vaults-example.py`

## Upload a document

Vault uploads use the `addVaultAttachment` mutation, which takes a file. Because
GraphQL file uploads need a multipart request (not plain JSON), you send it with
a small `requests` helper:

```python
import json
import requests
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

client = StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def upload_file(filepath, engagement_id=None, is_prerequisite=False):
    operations = {
        "query": (
            "mutation AddVaultAttachment($file: Upload!, $organizationId: UUID!) {"
            "  addVaultAttachment(file: $file, organizationId: $organizationId) {"
            "    vault { id documentName documentSize }"
            "  }"
            "}"
        ),
        "variables": {"file": None, "organizationId": enums.ORGANIZATION_ID},
    }
    map_ = {"0": ["variables.file"]}

    with open(filepath, "rb") as f:
        files = {"0": (filepath, f, "application/octet-stream")}
        response = requests.post(
            f"{client.app_url}api/public/graphql/",
            headers={
                "Authorization": f"token {enums.API_TOKEN}",
                "user-agent": enums.USER_AGENT,
            },
            data={"operations": json.dumps(operations), "map": json.dumps(map_)},
            files=files,
        )
    return response.json()

print(upload_file("path/to/document.pdf"))
```

> 🎥 **Video:** [Uploading a vault document](https://app.arcade.software/flows/F98XvHFDjmyEZMW8Z6xN/view)

### Fields

| Field | Required | Description |
|---|---|---|
| `file` | ✅ | The file to upload |
| `organization_id` | ✅ | Your organization UUID |
| `engagement_id` | — | Attach the document to an engagement (UUID, or empty/None) |
| `is_prerequisite` | — | Mark as an engagement prerequisite document |

### Example response

```json
{
  "data": {
    "addVaultAttachment": {
      "vault": { "id": "123", "documentName": "requirements.txt", "documentSize": 49 }
    }
  }
}
```

> For uploading to an **AI agent workspace** (a different destination), use the
> built-in `client.upload_workspace_file(...)` method instead — see
> [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports#upload-a-file-to-a-workspace).

## List vault documents

Use the `all_vault_attachments` query (offset-paginated).

```python
resp = client.execute_query("all_vault_attachments", organization_id=ORG)
docs = resp["data"]["allVaultAttachments"]["objects"]

for d in docs:
    who = (d.get("attachedBy") or {})
    name = f"{who.get('firstName','')} {who.get('lastName','')}".strip()
    print(f"- {d.get('document_name')} (by {name}, on {d.get('created')})")
```

### Search

```python
resp = client.execute_query(
    "all_vault_attachments",
    organization_id=ORG,
    search_query='document_name ~ "test"',
)
```

> 🎥 **Videos:** [List all documents](https://app.arcade.software/share/5O3FR2cQV1X6Sb4gmOFv) ·
> [Search documents](https://app.arcade.software/share/0atq1gLJ1ttmIAtUXts9)

## Related

- [Engagements](Engagements) — attach documents to an engagement
- [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports)
- [Reports](Reports) — report attachments
