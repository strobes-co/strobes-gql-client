Complete, exhaustive list of every mutation exposed on the public endpoint (15 total):

| Mutation | Key args |
|---|---|
| `uploadWorkspaceFile` | file, path, workspaceId |
| `importCsv` | file, importOverride, mergeWith, name, organizationId, sheetId, workBookId |
| `addVaultAttachment` | engagementId, file, organizationId, prerequisite |
| `addReportTemplate` | htmlData, mode, organizationId, templateName, type |
| `generateReport` | assetSearchQuery, customData, engagementId, organizationId, password, reportName, searchQuery, templateId, viewId |
| `addReportAttachment` | file, organizationId |
| `createEngagement` | assessmentData, credentialIds, customStatus, deliveryDate, documentIds, executiveSummary, fields, includeRelatedAssets, isSelfManaged, name, organizationId, plans, prerequisitesData, scheduledDate, **state**, subscribedServices, vendorCode |
| `addBugComment` | attachments, bugId, comment, internal, organizationId |
| `addEngagementComment` | attachments, comment, engagementId, organizationId |
| `bugCreate` | (finding fields) |
| `bugBulkUpdate` | organizationId, searchQuery, severity, **state** |
| `updateBugsFieldsWithCsv` | file, organizationId |
| `exportBugs` | organizationId, searchQuery |
| `createAsset` | (asset fields) |
| `exportAssets` | organizationId, searchQuery |


we need to add support for engagement state update mutation 
i thought we had it


check first we have public api calls in strobes folder 

if no support add the full support

---

**Resolved:** `client.py` had no wrapper for updating an engagement's state after
creation — `createEngagement` only sets it at creation time, and neither
`updateEngagement` nor `bulkUpdateEngagements` had a case in
`execute_mutation`'s field-selection logic (so calling either would build a
mutation with no subselection, which the backend must have rejected).

Added support for both, since they cover different use cases:
- `update_engagement` — single engagement by `engagement_id`, full field set
  (name, dates, assignees, executive summary, etc., not just state).
- `bulk_update_engagements` — many engagements at once by `engagement_ids`,
  mirroring the existing `bug_bulk_update` pattern.

Changes: `ENGAGEMENT_FULL_FIELDS` / `ENGAGEMENT_CUSTOM_STATUS_FIELDS` +
`_select_engagement()` helper in `strobes_gql_client/client.py`, wired into
`execute_mutation` for both mutation names; new
`examples/test-update-engagement-state-example.py` demonstrating both paths.

Note: this was implemented against `schema.py`/`schema.json` (the full
internal schema) since the live `/api/public/graphql/` endpoint
(`path.in.strobes.local`, per the uncommitted `enums.py` change) wasn't
reachable from this sandbox to re-confirm the two mutations are actually
permitted there — worth a quick live test before relying on this in
production, since the "15 total" public-mutation list above doesn't
currently list either one.

---

**Follow-up (confirmed 403 live, root-caused, fixed in the `strobes` backend
repo):** running `test-update-engagement-state-example.py` against the real
`/api/public/graphql/` confirmed `bulkUpdateEngagements` was rejected with
`403 "You do not have permission to perform this action."` — checked the
`strobes` repo and found the mutation genuinely didn't exist on the public
GraphQL schema at all:

- `strobes/graphql/public/engagements/schema.py` registered only
  `create_engagement` — `updateEngagement`/`bulkUpdateEngagements` exist only
  on the *internal* schema (`strobes/graphql/engagements/schema.py:549`),
  never forked into the public one.
- `strobes/connectors/permissions.py`'s `MasterKeyAccessPermission` (a
  substring allowlist checked against the raw request body before GraphQL
  even runs) already listed `"updateEngagement"` — dead/aspirational, since
  the field it names didn't exist — but had no `"bulkUpdateEngagements"`
  entry at all, hence the clean 403 before GraphQL validation.

Fixed in the `strobes` repo (separate PR from this client):
- Added `PublicUpdateEngagementMutation` / `PublicBulkUpdateEngagementsMutation`
  in `strobes/graphql/public/engagements/mutations.py`, deliberately scoped to
  `state`/`custom_status` only (the internal mutation also touches assignees,
  documents, prerequisites, assessment data — out of scope for the public
  surface). Registered both in `PublicEngagementMutations`
  (`strobes/graphql/public/engagements/schema.py`).
- Added `"bulkUpdateEngagements"` to the `MasterKeyAccessPermission`
  allowlist in `strobes/connectors/permissions.py`.
- Fixed the public-contract docstring in `strobes/graphql/public/schema.py`
  (was also missing `bugBulkUpdate`, which was already registered).

Needs a backend restart to pick up the new resolvers before re-running
`examples/test-update-engagement-state-example.py`.
---

## Asset custom-field updates (bulkUpdateAssetCustomFieldMutation)

Added `StrobesGQLClient.bulk_update_asset_custom_fields(organization_id,
search_query, fields)` plus `examples/test-update-asset-custom-fields-example.py`.

Background: the public endpoint only had `createAsset`; there was no way to
change custom-field values on assets that already exist. The backend forked
the internal `BulkUpdateAssetCustomFields` mutation into
`strobes/graphql/public/assets/mutations.py` under the **same GraphQL name and
return field as the internal one** (`bulkUpdateAssetCustomFieldMutation`,
returning `asset: [AssetType]`), so this client's generated `schema.py` (built
from the internal schema) already described it and needed no regeneration.
`"bulkUpdateAssetCustomFieldMutation"` was also added to the
`MasterKeyAccessPermission` allowlist.

Args: `organizationId: UUID!`, `searchQuery: String!` (RQL, must be non-empty),
`fields: GenericScalar!` (slug -> value). Up to 100 matching assets are updated
inline and returned; above that the backend queues a Celery task and returns an
empty `asset` list.

Follow-up: `fields` is now sent as a GraphQL variable (`$fields: GenericScalar!`)
rather than inlined into the query. Inlining a dict produced JSON-quoted object
keys, which the GraphQL parser rejects with "Expected Name, found String".
The dedicated method no longer routes through `execute_mutation`.

## AI workspaces & agents (public)

Added pinned selections in `client.py` for the AI workspace / agent (pulse)
operations now exposed on the public endpoint by `strobes.graphql.public.agents`
(re-exposing the internal workspace/pulse/system-agent resolvers under MasterKey
auth). `schema.py` already carried these types/fields (generated from the
internal schema), so only selection pinning was needed.

New operations:
- Queries: `workspaces`, `workspace`, `workspace_stats`, `workspace_tasks`,
  `available_agents`, `threads`, `thread`, `messages`, `active_run`.
- Mutations: `create_workspace`, `archive_workspace`, `create_workspace_task`,
  `cancel_workspace_task`, `retry_workspace_task`, `create_thread`,
  `send_message`, `cancel_run`, `start_background_run`.

See `examples/test-agents-workspaces-example.py`. Consumed by `strobes-agents-mcp`.

### Update: workspace outputs & workflow control

Added pinned selections + `schema.py` arg fixes for more public agent ops:
- Queries: `workspace_findings`, `workspace_assets` (exposed as PLAIN LISTS on
  the public endpoint to match this client; `schema.py` args extended with
  page/page_size/search/severity|type/state), `workspace_files`,
  `workspace_file_download_url`, `workspace_download_url`, `workspace_chats`,
  `workflow_templates`, `workspace_workflow`.
- Mutations: `create_workspace_from_template`, `pause_workflow`,
  `resume_workflow`, `cancel_workflow`.

### Final surface (simplification)

The agent surface was consolidated to a task-centric model (chat == tasks). The
standalone thread/chat/run ops (`threads`, `thread`, `messages`, `active_run`,
`workspace_chats`, `create_thread`, `send_message`, `cancel_run`,
`start_background_run`) were removed from the public endpoint and this client in
favour of a single new query **`workspace_task_messages(workspace_id, task_id,
limit, offset)`** (a task's run-thread messages). Final client-pinned agent ops:
- Queries: `workspaces`, `workspace`, `workspace_stats`, `workspace_tasks`,
  `workspace_task_messages`, `workspace_findings`, `workspace_assets`,
  `workspace_files`, `workspace_file_download_url`, `workspace_download_url`,
  `workflow_templates`, `workspace_workflow`, `available_agents`.
- Mutations: `create_workspace`, `archive_workspace`,
  `create_workspace_from_template`, `create_workspace_task`,
  `cancel_workspace_task`, `retry_workspace_task`, `pause_workflow`,
  `resume_workflow`, `cancel_workflow`.
