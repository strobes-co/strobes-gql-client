import sgqlc.types
import sgqlc.types.datetime


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSONString(sgqlc.types.Scalar):
    __schema__ = schema


class ParentConnectorsType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('A_0', 'A_1', 'A_10', 'A_11', 'A_12', 'A_2', 'A_3', 'A_4', 'A_5', 'A_6', 'A_7', 'A_8', 'A_9')


String = sgqlc.types.String

class UUID(sgqlc.types.Scalar):
    __schema__ = schema



########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class AddBulkCommentsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bugs',)
    bugs = sgqlc.types.Field(sgqlc.types.list_of('BugType'), graphql_name='bugs')


class AddGroupMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups',)
    groups = sgqlc.types.Field(sgqlc.types.list_of('GroupsType'), graphql_name='groups')


class AssetPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('AssetType'), graphql_name='objects')


class AssetType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'target', 'exposed', 'type', 'cloud_type', 'organization', 'disabled', 'sensitivity', 'keys', 'data', 'created_by', 'linked_assets', 'additional_info', 'scan', 'temp_id', 'created', 'updated', 'tags', 'location', 'lined_assets', 'group_assets', 'engagement_assets', 'configuration_asset', 'bug_set', 'ipaddress', 'hostname', 'mac_address', 'os')
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
    created_by = sgqlc.types.Field('UserType', graphql_name='createdBy')
    linked_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='linkedAssets')
    additional_info = sgqlc.types.Field(JSONString, graphql_name='additionalInfo')
    scan = sgqlc.types.Field('ScanLog', graphql_name='scan')
    temp_id = sgqlc.types.Field(UUID, graphql_name='tempId')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='tags')
    location = sgqlc.types.Field(String, graphql_name='location')
    lined_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssetType'))), graphql_name='linedAssets')
    group_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GroupsType'))), graphql_name='groupAssets')
    engagement_assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EngagementType'))), graphql_name='engagementAssets')
    configuration_asset = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConfigurationType'))), graphql_name='configurationAsset')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BugType'))), graphql_name='bugSet')
    ipaddress = sgqlc.types.Field(String, graphql_name='ipaddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    mac_address = sgqlc.types.Field(String, graphql_name='macAddress')
    os = sgqlc.types.Field(String, graphql_name='os')


class BugPaginatedType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page', 'total_pages', 'page_size', 'total_count', 'has_next', 'has_prev', 'objects')
    page = sgqlc.types.Field(Int, graphql_name='page')
    total_pages = sgqlc.types.Field(Int, graphql_name='totalPages')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    has_next = sgqlc.types.Field(Boolean, graphql_name='hasNext')
    has_prev = sgqlc.types.Field(Boolean, graphql_name='hasPrev')
    objects = sgqlc.types.Field(sgqlc.types.list_of('BugType'), graphql_name='objects')


class BugType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('state', 'severity', 'bug_level', 'id', 'title', 'description', 'mitigation', 'steps_to_reproduce', 'object_id', 'hash', 'duplicate', 'cwe', 'cve', 'cvss', 'attack_vector', 'bug_tags', 'assigned_to', 'organization', 'asset', 'team', 'reported_by', 'due_date', 'sla_violated', 'has_user_defined_due_date', 'exploit_available', 'exploit_info', 'patch_available', 'patch_info', 'prioritization_score', 'prioritization_score_calculated', 'drill_down_score', 'connector', 'configuration_name', 'connector_config', 'scan', 'scanner_raw_response', 'vulnerable_since', 'engagement', 'created', 'updated', 'original_bug', 'ipaddress', 'hostname', 'mac_address', 'os')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')
    severity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='severity')
    bug_level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bugLevel')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    mitigation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mitigation')
    steps_to_reproduce = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stepsToReproduce')
    object_id = sgqlc.types.Field(Int, graphql_name='objectId')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    duplicate = sgqlc.types.Field('BugType', graphql_name='duplicate')
    cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CWEType'))), graphql_name='cwe')
    cve = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CVEType'))), graphql_name='cve')
    cvss = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cvss')
    attack_vector = sgqlc.types.Field(String, graphql_name='attackVector')
    bug_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='bugTags')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserType'))), graphql_name='assignedTo')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    asset = sgqlc.types.Field(AssetType, graphql_name='asset')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    reported_by = sgqlc.types.Field('UserType', graphql_name='reportedBy')
    due_date = sgqlc.types.Field(DateTime, graphql_name='dueDate')
    sla_violated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slaViolated')
    has_user_defined_due_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasUserDefinedDueDate')
    exploit_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exploitAvailable')
    exploit_info = sgqlc.types.Field(JSONString, graphql_name='exploitInfo')
    patch_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='patchAvailable')
    patch_info = sgqlc.types.Field(JSONString, graphql_name='patchInfo')
    prioritization_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritizationScore')
    prioritization_score_calculated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='prioritizationScoreCalculated')
    drill_down_score = sgqlc.types.Field(JSONString, graphql_name='drillDownScore')
    connector = sgqlc.types.Field('ConnectorType', graphql_name='connector')
    configuration_name = sgqlc.types.Field(String, graphql_name='configurationName')
    connector_config = sgqlc.types.Field('ConfigurationType', graphql_name='connectorConfig')
    scan = sgqlc.types.Field('ScanLog', graphql_name='scan')
    scanner_raw_response = sgqlc.types.Field(JSONString, graphql_name='scannerRawResponse')
    vulnerable_since = sgqlc.types.Field(DateTime, graphql_name='vulnerableSince')
    engagement = sgqlc.types.Field('EngagementType', graphql_name='engagement')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    original_bug = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BugType'))), graphql_name='originalBug')
    ipaddress = sgqlc.types.Field(String, graphql_name='ipaddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    mac_address = sgqlc.types.Field(String, graphql_name='macAddress')
    os = sgqlc.types.Field(String, graphql_name='os')


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


class BulkDeleteTeamMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('members',)
    members = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='members')


class BulkLinkAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkMergeAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkUpdateAssetsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.list_of(AssetType), graphql_name='assets')


class BulkUpdateBugCVEMutation(sgqlc.types.Type):
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


class BulkUpdateOrgMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('users',)
    users = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='users')


class BulkUpdateTeamMemberRoleMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('users',)
    users = sgqlc.types.Field(sgqlc.types.list_of('MemberType'), graphql_name='users')


class CVEType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'description', 'cvss_v2_data', 'cvss_v3_data', 'cvss', 'cve_id', 'cve_tags', 'related_cwe', 'exploit_available', 'exploit_info', 'patch_available', 'patch_info', 'zero_day_available', 'is_wormable', 'ti_raw_response', 'summary', 'published', 'last_modified', 'created', 'updated', 'bug_cve')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    cvss_v2_data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='cvssV2Data')
    cvss_v3_data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='cvssV3Data')
    cvss = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cvss')
    cve_id = sgqlc.types.Field(String, graphql_name='cveId')
    cve_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagType'))), graphql_name='cveTags')
    related_cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CWEType'))), graphql_name='relatedCwe')
    exploit_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exploitAvailable')
    exploit_info = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='exploitInfo')
    patch_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='patchAvailable')
    patch_info = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='patchInfo')
    zero_day_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='zeroDayAvailable')
    is_wormable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isWormable')
    ti_raw_response = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='tiRawResponse')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    published = sgqlc.types.Field(DateTime, graphql_name='published')
    last_modified = sgqlc.types.Field(DateTime, graphql_name='lastModified')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    bug_cve = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='bugCve')


class CWEType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'cwe_id', 'type', 'cwe_tags', 'bug_cwe')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cwe_id = sgqlc.types.Field(String, graphql_name='cweId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    cwe_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='cweTags')
    bug_cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='bugCwe')


class ConfigurationType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'connector', 'organization', 'asset', 'team', 'object_id', 'key', 'remote_access_id', 'remote_access_url', 'created_by', 'is_default', 'created', 'updated', 'extra', 'scanlog_set', 'bug_set')
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
    created_by = sgqlc.types.Field('UserType', graphql_name='createdBy')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    scanlog_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ScanLog'))), graphql_name='scanlogSet')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='bugSet')


class ConnectorType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'slug', 'name', 'description', 'short_description', 'usage', 'image', 'link', 'type', 'is_internal', 'is_active', 'created', 'updated', 'configurations_set', 'parent_connector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')
    usage = sgqlc.types.Field(String, graphql_name='usage')
    image = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='image')
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')
    type = sgqlc.types.Field(sgqlc.types.non_null(ParentConnectorsType), graphql_name='type')
    is_internal = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInternal')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationType))), graphql_name='configurationsSet')
    parent_connector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='parentConnector')


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
    __field_names__ = ('id', 'service', 'package', 'assessment_data', 'state', 'security_posture', 'assets', 'created_by', 'organization', 'scheduled_date', 'created', 'updated', 'bug_engagement')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    service = sgqlc.types.Field(String, graphql_name='service')
    package = sgqlc.types.Field(String, graphql_name='package')
    assessment_data = sgqlc.types.Field(JSONString, graphql_name='assessmentData')
    state = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='state')
    security_posture = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='securityPosture')
    assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assets')
    created_by = sgqlc.types.Field('UserType', graphql_name='createdBy')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    scheduled_date = sgqlc.types.Field(DateTime, graphql_name='scheduledDate')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    bug_engagement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='bugEngagement')


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
    created_by = sgqlc.types.Field('UserType', graphql_name='createdBy')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')


class MemberType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'user', 'organization', 'role')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field('UserType', graphql_name='user')
    organization = sgqlc.types.Field(sgqlc.types.non_null('TenantOrganizationType'), graphql_name='organization')
    role = sgqlc.types.Field(String, graphql_name='role')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('add_group', 'update_group', 'group_bulk_delete', 'org_member_role_bulk_update', 'team_member_role_bulk_update', 'org_member_role_bulk_delete', 'team_member_role_bulk_delete', 'bug_bulk_update', 'bug_bulk_assignment', 'bug_bulk_unassignment', 'bug_bulk_update_tags', 'bug_bulk_update_cve', 'bug_bulk_delete', 'add_bulk_comment', 'assets_bulk_update', 'assets_bulk_merge', 'assets_bulk_link', 'assets_bulk_delete')
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
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('role', sgqlc.types.Arg(Int, graphql_name='role', default=None)),
        ('team_id', sgqlc.types.Arg(Int, graphql_name='teamId', default=None)),
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
    bug_bulk_update = sgqlc.types.Field(BulkUpdateBugMutation, graphql_name='bugBulkUpdate', args=sgqlc.types.ArgDict((
        ('cvss', sgqlc.types.Arg(Float, graphql_name='cvss', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('severity', sgqlc.types.Arg(Int, graphql_name='severity', default=None)),
        ('state', sgqlc.types.Arg(Int, graphql_name='state', default=None)),
))
    )
    bug_bulk_assignment = sgqlc.types.Field(BulkBugAssignmentMutation, graphql_name='bugBulkAssignment', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    bug_bulk_unassignment = sgqlc.types.Field(BulkBugUnAssignmentMutation, graphql_name='bugBulkUnassignment', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='userIds', default=None)),
))
    )
    bug_bulk_update_tags = sgqlc.types.Field(BulkUpdateBugTagMutation, graphql_name='bugBulkUpdateTags', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    bug_bulk_update_cve = sgqlc.types.Field(BulkUpdateBugCVEMutation, graphql_name='bugBulkUpdateCve', args=sgqlc.types.ArgDict((
        ('cves', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='cves', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    bug_bulk_delete = sgqlc.types.Field(BulkDeleteBugMutation, graphql_name='bugBulkDelete', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    add_bulk_comment = sgqlc.types.Field(AddBulkCommentsMutation, graphql_name='addBulkComment', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('internal', sgqlc.types.Arg(Boolean, graphql_name='internal', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )
    assets_bulk_update = sgqlc.types.Field(BulkUpdateAssetsMutation, graphql_name='assetsBulkUpdate', args=sgqlc.types.ArgDict((
        ('exposed', sgqlc.types.Arg(Int, graphql_name='exposed', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('sensitivity', sgqlc.types.Arg(Int, graphql_name='sensitivity', default=None)),
))
    )
    assets_bulk_merge = sgqlc.types.Field(BulkMergeAssetsMutation, graphql_name='assetsBulkMerge', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('source_asset', sgqlc.types.Arg(Int, graphql_name='sourceAsset', default=None)),
))
    )
    assets_bulk_link = sgqlc.types.Field(BulkLinkAssetsMutation, graphql_name='assetsBulkLink', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('source_asset', sgqlc.types.Arg(Int, graphql_name='sourceAsset', default=None)),
))
    )
    assets_bulk_delete = sgqlc.types.Field(BulkDeleteAssetsMutation, graphql_name='assetsBulkDelete', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_groups', 'get_current_tenant', 'all_engagements', 'all_assets', 'all_bugs')
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
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('asset_id', sgqlc.types.Arg(Int, graphql_name='assetId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    all_assets = sgqlc.types.Field(AssetPaginatedType, graphql_name='allAssets', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('group_id', sgqlc.types.Arg(Int, graphql_name='groupId', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('export_report_type', sgqlc.types.Arg(String, graphql_name='exportReportType', default=None)),
))
    )
    all_bugs = sgqlc.types.Field(BugPaginatedType, graphql_name='allBugs', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(UUID, graphql_name='organizationId', default=None)),
        ('search_query', sgqlc.types.Arg(String, graphql_name='searchQuery', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('export_report_type', sgqlc.types.Arg(String, graphql_name='exportReportType', default=None)),
))
    )


class ScanLog(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'config', 'finished', 'connector_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    config = sgqlc.types.Field(String, graphql_name='config')
    finished = sgqlc.types.Field(DateTime, graphql_name='finished')
    connector_name = sgqlc.types.Field(String, graphql_name='connectorName')


class TagType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'slug', 'name', 'organization', 'created', 'updated', 'asset_tags', 'cve_tags', 'bug_tags')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    asset_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetTags')
    cve_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CVEType))), graphql_name='cveTags')
    bug_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='bugTags')


class TeamType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'organization', 'created', 'updated', 'configuration_team', 'team')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization = sgqlc.types.Field('TenantOrganizationType', graphql_name='organization')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    configuration_team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationType))), graphql_name='configurationTeam')
    team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='team')


class TenantOrganizationType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('schema_name', 'id', 'name', 'is_primary', 'industry', 'members', 'image', 'employee_size', 'purpose_of_use', 'created', 'updated', 'organizationmember_set', 'asset_set', 'group_set', 'team_set', 'tags_set', 'engagements_set', 'configuration_organization', 'bug_set', 'domain', 'is_verified')
    schema_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='schemaName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrimary')
    industry = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='industry')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserType'))), graphql_name='members')
    image = sgqlc.types.Field(String, graphql_name='image')
    employee_size = sgqlc.types.Field(Int, graphql_name='employeeSize')
    purpose_of_use = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='purposeOfUse')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    organizationmember_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MemberType))), graphql_name='organizationmemberSet')
    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetSet')
    group_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupsType))), graphql_name='groupSet')
    team_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TeamType))), graphql_name='teamSet')
    tags_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TagType))), graphql_name='tagsSet')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')
    configuration_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationType))), graphql_name='configurationOrganization')
    bug_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='bugSet')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    is_verified = sgqlc.types.Field(Boolean, graphql_name='isVerified')


class UpdateGroupMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('groups',)
    groups = sgqlc.types.Field(sgqlc.types.list_of(GroupsType), graphql_name='groups')


class UserType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('password', 'last_login', 'is_superuser', 'id', 'email', 'first_name', 'last_name', 'created', 'updated', 'is_superadmin', 'is_staff', 'is_active', 'activation_id', 'org_members', 'organizationmember_set', 'asset_set', 'group_set', 'engagements_set', 'configurations_set', 'assigned_to', 'reported_by')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    last_login = sgqlc.types.Field(DateTime, graphql_name='lastLogin')
    is_superuser = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperuser')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')
    created = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='created')
    updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updated')
    is_superadmin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuperadmin')
    is_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStaff')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    activation_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='activationId')
    org_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TenantOrganizationType))), graphql_name='orgMembers')
    organizationmember_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MemberType))), graphql_name='organizationmemberSet')
    asset_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AssetType))), graphql_name='assetSet')
    group_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupsType))), graphql_name='groupSet')
    engagements_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EngagementType))), graphql_name='engagementsSet')
    configurations_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConfigurationType))), graphql_name='configurationsSet')
    assigned_to = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='assignedTo')
    reported_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BugType))), graphql_name='reportedBy')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

