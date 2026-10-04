# File Uploads & CSV Imports

GraphQL file uploads can't travel over the normal JSON transport, so the client
handles them with the
[GraphQL multipart request spec](https://github.com/jaydenseric/graphql-multipart-request-spec)
under the hood. For the built-in methods below you just pass a **file path** —
the client does the rest.

> **Example scripts:** `test-upload-workspace-file-example.py`,
> `test-import-sheet-csv-example.py`,
> `test-update-bugs-fields-csv-example.py`,
> `test-add-report-attachment-example.py`

## Upload a file to a workspace

Uploads a file into an AI agent **workspace**'s storage.

```python
result = client.upload_workspace_file(
    workspace_id="6f1e...-uuid",
    file_path="notes.txt",
    path="notes/notes.txt",        # optional destination path within the workspace
)
print(result["success"], result["file"]["name"])
```

Returns `success` and a `file` object (`name`, `path`, `is_folder`, `size`,
`last_modified`, `content_type`).

## Import a CSV into a sheet / workbook

Imports CSV rows into a Strobes **sheet**. Give a `work_book_id` (and optionally
a `sheet_id`) to target an existing sheet, or a `name` to create a new one.

```python
result = client.import_csv(
    "data.csv",
    ORG,
    work_book_id=2,
    name="Imported Sheet",         # creates a new sheet when no sheet_id is given
)
print(result["success"], result["message"])
```

### Signature

```python
client.import_csv(file_path, organization_id, sheet_id=None,
                  work_book_id=None, import_override=None,
                  merge_with=None, name=None)
```

| Argument | Description |
|---|---|
| `file_path` | Path to the CSV on disk |
| `organization_id` | Your org UUID |
| `sheet_id` | Target an existing sheet |
| `work_book_id` | Workbook to import into |
| `name` | Name for a newly created sheet |
| `import_override` | Replace existing rows |
| `merge_with` | Merge strategy |

## Update finding fields from a CSV

Bulk-updates finding (bug) custom fields from a spreadsheet.

```python
result = client.update_bugs_fields_with_csv("findings-fields.csv", ORG)
```

Returns the updated findings (`bug` → list of `{id}`). Prepare the CSV with the
finding identifier column plus one column per custom-field slug you want to set.

## Add a report attachment

Uploads a file as a report attachment.

```python
result = client.add_report_attachment("appendix.pdf", ORG)
print(result["attachment"]["url"])
```

See [Reports → Report attachments](Reports#4-report-attachments) for the return
shape.

## Upload a vault document

Vault uploads currently use a small inline `requests` snippet rather than a
built-in method — see
[Vault Documents → Upload a document](Vault-Documents#upload-a-document).

## How it works (for the curious)

Each of the built-in methods builds a schema-validated GraphQL operation with an
`Upload!` variable, then serializes it into a multipart POST: the operation goes
in the `operations` part, the variable-to-file mapping in `map`, and the file as
its own part. You never have to assemble this by hand — see
`_execute_multipart_operation` in
[`client.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/client.py).

## Related

- [Reports](Reports)
- [Vault Documents](Vault-Documents)
- [Findings](Findings)
- [Python API Reference](Python-API-Reference)
