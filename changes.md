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