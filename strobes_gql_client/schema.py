import sgqlc.types
import sgqlc.types.datetime


schema = sgqlc.types.Schema()


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
class AppCredentialManagerTypeChoices(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ANCHORE_CM`: anchore_cm
    * `APPKNOX_CM`: appknox_cm
    * `APP_SCAN_CM`: app_scan_cm
    * `APP_SENTINELS_CM`: app_sentinels_cm
    * `AWS_CM`: aws_cm
    * `AZURE_CM`: azure_cm
    * `AZURE_DEVOPS_CM`: azure_devops_cm
    * `BITBUCKET_CM`: bitbucket_cm
    * `BLACKDUCK_CM`: blackduck_cm
    * `BUGZILLA_CM`: bugzilla_cm
    * `BURPSUITE_CM`: burpsuite_cm
    * `BURP_ENTERPRISE_CM`: burp_enterprise_cm
    * `DOCKER_CM`: docker_cm
    * `ECR_CM`: ecr_cm
    * `FORTIFY_CM`: fortify_cm
    * `GITHUB_CM`: github_cm
    * `GIT_CM`: git_cm
    * `HACKERONE_CM`: hackerone_cm
    * `INSIGHT_PLATFORM_API_CM`: insight_platform_api_cm
    * `INSIGHT_VM_CM`: insight_vm_cm
    * `INTEL_GRAPH_CM`: intel_graph_cm
    * `JFROG_XRAY_CM`: jfrog_xray_cm
    * `JIRA_CM`: jira_cm
    * `NESSUS_CM`: nessus_cm
    * `NEXPOSE_CM`: nexpose_cm
    * `OPEN_AI_CM`: open_ai_cm
    * `PALO_ALTO_XPANSE_CM`: palo_alto_xpanse_cm
    * `PRISMA_CLOUD_CM`: prisma_cloud_cm
    * `QUALYS_CM`: qualys_cm
    * `SMTP_CM`: smtp_cm
    * `SNYK_CM`: snyk_cm
    * `SONAR_CLOUD_CM`: sonar_cloud_cm
    * `SONAR_CM`: sonar_cm
    * `SONATYPE_NEXUS_CM`: sonatype_nexus_cm
    * `SVN_CM`: svn_cm
    * `TANIUM_CM`: tanium_cm
    * `TENABLEIO_CM`: tenableio_cm
    * `TENABLESC_CM`: tenablesc_cm
    * `VERACODE_CM`: veracode_cm
    * `WIZ_CM`: wiz_cm
    '''
    __schema__ = schema
    __choices__ = ('ANCHORE_CM', 'APPKNOX_CM', 'APP_SCAN_CM', 'APP_SENTINELS_CM', 'AWS_CM', 'AZURE_CM', 'AZURE_DEVOPS_CM', 'BITBUCKET_CM', 'BLACKDUCK_CM', 'BUGZILLA_CM', 'BURPSUITE_CM', 'BURP_ENTERPRISE_CM', 'DOCKER_CM', 'ECR_CM', 'FORTIFY_CM', 'GITHUB_CM', 'GIT_CM', 'HACKERONE_CM', 'INSIGHT_PLATFORM_API_CM', 'INSIGHT_VM_CM', 'INTEL_GRAPH_CM', 'JFROG_XRAY_CM', 'JIRA_CM', 'NESSUS_CM', 'NEXPOSE_CM', 'OPEN_AI_CM', 'PALO_ALTO_XPANSE_CM', 'PRISMA_CLOUD_CM', 'QUALYS_CM', 'SMTP_CM', 'SNYK_CM', 'SONAR_CLOUD_CM', 'SONAR_CM', 'SONATYPE_NEXUS_CM', 'SVN_CM', 'TANIUM_CM', 'TENABLEIO_CM', 'TENABLESC_CM', 'VERACODE_CM', 'WIZ_CM')


class AppPatchPatchTypeChoices(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `A_1`: Software Package
    '''
    __schema__ = schema
    __choices__ = ('A_1',)


class AppPortStateChoices(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CLOSED`: CLOSED
    * `FILTERED`: FILTERED
    * `NOTDEFINED`: NOTDEFINED
    * `OPEN`: OPEN
    * `OPEN_OR_FILTERED`: OPEN_OR_FILTERED
    * `UNFILTERED`: UNFILTERED
    '''
    __schema__ = schema
    __choices__ = ('CLOSED', 'FILTERED', 'NOTDEFINED', 'OPEN', 'OPEN_OR_FILTERED', 'UNFILTERED')


Boolean = sgqlc.types.Boolean

Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

class GenericScalar(sgqlc.types.Scalar):
    '''The `GenericScalar` scalar type represents a generic GraphQL
    scalar value that could be: String, Boolean, Int, Float, List or
    Object.
    '''
    __schema__ = schema


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSONString(sgqlc.types.Scalar):
    '''Allows use of a JSON String for input / output from the GraphQL
    schema.  Use of this type is *not recommended* as you lose the
    benefits of having a defined, static schema (one of the key
    benefits of GraphQL).
    '''
    __schema__ = schema


String = sgqlc.types.String

class TenantCVESourceChoices(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `INTEL_GRAPH`: intel_graph
    * `XO_INTEL`: xo_intel
    '''
    __schema__ = schema
    __choices__ = ('INTEL_GRAPH', 'XO_INTEL')


class TenantCVETrendChoices(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `A_1`: Low
    * `A_2`: Medium
    * `A_3`: High
    * `A_4`: Ultra
    * `A_5`: Extreme
    '''
    __schema__ = schema
    __choices__ = ('A_1', 'A_2', 'A_3', 'A_4', 'A_5')


class UUID(sgqlc.types.Scalar):
    '''Leverages the internal Python implementation of UUID (uuid.UUID)
    to provide native UUID objects in fields, resolvers and input.
    '''
    __schema__ = schema


class Upload(sgqlc.types.Scalar):
    '''Create scalar that ignores normal serialization/deserialization,
    since that will be handled by the multipart request spec
    '''
    __schema__ = schema



########################################################################
# Input Objects
########################################################################

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

    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='tags')

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
    __field_names__ = ('id', 'action', 'data', 'user', 'team', 'bug', 'asset', 'connector_config', 'engagement', 'connector', 'credential_manager', 'task', 'approval', 'is_automation_activity', 'automation_workflow', 'automation_workflow_reason', 'created', 'updated', 'comment_set')
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

    credential_manager = sgqlc.types.Field('CredentialManagerType', graphql_name='credentialManager')

    task = sgqlc.types.Field('AllScanLogType', graphql_name='task')

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



class AddTemplateMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field('TemplateType', graphql_name='templates')



class AddVaultAttachmentMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('vault',)
    vault = sgqlc.types.Field('VaultType', graphql_name='vault')



class AllScanLogType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'task_id', 'config', 'finished', 'created_by', 'type', 'is_triangulum_scanner', 'task_retry_count', 'triangulum_task_finished', 'scanner_task_id', 'build_status', 'is_scheduled', 'external_scheduled_task', 'bugs', 'extra_data', 'scan_arguments', 'assets', 'temp_file', 'logs', 'error_code', 'bug_stats', 'merge_data', 'scan_filter_data', 'status', 'artifacts_file_paths', 'child_tasks', 'is_child_task', 'started', 'asset_set', 'last_seen', 'exportreport_set', 'bottask_set', 'bug_set', 'rediscovered_finding', 'activity_task', 'asset', 'organization_id', 'connector_name', 'connector_slug')
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
    __field_names__ = ('password', 'is_superuser', 'id', 'email', 'first_name', 'last_name', 'created', 'updated', 'is_superadmin', 'is_staff', 'is_active', 'activation_id', 'bio', 'profile_picture', 'cover_heading', 'linkedin_url', 'twitter_url', 'designation', 'phone_number', 'last_login', 'username', 'org_members', 'organizationmember_set', 'asset_set', 'group_set', 'engagements_set', 'assessment_asset_assigned_to', 'vault_set', 'prerequisites_assigned_to', 'prerequisites_user', 'configurations_set', 'scanlog_set', 'exportreport_set', 'reportattachment_set', 'credentialmanager_set', 'bottask_set', 'automationworkflows_set', 'assigned_to', 'reported_by', 'attachment_set', 'activity_set', 'comment_set', 'filterviews_set', 'views_members', 'reporttemplates_set', 'profile_picture_url')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')

    is_superuser = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperuser')
    '''Designates that this user has all permissions without explicitly
    assigning them.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')

    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

    is_superadmin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperadmin')

    is_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStaff')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    '''Designates whether this user should be treated as active. Un-
    select this instead of deleting accounts.
    '''

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

    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementType'))), graphql_name='engagementsSet')

    assessment_asset_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssessmentType'))), graphql_name='assessmentAssetAssignedTo')

    vault_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='vaultSet')

    prerequisites_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PreRequisitesType'))), graphql_name='prerequisitesAssignedTo')

    prerequisites_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PreRequisitesType'))), graphql_name='prerequisitesUser')

    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationsSet')

    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='scanlogSet')

    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='exportreportSet')

    reportattachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportAttachmentType'))), graphql_name='reportattachmentSet')

    credentialmanager_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CredentialManagerType'))), graphql_name='credentialmanagerSet')

    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BotTaskType'))), graphql_name='bottaskSet')

    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AutomationWorkflowType'))), graphql_name='automationworkflowsSet')

    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='assignedTo')

    reported_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='reportedBy')

    attachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentType'))), graphql_name='attachmentSet')

    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')

    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')

    filterviews_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FilterViewsType'))), graphql_name='filterviewsSet')

    views_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FilterViewsType'))), graphql_name='viewsMembers')

    reporttemplates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TemplateType'))), graphql_name='reporttemplatesSet')

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
    __field_names__ = ('id', 'service', 'package', 'engagement', 'asset', 'state', 'scope', 'instructions', 'test_accounts', 'vpn_accounts', 'assigned_to', 'scheduled_date', 'delivery_date', 'total_hours_spent', 'assessment_category', 'created', 'updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    service = sgqlc.types.Field(String, graphql_name='service')

    package = sgqlc.types.Field(String, graphql_name='package')

    engagement = sgqlc.types.Field(sgqlc.types.non_null('EngagementType'), graphql_name='engagement')

    asset = sgqlc.types.Field(sgqlc.types.non_null('AssetType'), graphql_name='asset')

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
    __field_names__ = ('id', 'name', 'slug', 'description', 'field_type', 'options', 'is_required', 'is_active', 'extra_data', 'created', 'updated', 'organization')
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



class AssetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'target', 'exposed', 'type', 'cloud_type', 'organization', 'disabled', 'sensitivity', 'keys', 'data', 'created_by', 'linked_assets', 'additional_info', 'scan', 'last_seen', 'temp_id', 'is_active', 'created', 'updated', 'tags', 'location', 'scanner_raw_response', 'region', 'resource_id', 'account_id', 'fields', 'asset_region', 'dns_info', 'whois_info', 'asn', 'waf', 'cdn', 'asm_last_alive', 'connector', 'other_connectors', 'linked_to', 'group_assets', 'asset_port', 'assessments_set', 'asset_package', 'configuration_asset', 'bug_set', 'activity_set', 'trackers_set', 'patch_set', 'ipaddress', 'hostname', 'mac_address', 'os', 'cpe', 'risk_score', 'dns_a', 'dns_ns', 'dns_soa', 'dns_aaaa', 'dns_axfr', 'dns_cname', 'domain_org', 'domain_city', 'domain_state', 'domain_dnssec', 'domain_emails', 'domain_status', 'domain_address', 'domain_country', 'domain_registrar', 'domain_name', 'domain_name_servers', 'domain_referral_url', 'domain_updated_date', 'domain_server', 'domain_expiration_date', 'domain_creation_date', 'domain_registrant_postal_code', 'port_addresses', 'package_count', 'webserver', 'technology_used')
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

    configuration_asset = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationAsset')

    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')

    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')

    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')

    patch_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PatchesType'))), graphql_name='patchSet')

    ipaddress = sgqlc.types.Field(String, graphql_name='ipaddress')

    hostname = sgqlc.types.Field(String, graphql_name='hostname')

    mac_address = sgqlc.types.Field(String, graphql_name='macAddress')

    os = sgqlc.types.Field(String, graphql_name='os')

    cpe = sgqlc.types.Field(String, graphql_name='cpe')

    risk_score = sgqlc.types.Field(Float, graphql_name='riskScore')

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
    __field_names__ = ('id', 'name', 'target', 'exposed', 'type', 'cloud_type', 'organization', 'disabled', 'sensitivity', 'keys', 'data', 'created_by', 'linked_assets', 'additional_info', 'scan', 'last_seen', 'temp_id', 'is_active', 'created', 'updated', 'tags', 'location', 'scanner_raw_response', 'region', 'resource_id', 'account_id', 'fields', 'asset_region', 'dns_info', 'whois_info', 'asn', 'waf', 'cdn', 'asm_last_alive', 'connector', 'other_connectors', 'linked_to', 'group_assets', 'asset_port', 'assessments_set', 'asset_package', 'configuration_asset', 'bug_set', 'activity_set', 'trackers_set', 'patch_set', 'ipaddress', 'hostname', 'mac_address', 'total', 'open', 'closed', 'new', 'active', 'resolved', 'not_applicable', 'risk_score', 'info_open', 'info_closed', 'low_open', 'low_closed', 'medium_open', 'medium_closed', 'high_open', 'high_closed', 'critical_open', 'critical_closed')
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

    configuration_asset = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationsFieldType'))), graphql_name='configurationAsset')

    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')

    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')

    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')

    patch_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PatchesType'))), graphql_name='patchSet')

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



class AssignAssetViewToUsersMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('views',)
    views = sgqlc.types.Field('FilterViewsType', graphql_name='views')



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
    __field_names__ = ('id', 'name', 'role', 'tool', 'module', 'search_query', 'instructions', 'weightage', 'ignore_weightage', 'organization', 'credential_manager', 'llm_model', 'created_by', 'hooks', 'triggers', 'agent_avatar', 'created', 'updated', 'activity_set', 'comment_set', 'avatar')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    role = sgqlc.types.Field(String, graphql_name='role')

    tool = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tool')

    module = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='module')

    search_query = sgqlc.types.Field(String, graphql_name='searchQuery')

    instructions = sgqlc.types.Field(String, graphql_name='instructions')

    weightage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightage')

    ignore_weightage = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='ignoreWeightage')

    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')

    credential_manager = sgqlc.types.Field('CredentialManagerType', graphql_name='credentialManager')

    llm_model = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='llmModel')

    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')

    hooks = sgqlc.types.Field(GenericScalar, graphql_name='hooks')

    triggers = sgqlc.types.Field(GenericScalar, graphql_name='triggers')

    agent_avatar = sgqlc.types.Field(String, graphql_name='agentAvatar')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

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
    __field_names__ = ('id', 'type', 'task_id', 'config', 'extra_data', 'status', 'started', 'finished', 'initiated_by', 'total_findings_closed', 'config_name', 'connector')
    id = sgqlc.types.Field(Int, graphql_name='id')

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')

    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')

    config = sgqlc.types.Field('ConfigurationsFieldType', graphql_name='config')

    extra_data = sgqlc.types.Field(GenericScalar, graphql_name='extraData')

    status = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='status')

    started = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='started')

    finished = sgqlc.types.Field(DateTime, graphql_name='finished')

    initiated_by = sgqlc.types.Field(ApprovalUserType, graphql_name='initiatedBy')

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
    __field_names__ = ('id', 'name', 'slug', 'description', 'field_type', 'options', 'is_required', 'is_active', 'extra_data', 'created', 'updated', 'organization')
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



class BugType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('state', 'severity', 'bug_level', 'alert_category', 'id', 'title', 'description', 'mitigation', 'steps_to_reproduce', 'object_id', 'hash', 'duplicate', 'cwe', 'cve', 'cvss', 'attack_vector', 'bug_tags', 'bug_references', 'assigned_to', 'organization', 'asset', 'team', 'reported_by', 'due_date', 'sla_violated', 'has_user_defined_due_date', 'exploit_available', 'exploit_info', 'patch_available', 'patch_info', 'prioritization_score', 'prioritization_score_calculated', 'drill_down_score', 'bug_attachments', 'connector', 'configuration_name', 'connector_config', 'scan', 'other_scans', 'scanner_raw_response', 'scan_raw_response', 'batch_id', 'temp_id', 'vulnerable_since', 'engagements', 'priority_last_updated', 'zero_day_available', 'is_wormable', 'trend', 'advisories_seen', 'epss_score', 'cisa_due_date', 'nist', 'owasp', 'records_at_risk', 'records_type', 'fields', 'links', 'asm_last_updated', 'is_misconfiguration', 'sla_rule_search_query', 'created', 'updated', 'is_active', 'is_alert', 'patch', 'smart_close', 'is_reopened', 'last_smart_closed_on', 'last_reopened_on', 'original_bug', 'attachment_set', 'activity_set', 'comment_set', 'bug_tracker', 'approval_finding', 'ipaddress', 'hostname', 'mac_address', 'os', 'tracker', 'last_resolved_on', 'cost_of_risk', 'port', 'duplicate_instances', 'content_object', 'references', 'config_content_object')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')

    severity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='severity')

    bug_level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bugLevel')

    alert_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='alertCategory')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    mitigation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mitigation')

    steps_to_reproduce = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stepsToReproduce')

    object_id = sgqlc.types.Field(Int, graphql_name='objectId')

    hash = sgqlc.types.Field(String, graphql_name='hash')

    duplicate = sgqlc.types.Field('TestsType', graphql_name='duplicate')

    cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CWEType'))), graphql_name='cwe')

    cve = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CVEType'))), graphql_name='cve')

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



class BulkDeleteGroupMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups',)
    groups = sgqlc.types.Field(sgqlc.types.list_of('GroupsType'), graphql_name='groups')



class BulkDeleteOrgMemberRoleMutation(sgqlc.types.Type):
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
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')



class BulkUpdateBugCWEMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')



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



class BulkUpdateMemberAssetAccessMutation(sgqlc.types.Type):
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



class CloneDefaultWidgetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('widget', 'graph_data')
    widget = sgqlc.types.Field('WidgetV2Type', graphql_name='widget')

    graph_data = sgqlc.types.Field(GenericScalar, graphql_name='graphData')



class CloseFindingType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('result',)
    result = sgqlc.types.Field(GenericScalar, graphql_name='result')



class CommentType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'comment', 'bug', 'attachments', 'internal', 'activity', 'commented_by', 'connector_config', 'connector', 'team', 'approval', 'engagement', 'automation_workflow', 'automation_workflow_reason', 'created', 'updated', 'comment_id', 'organization_id', 'bug_id', 'engagement_id')
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

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

    comment_id = sgqlc.types.Field(UUID, graphql_name='commentId')

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')

    bug_id = sgqlc.types.Field(UUID, graphql_name='bugId')

    engagement_id = sgqlc.types.Field(UUID, graphql_name='engagementId')



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
    __field_names__ = ('id', 'name', 'connector', 'organization', 'asset', 'team', 'object_id', 'key', 'remote_access_id', 'remote_access_url', 'created_by', 'is_default', 'created', 'updated', 'extra', 'triangulum', 'is_automated', 'auto_close_findings', 'auto_smart_merge_assets', 'send_csv_report_with_summary', 'enable_github_webhook', 'github_webhook_triggers', 'configurations_set', 'scanlog_set', 'bottask_set', 'bug_set', 'activity_set', 'comment_set', 'tracker_configs')
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

    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')

    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementActivityType'))), graphql_name='activitySet')

    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementCommentType'))), graphql_name='commentSet')

    tracker_configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackerConfigs')



class ConfigurationsFieldType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'connector', 'organization', 'asset', 'team', 'object_id', 'key', 'remote_access_id', 'remote_access_url', 'created_by', 'is_default', 'created', 'updated', 'extra', 'triangulum', 'is_automated', 'auto_close_findings', 'auto_smart_merge_assets', 'send_csv_report_with_summary', 'enable_github_webhook', 'github_webhook_triggers', 'configurations_set', 'scanlog_set', 'bottask_set', 'bug_set', 'activity_set', 'comment_set', 'tracker_configs')
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



class CreateAutomationWorkflowMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('automation_workflow',)
    automation_workflow = sgqlc.types.Field(AutomationWorkflowType, graphql_name='automationWorkflow')



class CreateBugMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bug',)
    bug = sgqlc.types.Field(BugType, graphql_name='bug')



class CreateDashboardMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dashboard',)
    dashboard = sgqlc.types.Field('DashboardType', graphql_name='dashboard')



class CreateEngagementMutation(sgqlc.types.Type):
    '''Engagement create graphene mutation'''
    __schema__ = schema
    __field_names__ = ('engagement',)
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')



class CreateSLARuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sla_rule',)
    sla_rule = sgqlc.types.Field('ServiceLevelAgreementCustomRulesType', graphql_name='slaRule')



class CreateSoftwarePackageMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('packages',)
    packages = sgqlc.types.Field(sgqlc.types.list_of('SoftwarePackageType'), graphql_name='packages')



class CreateWidgetMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('widget', 'graph_data')
    widget = sgqlc.types.Field('WidgetV2Type', graphql_name='widget')

    graph_data = sgqlc.types.Field(GenericScalar, graphql_name='graphData')



class CredentialManagerType(sgqlc.types.Type):
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



class DashboardExportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('json_data',)
    json_data = sgqlc.types.Field(String, graphql_name='jsonData')



class DashboardImportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dashboard',)
    dashboard = sgqlc.types.Field('DashboardType', graphql_name='dashboard')



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

    created_by = sgqlc.types.Field('OrganizationMembersType', graphql_name='createdBy')

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



class DeleteSLARuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'bug_count')
    success = sgqlc.types.Field(Boolean, graphql_name='success')

    bug_count = sgqlc.types.Field(BugsCountType, graphql_name='bugCount')



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
    __field_names__ = ('id', 'action', 'data', 'user', 'team', 'bug', 'asset', 'connector_config', 'engagement', 'connector', 'credential_manager', 'task', 'approval', 'is_automation_activity', 'automation_workflow', 'automation_workflow_reason', 'created', 'updated', 'comment_set')
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

    credential_manager = sgqlc.types.Field(CredentialManagerType, graphql_name='credentialManager')

    task = sgqlc.types.Field(AllScanLogType, graphql_name='task')

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
    __field_names__ = ('id', 'comment', 'bug', 'attachments', 'internal', 'activity', 'commented_by', 'connector_config', 'connector', 'team', 'approval', 'engagement', 'automation_workflow', 'automation_workflow_reason', 'created', 'updated')
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

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')



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
    __field_names__ = ('id', 'engagement_custom_id', 'name', 'organization', 'vendor', 'security_posture', 'scheduled_date', 'delivery_date', 'documents', 'subscribed_services', 'checked_terms_and_conditions', 'executive_summary', 'credits_estimated', 'credits', 'created_by', 'created', 'updated', 'is_active', 'plans', 'fields', 'engagement_assessment', 'prerequisites_engagement', 'exportreport_set', 'bug_engagements', 'activity_engagement', 'comments_engagement', 'assessments_count', 'engagement_completion', 'assessments_per_service', 'total_hours_spent', 'prerequisites_completion', 'state')
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

    created_by = sgqlc.types.Field(ApprovalUserType, graphql_name='createdBy')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')

    plans = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='plans')

    fields = sgqlc.types.Field(JSONString, graphql_name='fields')

    engagement_assessment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='engagementAssessment')

    prerequisites_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PreRequisitesType'))), graphql_name='prerequisitesEngagement')

    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='exportreportSet')

    bug_engagements = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugEngagements')

    activity_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementActivityType))), graphql_name='activityEngagement')

    comments_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementCommentType))), graphql_name='commentsEngagement')

    assessments_count = sgqlc.types.Field(Int, graphql_name='assessmentsCount')

    engagement_completion = sgqlc.types.Field(Int, graphql_name='engagementCompletion')

    assessments_per_service = sgqlc.types.Field(GenericScalar, graphql_name='assessmentsPerService')

    total_hours_spent = sgqlc.types.Field(Int, graphql_name='totalHoursSpent')

    prerequisites_completion = sgqlc.types.Field(GenericScalar, graphql_name='prerequisitesCompletion')

    state = sgqlc.types.Field(String, graphql_name='state')



class EngagementsFieldType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'slug', 'description', 'field_type', 'options', 'is_required', 'is_active', 'extra_data', 'created', 'updated', 'organization')
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



class GenerateReportMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('reports',)
    reports = sgqlc.types.Field(String, graphql_name='reports')



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



class MemberType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'user', 'organization', 'role', 'asset_search_query', 'permitted_apps', 'permitted_modules', 'default_page', 'preset_set', 'approval_approved_by', 'approval_raised_by', 'dashboards_set', 'widget_set', 'is_active', 'engagements', 'assets')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')

    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')

    role = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='role')

    asset_search_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetSearchQuery')

    permitted_apps = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='permittedApps')

    permitted_modules = sgqlc.types.Field(JSONString, graphql_name='permittedModules')

    default_page = sgqlc.types.Field(JSONString, graphql_name='defaultPage')

    preset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PresetType'))), graphql_name='presetSet')

    approval_approved_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalApprovedBy')

    approval_raised_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalRaisedBy')

    dashboards_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='dashboardsSet')

    widget_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetSet')

    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')

    engagements = sgqlc.types.Field(sgqlc.types.list_of(EngagementType), graphql_name='engagements')

    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')



class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('create_automation_workflow', 'update_automation_workflow', 'delete_automation_workflow', 'create_sla_rule', 'update_sla_rule', 'delete_sla_rule', 'add_preset', 'update_presets', 'delete_presets', 'update_data_retention_setting', 'update_asm_settings', 'bulk_update_credential_manager', 'vaults', 'add_vault_attachment', 'bulk_delete_vault_mutation', 'add_widget', 'update_widgets', 'delete_widgets', 'clone_widget', 'add_dashboard', 'update_dashboard', 'delete_dashboard', 'export_dashboard', 'import_dashboard', 'comment_update', 'comment_delete', 'assessment', 'bulk_update_prerequisites', 'bulk_delete_prerequisites', 'update_assessments', 'bulk_update_assessment', 'update_engagement', 'add_attachment', 'archive_engagements', 'create_engagement', 'add_engagements_field_settings_mutation', 'delete_engagement_field_settings_mutation', 'update_engagement_field_settings_mutation', 'assign_asset_view_to_users', 'add_report_attachment', 'bulk_delete_attachment', 'restore_default_prioritization_rule', 'report_bulk_delete', 'generate_report', 'update_report', 'delete_report_template', 'add_report_template', 'update_report_template', 'add_group', 'update_group', 'group_bulk_delete', 'org_member_role_bulk_update', 'team_member_role_bulk_update', 'org_member_role_bulk_delete', 'team_member_role_bulk_delete', 'bulk_update_member_asset_access', 'bug_bulk_update', 'bug_bulk_assignment', 'bug_bulk_unassignment', 'bug_bulk_update_tags', 'bug_bulk_update_cve', 'bug_bulk_update_cwe', 'bug_bulk_delete', 'add_bulk_comment', 'bug_bulk_add_to_tracker', 'approve_state_change', 'deduplicate_bug_preview', 'deduplicate_bug_confirm', 'calculate_priority_score', 'transfer_engagement_bugs', 'bug_update_risk_records', 'add_bug_settings_fields', 'update_bug_settings_fields', 'delete_bug_settings_fields', 'bug_bulk_update_title', 'bug_bulk_update_mitigation_description', 'archive_bug_bulk_update', 'bug_bulk_update_custom_fields', 'update_bugs_fields_with_csv', 'bug_create', 'sync_bug_with_trackers', 'assets_bulk_update', 'assets_bulk_merge', 'assets_bulk_link', 'assets_bulk_delete', 'assets_bulk_update_tags', 'archive_assets_bulk_update', 'assets_merge_preview', 'assets_merge_confirm', 'calculate_risk_score', 'software_packages_bulk_update', 'software_packages_bulk_delete', 'software_package_create', 'add_asset_settings_fields', 'update_asset_settings_fields', 'delete_asset_settings_fields', 'bulk_update_asset_custom_field_mutation', 'create_asset', 'update_asset_fields_with_csv', 'bulk_asset_access_user_mutation')
    create_automation_workflow = sgqlc.types.Field(CreateAutomationWorkflowMutation, graphql_name='createAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('credential_manager_id', sgqlc.types.Arg(Int, graphql_name='credentialManagerId', default=None)),
        ('hooks', sgqlc.types.Arg(GenericScalar, graphql_name='hooks', default=None)),
        ('ignore_weightage', sgqlc.types.Arg(Boolean, graphql_name='ignoreWeightage', default=None)),
        ('instructions', sgqlc.types.Arg(String, graphql_name='instructions', default=None)),
        ('llm_model', sgqlc.types.Arg(Int, graphql_name='llmModel', default=None)),
        ('module', sgqlc.types.Arg(Int, graphql_name='module', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('tool', sgqlc.types.Arg(Int, graphql_name='tool', default=None)),
        ('triggers', sgqlc.types.Arg(GenericScalar, graphql_name='triggers', default=None)),
        ('weightage', sgqlc.types.Arg(Int, graphql_name='weightage', default=None)),
))
    )
    '''Arguments:

    * `credential_manager_id` (`Int`)None
    * `hooks` (`GenericScalar`)None
    * `ignore_weightage` (`Boolean`)None
    * `instructions` (`String`)None
    * `llm_model` (`Int`)None
    * `module` (`Int`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `role` (`String`)None
    * `search_query` (`String`)None
    * `tool` (`Int`)None
    * `triggers` (`GenericScalar`)None
    * `weightage` (`Int`)None
    '''

    update_automation_workflow = sgqlc.types.Field('UpdateAutomationWorkflowMutation', graphql_name='updateAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('credential_manager_id', sgqlc.types.Arg(Int, graphql_name='credentialManagerId', default=None)),
        ('hooks', sgqlc.types.Arg(GenericScalar, graphql_name='hooks', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('ignore_weightage', sgqlc.types.Arg(Boolean, graphql_name='ignoreWeightage', default=None)),
        ('instructions', sgqlc.types.Arg(String, graphql_name='instructions', default=None)),
        ('llm_model', sgqlc.types.Arg(Int, graphql_name='llmModel', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('triggers', sgqlc.types.Arg(GenericScalar, graphql_name='triggers', default=None)),
        ('weightage', sgqlc.types.Arg(Int, graphql_name='weightage', default=None)),
))
    )
    '''Arguments:

    * `credential_manager_id` (`Int`)None
    * `hooks` (`GenericScalar`)None
    * `id` (`Int`)None
    * `ignore_weightage` (`Boolean`)None
    * `instructions` (`String`)None
    * `llm_model` (`Int`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `role` (`String`)None
    * `search_query` (`String`)None
    * `triggers` (`GenericScalar`)None
    * `weightage` (`Int`)None
    '''

    delete_automation_workflow = sgqlc.types.Field(DeleteAutomationWorkMutation, graphql_name='deleteAutomationWorkflow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `id` (`Int`)None
    * `organization_id` (`UUID`)None
    '''

    create_sla_rule = sgqlc.types.Field(CreateSLARuleMutation, graphql_name='createSlaRule', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('rules_data', sgqlc.types.Arg(sgqlc.types.non_null(GenericScalar), graphql_name='rulesData', default=None)),
        ('update_existing_findings', sgqlc.types.Arg(Boolean, graphql_name='updateExistingFindings', default=False)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    * `rules_data` (`GenericScalar!`)None
    * `update_existing_findings` (`Boolean`)None (default: `false`)
    '''

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
    '''Arguments:

    * `duration` (`Int`)None
    * `name` (`String`)None
    * `organization_id` (`UUID!`)None
    * `preview` (`Boolean`)None (default: `false`)
    * `rule_id` (`Int!`)None
    * `search_query` (`String`)None
    * `weightage` (`Int`)None
    '''

    delete_sla_rule = sgqlc.types.Field(DeleteSLARuleMutation, graphql_name='deleteSlaRule', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('preview', sgqlc.types.Arg(Boolean, graphql_name='preview', default=False)),
        ('rule_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='ruleId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    * `preview` (`Boolean`)None (default: `false`)
    * `rule_id` (`Int!`)None
    '''

    add_preset = sgqlc.types.Field(AddPresetMutation, graphql_name='addPreset', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(JSONString, graphql_name='data', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('preset_type', sgqlc.types.Arg(Int, graphql_name='presetType', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `data` (`JSONString`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `preset_type` (`Int`)None
    * `search_query` (`String`)None
    '''

    update_presets = sgqlc.types.Field('UpdatePresetsMutation', graphql_name='updatePresets', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(JSONString, graphql_name='data', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('preset_id', sgqlc.types.Arg(Int, graphql_name='presetId', default=None)),
        ('preset_type', sgqlc.types.Arg(Int, graphql_name='presetType', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `data` (`JSONString`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `preset_id` (`Int`)None
    * `preset_type` (`Int`)None
    * `search_query` (`String`)None
    '''

    delete_presets = sgqlc.types.Field(DeletePresetsMutation, graphql_name='deletePresets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    update_data_retention_setting = sgqlc.types.Field('UpdateDataRetentionSettingMutation', graphql_name='updateDataRetentionSetting', args=sgqlc.types.ArgDict((
        ('data_retention_setting', sgqlc.types.Arg(JSONString, graphql_name='dataRetentionSetting', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `data_retention_setting` (`JSONString`)None
    * `organization_id` (`UUID!`)None
    '''

    update_asm_settings = sgqlc.types.Field('UpdateASMSettingsMutations', graphql_name='updateAsmSettings', args=sgqlc.types.ArgDict((
        ('is_enabled', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isEnabled', default=None)),
        ('is_finding_scanning_enabled', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isFindingScanningEnabled', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('out_of_scope', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='outOfScope', default=None)),
        ('scheduled_at', sgqlc.types.Arg(String, graphql_name='scheduledAt', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='scope', default=None)),
))
    )
    '''Arguments:

    * `is_enabled` (`Boolean!`)None
    * `is_finding_scanning_enabled` (`Boolean!`)None
    * `organization_id` (`UUID!`)None
    * `out_of_scope` (`[String]`)None
    * `scheduled_at` (`String`)None
    * `scope` (`[String]!`)None
    '''

    bulk_update_credential_manager = sgqlc.types.Field(BulkUpdateCredentialManager, graphql_name='bulkUpdateCredentialManager', args=sgqlc.types.ArgDict((
        ('new_credential_manager_id', sgqlc.types.Arg(Int, graphql_name='newCredentialManagerId', default=None)),
        ('old_credential_manager_id', sgqlc.types.Arg(Int, graphql_name='oldCredentialManagerId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `new_credential_manager_id` (`Int`)None
    * `old_credential_manager_id` (`Int`)None
    * `organization_id` (`UUID`)None
    '''

    vaults = sgqlc.types.Field(sgqlc.types.list_of('VaultType'), graphql_name='vaults')

    add_vault_attachment = sgqlc.types.Field(AddVaultAttachmentMutation, graphql_name='addVaultAttachment', args=sgqlc.types.ArgDict((
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('prerequisite', sgqlc.types.Arg(Boolean, graphql_name='prerequisite', default=None)),
))
    )
    '''Arguments:

    * `engagement_id` (`UUID`)None
    * `file` (`Upload!`)None
    * `organization_id` (`UUID!`)None
    * `prerequisite` (`Boolean`)None
    '''

    bulk_delete_vault_mutation = sgqlc.types.Field(BulkDeleteVaultMutation, graphql_name='bulkDeleteVaultMutation', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('vault_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='vaultIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `vault_ids` (`[Int]`)None
    '''

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
    '''Arguments:

    * `aggregate_field` (`String`)None
    * `annotated_fields` (`[GenericScalar]`)None
    * `assessment_search_query` (`String`)None
    * `asset_search_query` (`String`)None
    * `asset_view_id` (`Int`)None
    * `bug_search_query` (`String`)None
    * `bug_view_id` (`Int`)None
    * `chart_type` (`String!`)None
    * `connector_search_query` (`String`)None
    * `custom_fields` (`GenericScalar`)None
    * `datetime_filter` (`Int`)None
    * `description` (`String!`)None
    * `engagement_search_query` (`String`)None
    * `fields` (`[String]`)None
    * `filter_field_name` (`String`)None
    * `function` (`String`)None
    * `group_by_field` (`String`)None
    * `module` (`String!`)None
    * `name` (`String!`)None
    * `organization_id` (`UUID!`)None
    * `organization_search_query` (`String`)None
    * `positional_data` (`[GenericScalar]`)None
    * `prefix` (`String`)None
    * `scan_log_search_query` (`String`)None
    * `suffix` (`String`)None
    * `tags` (`[String]`)None
    * `teams_search_query` (`String`)None
    * `time_group` (`String`)None
    * `timeseries_field` (`String`)None
    * `tracker_search_query` (`String`)None
    * `widget_params` (`GenericScalar`)None
    '''

    update_widgets = sgqlc.types.Field('UpdateWidgetMutation', graphql_name='updateWidgets', args=sgqlc.types.ArgDict((
        ('annotated_fields', sgqlc.types.Arg(sgqlc.types.list_of(GenericScalar), graphql_name='annotatedFields', default=None)),
        ('assessment_search_query', sgqlc.types.Arg(String, graphql_name='assessmentSearchQuery', default=None)),
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('asset_view_id', sgqlc.types.Arg(Int, graphql_name='assetViewId', default=None)),
        ('bug_search_query', sgqlc.types.Arg(String, graphql_name='bugSearchQuery', default=None)),
        ('bug_view_id', sgqlc.types.Arg(Int, graphql_name='bugViewId', default=None)),
        ('connector_search_query', sgqlc.types.Arg(String, graphql_name='connectorSearchQuery', default=None)),
        ('custom_fields', sgqlc.types.Arg(GenericScalar, graphql_name='customFields', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('engagement_search_query', sgqlc.types.Arg(String, graphql_name='engagementSearchQuery', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fields', default=None)),
        ('filter_field_name', sgqlc.types.Arg(String, graphql_name='filterFieldName', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('organization_search_query', sgqlc.types.Arg(String, graphql_name='organizationSearchQuery', default=None)),
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
    '''Arguments:

    * `annotated_fields` (`[GenericScalar]`)None
    * `assessment_search_query` (`String`)None
    * `asset_search_query` (`String`)None
    * `asset_view_id` (`Int`)None
    * `bug_search_query` (`String`)None
    * `bug_view_id` (`Int`)None
    * `connector_search_query` (`String`)None
    * `custom_fields` (`GenericScalar`)None
    * `description` (`String`)None
    * `engagement_search_query` (`String`)None
    * `fields` (`[String]`)None
    * `filter_field_name` (`String`)None
    * `id` (`Int`)None
    * `name` (`String`)None
    * `organization_id` (`UUID!`)None
    * `organization_search_query` (`String`)None
    * `positional_data` (`GenericScalar`)None
    * `prefix` (`String`)None
    * `scan_log_search_query` (`String`)None
    * `suffix` (`String`)None
    * `tags` (`[String]`)None
    * `teams_search_query` (`String`)None
    * `time_group` (`String`)None
    * `timeseries_field` (`String`)None
    * `tracker_search_query` (`String`)None
    * `widget_params` (`GenericScalar`)None
    '''

    delete_widgets = sgqlc.types.Field(DeleteWidgetMutation, graphql_name='deleteWidgets', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `id` (`Int`)None
    * `organization_id` (`UUID!`)None
    '''

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
    '''Arguments:

    * `annotated_fields` (`[GenericScalar]`)None
    * `assessment_search_query` (`String`)None
    * `asset_search_query` (`String`)None
    * `asset_view_id` (`Int`)None
    * `bug_search_query` (`String`)None
    * `bug_view_id` (`Int`)None
    * `connector_search_query` (`String`)None
    * `datetime_filter` (`Int`)None
    * `default_widget_id` (`Int!`)None
    * `engagement_search_query` (`String`)None
    * `name` (`String!`)None
    * `organization_id` (`UUID!`)None
    * `organization_search_query` (`String`)None
    * `positional_data` (`[GenericScalar]`)None
    * `prefix` (`String`)None
    * `scan_log_search_query` (`String`)None
    * `suffix` (`String`)None
    * `tags` (`[String]`)None
    * `teams_search_query` (`String`)None
    * `time_group` (`String`)None
    * `timeseries_field` (`String`)None
    * `tracker_search_query` (`String`)None
    * `widget_params` (`GenericScalar`)None
    '''

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
    '''Arguments:

    * `data` (`[GenericScalar]`)None
    * `description` (`String`)None
    * `is_default` (`Boolean`)None
    * `name` (`String`)None
    * `organization_id` (`UUID!`)None
    * `positional_data` (`[GenericScalar]`)None
    * `tags` (`[String]`)None
    * `widgets` (`[Int]`)None
    '''

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
    '''Arguments:

    * `data` (`[GenericScalar]`)None
    * `description` (`String`)None
    * `id` (`Int`)None
    * `is_default` (`Boolean`)None
    * `name` (`String`)None
    * `organization_id` (`UUID!`)None
    * `positional_data` (`[GenericScalar]`)None
    * `tags` (`[String]`)None
    * `widgets` (`[Int]`)None
    '''

    delete_dashboard = sgqlc.types.Field(DeleteDashboardMutation, graphql_name='deleteDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `id` (`Int`)None
    * `organization_id` (`UUID!`)None
    '''

    export_dashboard = sgqlc.types.Field(DashboardExportMutation, graphql_name='exportDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `id` (`Int`)None
    * `name` (`String`)None
    * `organization_id` (`UUID!`)None
    '''

    import_dashboard = sgqlc.types.Field(DashboardImportMutation, graphql_name='importDashboard', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `file` (`Upload!`)None
    * `name` (`String!`)None
    * `organization_id` (`UUID!`)None
    '''

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
    '''Arguments:

    * `add_attachments` (`[Int]`)None
    * `bug_id` (`Int`)None
    * `comment` (`String!`)None
    * `comment_id` (`Int!`)None
    * `engagement_id` (`UUID`)None
    * `organization_id` (`UUID!`)None
    * `remove_attachments` (`[Int]`)None
    '''

    comment_delete = sgqlc.types.Field(DeleteCommentMutation, graphql_name='commentDelete', args=sgqlc.types.ArgDict((
        ('bug_id', sgqlc.types.Arg(Int, graphql_name='bugId', default=None)),
        ('comment_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='commentId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `bug_id` (`Int`)None
    * `comment_id` (`Int!`)None
    * `engagement_id` (`UUID`)None
    * `organization_id` (`UUID!`)None
    '''

    assessment = sgqlc.types.Field(sgqlc.types.list_of(AssessmentType), graphql_name='assessment')

    bulk_update_prerequisites = sgqlc.types.Field(BulkUpdatePreRequisitesMutation, graphql_name='bulkUpdatePrerequisites', args=sgqlc.types.ArgDict((
        ('engagement_id', sgqlc.types.Arg(String, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('prerequisites_data', sgqlc.types.Arg(JSONString, graphql_name='prerequisitesData', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `engagement_id` (`String`)None
    * `organization_id` (`UUID`)None
    * `prerequisites_data` (`JSONString`)None
    * `search_query` (`String`)None
    '''

    bulk_delete_prerequisites = sgqlc.types.Field(BulkDeletePrerequisitesMutation, graphql_name='bulkDeletePrerequisites', args=sgqlc.types.ArgDict((
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `engagement_id` (`UUID`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    update_assessments = sgqlc.types.Field('UpdateAssessmentMutation', graphql_name='updateAssessments', args=sgqlc.types.ArgDict((
        ('assessment_category', sgqlc.types.Arg(Int, graphql_name='assessmentCategory', default=None)),
        ('assessment_id', sgqlc.types.Arg(Int, graphql_name='assessmentId', default=None)),
        ('assigned_to', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assignedTo', default=None)),
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
    '''Arguments:

    * `assessment_category` (`Int`)None
    * `assessment_id` (`Int`)None
    * `assigned_to` (`[Int]`)None
    * `delivery_date` (`Date`)None
    * `engagement_id` (`UUID`)None
    * `instructions` (`String`)None
    * `organization_id` (`UUID`)None
    * `scheduled_date` (`Date`)None
    * `state` (`Int`)None
    * `test_accounts` (`String`)None
    * `total_hours_spent` (`Int`)None
    * `vpn_accounts` (`String`)None
    '''

    bulk_update_assessment = sgqlc.types.Field(BulkUpdateAssessmentMutation, graphql_name='bulkUpdateAssessment', args=sgqlc.types.ArgDict((
        ('assessment_timelines', sgqlc.types.Arg(JSONString, graphql_name='assessmentTimelines', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('total_hours_spent', sgqlc.types.Arg(Int, graphql_name='totalHoursSpent', default=None)),
))
    )
    '''Arguments:

    * `assessment_timelines` (`JSONString`)None
    * `delivery_date` (`Date`)None
    * `engagement_id` (`UUID`)None
    * `organization_id` (`UUID`)None
    * `scheduled_date` (`Date`)None
    * `search_query` (`String`)None
    * `state` (`Int`)None
    * `total_hours_spent` (`Int`)None
    '''

    update_engagement = sgqlc.types.Field('UpdateEngagementMutation', graphql_name='updateEngagement', args=sgqlc.types.ArgDict((
        ('add_document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='addDocumentIds', default=None)),
        ('assessment_data', sgqlc.types.Arg(JSONString, graphql_name='assessmentData', default=None)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('comment_attachments', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='commentAttachments', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('executive_summary', sgqlc.types.Arg(String, graphql_name='executiveSummary', default=None)),
        ('fields', sgqlc.types.Arg(JSONString, graphql_name='fields', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('plans', sgqlc.types.Arg(Int, graphql_name='plans', default=None)),
        ('prerequisites_data', sgqlc.types.Arg(JSONString, graphql_name='prerequisitesData', default=None)),
        ('remove_document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='removeDocumentIds', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('service', sgqlc.types.Arg(String, graphql_name='service', default=None)),
        ('subscribed_services', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='subscribedServices', default=None)),
))
    )
    '''Arguments:

    * `add_document_ids` (`[Int]`)None
    * `assessment_data` (`JSONString`)None
    * `comment` (`String`)None
    * `comment_attachments` (`[Int]`)None
    * `delivery_date` (`Date`)None
    * `engagement_id` (`UUID`)None
    * `executive_summary` (`String`)None
    * `fields` (`JSONString`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `package` (`String`)None
    * `plans` (`Int`)None
    * `prerequisites_data` (`JSONString`)None
    * `remove_document_ids` (`[Int]`)None
    * `scheduled_date` (`Date`)None
    * `service` (`String`)None
    * `subscribed_services` (`[String]`)None
    '''

    add_attachment = sgqlc.types.Field(AddAttachmentMutation, graphql_name='addAttachment', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `file` (`Upload!`)None
    * `organization_id` (`UUID!`)None
    '''

    archive_engagements = sgqlc.types.Field(BulkArchiveEngagementsMutation, graphql_name='archiveEngagements', args=sgqlc.types.ArgDict((
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `is_active` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    create_engagement = sgqlc.types.Field(CreateEngagementMutation, graphql_name='createEngagement', args=sgqlc.types.ArgDict((
        ('assessment_data', sgqlc.types.Arg(JSONString, graphql_name='assessmentData', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='deliveryDate', default=None)),
        ('document_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='documentIds', default=None)),
        ('executive_summary', sgqlc.types.Arg(String, graphql_name='executiveSummary', default=None)),
        ('fields', sgqlc.types.Arg(JSONString, graphql_name='fields', default=None)),
        ('include_related_assets', sgqlc.types.Arg(Boolean, graphql_name='includeRelatedAssets', default=None)),
        ('is_self_managed', sgqlc.types.Arg(Boolean, graphql_name='isSelfManaged', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('plans', sgqlc.types.Arg(Int, graphql_name='plans', default=None)),
        ('prerequisites_data', sgqlc.types.Arg(JSONString, graphql_name='prerequisitesData', default=None)),
        ('scheduled_date', sgqlc.types.Arg(Date, graphql_name='scheduledDate', default=None)),
        ('subscribed_services', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='subscribedServices', default=None)),
        ('vendor_code', sgqlc.types.Arg(String, graphql_name='vendorCode', default=None)),
))
    )
    '''Engagement create graphene mutation

    Arguments:

    * `assessment_data` (`JSONString`)None
    * `delivery_date` (`Date`)None
    * `document_ids` (`[Int]`)None
    * `executive_summary` (`String`)None
    * `fields` (`JSONString`)None
    * `include_related_assets` (`Boolean`)None
    * `is_self_managed` (`Boolean`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `plans` (`Int`)None
    * `prerequisites_data` (`JSONString`)None
    * `scheduled_date` (`Date`)None
    * `subscribed_services` (`[String]`)None
    * `vendor_code` (`String`)None
    '''

    add_engagements_field_settings_mutation = sgqlc.types.Field(AddEngagementsFieldSettingsMutation, graphql_name='addEngagementsFieldSettingsMutation', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('field_type', sgqlc.types.Arg(Int, graphql_name='fieldType', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `description` (`String`)None
    * `field_type` (`Int`)None
    * `is_required` (`Boolean`)None
    * `name` (`String`)None
    * `options` (`[String]`)None
    * `organization_id` (`UUID`)None
    '''

    delete_engagement_field_settings_mutation = sgqlc.types.Field(DeleteEngagementFieldSettingsMutation, graphql_name='deleteEngagementFieldSettingsMutation', args=sgqlc.types.ArgDict((
        ('engagement_field_id', sgqlc.types.Arg(Int, graphql_name='engagementFieldId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `engagement_field_id` (`Int`)None
    * `organization_id` (`UUID`)None
    '''

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
    '''Arguments:

    * `description` (`String`)None
    * `engagement_field_id` (`Int`)None
    * `is_active` (`Boolean`)None
    * `is_required` (`Boolean`)None
    * `name` (`String`)None
    * `new_selected_option` (`String`)None
    * `old_selected_option` (`String`)None
    * `options` (`[String]`)None
    * `organization_id` (`UUID`)None
    '''

    assign_asset_view_to_users = sgqlc.types.Field(AssignAssetViewToUsersMutation, graphql_name='assignAssetViewToUsers', args=sgqlc.types.ArgDict((
        ('assign_bugs', sgqlc.types.Arg(String, graphql_name='assignBugs', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
))
    )
    '''Arguments:

    * `assign_bugs` (`String`)None
    * `organization_id` (`UUID`)None
    * `user_ids` (`[Int]`)None
    * `view_id` (`Int`)None
    '''

    add_report_attachment = sgqlc.types.Field(AddReportAttachmentMutation, graphql_name='addReportAttachment', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `file` (`Upload!`)None
    * `organization_id` (`UUID!`)None
    '''

    bulk_delete_attachment = sgqlc.types.Field(DestroyBulkReportAttachmentMutation, graphql_name='bulkDeleteAttachment', args=sgqlc.types.ArgDict((
        ('attachment_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='attachmentIds', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `attachment_ids` (`[Int]`)None
    * `organization_id` (`UUID`)None
    '''

    restore_default_prioritization_rule = sgqlc.types.Field('RestoreDefaultPriortizationRuleMutation', graphql_name='restoreDefaultPrioritizationRule', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    '''

    report_bulk_delete = sgqlc.types.Field(DestroyBulkReportMutation, graphql_name='reportBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('report_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='reportIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `report_ids` (`[Int]`)None
    '''

    generate_report = sgqlc.types.Field(GenerateReportMutation, graphql_name='generateReport', args=sgqlc.types.ArgDict((
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('custom_data', sgqlc.types.Arg(JSONString, graphql_name='customData', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('report_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reportName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='templateId', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
))
    )
    '''Arguments:

    * `asset_search_query` (`String`)None
    * `custom_data` (`JSONString`)None
    * `engagement_id` (`UUID`)None
    * `organization_id` (`UUID!`)None
    * `report_name` (`String!`)None
    * `search_query` (`String`)None
    * `template_id` (`Int!`)None
    * `view_id` (`Int`)None
    '''

    update_report = sgqlc.types.Field('UpdateReportMutation', graphql_name='updateReport', args=sgqlc.types.ArgDict((
        ('export_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='exportId', default=None)),
        ('html_content', sgqlc.types.Arg(String, graphql_name='htmlContent', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `export_id` (`Int!`)None
    * `html_content` (`String`)None
    * `name` (`String`)None
    * `organization_id` (`UUID!`)None
    '''

    delete_report_template = sgqlc.types.Field(BulkDeleteTemplateMutation, graphql_name='deleteReportTemplate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('template_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='templateIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `template_ids` (`[Int]`)None
    '''

    add_report_template = sgqlc.types.Field(AddTemplateMutation, graphql_name='addReportTemplate', args=sgqlc.types.ArgDict((
        ('footer_template', sgqlc.types.Arg(String, graphql_name='footerTemplate', default=None)),
        ('header_template', sgqlc.types.Arg(String, graphql_name='headerTemplate', default=None)),
        ('html_data', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='htmlData', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='templateName', default=None)),
))
    )
    '''Arguments:

    * `footer_template` (`String`)None
    * `header_template` (`String`)None
    * `html_data` (`String!`)None
    * `organization_id` (`UUID!`)None
    * `template_name` (`String!`)None
    '''

    update_report_template = sgqlc.types.Field('UpdateTemplateMutation', graphql_name='updateReportTemplate', args=sgqlc.types.ArgDict((
        ('footer_template', sgqlc.types.Arg(String, graphql_name='footerTemplate', default=None)),
        ('header_template', sgqlc.types.Arg(String, graphql_name='headerTemplate', default=None)),
        ('html_data', sgqlc.types.Arg(String, graphql_name='htmlData', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='templateId', default=None)),
        ('template_name', sgqlc.types.Arg(String, graphql_name='templateName', default=None)),
))
    )
    '''Arguments:

    * `footer_template` (`String`)None
    * `header_template` (`String`)None
    * `html_data` (`String`)None
    * `organization_id` (`UUID!`)None
    * `template_id` (`Int!`)None
    * `template_name` (`String`)None
    '''

    add_group = sgqlc.types.Field(AddGroupMutation, graphql_name='addGroup', args=sgqlc.types.ArgDict((
        ('asset_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assetIds', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `asset_ids` (`[Int]`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    '''

    update_group = sgqlc.types.Field('UpdateGroupMutation', graphql_name='updateGroup', args=sgqlc.types.ArgDict((
        ('asset_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assetIds', default=None)),
        ('group_id', sgqlc.types.Arg(Int, graphql_name='groupId', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `asset_ids` (`[Int]`)None
    * `group_id` (`Int`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    '''

    group_bulk_delete = sgqlc.types.Field(BulkDeleteGroupMutation, graphql_name='groupBulkDelete', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[Int]`)None
    * `organization_id` (`UUID`)None
    '''

    org_member_role_bulk_update = sgqlc.types.Field(BulkUpdateOrgMemberRoleMutation, graphql_name='orgMemberRoleBulkUpdate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(Int, graphql_name='role', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `role` (`Int`)None
    * `user_ids` (`[Int]`)None
    '''

    team_member_role_bulk_update = sgqlc.types.Field(BulkUpdateTeamMemberRoleMutation, graphql_name='teamMemberRoleBulkUpdate', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='role', default=None)),
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='teamId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    * `role` (`Int!`)None
    * `team_id` (`Int!`)None
    * `user_ids` (`[Int]`)None
    '''

    org_member_role_bulk_delete = sgqlc.types.Field(BulkDeleteOrgMemberRoleMutation, graphql_name='orgMemberRoleBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `user_ids` (`[Int]`)None
    '''

    team_member_role_bulk_delete = sgqlc.types.Field(BulkDeleteTeamMemberRoleMutation, graphql_name='teamMemberRoleBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('team_id', sgqlc.types.Arg(Int, graphql_name='teamId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `team_id` (`Int`)None
    * `user_ids` (`[Int]`)None
    '''

    bulk_update_member_asset_access = sgqlc.types.Field(BulkUpdateMemberAssetAccessMutation, graphql_name='bulkUpdateMemberAssetAccess', args=sgqlc.types.ArgDict((
        ('add_users_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='addUsersList', default=None)),
        ('asset_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='assetIds', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('remove_users_list', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='removeUsersList', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `add_users_list` (`[Int]`)None
    * `asset_ids` (`[Int]`)None
    * `organization_id` (`UUID`)None
    * `remove_users_list` (`[Int]`)None
    * `search_query` (`String`)None
    '''

    bug_bulk_update = sgqlc.types.Field(BulkUpdateBugMutation, graphql_name='bugBulkUpdate', args=sgqlc.types.ArgDict((
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
    '''Arguments:

    * `cvss` (`Float`)None
    * `due_date` (`Date`)None
    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `severity` (`Int`)None
    * `state` (`Int`)None
    '''

    bug_bulk_assignment = sgqlc.types.Field(BulkBugAssignmentMutation, graphql_name='bugBulkAssignment', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `user_ids` (`[Int]`)None
    '''

    bug_bulk_unassignment = sgqlc.types.Field(BulkBugUnAssignmentMutation, graphql_name='bugBulkUnassignment', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `user_ids` (`[Int]`)None
    '''

    bug_bulk_update_tags = sgqlc.types.Field(BulkUpdateBugTagMutation, graphql_name='bugBulkUpdateTags', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `tags` (`[String]`)None
    '''

    bug_bulk_update_cve = sgqlc.types.Field(BulkUpdateBugCVEMutation, graphql_name='bugBulkUpdateCve', args=sgqlc.types.ArgDict((
        ('cves', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='cves', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `cves` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    bug_bulk_update_cwe = sgqlc.types.Field(BulkUpdateBugCWEMutation, graphql_name='bugBulkUpdateCwe', args=sgqlc.types.ArgDict((
        ('cwes', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='cwes', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `cwes` (`[Int]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    bug_bulk_delete = sgqlc.types.Field(BulkDeleteBugMutation, graphql_name='bugBulkDelete', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('is_archived_view', sgqlc.types.Arg(Boolean, graphql_name='isArchivedView', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `is_archived_view` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

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
    '''Arguments:

    * `attachment_list` (`[Int]`)None
    * `comment` (`String`)None
    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `internal` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    bug_bulk_add_to_tracker = sgqlc.types.Field(BulkAddToTrackerMutation, graphql_name='bugBulkAddToTracker', args=sgqlc.types.ArgDict((
        ('configuration_id', sgqlc.types.Arg(Int, graphql_name='configurationId', default=None)),
        ('create_grouped_issues', sgqlc.types.Arg(Boolean, graphql_name='createGroupedIssues', default=None)),
        ('custom_title', sgqlc.types.Arg(String, graphql_name='customTitle', default=None)),
        ('issue_groupby', sgqlc.types.Arg(String, graphql_name='issueGroupby', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('overwrite_existing_issues', sgqlc.types.Arg(Boolean, graphql_name='overwriteExistingIssues', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('severity', sgqlc.types.Arg(Int, graphql_name='severity', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
        ('tracker_slug', sgqlc.types.Arg(String, graphql_name='trackerSlug', default=None)),
))
    )
    '''Arguments:

    * `configuration_id` (`Int`)None
    * `create_grouped_issues` (`Boolean`)None
    * `custom_title` (`String`)None
    * `issue_groupby` (`String`)None
    * `organization_id` (`UUID`)None
    * `overwrite_existing_issues` (`Boolean`)None
    * `search_query` (`String`)None
    * `severity` (`Int`)None
    * `state` (`Int`)None
    * `tracker_slug` (`String`)None
    '''

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
    '''Arguments:

    * `comment` (`String`)None
    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `is_approved` (`Boolean`)None
    * `is_declined` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    deduplicate_bug_preview = sgqlc.types.Field(DeduplicateBugPreviewMutation, graphql_name='deduplicateBugPreview', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('strategy', sgqlc.types.Arg(Int, graphql_name='strategy', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `strategy` (`Int`)None
    '''

    deduplicate_bug_confirm = sgqlc.types.Field(DeduplicateBugConfirmMutation, graphql_name='deduplicateBugConfirm', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('strategy', sgqlc.types.Arg(Int, graphql_name='strategy', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `strategy` (`Int`)None
    '''

    calculate_priority_score = sgqlc.types.Field(CalculatePrioritizationScoreMutation, graphql_name='calculatePriorityScore', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    transfer_engagement_bugs = sgqlc.types.Field('TransferEngagementBugMutation', graphql_name='transferEngagementBugs', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('transfer_engagement_id', sgqlc.types.Arg(UUID, graphql_name='transferEngagementId', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `transfer_engagement_id` (`UUID`)None
    '''

    bug_update_risk_records = sgqlc.types.Field('UpdateRiskRecordsMutation', graphql_name='bugUpdateRiskRecords', args=sgqlc.types.ArgDict((
        ('bug_id', sgqlc.types.Arg(Int, graphql_name='bugId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('records_at_risk', sgqlc.types.Arg(Int, graphql_name='recordsAtRisk', default=None)),
        ('records_type', sgqlc.types.Arg(Int, graphql_name='recordsType', default=None)),
))
    )
    '''Arguments:

    * `bug_id` (`Int`)None
    * `organization_id` (`UUID`)None
    * `records_at_risk` (`Int`)None
    * `records_type` (`Int`)None
    '''

    add_bug_settings_fields = sgqlc.types.Field(AddBugFieldSettingsMutation, graphql_name='addBugSettingsFields', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('field_type', sgqlc.types.Arg(Int, graphql_name='fieldType', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `description` (`String`)None
    * `field_type` (`Int`)None
    * `is_required` (`Boolean`)None
    * `name` (`String`)None
    * `options` (`[String]`)None
    * `organization_id` (`UUID`)None
    '''

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
    '''Arguments:

    * `bug_field_id` (`Int`)None
    * `description` (`String`)None
    * `is_active` (`Boolean`)None
    * `is_required` (`Boolean`)None
    * `name` (`String`)None
    * `new_selected_option` (`String`)None
    * `old_selected_option` (`String`)None
    * `options` (`[String]`)None
    * `organization_id` (`UUID`)None
    '''

    delete_bug_settings_fields = sgqlc.types.Field(DeleteBugFieldSettingsMutation, graphql_name='deleteBugSettingsFields', args=sgqlc.types.ArgDict((
        ('bug_field_id', sgqlc.types.Arg(Int, graphql_name='bugFieldId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `bug_field_id` (`Int`)None
    * `organization_id` (`UUID`)None
    '''

    bug_bulk_update_title = sgqlc.types.Field(BulkUpdateBugTitleMutation, graphql_name='bugBulkUpdateTitle', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `title` (`String`)None
    '''

    bug_bulk_update_mitigation_description = sgqlc.types.Field(BulkUpdateBugMitigationMutation, graphql_name='bugBulkUpdateMitigationDescription', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('mitigation', sgqlc.types.Arg(String, graphql_name='mitigation', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('steps_to_reproduce', sgqlc.types.Arg(String, graphql_name='stepsToReproduce', default=None)),
))
    )
    '''Arguments:

    * `description` (`String`)None (default: `null`)
    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `mitigation` (`String`)None (default: `null`)
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `steps_to_reproduce` (`String`)None (default: `null`)
    '''

    archive_bug_bulk_update = sgqlc.types.Field(BulkUpdateArchiveBugsMutation, graphql_name='archiveBugBulkUpdate', args=sgqlc.types.ArgDict((
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `is_active` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    bug_bulk_update_custom_fields = sgqlc.types.Field(BulkUpdateBugCustomFieldMutation, graphql_name='bugBulkUpdateCustomFields', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(GenericScalar, graphql_name='fields', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `fields` (`GenericScalar`)None (default: `null`)
    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    update_bugs_fields_with_csv = sgqlc.types.Field(BulkUpdateBugsFieldsWithCSVMutation, graphql_name='updateBugsFieldsWithCsv', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `file` (`Upload!`)None
    * `organization_id` (`UUID!`)None
    '''

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
    '''Arguments:

    * `asset_id` (`Int`)None
    * `asset_search_query` (`String`)None
    * `attack_vector` (`String`)None
    * `bug_attachment_list` (`[Int]`)None
    * `bug_level` (`Int!`)None
    * `cloud` (`JSONString`)None
    * `cloud_asset_type` (`Int`)None
    * `code` (`JSONString`)None
    * `config_id` (`Int`)None
    * `custom_fields` (`JSONString`)None
    * `cve_list` (`[String]`)None
    * `cvss` (`Float`)None
    * `cwe_list` (`[Int]`)None
    * `description` (`String!`)None
    * `engagement_id` (`String`)None
    * `engagement_ids` (`[String]`)None
    * `mitigation` (`String`)None
    * `mobile` (`JSONString`)None
    * `network` (`JSONString`)None
    * `organization_id` (`UUID!`)None
    * `package` (`JSONString`)None
    * `select_all_assets` (`Boolean`)None (default: `null`)
    * `selected_asset` (`Int`)None
    * `selected_assets` (`[Int]`)None
    * `selected_team` (`Int`)None (default: `null`)
    * `severity` (`Int`)None
    * `steps_to_reproduce` (`String`)None
    * `tags` (`[String]`)None
    * `title` (`String!`)None
    * `web` (`JSONString`)None
    '''

    sync_bug_with_trackers = sgqlc.types.Field('SyncBugWithTrackersMutation', graphql_name='syncBugWithTrackers', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`ID`)None
    * `search_query` (`String`)None
    '''

    assets_bulk_update = sgqlc.types.Field(BulkUpdateAssetsMutation, graphql_name='assetsBulkUpdate', args=sgqlc.types.ArgDict((
        ('exposed', sgqlc.types.Arg(Int, graphql_name='exposed', default=None)),
        ('group_by_field', sgqlc.types.Arg(String, graphql_name='groupByField', default=None)),
        ('group_by_value', sgqlc.types.Arg(String, graphql_name='groupByValue', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('sensitivity', sgqlc.types.Arg(Int, graphql_name='sensitivity', default=None)),
))
    )
    '''Arguments:

    * `exposed` (`Int`)None
    * `group_by_field` (`String`)None
    * `group_by_value` (`String`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `sensitivity` (`Int`)None
    '''

    assets_bulk_merge = sgqlc.types.Field(BulkMergeAssetsMutation, graphql_name='assetsBulkMerge', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('source_asset', sgqlc.types.Arg(Int, graphql_name='sourceAsset', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `source_asset` (`Int`)None
    '''

    assets_bulk_link = sgqlc.types.Field(BulkLinkAssetsMutation, graphql_name='assetsBulkLink', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('source_asset', sgqlc.types.Arg(Int, graphql_name='sourceAsset', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `source_asset` (`Int`)None
    '''

    assets_bulk_delete = sgqlc.types.Field(BulkDeleteAssetsMutation, graphql_name='assetsBulkDelete', args=sgqlc.types.ArgDict((
        ('is_archived_view', sgqlc.types.Arg(Boolean, graphql_name='isArchivedView', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `is_archived_view` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    assets_bulk_update_tags = sgqlc.types.Field(BulkUpdateAssetsTagMutation, graphql_name='assetsBulkUpdateTags', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `tags` (`[String]`)None
    '''

    archive_assets_bulk_update = sgqlc.types.Field(BulkUpdateArchiveAssetsMutation, graphql_name='archiveAssetsBulkUpdate', args=sgqlc.types.ArgDict((
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `is_active` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    assets_merge_preview = sgqlc.types.Field(BulkMergeAssetsPreviewMutation, graphql_name='assetsMergePreview', args=sgqlc.types.ArgDict((
        ('host_name', sgqlc.types.Arg(Boolean, graphql_name='hostName', default=None)),
        ('ip_address', sgqlc.types.Arg(Boolean, graphql_name='ipAddress', default=None)),
        ('mac_address', sgqlc.types.Arg(Boolean, graphql_name='macAddress', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `host_name` (`Boolean`)None
    * `ip_address` (`Boolean`)None
    * `mac_address` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    assets_merge_confirm = sgqlc.types.Field(BulkMergeAssetsConfirmMutation, graphql_name='assetsMergeConfirm', args=sgqlc.types.ArgDict((
        ('host_name', sgqlc.types.Arg(Boolean, graphql_name='hostName', default=None)),
        ('ip_address', sgqlc.types.Arg(Boolean, graphql_name='ipAddress', default=None)),
        ('mac_address', sgqlc.types.Arg(Boolean, graphql_name='macAddress', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `host_name` (`Boolean`)None
    * `ip_address` (`Boolean`)None
    * `mac_address` (`Boolean`)None
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    calculate_risk_score = sgqlc.types.Field(CalculateRiskScoreMutation, graphql_name='calculateRiskScore', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    software_packages_bulk_update = sgqlc.types.Field(BulkUpdateSoftwarePackageMutation, graphql_name='softwarePackagesBulkUpdate', args=sgqlc.types.ArgDict((
        ('installed_version', sgqlc.types.Arg(String, graphql_name='installedVersion', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('package_name', sgqlc.types.Arg(String, graphql_name='packageName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `installed_version` (`String`)None
    * `organization_id` (`UUID`)None
    * `package_name` (`String`)None
    * `search_query` (`String`)None
    '''

    software_packages_bulk_delete = sgqlc.types.Field(BulkDeleteSoftwarePackageMutation, graphql_name='softwarePackagesBulkDelete', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    software_package_create = sgqlc.types.Field(CreateSoftwarePackageMutation, graphql_name='softwarePackageCreate', args=sgqlc.types.ArgDict((
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('installed_version', sgqlc.types.Arg(String, graphql_name='installedVersion', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('package_name', sgqlc.types.Arg(String, graphql_name='packageName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `asset_id` (`Int`)None
    * `installed_version` (`String`)None
    * `organization_id` (`UUID`)None
    * `package_name` (`String`)None
    * `search_query` (`String`)None
    '''

    add_asset_settings_fields = sgqlc.types.Field(AddAssetFieldSettingsMutation, graphql_name='addAssetSettingsFields', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('field_type', sgqlc.types.Arg(Int, graphql_name='fieldType', default=None)),
        ('is_required', sgqlc.types.Arg(Boolean, graphql_name='isRequired', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='options', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `description` (`String`)None
    * `field_type` (`Int`)None
    * `is_required` (`Boolean`)None
    * `name` (`String`)None
    * `options` (`[String]`)None
    * `organization_id` (`UUID`)None
    '''

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
    '''Arguments:

    * `asset_field_id` (`Int`)None
    * `description` (`String`)None
    * `is_active` (`Boolean`)None
    * `is_required` (`Boolean`)None
    * `name` (`String`)None
    * `new_selected_option` (`String`)None
    * `old_selected_option` (`String`)None
    * `options` (`[String]`)None
    * `organization_id` (`UUID`)None
    '''

    delete_asset_settings_fields = sgqlc.types.Field(DeleteAssetFieldSettingsMutation, graphql_name='deleteAssetSettingsFields', args=sgqlc.types.ArgDict((
        ('asset_field_id', sgqlc.types.Arg(Int, graphql_name='assetFieldId', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `asset_field_id` (`Int`)None
    * `organization_id` (`UUID`)None
    '''

    bulk_update_asset_custom_field_mutation = sgqlc.types.Field(BulkUpdateAssetCustomFields, graphql_name='bulkUpdateAssetCustomFieldMutation', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(GenericScalar, graphql_name='fields', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `fields` (`GenericScalar`)None (default: `null`)
    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

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
        ('region', sgqlc.types.Arg(String, graphql_name='region', default=None)),
        ('account_id',sgqlc.types.Arg(String, graphql_name='account_id', default=None)),
        ('resource_id',sgqlc.types.Arg(String,graphql_name="resource_id",default=None)),
        

))
    )
    '''Arguments:

    * `cloud_type` (`Int`)None
    * `cpe` (`String`)None
    * `custom_fields` (`GenericScalar`)None
    * `excluded_ipaddress_list` (`[String]`)None
    * `exposed` (`Int`)None
    * `hostname` (`String`)None
    * `ipaddress` (`String`)None
    * `ipaddress_list` (`[String]`)None
    * `mac_address` (`String`)None
    * `name` (`String`)None
    * `organization_id` (`UUID`)None
    * `os` (`String`)None
    * `package` (`String`)None
    * `sensitivity` (`Int`)None
    * `tags` (`[String]`)None
    * `type` (`Int`)None
    * `url` (`String`)None
    * `region` (`String`)None
    * `account_id` (`String`)None
    * `resource_id` (`String`)None
    '''

    update_asset_fields_with_csv = sgqlc.types.Field(BulkUpdateAssetFieldsWithCSVMutation, graphql_name='updateAssetFieldsWithCsv', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `file` (`Upload!`)None
    * `organization_id` (`UUID!`)None
    '''

    bulk_asset_access_user_mutation = sgqlc.types.Field(BulkAssetAccessUserMutation, graphql_name='bulkAssetAccessUserMutation', args=sgqlc.types.ArgDict((
        ('asset_search_query', sgqlc.types.Arg(String, graphql_name='assetSearchQuery', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    '''Arguments:

    * `asset_search_query` (`String`)None
    * `organization_id` (`UUID`)None
    * `user_ids` (`[Int]`)None
    '''



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



class OrganizationMembersType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'user', 'organization', 'role', 'asset_search_query', 'permitted_apps', 'permitted_modules', 'default_page', 'preset_set', 'approval_approved_by', 'approval_raised_by', 'dashboards_set', 'widget_set', 'email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')

    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')

    role = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='role')

    asset_search_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetSearchQuery')

    permitted_apps = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='permittedApps')

    permitted_modules = sgqlc.types.Field(JSONString, graphql_name='permittedModules')

    default_page = sgqlc.types.Field(JSONString, graphql_name='defaultPage')

    preset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PresetType'))), graphql_name='presetSet')

    approval_approved_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalApprovedBy')

    approval_raised_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApprovalType))), graphql_name='approvalRaisedBy')

    dashboards_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='dashboardsSet')

    widget_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetSet')

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
    __field_names__ = ('id', 'package_name', 'affected_versions', 'installed_version', 'fixed_version', 'digest', 'commit', 'file_name', 'ecosystem', 'branch', 'batch_id', 'temp_id')
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



class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_engagements_fields', 'all_automation_worfklow_activities', 'all_automation_workflows', 'all_configurations', 'all_patches', 'all_azure_devops_repositories', 'all_package_asset_count', 'all_tickets', 'all_docker_registry_images', 'all_ecr_images', 'all_sla_rules', 'search_query_exist', 'weightage_exist', 'all_presets', 'all_data_retention_settings', 'all_grouped_bugs', 'all_grouped_assets', 'all_asm_settings', 'all_asset_fields', 'all_bug_fields', 'all_vault_attachments', 'all_widgets_v2', 'all_dashboards_v2', 'all_veracode_projects', 'all_logs', 'all_action_logs', 'all_prerequisites', 'all_software_packages', 'all_packages', 'all_bitbucket_repositories', 'all_github_repositories', 'all_black_duck_projects', 'all_engagements_comment_activities', 'all_attachments', 'all_assessments', 'all_approvals', 'all_assigned_user_views', 'check_view_name', 'all_report_attachments', 'all_prioritization_rules', 'all_bug_reports', 'download_report', 'preview_report', 'all_templates', 'default_templates', 'template_name_exist', 'all_widgets', 'all_assets_bugs_count_widget', 'all_software_packages_assets_bugs_count_widget', 'all_dashboards', 'all_groups', 'get_current_tenant', 'all_engagements', 'all_engagement_activities', 'all_engagements_activities', 'all_engagement_assets', 'all_engagement_bugs', 'all_nist', 'all_owasp', 'all_cve', 'all_cwe', 'pentesters_involved', 'all_tests', 'engagement_compliance_count', 'all_assets', 'all_bugs', 'close_findings', 'revert_closed_findings')
    all_engagements_fields = sgqlc.types.Field(EngagementFieldPaginatedType, graphql_name='allEngagementsFields', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_automation_worfklow_activities = sgqlc.types.Field(AutomationWorkflowActivityPaginatedType, graphql_name='allAutomationWorfklowActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_automation_workflows = sgqlc.types.Field(AutomationWorkflowPaginatedType, graphql_name='allAutomationWorkflows', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_configurations = sgqlc.types.Field(ConfigurationsPaginatedType, graphql_name='allConfigurations', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `order_by` (`[String]`)None
    * `search_query` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_patches = sgqlc.types.Field(PatchesPaginatedType, graphql_name='allPatches', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_azure_devops_repositories = sgqlc.types.Field(AzureDevopsRepositoriesTypePaginatedType, graphql_name='allAzureDevopsRepositories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('repo_name', sgqlc.types.Arg(String, graphql_name='repoName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('refresh', sgqlc.types.Arg(Boolean, graphql_name='refresh', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `cm_id` (`Int`)None
    * `repo_name` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `refresh` (`Boolean`)None
    '''

    all_package_asset_count = sgqlc.types.Field(PackageAssetPaginatedType, graphql_name='allPackageAssetCount', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_tickets = sgqlc.types.Field('TicketsPaginatedType', graphql_name='allTickets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_docker_registry_images = sgqlc.types.Field(DockerRegistryTypePaginatedType, graphql_name='allDockerRegistryImages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('image_name', sgqlc.types.Arg(String, graphql_name='imageName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `cm_id` (`Int`)None
    * `image_name` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_ecr_images = sgqlc.types.Field(ECRImagesTypePaginatedType, graphql_name='allEcrImages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('image_name', sgqlc.types.Arg(String, graphql_name='imageName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `cm_id` (`Int`)None
    * `image_name` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_sla_rules = sgqlc.types.Field('ServiceLevelAgreementCustomRulesPaginatedType', graphql_name='allSlaRules', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    search_query_exist = sgqlc.types.Field(Boolean, graphql_name='searchQueryExist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String!`)None
    '''

    weightage_exist = sgqlc.types.Field(Boolean, graphql_name='weightageExist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('weightage', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='weightage', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `weightage` (`Int!`)None
    '''

    all_presets = sgqlc.types.Field(sgqlc.types.list_of(PresetType), graphql_name='allPresets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    '''

    all_data_retention_settings = sgqlc.types.Field(sgqlc.types.list_of(DataRetentionSettingsType), graphql_name='allDataRetentionSettings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `group_by` (`String`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `after` (`String`)None
    * `before` (`String`)None
    '''

    all_grouped_assets = sgqlc.types.Field(GroupAssetPaginatedType, graphql_name='allGroupedAssets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('group_by', sgqlc.types.Arg(String, graphql_name='groupBy', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `group_by` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_asm_settings = sgqlc.types.Field(ASMSettingsType, graphql_name='allAsmSettings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('refresh_scope', sgqlc.types.Arg(Boolean, graphql_name='refreshScope', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `refresh_scope` (`Boolean`)None
    '''

    all_asset_fields = sgqlc.types.Field(AssetFieldPaginatedType, graphql_name='allAssetFields', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_bug_fields = sgqlc.types.Field(BugFieldPaginatedType, graphql_name='allBugFields', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_vault_attachments = sgqlc.types.Field('VaultPaginatedType', graphql_name='allVaultAttachments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `order_by` (`[String]`)None
    '''

    all_widgets_v2 = sgqlc.types.Field('WidgetsV2Type', graphql_name='allWidgetsV2', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('asset_filter_field_query', sgqlc.types.Arg(String, graphql_name='assetFilterFieldQuery', default=None)),
        ('bug_filter_field_query', sgqlc.types.Arg(String, graphql_name='bugFilterFieldQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `asset_filter_field_query` (`String`)None
    * `bug_filter_field_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_dashboards_v2 = sgqlc.types.Field(DashboardsV2Type, graphql_name='allDashboardsV2', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `slug` (`String`)None
    * `cm_id` (`Int`)None
    * `agent_id` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `search_query` (`String`)None
    '''

    all_logs = sgqlc.types.Field('ScanLogPaginatedType', graphql_name='allLogs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('log_type', sgqlc.types.Arg(String, graphql_name='logType', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `log_type` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_action_logs = sgqlc.types.Field(BotTaskPaginatedType, graphql_name='allActionLogs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_prerequisites = sgqlc.types.Field(PreRequisitesPaginatedType, graphql_name='allPrerequisites', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(String, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`String`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_software_packages = sgqlc.types.Field('SoftwarePackagePaginatedType', graphql_name='allSoftwarePackages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `asset_id` (`Int`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_packages = sgqlc.types.Field(PackagePaginatedType, graphql_name='allPackages', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_bitbucket_repositories = sgqlc.types.Field(BitbucketRepositoriesTypePaginatedType, graphql_name='allBitbucketRepositories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('repo_name', sgqlc.types.Arg(String, graphql_name='repoName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `cm_id` (`Int`)None
    * `repo_name` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_github_repositories = sgqlc.types.Field(GithubRepositoriesTypePaginatedType, graphql_name='allGithubRepositories', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('cm_id', sgqlc.types.Arg(Int, graphql_name='cmId', default=None)),
        ('repo_name', sgqlc.types.Arg(String, graphql_name='repoName', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('refresh', sgqlc.types.Arg(Boolean, graphql_name='refresh', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `cm_id` (`Int`)None
    * `repo_name` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `refresh` (`Boolean`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `slug` (`String`)None
    * `cm_id` (`Int`)None
    * `agent_id` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `search_query` (`String`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `assessment_state_last_updated` (`Boolean`)None
    * `assessment_id` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_attachments = sgqlc.types.Field(AttachmentPaginatedType, graphql_name='allAttachments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `asset_id` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_approvals = sgqlc.types.Field(ApprovalPaginatedType, graphql_name='allApprovals', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_assigned_user_views = sgqlc.types.Field(sgqlc.types.list_of(FilterViewsType), graphql_name='allAssignedUserViews', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `view_id` (`Int`)None
    '''

    check_view_name = sgqlc.types.Field(Boolean, graphql_name='checkViewName', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('is_asset_view', sgqlc.types.Arg(Boolean, graphql_name='isAssetView', default=None)),
        ('is_bug_view', sgqlc.types.Arg(Boolean, graphql_name='isBugView', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `name` (`String`)None
    * `is_asset_view` (`Boolean`)None
    * `is_bug_view` (`Boolean`)None
    '''

    all_report_attachments = sgqlc.types.Field('ReportAttachmentPaginatedType', graphql_name='allReportAttachments', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_prioritization_rules = sgqlc.types.Field(PrioritizationType, graphql_name='allPrioritizationRules', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    '''

    all_bug_reports = sgqlc.types.Field('ReportPaginatedType', graphql_name='allBugReports', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    download_report = sgqlc.types.Field('ReportType', graphql_name='downloadReport', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('export_id', sgqlc.types.Arg(UUID, graphql_name='exportId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `export_id` (`UUID`)None
    '''

    preview_report = sgqlc.types.Field(String, graphql_name='previewReport', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='templateId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('view_id', sgqlc.types.Arg(Int, graphql_name='viewId', default=None)),
        ('custom_data', sgqlc.types.Arg(JSONString, graphql_name='customData', default=None)),
        ('report_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reportName', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    * `template_id` (`Int!`)None
    * `engagement_id` (`UUID`)None
    * `view_id` (`Int`)None
    * `custom_data` (`JSONString`)None
    * `report_name` (`String!`)None
    * `search_query` (`String`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `search_query` (`String`)None
    * `template_id` (`Int`)None
    * `header_template` (`String`)None
    * `footer_template` (`String`)None
    '''

    default_templates = sgqlc.types.Field(GenericScalar, graphql_name='defaultTemplates')

    template_name_exist = sgqlc.types.Field(Boolean, graphql_name='templateNameExist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `name` (`String!`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `widgets` (`[String]`)None
    * `datetime` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `asset_view_id` (`Int`)None
    * `bug_view_id` (`Int`)None
    * `cache_refresh` (`Boolean`)None
    * `asset_search_query` (`String`)None
    * `bug_search_query` (`String`)None
    * `engagement_search_query` (`String`)None
    * `fetch_from_cache` (`Boolean`)None
    * `widget_filter` (`JSONString`)None
    * `is_archived_view` (`Boolean`)None
    * `scan_log_search_query` (`String`)None
    * `tracker_search_query` (`String`)None
    * `engagement_id` (`UUID`)None
    * `assessment_search_query` (`String`)None
    * `software_package_search_query` (`String`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `datetime` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `asset_view_id` (`Int`)None
    * `bug_view_id` (`Int`)None
    * `cache_refresh` (`Boolean`)None
    * `asset_search_query` (`String`)None
    * `bug_search_query` (`String`)None
    * `engagement_search_query` (`String`)None
    * `fetch_from_cache` (`Boolean`)None
    * `widget_filter` (`JSONString`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `datetime` (`Int`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `asset_view_id` (`Int`)None
    * `bug_view_id` (`Int`)None
    * `cache_refresh` (`Boolean`)None
    * `asset_search_query` (`String`)None
    * `bug_search_query` (`String`)None
    * `package_search_query` (`String`)None
    * `engagement_search_query` (`String`)None
    * `fetch_from_cache` (`Boolean`)None
    * `widget_filter` (`JSONString`)None
    '''

    all_dashboards = sgqlc.types.Field(GenericScalar, graphql_name='allDashboards')

    all_groups = sgqlc.types.Field(GroupPaginatedType, graphql_name='allGroups', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `export_report_type` (`String`)None
    * `order_by` (`[String]`)None
    * `asset_id` (`Int`)None
    * `export_with_log_hours` (`Boolean`)None (default: `false`)
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_engagement_activities = sgqlc.types.Field(EngagementCommentPaginatedType, graphql_name='allEngagementActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_engagements_activities = sgqlc.types.Field(EngagementCommentPaginatedType, graphql_name='allEngagementsActivities', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_engagement_assets = sgqlc.types.Field(EngagementAssetPaginatedType, graphql_name='allEngagementAssets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_engagement_bugs = sgqlc.types.Field(EngagementBugPaginatedType, graphql_name='allEngagementBugs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_nist = sgqlc.types.Field(NISTPaginatedType, graphql_name='allNist', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_owasp = sgqlc.types.Field(OWASPPaginatedType, graphql_name='allOwasp', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_cve = sgqlc.types.Field(CVEPaginatedType, graphql_name='allCve', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    all_cwe = sgqlc.types.Field(CWEPaginatedType, graphql_name='allCwe', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    pentesters_involved = sgqlc.types.Field('UserPaginatedType', graphql_name='pentestersInvolved', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `compliance_type` (`String`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

    engagement_compliance_count = sgqlc.types.Field(CompliancePaginatedType, graphql_name='engagementComplianceCount', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('engagement_id', sgqlc.types.Arg(UUID, graphql_name='engagementId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `engagement_id` (`UUID`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `export_report_type` (`String`)None
    * `after` (`String`)None
    * `before` (`String`)None
    * `selected_fields` (`[String]`)None
    * `group_by_field` (`String`)None
    * `group_by_value` (`String`)None
    * `preset_id` (`Int`)None
    * `exclude_search_query` (`String`)None
    '''

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
    '''Arguments:

    * `organization_id` (`UUID`)None
    * `search_query` (`String`)None
    * `order_by` (`[String]`)None
    * `page` (`Int`)None
    * `page_size` (`Int`)None
    * `export_report_type` (`String`)None
    * `after` (`String`)None
    * `before` (`String`)None
    * `selected_fields` (`[String]`)None
    * `group_by_field` (`String`)None
    * `group_by_value` (`[String]`)None
    * `preset_id` (`Int`)None
    '''

    close_findings = sgqlc.types.Field(CloseFindingType, graphql_name='closeFindings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('configuration_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='configurationId', default=None)),
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('view_id', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='viewId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    * `configuration_id` (`Int!`)None
    * `slug` (`String!`)None
    * `view_id` (`[Int]`)None
    '''

    revert_closed_findings = sgqlc.types.Field(CloseFindingType, graphql_name='revertClosedFindings', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='organizationId', default=None)),
        ('close_task_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='closeTaskId', default=None)),
))
    )
    '''Arguments:

    * `organization_id` (`UUID!`)None
    * `close_task_id` (`UUID!`)None
    '''



class ReferenceType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'tenant_cwe_references', 'tenant_cve_references', 'bug_references')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    tenant_cwe_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CWEType))), graphql_name='tenantCweReferences')

    tenant_cve_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='tenantCveReferences')

    bug_references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugReferences')



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
    __field_names__ = ('id', 'export_id', 'user', 'report_type', 'scan', 'report_name', 'report_path', 'file', 'created', 'status', 'bug_ids', 'asset_ids', 'organization', 'engagement', 'template', 'exported_app', 'html_report', 'revised_from', 'original_report', 'self_revised_from', 'self_original_report', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    export_id = sgqlc.types.Field(UUID, graphql_name='exportId')

    user = sgqlc.types.Field(ApprovalUserType, graphql_name='user')

    report_type = sgqlc.types.Field(String, graphql_name='reportType')

    scan = sgqlc.types.Field(AllScanLogType, graphql_name='scan')

    report_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reportName')

    report_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reportPath')

    file = sgqlc.types.Field(String, graphql_name='file')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    status = sgqlc.types.Field(String, graphql_name='status')

    bug_ids = sgqlc.types.Field(GenericScalar, graphql_name='bugIds')

    asset_ids = sgqlc.types.Field(GenericScalar, graphql_name='assetIds')

    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')

    engagement = sgqlc.types.Field(EngagementType, graphql_name='engagement')

    template = sgqlc.types.Field('TemplateType', graphql_name='template')

    exported_app = sgqlc.types.Field(String, graphql_name='exportedApp')

    html_report = sgqlc.types.Field(String, graphql_name='htmlReport')

    revised_from = sgqlc.types.Field('ReportType', graphql_name='revisedFrom')

    original_report = sgqlc.types.Field('ReportType', graphql_name='originalReport')

    self_revised_from = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='selfRevisedFrom')

    self_original_report = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ReportType'))), graphql_name='selfOriginalReport')

    url = sgqlc.types.Field(String, graphql_name='url')



class RestoreDefaultPriortizationRuleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rules',)
    rules = sgqlc.types.Field(PrioritizationType, graphql_name='rules')



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
    __field_names__ = ('id', 'package_name', 'affected_versions', 'installed_version', 'fixed_version', 'digest', 'commit', 'file_name', 'ecosystem', 'branch', 'batch_id', 'temp_id', 'total', 'open', 'closed', 'risk_score', 'info_open', 'info_closed', 'low_open', 'low_closed', 'medium_open', 'medium_closed', 'high_open', 'high_closed', 'critical_open', 'critical_closed')
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



class SyncBugWithTrackersMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'msg')
    success = sgqlc.types.Field(Boolean, graphql_name='success')

    msg = sgqlc.types.Field(String, graphql_name='msg')



class TagType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'slug', 'name', 'created', 'updated', 'organization', 'tenant_cve_tags', 'asset_tags', 'asmconfig_set', 'bug_tags')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    slug = sgqlc.types.Field(String, graphql_name='slug')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')

    tenant_cve_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='tenantCveTags')

    asset_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetTags')

    asmconfig_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ASMSettingsType))), graphql_name='asmconfigSet')

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
    __field_names__ = ('id', 'template_name', 'organization', 'custom_fields', 'html_content', 'is_active', 'is_editable', 'created_by', 'created', 'updated', 'header_template', 'footer_template', 'exportreport_set', 'html', 'header', 'footer')
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

    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportType))), graphql_name='exportreportSet')

    html = sgqlc.types.Field(String, graphql_name='html')

    header = sgqlc.types.Field(String, graphql_name='header')

    footer = sgqlc.types.Field(String, graphql_name='footer')



class TenantOrganizationType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('schema_name', 'id', 'name', 'is_primary', 'is_base_schema', 'industry', 'referer', 'members', 'image', 'employee_size', 'purpose_of_use', 'strobes_customer', 'account_details', 'billing_address', 'revenue', 'country', 'datacenter', 'created', 'updated', 'tenant_organization', 'organizationmember_set', 'asset_set', 'group_set', 'servicelevelagreementcustomrules_set', 'team_set', 'prioritizationrules_set', 'port_set', 'subscribed_org', 'engagements_set', 'engagementsfield_set', 'softwarepackages_set', 'vault_set', 'prerequisites_organization', 'assetfield_set', 'dataretentionsettings_set', 'configuration_organization', 'export_org', 'report_attachment_org', 'credential_manager_org', 'bottask_organization', 'preset_organization', 'organization', 'bug_set', 'trackers_set', 'filterviews_set', 'reporttemplates_set', 'bugfield_set', 'patch_set', 'dashboards_set', 'widget_set', 'dashboardtags_set', 'domain', 'is_verified')
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

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

    tenant_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TagType))), graphql_name='tenantOrganization')

    organizationmember_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationMembersType))), graphql_name='organizationmemberSet')

    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetSet')

    group_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupsType))), graphql_name='groupSet')

    servicelevelagreementcustomrules_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ServiceLevelAgreementCustomRulesType))), graphql_name='servicelevelagreementcustomrulesSet')

    team_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TeamType))), graphql_name='teamSet')

    prioritizationrules_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PrioritizationType))), graphql_name='prioritizationrulesSet')

    port_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PortType))), graphql_name='portSet')

    subscribed_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VendorType'))), graphql_name='subscribedOrg')

    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')

    engagementsfield_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementsFieldType))), graphql_name='engagementsfieldSet')

    softwarepackages_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PackageAssetType))), graphql_name='softwarepackagesSet')

    vault_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='vaultSet')

    prerequisites_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesOrganization')

    assetfield_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetFieldType))), graphql_name='assetfieldSet')

    dataretentionsettings_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DataRetentionSettingsType))), graphql_name='dataretentionsettingsSet')

    configuration_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationsFieldType))), graphql_name='configurationOrganization')

    export_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportType))), graphql_name='exportOrg')

    report_attachment_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportAttachmentType))), graphql_name='reportAttachmentOrg')

    credential_manager_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CredentialManagerType))), graphql_name='credentialManagerOrg')

    bottask_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BotTaskType))), graphql_name='bottaskOrganization')

    preset_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PresetType))), graphql_name='presetOrganization')

    organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='organization')

    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestsType'))), graphql_name='bugSet')

    trackers_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TicketType'))), graphql_name='trackersSet')

    filterviews_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterViewsType))), graphql_name='filterviewsSet')

    reporttemplates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TemplateType))), graphql_name='reporttemplatesSet')

    bugfield_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugFieldType))), graphql_name='bugfieldSet')

    patch_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PatchesType))), graphql_name='patchSet')

    dashboards_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardType))), graphql_name='dashboardsSet')

    widget_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WidgetV2Type'))), graphql_name='widgetSet')

    dashboardtags_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardsTagType))), graphql_name='dashboardtagsSet')

    domain = sgqlc.types.Field(String, graphql_name='domain')

    is_verified = sgqlc.types.Field(Boolean, graphql_name='isVerified')



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



class TrackersType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'config', 'url', 'issue_key', 'bug', 'organization', 'asset', 'patch', 'is_groupped_issues', 'grouped_by', 'last_log', 'tracker_slug', 'created', 'updated')
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

    tracker_slug = sgqlc.types.Field(String, graphql_name='trackerSlug')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')



class TransferEngagementBugMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of(BugType), graphql_name='bugs')



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
    __field_names__ = ('password', 'is_superuser', 'id', 'email', 'first_name', 'last_name', 'created', 'updated', 'is_superadmin', 'is_staff', 'is_active', 'activation_id', 'bio', 'profile_picture', 'cover_heading', 'linkedin_url', 'twitter_url', 'designation', 'phone_number', 'last_login', 'username', 'org_members', 'organizationmember_set', 'asset_set', 'group_set', 'engagements_set', 'assessment_asset_assigned_to', 'vault_set', 'prerequisites_assigned_to', 'prerequisites_user', 'configurations_set', 'scanlog_set', 'exportreport_set', 'reportattachment_set', 'credentialmanager_set', 'bottask_set', 'automationworkflows_set', 'assigned_to', 'reported_by', 'attachment_set', 'activity_set', 'comment_set', 'filterviews_set', 'views_members', 'reporttemplates_set')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')

    is_superuser = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperuser')
    '''Designates that this user has all permissions without explicitly
    assigning them.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')

    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')

    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')

    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')

    is_superadmin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperadmin')

    is_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStaff')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    '''Designates whether this user should be treated as active. Un-
    select this instead of deleting accounts.
    '''

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

    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')

    assessment_asset_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssessmentType))), graphql_name='assessmentAssetAssignedTo')

    vault_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VaultType'))), graphql_name='vaultSet')

    prerequisites_assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesAssignedTo')

    prerequisites_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PreRequisitesType))), graphql_name='prerequisitesUser')

    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationsFieldType))), graphql_name='configurationsSet')

    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllScanLogType))), graphql_name='scanlogSet')

    exportreport_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportType))), graphql_name='exportreportSet')

    reportattachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReportAttachmentType))), graphql_name='reportattachmentSet')

    credentialmanager_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CredentialManagerType))), graphql_name='credentialmanagerSet')

    bottask_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BotTaskType))), graphql_name='bottaskSet')

    automationworkflows_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AutomationWorkflowType))), graphql_name='automationworkflowsSet')

    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TestsType))), graphql_name='assignedTo')

    reported_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TestsType))), graphql_name='reportedBy')

    attachment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentType))), graphql_name='attachmentSet')

    activity_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementActivityType))), graphql_name='activitySet')

    comment_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementCommentType))), graphql_name='commentSet')

    filterviews_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterViewsType))), graphql_name='filterviewsSet')

    views_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterViewsType))), graphql_name='viewsMembers')

    reporttemplates_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TemplateType))), graphql_name='reporttemplatesSet')



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

    created_by = sgqlc.types.Field(OrganizationMembersType, graphql_name='createdBy')

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




########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

