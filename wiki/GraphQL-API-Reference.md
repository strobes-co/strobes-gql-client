# GraphQL API Reference

This page documents the Strobes **public** GraphQL surface as used by the
client — the queries and mutations exposed at `/api/public/graphql/`, their
GraphQL (camelCase) names, arguments, and return types.

> **Public vs. internal schema.** The bundled `schema.py` is generated from the
> full *internal* schema and contains far more types than the public endpoint
> exposes. Selecting internal-only fields against the public endpoint is
> rejected, which is why the client pins specific field selections per
> operation (see the `*_FULL_FIELDS` constants in `client.py`). The operations
> below are the public ones the client is built around.

Argument types follow GraphQL conventions: `!` = required (non-null), `[T]` =
list of `T`. In Python you pass these as snake_case keyword arguments
(`organizationId` → `organization_id`).

---

## Queries

### `allAssets` → `AssetCursorPaginatedType`

Cursor-paginated list of assets.

| Argument | Type |
|---|---|
| `organizationId` | UUID! |
| `searchQuery` | String |
| `orderBy` | [String] |
| `groupId` | Int |
| `pageSize` | Int |
| `after` / `before` | String |

Returns `{ objects: [AssetType], hasNext, hasPrevious, lastCursor, beforeCursor }`.

### `asset` → `AssetType`

A single asset by `id` (Int/ID).

### `allBugs` → `BugCursorPaginatedType`

Cursor-paginated list of findings.

| Argument | Type |
|---|---|
| `organizationId` | UUID! |
| `searchQuery` | String |
| `orderBy` | [String] |
| `pageSize` | Int |
| `after` / `before` | String |

Returns `{ objects: [BugType], hasNext, hasPrevious, lastCursor, beforeCursor }`.

### `allEngagements` → `EngagementPaginatedType`

Offset-paginated list of engagements.

| Argument | Type |
|---|---|
| `organizationId` | UUID! |
| `searchQuery` | String |
| `orderBy` | [String] |
| `assetId` | Int |
| `page` / `pageSize` | Int |

Returns `{ objects: [EngagementType], page, pageSize, totalPages, totalCount, hasNext, hasPrev }`.

### `allComments` → `CommentPaginatedType`

Offset-paginated list of comments on a finding or engagement.

| Argument | Type |
|---|---|
| `organizationId` | UUID! |
| `bugId` | Int |
| `engagementId` | UUID |
| `internal` | Boolean |
| `searchQuery` | String |
| `orderBy` | [String] |
| `page` / `pageSize` | Int |

### `allVaultAttachments` → vault paginated type

Offset-paginated list of vault documents. Args: `organizationId`,
`searchQuery`, `page`, `pageSize`.

### `allConfigurations` → paginated `ConfigurationsFieldType`

Connector configurations. Args: `organizationId`, `orderBy`, `searchQuery`,
`page`, `pageSize`.

### `allLogs` → paginated `AllScanLogType`

Scan logs. Args: `organizationId`, `searchQuery`, `orderBy`, `page`,
`pageSize`. (No `logType` filter on the public endpoint.)

### `allTemplates` → paginated `TemplateType`

Report templates. Args: `organizationId`, `templateId`, `searchQuery`, `page`,
`pageSize`.

### `previewReport` → String

Rendered report HTML. Args: `organizationId`, `templateId`, `reportName`,
`searchQuery`, `assetSearchQuery`.

### `downloadReport` → `ReportType`

Fetch a generated report/export by id. Args: `organizationId`, `exportId`.

---

## Mutations

The public endpoint exposes a deliberately small, allow-listed set of mutations.

### Assets

#### `createAsset`
Create an asset. Required: `organizationId`, `name`, `type`, `sensitivity`,
`exposed`, plus a type-specific field (`url` / `package` / `ipaddress` /
`cloudType`). Optional: `tags`, `customFields`, and type-specific extras.
→ [Assets](Assets#create-an-asset)

#### `bulkUpdateAssetCustomFieldMutation`
Set custom-field values on assets matching a query. Args: `organizationId: UUID!`,
`searchQuery: String!` (non-empty), `fields: GenericScalar!` (slug → value).
Returns `asset: [AssetType]` (≤100 inline, else queued).
→ [Assets](Assets#updating-custom-fields-on-existing-assets)

#### `exportAssets`
Start an async CSV export of assets. Args: `organizationId`, `searchQuery`.
Returns `exportId`, `status`.
→ [Exporting Data](Exporting-Data)

#### `updateAssetFieldsWithCsv`
Bulk-update asset fields from an uploaded CSV (`file`, `organizationId`).

### Findings (bugs)

#### `bugCreate`
Create a finding. → [Findings](Findings#create-a-finding)

#### `bugBulkUpdate`
Update `state` / `severity` on findings matching `searchQuery`. Args:
`organizationId`, `searchQuery`, `state`, `severity`. Returns `bugs: [BugType]`.
→ [Findings](Findings#update-state-andor-severity)

#### `exportBugs`
Start an async CSV export of findings. Args: `organizationId`, `searchQuery`.
Returns `exportId`, `status`.

#### `updateBugsFieldsWithCsv`
Bulk-update finding custom fields from an uploaded CSV (`file`,
`organizationId`).

### Engagements

#### `createEngagement`
Create an engagement. Key args: `organizationId`, `name`, `scheduledDate`,
`deliveryDate`, `subscribedServices`, `plans`, `assessmentData`, `state`, plus
optional `prerequisitesData`, `documentIds`, `fields`, `vendorCode`,
`isSelfManaged`, `includeRelatedAssets`, `credentialIds`, `executiveSummary`,
`customStatus`. → [Engagements](Engagements#create-an-engagement)

#### `updateEngagement`
Update one engagement (public scope: `state` / `customStatus`). Args:
`organizationId`, `engagementId`, `state`. Returns `engagement: EngagementType`.

#### `bulkUpdateEngagements`
Update many engagements' state. Args: `organizationId`, `engagementIds`,
`state`. Returns `engagements: [EngagementType]`.

### Comments

#### `addBugComment`
Args: `organizationId`, `bugId`, `comment`, `internal`, `attachments`. Returns
`comment: CommentType`.

#### `addEngagementComment`
Args: `organizationId`, `engagementId`, `comment`, `attachments`. Returns
`comment: CommentType`.

### Reports & files

#### `addReportTemplate`
Args: `organizationId`, `templateName`, `htmlData`, `mode`, `type`. Returns
`templates: TemplateType`.

#### `generateReport`
Args: `organizationId`, `templateId`, `reportName`, `searchQuery`,
`assetSearchQuery`, `password`, `engagementId`, `viewId`, `customData`. Returns
`reports`, `passwordRequired`.

#### `addReportAttachment`
Args: `file: Upload!`, `organizationId`. Returns `attachment: AttachmentType`.

#### `addVaultAttachment`
Args: `file: Upload!`, `organizationId`, and optionally `engagementId`,
`prerequisite`. Returns `vault`. → [Vault Documents](Vault-Documents)

#### `uploadWorkspaceFile`
Args: `file: Upload!`, `workspaceId`, `path`. Returns `success`, `file`.

#### `importCsv`
Args: `file: Upload!`, `organizationId`, `sheetId`, `workBookId`,
`importOverride`, `mergeWith`, `name`. Returns `success`, `message`.

---

## Core object types

### `AssetType` (selected fields)
`id`, `name`, `target`, `type`, `cloudType`, `sensitivity`, `exposed`,
`riskScore`, `ipaddress`, `hostname`, `os`, `region`, `accountId`, `resourceId`,
`fields`, `created`, `updated`, `connector`, `otherConnectors`, `lastSeen`,
and the `dns*` / `domain*` / `whoisInfo` metadata. Full list in
[Assets](Assets#response-fields).

### `BugType` (selected fields)
`id`, `title`, `description`, `severity`, `state`, `bugLevel`, `cvss`,
`cvssV3`, `cvssV4`, `mitigation`, `stepsToReproduce`, `exploitAvailable`,
`patchAvailable`, `prioritizationScore`, `epssScore`, `slaViolated`, `dueDate`,
`fields`, `created`, `updated`, `connector`. Full list in
[Findings](Findings#response-fields).

### `EngagementType` (selected fields)
`id`, `engagementCustomId`, `name`, `state`, `stateId`, `parentState`,
`customStatus`, `scheduledDate`, `deliveryDate`, `subscribedServices`, `plans`,
`securityPosture`, `credits`, `assessmentsCount`, `engagementCompletion`,
`fields`, `isActive`, `created`, `updated`. Full list in
[Engagements](Engagements#response-fields).

### `CommentType`
`id`, `comment`, `internal`, `bugId`, `engagementId`, `commentedBy`,
`attachments`, `created`, `updated`. → [Comments](Comments#response-fields-commenttype)

### `ReportType`
`id`, `reportName`, `status` (`"0"`–`"3"`), `created`, `exportId`, `file`,
`hasPassword`, `template`. → [Reports](Reports#download_report--reporttype-fields)

### Scalars
`Boolean`, `Int`, `Float`, `String`, `ID`, `DateTime`, `Date`, `UUID`,
`JSONString`, `GenericScalar`, `Upload`.

---

## See also

- The generated schema: [`strobes_gql_client/schema.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/schema.py)
- Per-operation field selections: [`strobes_gql_client/client.py`](https://github.com/strobes-co/strobes-gql-client/blob/main/strobes_gql_client/client.py)
- The filter language: [Search Query Language](Search-Query-Language)
- Pythonic call reference: [Python API Reference](Python-API-Reference)
