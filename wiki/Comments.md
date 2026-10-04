# Comments

Comments live on two kinds of object: **findings** (bugs) and **engagements**.
One query reads them; two mutations create them.

> **Example script:** `test-comments-example.py`

## Read comments

Use the `all_comments` query. Pass **either** `bug_id` **or** `engagement_id` to
scope to one object — passing both is an error. Omitting both returns every
comment on the findings and engagements you can see.

### On a finding

```python
resp = client.execute_query(
    "all_comments",
    organization_id=ORG,
    bug_id=12345,
    page=1,
    page_size=10,
    order_by=["-created"],          # newest first
)
result = resp["data"]["allComments"]

print("Total:", result["totalCount"])
for c in result["objects"]:
    author = c.get("commentedBy") or {}
    print(f"[{c['id']}] {c['comment']} — {author.get('email')}")
```

### On an engagement

```python
resp = client.execute_query(
    "all_comments",
    organization_id=ORG,
    engagement_id="0c5c2d61-4a3a-4a58-9b4b-4a1b9f0f2f11",
)
comments = resp["data"]["allComments"]["objects"]
```

`all_comments` is **offset-paginated** — see [Core Concepts](Core-Concepts#pagination).

### Arguments

| Argument | Type | Description |
|---|---|---|
| `organization_id` | UUID! | Required |
| `bug_id` | Int | Only comments on this finding |
| `engagement_id` | UUID | Only comments on this engagement |
| `internal` | Boolean | `True` = internal only · `False` = external only · omit = both |
| `search_query` | String | RQL, e.g. `comment ~ "credentials"` |
| `order_by` | [String] | e.g. `["-created"]` |
| `page` / `page_size` | Int | Offset pagination |

## Add a comment to a finding

```python
result = client.execute_mutation(
    "add_bug_comment",
    organization_id=ORG,
    bug_id=12345,
    comment="Retested — the fix holds. Closing.",
    internal=False,            # optional, defaults to False
    attachments=[10, 11],      # optional attachment IDs
)
print(result["comment"]["id"])
```

> `internal=True` is honoured only for organization **owners and managers**. For
> anyone else, the comment is stored as external — matching the Strobes UI.

## Add a comment to an engagement

```python
result = client.execute_mutation(
    "add_engagement_comment",
    organization_id=ORG,
    engagement_id="0c5c2d61-4a3a-4a58-9b4b-4a1b9f0f2f11",
    comment="Scope confirmed with the client — kickoff Monday.",
    attachments=[12],          # optional attachment IDs
)
```

Engagement comments fire the `ON_ENGAGEMENT_COMMENT` automation hook and the
usual notifications, exactly like a comment posted from the UI.

## Response fields (`CommentType`)

Both the query and the mutations return a comment object with:

| Field | Type | Notes |
|---|---|---|
| `id` | ID! | Comment identifier |
| `comment` | String! | Body text |
| `internal` | Boolean! | Whether it's internal-only |
| `bug_id` | Int | Set for finding comments (null for engagement comments) |
| `engagement_id` | UUID | Set for engagement comments (null for finding comments) |
| `commented_by` | UserType | Author: `id`, `email`, `first_name`, `last_name` |
| `attachments` | [AttachmentType] | `id`, `attachment_name`, `attachment_size`, `caption`, `url` |
| `created` / `updated` | DateTime! | Timestamps |

## Related

- [Findings](Findings)
- [Engagements](Engagements)
- [Search Query Language](Search-Query-Language)
