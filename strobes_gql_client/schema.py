import sgqlc.types
import sgqlc.types.datetime


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AppAgentDocumentIndexingStatusChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FAILED', 'INDEXED', 'PENDING', 'PROCESSING')


class AppCredentialManagerTypeChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACCUKNOX_CM', 'ACUNETIX_CM', 'ANCHORE_CM', 'APPKNOX_CM', 'APP_SCAN_CM', 'APP_SENTINELS_CM', 'AWS_CM', 'AZURE_CM', 'AZURE_DEVOPS_CM', 'BITBUCKET_CM', 'BLACKDUCK_CM', 'BUGZILLA_CM', 'BURPSUITE_CM', 'BURP_ENTERPRISE_CM', 'CROWDSTRIKE_CM', 'DOCKER_CM', 'ECR_CM', 'FORTIFY_CM', 'GCP_CM', 'GITHUB_CM', 'GIT_CM', 'HACKERONE_CM', 'INSIGHT_PLATFORM_API_CM', 'INSIGHT_VM_CM', 'INTEL_GRAPH_CM', 'JFROG_XRAY_CM', 'JIRA_CM', 'MANDIANT_CM', 'MS_DEFENDER_CM', 'NESSUS_CM', 'NEXPOSE_CM', 'OPEN_AI_CM', 'ORCA_CM', 'PALO_ALTO_XDR_CM', 'PALO_ALTO_XPANSE_CM', 'PRISMA_CLOUD_CM', 'QUALYS_CM', 'SMTP_CM', 'SNYK_CM', 'SONAR_CLOUD_CM', 'SONAR_CM', 'SONATYPE_NEXUS_CM', 'SVN_CM', 'TANIUM_CM', 'TENABLEIO_CM', 'TENABLESC_CM', 'VERACODE_CM', 'WIZ_CM')


class AppPatchPatchTypeChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('A_1',)


class AppPortStateChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'FILTERED', 'NOTDEFINED', 'OPEN', 'OPEN_OR_FILTERED', 'UNFILTERED')


class AppPulseArtifactArtifactTypeChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CODE', 'CSV', 'HTML', 'JAVASCRIPT', 'JSON', 'MARKDOWN', 'PYTHON', 'SQL', 'TEXT', 'TYPESCRIPT', 'XML', 'YAML')


class AppPulseArtifactStatusChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATING', 'ERROR', 'READY')


class AppPulseMessageAuthorChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AGENT', 'ORCHESTRATOR', 'SYSTEM', 'TOOL', 'USER')


class AppPulseMessageStatusChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FINAL', 'STREAMING')


class AppPulseParticipantRoleChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AGENT', 'ORCHESTRATOR')


class AppPulseRunStatusChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CANCELED', 'COMPLETED', 'FAILED', 'QUEUED', 'RUNNING')


class AppPulseTaskStatusChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLOCKED', 'CANCELED', 'COMPLETED', 'FAILED', 'QUEUED', 'RUNNING')


class AppPulseThreadModeChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BACKGROUND', 'CHAT')


Boolean = sgqlc.types.Boolean

Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

class GQLRelationshipDirectionEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BIDIRECTIONAL', 'UNIDIRECTIONAL')


class GQLRelationshipTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONNECTS_TO', 'DEPENDS_ON', 'PART_OF_NETWORK', 'RUNS_ON')


class GenericScalar(sgqlc.types.Scalar):
    __schema__ = schema


class GroupingFieldType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AGE_RANGE_FIELD', 'BOOLEAN_FIELD', 'CUSTOM_BOOLEAN_FIELD', 'CUSTOM_MULTI_SELECT_FIELD', 'CUSTOM_NUMBER_FIELD', 'CUSTOM_SELECT_FIELD', 'CUSTOM_TEXT_FIELD', 'ENUM_FIELD', 'SCORE_RANGE_FIELD', 'TAG_FIELD')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSONString(sgqlc.types.Scalar):
    __schema__ = schema


String = sgqlc.types.String

class TenantCVESourceChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTEL_GRAPH', 'XO_INTEL')


class TenantCVETrendChoices(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('A_1', 'A_2', 'A_3', 'A_4', 'A_5')


Time = sgqlc.types.datetime.Time

class UUID(sgqlc.types.Scalar):
    __schema__ = schema


class Upload(sgqlc.types.Scalar):
    __schema__ = schema



########################################################################
# Input Objects
########################################################################
class GroupingCriterionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field_name', 'field_type', 'boolean_true_label', 'boolean_false_label', 'ranges', 'custom_field_values')
    field_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fieldName')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(GroupingFieldType), graphql_name='fieldType')
    boolean_true_label = sgqlc.types.Field(String, graphql_name='booleanTrueLabel')
    boolean_false_label = sgqlc.types.Field(String, graphql_name='booleanFalseLabel')
    ranges = sgqlc.types.Field(sgqlc.types.list_of('ScoreRangeInput'), graphql_name='ranges')
    custom_field_values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='customFieldValues')


class RangeInputType(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('preset', 'from_date', 'to_date')
    preset = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='preset')
    from_date = sgqlc.types.Field(DateTime, graphql_name='fromDate')
    to_date = sgqlc.types.Field(DateTime, graphql_name='toDate')


class ScoreRangeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('min', 'max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    max = sgqlc.types.Field(Float, graphql_name='max')



########################################################################
# Output Objects and Interfaces
########################################################################
class ASMSettingsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'merge_assets', 'merge_options', 'meta_data', 'tags', 'newly_added_assets', 'total_added_assets', 'last_synced', 'scheduled_interval', 'scope', 'verified_scope', 'out_of_scope', 'is_enabled', 'is_finding_scanning_enabled', 'scheduled_at', 'updated', 'created', 'last_scope_refreshed_on')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    merge_assets = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mergeAssets')
    merge_options = sgqlc.types.Field(JSONString, graphql_name='mergeOptions')
    meta_data = sgqlc.types.Field(JSONString, graphql_name='metaData')
    tags = sgqlc.types.Field(JSONString, graphql_name='tags')
    newly_added_assets = sgqlc.types.Field(Int, graphql_name='newlyAddedAssets')
    total_added_assets = sgqlc.types.Field(Int, graphql_name='totalAddedAssets')
    last_synced = sgqlc.types.Field(DateTime, graphql_name='lastSynced')
    scheduled_interval = sgqlc.types.Field(Int, graphql_name='scheduledInterval')
    scope = sgqlc.types.Field(GenericScalar, graphql_name='scope')
    verified_scope = sgqlc.types.Field(GenericScalar, graphql_name='verifiedScope')
    out_of_scope = sgqlc.types.Field(GenericScalar, graphql_name='outOfScope')
    is_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEnabled')
    is_finding_scanning_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFindingScanningEnabled')
    scheduled_at = sgqlc.types.Field(String, graphql_name='scheduledAt')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    last_scope_refreshed_on = sgqlc.types.Field(String, graphql_name='lastScopeRefreshedOn')


class ActivityType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'action', 'data', 'user', 'team', 'bug', 'asset', 'connector_config', 'engagement', 'connector', 'credential_manager', 'task', 'bot_task', 'approval', 'is_automation_activity', 'automation_workflow', 'automation_workflow_reason', 'created', 'updated', 'comment_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='action')
    data = sgqlc.types.Field(GenericScalar, graphql_name='data')
    user = sgqlc.types.Field('ApprovalUserType', graphql_name='user')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    bug = sgqlc.types.Field('TestsType', graphql_name='bug')
    asset = sgqlc.types.Field('AssetType', graphql_name='asset')
    connector_config = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='connectorConfig')
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    credential_manager = sgqlc.types.Field('CredentialManagerDetailType', graphql_name='credentialManager')
    task = sgqlc.types.Field('AllScanLogType', graphql_name='task')
    bot_task = sgqlc.types.Field('BotTaskType', graphql_name='botTask')
    approval = sgqlc.types.Field('ApprovalType', graphql_name='approval')
    is_automation_activity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAutomationActivity')
    automation_workflow = sgqlc.types.Field('AutomationWorkflowType', graphql_name='automationWorkflow')
    automation_workflow_reason = sgqlc.types.Field(JSONString, graphql_name='automationWorkflowReason')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')


class AddAssetFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset_field',)
    asset_field = sgqlc.types.Field('AssetFieldType', graphql_name='assetField')


class AddAttachmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('attachment',)
    attachment = sgqlc.types.Field('AttachmentType', graphql_name='attachment')


class AddBugFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug_field',)
    bug_field = sgqlc.types.Field('BugFieldType', graphql_name='bugField')


class AddBulkCommentsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of('BugType'), graphql_name='bugs')


class AddEngagementsFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagement_field',)
    engagement_field = sgqlc.types.Field('EngagementsFieldType', graphql_name='engagementField')


class AddGroupMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups',)
    groups = sgqlc.types.Field(sgqlc.types.list_of('GroupsType'), graphql_name='groups')


class AddPresetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('preset',)
    preset = sgqlc.types.Field('PresetType', graphql_name='preset')


class AddReportAttachmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('attachment',)
    attachment = sgqlc.types.Field('ReportAttachmentType', graphql_name='attachment')


class AddSelfManagedServiceMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('service',)
    service = sgqlc.types.Field('SelfManagedServiceType', graphql_name='service')


class AddTemplateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field('TemplateType', graphql_name='templates')


class AddVaultAttachmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('vault',)
    vault = sgqlc.types.Field('VaultType', graphql_name='vault')


class AgentDocumentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'agent', 'name', 'document', 'file_size', 'file_type', 'indexing_status', 'last_indexed_at', 'indexing_error', 'vector_store_references', 'attached_by', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    agent = sgqlc.types.Field('AutomationWorkflowType', graphql_name='agent')
    name = sgqlc.types.Field(String, graphql_name='name')
    document = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='document')
    file_size = sgqlc.types.Field(Int, graphql_name='fileSize')
    file_type = sgqlc.types.Field(String, graphql_name='fileType')
    indexing_status = sgqlc.types.Field(sgqlc.types.non_null(AppAgentDocumentIndexingStatusChoices), graphql_name='indexingStatus')
    last_indexed_at = sgqlc.types.Field(DateTime, graphql_name='lastIndexedAt')
    indexing_error = sgqlc.types.Field(String, graphql_name='indexingError')
    vector_store_references = sgqlc.types.Field(JSONString, graphql_name='vectorStoreReferences')
    attached_by = sgqlc.types.Field('ApprovalUserType', graphql_name='attachedBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class AllPossibleDuplicatesPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AllPossibleDuplicatesType'), graphql_name='objects')


class AllPossibleDuplicatesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'type', 'finding_ids', 'asset_ids', 'strategy', 'confidence', 'count', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    type = sgqlc.types.Field(Int, graphql_name='type')
    finding_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='findingIds')
    asset_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='assetIds')
    strategy = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='strategy')
    confidence = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='confidence')
    count = sgqlc.types.Field(Int, graphql_name='count')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class AllScanLogType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'task_id', 'config', 'finished', 'created_by', 'type', 'is_triangulum_scanner', 'task_retry_count', 'triangulum_task_finished', 'scanner_task_id', 'build_status', 'is_scheduled', 'external_scheduled_task', 'bugs', 'extra_data', 'scan_arguments', 'assets', 'temp_file', 'logs', 'error_code', 'bug_stats', 'merge_data', 'scan_filter_data', 'status', 'artifacts_file_paths', 'child_tasks', 'is_child_task', 'started', 'status_last_updated', 'error_info', 'events', 'single_scan_metadata', 'asset_set', 'last_seen', 'exportreport_set', 'bottask_set', 'bug_set', 'rediscovered_finding', 'activity_task', 'asset', 'organization_id', 'connector_name', 'connector_slug')
    id = sgqlc.types.Field(Int, graphql_name='id')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')
    config = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='config')
    finished = sgqlc.types.Field(DateTime, graphql_name='finished')
    created_by = sgqlc.types.Field('ApprovalUserType', graphql_name='createdBy')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    is_triangulum_scanner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTriangulumScanner')
    task_retry_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskRetryCount')
    triangulum_task_finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='triangulumTaskFinished')
    scanner_task_id = sgqlc.types.Field(String, graphql_name='scannerTaskId')
    build_status = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='buildStatus')
    is_scheduled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isScheduled')
    external_scheduled_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='externalScheduledTask')
    bugs = sgqlc.types.Field(JSONString, graphql_name='bugs')
    extra_data = sgqlc.types.Field(JSONString, graphql_name='extraData')
    scan_arguments = sgqlc.types.Field(GenericScalar, graphql_name='scanArguments')
    assets = sgqlc.types.Field(JSONString, graphql_name='assets')
    temp_file = sgqlc.types.Field(String, graphql_name='tempFile')
    logs = sgqlc.types.Field(JSONString, graphql_name='logs')
    error_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='errorCode')
    bug_stats = sgqlc.types.Field(JSONString, graphql_name='bugStats')
    merge_data = sgqlc.types.Field(JSONString, graphql_name='mergeData')
    scan_filter_data = sgqlc.types.Field(JSONString, graphql_name='scanFilterData')
    status = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='status')
    artifacts_file_paths = sgqlc.types.Field(JSONString, graphql_name='artifactsFilePaths')
    child_tasks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AllScanLogType'))), graphql_name='childTasks')
    is_child_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isChildTask')
    started = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='started')
    status_last_updated = sgqlc.types.Field(DateTime, graphql_name='statusLastUpdated')
    error_info = sgqlc.types.Field(String, graphql_name='errorInfo')
    events = sgqlc.types.Field(GenericScalar, graphql_name='events')
    single_scan_metadata = sgqlc.types.Field(JSONString, graphql_name='singleScanMetadata')
    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='assetSet')
    last_seen = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='lastSeen')
    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='exportreportSet')
    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BotTaskType'))), graphql_name='bottaskSet')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    rediscovered_finding = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='rediscoveredFinding')
    activity_task = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activityTask')
    asset = sgqlc.types.Field(Int, graphql_name='asset')
    organization_id = sgqlc.types.Field(String, graphql_name='organizationId')
    connector_name = sgqlc.types.Field(String, graphql_name='connectorName')
    connector_slug = sgqlc.types.Field(String, graphql_name='connectorSlug')


class ApiCursorPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('objects', 'has_next', 'has_previous', 'last_cursor', 'before_cursor')
    objects = sgqlc.types.Field(sgqlc.types.list_of('ApiType'), graphql_name='objects')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_previous = sgqlc.types.Field(Boolean, graphql_name='hasPrevious')
    last_cursor = sgqlc.types.Field(String, graphql_name='lastCursor')
    before_cursor = sgqlc.types.Field(String, graphql_name='beforeCursor')


class ApiType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'method', 'path', 'summary', 'description', 'tags', 'parameters', 'request_body', 'responses', 'asset', 'organization', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='method')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    description = sgqlc.types.Field(String, graphql_name='description')
    tags = sgqlc.types.Field(GenericScalar, graphql_name='tags')
    parameters = sgqlc.types.Field(GenericScalar, graphql_name='parameters')
    request_body = sgqlc.types.Field(GenericScalar, graphql_name='requestBody')
    responses = sgqlc.types.Field(GenericScalar, graphql_name='responses')
    asset = sgqlc.types.Field('AssetType', graphql_name='asset')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class ApprovalPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('ApprovalType'), graphql_name='objects')


class ApprovalType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'finding', 'approved_by', 'approval_state', 'raised_by', 'from_state', 'to_state', 'is_expired', 'created', 'updated', 'activity_approval', 'comments_approval')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    finding = sgqlc.types.Field('TestsType', graphql_name='finding')
    approved_by = sgqlc.types.Field('OrganizationMembersType', graphql_name='approvedBy')
    approval_state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='approvalState')
    raised_by = sgqlc.types.Field('OrganizationMembersType', graphql_name='raisedBy')
    from_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fromState')
    to_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='toState')
    is_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExpired')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    activity_approval = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activityApproval')
    comments_approval = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentsApproval')


class ApprovalUserType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('password', 'is_superuser', 'id', 'email', 'first_name', 'last_name', 'created', 'updated', 'is_superadmin', 'is_staff', 'is_ai_agent', 'is_active', 'activation_id', 'bio', 'profile_picture', 'cover_heading', 'linkedin_url', 'twitter_url', 'designation', 'phone_number', 'last_login', 'username', 'org_members', 'organizationmember_set', 'asset_set', 'group_set', 'created_priority_rule_sets', 'engagements_set', 'engagement_assignees', 'assessment_asset_assigned_to', 'vault_set', 'prerequisites_assigned_to', 'prerequisites_user', 'workbook_set', 'sheet_set', 'sheetrow_set', 'prefills_set', 'configurations_set', 'scanlog_set', 'exportreport_set', 'reportattachment_set', 'credentialmanager_set', 'bottask_set', 'automationworkflows_set', 'agentdocument_set', 'assigned_to', 'reported_by', 'attachment_set', 'activity_set', 'comment_set', 'filterviews_set', 'views_members', 'reporttemplates_set', 'draft_set', 'pulse_threads', 'dashboards_set', 'widget_set', 'created_asset_relationships', 'profile_picture_url')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    is_superuser = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperuser')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    is_superadmin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperadmin')
    is_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStaff')
    is_ai_agent = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAiAgent')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    activation_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='activationId')
    bio = sgqlc.types.Field(String, graphql_name='bio')
    profile_picture = sgqlc.types.Field(String, graphql_name='profilePicture')
    cover_heading = sgqlc.types.Field(String, graphql_name='coverHeading')
    linkedin_url = sgqlc.types.Field(String, graphql_name='linkedinUrl')
    twitter_url = sgqlc.types.Field(String, graphql_name='twitterUrl')
    designation = sgqlc.types.Field(String, graphql_name='designation')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    last_login = sgqlc.types.Field(DateTime, graphql_name='lastLogin')
    username = sgqlc.types.Field(String, graphql_name='username')
    org_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TenantOrganizationType'))), graphql_name='orgMembers')
    organizationmember_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationMembersType'))), graphql_name='organizationmemberSet')
    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='assetSet')
    group_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GroupsType'))), graphql_name='groupSet')
    created_priority_rule_sets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriorityRuleSetType'))), graphql_name='createdPriorityRuleSets')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementType'))), graphql_name='engagementsSet')
    engagement_assignees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementType'))), graphql_name='engagementAssignees')
    assessment_asset_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssessmentType'))), graphql_name='assessmentAssetAssignedTo')
    vault_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='vaultSet')
    prerequisites_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PreRequisitesType'))), graphql_name='prerequisitesAssignedTo')
    prerequisites_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PreRequisitesType'))), graphql_name='prerequisitesUser')
    workbook_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkBookType'))), graphql_name='workbookSet')
    sheet_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SheetType'))), graphql_name='sheetSet')
    sheetrow_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SheetRowType'))), graphql_name='sheetrowSet')
    prefills_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PrefillsType'))), graphql_name='prefillsSet')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationsSet')
    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='scanlogSet')
    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='exportreportSet')
    reportattachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportAttachmentType'))), graphql_name='reportattachmentSet')
    credentialmanager_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CredentialManagerDetailType'))), graphql_name='credentialmanagerSet')
    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BotTaskType'))), graphql_name='bottaskSet')
    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AutomationWorkflowType'))), graphql_name='automationworkflowsSet')
    agentdocument_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AgentDocumentType))), graphql_name='agentdocumentSet')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='assignedTo')
    reported_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='reportedBy')
    attachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentType'))), graphql_name='attachmentSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')
    filterviews_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FilterViewsType'))), graphql_name='filterviewsSet')
    views_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FilterViewsType'))), graphql_name='viewsMembers')
    reporttemplates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TemplateType'))), graphql_name='reporttemplatesSet')
    draft_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DraftType'))), graphql_name='draftSet')
    pulse_threads = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PulseThreadType'))), graphql_name='pulseThreads')
    dashboards_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DashboardType'))), graphql_name='dashboardsSet')
    widget_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetSet')
    created_asset_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetRelationshipType'))), graphql_name='createdAssetRelationships')
    profile_picture_url = sgqlc.types.Field(String, graphql_name='profilePictureUrl')


class ApproveStateChangeMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('approvals',)
    approvals = sgqlc.types.Field(sgqlc.types.list_of(ApprovalType), graphql_name='approvals')


class AssessmentPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AssessmentType'), graphql_name='objects')


class AssessmentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'service', 'package', 'engagement', 'asset', 'state', 'scope', 'instructions', 'test_accounts', 'vpn_accounts', 'assigned_to', 'scheduled_date', 'delivery_date', 'total_hours_spent', 'assessment_category', 'created', 'updated', 'custom_assessment_status', 'current_status', 'current_status_id', 'is_using_custom_status', 'parent_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    service = sgqlc.types.Field(String, graphql_name='service')
    package = sgqlc.types.Field(String, graphql_name='package')
    engagement = sgqlc.types.Field(sgqlc.types.non_null('EngagementType'), graphql_name='engagement')
    asset = sgqlc.types.Field('AssetType', graphql_name='asset')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')
    scope = sgqlc.types.Field(String, graphql_name='scope')
    instructions = sgqlc.types.Field(String, graphql_name='instructions')
    test_accounts = sgqlc.types.Field(String, graphql_name='testAccounts')
    vpn_accounts = sgqlc.types.Field(String, graphql_name='vpnAccounts')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalUserType))), graphql_name='assignedTo')
    scheduled_date = sgqlc.types.Field(Date, graphql_name='scheduledDate')
    delivery_date = sgqlc.types.Field(Date, graphql_name='deliveryDate')
    total_hours_spent = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalHoursSpent')
    assessment_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assessmentCategory')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    custom_assessment_status = sgqlc.types.Field('CustomAssessmentStatusType', graphql_name='customAssessmentStatus')
    current_status = sgqlc.types.Field(String, graphql_name='currentStatus')
    current_status_id = sgqlc.types.Field(String, graphql_name='currentStatusId')
    is_using_custom_status = sgqlc.types.Field(Boolean, graphql_name='isUsingCustomStatus')
    parent_state = sgqlc.types.Field(Int, graphql_name='parentState')


class AssetCursorPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('objects', 'has_next', 'has_previous', 'last_cursor', 'before_cursor')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AssetType'), graphql_name='objects')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_previous = sgqlc.types.Field(Boolean, graphql_name='hasPrevious')
    last_cursor = sgqlc.types.Field(String, graphql_name='lastCursor')
    before_cursor = sgqlc.types.Field(String, graphql_name='beforeCursor')


class AssetFieldPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AssetFieldType'), graphql_name='objects')


class AssetFieldType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'slug', 'description', 'field_type', 'options', 'is_required', 'is_active', 'extra_data', 'created', 'updated', 'organization', 'engagementsfield', 'assetfield', 'bugfield')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldType')
    options = sgqlc.types.Field(GenericScalar, graphql_name='options')
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    extra_data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='extraData')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    engagementsfield = sgqlc.types.Field('EngagementsFieldType', graphql_name='engagementsfield')
    assetfield = sgqlc.types.Field('AssetFieldType', graphql_name='assetfield')
    bugfield = sgqlc.types.Field('BugFieldType', graphql_name='bugfield')


class AssetRelationshipPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AssetRelationshipType'), graphql_name='objects')


class AssetRelationshipType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'source_asset', 'target_asset', 'relationship_type', 'direction', 'metadata', 'created_by', 'organization', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    source_asset = sgqlc.types.Field('AssetType', graphql_name='sourceAsset')
    target_asset = sgqlc.types.Field('AssetType', graphql_name='targetAsset')
    relationship_type = sgqlc.types.Field(GQLRelationshipTypeEnum, graphql_name='relationshipType')
    direction = sgqlc.types.Field(GQLRelationshipDirectionEnum, graphql_name='direction')
    metadata = sgqlc.types.Field(GenericScalar, graphql_name='metadata')
    created_by = sgqlc.types.Field('UserType', graphql_name='createdBy')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class AssetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'target', 'exposed', 'type', 'cloud_type', 'organization', 'disabled', 'sensitivity', 'keys', 'data', 'created_by', 'linked_assets', 'additional_info', 'scan', 'last_seen', 'temp_id', 'is_active', 'created', 'updated', 'tags', 'location', 'scanner_raw_response', 'region', 'resource_id', 'account_id', 'fields', 'asset_region', 'dns_info', 'whois_info', 'asn', 'waf', 'cdn', 'asm_last_alive', 'connector', 'other_connectors', 'linked_to', 'group_assets', 'asset_port', 'assessments_set', 'asset_package', 'asset_apis', 'configuration_asset', 'bug_set', 'activity_set', 'trackers_set', 'patch_set', 'source_relationships', 'target_relationships', 'ipaddress', 'hostname', 'mac_address', 'os', 'cpe', 'risk_score', 'apis', 'dns_a', 'dns_ns', 'dns_soa', 'dns_aaaa', 'dns_axfr', 'dns_cname', 'domain_org', 'domain_city', 'domain_state', 'domain_dnssec', 'domain_emails', 'domain_status', 'domain_address', 'domain_country', 'domain_registrar', 'domain_name', 'domain_name_servers', 'domain_referral_url', 'domain_updated_date', 'domain_server', 'domain_expiration_date', 'domain_creation_date', 'domain_registrant_postal_code', 'port_addresses', 'package_count', 'webserver', 'technology_used', 'outgoing_relationships', 'incoming_relationships', 'all_relationships')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(String, graphql_name='target')
    exposed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='exposed')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    cloud_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cloudType')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disabled')
    sensitivity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sensitivity')
    keys = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='keys')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    linked_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='linkedAssets')
    additional_info = sgqlc.types.Field(JSONString, graphql_name='additionalInfo')
    scan = sgqlc.types.Field(AllScanLogType, graphql_name='scan')
    last_seen = sgqlc.types.Field(AllScanLogType, graphql_name='lastSeen')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='tags')
    location = sgqlc.types.Field(String, graphql_name='location')
    scanner_raw_response = sgqlc.types.Field(JSONString, graphql_name='scannerRawResponse')
    region = sgqlc.types.Field(String, graphql_name='region')
    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')
    account_id = sgqlc.types.Field(String, graphql_name='accountId')
    fields = sgqlc.types.Field(GenericScalar, graphql_name='fields')
    asset_region = sgqlc.types.Field(String, graphql_name='assetRegion')
    dns_info = sgqlc.types.Field(GenericScalar, graphql_name='dnsInfo')
    whois_info = sgqlc.types.Field(GenericScalar, graphql_name='whoisInfo')
    asn = sgqlc.types.Field(String, graphql_name='asn')
    waf = sgqlc.types.Field(String, graphql_name='waf')
    cdn = sgqlc.types.Field(String, graphql_name='cdn')
    asm_last_alive = sgqlc.types.Field(DateTime, graphql_name='asmLastAlive')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    other_connectors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConnectorType'))), graphql_name='otherConnectors')
    linked_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='linkedTo')
    group_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GroupsType'))), graphql_name='groupAssets')
    asset_port = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PortType'))), graphql_name='assetPort')
    assessments_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='assessmentsSet')
    asset_package = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PackageAssetType'))), graphql_name='assetPackage')
    asset_apis = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApiType))), graphql_name='assetApis')
    configuration_asset = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationAsset')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')
    patch_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PatchesType'))), graphql_name='patchSet')
    source_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetRelationshipType))), graphql_name='sourceRelationships')
    target_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetRelationshipType))), graphql_name='targetRelationships')
    ipaddress = sgqlc.types.Field(String, graphql_name='ipaddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    mac_address = sgqlc.types.Field(String, graphql_name='macAddress')
    os = sgqlc.types.Field(String, graphql_name='os')
    cpe = sgqlc.types.Field(String, graphql_name='cpe')
    risk_score = sgqlc.types.Field(Float, graphql_name='riskScore')
    apis = sgqlc.types.Field(sgqlc.types.list_of(ApiType), graphql_name='apis')
    dns_a = sgqlc.types.Field(GenericScalar, graphql_name='dnsA')
    dns_ns = sgqlc.types.Field(GenericScalar, graphql_name='dnsNs')
    dns_soa = sgqlc.types.Field(GenericScalar, graphql_name='dnsSoa')
    dns_aaaa = sgqlc.types.Field(GenericScalar, graphql_name='dnsAaaa')
    dns_axfr = sgqlc.types.Field(GenericScalar, graphql_name='dnsAxfr')
    dns_cname = sgqlc.types.Field(GenericScalar, graphql_name='dnsCname')
    domain_org = sgqlc.types.Field(String, graphql_name='domainOrg')
    domain_city = sgqlc.types.Field(String, graphql_name='domainCity')
    domain_state = sgqlc.types.Field(String, graphql_name='domainState')
    domain_dnssec = sgqlc.types.Field(String, graphql_name='domainDnssec')
    domain_emails = sgqlc.types.Field(String, graphql_name='domainEmails')
    domain_status = sgqlc.types.Field(String, graphql_name='domainStatus')
    domain_address = sgqlc.types.Field(String, graphql_name='domainAddress')
    domain_country = sgqlc.types.Field(String, graphql_name='domainCountry')
    domain_registrar = sgqlc.types.Field(String, graphql_name='domainRegistrar')
    domain_name = sgqlc.types.Field(String, graphql_name='domainName')
    domain_name_servers = sgqlc.types.Field(GenericScalar, graphql_name='domainNameServers')
    domain_referral_url = sgqlc.types.Field(String, graphql_name='domainReferralUrl')
    domain_updated_date = sgqlc.types.Field(String, graphql_name='domainUpdatedDate')
    domain_server = sgqlc.types.Field(String, graphql_name='domainServer')
    domain_expiration_date = sgqlc.types.Field(String, graphql_name='domainExpirationDate')
    domain_creation_date = sgqlc.types.Field(String, graphql_name='domainCreationDate')
    domain_registrant_postal_code = sgqlc.types.Field(String, graphql_name='domainRegistrantPostalCode')
    port_addresses = sgqlc.types.Field(String, graphql_name='portAddresses')
    package_count = sgqlc.types.Field(Int, graphql_name='packageCount')
    webserver = sgqlc.types.Field(GenericScalar, graphql_name='webserver')
    technology_used = sgqlc.types.Field(GenericScalar, graphql_name='technologyUsed')
    outgoing_relationships = sgqlc.types.Field(sgqlc.types.list_of(AssetRelationshipType), graphql_name='outgoingRelationships')
    incoming_relationships = sgqlc.types.Field(sgqlc.types.list_of(AssetRelationshipType), graphql_name='incomingRelationships')
    all_relationships = sgqlc.types.Field(sgqlc.types.list_of(AssetRelationshipType), graphql_name='allRelationships')


class AssetWidgetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AssetWidgetType'), graphql_name='objects')


class AssetWidgetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'target', 'exposed', 'type', 'cloud_type', 'organization', 'disabled', 'sensitivity', 'keys', 'data', 'created_by', 'linked_assets', 'additional_info', 'scan', 'last_seen', 'temp_id', 'is_active', 'created', 'updated', 'tags', 'location', 'scanner_raw_response', 'region', 'resource_id', 'account_id', 'fields', 'asset_region', 'dns_info', 'whois_info', 'asn', 'waf', 'cdn', 'asm_last_alive', 'connector', 'other_connectors', 'linked_to', 'group_assets', 'asset_port', 'assessments_set', 'asset_package', 'asset_apis', 'configuration_asset', 'bug_set', 'activity_set', 'trackers_set', 'patch_set', 'source_relationships', 'target_relationships', 'ipaddress', 'hostname', 'mac_address', 'total', 'open', 'closed', 'new', 'active', 'resolved', 'not_applicable', 'risk_score', 'info_open', 'info_closed', 'low_open', 'low_closed', 'medium_open', 'medium_closed', 'high_open', 'high_closed', 'critical_open', 'critical_closed')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(String, graphql_name='target')
    exposed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='exposed')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    cloud_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cloudType')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disabled')
    sensitivity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sensitivity')
    keys = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='keys')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    linked_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='linkedAssets')
    additional_info = sgqlc.types.Field(JSONString, graphql_name='additionalInfo')
    scan = sgqlc.types.Field(AllScanLogType, graphql_name='scan')
    last_seen = sgqlc.types.Field(AllScanLogType, graphql_name='lastSeen')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='tags')
    location = sgqlc.types.Field(String, graphql_name='location')
    scanner_raw_response = sgqlc.types.Field(JSONString, graphql_name='scannerRawResponse')
    region = sgqlc.types.Field(String, graphql_name='region')
    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')
    account_id = sgqlc.types.Field(String, graphql_name='accountId')
    fields = sgqlc.types.Field(JSONString, graphql_name='fields')
    asset_region = sgqlc.types.Field(String, graphql_name='assetRegion')
    dns_info = sgqlc.types.Field(JSONString, graphql_name='dnsInfo')
    whois_info = sgqlc.types.Field(JSONString, graphql_name='whoisInfo')
    asn = sgqlc.types.Field(String, graphql_name='asn')
    waf = sgqlc.types.Field(String, graphql_name='waf')
    cdn = sgqlc.types.Field(String, graphql_name='cdn')
    asm_last_alive = sgqlc.types.Field(DateTime, graphql_name='asmLastAlive')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    other_connectors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConnectorType'))), graphql_name='otherConnectors')
    linked_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='linkedTo')
    group_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GroupsType'))), graphql_name='groupAssets')
    asset_port = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PortType'))), graphql_name='assetPort')
    assessments_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='assessmentsSet')
    asset_package = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PackageAssetType'))), graphql_name='assetPackage')
    asset_apis = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApiType))), graphql_name='assetApis')
    configuration_asset = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationAsset')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')
    patch_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PatchesType'))), graphql_name='patchSet')
    source_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetRelationshipType))), graphql_name='sourceRelationships')
    target_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetRelationshipType))), graphql_name='targetRelationships')
    ipaddress = sgqlc.types.Field(String, graphql_name='ipaddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    mac_address = sgqlc.types.Field(String, graphql_name='macAddress')
    total = sgqlc.types.Field(Int, graphql_name='total')
    open = sgqlc.types.Field(Int, graphql_name='open')
    closed = sgqlc.types.Field(Int, graphql_name='closed')
    new = sgqlc.types.Field(Int, graphql_name='new')
    active = sgqlc.types.Field(Int, graphql_name='active')
    resolved = sgqlc.types.Field(Int, graphql_name='resolved')
    not_applicable = sgqlc.types.Field(Int, graphql_name='notApplicable')
    risk_score = sgqlc.types.Field(Float, graphql_name='riskScore')
    info_open = sgqlc.types.Field(Int, graphql_name='infoOpen')
    info_closed = sgqlc.types.Field(Int, graphql_name='infoClosed')
    low_open = sgqlc.types.Field(Int, graphql_name='lowOpen')
    low_closed = sgqlc.types.Field(Int, graphql_name='lowClosed')
    medium_open = sgqlc.types.Field(Int, graphql_name='mediumOpen')
    medium_closed = sgqlc.types.Field(Int, graphql_name='mediumClosed')
    high_open = sgqlc.types.Field(Int, graphql_name='highOpen')
    high_closed = sgqlc.types.Field(Int, graphql_name='highClosed')
    critical_open = sgqlc.types.Field(Int, graphql_name='criticalOpen')
    critical_closed = sgqlc.types.Field(Int, graphql_name='criticalClosed')


class AssetsDistributionType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups', 'risk_buckets', 'sensitivity_buckets', 'regions')
    groups = sgqlc.types.Field(sgqlc.types.list_of('DistributionGroupType'), graphql_name='groups')
    risk_buckets = sgqlc.types.Field(sgqlc.types.list_of('RiskBucketType'), graphql_name='riskBuckets')
    sensitivity_buckets = sgqlc.types.Field(sgqlc.types.list_of('RiskBucketType'), graphql_name='sensitivityBuckets')
    regions = sgqlc.types.Field(sgqlc.types.list_of('RegionType'), graphql_name='regions')


class AssignAssetViewToUsersMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('views',)
    views = sgqlc.types.Field('FilterViewsType', graphql_name='views')


class AtRiskSLAType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug_id', 'title', 'severity', 'asset_name', 'time_remaining', 'status')
    bug_id = sgqlc.types.Field(String, graphql_name='bugId')
    title = sgqlc.types.Field(String, graphql_name='title')
    severity = sgqlc.types.Field(Int, graphql_name='severity')
    asset_name = sgqlc.types.Field(String, graphql_name='assetName')
    time_remaining = sgqlc.types.Field(String, graphql_name='timeRemaining')
    status = sgqlc.types.Field(String, graphql_name='status')


class AttachmentPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AttachmentType'), graphql_name='objects')


class AttachmentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'attachment', 'attachment_name', 'attachment_size', 'bug', 'attached_by', 'created', 'updated', 'bug_attachments', 'comment_set', 'url', 'attachment_extenstion')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    attachment = sgqlc.types.Field(String, graphql_name='attachment')
    attachment_name = sgqlc.types.Field(String, graphql_name='attachmentName')
    attachment_size = sgqlc.types.Field(Int, graphql_name='attachmentSize')
    bug = sgqlc.types.Field('TestsType', graphql_name='bug')
    attached_by = sgqlc.types.Field(ApprovalUserType, graphql_name='attachedBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    bug_attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugAttachments')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')
    url = sgqlc.types.Field(String, graphql_name='url')
    attachment_extenstion = sgqlc.types.Field(String, graphql_name='attachmentExtenstion')


class AutomationWorkflowActivityPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(ActivityType), graphql_name='objects')


class AutomationWorkflowPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AutomationWorkflowType'), graphql_name='objects')


class AutomationWorkflowType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'system_agent_id', 'role', 'tool', 'workflow_mode', 'schedule_frequency', 'schedule_day_of_week', 'schedule_time', 'timezone', 'module', 'search_query', 'group_by', 'instructions', 'weightage', 'ignore_weightage', 'organization', 'credential_manager', 'llm_model', 'initial_chat_suggestions', 'created_by', 'hooks', 'triggers', 'agent_avatar', 'pipeline_code', 'is_active', 'tracking_rules', 'tracker_configuration', 'last_scheduled_task_on', 'tools', 'dashboard_pdf', 'dashboard_pdf_generated_at', 'report_attachment', 'report_attachment_generated_at', 'created', 'updated', 'documents', 'activity_set', 'comment_set', 'avatar')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    system_agent_id = sgqlc.types.Field(String, graphql_name='systemAgentId')
    role = sgqlc.types.Field(String, graphql_name='role')
    tool = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tool')
    workflow_mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='workflowMode')
    schedule_frequency = sgqlc.types.Field(Int, graphql_name='scheduleFrequency')
    schedule_day_of_week = sgqlc.types.Field(Int, graphql_name='scheduleDayOfWeek')
    schedule_time = sgqlc.types.Field(Time, graphql_name='scheduleTime')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    module = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='module')
    search_query = sgqlc.types.Field(String, graphql_name='searchQuery')
    group_by = sgqlc.types.Field(String, graphql_name='groupBy')
    instructions = sgqlc.types.Field(String, graphql_name='instructions')
    weightage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightage')
    ignore_weightage = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='ignoreWeightage')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    credential_manager = sgqlc.types.Field('CredentialManagerDetailType', graphql_name='credentialManager')
    llm_model = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='llmModel')
    initial_chat_suggestions = sgqlc.types.Field(JSONString, graphql_name='initialChatSuggestions')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    hooks = sgqlc.types.Field(GenericScalar, graphql_name='hooks')
    triggers = sgqlc.types.Field(GenericScalar, graphql_name='triggers')
    agent_avatar = sgqlc.types.Field(String, graphql_name='agentAvatar')
    pipeline_code = sgqlc.types.Field(String, graphql_name='pipelineCode')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    tracking_rules = sgqlc.types.Field('TrackingRulesType', graphql_name='trackingRules')
    tracker_configuration = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='trackerConfiguration')
    last_scheduled_task_on = sgqlc.types.Field(DateTime, graphql_name='lastScheduledTaskOn')
    tools = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='tools')
    dashboard_pdf = sgqlc.types.Field(String, graphql_name='dashboardPdf')
    dashboard_pdf_generated_at = sgqlc.types.Field(DateTime, graphql_name='dashboardPdfGeneratedAt')
    report_attachment = sgqlc.types.Field('ReportType', graphql_name='reportAttachment')
    report_attachment_generated_at = sgqlc.types.Field(DateTime, graphql_name='reportAttachmentGeneratedAt')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    documents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AgentDocumentType))), graphql_name='documents')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')


class AzureDevopsRepositoriesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('repo_url',)
    repo_url = sgqlc.types.Field(String, graphql_name='repoUrl')


class AzureDevopsRepositoriesTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(AzureDevopsRepositoriesType), graphql_name='objects')


class BitbucketRepositoriesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('repo_url',)
    repo_url = sgqlc.types.Field(String, graphql_name='repoUrl')


class BitbucketRepositoriesTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(BitbucketRepositoriesType), graphql_name='objects')


class BlackDuckProjectsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'url')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')


class BlackDuckProjectsTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(BlackDuckProjectsType), graphql_name='objects')


class BotTaskPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('BotTaskType'), graphql_name='objects')


class BotTaskType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'task_id', 'config', 'extra_data', 'status', 'started', 'finished', 'initiated_by', 'is_reverted', 'total_findings_closed', 'config_name', 'connector')
    id = sgqlc.types.Field(Int, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')
    config = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='config')
    extra_data = sgqlc.types.Field(GenericScalar, graphql_name='extraData')
    status = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='status')
    started = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='started')
    finished = sgqlc.types.Field(DateTime, graphql_name='finished')
    initiated_by = sgqlc.types.Field(ApprovalUserType, graphql_name='initiatedBy')
    is_reverted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isReverted')
    total_findings_closed = sgqlc.types.Field(Int, graphql_name='totalFindingsClosed')
    config_name = sgqlc.types.Field(String, graphql_name='configName')
    connector = sgqlc.types.Field(String, graphql_name='connector')


class BugCursorPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('objects', 'has_next', 'has_previous', 'last_cursor', 'before_cursor')
    objects = sgqlc.types.Field(sgqlc.types.list_of('BugType'), graphql_name='objects')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_previous = sgqlc.types.Field(Boolean, graphql_name='hasPrevious')
    last_cursor = sgqlc.types.Field(String, graphql_name='lastCursor')
    before_cursor = sgqlc.types.Field(String, graphql_name='beforeCursor')


class BugFieldPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('BugFieldType'), graphql_name='objects')


class BugFieldType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'slug', 'description', 'field_type', 'options', 'is_required', 'is_active', 'extra_data', 'created', 'updated', 'engagementsfield', 'assetfield', 'bugfield', 'organization')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldType')
    options = sgqlc.types.Field(GenericScalar, graphql_name='options')
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    extra_data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='extraData')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    engagementsfield = sgqlc.types.Field('EngagementsFieldType', graphql_name='engagementsfield')
    assetfield = sgqlc.types.Field(AssetFieldType, graphql_name='assetfield')
    bugfield = sgqlc.types.Field('BugFieldType', graphql_name='bugfield')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')


class BugType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('state', 'severity', 'bug_level', 'alert_category', 'id', 'title', 'description', 'mitigation', 'steps_to_reproduce', 'evidence', 'object_id', 'hash', 'duplicate', 'cwe', 'cve', 'cvss', 'attack_vector', 'bug_tags', 'bug_references', 'assigned_to', 'organization', 'asset', 'team', 'reported_by', 'due_date', 'sla_violated', 'has_user_defined_due_date', 'exploit_available', 'exploit_info', 'patch_available', 'patch_info', 'prioritization_score', 'prioritization_score_calculated', 'drill_down_score', 'nuclie_template', 'nuclie_rule_set', 'nuclie_target', 'bug_attachments', 'connector', 'configuration_name', 'connector_config', 'scan', 'other_scans', 'scanner_raw_response', 'scan_raw_response', 'batch_id', 'temp_id', 'recently_rediscovered_batch_id', 'vulnerable_since', 'engagements', 'priority_last_updated', 'zero_day_available', 'is_wormable', 'trend', 'advisories_seen', 'epss_score', 'cisa_due_date', 'nist', 'owasp', 'records_at_risk', 'records_type', 'fields', 'links', 'metadata', 'asm_last_updated', 'is_misconfiguration', 'sla_rule_search_query', 'created', 'updated', 'is_active', 'is_alert', 'patch', 'smart_close', 'is_reopened', 'last_smart_closed_on', 'last_reopened_on', 'is_automated_patched', 'patch_data', 'maintf', 'tf_prev_state', 'last_data_enriched', 'is_data_enriched', 'ai_title', 'ai_description', 'ai_mitigation', 'priority_rule_data', 'original_bug', 'attachment_set', 'activity_set', 'comment_set', 'bug_tracker', 'approval_finding', 'ipaddress', 'hostname', 'mac_address', 'os', 'tracker', 'last_resolved_on', 'cost_of_risk', 'port', 'duplicate_instances', 'content_object', 'references', 'config_content_object', 'maintf_content')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')
    severity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='severity')
    bug_level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bugLevel')
    alert_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='alertCategory')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    mitigation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mitigation')
    steps_to_reproduce = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stepsToReproduce')
    evidence = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='evidence')
    object_id = sgqlc.types.Field(Int, graphql_name='objectId')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    duplicate = sgqlc.types.Field('TestsType', graphql_name='duplicate')
    cwe = sgqlc.types.Field(sgqlc.types.list_of('CWEType'), graphql_name='cwe')
    cve = sgqlc.types.Field(sgqlc.types.list_of('CVEType'), graphql_name='cve')
    cvss = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cvss')
    attack_vector = sgqlc.types.Field(String, graphql_name='attackVector')
    bug_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='bugTags')
    bug_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReferenceType'))), graphql_name='bugReferences')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalUserType))), graphql_name='assignedTo')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    reported_by = sgqlc.types.Field(ApprovalUserType, graphql_name='reportedBy')
    due_date = sgqlc.types.Field(DateTime, graphql_name='dueDate')
    sla_violated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slaViolated')
    has_user_defined_due_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasUserDefinedDueDate')
    exploit_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exploitAvailable')
    exploit_info = sgqlc.types.Field(GenericScalar, graphql_name='exploitInfo')
    patch_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='patchAvailable')
    patch_info = sgqlc.types.Field(GenericScalar, graphql_name='patchInfo')
    prioritization_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritizationScore')
    prioritization_score_calculated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='prioritizationScoreCalculated')
    drill_down_score = sgqlc.types.Field(GenericScalar, graphql_name='drillDownScore')
    nuclie_template = sgqlc.types.Field(String, graphql_name='nuclieTemplate')
    nuclie_rule_set = sgqlc.types.Field(JSONString, graphql_name='nuclieRuleSet')
    nuclie_target = sgqlc.types.Field(String, graphql_name='nuclieTarget')
    bug_attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentType))), graphql_name='bugAttachments')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    configuration_name = sgqlc.types.Field(String, graphql_name='configurationName')
    connector_config = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='connectorConfig')
    scan = sgqlc.types.Field(AllScanLogType, graphql_name='scan')
    other_scans = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='otherScans')
    scanner_raw_response = sgqlc.types.Field(GenericScalar, graphql_name='scannerRawResponse')
    scan_raw_response = sgqlc.types.Field(GenericScalar, graphql_name='scanRawResponse')
    batch_id = sgqlc.types.Field(UUID, graphql_name='batchId')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')
    recently_rediscovered_batch_id = sgqlc.types.Field(UUID, graphql_name='recentlyRediscoveredBatchId')
    vulnerable_since = sgqlc.types.Field(DateTime, graphql_name='vulnerableSince')
    engagements = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementType'))), graphql_name='engagements')
    priority_last_updated = sgqlc.types.Field(DateTime, graphql_name='priorityLastUpdated')
    zero_day_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='zeroDayAvailable')
    is_wormable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isWormable')
    trend = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='trend')
    advisories_seen = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='advisoriesSeen')
    epss_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='epssScore')
    cisa_due_date = sgqlc.types.Field(Date, graphql_name='cisaDueDate')
    nist = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NISTType'))), graphql_name='nist')
    owasp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OWASPType'))), graphql_name='owasp')
    records_at_risk = sgqlc.types.Field(Int, graphql_name='recordsAtRisk')
    records_type = sgqlc.types.Field(Int, graphql_name='recordsType')
    fields = sgqlc.types.Field(GenericScalar, graphql_name='fields')
    links = sgqlc.types.Field(GenericScalar, graphql_name='links')
    metadata = sgqlc.types.Field(JSONString, graphql_name='metadata')
    asm_last_updated = sgqlc.types.Field(DateTime, graphql_name='asmLastUpdated')
    is_misconfiguration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMisconfiguration')
    sla_rule_search_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slaRuleSearchQuery')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    is_alert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAlert')
    patch = sgqlc.types.Field('PatchesType', graphql_name='patch')
    smart_close = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='smartClose')
    is_reopened = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isReopened')
    last_smart_closed_on = sgqlc.types.Field(DateTime, graphql_name='lastSmartClosedOn')
    last_reopened_on = sgqlc.types.Field(String, graphql_name='lastReopenedOn')
    is_automated_patched = sgqlc.types.Field(Boolean, graphql_name='isAutomatedPatched')
    patch_data = sgqlc.types.Field(GenericScalar, graphql_name='patchData')
    maintf = sgqlc.types.Field(String, graphql_name='maintf')
    tf_prev_state = sgqlc.types.Field(String, graphql_name='tfPrevState')
    last_data_enriched = sgqlc.types.Field(DateTime, graphql_name='lastDataEnriched')
    is_data_enriched = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDataEnriched')
    ai_title = sgqlc.types.Field(String, graphql_name='aiTitle')
    ai_description = sgqlc.types.Field(String, graphql_name='aiDescription')
    ai_mitigation = sgqlc.types.Field(String, graphql_name='aiMitigation')
    priority_rule_data = sgqlc.types.Field(JSONString, graphql_name='priorityRuleData')
    original_bug = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='originalBug')
    attachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentType))), graphql_name='attachmentSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')
    bug_tracker = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='bugTracker')
    approval_finding = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalFinding')
    ipaddress = sgqlc.types.Field(String, graphql_name='ipaddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    mac_address = sgqlc.types.Field(String, graphql_name='macAddress')
    os = sgqlc.types.Field(String, graphql_name='os')
    tracker = sgqlc.types.Field(sgqlc.types.list_of('TrackersType'), graphql_name='tracker')
    last_resolved_on = sgqlc.types.Field(String, graphql_name='lastResolvedOn')
    cost_of_risk = sgqlc.types.Field(Int, graphql_name='costOfRisk')
    port = sgqlc.types.Field(Int, graphql_name='port')
    duplicate_instances = sgqlc.types.Field(GenericScalar, graphql_name='duplicateInstances')
    content_object = sgqlc.types.Field(GenericScalar, graphql_name='contentObject')
    references = sgqlc.types.Field(sgqlc.types.list_of('ReferenceType'), graphql_name='references')
    config_content_object = sgqlc.types.Field(GenericScalar, graphql_name='configContentObject')
    maintf_content = sgqlc.types.Field(String, graphql_name='maintfContent')


class BugsCountType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs_count',)
    bugs_count = sgqlc.types.Field(Int, graphql_name='bugsCount')


class BulkAddToTrackerMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkArchiveEngagementsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagements',)
    engagements = sgqlc.types.Field(sgqlc.types.list_of('EngagementType'), graphql_name='engagements')


class BulkAssetAccessUserMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkBugAssignmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkBugUnAssignmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkDeleteAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkDeleteBugMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkDeleteFolders(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class BulkDeleteGroupMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups',)
    groups = sgqlc.types.Field(sgqlc.types.list_of('GroupsType'), graphql_name='groups')


class BulkDeleteOrgMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('members',)
    members = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='members')


class BulkDeleteOrganizationMemberMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('members',)
    members = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='members')


class BulkDeletePrerequisitesMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('prerequisites',)
    prerequisites = sgqlc.types.Field(sgqlc.types.list_of('PreRequisitesType'), graphql_name='prerequisites')


class BulkDeleteSoftwarePackageMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('packages',)
    packages = sgqlc.types.Field(sgqlc.types.list_of('SoftwarePackageType'), graphql_name='packages')


class BulkDeleteTeamMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('members',)
    members = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='members')


class BulkDeleteTemplateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field(sgqlc.types.list_of('TemplateType'), graphql_name='templates')


class BulkDeleteVaultMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('vaults',)
    vaults = sgqlc.types.Field(sgqlc.types.list_of('VaultType'), graphql_name='vaults')


class BulkDeleteViews(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class BulkLinkAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkMergeAssetsConfirmMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(String, graphql_name='assets')


class BulkMergeAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkMergeAssetsPreviewMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(Int, graphql_name='assets')


class BulkTestWithNuclieMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateArchiveAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkUpdateArchiveBugsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateAssessmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assessment',)
    assessment = sgqlc.types.Field(sgqlc.types.list_of(AssessmentType), graphql_name='assessment')


class BulkUpdateAssetCustomFields(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset',)
    asset = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='asset')


class BulkUpdateAssetFieldsWithCSVMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset',)
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')


class BulkUpdateAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkUpdateAssetsTagMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkUpdateBugCVEMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs', 'message')
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')
    message = sgqlc.types.Field(String, graphql_name='message')


class BulkUpdateBugCWEMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs', 'message')
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')
    message = sgqlc.types.Field(String, graphql_name='message')


class BulkUpdateBugCustomFieldMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateBugMitigationMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateBugMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateBugTagMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateBugTitleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class BulkUpdateBugsFieldsWithCSVMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug',)
    bug = sgqlc.types.Field(BugType, graphql_name='bug')


class BulkUpdateCredentialManager(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('configurations',)
    configurations = sgqlc.types.Field(sgqlc.types.list_of('ConfigurationType'), graphql_name='configurations')


class BulkUpdateEngagementsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagements',)
    engagements = sgqlc.types.Field(sgqlc.types.list_of('EngagementType'), graphql_name='engagements')


class BulkUpdateMemberAssetAccessMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('members',)
    members = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='members')


class BulkUpdateMemberPermissionAlertsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('members',)
    members = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='members')


class BulkUpdateOrgMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('users',)
    users = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='users')


class BulkUpdatePreRequisitesMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('prerequisites',)
    prerequisites = sgqlc.types.Field(sgqlc.types.list_of('PreRequisitesType'), graphql_name='prerequisites')


class BulkUpdateSoftwarePackageMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('packages',)
    packages = sgqlc.types.Field(sgqlc.types.list_of('SoftwarePackageType'), graphql_name='packages')


class BulkUpdateTeamMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('users',)
    users = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='users')


class CVEPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('CVEType'), graphql_name='objects')


class CVETrendItemType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cve_id', 'description', 'tag', 'percentage')
    cve_id = sgqlc.types.Field(String, graphql_name='cveId')
    description = sgqlc.types.Field(String, graphql_name='description')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    percentage = sgqlc.types.Field(Int, graphql_name='percentage')


class CVETrendsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cves',)
    cves = sgqlc.types.Field(sgqlc.types.list_of(CVETrendItemType), graphql_name='cves')


class CVEType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'description', 'cvss_v2_data', 'cvss_v3_data', 'cvss', 'cve_id', 'exploit_available', 'exploit_info', 'patch_available', 'patch_info', 'zero_day_available', 'is_wormable', 'ti_raw_response', 'nvd_raw_response', 'summary', 'published', 'last_modified', 'last_updated_nvd', 'last_updated_ti', 'trend', 'source', 'advisories_seen', 'epss_score', 'cisa_due_date', 'created', 'updated', 'cve_tags', 'related_cwe', 'cve_references', 'bug_cve')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    cvss_v2_data = sgqlc.types.Field(GenericScalar, graphql_name='cvssV2Data')
    cvss_v3_data = sgqlc.types.Field(GenericScalar, graphql_name='cvssV3Data')
    cvss = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cvss')
    cve_id = sgqlc.types.Field(String, graphql_name='cveId')
    exploit_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exploitAvailable')
    exploit_info = sgqlc.types.Field(GenericScalar, graphql_name='exploitInfo')
    patch_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='patchAvailable')
    patch_info = sgqlc.types.Field(GenericScalar, graphql_name='patchInfo')
    zero_day_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='zeroDayAvailable')
    is_wormable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isWormable')
    ti_raw_response = sgqlc.types.Field(GenericScalar, graphql_name='tiRawResponse')
    nvd_raw_response = sgqlc.types.Field(GenericScalar, graphql_name='nvdRawResponse')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    published = sgqlc.types.Field(DateTime, graphql_name='published')
    last_modified = sgqlc.types.Field(DateTime, graphql_name='lastModified')
    last_updated_nvd = sgqlc.types.Field(DateTime, graphql_name='lastUpdatedNvd')
    last_updated_ti = sgqlc.types.Field(DateTime, graphql_name='lastUpdatedTi')
    trend = sgqlc.types.Field(sgqlc.types.non_null(TenantCVETrendChoices), graphql_name='trend')
    source = sgqlc.types.Field(sgqlc.types.non_null(TenantCVESourceChoices), graphql_name='source')
    advisories_seen = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='advisoriesSeen')
    epss_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='epssScore')
    cisa_due_date = sgqlc.types.Field(Date, graphql_name='cisaDueDate')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    cve_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='cveTags')
    related_cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CWEType'))), graphql_name='relatedCwe')
    cve_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReferenceType'))), graphql_name='cveReferences')
    bug_cve = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugCve')


class CWEPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('CWEType'), graphql_name='objects')


class CWEType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'cwe_id', 'type', 'description', 'cwe_references', 'tenant_cwe_tags', 'bug_cwe')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cwe_id = sgqlc.types.Field(String, graphql_name='cweId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    description = sgqlc.types.Field(String, graphql_name='description')
    cwe_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReferenceType'))), graphql_name='cweReferences')
    tenant_cwe_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='tenantCweTags')
    bug_cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugCwe')


class CalculatePrioritizationScoreMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('message',)
    message = sgqlc.types.Field(String, graphql_name='message')


class CalculateRiskScoreMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('message',)
    message = sgqlc.types.Field(String, graphql_name='message')


class ClearDraft(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class CloneDefaultWidgetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('widget', 'graph_data')
    widget = sgqlc.types.Field('WidgetV2Type', graphql_name='widget')
    graph_data = sgqlc.types.Field(GenericScalar, graphql_name='graphData')


class CloneFoldersViewMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class CloseFindingType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('result',)
    result = sgqlc.types.Field(GenericScalar, graphql_name='result')


class CommentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'comment', 'bug', 'attachments', 'internal', 'activity', 'commented_by', 'connector_config', 'connector', 'team', 'approval', 'engagement', 'automation_workflow', 'automation_workflow_reason', 'references', 'created', 'updated', 'comment_id', 'organization_id', 'bug_id', 'engagement_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    comment = sgqlc.types.Field(String, graphql_name='comment')
    bug = sgqlc.types.Field('TestsType', graphql_name='bug')
    attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentType))), graphql_name='attachments')
    internal = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='internal')
    activity = sgqlc.types.Field('EngagementActivityType', graphql_name='activity')
    commented_by = sgqlc.types.Field(ApprovalUserType, graphql_name='commentedBy')
    connector_config = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='connectorConfig')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    approval = sgqlc.types.Field(ApprovalType, graphql_name='approval')
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')
    automation_workflow_reason = sgqlc.types.Field(JSONString, graphql_name='automationWorkflowReason')
    references = sgqlc.types.Field(JSONString, graphql_name='references')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    comment_id = sgqlc.types.Field(UUID, graphql_name='commentId')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    bug_id = sgqlc.types.Field(UUID, graphql_name='bugId')
    engagement_id = sgqlc.types.Field(UUID, graphql_name='engagementId')


class ComplexityBreakdownType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('low_complexity', 'medium_complexity', 'high_complexity')
    low_complexity = sgqlc.types.Field(Int, graphql_name='lowComplexity')
    medium_complexity = sgqlc.types.Field(Int, graphql_name='mediumComplexity')
    high_complexity = sgqlc.types.Field(Int, graphql_name='highComplexity')


class CompliancePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('ComplianceType'), graphql_name='objects')


class ComplianceType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'failed_count', 'slug')
    name = sgqlc.types.Field(String, graphql_name='name')
    failed_count = sgqlc.types.Field(Int, graphql_name='failedCount')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class ConfigurationType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'connector', 'organization', 'asset', 'team', 'object_id', 'key', 'remote_access_id', 'remote_access_url', 'created_by', 'is_default', 'created', 'updated', 'extra', 'triangulum', 'is_automated', 'auto_close_findings', 'auto_smart_merge_assets', 'send_csv_report_with_summary', 'enable_github_webhook', 'github_webhook_triggers', 'configurations_set', 'scanlog_set', 'bottask_set', 'automationworkflows_set', 'bug_set', 'activity_set', 'comment_set', 'tracker_configs')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    object_id = sgqlc.types.Field(Int, graphql_name='objectId')
    key = sgqlc.types.Field(String, graphql_name='key')
    remote_access_id = sgqlc.types.Field(UUID, graphql_name='remoteAccessId')
    remote_access_url = sgqlc.types.Field(String, graphql_name='remoteAccessUrl')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    triangulum = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='triangulum')
    is_automated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAutomated')
    auto_close_findings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoCloseFindings')
    auto_smart_merge_assets = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoSmartMergeAssets')
    send_csv_report_with_summary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendCsvReportWithSummary')
    enable_github_webhook = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableGithubWebhook')
    github_webhook_triggers = sgqlc.types.Field(JSONString, graphql_name='githubWebhookTriggers')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationsSet')
    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='scanlogSet')
    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BotTaskType))), graphql_name='bottaskSet')
    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='automationworkflowsSet')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')
    tracker_configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackerConfigs')


class ConfigurationsFieldType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'connector', 'organization', 'asset', 'team', 'object_id', 'key', 'remote_access_id', 'remote_access_url', 'created_by', 'is_default', 'created', 'updated', 'extra', 'triangulum', 'is_automated', 'auto_close_findings', 'auto_smart_merge_assets', 'send_csv_report_with_summary', 'enable_github_webhook', 'github_webhook_triggers', 'configurations_set', 'scanlog_set', 'bottask_set', 'automationworkflows_set', 'bug_set', 'activity_set', 'comment_set', 'tracker_configs')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    object_id = sgqlc.types.Field(Int, graphql_name='objectId')
    key = sgqlc.types.Field(String, graphql_name='key')
    remote_access_id = sgqlc.types.Field(UUID, graphql_name='remoteAccessId')
    remote_access_url = sgqlc.types.Field(String, graphql_name='remoteAccessUrl')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    triangulum = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='triangulum')
    is_automated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAutomated')
    auto_close_findings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoCloseFindings')
    auto_smart_merge_assets = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoSmartMergeAssets')
    send_csv_report_with_summary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendCsvReportWithSummary')
    enable_github_webhook = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableGithubWebhook')
    github_webhook_triggers = sgqlc.types.Field(JSONString, graphql_name='githubWebhookTriggers')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationsSet')
    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='scanlogSet')
    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BotTaskType))), graphql_name='bottaskSet')
    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='automationworkflowsSet')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')
    tracker_configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackerConfigs')


class ConfigurationsPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(ConfigurationsFieldType), graphql_name='objects')


class ConnectorInfoType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('connector_name', 'is_active')
    connector_name = sgqlc.types.Field(String, graphql_name='connectorName')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')


class ConnectorType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'slug', 'name', 'description', 'short_description', 'usage', 'image', 'link', 'type', 'license_type', 'scanner_type', 'is_internal', 'is_active', 'created', 'updated', 'asset_parent_connector', 'asset_other_parent_connector', 'configurations_set', 'parent_connector', 'activity_parent_connector', 'comments_parent_connector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')
    usage = sgqlc.types.Field(String, graphql_name='usage')
    image = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='image')
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    license_type = sgqlc.types.Field(Int, graphql_name='licenseType')
    scanner_type = sgqlc.types.Field(Int, graphql_name='scannerType')
    is_internal = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInternal')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    asset_parent_connector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetParentConnector')
    asset_other_parent_connector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetOtherParentConnector')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationsFieldType))), graphql_name='configurationsSet')
    parent_connector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='parentConnector')
    activity_parent_connector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activityParentConnector')
    comments_parent_connector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentsParentConnector')


class CreateAssetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset',)
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')


class CreateAssetRelationship(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset_relationship', 'success', 'message')
    asset_relationship = sgqlc.types.Field(sgqlc.types.list_of(AssetRelationshipType), graphql_name='assetRelationship')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class CreateAutomationWorkflowMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('automation_workflow',)
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')


class CreateBugMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug',)
    bug = sgqlc.types.Field(BugType, graphql_name='bug')


class CreateCloneSheetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('clone_sheet', 'message')
    clone_sheet = sgqlc.types.Field('SheetType', graphql_name='cloneSheet')
    message = sgqlc.types.Field(String, graphql_name='message')


class CreateCloneWorkBookMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('work_book', 'message')
    work_book = sgqlc.types.Field('WorkBookType', graphql_name='workBook')
    message = sgqlc.types.Field(String, graphql_name='message')


class CreateCustomAssessmentStatusMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('custom_assessment_status',)
    custom_assessment_status = sgqlc.types.Field('CustomAssessmentStatusType', graphql_name='customAssessmentStatus')


class CreateDashboardMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dashboard',)
    dashboard = sgqlc.types.Field('DashboardType', graphql_name='dashboard')


class CreateDraft(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('draft',)
    draft = sgqlc.types.Field('DraftType', graphql_name='draft')


class CreateEngagementMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagement',)
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')


class CreateGithubReportTemplateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field('TemplateType', graphql_name='templates')


class CreatePriorityRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rule',)
    rule = sgqlc.types.Field('PriorityRuleType', graphql_name='rule')


class CreatePriorityRuleSet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rule_set',)
    rule_set = sgqlc.types.Field('PriorityRuleSetType', graphql_name='ruleSet')


class CreateSLARuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sla_rule',)
    sla_rule = sgqlc.types.Field('ServiceLevelAgreementCustomRulesType', graphql_name='slaRule')


class CreateSoftwarePackageMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('packages',)
    packages = sgqlc.types.Field(sgqlc.types.list_of('SoftwarePackageType'), graphql_name='packages')


class CreateThread(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('thread', 'participants')
    thread = sgqlc.types.Field('PulseThreadType', graphql_name='thread')
    participants = sgqlc.types.Field(sgqlc.types.list_of('PulseParticipantType'), graphql_name='participants')


class CreateWidgetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('widget', 'graph_data')
    widget = sgqlc.types.Field('WidgetV2Type', graphql_name='widget')
    graph_data = sgqlc.types.Field(GenericScalar, graphql_name='graphData')


class CredentialManagerDetailType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'type', 'organization', 'extra', 'is_expired', 'fernet_key', 'created_by', 'config_count', 'created', 'updated', 'last_cached_repo_updated_on', 'automationworkflows_set', 'activity_credential')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(AppCredentialManagerTypeChoices), graphql_name='type')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    is_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExpired')
    fernet_key = sgqlc.types.Field(String, graphql_name='fernetKey')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    config_count = sgqlc.types.Field(Int, graphql_name='configCount')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    last_cached_repo_updated_on = sgqlc.types.Field(DateTime, graphql_name='lastCachedRepoUpdatedOn')
    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='automationworkflowsSet')
    activity_credential = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activityCredential')


class CustomAssessmentStatusPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('CustomAssessmentStatusType'), graphql_name='objects')


class CustomAssessmentStatusType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'parent_state', 'status', 'description', 'organization', 'created', 'updated', 'engagements_set', 'assessments_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent_state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='parentState')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    description = sgqlc.types.Field(String, graphql_name='description')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementType'))), graphql_name='engagementsSet')
    assessments_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='assessmentsSet')


class DashboardExportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('json_data',)
    json_data = sgqlc.types.Field(String, graphql_name='jsonData')


class DashboardImportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dashboard',)
    dashboard = sgqlc.types.Field('DashboardType', graphql_name='dashboard')


class DashboardStatsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_findings', 'high_priority', 'exploitable_open', 'open_critical_high')
    total_findings = sgqlc.types.Field('StatMetricType', graphql_name='totalFindings')
    high_priority = sgqlc.types.Field('StatMetricType', graphql_name='highPriority')
    exploitable_open = sgqlc.types.Field('StatMetricType', graphql_name='exploitableOpen')
    open_critical_high = sgqlc.types.Field('StatMetricType', graphql_name='openCriticalHigh')


class DashboardType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'slug', 'description', 'is_default', 'tags', 'data', 'organization', 'created_by', 'widgets', 'positional_data', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    data = sgqlc.types.Field(GenericScalar, graphql_name='data')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    widgets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgets')
    positional_data = sgqlc.types.Field(JSONString, graphql_name='positionalData')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class DashboardsTagType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'slug', 'name', 'organization', 'created', 'updated', 'dashboard_tags', 'widget_tags')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    dashboard_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='dashboardTags')
    widget_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetTags')


class DashboardsV2Type(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(DashboardType), graphql_name='objects')


class DataRetentionSettingsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'data_retention_type', 'delete_interval', 'is_enabled')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    data_retention_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dataRetentionType')
    delete_interval = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deleteInterval')
    is_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEnabled')


class DeduplicateBugConfirmMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class DeduplicateBugPreviewMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(Int, graphql_name='bugs')


class DeleteAssetFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset_field',)
    asset_field = sgqlc.types.Field(AssetFieldType, graphql_name='assetField')


class DeleteAssetRelationship(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class DeleteAutomationWorkMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('automation_workflow',)
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')


class DeleteBugFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug_field',)
    bug_field = sgqlc.types.Field(BugFieldType, graphql_name='bugField')


class DeleteCommentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('comments',)
    comments = sgqlc.types.Field(sgqlc.types.list_of(CommentType), graphql_name='comments')


class DeleteCustomAssessmentStatusMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteDashboardMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dashboard',)
    dashboard = sgqlc.types.Field(sgqlc.types.list_of(DashboardType), graphql_name='dashboard')


class DeleteEngagementFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagement_field',)
    engagement_field = sgqlc.types.Field('EngagementsFieldType', graphql_name='engagementField')


class DeletePresetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('presets',)
    presets = sgqlc.types.Field(sgqlc.types.list_of('PresetType'), graphql_name='presets')


class DeletePriorityRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeletePriorityRuleSet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteSLARuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'bug_count')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    bug_count = sgqlc.types.Field(BugsCountType, graphql_name='bugCount')


class DeleteSelfManagedServiceMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('service',)
    service = sgqlc.types.Field(sgqlc.types.list_of('SelfManagedServiceType'), graphql_name='service')


class DeleteWidgetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('widgets',)
    widgets = sgqlc.types.Field(sgqlc.types.list_of('WidgetV2Type'), graphql_name='widgets')


class DestroyBulkReportAttachmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('attachments',)
    attachments = sgqlc.types.Field(sgqlc.types.list_of('ReportAttachmentType'), graphql_name='attachments')


class DestroyBulkReportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('reports',)
    reports = sgqlc.types.Field(sgqlc.types.list_of('ReportType'), graphql_name='reports')


class DistributionGroupType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('label', 'count')
    label = sgqlc.types.Field(String, graphql_name='label')
    count = sgqlc.types.Field(Int, graphql_name='count')


class DockerRegistryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(String, graphql_name='url')


class DockerRegistryTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(DockerRegistryType), graphql_name='objects')


class DownloadSheetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message', 'download_url', 'file_name')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')
    download_url = sgqlc.types.Field(String, graphql_name='downloadUrl')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')


class DraftType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'draft_type', 'bug_level', 'report_template', 'created_by', 'organization', 'draft_hash', 'created', 'draft_data', 'draft_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    draft_type = sgqlc.types.Field(Int, graphql_name='draftType')
    bug_level = sgqlc.types.Field(Int, graphql_name='bugLevel')
    report_template = sgqlc.types.Field('TemplateType', graphql_name='reportTemplate')
    created_by = sgqlc.types.Field(sgqlc.types.non_null(ApprovalUserType), graphql_name='createdBy')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    draft_hash = sgqlc.types.Field(String, graphql_name='draftHash')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    draft_data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='draftData')
    draft_name = sgqlc.types.Field(String, graphql_name='draftName')


class DuplicateFindingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_possible_duplicates', 'message')
    all_possible_duplicates = sgqlc.types.Field(AllPossibleDuplicatesType, graphql_name='allPossibleDuplicates')
    message = sgqlc.types.Field(String, graphql_name='message')


class ECRImagesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(String, graphql_name='url')


class ECRImagesTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(ECRImagesType), graphql_name='objects')


class EPSSHighRiskItemType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cve_id', 'title', 'epss_percentage', 'cvss_score')
    cve_id = sgqlc.types.Field(String, graphql_name='cveId')
    title = sgqlc.types.Field(String, graphql_name='title')
    epss_percentage = sgqlc.types.Field(Float, graphql_name='epssPercentage')
    cvss_score = sgqlc.types.Field(Float, graphql_name='cvssScore')


class EngagementActivityPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('EngagementActivityType'), graphql_name='objects')


class EngagementActivityType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'action', 'data', 'user', 'team', 'bug', 'asset', 'connector_config', 'engagement', 'connector', 'credential_manager', 'task', 'bot_task', 'approval', 'is_automation_activity', 'automation_workflow', 'automation_workflow_reason', 'created', 'updated', 'comment_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='action')
    data = sgqlc.types.Field(GenericScalar, graphql_name='data')
    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    bug = sgqlc.types.Field('TestsType', graphql_name='bug')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    connector_config = sgqlc.types.Field(ConfigurationsFieldType, graphql_name='connectorConfig')
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')
    connector = sgqlc.types.Field(ConnectorType, graphql_name='connector')
    credential_manager = sgqlc.types.Field(CredentialManagerDetailType, graphql_name='credentialManager')
    task = sgqlc.types.Field(AllScanLogType, graphql_name='task')
    bot_task = sgqlc.types.Field(BotTaskType, graphql_name='botTask')
    approval = sgqlc.types.Field(ApprovalType, graphql_name='approval')
    is_automation_activity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAutomationActivity')
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')
    automation_workflow_reason = sgqlc.types.Field(JSONString, graphql_name='automationWorkflowReason')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')


class EngagementAssetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='objects')


class EngagementBugPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='objects')


class EngagementCommentPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('EngagementCommentType'), graphql_name='objects')


class EngagementCommentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'comment', 'bug', 'attachments', 'internal', 'activity', 'commented_by', 'connector_config', 'connector', 'team', 'approval', 'engagement', 'automation_workflow', 'automation_workflow_reason', 'references', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')
    bug = sgqlc.types.Field('TestsType', graphql_name='bug')
    attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentType))), graphql_name='attachments')
    internal = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='internal')
    activity = sgqlc.types.Field(EngagementActivityType, graphql_name='activity')
    commented_by = sgqlc.types.Field(ApprovalUserType, graphql_name='commentedBy')
    connector_config = sgqlc.types.Field(ConfigurationsFieldType, graphql_name='connectorConfig')
    connector = sgqlc.types.Field(ConnectorType, graphql_name='connector')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    approval = sgqlc.types.Field(ApprovalType, graphql_name='approval')
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')
    automation_workflow_reason = sgqlc.types.Field(JSONString, graphql_name='automationWorkflowReason')
    references = sgqlc.types.Field(JSONString, graphql_name='references')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class EngagementConnectorType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('connector', 'is_attached', 'configuration_count')
    connector = sgqlc.types.Field(ConnectorType, graphql_name='connector')
    is_attached = sgqlc.types.Field(Boolean, graphql_name='isAttached')
    configuration_count = sgqlc.types.Field(Int, graphql_name='configurationCount')


class EngagementFieldPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('EngagementsFieldType'), graphql_name='objects')


class EngagementPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('EngagementType'), graphql_name='objects')


class EngagementType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'engagement_custom_id', 'name', 'organization', 'vendor', 'security_posture', 'scheduled_date', 'delivery_date', 'documents', 'subscribed_services', 'checked_terms_and_conditions', 'executive_summary', 'credits_estimated', 'credits', 'is_self_managed_engagement', 'created_by', 'created', 'updated', 'is_active', 'plans', 'fields', 'state', 'custom_status', 'assignees', 'engagement_assessment', 'prerequisites_engagement', 'work_books', 'exportreport_set', 'bug_engagements', 'activity_engagement', 'comments_engagement', 'assessments_count', 'engagement_completion', 'assessments_per_service', 'total_hours_spent', 'prerequisites_completion', 'state_id', 'parent_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    engagement_custom_id = sgqlc.types.Field(Int, graphql_name='engagementCustomId')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    vendor = sgqlc.types.Field('VendorType', graphql_name='vendor')
    security_posture = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='securityPosture')
    scheduled_date = sgqlc.types.Field(Date, graphql_name='scheduledDate')
    delivery_date = sgqlc.types.Field(Date, graphql_name='deliveryDate')
    documents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='documents')
    subscribed_services = sgqlc.types.Field(GenericScalar, graphql_name='subscribedServices')
    checked_terms_and_conditions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkedTermsAndConditions')
    executive_summary = sgqlc.types.Field(String, graphql_name='executiveSummary')
    credits_estimated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='creditsEstimated')
    credits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='credits')
    is_self_managed_engagement = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSelfManagedEngagement')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    plans = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='plans')
    fields = sgqlc.types.Field(JSONString, graphql_name='fields')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')
    custom_status = sgqlc.types.Field(CustomAssessmentStatusType, graphql_name='customStatus')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalUserType))), graphql_name='assignees')
    engagement_assessment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='engagementAssessment')
    prerequisites_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PreRequisitesType'))), graphql_name='prerequisitesEngagement')
    work_books = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkBookType'))), graphql_name='workBooks')
    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='exportreportSet')
    bug_engagements = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugEngagements')
    activity_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementActivityType))), graphql_name='activityEngagement')
    comments_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementCommentType))), graphql_name='commentsEngagement')
    assessments_count = sgqlc.types.Field(Int, graphql_name='assessmentsCount')
    engagement_completion = sgqlc.types.Field(Int, graphql_name='engagementCompletion')
    assessments_per_service = sgqlc.types.Field(GenericScalar, graphql_name='assessmentsPerService')
    total_hours_spent = sgqlc.types.Field(Int, graphql_name='totalHoursSpent')
    prerequisites_completion = sgqlc.types.Field(GenericScalar, graphql_name='prerequisitesCompletion')
    state_id = sgqlc.types.Field(Int, graphql_name='stateId')
    parent_state = sgqlc.types.Field(Int, graphql_name='parentState')


class EngagementsFieldType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'slug', 'description', 'field_type', 'options', 'is_required', 'is_active', 'extra_data', 'created', 'updated', 'engagementsfield', 'assetfield', 'bugfield', 'organization')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldType')
    options = sgqlc.types.Field(GenericScalar, graphql_name='options')
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    extra_data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='extraData')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    engagementsfield = sgqlc.types.Field('EngagementsFieldType', graphql_name='engagementsfield')
    assetfield = sgqlc.types.Field(AssetFieldType, graphql_name='assetfield')
    bugfield = sgqlc.types.Field(BugFieldType, graphql_name='bugfield')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')


class EventEnvelopeType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'seq', 'ts', 'thread_id', 'run_id', 'type', 'actor', 'agent_id', 'agent_name', 'task_id', 'severity', 'payload', 'version', 'correlation_id', 'trace_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    seq = sgqlc.types.Field(Int, graphql_name='seq')
    ts = sgqlc.types.Field(String, graphql_name='ts')
    thread_id = sgqlc.types.Field(String, graphql_name='threadId')
    run_id = sgqlc.types.Field(String, graphql_name='runId')
    type = sgqlc.types.Field(String, graphql_name='type')
    actor = sgqlc.types.Field(String, graphql_name='actor')
    agent_id = sgqlc.types.Field(String, graphql_name='agentId')
    agent_name = sgqlc.types.Field(String, graphql_name='agentName')
    task_id = sgqlc.types.Field(String, graphql_name='taskId')
    severity = sgqlc.types.Field(String, graphql_name='severity')
    payload = sgqlc.types.Field(GenericScalar, graphql_name='payload')
    version = sgqlc.types.Field(String, graphql_name='version')
    correlation_id = sgqlc.types.Field(String, graphql_name='correlationId')
    trace_id = sgqlc.types.Field(String, graphql_name='traceId')


class ExportEngagementsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')


class FilterViewsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'created_by', 'organization', 'filter_data', 'shared_with', 'share_with_everyone', 'is_bug_view', 'is_asset_view', 'is_default')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    filter_data = sgqlc.types.Field(GenericScalar, graphql_name='filterData')
    shared_with = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalUserType))), graphql_name='sharedWith')
    share_with_everyone = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shareWithEveryone')
    is_bug_view = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBugView')
    is_asset_view = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAssetView')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')


class FindingAnalysisType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_count', 'percentage_change', 'severity_counts', 'state_counts', 'sources')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    percentage_change = sgqlc.types.Field(Float, graphql_name='percentageChange')
    severity_counts = sgqlc.types.Field('SeverityCountType', graphql_name='severityCounts')
    state_counts = sgqlc.types.Field('StateCountType', graphql_name='stateCounts')
    sources = sgqlc.types.Field(sgqlc.types.list_of('SourceDistributionType'), graphql_name='sources')


class GenerateReportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('reports', 'password', 'password_required')
    reports = sgqlc.types.Field(String, graphql_name='reports')
    password = sgqlc.types.Field(String, graphql_name='password')
    password_required = sgqlc.types.Field(Boolean, graphql_name='passwordRequired')


class GithubBranchesBatchType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('results',)
    results = sgqlc.types.Field(sgqlc.types.list_of('GithubBranchesType'), graphql_name='results')


class GithubBranchesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('repo_url', 'branches')
    repo_url = sgqlc.types.Field(String, graphql_name='repoUrl')
    branches = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='branches')


class GithubRepositoriesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('repo_url',)
    repo_url = sgqlc.types.Field(String, graphql_name='repoUrl')


class GithubRepositoriesTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(GithubRepositoriesType), graphql_name='objects')


class GroupAssetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='objects')


class GroupBugPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('objects', 'has_next', 'has_previous', 'last_cursor', 'before_cursor')
    objects = sgqlc.types.Field(GenericScalar, graphql_name='objects')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_previous = sgqlc.types.Field(Boolean, graphql_name='hasPrevious')
    last_cursor = sgqlc.types.Field(String, graphql_name='lastCursor')
    before_cursor = sgqlc.types.Field(String, graphql_name='beforeCursor')


class GroupPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('GroupsType'), graphql_name='objects')


class GroupsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'assets', 'created_by', 'created')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assets')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')


class ImportSheetCSVMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message', 'data')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')
    data = sgqlc.types.Field(sgqlc.types.list_of(JSONString), graphql_name='data')


class IndustryBenchmarkType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('critical', 'high', 'medium', 'overall')
    critical = sgqlc.types.Field(Int, graphql_name='critical')
    high = sgqlc.types.Field(Int, graphql_name='high')
    medium = sgqlc.types.Field(Int, graphql_name='medium')
    overall = sgqlc.types.Field(Int, graphql_name='overall')


class IntegrationItemType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'connector_name', 'status', 'last_sync', 'data_points')
    name = sgqlc.types.Field(String, graphql_name='name')
    connector_name = sgqlc.types.Field(String, graphql_name='connectorName')
    status = sgqlc.types.Field(String, graphql_name='status')
    last_sync = sgqlc.types.Field(String, graphql_name='lastSync')
    data_points = sgqlc.types.Field(Int, graphql_name='dataPoints')


class IntegrationStatusType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('overall_health', 'active_integrations', 'total_integrations', 'failed_connections', 'average_response_time', 'integrations')
    overall_health = sgqlc.types.Field(Int, graphql_name='overallHealth')
    active_integrations = sgqlc.types.Field(Int, graphql_name='activeIntegrations')
    total_integrations = sgqlc.types.Field(Int, graphql_name='totalIntegrations')
    failed_connections = sgqlc.types.Field(Int, graphql_name='failedConnections')
    average_response_time = sgqlc.types.Field(Float, graphql_name='averageResponseTime')
    integrations = sgqlc.types.Field(sgqlc.types.list_of(IntegrationItemType), graphql_name='integrations')


class ListScans(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'scans')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    scans = sgqlc.types.Field(sgqlc.types.list_of('ScanType'), graphql_name='scans')


class MemberType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'user', 'organization', 'role', 'asset_search_query', 'permitted_apps', 'permitted_modules', 'default_page', 'default_asset_view', 'default_finding_view', 'permitted_dashboards', 'my_favorites', 'preset_set', 'approval_approved_by', 'approval_raised_by', 'is_active', 'engagements', 'assets')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    role = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='role')
    asset_search_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetSearchQuery')
    permitted_apps = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='permittedApps')
    permitted_modules = sgqlc.types.Field(JSONString, graphql_name='permittedModules')
    default_page = sgqlc.types.Field(JSONString, graphql_name='defaultPage')
    default_asset_view = sgqlc.types.Field(JSONString, graphql_name='defaultAssetView')
    default_finding_view = sgqlc.types.Field(JSONString, graphql_name='defaultFindingView')
    permitted_dashboards = sgqlc.types.Field(JSONString, graphql_name='permittedDashboards')
    my_favorites = sgqlc.types.Field(JSONString, graphql_name='myFavorites')
    preset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PresetType'))), graphql_name='presetSet')
    approval_approved_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalApprovedBy')
    approval_raised_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalRaisedBy')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    engagements = sgqlc.types.Field(sgqlc.types.list_of(EngagementType), graphql_name='engagements')
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class MergeDuplicateAssetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_possible_duplicates', 'message')
    all_possible_duplicates = sgqlc.types.Field(AllPossibleDuplicatesType, graphql_name='allPossibleDuplicates')
    message = sgqlc.types.Field(String, graphql_name='message')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bulk_update_member_permission_alerts', 'bulk_delete_organization_member', 'create_thread', 'send_message', 'select_agents_for_thread', 'start_background_run', 'start_system_agent_chat', 'revert_bulk_update_action', 'update_merge_duplicate_asset', 'update_duplicate_findings', 'create_prefills', 'update_prefills', 'delete_prefills', 'bulk_create_and_update', 'list_scans', 'add_self_managed_service', 'update_self_managed_service', 'delete_self_managed_service', 'bulk_delete_folders', 'bulk_delete_views', 'my_favorites_views', 'clone_folders', 'create_work_book', 'update_work_book', 'delete_work_book', 'clone_create_work_book', 'create_sheet', 'update_sheet', 'delete_sheet', 'clone_create_sheet', 'update_sheet_row', 'delete_sheet_row', 'import_csv', 'download_csv_sheet', 'create_draft', 'clear_draft', 'create_automation_workflow', 'update_automation_workflow', 'delete_automation_workflow', 'trigger_automation_workflow', 'test_pipeline_code', 'create_sla_rule', 'update_sla_rule', 'delete_sla_rule', 'add_preset', 'update_presets', 'delete_presets', 'update_data_retention_setting', 'update_asm_settings', 'bulk_update_credential_manager', 'update_credential_manager_state', 'vaults', 'add_vault_attachment', 'bulk_delete_vault_mutation', 'add_widget', 'update_widgets', 'delete_widgets', 'clone_widget', 'add_dashboard', 'update_dashboard', 'delete_dashboard', 'export_dashboard', 'import_dashboard', 'comment_update', 'comment_delete', 'assessment', 'bulk_update_prerequisites', 'bulk_delete_prerequisites', 'update_assessments', 'bulk_update_assessment', 'create_custom_assessment_status', 'update_custom_assessment_status', 'delete_custom_assessment_status', 'update_engagement', 'add_attachment', 'bulk_update_engagements', 'archive_engagements', 'create_engagement', 'export_engagements', 'add_engagements_field_settings_mutation', 'delete_engagement_field_settings_mutation', 'update_engagement_field_settings_mutation', 'assign_asset_view_to_users', 'add_report_attachment', 'bulk_delete_attachment', 'restore_default_prioritization_rule', 'update_prioritization_settings', 'create_priority_rule_set', 'update_priority_rule_set', 'delete_priority_rule_set', 'create_priority_rule', 'update_priority_rule', 'delete_priority_rule', 'report_bulk_delete', 'generate_report', 'update_report', 'show_report_password', 'set_report_password', 'delete_report_template', 'add_report_template', 'update_report_template', 'create_github_report_template', 'add_group', 'update_group', 'group_bulk_delete', 'org_member_role_bulk_update', 'team_member_role_bulk_update', 'org_member_role_bulk_delete', 'team_member_role_bulk_delete', 'bulk_update_member_asset_access', 'bug_bulk_update', 'bug_bulk_assignment', 'bug_bulk_unassignment', 'bug_bulk_update_tags', 'bug_bulk_update_cve', 'bug_bulk_update_cwe', 'bug_bulk_delete', 'add_bulk_comment', 'bug_bulk_add_to_tracker', 'approve_state_change', 'deduplicate_bug_preview', 'deduplicate_bug_confirm', 'calculate_priority_score', 'transfer_engagement_bugs', 'bug_update_risk_records', 'add_bug_settings_fields', 'update_bug_settings_fields', 'delete_bug_settings_fields', 'bug_bulk_update_title', 'bug_bulk_update_mitigation_description', 'archive_bug_bulk_update', 'bug_bulk_update_custom_fields', 'update_bugs_fields_with_csv', 'bug_create', 'sync_bug_with_trackers', 'test_with_nuclie_template', 'bulk_test_with_nuclie_template', 'assets_bulk_update', 'assets_bulk_merge', 'assets_bulk_link', 'assets_bulk_delete', 'assets_bulk_update_tags', 'archive_assets_bulk_update', 'assets_merge_preview', 'assets_merge_confirm', 'calculate_risk_score', 'software_packages_bulk_update', 'software_packages_bulk_delete', 'software_package_create', 'add_asset_settings_fields', 'update_asset_settings_fields', 'delete_asset_settings_fields', 'bulk_update_asset_custom_field_mutation', 'create_asset', 'update_asset_fields_with_csv', 'bulk_asset_access_user_mutation', 'create_asset_relationship', 'update_asset_relationship', 'delete_asset_relationship')
    bulk_update_member_permission_alerts = sgqlc.types.Field(BulkUpdateMemberPermissionAlertsMutation, graphql_name='bulkUpdateMemberPermissionAlerts', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(Int, graphql_name='role', default=None)),
        ('update_notifications', sgqlc.types.Arg(JSONString, graphql_name='updateNotifications', default=None)),
        ('update_permissions', sgqlc.types.Arg(JSONString, graphql_name='updatePermissions', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='userIds', default=None)),
))
    )
    bulk_delete_organization_member = sgqlc.types.Field(BulkDeleteOrganizationMemberMutation, graphql_name='bulkDeleteOrganizationMember', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='userIds', default=None)),
))
    )
    create_thread = sgqlc.types.Field(CreateThread, graphql_name='createThread', args=sgqlc.types.ArgDict((
        ('agent_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='agentIds', default=None)),
        ('context', sgqlc.types.Arg(GenericScalar, graphql_name='context', default=None)),
        ('mode', sgqlc.types.Arg(String, graphql_name='mode', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
))
    )
    send_message = sgqlc.types.Field('SendMessage', graphql_name='sendMessage', args=sgqlc.types.ArgDict((
        ('attachments', sgqlc.types.Arg(GenericScalar, graphql_name='attachments', default=None)),
        ('context', sgqlc.types.Arg(GenericScalar, graphql_name='context', default=None)),
        ('text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='text', default=None)),
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
))
    )
    select_agents_for_thread = sgqlc.types.Field('SelectAgentsForThread', graphql_name='selectAgentsForThread', args=sgqlc.types.ArgDict((
        ('agent_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='agentIds', default=None)),
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
))
    )
    start_background_run = sgqlc.types.Field('StartBackgroundRun', graphql_name='startBackgroundRun', args=sgqlc.types.ArgDict((
        ('agent_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='agentIds', default=None)),
        ('context', sgqlc.types.Arg(GenericScalar, graphql_name='context', default=None)),
        ('input_text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='inputText', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
))
    )
    start_system_agent_chat = sgqlc.types.Field('StartSystemAgentChat', graphql_name='startSystemAgentChat', args=sgqlc.types.ArgDict((
        ('agent_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='agentId', default=None)),
        ('context', sgqlc.types.Arg(GenericScalar, graphql_name='context', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
))
    )
    revert_bulk_update_action = sgqlc.types.Field('RevertBulkUpdateActionMutation', graphql_name='revertBulkUpdateAction', args=sgqlc.types.ArgDict((
        ('bot_task_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='botTaskId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_merge_duplicate_asset = sgqlc.types.Field(MergeDuplicateAssetMutation, graphql_name='updateMergeDuplicateAsset', args=sgqlc.types.ArgDict((
        ('main_asset_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mainAssetId', default=None)),
        ('merge_asset_id', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mergeAssetId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_duplicate_findings = sgqlc.types.Field(DuplicateFindingsMutation, graphql_name='updateDuplicateFindings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('primary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='primaryId', default=None)),
        ('to_be_duplicated_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='toBeDuplicatedIds', default=None)),
))
    )
    create_prefills = sgqlc.types.Field('PrefillsCreateMutation', graphql_name='createPrefills', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('prefills_condition', sgqlc.types.Arg(JSONString, graphql_name='prefillsCondition', default=None)),
        ('prefills_data', sgqlc.types.Arg(JSONString, graphql_name='prefillsData', default=None)),
))
    )
    update_prefills = sgqlc.types.Field('PrefillsUpdateMutation', graphql_name='updatePrefills', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('prefills_condition', sgqlc.types.Arg(JSONString, graphql_name='prefillsCondition', default=None)),
        ('prefills_data', sgqlc.types.Arg(JSONString, graphql_name='prefillsData', default=None)),
))
    )
    delete_prefills = sgqlc.types.Field('PrefillsBulkDeleteMutation', graphql_name='deletePrefills', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bulk_create_and_update = sgqlc.types.Field('PrefillsBulkCreateAndUpdateMutation', graphql_name='bulkCreateAndUpdate', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('override_existing_prefills', sgqlc.types.Arg(Boolean, graphql_name='overrideExistingPrefills', default=None)),
))
    )
    list_scans = sgqlc.types.Field(ListScans, graphql_name='listScans', args=sgqlc.types.ArgDict((
        ('credential_manager', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='credentialManager', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    add_self_managed_service = sgqlc.types.Field(AddSelfManagedServiceMutation, graphql_name='addSelfManagedService', args=sgqlc.types.ArgDict((
        ('category_id', sgqlc.types.Arg(UUID, graphql_name='categoryId', default=None)),
        ('category_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='categoryName', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_self_managed_service = sgqlc.types.Field('UpdateSelfManagedServiceMutation', graphql_name='updateSelfManagedService', args=sgqlc.types.ArgDict((
        ('category_id', sgqlc.types.Arg(UUID, graphql_name='categoryId', default=None)),
        ('category_name', sgqlc.types.Arg(String, graphql_name='categoryName', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    delete_self_managed_service = sgqlc.types.Field(DeleteSelfManagedServiceMutation, graphql_name='deleteSelfManagedService', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bulk_delete_folders = sgqlc.types.Field(BulkDeleteFolders, graphql_name='bulkDeleteFolders', args=sgqlc.types.ArgDict((
        ('folder_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='folderIds', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bulk_delete_views = sgqlc.types.Field(BulkDeleteViews, graphql_name='bulkDeleteViews', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('view_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='viewIds', default=None)),
))
    )
    my_favorites_views = sgqlc.types.Field('MyFavoritesViewsMutation', graphql_name='myFavoritesViews', args=sgqlc.types.ArgDict((
        ('add', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='add', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('remove', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='remove', default=None)),
))
    )
    clone_folders = sgqlc.types.Field(CloneFoldersViewMutation, graphql_name='cloneFolders', args=sgqlc.types.ArgDict((
        ('folder_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='folderId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    create_work_book = sgqlc.types.Field('WorkBookCreateMutation', graphql_name='createWorkBook', args=sgqlc.types.ArgDict((
        ('engagement_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='engagementIds', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_work_book = sgqlc.types.Field('WorkBookUpdateMutation', graphql_name='updateWorkBook', args=sgqlc.types.ArgDict((
        ('engagement_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='engagementIds', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    delete_work_book = sgqlc.types.Field('WorkBookDeleteMutation', graphql_name='deleteWorkBook', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    clone_create_work_book = sgqlc.types.Field(CreateCloneWorkBookMutation, graphql_name='cloneCreateWorkBook', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('work_book_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='workBookId', default=None)),
))
    )
    create_sheet = sgqlc.types.Field('SheetCreateMutation', graphql_name='createSheet', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('row_data', sgqlc.types.Arg(JSONString, graphql_name='rowData', default=None)),
        ('state', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(JSONString)), graphql_name='state', default=None)),
        ('work_book_id', sgqlc.types.Arg(Int, graphql_name='workBookId', default=None)),
))
    )
    update_sheet = sgqlc.types.Field('SheetUpdateMutation', graphql_name='updateSheet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('state', sgqlc.types.Arg(sgqlc.types.list_of(JSONString), graphql_name='state', default=None)),
))
    )
    delete_sheet = sgqlc.types.Field('SheetDeleteMutation', graphql_name='deleteSheet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    clone_create_sheet = sgqlc.types.Field(CreateCloneSheetMutation, graphql_name='cloneCreateSheet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('work_book_id', sgqlc.types.Arg(Int, graphql_name='workBookId', default=None)),
))
    )
    update_sheet_row = sgqlc.types.Field('SheetRowUpdateMutation', graphql_name='updateSheetRow', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('row_data', sgqlc.types.Arg(JSONString, graphql_name='rowData', default=None)),
        ('sheet_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sheetId', default=None)),
))
    )
    delete_sheet_row = sgqlc.types.Field('SheetRowDeleteMutation', graphql_name='deleteSheetRow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    import_csv = sgqlc.types.Field(ImportSheetCSVMutation, graphql_name='importCsv', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('import_override', sgqlc.types.Arg(Boolean, graphql_name='importOverride', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('sheet_id', sgqlc.types.Arg(Int, graphql_name='sheetId', default=None)),
        ('work_book_id', sgqlc.types.Arg(Int, graphql_name='workBookId', default=None)),
))
    )
    download_csv_sheet = sgqlc.types.Field(DownloadSheetMutation, graphql_name='downloadCsvSheet', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('sheet_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sheetId', default=None)),
))
    )
    create_draft = sgqlc.types.Field(CreateDraft, graphql_name='createDraft', args=sgqlc.types.ArgDict((
        ('bug_level', sgqlc.types.Arg(Int, graphql_name='bugLevel', default=None)),
        ('draft_data', sgqlc.types.Arg(JSONString, graphql_name='draftData', default=None)),
        ('draft_id', sgqlc.types.Arg(Int, graphql_name='draftId', default=None)),
        ('draft_type', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='draftType', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('report_template_id', sgqlc.types.Arg(Int, graphql_name='reportTemplateId', default=None)),
))
    )
    clear_draft = sgqlc.types.Field(ClearDraft, graphql_name='clearDraft', args=sgqlc.types.ArgDict((
        ('draft_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='draftId', default=None)),
))
    )
    create_automation_workflow = sgqlc.types.Field(CreateAutomationWorkflowMutation, graphql_name='createAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('credential_manager_id', sgqlc.types.Arg(Int, graphql_name='credentialManagerId', default=None)),
        ('document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='documentIds', default=None)),
        ('group_by', sgqlc.types.Arg(String, graphql_name='groupBy', default=None)),
        ('hooks', sgqlc.types.Arg(GenericScalar, graphql_name='hooks', default=None)),
        ('ignore_weightage', sgqlc.types.Arg(Boolean, graphql_name='ignoreWeightage', default=None)),
        ('instructions', sgqlc.types.Arg(String, graphql_name='instructions', default=None)),
        ('llm_model', sgqlc.types.Arg(Int, graphql_name='llmModel', default=None)),
        ('module', sgqlc.types.Arg(Int, graphql_name='module', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('pipeline_code', sgqlc.types.Arg(String, graphql_name='pipelineCode', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
        ('schedule_day_of_week', sgqlc.types.Arg(Int, graphql_name='scheduleDayOfWeek', default=None)),
        ('schedule_frequency', sgqlc.types.Arg(Int, graphql_name='scheduleFrequency', default=None)),
        ('schedule_time', sgqlc.types.Arg(Time, graphql_name='scheduleTime', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
        ('tool', sgqlc.types.Arg(Int, graphql_name='tool', default=None)),
        ('tools', sgqlc.types.Arg(GenericScalar, graphql_name='tools', default=None)),
        ('triggers', sgqlc.types.Arg(GenericScalar, graphql_name='triggers', default=None)),
        ('weightage', sgqlc.types.Arg(Int, graphql_name='weightage', default=None)),
        ('workflow_mode', sgqlc.types.Arg(Int, graphql_name='workflowMode', default=None)),
))
    )
    update_automation_workflow = sgqlc.types.Field('UpdateAutomationWorkflowMutation', graphql_name='updateAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('credential_manager_id', sgqlc.types.Arg(Int, graphql_name='credentialManagerId', default=None)),
        ('document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='documentIds', default=None)),
        ('group_by', sgqlc.types.Arg(String, graphql_name='groupBy', default=None)),
        ('hooks', sgqlc.types.Arg(GenericScalar, graphql_name='hooks', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('ignore_weightage', sgqlc.types.Arg(Boolean, graphql_name='ignoreWeightage', default=None)),
        ('instructions', sgqlc.types.Arg(String, graphql_name='instructions', default=None)),
        ('llm_model', sgqlc.types.Arg(Int, graphql_name='llmModel', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('pipeline_code', sgqlc.types.Arg(String, graphql_name='pipelineCode', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
        ('schedule_day_of_week', sgqlc.types.Arg(Int, graphql_name='scheduleDayOfWeek', default=None)),
        ('schedule_frequency', sgqlc.types.Arg(Int, graphql_name='scheduleFrequency', default=None)),
        ('schedule_time', sgqlc.types.Arg(Time, graphql_name='scheduleTime', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
        ('tools', sgqlc.types.Arg(GenericScalar, graphql_name='tools', default=None)),
        ('triggers', sgqlc.types.Arg(GenericScalar, graphql_name='triggers', default=None)),
        ('weightage', sgqlc.types.Arg(Int, graphql_name='weightage', default=None)),
        ('workflow_mode', sgqlc.types.Arg(Int, graphql_name='workflowMode', default=None)),
))
    )
    delete_automation_workflow = sgqlc.types.Field(DeleteAutomationWorkMutation, graphql_name='deleteAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    trigger_automation_workflow = sgqlc.types.Field('TriggerAutomationWorkflowMutation', graphql_name='triggerAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('enrol_search_query', sgqlc.types.Arg(String, graphql_name='enrolSearchQuery', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    test_pipeline_code = sgqlc.types.Field('TestPipelineCodeMutation', graphql_name='testPipelineCode', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(String, graphql_name='code', default=None)),
        ('module', sgqlc.types.Arg(Int, graphql_name='module', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('use_queryset', sgqlc.types.Arg(Boolean, graphql_name='useQueryset', default=None)),
))
    )
    create_sla_rule = sgqlc.types.Field(CreateSLARuleMutation, graphql_name='createSlaRule', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('rules_data', sgqlc.types.Arg(sgqlc.types.non_null(GenericScalar), graphql_name='rulesData', default=None)),
        ('update_existing_findings', sgqlc.types.Arg(Boolean, graphql_name='updateExistingFindings', default=False)),
))
    )
    update_sla_rule = sgqlc.types.Field('UpdateSLARuleMutation', graphql_name='updateSlaRule', args=sgqlc.types.ArgDict((
        ('duration', sgqlc.types.Arg(Int, graphql_name='duration', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('preview', sgqlc.types.Arg(Boolean, graphql_name='preview', default=False)),
        ('rule_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='ruleId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('weightage', sgqlc.types.Arg(Int, graphql_name='weightage', default=None)),
))
    )
    delete_sla_rule = sgqlc.types.Field(DeleteSLARuleMutation, graphql_name='deleteSlaRule', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('preview', sgqlc.types.Arg(Boolean, graphql_name='preview', default=False)),
        ('rule_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='ruleId', default=None)),
))
    )
    add_preset = sgqlc.types.Field(AddPresetMutation, graphql_name='addPreset', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(JSONString, graphql_name='data', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('preset_type', sgqlc.types.Arg(Int, graphql_name='presetType', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    update_presets = sgqlc.types.Field('UpdatePresetsMutation', graphql_name='updatePresets', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(JSONString, graphql_name='data', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('preset_id', sgqlc.types.Arg(Int, graphql_name='presetId', default=None)),
        ('preset_type', sgqlc.types.Arg(Int, graphql_name='presetType', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    delete_presets = sgqlc.types.Field(DeletePresetsMutation, graphql_name='deletePresets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    update_data_retention_setting = sgqlc.types.Field('UpdateDataRetentionSettingMutation', graphql_name='updateDataRetentionSetting', args=sgqlc.types.ArgDict((
        ('data_retention_setting', sgqlc.types.Arg(JSONString, graphql_name='dataRetentionSetting', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_asm_settings = sgqlc.types.Field('UpdateASMSettingsMutations', graphql_name='updateAsmSettings', args=sgqlc.types.ArgDict((
        ('is_enabled', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isEnabled', default=None)),
        ('is_finding_scanning_enabled', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isFindingScanningEnabled', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('out_of_scope', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='outOfScope', default=None)),
        ('scheduled_at', sgqlc.types.Arg(String, graphql_name='scheduledAt', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='scope', default=None)),
))
    )
    bulk_update_credential_manager = sgqlc.types.Field(BulkUpdateCredentialManager, graphql_name='bulkUpdateCredentialManager', args=sgqlc.types.ArgDict((
        ('new_credential_manager_id', sgqlc.types.Arg(Int, graphql_name='newCredentialManagerId', default=None)),
        ('old_credential_manager_id', sgqlc.types.Arg(Int, graphql_name='oldCredentialManagerId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    update_credential_manager_state = sgqlc.types.Field('UpdateCredentialManagerState', graphql_name='updateCredentialManagerState', args=sgqlc.types.ArgDict((
        ('credential_manager_id_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='credentialManagerIdList', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    vaults = sgqlc.types.Field(sgqlc.types.list_of('VaultType'), graphql_name='vaults')
    add_vault_attachment = sgqlc.types.Field(AddVaultAttachmentMutation, graphql_name='addVaultAttachment', args=sgqlc.types.ArgDict((
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('prerequisite', sgqlc.types.Arg(Boolean, graphql_name='prerequisite', default=None)),
))
    )
    bulk_delete_vault_mutation = sgqlc.types.Field(BulkDeleteVaultMutation, graphql_name='bulkDeleteVaultMutation', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('vault_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='vaultIds', default=None)),
))
    )
    add_widget = sgqlc.types.Field(CreateWidgetMutation, graphql_name='addWidget', args=sgqlc.types.ArgDict((
        ('aggregate_field', sgqlc.types.Arg(String, graphql_name='aggregateField', default=None)),
        ('annotated_fields', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='annotatedFields', default=None)),
        ('assessment_search_query', sgqlc.types.Arg(String, graphql_name='assessmentSearchQuery', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('chart_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='chartType', default=None)),
        ('connector_search_query', sgqlc.types.Arg(String, graphql_name='connectorSearchQuery', default=None)),
        ('custom_fields', sgqlc.types.Arg(GenericScalar, graphql_name='customFields', default=None)),
        ('datetime_filter', sgqlc.types.Arg(Int, graphql_name='datetimeFilter', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fields', default=None)),
        ('filter_field_name', sgqlc.types.Arg(String, graphql_name='filterFieldName', default=None)),
        ('function', sgqlc.types.Arg(String, graphql_name='function', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('module', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='module', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('organization_search_query', sgqlc.types.Arg(String, graphql_name='organizationSearchQuery', default=None)),
        ('pivot_by_field', sgqlc.types.Arg(String, graphql_name='pivotByField', default=None)),
        ('positional_data', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='positionalData', default=None)),
        ('prefix', sgqlc.types.Arg(String, graphql_name='prefix', default=None)),
        ('scan_log_search_query', sgqlc.types.Arg(String, graphql_name='scanLogSearchQuery', default=None)),
        ('suffix', sgqlc.types.Arg(String, graphql_name='suffix', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('teams_search_query', sgqlc.types.Arg(String, graphql_name='teamsSearchQuery', default=None)),
        ('time_group', sgqlc.types.Arg(String, graphql_name='timeGroup', default=None)),
        ('timeseries_field', sgqlc.types.Arg(String, graphql_name='timeseriesField', default=None)),
        ('tracker_search_query', sgqlc.types.Arg(String, graphql_name='trackerSearchQuery', default=None)),
        ('widget_params', sgqlc.types.Arg(GenericScalar, graphql_name='widgetParams', default=None)),
))
    )
    update_widgets = sgqlc.types.Field('UpdateWidgetMutation', graphql_name='updateWidgets', args=sgqlc.types.ArgDict((
        ('aggregate_field', sgqlc.types.Arg(String, graphql_name='aggregateField', default=None)),
        ('annotated_fields', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='annotatedFields', default=None)),
        ('assessment_search_query', sgqlc.types.Arg(String, graphql_name='assessmentSearchQuery', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('connector_search_query', sgqlc.types.Arg(String, graphql_name='connectorSearchQuery', default=None)),
        ('custom_fields', sgqlc.types.Arg(GenericScalar, graphql_name='customFields', default=None)),
        ('datetime_filter', sgqlc.types.Arg(Int, graphql_name='datetimeFilter', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fields', default=None)),
        ('filter_field_name', sgqlc.types.Arg(String, graphql_name='filterFieldName', default=None)),
        ('function', sgqlc.types.Arg(String, graphql_name='function', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('organization_search_query', sgqlc.types.Arg(String, graphql_name='organizationSearchQuery', default=None)),
        ('pivot_by_field', sgqlc.types.Arg(String, graphql_name='pivotByField', default=None)),
        ('positional_data', sgqlc.types.Arg(GenericScalar, graphql_name='positionalData', default=None)),
        ('prefix', sgqlc.types.Arg(String, graphql_name='prefix', default=None)),
        ('scan_log_search_query', sgqlc.types.Arg(String, graphql_name='scanLogSearchQuery', default=None)),
        ('suffix', sgqlc.types.Arg(String, graphql_name='suffix', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('teams_search_query', sgqlc.types.Arg(String, graphql_name='teamsSearchQuery', default=None)),
        ('time_group', sgqlc.types.Arg(String, graphql_name='timeGroup', default=None)),
        ('timeseries_field', sgqlc.types.Arg(String, graphql_name='timeseriesField', default=None)),
        ('tracker_search_query', sgqlc.types.Arg(String, graphql_name='trackerSearchQuery', default=None)),
        ('widget_params', sgqlc.types.Arg(GenericScalar, graphql_name='widgetParams', default=None)),
))
    )
    delete_widgets = sgqlc.types.Field(DeleteWidgetMutation, graphql_name='deleteWidgets', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    clone_widget = sgqlc.types.Field(CloneDefaultWidgetMutation, graphql_name='cloneWidget', args=sgqlc.types.ArgDict((
        ('annotated_fields', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='annotatedFields', default=None)),
        ('assessment_search_query', sgqlc.types.Arg(String, graphql_name='assessmentSearchQuery', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('connector_search_query', sgqlc.types.Arg(String, graphql_name='connectorSearchQuery', default=None)),
        ('datetime_filter', sgqlc.types.Arg(Int, graphql_name='datetimeFilter', default=None)),
        ('default_widget_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='defaultWidgetId', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('organization_search_query', sgqlc.types.Arg(String, graphql_name='organizationSearchQuery', default=None)),
        ('positional_data', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='positionalData', default=None)),
        ('prefix', sgqlc.types.Arg(String, graphql_name='prefix', default=None)),
        ('scan_log_search_query', sgqlc.types.Arg(String, graphql_name='scanLogSearchQuery', default=None)),
        ('suffix', sgqlc.types.Arg(String, graphql_name='suffix', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('teams_search_query', sgqlc.types.Arg(String, graphql_name='teamsSearchQuery', default=None)),
        ('time_group', sgqlc.types.Arg(String, graphql_name='timeGroup', default=None)),
        ('timeseries_field', sgqlc.types.Arg(String, graphql_name='timeseriesField', default=None)),
        ('tracker_search_query', sgqlc.types.Arg(String, graphql_name='trackerSearchQuery', default=None)),
        ('widget_params', sgqlc.types.Arg(GenericScalar, graphql_name='widgetParams', default=None)),
))
    )
    add_dashboard = sgqlc.types.Field(CreateDashboardMutation, graphql_name='addDashboard', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='data', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('is_default', sgqlc.types.Arg(Boolean, graphql_name='isDefault', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('positional_data', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='positionalData', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('widgets', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='widgets', default=None)),
))
    )
    update_dashboard = sgqlc.types.Field('UpdateDashboardMutation', graphql_name='updateDashboard', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='data', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('is_default', sgqlc.types.Arg(Boolean, graphql_name='isDefault', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('positional_data', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='positionalData', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('widgets', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='widgets', default=None)),
))
    )
    delete_dashboard = sgqlc.types.Field(DeleteDashboardMutation, graphql_name='deleteDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    export_dashboard = sgqlc.types.Field(DashboardExportMutation, graphql_name='exportDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    import_dashboard = sgqlc.types.Field(DashboardImportMutation, graphql_name='importDashboard', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    comment_update = sgqlc.types.Field('UpdateCommentMutation', graphql_name='commentUpdate', args=sgqlc.types.ArgDict((
        ('add_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='addAttachments', default=None)),
        ('bug_id', sgqlc.types.Arg(Int, graphql_name='bugId', default=None)),
        ('comment', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='comment', default=None)),
        ('comment_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='commentId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('remove_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='removeAttachments', default=None)),
))
    )
    comment_delete = sgqlc.types.Field(DeleteCommentMutation, graphql_name='commentDelete', args=sgqlc.types.ArgDict((
        ('bug_id', sgqlc.types.Arg(Int, graphql_name='bugId', default=None)),
        ('comment_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='commentId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    assessment = sgqlc.types.Field(sgqlc.types.list_of(AssessmentType), graphql_name='assessment')
    bulk_update_prerequisites = sgqlc.types.Field(BulkUpdatePreRequisitesMutation, graphql_name='bulkUpdatePrerequisites', args=sgqlc.types.ArgDict((
        ('engagement_id', sgqlc.types.Arg(String, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('prerequisites_data', sgqlc.types.Arg(JSONString, graphql_name='prerequisitesData', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    bulk_delete_prerequisites = sgqlc.types.Field(BulkDeletePrerequisitesMutation, graphql_name='bulkDeletePrerequisites', args=sgqlc.types.ArgDict((
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    update_assessments = sgqlc.types.Field('UpdateAssessmentMutation', graphql_name='updateAssessments', args=sgqlc.types.ArgDict((
        ('assessment_category', sgqlc.types.Arg(Int, graphql_name='assessmentCategory', default=None)),
        ('assessment_id', sgqlc.types.Arg(Int, graphql_name='assessmentId', default=None)),
        ('assigned_to', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assignedTo', default=None)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('comment_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='commentAttachments', default=None)),
        ('custom_assessment_status_id', sgqlc.types.Arg(Int, graphql_name='customAssessmentStatusId', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('instructions', sgqlc.types.Arg(String, graphql_name='instructions', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('test_accounts', sgqlc.types.Arg(String, graphql_name='testAccounts', default=None)),
        ('total_hours_spent', sgqlc.types.Arg(Int, graphql_name='totalHoursSpent', default=None)),
        ('vpn_accounts', sgqlc.types.Arg(String, graphql_name='vpnAccounts', default=None)),
))
    )
    bulk_update_assessment = sgqlc.types.Field(BulkUpdateAssessmentMutation, graphql_name='bulkUpdateAssessment', args=sgqlc.types.ArgDict((
        ('assessment_timelines', sgqlc.types.Arg(JSONString, graphql_name='assessmentTimelines', default=None)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('comment_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='commentAttachments', default=None)),
        ('custom_assessment_status_id', sgqlc.types.Arg(Int, graphql_name='customAssessmentStatusId', default=None)),
        ('delete_custom_status_field_id', sgqlc.types.Arg(Int, graphql_name='deleteCustomStatusFieldId', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('total_hours_spent', sgqlc.types.Arg(Int, graphql_name='totalHoursSpent', default=None)),
))
    )
    create_custom_assessment_status = sgqlc.types.Field(CreateCustomAssessmentStatusMutation, graphql_name='createCustomAssessmentStatus', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('parent_state', sgqlc.types.Arg(Int, graphql_name='parentState', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='status', default=None)),
))
    )
    update_custom_assessment_status = sgqlc.types.Field('UpdateCustomAssessmentStatusMutation', graphql_name='updateCustomAssessmentStatus', args=sgqlc.types.ArgDict((
        ('assessment_update_custom_status_id', sgqlc.types.Arg(Int, graphql_name='assessmentUpdateCustomStatusId', default=None)),
        ('assessment_update_status', sgqlc.types.Arg(Int, graphql_name='assessmentUpdateStatus', default=None)),
        ('custom_assessment_status_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='customAssessmentStatusId', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('is_update_assessment_status', sgqlc.types.Arg(Boolean, graphql_name='isUpdateAssessmentStatus', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('parent_state', sgqlc.types.Arg(Int, graphql_name='parentState', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='status', default=None)),
))
    )
    delete_custom_assessment_status = sgqlc.types.Field(DeleteCustomAssessmentStatusMutation, graphql_name='deleteCustomAssessmentStatus', args=sgqlc.types.ArgDict((
        ('custom_assessment_status_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='customAssessmentStatusId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_engagement = sgqlc.types.Field('UpdateEngagementMutation', graphql_name='updateEngagement', args=sgqlc.types.ArgDict((
        ('add_document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='addDocumentIds', default=None)),
        ('apply_assignees_to_assessments', sgqlc.types.Arg(Boolean, graphql_name='applyAssigneesToAssessments', default=False)),
        ('apply_state_to_assessments', sgqlc.types.Arg(Boolean, graphql_name='applyStateToAssessments', default=False)),
        ('assessment_data', sgqlc.types.Arg(JSONString, graphql_name='assessmentData', default=None)),
        ('assignees', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assignees', default=None)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('comment_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='commentAttachments', default=None)),
        ('custom_status', sgqlc.types.Arg(Int, graphql_name='customStatus', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('executive_summary', sgqlc.types.Arg(String, graphql_name='executiveSummary', default=None)),
        ('fields', sgqlc.types.Arg(JSONString, graphql_name='fields', default=None)),
        ('include_related_assets', sgqlc.types.Arg(Boolean, graphql_name='includeRelatedAssets', default=False)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('plans', sgqlc.types.Arg(Int, graphql_name='plans', default=None)),
        ('prerequisites_data', sgqlc.types.Arg(JSONString, graphql_name='prerequisitesData', default=None)),
        ('remove_document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='removeDocumentIds', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('service', sgqlc.types.Arg(String, graphql_name='service', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('subscribed_services', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='subscribedServices', default=None)),
))
    )
    add_attachment = sgqlc.types.Field(AddAttachmentMutation, graphql_name='addAttachment', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bulk_update_engagements = sgqlc.types.Field(BulkUpdateEngagementsMutation, graphql_name='bulkUpdateEngagements', args=sgqlc.types.ArgDict((
        ('apply_state_to_assessments', sgqlc.types.Arg(Boolean, graphql_name='applyStateToAssessments', default=False)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('comment_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='commentAttachments', default=None)),
        ('custom_status', sgqlc.types.Arg(Int, graphql_name='customStatus', default=None)),
        ('engagement_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='engagementIds', default=None)),
        ('fields', sgqlc.types.Arg(JSONString, graphql_name='fields', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
))
    )
    archive_engagements = sgqlc.types.Field(BulkArchiveEngagementsMutation, graphql_name='archiveEngagements', args=sgqlc.types.ArgDict((
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    create_engagement = sgqlc.types.Field(CreateEngagementMutation, graphql_name='createEngagement', args=sgqlc.types.ArgDict((
        ('assessment_data', sgqlc.types.Arg(JSONString, graphql_name='assessmentData', default=None)),
        ('custom_status', sgqlc.types.Arg(Int, graphql_name='customStatus', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='documentIds', default=None)),
        ('executive_summary', sgqlc.types.Arg(String, graphql_name='executiveSummary', default=None)),
        ('fields', sgqlc.types.Arg(JSONString, graphql_name='fields', default=None)),
        ('include_related_assets', sgqlc.types.Arg(Boolean, graphql_name='includeRelatedAssets', default=False)),
        ('is_self_managed', sgqlc.types.Arg(Boolean, graphql_name='isSelfManaged', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('plans', sgqlc.types.Arg(Int, graphql_name='plans', default=None)),
        ('prerequisites_data', sgqlc.types.Arg(JSONString, graphql_name='prerequisitesData', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('subscribed_services', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='subscribedServices', default=None)),
        ('vendor_code', sgqlc.types.Arg(String, graphql_name='vendorCode', default=None)),
))
    )
    export_engagements = sgqlc.types.Field(ExportEngagementsMutation, graphql_name='exportEngagements', args=sgqlc.types.ArgDict((
        ('assessment_search_query', sgqlc.types.Arg(String, graphql_name='assessmentSearchQuery', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('engagement_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='engagementIds', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('export_report_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='exportReportType', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('selected_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='selectedFields', default=None)),
))
    )
    add_engagements_field_settings_mutation = sgqlc.types.Field(AddEngagementsFieldSettingsMutation, graphql_name='addEngagementsFieldSettingsMutation', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('field_type', sgqlc.types.Arg(Int, graphql_name='fieldType', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    delete_engagement_field_settings_mutation = sgqlc.types.Field(DeleteEngagementFieldSettingsMutation, graphql_name='deleteEngagementFieldSettingsMutation', args=sgqlc.types.ArgDict((
        ('engagement_field_id', sgqlc.types.Arg(Int, graphql_name='engagementFieldId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    update_engagement_field_settings_mutation = sgqlc.types.Field('UpdateEngagementFieldSettingsMutation', graphql_name='updateEngagementFieldSettingsMutation', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('engagement_field_id', sgqlc.types.Arg(Int, graphql_name='engagementFieldId', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('new_selected_option', sgqlc.types.Arg(String, graphql_name='newSelectedOption', default=None)),
        ('old_selected_option', sgqlc.types.Arg(String, graphql_name='oldSelectedOption', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    assign_asset_view_to_users = sgqlc.types.Field(AssignAssetViewToUsersMutation, graphql_name='assignAssetViewToUsers', args=sgqlc.types.ArgDict((
        ('assign_bugs', sgqlc.types.Arg(String, graphql_name='assignBugs', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
))
    )
    add_report_attachment = sgqlc.types.Field(AddReportAttachmentMutation, graphql_name='addReportAttachment', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bulk_delete_attachment = sgqlc.types.Field(DestroyBulkReportAttachmentMutation, graphql_name='bulkDeleteAttachment', args=sgqlc.types.ArgDict((
        ('attachment_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='attachmentIds', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    restore_default_prioritization_rule = sgqlc.types.Field('RestoreDefaultPriortizationRuleMutation', graphql_name='restoreDefaultPrioritizationRule', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    update_prioritization_settings = sgqlc.types.Field('UpdatePrioritizationSettings', graphql_name='updatePrioritizationSettings', args=sgqlc.types.ArgDict((
        ('fallback_score', sgqlc.types.Arg(Int, graphql_name='fallbackScore', default=None)),
        ('method', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='method', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    create_priority_rule_set = sgqlc.types.Field(CreatePriorityRuleSet, graphql_name='createPriorityRuleSet', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('filter_query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filterQuery', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('stop_processing_on_match', sgqlc.types.Arg(Boolean, graphql_name='stopProcessingOnMatch', default=None)),
        ('weight', sgqlc.types.Arg(Int, graphql_name='weight', default=None)),
))
    )
    update_priority_rule_set = sgqlc.types.Field('UpdatePriorityRuleSet', graphql_name='updatePriorityRuleSet', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('filter_query', sgqlc.types.Arg(String, graphql_name='filterQuery', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('stop_processing_on_match', sgqlc.types.Arg(Boolean, graphql_name='stopProcessingOnMatch', default=None)),
        ('weight', sgqlc.types.Arg(Int, graphql_name='weight', default=None)),
))
    )
    delete_priority_rule_set = sgqlc.types.Field(DeletePriorityRuleSet, graphql_name='deletePriorityRuleSet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_priority_rule = sgqlc.types.Field(CreatePriorityRule, graphql_name='createPriorityRule', args=sgqlc.types.ArgDict((
        ('action', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='action', default=None)),
        ('condition_query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='conditionQuery', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('rule_set_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='ruleSetId', default=None)),
        ('score_value', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='scoreValue', default=None)),
))
    )
    update_priority_rule = sgqlc.types.Field('UpdatePriorityRule', graphql_name='updatePriorityRule', args=sgqlc.types.ArgDict((
        ('action', sgqlc.types.Arg(Int, graphql_name='action', default=None)),
        ('condition_query', sgqlc.types.Arg(String, graphql_name='conditionQuery', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('score_value', sgqlc.types.Arg(Int, graphql_name='scoreValue', default=None)),
))
    )
    delete_priority_rule = sgqlc.types.Field(DeletePriorityRule, graphql_name='deletePriorityRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    report_bulk_delete = sgqlc.types.Field(DestroyBulkReportMutation, graphql_name='reportBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('report_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='reportIds', default=None)),
))
    )
    generate_report = sgqlc.types.Field(GenerateReportMutation, graphql_name='generateReport', args=sgqlc.types.ArgDict((
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('custom_data', sgqlc.types.Arg(JSONString, graphql_name='customData', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('report_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reportName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='templateId', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
))
    )
    update_report = sgqlc.types.Field('UpdateReportMutation', graphql_name='updateReport', args=sgqlc.types.ArgDict((
        ('export_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='exportId', default=None)),
        ('html_content', sgqlc.types.Arg(String, graphql_name='htmlContent', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    show_report_password = sgqlc.types.Field('ShowReportPasswordMutation', graphql_name='showReportPassword', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='reportId', default=None)),
        ('user_password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userPassword', default=None)),
))
    )
    set_report_password = sgqlc.types.Field('SetReportPasswordMutation', graphql_name='setReportPassword', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='reportId', default=None)),
        ('user_password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userPassword', default=None)),
))
    )
    delete_report_template = sgqlc.types.Field(BulkDeleteTemplateMutation, graphql_name='deleteReportTemplate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('template_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='templateIds', default=None)),
))
    )
    add_report_template = sgqlc.types.Field(AddTemplateMutation, graphql_name='addReportTemplate', args=sgqlc.types.ArgDict((
        ('footer_template', sgqlc.types.Arg(String, graphql_name='footerTemplate', default=None)),
        ('header_template', sgqlc.types.Arg(String, graphql_name='headerTemplate', default=None)),
        ('html_data', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='htmlData', default=None)),
        ('mode', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mode', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='templateName', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='type', default=None)),
))
    )
    update_report_template = sgqlc.types.Field('UpdateTemplateMutation', graphql_name='updateReportTemplate', args=sgqlc.types.ArgDict((
        ('branch', sgqlc.types.Arg(String, graphql_name='branch', default=None)),
        ('file_path', sgqlc.types.Arg(String, graphql_name='filePath', default=None)),
        ('footer_template', sgqlc.types.Arg(String, graphql_name='footerTemplate', default=None)),
        ('header_template', sgqlc.types.Arg(String, graphql_name='headerTemplate', default=None)),
        ('html_data', sgqlc.types.Arg(String, graphql_name='htmlData', default=None)),
        ('is_replace_with_github_template', sgqlc.types.Arg(Boolean, graphql_name='isReplaceWithGithubTemplate', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='templateId', default=None)),
        ('template_name', sgqlc.types.Arg(String, graphql_name='templateName', default=None)),
))
    )
    create_github_report_template = sgqlc.types.Field(CreateGithubReportTemplateMutation, graphql_name='createGithubReportTemplate', args=sgqlc.types.ArgDict((
        ('branch', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='branch', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='templateName', default=None)),
))
    )
    add_group = sgqlc.types.Field(AddGroupMutation, graphql_name='addGroup', args=sgqlc.types.ArgDict((
        ('asset_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assetIds', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    update_group = sgqlc.types.Field('UpdateGroupMutation', graphql_name='updateGroup', args=sgqlc.types.ArgDict((
        ('asset_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assetIds', default=None)),
        ('group_id', sgqlc.types.Arg(Int, graphql_name='groupId', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    group_bulk_delete = sgqlc.types.Field(BulkDeleteGroupMutation, graphql_name='groupBulkDelete', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    org_member_role_bulk_update = sgqlc.types.Field(BulkUpdateOrgMemberRoleMutation, graphql_name='orgMemberRoleBulkUpdate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(Int, graphql_name='role', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    team_member_role_bulk_update = sgqlc.types.Field(BulkUpdateTeamMemberRoleMutation, graphql_name='teamMemberRoleBulkUpdate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='role', default=None)),
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='teamId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    org_member_role_bulk_delete = sgqlc.types.Field(BulkDeleteOrgMemberRoleMutation, graphql_name='orgMemberRoleBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    team_member_role_bulk_delete = sgqlc.types.Field(BulkDeleteTeamMemberRoleMutation, graphql_name='teamMemberRoleBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('team_id', sgqlc.types.Arg(Int, graphql_name='teamId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    bulk_update_member_asset_access = sgqlc.types.Field(BulkUpdateMemberAssetAccessMutation, graphql_name='bulkUpdateMemberAssetAccess', args=sgqlc.types.ArgDict((
        ('add_users_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='addUsersList', default=None)),
        ('asset_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assetIds', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('remove_users_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='removeUsersList', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    bug_bulk_update = sgqlc.types.Field(BulkUpdateBugMutation, graphql_name='bugBulkUpdate', args=sgqlc.types.ArgDict((
        ('attack_vector', sgqlc.types.Arg(String, graphql_name='attackVector', default=None)),
        ('cvss', sgqlc.types.Arg(Float, graphql_name='cvss', default=None)),
        ('due_date', sgqlc.types.Arg(Date, graphql_name='dueDate', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('severity', sgqlc.types.Arg(Int, graphql_name='severity', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
))
    )
    bug_bulk_assignment = sgqlc.types.Field(BulkBugAssignmentMutation, graphql_name='bugBulkAssignment', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    bug_bulk_unassignment = sgqlc.types.Field(BulkBugUnAssignmentMutation, graphql_name='bugBulkUnassignment', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    bug_bulk_update_tags = sgqlc.types.Field(BulkUpdateBugTagMutation, graphql_name='bugBulkUpdateTags', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    bug_bulk_update_cve = sgqlc.types.Field(BulkUpdateBugCVEMutation, graphql_name='bugBulkUpdateCve', args=sgqlc.types.ArgDict((
        ('clear_existing', sgqlc.types.Arg(Boolean, graphql_name='clearExisting', default=False)),
        ('cves', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='cves', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    bug_bulk_update_cwe = sgqlc.types.Field(BulkUpdateBugCWEMutation, graphql_name='bugBulkUpdateCwe', args=sgqlc.types.ArgDict((
        ('clear_existing', sgqlc.types.Arg(Boolean, graphql_name='clearExisting', default=False)),
        ('cwes', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='cwes', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    bug_bulk_delete = sgqlc.types.Field(BulkDeleteBugMutation, graphql_name='bugBulkDelete', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('is_archived_view', sgqlc.types.Arg(Boolean, graphql_name='isArchivedView', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    add_bulk_comment = sgqlc.types.Field(AddBulkCommentsMutation, graphql_name='addBulkComment', args=sgqlc.types.ArgDict((
        ('attachment_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='attachmentList', default=None)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('internal', sgqlc.types.Arg(Boolean, graphql_name='internal', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    bug_bulk_add_to_tracker = sgqlc.types.Field(BulkAddToTrackerMutation, graphql_name='bugBulkAddToTracker', args=sgqlc.types.ArgDict((
        ('assignees_list', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='assigneesList', default=None)),
        ('configuration_id', sgqlc.types.Arg(Int, graphql_name='configurationId', default=None)),
        ('create_grouped_issues', sgqlc.types.Arg(Boolean, graphql_name='createGroupedIssues', default=None)),
        ('custom_title', sgqlc.types.Arg(String, graphql_name='customTitle', default=None)),
        ('issue_groupby', sgqlc.types.Arg(String, graphql_name='issueGroupby', default=None)),
        ('labels_list', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labelsList', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('overwrite_existing_issues', sgqlc.types.Arg(Boolean, graphql_name='overwriteExistingIssues', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('severity', sgqlc.types.Arg(Int, graphql_name='severity', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('tracker_slug', sgqlc.types.Arg(String, graphql_name='trackerSlug', default=None)),
))
    )
    approve_state_change = sgqlc.types.Field(ApproveStateChangeMutation, graphql_name='approveStateChange', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('is_approved', sgqlc.types.Arg(Boolean, graphql_name='isApproved', default=None)),
        ('is_declined', sgqlc.types.Arg(Boolean, graphql_name='isDeclined', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    deduplicate_bug_preview = sgqlc.types.Field(DeduplicateBugPreviewMutation, graphql_name='deduplicateBugPreview', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('strategy', sgqlc.types.Arg(Int, graphql_name='strategy', default=None)),
))
    )
    deduplicate_bug_confirm = sgqlc.types.Field(DeduplicateBugConfirmMutation, graphql_name='deduplicateBugConfirm', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('strategy', sgqlc.types.Arg(Int, graphql_name='strategy', default=None)),
))
    )
    calculate_priority_score = sgqlc.types.Field(CalculatePrioritizationScoreMutation, graphql_name='calculatePriorityScore', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    transfer_engagement_bugs = sgqlc.types.Field('TransferEngagementBugMutation', graphql_name='transferEngagementBugs', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('transfer_engagement_id', sgqlc.types.Arg(UUID, graphql_name='transferEngagementId', default=None)),
))
    )
    bug_update_risk_records = sgqlc.types.Field('UpdateRiskRecordsMutation', graphql_name='bugUpdateRiskRecords', args=sgqlc.types.ArgDict((
        ('bug_id', sgqlc.types.Arg(Int, graphql_name='bugId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('records_at_risk', sgqlc.types.Arg(Int, graphql_name='recordsAtRisk', default=None)),
        ('records_type', sgqlc.types.Arg(Int, graphql_name='recordsType', default=None)),
))
    )
    add_bug_settings_fields = sgqlc.types.Field(AddBugFieldSettingsMutation, graphql_name='addBugSettingsFields', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('field_type', sgqlc.types.Arg(Int, graphql_name='fieldType', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    update_bug_settings_fields = sgqlc.types.Field('UpdateBugFieldSettingsMutation', graphql_name='updateBugSettingsFields', args=sgqlc.types.ArgDict((
        ('bug_field_id', sgqlc.types.Arg(Int, graphql_name='bugFieldId', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('new_selected_option', sgqlc.types.Arg(String, graphql_name='newSelectedOption', default=None)),
        ('old_selected_option', sgqlc.types.Arg(String, graphql_name='oldSelectedOption', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    delete_bug_settings_fields = sgqlc.types.Field(DeleteBugFieldSettingsMutation, graphql_name='deleteBugSettingsFields', args=sgqlc.types.ArgDict((
        ('bug_field_id', sgqlc.types.Arg(Int, graphql_name='bugFieldId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    bug_bulk_update_title = sgqlc.types.Field(BulkUpdateBugTitleMutation, graphql_name='bugBulkUpdateTitle', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
))
    )
    bug_bulk_update_mitigation_description = sgqlc.types.Field(BulkUpdateBugMitigationMutation, graphql_name='bugBulkUpdateMitigationDescription', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('evidence', sgqlc.types.Arg(String, graphql_name='evidence', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('mitigation', sgqlc.types.Arg(String, graphql_name='mitigation', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('steps_to_reproduce', sgqlc.types.Arg(String, graphql_name='stepsToReproduce', default=None)),
))
    )
    archive_bug_bulk_update = sgqlc.types.Field(BulkUpdateArchiveBugsMutation, graphql_name='archiveBugBulkUpdate', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    bug_bulk_update_custom_fields = sgqlc.types.Field(BulkUpdateBugCustomFieldMutation, graphql_name='bugBulkUpdateCustomFields', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(GenericScalar, graphql_name='fields', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    update_bugs_fields_with_csv = sgqlc.types.Field(BulkUpdateBugsFieldsWithCSVMutation, graphql_name='updateBugsFieldsWithCsv', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bug_create = sgqlc.types.Field(CreateBugMutation, graphql_name='bugCreate', args=sgqlc.types.ArgDict((
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('attack_vector', sgqlc.types.Arg(String, graphql_name='attackVector', default=None)),
        ('bug_attachment_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='bugAttachmentList', default=None)),
        ('bug_level', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='bugLevel', default=None)),
        ('cloud', sgqlc.types.Arg(JSONString, graphql_name='cloud', default=None)),
        ('cloud_asset_type', sgqlc.types.Arg(Int, graphql_name='cloudAssetType', default=None)),
        ('code', sgqlc.types.Arg(JSONString, graphql_name='code', default=None)),
        ('config_id', sgqlc.types.Arg(Int, graphql_name='configId', default=None)),
        ('custom_fields', sgqlc.types.Arg(JSONString, graphql_name='customFields', default=None)),
        ('cve_list', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='cveList', default=None)),
        ('cvss', sgqlc.types.Arg(Float, graphql_name='cvss', default=None)),
        ('cwe_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='cweList', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('engagement_id', sgqlc.types.Arg(String, graphql_name='engagementId', default=None)),
        ('engagement_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='engagementIds', default=None)),
        ('evidence', sgqlc.types.Arg(String, graphql_name='evidence', default=None)),
        ('mitigation', sgqlc.types.Arg(String, graphql_name='mitigation', default=None)),
        ('mobile', sgqlc.types.Arg(JSONString, graphql_name='mobile', default=None)),
        ('network', sgqlc.types.Arg(JSONString, graphql_name='network', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('package', sgqlc.types.Arg(JSONString, graphql_name='package', default=None)),
        ('select_all_assets', sgqlc.types.Arg(Boolean, graphql_name='selectAllAssets', default=None)),
        ('selected_asset', sgqlc.types.Arg(Int, graphql_name='selectedAsset', default=None)),
        ('selected_assets', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='selectedAssets', default=None)),
        ('selected_team', sgqlc.types.Arg(Int, graphql_name='selectedTeam', default=None)),
        ('severity', sgqlc.types.Arg(Int, graphql_name='severity', default=None)),
        ('steps_to_reproduce', sgqlc.types.Arg(String, graphql_name='stepsToReproduce', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('web', sgqlc.types.Arg(JSONString, graphql_name='web', default=None)),
))
    )
    sync_bug_with_trackers = sgqlc.types.Field('SyncBugWithTrackersMutation', graphql_name='syncBugWithTrackers', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    test_with_nuclie_template = sgqlc.types.Field('TestNuclieTemplateMutation', graphql_name='testWithNuclieTemplate', args=sgqlc.types.ArgDict((
        ('bug_id', sgqlc.types.Arg(Int, graphql_name='bugId', default=None)),
        ('nuclie_target', sgqlc.types.Arg(String, graphql_name='nuclieTarget', default=None)),
        ('nuclie_template', sgqlc.types.Arg(String, graphql_name='nuclieTemplate', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='organizationId', default=None)),
))
    )
    bulk_test_with_nuclie_template = sgqlc.types.Field(BulkTestWithNuclieMutation, graphql_name='bulkTestWithNuclieTemplate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    assets_bulk_update = sgqlc.types.Field(BulkUpdateAssetsMutation, graphql_name='assetsBulkUpdate', args=sgqlc.types.ArgDict((
        ('exposed', sgqlc.types.Arg(Int, graphql_name='exposed', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(String, graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('sensitivity', sgqlc.types.Arg(Int, graphql_name='sensitivity', default=None)),
))
    )
    assets_bulk_merge = sgqlc.types.Field(BulkMergeAssetsMutation, graphql_name='assetsBulkMerge', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('source_asset', sgqlc.types.Arg(Int, graphql_name='sourceAsset', default=None)),
))
    )
    assets_bulk_link = sgqlc.types.Field(BulkLinkAssetsMutation, graphql_name='assetsBulkLink', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('source_asset', sgqlc.types.Arg(Int, graphql_name='sourceAsset', default=None)),
))
    )
    assets_bulk_delete = sgqlc.types.Field(BulkDeleteAssetsMutation, graphql_name='assetsBulkDelete', args=sgqlc.types.ArgDict((
        ('is_archived_view', sgqlc.types.Arg(Boolean, graphql_name='isArchivedView', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    assets_bulk_update_tags = sgqlc.types.Field(BulkUpdateAssetsTagMutation, graphql_name='assetsBulkUpdateTags', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    archive_assets_bulk_update = sgqlc.types.Field(BulkUpdateArchiveAssetsMutation, graphql_name='archiveAssetsBulkUpdate', args=sgqlc.types.ArgDict((
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    assets_merge_preview = sgqlc.types.Field(BulkMergeAssetsPreviewMutation, graphql_name='assetsMergePreview', args=sgqlc.types.ArgDict((
        ('host_name', sgqlc.types.Arg(Boolean, graphql_name='hostName', default=None)),
        ('ip_address', sgqlc.types.Arg(Boolean, graphql_name='ipAddress', default=None)),
        ('mac_address', sgqlc.types.Arg(Boolean, graphql_name='macAddress', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    assets_merge_confirm = sgqlc.types.Field(BulkMergeAssetsConfirmMutation, graphql_name='assetsMergeConfirm', args=sgqlc.types.ArgDict((
        ('host_name', sgqlc.types.Arg(Boolean, graphql_name='hostName', default=None)),
        ('ip_address', sgqlc.types.Arg(Boolean, graphql_name='ipAddress', default=None)),
        ('mac_address', sgqlc.types.Arg(Boolean, graphql_name='macAddress', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    calculate_risk_score = sgqlc.types.Field(CalculateRiskScoreMutation, graphql_name='calculateRiskScore', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    software_packages_bulk_update = sgqlc.types.Field(BulkUpdateSoftwarePackageMutation, graphql_name='softwarePackagesBulkUpdate', args=sgqlc.types.ArgDict((
        ('installed_version', sgqlc.types.Arg(String, graphql_name='installedVersion', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('package_name', sgqlc.types.Arg(String, graphql_name='packageName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    software_packages_bulk_delete = sgqlc.types.Field(BulkDeleteSoftwarePackageMutation, graphql_name='softwarePackagesBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    software_package_create = sgqlc.types.Field(CreateSoftwarePackageMutation, graphql_name='softwarePackageCreate', args=sgqlc.types.ArgDict((
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('installed_version', sgqlc.types.Arg(String, graphql_name='installedVersion', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('package_name', sgqlc.types.Arg(String, graphql_name='packageName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    add_asset_settings_fields = sgqlc.types.Field(AddAssetFieldSettingsMutation, graphql_name='addAssetSettingsFields', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('field_type', sgqlc.types.Arg(Int, graphql_name='fieldType', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    update_asset_settings_fields = sgqlc.types.Field('UpdateAssetFieldSettingsMutation', graphql_name='updateAssetSettingsFields', args=sgqlc.types.ArgDict((
        ('asset_field_id', sgqlc.types.Arg(Int, graphql_name='assetFieldId', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('new_selected_option', sgqlc.types.Arg(String, graphql_name='newSelectedOption', default=None)),
        ('old_selected_option', sgqlc.types.Arg(String, graphql_name='oldSelectedOption', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    delete_asset_settings_fields = sgqlc.types.Field(DeleteAssetFieldSettingsMutation, graphql_name='deleteAssetSettingsFields', args=sgqlc.types.ArgDict((
        ('asset_field_id', sgqlc.types.Arg(Int, graphql_name='assetFieldId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    bulk_update_asset_custom_field_mutation = sgqlc.types.Field(BulkUpdateAssetCustomFields, graphql_name='bulkUpdateAssetCustomFieldMutation', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(GenericScalar, graphql_name='fields', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    create_asset = sgqlc.types.Field(CreateAssetMutation, graphql_name='createAsset', args=sgqlc.types.ArgDict((
        ('cloud_type', sgqlc.types.Arg(Int, graphql_name='cloudType', default=None)),
        ('cpe', sgqlc.types.Arg(String, graphql_name='cpe', default=None)),
        ('custom_fields', sgqlc.types.Arg(GenericScalar, graphql_name='customFields', default=None)),
        ('excluded_ipaddress_list', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='excludedIpaddressList', default=None)),
        ('exposed', sgqlc.types.Arg(Int, graphql_name='exposed', default=None)),
        ('hostname', sgqlc.types.Arg(String, graphql_name='hostname', default=None)),
        ('ipaddress', sgqlc.types.Arg(String, graphql_name='ipaddress', default=None)),
        ('ipaddress_list', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ipaddressList', default=None)),
        ('mac_address', sgqlc.types.Arg(String, graphql_name='macAddress', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('os', sgqlc.types.Arg(String, graphql_name='os', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('sensitivity', sgqlc.types.Arg(Int, graphql_name='sensitivity', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('type', sgqlc.types.Arg(Int, graphql_name='type', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
))
    )
    update_asset_fields_with_csv = sgqlc.types.Field(BulkUpdateAssetFieldsWithCSVMutation, graphql_name='updateAssetFieldsWithCsv', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    bulk_asset_access_user_mutation = sgqlc.types.Field(BulkAssetAccessUserMutation, graphql_name='bulkAssetAccessUserMutation', args=sgqlc.types.ArgDict((
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    create_asset_relationship = sgqlc.types.Field(CreateAssetRelationship, graphql_name='createAssetRelationship', args=sgqlc.types.ArgDict((
        ('direction', sgqlc.types.Arg(sgqlc.types.non_null(GQLRelationshipDirectionEnum), graphql_name='direction', default=None)),
        ('metadata', sgqlc.types.Arg(GenericScalar, graphql_name='metadata', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('relationship_type', sgqlc.types.Arg(sgqlc.types.non_null(GQLRelationshipTypeEnum), graphql_name='relationshipType', default=None)),
        ('source_asset_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sourceAssetId', default=None)),
        ('target_asset_id', sgqlc.types.Arg(Int, graphql_name='targetAssetId', default=None)),
        ('target_asset_qs', sgqlc.types.Arg(String, graphql_name='targetAssetQs', default=None)),
))
    )
    update_asset_relationship = sgqlc.types.Field('UpdateAssetRelationship', graphql_name='updateAssetRelationship', args=sgqlc.types.ArgDict((
        ('direction', sgqlc.types.Arg(GQLRelationshipDirectionEnum, graphql_name='direction', default=None)),
        ('metadata', sgqlc.types.Arg(GenericScalar, graphql_name='metadata', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('relationship_id', sgqlc.types.Arg(Int, graphql_name='relationshipId', default=None)),
        ('relationship_query', sgqlc.types.Arg(String, graphql_name='relationshipQuery', default=None)),
        ('relationship_type', sgqlc.types.Arg(GQLRelationshipTypeEnum, graphql_name='relationshipType', default=None)),
))
    )
    delete_asset_relationship = sgqlc.types.Field(DeleteAssetRelationship, graphql_name='deleteAssetRelationship', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('relationship_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='relationshipId', default=None)),
))
    )


class MyFavoritesViewsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class NISTPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('NISTType'), graphql_name='objects')


class NISTType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'description', 'summary', 'nist_id', 'reference', 'revision', 'bug_nist')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    nist_id = sgqlc.types.Field(String, graphql_name='nistId')
    reference = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reference')
    revision = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='revision')
    bug_nist = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugNist')


class NetworkType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'port', 'os', 'cpe', 'batch_id', 'temp_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    port = sgqlc.types.Field('PortType', graphql_name='port')
    os = sgqlc.types.Field(String, graphql_name='os')
    cpe = sgqlc.types.Field(JSONString, graphql_name='cpe')
    batch_id = sgqlc.types.Field(UUID, graphql_name='batchId')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')


class OWASPPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('OWASPType'), graphql_name='objects')


class OWASPType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'year', 'label', 'bug_owasp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    year = sgqlc.types.Field(Int, graphql_name='year')
    label = sgqlc.types.Field(String, graphql_name='label')
    bug_owasp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugOwasp')


class OrganizationMembersPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('OrganizationMembersType'), graphql_name='objects')


class OrganizationMembersType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'user', 'organization', 'role', 'asset_search_query', 'permitted_apps', 'permitted_modules', 'default_page', 'default_asset_view', 'default_finding_view', 'permitted_dashboards', 'my_favorites', 'preset_set', 'approval_approved_by', 'approval_raised_by', 'assets', 'engagements', 'is_active', 'invitation_link', 'profile_picture_url', 'last_login', 'email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    role = sgqlc.types.Field(Int, graphql_name='role')
    asset_search_query = sgqlc.types.Field(String, graphql_name='assetSearchQuery')
    permitted_apps = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='permittedApps')
    permitted_modules = sgqlc.types.Field(GenericScalar, graphql_name='permittedModules')
    default_page = sgqlc.types.Field(GenericScalar, graphql_name='defaultPage')
    default_asset_view = sgqlc.types.Field(GenericScalar, graphql_name='defaultAssetView')
    default_finding_view = sgqlc.types.Field(GenericScalar, graphql_name='defaultFindingView')
    permitted_dashboards = sgqlc.types.Field(GenericScalar, graphql_name='permittedDashboards')
    my_favorites = sgqlc.types.Field(JSONString, graphql_name='myFavorites')
    preset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PresetType'))), graphql_name='presetSet')
    approval_approved_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalApprovedBy')
    approval_raised_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalRaisedBy')
    assets = sgqlc.types.Field(Int, graphql_name='assets')
    engagements = sgqlc.types.Field(Int, graphql_name='engagements')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    invitation_link = sgqlc.types.Field(String, graphql_name='invitationLink')
    profile_picture_url = sgqlc.types.Field(String, graphql_name='profilePictureUrl')
    last_login = sgqlc.types.Field(DateTime, graphql_name='lastLogin')
    email = sgqlc.types.Field(String, graphql_name='email')


class PackageAssetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('PackageAssetType'), graphql_name='objects')


class PackageAssetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'package_name', 'installed_version', 'file_name', 'ecosystem', 'asset', 'organization', 'created', 'updated', 'asset_count')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    package_name = sgqlc.types.Field(String, graphql_name='packageName')
    installed_version = sgqlc.types.Field(String, graphql_name='installedVersion')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')
    ecosystem = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ecosystem')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    asset_count = sgqlc.types.Field(Int, graphql_name='assetCount')


class PackagePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('PackageType'), graphql_name='objects')


class PackageType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'package_name', 'affected_versions', 'installed_version', 'fixed_version', 'digest', 'commit', 'file_name', 'ecosystem', 'branch', 'batch_id', 'temp_id', 'releases')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    package_name = sgqlc.types.Field(String, graphql_name='packageName')
    affected_versions = sgqlc.types.Field(JSONString, graphql_name='affectedVersions')
    installed_version = sgqlc.types.Field(String, graphql_name='installedVersion')
    fixed_version = sgqlc.types.Field(String, graphql_name='fixedVersion')
    digest = sgqlc.types.Field(String, graphql_name='digest')
    commit = sgqlc.types.Field(String, graphql_name='commit')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')
    ecosystem = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ecosystem')
    branch = sgqlc.types.Field(JSONString, graphql_name='branch')
    batch_id = sgqlc.types.Field(UUID, graphql_name='batchId')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')
    releases = sgqlc.types.Field(JSONString, graphql_name='releases')


class ParticipantSummaryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('agent_id', 'agent_name', 'role')
    agent_id = sgqlc.types.Field(String, graphql_name='agentId')
    agent_name = sgqlc.types.Field(String, graphql_name='agentName')
    role = sgqlc.types.Field(String, graphql_name='role')


class PatchesPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('PatchesType'), graphql_name='objects')


class PatchesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'patch_type', 'package_name', 'highest_fixed_version', 'asset', 'extra_data', 'created', 'updated', 'bug_set', 'trackers_set', 'bug_count', 'asset_name', 'ticket_id', 'ticket_url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    patch_type = sgqlc.types.Field(sgqlc.types.non_null(AppPatchPatchTypeChoices), graphql_name='patchType')
    package_name = sgqlc.types.Field(String, graphql_name='packageName')
    highest_fixed_version = sgqlc.types.Field(String, graphql_name='highestFixedVersion')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    extra_data = sgqlc.types.Field(JSONString, graphql_name='extraData')
    created = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')
    bug_count = sgqlc.types.Field(Int, graphql_name='bugCount')
    asset_name = sgqlc.types.Field(String, graphql_name='assetName')
    ticket_id = sgqlc.types.Field(String, graphql_name='ticketId')
    ticket_url = sgqlc.types.Field(String, graphql_name='ticketUrl')


class PortType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'asset', 'port', 'title', 'service', 'protocol', 'product', 'state', 'favicon', 'tls_info', 'technology_used', 'webserver', 'waf', 'created', 'updated', 'network_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    port = sgqlc.types.Field(Int, graphql_name='port')
    title = sgqlc.types.Field(String, graphql_name='title')
    service = sgqlc.types.Field(String, graphql_name='service')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    product = sgqlc.types.Field(String, graphql_name='product')
    state = sgqlc.types.Field(sgqlc.types.non_null(AppPortStateChoices), graphql_name='state')
    favicon = sgqlc.types.Field(String, graphql_name='favicon')
    tls_info = sgqlc.types.Field(GenericScalar, graphql_name='tlsInfo')
    technology_used = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='technologyUsed')
    webserver = sgqlc.types.Field(String, graphql_name='webserver')
    waf = sgqlc.types.Field(String, graphql_name='waf')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    network_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NetworkType))), graphql_name='networkSet')


class PreRequisitesPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('PreRequisitesType'), graphql_name='objects')


class PreRequisitesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'description', 'engagement', 'organization', 'is_completed', 'assigned_to', 'attachments', 'due_date', 'order_index', 'created', 'created_by', 'prerequisites_completion')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    engagement = sgqlc.types.Field(EngagementType, graphql_name='engagement')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    is_completed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCompleted')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalUserType))), graphql_name='assignedTo')
    attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='attachments')
    due_date = sgqlc.types.Field(Date, graphql_name='dueDate')
    order_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='orderIndex')
    created = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    prerequisites_completion = sgqlc.types.Field(GenericScalar, graphql_name='prerequisitesCompletion')


class PrefillsBulkCreateAndUpdateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class PrefillsBulkDeleteMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'prefills_deleted')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    prefills_deleted = sgqlc.types.Field(sgqlc.types.list_of('PrefillsType'), graphql_name='prefillsDeleted')


class PrefillsCreateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('prefills',)
    prefills = sgqlc.types.Field('PrefillsType', graphql_name='prefills')


class PrefillsPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('PrefillsType'), graphql_name='objects')


class PrefillsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'prefills_condition', 'prefills_data', 'hash', 'prefills_data_hash', 'created_by', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    prefills_condition = sgqlc.types.Field(JSONString, graphql_name='prefillsCondition')
    prefills_data = sgqlc.types.Field(JSONString, graphql_name='prefillsData')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    prefills_data_hash = sgqlc.types.Field(String, graphql_name='prefillsDataHash')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class PrefillsUpdateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('prefills',)
    prefills = sgqlc.types.Field(PrefillsType, graphql_name='prefills')


class PresetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'user', 'data', 'preset_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    user = sgqlc.types.Field(OrganizationMembersType, graphql_name='user')
    data = sgqlc.types.Field(GenericScalar, graphql_name='data')
    preset_type = sgqlc.types.Field(Int, graphql_name='presetType')


class PrioritizationType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'exploit_availability', 'sla', 'asset_exposure', 'asset_sensitivity', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization = sgqlc.types.Field(String, graphql_name='organization')
    exploit_availability = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='exploitAvailability')
    sla = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sla')
    asset_exposure = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetExposure')
    asset_sensitivity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetSensitivity')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class PriorityRuleSetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'name', 'description', 'filter_query', 'weight', 'stop_processing_on_match', 'is_active', 'created', 'updated', 'created_by', 'rules')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    filter_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filterQuery')
    weight = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weight')
    stop_processing_on_match = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='stopProcessingOnMatch')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    rules = sgqlc.types.Field(sgqlc.types.list_of('PriorityRuleType'), graphql_name='rules')


class PriorityRuleType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'rule_set', 'name', 'condition_query', 'action', 'score_value', 'is_active', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rule_set = sgqlc.types.Field(sgqlc.types.non_null(PriorityRuleSetType), graphql_name='ruleSet')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    condition_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='conditionQuery')
    action = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='action')
    score_value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scoreValue')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class PulseArtifactType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'thread', 'run', 'name', 'description', 'artifact_type', 'language', 'status', 'content', 'content_size', 'error_message', 'metadata', 'created_at', 'updated_at', 'download_url', 'formatted_size')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    thread = sgqlc.types.Field(sgqlc.types.non_null('PulseThreadType'), graphql_name='thread')
    run = sgqlc.types.Field('PulseRunType', graphql_name='run')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    artifact_type = sgqlc.types.Field(sgqlc.types.non_null(AppPulseArtifactArtifactTypeChoices), graphql_name='artifactType')
    language = sgqlc.types.Field(String, graphql_name='language')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppPulseArtifactStatusChoices), graphql_name='status')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    content_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='contentSize')
    error_message = sgqlc.types.Field(String, graphql_name='errorMessage')
    metadata = sgqlc.types.Field(GenericScalar, graphql_name='metadata')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    download_url = sgqlc.types.Field(String, graphql_name='downloadUrl')
    formatted_size = sgqlc.types.Field(String, graphql_name='formattedSize')


class PulseMessageType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'thread', 'run', 'author', 'agent_id', 'agent_name', 'blocks', 'status', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    thread = sgqlc.types.Field(sgqlc.types.non_null('PulseThreadType'), graphql_name='thread')
    run = sgqlc.types.Field('PulseRunType', graphql_name='run')
    author = sgqlc.types.Field(sgqlc.types.non_null(AppPulseMessageAuthorChoices), graphql_name='author')
    agent_id = sgqlc.types.Field(String, graphql_name='agentId')
    agent_name = sgqlc.types.Field(String, graphql_name='agentName')
    blocks = sgqlc.types.Field(GenericScalar, graphql_name='blocks')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppPulseMessageStatusChoices), graphql_name='status')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PulseParticipantType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'thread', 'role', 'agent_ref', 'agent_name', 'capabilities', 'added_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    thread = sgqlc.types.Field(sgqlc.types.non_null('PulseThreadType'), graphql_name='thread')
    role = sgqlc.types.Field(sgqlc.types.non_null(AppPulseParticipantRoleChoices), graphql_name='role')
    agent_ref = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='agentRef')
    agent_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='agentName')
    capabilities = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='capabilities')
    added_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='addedAt')


class PulsePlanType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'thread', 'run', 'title', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    thread = sgqlc.types.Field(sgqlc.types.non_null('PulseThreadType'), graphql_name='thread')
    run = sgqlc.types.Field(sgqlc.types.non_null('PulseRunType'), graphql_name='run')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PulseRunType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'thread', 'status', 'selected_agents', 'started_at', 'ended_at', 'metrics', 'error_message', 'created_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    thread = sgqlc.types.Field(sgqlc.types.non_null('PulseThreadType'), graphql_name='thread')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppPulseRunStatusChoices), graphql_name='status')
    selected_agents = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='selectedAgents')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    ended_at = sgqlc.types.Field(DateTime, graphql_name='endedAt')
    metrics = sgqlc.types.Field(JSONString, graphql_name='metrics')
    error_message = sgqlc.types.Field(String, graphql_name='errorMessage')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class PulseTaskType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'plan', 'task_id', 'agent_id', 'agent_name', 'title', 'status', 'progress', 'order', 'metadata', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    plan = sgqlc.types.Field(sgqlc.types.non_null(PulsePlanType), graphql_name='plan')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')
    agent_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='agentId')
    agent_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='agentName')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppPulseTaskStatusChoices), graphql_name='status')
    progress = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='progress')
    order = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='order')
    metadata = sgqlc.types.Field(JSONString, graphql_name='metadata')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PulseThreadType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'organization', 'user', 'title', 'context', 'mode', 'archived', 'created_at', 'updated_at', 'organization_id', 'latest_run_status', 'is_background_mode')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    user = sgqlc.types.Field(sgqlc.types.non_null(ApprovalUserType), graphql_name='user')
    title = sgqlc.types.Field(String, graphql_name='title')
    context = sgqlc.types.Field(JSONString, graphql_name='context')
    mode = sgqlc.types.Field(sgqlc.types.non_null(AppPulseThreadModeChoices), graphql_name='mode')
    archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='archived')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    latest_run_status = sgqlc.types.Field(String, graphql_name='latestRunStatus')
    is_background_mode = sgqlc.types.Field(Boolean, graphql_name='isBackgroundMode')


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organization_members', 'all_apis', 'thread', 'threads', 'messages', 'plan', 'tasks', 'events', 'active_run', 'artifacts', 'available_system_agents', 'risk_playground_data', 'all_possible_duplicates', 'total_count', 'all_prefills', 'all_self_managed_service_categories', 'all_self_managed_services', 'all_workbooks', 'all_sheet_rows', 'all_sheets', 'list_drafts', 'all_engagements_fields', 'engagement_connectors', 'all_automation_worfklow_activities', 'all_automation_workflows', 'engagement_automation_workflows', 'all_configurations', 'all_patches', 'all_azure_devops_repositories', 'all_package_asset_count', 'all_tickets', 'all_docker_registry_images', 'all_ecr_images', 'all_sla_rules', 'search_query_exist', 'weightage_exist', 'all_presets', 'all_data_retention_settings', 'all_grouped_bugs', 'all_grouped_assets', 'all_asm_settings', 'all_asset_fields', 'all_bug_fields', 'all_vault_attachments', 'all_widgets_v2', 'all_dashboards_v2', 'all_veracode_projects', 'all_logs', 'all_action_logs', 'all_prerequisites', 'all_software_packages', 'all_packages', 'all_bitbucket_repositories', 'all_github_repositories', 'github_repository_branches', 'github_repository_branches_batch', 'all_black_duck_projects', 'all_engagements_comment_activities', 'all_attachments', 'all_assessments', 'all_custom_assessment_statuses', 'all_approvals', 'all_assigned_user_views', 'check_view_name', 'all_report_attachments', 'all_prioritization_rules', 'all_priority_rule_sets', 'all_bug_reports', 'download_report', 'preview_report', 'all_templates', 'list_github_branch_tags', 'list_github_branch_tree', 'default_templates', 'default_asset_summary_report_template', 'default_sast_summary_report_template', 'default_dast_summary_report_template', 'default_executive_summary_report_template', 'default_cloud_security_overview_report_template', 'default_network_security_overview_report_template', 'default_container_security_overview_report_template', 'template_name_exist', 'assets_distribution', 'remediation_summary', 'remediation_trend', 'dashboard_stats', 'scanner_metric_sast', 'scanner_metric_dast', 'scanner_metric_sca', 'scanner_metric_secret_scan', 'scanner_metric_vm_scan', 'scanner_metric_cloud_security', 'scanner_metric_container_security', 'scanner_metric_asm', 'scanner_metric_internal_pentest', 'scanner_metric_external_pentest', 'scanner_metric_bug_bounty', 'finding_analysis', 'sla_violations_summary', 'sla_violations_health_matrix', 'sla_violations_at_risk', 'sla_violations_avg_time', 'integration_status', 'threat_analysis', 'security_gaps', 'scanners_available', 'scanner_config', 'top_vulnerabilities', 'cve_trends', 'security_highlights', 'all_widgets', 'all_assets_bugs_count_widget', 'all_software_packages_assets_bugs_count_widget', 'all_dashboards', 'all_groups', 'get_current_tenant', 'all_engagements', 'all_engagement_activities', 'all_engagements_activities', 'all_engagement_assets', 'all_engagement_bugs', 'all_nist', 'all_owasp', 'all_cve', 'all_cwe', 'pentesters_involved', 'all_tests', 'engagement_compliance_count', 'all_assets', 'asset_relationships_for_asset', 'all_asset_relationships_in_org', 'asset', 'all_bugs', 'close_findings', 'revert_closed_findings')
    organization_members = sgqlc.types.Field(OrganizationMembersPaginatedType, graphql_name='organizationMembers', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_apis = sgqlc.types.Field(ApiCursorPaginatedType, graphql_name='allApis', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    thread = sgqlc.types.Field(PulseThreadType, graphql_name='thread', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    threads = sgqlc.types.Field(sgqlc.types.list_of('ThreadSummaryType'), graphql_name='threads', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('archived', sgqlc.types.Arg(Boolean, graphql_name='archived', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    messages = sgqlc.types.Field(sgqlc.types.list_of(PulseMessageType), graphql_name='messages', args=sgqlc.types.ArgDict((
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    plan = sgqlc.types.Field(PulsePlanType, graphql_name='plan', args=sgqlc.types.ArgDict((
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
))
    )
    tasks = sgqlc.types.Field(sgqlc.types.list_of(PulseTaskType), graphql_name='tasks', args=sgqlc.types.ArgDict((
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
))
    )
    events = sgqlc.types.Field(sgqlc.types.list_of(EventEnvelopeType), graphql_name='events', args=sgqlc.types.ArgDict((
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
        ('after_seq', sgqlc.types.Arg(Int, graphql_name='afterSeq', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    active_run = sgqlc.types.Field(PulseRunType, graphql_name='activeRun', args=sgqlc.types.ArgDict((
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
))
    )
    artifacts = sgqlc.types.Field(sgqlc.types.list_of(PulseArtifactType), graphql_name='artifacts', args=sgqlc.types.ArgDict((
        ('thread_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='threadId', default=None)),
))
    )
    available_system_agents = sgqlc.types.Field(sgqlc.types.list_of('SystemAgentInfo'), graphql_name='availableSystemAgents')
    risk_playground_data = sgqlc.types.Field(sgqlc.types.list_of('RiskPlaygroundAssetGroup'), graphql_name='riskPlaygroundData', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('asset_grouping', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(GroupingCriterionInput)), graphql_name='assetGrouping', default=None)),
        ('findings_grouping', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(GroupingCriterionInput)), graphql_name='findingsGrouping', default=None)),
        ('asset_filters', sgqlc.types.Arg(String, graphql_name='assetFilters', default=None)),
        ('vulnerability_filters', sgqlc.types.Arg(String, graphql_name='vulnerabilityFilters', default=None)),
))
    )
    all_possible_duplicates = sgqlc.types.Field(AllPossibleDuplicatesPaginatedType, graphql_name='allPossibleDuplicates', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    all_prefills = sgqlc.types.Field(PrefillsPaginatedType, graphql_name='allPrefills', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_self_managed_service_categories = sgqlc.types.Field(sgqlc.types.list_of('SelfManagedServiceCategoryType'), graphql_name='allSelfManagedServiceCategories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    all_self_managed_services = sgqlc.types.Field('SelfManagedServicePaginatedType', graphql_name='allSelfManagedServices', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_workbooks = sgqlc.types.Field('WorkBookPaginatedType', graphql_name='allWorkbooks', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_sheet_rows = sgqlc.types.Field('SheetRowPaginatedType', graphql_name='allSheetRows', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_sheets = sgqlc.types.Field('SheetPaginatedType', graphql_name='allSheets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    list_drafts = sgqlc.types.Field(sgqlc.types.list_of(DraftType), graphql_name='listDrafts', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('draft_type', sgqlc.types.Arg(Int, graphql_name='draftType', default=None)),
        ('bug_level', sgqlc.types.Arg(Int, graphql_name='bugLevel', default=None)),
        ('report_template_id', sgqlc.types.Arg(Int, graphql_name='reportTemplateId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    all_engagements_fields = sgqlc.types.Field(EngagementFieldPaginatedType, graphql_name='allEngagementsFields', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    engagement_connectors = sgqlc.types.Field(sgqlc.types.list_of(EngagementConnectorType), graphql_name='engagementConnectors', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='engagementId', default=None)),
))
    )
    all_automation_worfklow_activities = sgqlc.types.Field(AutomationWorkflowActivityPaginatedType, graphql_name='allAutomationWorfklowActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_automation_workflows = sgqlc.types.Field(AutomationWorkflowPaginatedType, graphql_name='allAutomationWorkflows', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    engagement_automation_workflows = sgqlc.types.Field(AutomationWorkflowPaginatedType, graphql_name='engagementAutomationWorkflows', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='engagementId', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_configurations = sgqlc.types.Field(ConfigurationsPaginatedType, graphql_name='allConfigurations', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_patches = sgqlc.types.Field(PatchesPaginatedType, graphql_name='allPatches', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_azure_devops_repositories = sgqlc.types.Field(AzureDevopsRepositoriesTypePaginatedType, graphql_name='allAzureDevopsRepositories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('repo_name', sgqlc.types.Arg(String, graphql_name='repoName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('refresh', sgqlc.types.Arg(Boolean, graphql_name='refresh', default=None)),
))
    )
    all_package_asset_count = sgqlc.types.Field(PackageAssetPaginatedType, graphql_name='allPackageAssetCount', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_tickets = sgqlc.types.Field('TicketsPaginatedType', graphql_name='allTickets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_docker_registry_images = sgqlc.types.Field(DockerRegistryTypePaginatedType, graphql_name='allDockerRegistryImages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('image_name', sgqlc.types.Arg(String, graphql_name='imageName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_ecr_images = sgqlc.types.Field(ECRImagesTypePaginatedType, graphql_name='allEcrImages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('image_name', sgqlc.types.Arg(String, graphql_name='imageName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_sla_rules = sgqlc.types.Field('ServiceLevelAgreementCustomRulesPaginatedType', graphql_name='allSlaRules', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    search_query_exist = sgqlc.types.Field(Boolean, graphql_name='searchQueryExist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='searchQuery', default=None)),
))
    )
    weightage_exist = sgqlc.types.Field(Boolean, graphql_name='weightageExist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('weightage', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='weightage', default=None)),
))
    )
    all_presets = sgqlc.types.Field(sgqlc.types.list_of(PresetType), graphql_name='allPresets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    all_data_retention_settings = sgqlc.types.Field(sgqlc.types.list_of(DataRetentionSettingsType), graphql_name='allDataRetentionSettings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    all_grouped_bugs = sgqlc.types.Field(GroupBugPaginatedType, graphql_name='allGroupedBugs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('group_by', sgqlc.types.Arg(String, graphql_name='groupBy', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    all_grouped_assets = sgqlc.types.Field(GroupAssetPaginatedType, graphql_name='allGroupedAssets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('group_by', sgqlc.types.Arg(String, graphql_name='groupBy', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_asm_settings = sgqlc.types.Field(ASMSettingsType, graphql_name='allAsmSettings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('refresh_scope', sgqlc.types.Arg(Boolean, graphql_name='refreshScope', default=None)),
))
    )
    all_asset_fields = sgqlc.types.Field(AssetFieldPaginatedType, graphql_name='allAssetFields', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_bug_fields = sgqlc.types.Field(BugFieldPaginatedType, graphql_name='allBugFields', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_vault_attachments = sgqlc.types.Field('VaultPaginatedType', graphql_name='allVaultAttachments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
))
    )
    all_widgets_v2 = sgqlc.types.Field('WidgetsV2Type', graphql_name='allWidgetsV2', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('asset_filter_field_query', sgqlc.types.Arg(String, graphql_name='assetFilterFieldQuery', default=None)),
        ('bug_filter_field_query', sgqlc.types.Arg(String, graphql_name='bugFilterFieldQuery', default=None)),
        ('engagement_filter_field_query', sgqlc.types.Arg(String, graphql_name='engagementFilterFieldQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('row_page', sgqlc.types.Arg(Int, graphql_name='rowPage', default=None)),
        ('row_page_size', sgqlc.types.Arg(Int, graphql_name='rowPageSize', default=None)),
        ('col_page', sgqlc.types.Arg(Int, graphql_name='colPage', default=None)),
        ('col_page_size', sgqlc.types.Arg(Int, graphql_name='colPageSize', default=None)),
        ('row_search', sgqlc.types.Arg(String, graphql_name='rowSearch', default=None)),
        ('col_search', sgqlc.types.Arg(String, graphql_name='colSearch', default=None)),
))
    )
    all_dashboards_v2 = sgqlc.types.Field(DashboardsV2Type, graphql_name='allDashboardsV2', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_veracode_projects = sgqlc.types.Field('VeracodeProjectsTypePaginatedType', graphql_name='allVeracodeProjects', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('agent_id', sgqlc.types.Arg(Int, graphql_name='agentId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    all_logs = sgqlc.types.Field('ScanLogPaginatedType', graphql_name='allLogs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('log_type', sgqlc.types.Arg(String, graphql_name='logType', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_action_logs = sgqlc.types.Field(BotTaskPaginatedType, graphql_name='allActionLogs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_prerequisites = sgqlc.types.Field(PreRequisitesPaginatedType, graphql_name='allPrerequisites', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(String, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_software_packages = sgqlc.types.Field('SoftwarePackagePaginatedType', graphql_name='allSoftwarePackages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_packages = sgqlc.types.Field(PackagePaginatedType, graphql_name='allPackages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_bitbucket_repositories = sgqlc.types.Field(BitbucketRepositoriesTypePaginatedType, graphql_name='allBitbucketRepositories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('repo_name', sgqlc.types.Arg(String, graphql_name='repoName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_github_repositories = sgqlc.types.Field(GithubRepositoriesTypePaginatedType, graphql_name='allGithubRepositories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('repo_name', sgqlc.types.Arg(String, graphql_name='repoName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('refresh', sgqlc.types.Arg(Boolean, graphql_name='refresh', default=None)),
        ('github_enterprise_url', sgqlc.types.Arg(String, graphql_name='githubEnterpriseUrl', default=None)),
))
    )
    github_repository_branches = sgqlc.types.Field(GithubBranchesType, graphql_name='githubRepositoryBranches', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='cmId', default=None)),
        ('repo_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='repoUrl', default=None)),
))
    )
    github_repository_branches_batch = sgqlc.types.Field(GithubBranchesBatchType, graphql_name='githubRepositoryBranchesBatch', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='cmId', default=None)),
        ('repo_urls', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='repoUrls', default=None)),
))
    )
    all_black_duck_projects = sgqlc.types.Field(BlackDuckProjectsTypePaginatedType, graphql_name='allBlackDuckProjects', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('agent_id', sgqlc.types.Arg(Int, graphql_name='agentId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    all_engagements_comment_activities = sgqlc.types.Field(EngagementActivityPaginatedType, graphql_name='allEngagementsCommentActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('assessment_state_last_updated', sgqlc.types.Arg(Boolean, graphql_name='assessmentStateLastUpdated', default=None)),
        ('assessment_id', sgqlc.types.Arg(Int, graphql_name='assessmentId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_attachments = sgqlc.types.Field(AttachmentPaginatedType, graphql_name='allAttachments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_assessments = sgqlc.types.Field(AssessmentPaginatedType, graphql_name='allAssessments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_custom_assessment_statuses = sgqlc.types.Field(CustomAssessmentStatusPaginatedType, graphql_name='allCustomAssessmentStatuses', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_approvals = sgqlc.types.Field(ApprovalPaginatedType, graphql_name='allApprovals', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_assigned_user_views = sgqlc.types.Field(sgqlc.types.list_of(FilterViewsType), graphql_name='allAssignedUserViews', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
))
    )
    check_view_name = sgqlc.types.Field(Boolean, graphql_name='checkViewName', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('is_asset_view', sgqlc.types.Arg(Boolean, graphql_name='isAssetView', default=None)),
        ('is_bug_view', sgqlc.types.Arg(Boolean, graphql_name='isBugView', default=None)),
        ('folder_id', sgqlc.types.Arg(Int, graphql_name='folderId', default=None)),
))
    )
    all_report_attachments = sgqlc.types.Field('ReportAttachmentPaginatedType', graphql_name='allReportAttachments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_prioritization_rules = sgqlc.types.Field(PrioritizationType, graphql_name='allPrioritizationRules', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    all_priority_rule_sets = sgqlc.types.Field(sgqlc.types.list_of(PriorityRuleSetType), graphql_name='allPriorityRuleSets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    all_bug_reports = sgqlc.types.Field('ReportPaginatedType', graphql_name='allBugReports', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    download_report = sgqlc.types.Field('ReportType', graphql_name='downloadReport', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('export_id', sgqlc.types.Arg(UUID, graphql_name='exportId', default=None)),
))
    )
    preview_report = sgqlc.types.Field(String, graphql_name='previewReport', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='templateId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
        ('custom_data', sgqlc.types.Arg(JSONString, graphql_name='customData', default=None)),
        ('report_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reportName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
))
    )
    all_templates = sgqlc.types.Field('TemplatePaginatedType', graphql_name='allTemplates', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('template_id', sgqlc.types.Arg(Int, graphql_name='templateId', default=None)),
        ('header_template', sgqlc.types.Arg(String, graphql_name='headerTemplate', default=None)),
        ('footer_template', sgqlc.types.Arg(String, graphql_name='footerTemplate', default=None)),
))
    )
    list_github_branch_tags = sgqlc.types.Field(GenericScalar, graphql_name='listGithubBranchTags', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('branch_search_string', sgqlc.types.Arg(String, graphql_name='branchSearchString', default=None)),
))
    )
    list_github_branch_tree = sgqlc.types.Field(GenericScalar, graphql_name='listGithubBranchTree', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('branch', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='branch', default=None)),
))
    )
    default_templates = sgqlc.types.Field(GenericScalar, graphql_name='defaultTemplates')
    default_asset_summary_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultAssetSummaryReportTemplate')
    default_sast_summary_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultSastSummaryReportTemplate')
    default_dast_summary_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultDastSummaryReportTemplate')
    default_executive_summary_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultExecutiveSummaryReportTemplate')
    default_cloud_security_overview_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultCloudSecurityOverviewReportTemplate')
    default_network_security_overview_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultNetworkSecurityOverviewReportTemplate')
    default_container_security_overview_report_template = sgqlc.types.Field(GenericScalar, graphql_name='defaultContainerSecurityOverviewReportTemplate')
    template_name_exist = sgqlc.types.Field(Boolean, graphql_name='templateNameExist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    assets_distribution = sgqlc.types.Field(AssetsDistributionType, graphql_name='assetsDistribution', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('by', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='by', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    remediation_summary = sgqlc.types.Field('RemediationSummaryType', graphql_name='remediationSummary', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    remediation_trend = sgqlc.types.Field('RemediationTrendType', graphql_name='remediationTrend', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    dashboard_stats = sgqlc.types.Field(DashboardStatsType, graphql_name='dashboardStats', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_sast = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricSast', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_dast = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricDast', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_sca = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricSca', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_secret_scan = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricSecretScan', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_vm_scan = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricVmScan', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_cloud_security = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricCloudSecurity', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_container_security = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricContainerSecurity', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_asm = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricAsm', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_internal_pentest = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricInternalPentest', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_external_pentest = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricExternalPentest', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    scanner_metric_bug_bounty = sgqlc.types.Field('ScannerMetricType', graphql_name='scannerMetricBugBounty', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    finding_analysis = sgqlc.types.Field(FindingAnalysisType, graphql_name='findingAnalysis', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    sla_violations_summary = sgqlc.types.Field('SLAViolationsSummaryType', graphql_name='slaViolationsSummary', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    sla_violations_health_matrix = sgqlc.types.Field('SLAViolationsHealthMatrixType', graphql_name='slaViolationsHealthMatrix', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    sla_violations_at_risk = sgqlc.types.Field('SLAViolationsAtRiskType', graphql_name='slaViolationsAtRisk', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    sla_violations_avg_time = sgqlc.types.Field('SLAViolationsAvgTimeType', graphql_name='slaViolationsAvgTime', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    integration_status = sgqlc.types.Field(IntegrationStatusType, graphql_name='integrationStatus', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    threat_analysis = sgqlc.types.Field('ThreatAnalysisType', graphql_name='threatAnalysis', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('range', sgqlc.types.Arg(RangeInputType, graphql_name='range', default=None)),
))
    )
    security_gaps = sgqlc.types.Field('SecurityGapsType', graphql_name='securityGaps', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    scanners_available = sgqlc.types.Field('ScannersAvailableType', graphql_name='scannersAvailable', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    scanner_config = sgqlc.types.Field('ScannerConfigType', graphql_name='scannerConfig', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    top_vulnerabilities = sgqlc.types.Field('TopVulnerabilitiesType', graphql_name='topVulnerabilities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    cve_trends = sgqlc.types.Field(CVETrendsType, graphql_name='cveTrends', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    security_highlights = sgqlc.types.Field('SecurityHighlightsType', graphql_name='securityHighlights', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    all_widgets = sgqlc.types.Field('WidgetType', graphql_name='allWidgets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('widgets', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='widgets', default=None)),
        ('datetime', sgqlc.types.Arg(Int, graphql_name='datetime', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('cache_refresh', sgqlc.types.Arg(Boolean, graphql_name='cacheRefresh', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('fetch_from_cache', sgqlc.types.Arg(Boolean, graphql_name='fetchFromCache', default=None)),
        ('widget_filter', sgqlc.types.Arg(JSONString, graphql_name='widgetFilter', default=None)),
        ('is_archived_view', sgqlc.types.Arg(Boolean, graphql_name='isArchivedView', default=None)),
        ('scan_log_search_query', sgqlc.types.Arg(String, graphql_name='scanLogSearchQuery', default=None)),
        ('tracker_search_query', sgqlc.types.Arg(String, graphql_name='trackerSearchQuery', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('assessment_search_query', sgqlc.types.Arg(String, graphql_name='assessmentSearchQuery', default=None)),
        ('software_package_search_query', sgqlc.types.Arg(String, graphql_name='softwarePackageSearchQuery', default=None)),
))
    )
    all_assets_bugs_count_widget = sgqlc.types.Field(AssetWidgetPaginatedType, graphql_name='allAssetsBugsCountWidget', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('datetime', sgqlc.types.Arg(Int, graphql_name='datetime', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('cache_refresh', sgqlc.types.Arg(Boolean, graphql_name='cacheRefresh', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('fetch_from_cache', sgqlc.types.Arg(Boolean, graphql_name='fetchFromCache', default=None)),
        ('widget_filter', sgqlc.types.Arg(JSONString, graphql_name='widgetFilter', default=None)),
))
    )
    all_software_packages_assets_bugs_count_widget = sgqlc.types.Field('SoftwareWidgetPaginatedType', graphql_name='allSoftwarePackagesAssetsBugsCountWidget', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('datetime', sgqlc.types.Arg(Int, graphql_name='datetime', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('cache_refresh', sgqlc.types.Arg(Boolean, graphql_name='cacheRefresh', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('package_search_query', sgqlc.types.Arg(String, graphql_name='packageSearchQuery', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('fetch_from_cache', sgqlc.types.Arg(Boolean, graphql_name='fetchFromCache', default=None)),
        ('widget_filter', sgqlc.types.Arg(JSONString, graphql_name='widgetFilter', default=None)),
))
    )
    all_dashboards = sgqlc.types.Field(GenericScalar, graphql_name='allDashboards')
    all_groups = sgqlc.types.Field(GroupPaginatedType, graphql_name='allGroups', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    get_current_tenant = sgqlc.types.Field('TenantOrganizationType', graphql_name='getCurrentTenant')
    all_engagements = sgqlc.types.Field(EngagementPaginatedType, graphql_name='allEngagements', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('export_report_type', sgqlc.types.Arg(String, graphql_name='exportReportType', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('export_with_log_hours', sgqlc.types.Arg(Boolean, graphql_name='exportWithLogHours', default=False)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_engagement_activities = sgqlc.types.Field(EngagementCommentPaginatedType, graphql_name='allEngagementActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_engagements_activities = sgqlc.types.Field(EngagementCommentPaginatedType, graphql_name='allEngagementsActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_engagement_assets = sgqlc.types.Field(EngagementAssetPaginatedType, graphql_name='allEngagementAssets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_engagement_bugs = sgqlc.types.Field(EngagementBugPaginatedType, graphql_name='allEngagementBugs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_nist = sgqlc.types.Field(NISTPaginatedType, graphql_name='allNist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_owasp = sgqlc.types.Field(OWASPPaginatedType, graphql_name='allOwasp', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_cve = sgqlc.types.Field(CVEPaginatedType, graphql_name='allCve', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_cwe = sgqlc.types.Field(CWEPaginatedType, graphql_name='allCwe', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    pentesters_involved = sgqlc.types.Field('UserPaginatedType', graphql_name='pentestersInvolved', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_tests = sgqlc.types.Field('TestsPaginatedType', graphql_name='allTests', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('compliance_type', sgqlc.types.Arg(String, graphql_name='complianceType', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    engagement_compliance_count = sgqlc.types.Field(CompliancePaginatedType, graphql_name='engagementComplianceCount', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_assets = sgqlc.types.Field(AssetCursorPaginatedType, graphql_name='allAssets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('export_report_type', sgqlc.types.Arg(String, graphql_name='exportReportType', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('selected_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='selectedFields', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(String, graphql_name='groupByValue', default=None)),
        ('preset_id', sgqlc.types.Arg(Int, graphql_name='presetId', default=None)),
        ('exclude_search_query', sgqlc.types.Arg(String, graphql_name='excludeSearchQuery', default=None)),
))
    )
    asset_relationships_for_asset = sgqlc.types.Field(sgqlc.types.list_of(AssetRelationshipType), graphql_name='assetRelationshipsForAsset', args=sgqlc.types.ArgDict((
        ('asset_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='assetId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    all_asset_relationships_in_org = sgqlc.types.Field(AssetRelationshipPaginatedType, graphql_name='allAssetRelationshipsInOrg', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    asset = sgqlc.types.Field(AssetType, graphql_name='asset', args=sgqlc.types.ArgDict((
        ('asset_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='assetId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    all_bugs = sgqlc.types.Field(BugCursorPaginatedType, graphql_name='allBugs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('export_report_type', sgqlc.types.Arg(String, graphql_name='exportReportType', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('selected_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='selectedFields', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('preset_id', sgqlc.types.Arg(Int, graphql_name='presetId', default=None)),
))
    )
    close_findings = sgqlc.types.Field(CloseFindingType, graphql_name='closeFindings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('configuration_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='configurationId', default=None)),
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('view_id', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='viewId', default=None)),
))
    )
    revert_closed_findings = sgqlc.types.Field(CloseFindingType, graphql_name='revertClosedFindings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('close_task_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='closeTaskId', default=None)),
))
    )


class ReferenceType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'tenant_cwe_references', 'tenant_cve_references', 'bug_references')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    tenant_cwe_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CWEType))), graphql_name='tenantCweReferences')
    tenant_cve_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='tenantCveReferences')
    bug_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugReferences')


class RegionType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('code', 'label', 'count')
    code = sgqlc.types.Field(String, graphql_name='code')
    label = sgqlc.types.Field(String, graphql_name='label')
    count = sgqlc.types.Field(Int, graphql_name='count')


class RemediationSummaryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('current_mttr', 'previous_mttr', 'mttr_critical', 'mttr_high', 'mttr_medium', 'mttr_low', 'industry_benchmark', 'organization_industry')
    current_mttr = sgqlc.types.Field(Float, graphql_name='currentMttr')
    previous_mttr = sgqlc.types.Field(Float, graphql_name='previousMttr')
    mttr_critical = sgqlc.types.Field(Float, graphql_name='mttrCritical')
    mttr_high = sgqlc.types.Field(Float, graphql_name='mttrHigh')
    mttr_medium = sgqlc.types.Field(Float, graphql_name='mttrMedium')
    mttr_low = sgqlc.types.Field(Float, graphql_name='mttrLow')
    industry_benchmark = sgqlc.types.Field(IndustryBenchmarkType, graphql_name='industryBenchmark')
    organization_industry = sgqlc.types.Field(String, graphql_name='organizationIndustry')


class RemediationTrendType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('trend_data',)
    trend_data = sgqlc.types.Field(sgqlc.types.list_of('TrendDataPointType'), graphql_name='trendData')


class ReportAttachmentPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('ReportAttachmentType'), graphql_name='objects')


class ReportAttachmentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'attachment', 'attachment_name', 'organization', 'attached_by', 'created', 'updated', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    attachment = sgqlc.types.Field(String, graphql_name='attachment')
    attachment_name = sgqlc.types.Field(String, graphql_name='attachmentName')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    attached_by = sgqlc.types.Field(ApprovalUserType, graphql_name='attachedBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    url = sgqlc.types.Field(String, graphql_name='url')


class ReportPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('ReportType'), graphql_name='objects')


class ReportType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'export_id', 'user', 'report_type', 'scan', 'report_name', 'report_path', 'file', 'created', 'status', 'bug_ids', 'asset_ids', 'organization', 'engagement', 'template', 'template_custom_data', 'exported_app', 'html_report', 'revised_from', 'original_report', 'self_revised_from', 'self_original_report', 'automationworkflows_set', 'has_password')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    export_id = sgqlc.types.Field(UUID, graphql_name='exportId')
    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')
    report_type = sgqlc.types.Field(String, graphql_name='reportType')
    scan = sgqlc.types.Field(AllScanLogType, graphql_name='scan')
    report_name = sgqlc.types.Field(String, graphql_name='reportName')
    report_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reportPath')
    file = sgqlc.types.Field(String, graphql_name='file')
    created = sgqlc.types.Field(DateTime, graphql_name='created')
    status = sgqlc.types.Field(String, graphql_name='status')
    bug_ids = sgqlc.types.Field(JSONString, graphql_name='bugIds')
    asset_ids = sgqlc.types.Field(JSONString, graphql_name='assetIds')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    engagement = sgqlc.types.Field(EngagementType, graphql_name='engagement')
    template = sgqlc.types.Field('TemplateType', graphql_name='template')
    template_custom_data = sgqlc.types.Field(GenericScalar, graphql_name='templateCustomData')
    exported_app = sgqlc.types.Field(String, graphql_name='exportedApp')
    html_report = sgqlc.types.Field(String, graphql_name='htmlReport')
    revised_from = sgqlc.types.Field('ReportType', graphql_name='revisedFrom')
    original_report = sgqlc.types.Field('ReportType', graphql_name='originalReport')
    self_revised_from = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='selfRevisedFrom')
    self_original_report = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='selfOriginalReport')
    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='automationworkflowsSet')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')


class RestoreDefaultPriortizationRuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rules',)
    rules = sgqlc.types.Field(PrioritizationType, graphql_name='rules')


class RevertBulkUpdateActionMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('task', 'success', 'message')
    task = sgqlc.types.Field(BotTaskType, graphql_name='task')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class RiskBucketType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bucket_label', 'count')
    bucket_label = sgqlc.types.Field(String, graphql_name='bucketLabel')
    count = sgqlc.types.Field(Int, graphql_name='count')


class RiskPlaygroundAssetGroup(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('group_name', 'asset_count', 'total_vulnerability_count', 'finding_distribution', 'sub_groups')
    group_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupName')
    asset_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetCount')
    total_vulnerability_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalVulnerabilityCount')
    finding_distribution = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('RiskPlaygroundVulnerabilityDistribution')), graphql_name='findingDistribution')
    sub_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('RiskPlaygroundAssetGroup')), graphql_name='subGroups')


class RiskPlaygroundVulnerabilityDistribution(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('group_name', 'vulnerability_count', 'affected_asset_count', 'subdistribution')
    group_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupName')
    vulnerability_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='vulnerabilityCount')
    affected_asset_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affectedAssetCount')
    subdistribution = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('RiskPlaygroundVulnerabilityDistribution')), graphql_name='subdistribution')


class SLAHealthMatrixType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('today_critical', 'today_high', 'today_medium', 'today_low', 'week_critical', 'week_high', 'week_medium', 'week_low', 'month_critical', 'month_high', 'month_medium', 'month_low')
    today_critical = sgqlc.types.Field(Int, graphql_name='todayCritical')
    today_high = sgqlc.types.Field(Int, graphql_name='todayHigh')
    today_medium = sgqlc.types.Field(Int, graphql_name='todayMedium')
    today_low = sgqlc.types.Field(Int, graphql_name='todayLow')
    week_critical = sgqlc.types.Field(Int, graphql_name='weekCritical')
    week_high = sgqlc.types.Field(Int, graphql_name='weekHigh')
    week_medium = sgqlc.types.Field(Int, graphql_name='weekMedium')
    week_low = sgqlc.types.Field(Int, graphql_name='weekLow')
    month_critical = sgqlc.types.Field(Int, graphql_name='monthCritical')
    month_high = sgqlc.types.Field(Int, graphql_name='monthHigh')
    month_medium = sgqlc.types.Field(Int, graphql_name='monthMedium')
    month_low = sgqlc.types.Field(Int, graphql_name='monthLow')


class SLASeverityCountType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('critical', 'high', 'medium', 'low')
    critical = sgqlc.types.Field(Int, graphql_name='critical')
    high = sgqlc.types.Field(Int, graphql_name='high')
    medium = sgqlc.types.Field(Int, graphql_name='medium')
    low = sgqlc.types.Field(Int, graphql_name='low')


class SLAViolationsAtRiskType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('at_risk_slas',)
    at_risk_slas = sgqlc.types.Field(sgqlc.types.list_of(AtRiskSLAType), graphql_name='atRiskSlas')


class SLAViolationsAvgTimeType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('avg_violation_hours_critical', 'avg_violation_hours_high', 'avg_violation_hours_medium', 'avg_violation_hours_low')
    avg_violation_hours_critical = sgqlc.types.Field(Float, graphql_name='avgViolationHoursCritical')
    avg_violation_hours_high = sgqlc.types.Field(Float, graphql_name='avgViolationHoursHigh')
    avg_violation_hours_medium = sgqlc.types.Field(Float, graphql_name='avgViolationHoursMedium')
    avg_violation_hours_low = sgqlc.types.Field(Float, graphql_name='avgViolationHoursLow')


class SLAViolationsHealthMatrixType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('health_matrix',)
    health_matrix = sgqlc.types.Field(SLAHealthMatrixType, graphql_name='healthMatrix')


class SLAViolationsSummaryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_count', 'oldest_days', 'unique_units', 'severity_counts')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    oldest_days = sgqlc.types.Field(Int, graphql_name='oldestDays')
    unique_units = sgqlc.types.Field(Int, graphql_name='uniqueUnits')
    severity_counts = sgqlc.types.Field(SLASeverityCountType, graphql_name='severityCounts')


class ScanLogPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(AllScanLogType), graphql_name='objects')


class ScanType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'status', 'scan_frequency')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    status = sgqlc.types.Field(String, graphql_name='status')
    scan_frequency = sgqlc.types.Field(String, graphql_name='scanFrequency')


class ScannerConfigType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('configured_count', 'total_scanners', 'percentage')
    configured_count = sgqlc.types.Field(Int, graphql_name='configuredCount')
    total_scanners = sgqlc.types.Field(Int, graphql_name='totalScanners')
    percentage = sgqlc.types.Field(Int, graphql_name='percentage')


class ScannerMetricType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'name', 'is_configured', 'has_warning', 'finding_count', 'percentage_change', 'severity_distribution', 'last_scan_time', 'avg_risk_score', 'risk_level', 'connector_info')
    type = sgqlc.types.Field(String, graphql_name='type')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_configured = sgqlc.types.Field(Boolean, graphql_name='isConfigured')
    has_warning = sgqlc.types.Field(Boolean, graphql_name='hasWarning')
    finding_count = sgqlc.types.Field(Int, graphql_name='findingCount')
    percentage_change = sgqlc.types.Field(Float, graphql_name='percentageChange')
    severity_distribution = sgqlc.types.Field('SeverityDistributionType', graphql_name='severityDistribution')
    last_scan_time = sgqlc.types.Field(String, graphql_name='lastScanTime')
    avg_risk_score = sgqlc.types.Field(Int, graphql_name='avgRiskScore')
    risk_level = sgqlc.types.Field(String, graphql_name='riskLevel')
    connector_info = sgqlc.types.Field(ConnectorInfoType, graphql_name='connectorInfo')


class ScannersAvailableType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('count', 'scanner_types')
    count = sgqlc.types.Field(Int, graphql_name='count')
    scanner_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='scannerTypes')


class SecurityGapsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('count', 'scanner_types')
    count = sgqlc.types.Field(Int, graphql_name='count')
    scanner_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='scannerTypes')


class SecurityHighlightItemType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'title', 'description')
    type = sgqlc.types.Field(String, graphql_name='type')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')


class SecurityHighlightsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('highlights',)
    highlights = sgqlc.types.Field(sgqlc.types.list_of(SecurityHighlightItemType), graphql_name='highlights')


class SelectAgentsForThread(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('thread', 'participants')
    thread = sgqlc.types.Field(PulseThreadType, graphql_name='thread')
    participants = sgqlc.types.Field(sgqlc.types.list_of(PulseParticipantType), graphql_name='participants')


class SelfManagedServiceCategoryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'created', 'updated', 'selfmanagedservice_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field(String, graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    selfmanagedservice_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SelfManagedServiceType'))), graphql_name='selfmanagedserviceSet')


class SelfManagedServicePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('SelfManagedServiceType'), graphql_name='objects')


class SelfManagedServiceType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'category', 'image', 'organization', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    category = sgqlc.types.Field(sgqlc.types.non_null(SelfManagedServiceCategoryType), graphql_name='category')
    image = sgqlc.types.Field(String, graphql_name='image')
    organization = sgqlc.types.Field(String, graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class SendMessage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('run', 'message')
    run = sgqlc.types.Field(PulseRunType, graphql_name='run')
    message = sgqlc.types.Field(PulseMessageType, graphql_name='message')


class ServiceLevelAgreementCustomRulesPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('ServiceLevelAgreementCustomRulesType'), graphql_name='objects')


class ServiceLevelAgreementCustomRulesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'search_query', 'weightage', 'severity', 'duration', 'is_default', 'organization', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    search_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchQuery')
    weightage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightage')
    severity = sgqlc.types.Field(Int, graphql_name='severity')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class SetReportPasswordMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class SeverityCountType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('critical', 'high', 'medium', 'low')
    critical = sgqlc.types.Field(Int, graphql_name='critical')
    high = sgqlc.types.Field(Int, graphql_name='high')
    medium = sgqlc.types.Field(Int, graphql_name='medium')
    low = sgqlc.types.Field(Int, graphql_name='low')


class SeverityDistributionType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('critical', 'high', 'medium', 'low')
    critical = sgqlc.types.Field(Int, graphql_name='critical')
    high = sgqlc.types.Field(Int, graphql_name='high')
    medium = sgqlc.types.Field(Int, graphql_name='medium')
    low = sgqlc.types.Field(Int, graphql_name='low')


class SheetCreateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sheet',)
    sheet = sgqlc.types.Field('SheetType', graphql_name='sheet')


class SheetDeleteMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sheet',)
    sheet = sgqlc.types.Field('SheetType', graphql_name='sheet')


class SheetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('SheetType'), graphql_name='objects')


class SheetRowDeleteMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sheet_row',)
    sheet_row = sgqlc.types.Field('SheetRowType', graphql_name='sheetRow')


class SheetRowPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('SheetRowType'), graphql_name='objects')


class SheetRowType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'row', 'sheet', 'last_updated_by')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    row = sgqlc.types.Field(JSONString, graphql_name='row')
    sheet = sgqlc.types.Field(sgqlc.types.non_null('SheetType'), graphql_name='sheet')
    last_updated_by = sgqlc.types.Field(ApprovalUserType, graphql_name='lastUpdatedBy')


class SheetRowUpdateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sheet_row', 'message')
    sheet_row = sgqlc.types.Field(sgqlc.types.list_of(SheetRowType), graphql_name='sheetRow')
    message = sgqlc.types.Field(String, graphql_name='message')


class SheetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'state', 'organization', 'created_by', 'created', 'updated', 'workbook', 'rows')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    state = sgqlc.types.Field(JSONString, graphql_name='state')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    workbook = sgqlc.types.Field(sgqlc.types.non_null('WorkBookType'), graphql_name='workbook')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SheetRowType))), graphql_name='rows')


class SheetUpdateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sheet',)
    sheet = sgqlc.types.Field(SheetType, graphql_name='sheet')


class ShowReportPasswordMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'password', 'message')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    password = sgqlc.types.Field(String, graphql_name='password')
    message = sgqlc.types.Field(String, graphql_name='message')


class SoftwarePackagePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('SoftwarePackageType'), graphql_name='objects')


class SoftwarePackageType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'package_name', 'installed_version', 'file_name', 'ecosystem', 'asset', 'organization', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    package_name = sgqlc.types.Field(String, graphql_name='packageName')
    installed_version = sgqlc.types.Field(String, graphql_name='installedVersion')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')
    ecosystem = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ecosystem')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class SoftwarePackageWidgetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'package_name', 'affected_versions', 'installed_version', 'fixed_version', 'digest', 'commit', 'file_name', 'ecosystem', 'branch', 'batch_id', 'temp_id', 'releases', 'total', 'open', 'closed', 'risk_score', 'info_open', 'info_closed', 'low_open', 'low_closed', 'medium_open', 'medium_closed', 'high_open', 'high_closed', 'critical_open', 'critical_closed')
    id = sgqlc.types.Field(Int, graphql_name='id')
    package_name = sgqlc.types.Field(String, graphql_name='packageName')
    affected_versions = sgqlc.types.Field(JSONString, graphql_name='affectedVersions')
    installed_version = sgqlc.types.Field(String, graphql_name='installedVersion')
    fixed_version = sgqlc.types.Field(String, graphql_name='fixedVersion')
    digest = sgqlc.types.Field(String, graphql_name='digest')
    commit = sgqlc.types.Field(String, graphql_name='commit')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')
    ecosystem = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ecosystem')
    branch = sgqlc.types.Field(JSONString, graphql_name='branch')
    batch_id = sgqlc.types.Field(UUID, graphql_name='batchId')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')
    releases = sgqlc.types.Field(JSONString, graphql_name='releases')
    total = sgqlc.types.Field(Int, graphql_name='total')
    open = sgqlc.types.Field(Int, graphql_name='open')
    closed = sgqlc.types.Field(Int, graphql_name='closed')
    risk_score = sgqlc.types.Field(Float, graphql_name='riskScore')
    info_open = sgqlc.types.Field(Int, graphql_name='infoOpen')
    info_closed = sgqlc.types.Field(Int, graphql_name='infoClosed')
    low_open = sgqlc.types.Field(Int, graphql_name='lowOpen')
    low_closed = sgqlc.types.Field(Int, graphql_name='lowClosed')
    medium_open = sgqlc.types.Field(Int, graphql_name='mediumOpen')
    medium_closed = sgqlc.types.Field(Int, graphql_name='mediumClosed')
    high_open = sgqlc.types.Field(Int, graphql_name='highOpen')
    high_closed = sgqlc.types.Field(Int, graphql_name='highClosed')
    critical_open = sgqlc.types.Field(Int, graphql_name='criticalOpen')
    critical_closed = sgqlc.types.Field(Int, graphql_name='criticalClosed')


class SoftwareWidgetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(SoftwarePackageWidgetType), graphql_name='objects')


class SourceDistributionType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('source', 'count', 'percentage')
    source = sgqlc.types.Field(String, graphql_name='source')
    count = sgqlc.types.Field(Int, graphql_name='count')
    percentage = sgqlc.types.Field(Float, graphql_name='percentage')


class StartBackgroundRun(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('thread', 'run')
    thread = sgqlc.types.Field(PulseThreadType, graphql_name='thread')
    run = sgqlc.types.Field(PulseRunType, graphql_name='run')


class StartSystemAgentChat(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('thread',)
    thread = sgqlc.types.Field(PulseThreadType, graphql_name='thread')


class StatMetricType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('current_value', 'previous_value', 'percentage_change', 'trend', 'sparkline_data')
    current_value = sgqlc.types.Field(Int, graphql_name='currentValue')
    previous_value = sgqlc.types.Field(Int, graphql_name='previousValue')
    percentage_change = sgqlc.types.Field(Float, graphql_name='percentageChange')
    trend = sgqlc.types.Field(String, graphql_name='trend')
    sparkline_data = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='sparklineData')


class StateCountType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('open', 'resolved', 'not_applicable', 'duplicate', 'accepted_risk', 'wont_fix')
    open = sgqlc.types.Field(Int, graphql_name='open')
    resolved = sgqlc.types.Field(Int, graphql_name='resolved')
    not_applicable = sgqlc.types.Field(Int, graphql_name='notApplicable')
    duplicate = sgqlc.types.Field(Int, graphql_name='duplicate')
    accepted_risk = sgqlc.types.Field(Int, graphql_name='acceptedRisk')
    wont_fix = sgqlc.types.Field(Int, graphql_name='wontFix')


class SyncBugWithTrackersMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'msg')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    msg = sgqlc.types.Field(String, graphql_name='msg')


class SystemAgentInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'required_context', 'capabilities')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    required_context = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='requiredContext')
    capabilities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='capabilities')


class TagType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'slug', 'name', 'created', 'updated', 'organization', 'tenant_cve_tags', 'asset_tags', 'bug_tags')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    tenant_cve_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='tenantCveTags')
    asset_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetTags')
    bug_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugTags')


class TeamType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'vendor', 'created', 'updated', 'configuration_team', 'team', 'activity_team', 'comments_team')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    vendor = sgqlc.types.Field('VendorType', graphql_name='vendor')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    configuration_team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationsFieldType))), graphql_name='configurationTeam')
    team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='team')
    activity_team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementActivityType))), graphql_name='activityTeam')
    comments_team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementCommentType))), graphql_name='commentsTeam')


class TechnologyTagType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'count')
    name = sgqlc.types.Field(String, graphql_name='name')
    count = sgqlc.types.Field(Int, graphql_name='count')


class TemplatePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('TemplateType'), graphql_name='objects')


class TemplateType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'template_name', 'organization', 'custom_fields', 'html_content', 'is_active', 'is_editable', 'created_by', 'created', 'updated', 'header_template', 'footer_template', 'mode', 'type', 'file_path', 'branch', 'exportreport_set', 'draft_set', 'html', 'header', 'footer')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    template_name = sgqlc.types.Field(String, graphql_name='templateName')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    custom_fields = sgqlc.types.Field(GenericScalar, graphql_name='customFields')
    html_content = sgqlc.types.Field(String, graphql_name='htmlContent')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    is_editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEditable')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    header_template = sgqlc.types.Field(String, graphql_name='headerTemplate')
    footer_template = sgqlc.types.Field(String, graphql_name='footerTemplate')
    mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mode')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    file_path = sgqlc.types.Field(String, graphql_name='filePath')
    branch = sgqlc.types.Field(String, graphql_name='branch')
    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportType))), graphql_name='exportreportSet')
    draft_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DraftType))), graphql_name='draftSet')
    html = sgqlc.types.Field(String, graphql_name='html')
    header = sgqlc.types.Field(String, graphql_name='header')
    footer = sgqlc.types.Field(String, graphql_name='footer')


class TenantOrganizationType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('schema_name', 'id', 'name', 'is_primary', 'is_base_schema', 'industry', 'referer', 'members', 'image', 'employee_size', 'purpose_of_use', 'strobes_customer', 'account_details', 'billing_address', 'revenue', 'country', 'datacenter', 'managed_by', 'is_certin_required', 'created', 'updated', 'tenant_organization', 'organizationmember_set', 'asset_set', 'group_set', 'servicelevelagreementcustomrules_set', 'team_set', 'prioritizationrules_set', 'priorityruleset_set', 'port_set', 'subscribed_org', 'engagements_set', 'engagementsfield_set', 'softwarepackages_set', 'api_set', 'vault_set', 'prerequisites_organization', 'assetfield_set', 'dataretentionsettings_set', 'workbook_set', 'sheet_set', 'selfmanagedservicecategory_set', 'selfmanagedservice_set', 'prefills_set', 'customassessmentstatus_set', 'configuration_organization', 'export_org', 'report_attachment_org', 'tracking_rules_organization', 'credential_manager_org', 'bottask_organization', 'preset_organization', 'organization', 'agent_document_organization', 'bug_set', 'trackers_set', 'filterviews_set', 'reporttemplates_set', 'bugfield_set', 'patch_set', 'draft_set', 'allpossibleduplicates_set', 'pulse_threads', 'dashboards_set', 'widget_set', 'dashboardtags_set', 'asset_relationships', 'domain', 'is_verified')
    schema_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='schemaName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrimary')
    is_base_schema = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBaseSchema')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    referer = sgqlc.types.Field(String, graphql_name='referer')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalUserType))), graphql_name='members')
    image = sgqlc.types.Field(String, graphql_name='image')
    employee_size = sgqlc.types.Field(Int, graphql_name='employeeSize')
    purpose_of_use = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='purposeOfUse')
    strobes_customer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='strobesCustomer')
    account_details = sgqlc.types.Field(String, graphql_name='accountDetails')
    billing_address = sgqlc.types.Field(String, graphql_name='billingAddress')
    revenue = sgqlc.types.Field(String, graphql_name='revenue')
    country = sgqlc.types.Field(String, graphql_name='country')
    datacenter = sgqlc.types.Field(String, graphql_name='datacenter')
    managed_by = sgqlc.types.Field(String, graphql_name='managedBy')
    is_certin_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCertinRequired')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    tenant_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TagType))), graphql_name='tenantOrganization')
    organizationmember_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationMembersType))), graphql_name='organizationmemberSet')
    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetSet')
    group_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupsType))), graphql_name='groupSet')
    servicelevelagreementcustomrules_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ServiceLevelAgreementCustomRulesType))), graphql_name='servicelevelagreementcustomrulesSet')
    team_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TeamType))), graphql_name='teamSet')
    prioritizationrules_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PrioritizationType))), graphql_name='prioritizationrulesSet')
    priorityruleset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriorityRuleSetType))), graphql_name='priorityrulesetSet')
    port_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PortType))), graphql_name='portSet')
    subscribed_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VendorType'))), graphql_name='subscribedOrg')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')
    engagementsfield_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementsFieldType))), graphql_name='engagementsfieldSet')
    softwarepackages_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PackageAssetType))), graphql_name='softwarepackagesSet')
    api_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApiType))), graphql_name='apiSet')
    vault_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='vaultSet')
    prerequisites_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesOrganization')
    assetfield_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetFieldType))), graphql_name='assetfieldSet')
    dataretentionsettings_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DataRetentionSettingsType))), graphql_name='dataretentionsettingsSet')
    workbook_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkBookType'))), graphql_name='workbookSet')
    sheet_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SheetType))), graphql_name='sheetSet')
    selfmanagedservicecategory_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SelfManagedServiceCategoryType))), graphql_name='selfmanagedservicecategorySet')
    selfmanagedservice_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SelfManagedServiceType))), graphql_name='selfmanagedserviceSet')
    prefills_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PrefillsType))), graphql_name='prefillsSet')
    customassessmentstatus_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CustomAssessmentStatusType))), graphql_name='customassessmentstatusSet')
    configuration_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationsFieldType))), graphql_name='configurationOrganization')
    export_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportType))), graphql_name='exportOrg')
    report_attachment_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportAttachmentType))), graphql_name='reportAttachmentOrg')
    tracking_rules_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TrackingRulesType'))), graphql_name='trackingRulesOrganization')
    credential_manager_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CredentialManagerDetailType))), graphql_name='credentialManagerOrg')
    bottask_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BotTaskType))), graphql_name='bottaskOrganization')
    preset_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PresetType))), graphql_name='presetOrganization')
    organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='organization')
    agent_document_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AgentDocumentType))), graphql_name='agentDocumentOrganization')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')
    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')
    filterviews_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterViewsType))), graphql_name='filterviewsSet')
    reporttemplates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TemplateType))), graphql_name='reporttemplatesSet')
    bugfield_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugFieldType))), graphql_name='bugfieldSet')
    patch_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PatchesType))), graphql_name='patchSet')
    draft_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DraftType))), graphql_name='draftSet')
    allpossibleduplicates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllPossibleDuplicatesType))), graphql_name='allpossibleduplicatesSet')
    pulse_threads = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PulseThreadType))), graphql_name='pulseThreads')
    dashboards_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='dashboardsSet')
    widget_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetSet')
    dashboardtags_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardsTagType))), graphql_name='dashboardtagsSet')
    asset_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetRelationshipType))), graphql_name='assetRelationships')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    is_verified = sgqlc.types.Field(Boolean, graphql_name='isVerified')


class TestNuclieTemplateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'error')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    error = sgqlc.types.Field(String, graphql_name='error')


class TestPipelineCodeMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('pipeline_code_output',)
    pipeline_code_output = sgqlc.types.Field('TestPipelineCodeType', graphql_name='pipelineCodeOutput')


class TestPipelineCodeType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('result', 'errors', 'success', 'possible_attributes', 'is_group_response')
    result = sgqlc.types.Field(GenericScalar, graphql_name='result')
    errors = sgqlc.types.Field(String, graphql_name='errors')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    possible_attributes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='possibleAttributes')
    is_group_response = sgqlc.types.Field(Boolean, graphql_name='isGroupResponse')


class TestsPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('TestsType'), graphql_name='objects')


class TestsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('state', 'severity', 'id', 'title', 'exploit_available', 'patch_available', 'prioritization_score', 'exposure', 'status')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')
    severity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='severity')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    exploit_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exploitAvailable')
    patch_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='patchAvailable')
    prioritization_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritizationScore')
    exposure = sgqlc.types.Field(String, graphql_name='exposure')
    status = sgqlc.types.Field(String, graphql_name='status')


class ThreadSummaryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'mode', 'status', 'participant_count', 'participants', 'message_count', 'last_message', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    mode = sgqlc.types.Field(String, graphql_name='mode')
    status = sgqlc.types.Field(String, graphql_name='status')
    participant_count = sgqlc.types.Field(Int, graphql_name='participantCount')
    participants = sgqlc.types.Field(sgqlc.types.list_of(ParticipantSummaryType), graphql_name='participants')
    message_count = sgqlc.types.Field(Int, graphql_name='messageCount')
    last_message = sgqlc.types.Field(String, graphql_name='lastMessage')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')


class ThreatAnalysisType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('active_exploits', 'percentage_change', 'complexity_breakdown', 'technology_tags', 'zero_day_count', 'zero_day_items', 'epss_percentage', 'epss_vulnerability_count', 'epss_items')
    active_exploits = sgqlc.types.Field(Int, graphql_name='activeExploits')
    percentage_change = sgqlc.types.Field(Float, graphql_name='percentageChange')
    complexity_breakdown = sgqlc.types.Field(ComplexityBreakdownType, graphql_name='complexityBreakdown')
    technology_tags = sgqlc.types.Field(sgqlc.types.list_of(TechnologyTagType), graphql_name='technologyTags')
    zero_day_count = sgqlc.types.Field(Int, graphql_name='zeroDayCount')
    zero_day_items = sgqlc.types.Field(sgqlc.types.list_of('ZeroDayItemType'), graphql_name='zeroDayItems')
    epss_percentage = sgqlc.types.Field(Float, graphql_name='epssPercentage')
    epss_vulnerability_count = sgqlc.types.Field(Int, graphql_name='epssVulnerabilityCount')
    epss_items = sgqlc.types.Field(sgqlc.types.list_of(EPSSHighRiskItemType), graphql_name='epssItems')


class TicketType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'received_from', 'ticket_id', 'ticket_url', 'title', 'severity', 'state', 'team_included', 'last_sync', 'reported_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    received_from = sgqlc.types.Field(String, graphql_name='receivedFrom')
    ticket_id = sgqlc.types.Field(String, graphql_name='ticketId')
    ticket_url = sgqlc.types.Field(String, graphql_name='ticketUrl')
    title = sgqlc.types.Field(String, graphql_name='title')
    severity = sgqlc.types.Field(Int, graphql_name='severity')
    state = sgqlc.types.Field(Int, graphql_name='state')
    team_included = sgqlc.types.Field(sgqlc.types.list_of('UserType'), graphql_name='teamIncluded')
    last_sync = sgqlc.types.Field(Date, graphql_name='lastSync')
    reported_date = sgqlc.types.Field(Date, graphql_name='reportedDate')


class TicketsPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(TicketType), graphql_name='objects')


class TopVulnerabilitiesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('vulnerabilities',)
    vulnerabilities = sgqlc.types.Field(sgqlc.types.list_of('VulnerabilityItemType'), graphql_name='vulnerabilities')


class TrackersType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'config', 'url', 'issue_key', 'bug', 'organization', 'asset', 'patch', 'is_groupped_issues', 'grouped_by', 'last_log', 'assignees_list', 'tracker_slug', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    config = sgqlc.types.Field(ConfigurationsFieldType, graphql_name='config')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    issue_key = sgqlc.types.Field(String, graphql_name='issueKey')
    bug = sgqlc.types.Field(TestsType, graphql_name='bug')
    organization = sgqlc.types.Field(TenantOrganizationType, graphql_name='organization')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    patch = sgqlc.types.Field(PatchesType, graphql_name='patch')
    is_groupped_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGrouppedIssues')
    grouped_by = sgqlc.types.Field(String, graphql_name='groupedBy')
    last_log = sgqlc.types.Field(String, graphql_name='lastLog')
    assignees_list = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='assigneesList')
    tracker_slug = sgqlc.types.Field(String, graphql_name='trackerSlug')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')


class TrackingRulesType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'search_qs_list', 'overwrite_existing_issues', 'log_groupped_issues', 'custom_title', 'custom_state', 'custom_severity', 'custom_description_template', 'custom_title_template', 'group_by', 'assignees_list', 'labels_list', 'organization', 'app_automationworkflows_tracking_rules')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    search_qs_list = sgqlc.types.Field(JSONString, graphql_name='searchQsList')
    overwrite_existing_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='overwriteExistingIssues')
    log_groupped_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='logGrouppedIssues')
    custom_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customTitle')
    custom_state = sgqlc.types.Field(Int, graphql_name='customState')
    custom_severity = sgqlc.types.Field(Int, graphql_name='customSeverity')
    custom_description_template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customDescriptionTemplate')
    custom_title_template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customTitleTemplate')
    group_by = sgqlc.types.Field(String, graphql_name='groupBy')
    assignees_list = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='assigneesList')
    labels_list = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='labelsList')
    organization = sgqlc.types.Field(TenantOrganizationType, graphql_name='organization')
    app_automationworkflows_tracking_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='appAutomationworkflowsTrackingRules')


class TransferEngagementBugMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class TrendDataPointType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date', 'value', 'group')
    date = sgqlc.types.Field(String, graphql_name='date')
    value = sgqlc.types.Field(Float, graphql_name='value')
    group = sgqlc.types.Field(String, graphql_name='group')


class TriggerAutomationWorkflowMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('automation_workflow',)
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')


class UpdateASMSettingsMutations(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('settings',)
    settings = sgqlc.types.Field(ASMSettingsType, graphql_name='settings')


class UpdateAssessmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assessment',)
    assessment = sgqlc.types.Field(sgqlc.types.list_of(AssessmentType), graphql_name='assessment')


class UpdateAssetFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset_field',)
    asset_field = sgqlc.types.Field(AssetFieldType, graphql_name='assetField')


class UpdateAssetRelationship(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('asset_relationship', 'success', 'message')
    asset_relationship = sgqlc.types.Field(sgqlc.types.list_of(AssetRelationshipType), graphql_name='assetRelationship')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateAutomationWorkflowMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('automation_workflow',)
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')


class UpdateBugFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug_field',)
    bug_field = sgqlc.types.Field(BugFieldType, graphql_name='bugField')


class UpdateCommentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('comments',)
    comments = sgqlc.types.Field(sgqlc.types.list_of(CommentType), graphql_name='comments')


class UpdateCredentialManagerState(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('credential_manager',)
    credential_manager = sgqlc.types.Field(sgqlc.types.list_of(CredentialManagerDetailType), graphql_name='credentialManager')


class UpdateCustomAssessmentStatusMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('custom_assessment_status',)
    custom_assessment_status = sgqlc.types.Field(CustomAssessmentStatusType, graphql_name='customAssessmentStatus')


class UpdateDashboardMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dashboard',)
    dashboard = sgqlc.types.Field(sgqlc.types.list_of(DashboardType), graphql_name='dashboard')


class UpdateDataRetentionSettingMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('data_retention',)
    data_retention = sgqlc.types.Field(sgqlc.types.list_of(DataRetentionSettingsType), graphql_name='dataRetention')


class UpdateEngagementFieldSettingsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagement_field',)
    engagement_field = sgqlc.types.Field(EngagementsFieldType, graphql_name='engagementField')


class UpdateEngagementMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('engagement',)
    engagement = sgqlc.types.Field(sgqlc.types.list_of(EngagementType), graphql_name='engagement')


class UpdateGroupMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups',)
    groups = sgqlc.types.Field(sgqlc.types.list_of(GroupsType), graphql_name='groups')


class UpdatePresetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('presets',)
    presets = sgqlc.types.Field(sgqlc.types.list_of(PresetType), graphql_name='presets')


class UpdatePrioritizationSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdatePriorityRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rule',)
    rule = sgqlc.types.Field(PriorityRuleType, graphql_name='rule')


class UpdatePriorityRuleSet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rule_set',)
    rule_set = sgqlc.types.Field(PriorityRuleSetType, graphql_name='ruleSet')


class UpdateReportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('reports',)
    reports = sgqlc.types.Field(String, graphql_name='reports')


class UpdateRiskRecordsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')


class UpdateSLARuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sla_rule', 'bug_count')
    sla_rule = sgqlc.types.Field(ServiceLevelAgreementCustomRulesType, graphql_name='slaRule')
    bug_count = sgqlc.types.Field(BugsCountType, graphql_name='bugCount')


class UpdateSelfManagedServiceMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('service',)
    service = sgqlc.types.Field(SelfManagedServiceType, graphql_name='service')


class UpdateTemplateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field(TemplateType, graphql_name='templates')


class UpdateWidgetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('widgets',)
    widgets = sgqlc.types.Field(sgqlc.types.list_of('WidgetV2Type'), graphql_name='widgets')


class UserPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('UserType'), graphql_name='objects')


class UserType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('password', 'is_superuser', 'id', 'email', 'first_name', 'last_name', 'created', 'updated', 'is_superadmin', 'is_staff', 'is_ai_agent', 'is_active', 'activation_id', 'bio', 'profile_picture', 'cover_heading', 'linkedin_url', 'twitter_url', 'designation', 'phone_number', 'last_login', 'username', 'org_members', 'organizationmember_set', 'asset_set', 'group_set', 'created_priority_rule_sets', 'engagements_set', 'engagement_assignees', 'assessment_asset_assigned_to', 'vault_set', 'prerequisites_assigned_to', 'prerequisites_user', 'workbook_set', 'sheet_set', 'sheetrow_set', 'prefills_set', 'configurations_set', 'scanlog_set', 'exportreport_set', 'reportattachment_set', 'credentialmanager_set', 'bottask_set', 'automationworkflows_set', 'agentdocument_set', 'assigned_to', 'reported_by', 'attachment_set', 'activity_set', 'comment_set', 'filterviews_set', 'views_members', 'reporttemplates_set', 'draft_set', 'pulse_threads', 'dashboards_set', 'widget_set', 'created_asset_relationships')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    is_superuser = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperuser')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    is_superadmin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperadmin')
    is_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStaff')
    is_ai_agent = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAiAgent')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    activation_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='activationId')
    bio = sgqlc.types.Field(String, graphql_name='bio')
    profile_picture = sgqlc.types.Field(String, graphql_name='profilePicture')
    cover_heading = sgqlc.types.Field(String, graphql_name='coverHeading')
    linkedin_url = sgqlc.types.Field(String, graphql_name='linkedinUrl')
    twitter_url = sgqlc.types.Field(String, graphql_name='twitterUrl')
    designation = sgqlc.types.Field(String, graphql_name='designation')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    last_login = sgqlc.types.Field(DateTime, graphql_name='lastLogin')
    username = sgqlc.types.Field(String, graphql_name='username')
    org_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TenantOrganizationType))), graphql_name='orgMembers')
    organizationmember_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationMembersType))), graphql_name='organizationmemberSet')
    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetSet')
    group_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupsType))), graphql_name='groupSet')
    created_priority_rule_sets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriorityRuleSetType))), graphql_name='createdPriorityRuleSets')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')
    engagement_assignees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementAssignees')
    assessment_asset_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='assessmentAssetAssignedTo')
    vault_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='vaultSet')
    prerequisites_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesAssignedTo')
    prerequisites_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesUser')
    workbook_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkBookType'))), graphql_name='workbookSet')
    sheet_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SheetType))), graphql_name='sheetSet')
    sheetrow_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SheetRowType))), graphql_name='sheetrowSet')
    prefills_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PrefillsType))), graphql_name='prefillsSet')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationsFieldType))), graphql_name='configurationsSet')
    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='scanlogSet')
    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportType))), graphql_name='exportreportSet')
    reportattachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportAttachmentType))), graphql_name='reportattachmentSet')
    credentialmanager_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CredentialManagerDetailType))), graphql_name='credentialmanagerSet')
    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BotTaskType))), graphql_name='bottaskSet')
    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='automationworkflowsSet')
    agentdocument_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AgentDocumentType))), graphql_name='agentdocumentSet')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TestsType))), graphql_name='assignedTo')
    reported_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TestsType))), graphql_name='reportedBy')
    attachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentType))), graphql_name='attachmentSet')
    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementActivityType))), graphql_name='activitySet')
    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementCommentType))), graphql_name='commentSet')
    filterviews_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterViewsType))), graphql_name='filterviewsSet')
    views_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterViewsType))), graphql_name='viewsMembers')
    reporttemplates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TemplateType))), graphql_name='reporttemplatesSet')
    draft_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DraftType))), graphql_name='draftSet')
    pulse_threads = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PulseThreadType))), graphql_name='pulseThreads')
    dashboards_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='dashboardsSet')
    widget_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetSet')
    created_asset_relationships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetRelationshipType))), graphql_name='createdAssetRelationships')


class VaultPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('VaultType'), graphql_name='objects')


class VaultType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'document', 'document_name', 'document_size', 'organization', 'attached_by', 'created', 'updated', 'document_vault', 'prerequisites_attachments', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    document = sgqlc.types.Field(String, graphql_name='document')
    document_name = sgqlc.types.Field(String, graphql_name='documentName')
    document_size = sgqlc.types.Field(Int, graphql_name='documentSize')
    organization = sgqlc.types.Field(TenantOrganizationType, graphql_name='organization')
    attached_by = sgqlc.types.Field(ApprovalUserType, graphql_name='attachedBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    document_vault = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='documentVault')
    prerequisites_attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesAttachments')
    url = sgqlc.types.Field(String, graphql_name='url')


class VendorType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'vendor_code', 'organization', 'bio', 'cover_heading', 'linkedin_url', 'twitter_url', 'created', 'updated', 'vendor_team', 'engagements_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    vendor_code = sgqlc.types.Field(String, graphql_name='vendorCode')
    organization = sgqlc.types.Field(TenantOrganizationType, graphql_name='organization')
    bio = sgqlc.types.Field(String, graphql_name='bio')
    cover_heading = sgqlc.types.Field(String, graphql_name='coverHeading')
    linkedin_url = sgqlc.types.Field(String, graphql_name='linkedinUrl')
    twitter_url = sgqlc.types.Field(String, graphql_name='twitterUrl')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    vendor_team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TeamType))), graphql_name='vendorTeam')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')


class VeracodeProjectsType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'guid')
    name = sgqlc.types.Field(String, graphql_name='name')
    guid = sgqlc.types.Field(String, graphql_name='guid')


class VeracodeProjectsTypePaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(VeracodeProjectsType), graphql_name='objects')


class VulnerabilityItemType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'severity', 'asset_count', 'age')
    name = sgqlc.types.Field(String, graphql_name='name')
    severity = sgqlc.types.Field(String, graphql_name='severity')
    asset_count = sgqlc.types.Field(Int, graphql_name='assetCount')
    age = sgqlc.types.Field(String, graphql_name='age')


class WidgetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('result',)
    result = sgqlc.types.Field(GenericScalar, graphql_name='result')


class WidgetV2Type(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'slug', 'description', 'is_default', 'tags', 'data', 'positional_data', 'organization', 'created_by', 'cloned_from', 'created', 'widgets', 'self_cloned_from', 'result')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    data = sgqlc.types.Field(GenericScalar, graphql_name='data')
    positional_data = sgqlc.types.Field(JSONString, graphql_name='positionalData')
    organization = sgqlc.types.Field(TenantOrganizationType, graphql_name='organization')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    cloned_from = sgqlc.types.Field('WidgetV2Type', graphql_name='clonedFrom')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    widgets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='widgets')
    self_cloned_from = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='selfClonedFrom')
    result = sgqlc.types.Field(GenericScalar, graphql_name='result')


class WidgetsV2Type(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of(WidgetV2Type), graphql_name='objects')


class WorkBookCreateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('work_book',)
    work_book = sgqlc.types.Field('WorkBookType', graphql_name='workBook')


class WorkBookDeleteMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('work_book', 'message')
    work_book = sgqlc.types.Field('WorkBookType', graphql_name='workBook')
    message = sgqlc.types.Field(String, graphql_name='message')


class WorkBookPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('WorkBookType'), graphql_name='objects')


class WorkBookType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'engagements', 'created', 'updated', 'created_by', 'sheets')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization = sgqlc.types.Field(sgqlc.types.non_null(TenantOrganizationType), graphql_name='organization')
    engagements = sgqlc.types.Field(sgqlc.types.list_of(EngagementType), graphql_name='engagements')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')
    sheets = sgqlc.types.Field(sgqlc.types.list_of(SheetType), graphql_name='sheets')


class WorkBookUpdateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('work_book',)
    work_book = sgqlc.types.Field(WorkBookType, graphql_name='workBook')


class ZeroDayItemType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cve_id', 'title', 'severity', 'is_mitigated', 'has_patch')
    cve_id = sgqlc.types.Field(String, graphql_name='cveId')
    title = sgqlc.types.Field(String, graphql_name='title')
    severity = sgqlc.types.Field(Int, graphql_name='severity')
    is_mitigated = sgqlc.types.Field(Boolean, graphql_name='isMitigated')
    has_patch = sgqlc.types.Field(Boolean, graphql_name='hasPatch')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

