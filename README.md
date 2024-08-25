# StrobesGQLClient 

StrobesGQL client is a python wrapper around Strobes graphql


# Schema Types

<details>
  <summary><strong>Table of Contents</strong></summary>

  * [Query](#query)
  * [Mutation](#mutation)
  * [Objects](#objects)
    * [AddBulkCommentsMutation](#addbulkcommentsmutation)
    * [AddGroupMutation](#addgroupmutation)
    * [AssetCursorPaginatedType](#assetcursorpaginatedtype)
    * [AssetType](#assettype)
    * [BugCursorPaginatedType](#bugcursorpaginatedtype)
    * [BugType](#bugtype)
    * [BulkBugAssignmentMutation](#bulkbugassignmentmutation)
    * [BulkBugUnAssignmentMutation](#bulkbugunassignmentmutation)
    * [BulkDeleteAssetsMutation](#bulkdeleteassetsmutation)
    * [BulkDeleteBugMutation](#bulkdeletebugmutation)
    * [BulkDeleteGroupMutation](#bulkdeletegroupmutation)
    * [BulkDeleteOrgMemberRoleMutation](#bulkdeleteorgmemberrolemutation)
    * [BulkDeleteTeamMemberRoleMutation](#bulkdeleteteammemberrolemutation)
    * [BulkLinkAssetsMutation](#bulklinkassetsmutation)
    * [BulkMergeAssetsMutation](#bulkmergeassetsmutation)
    * [BulkUpdateAssetsMutation](#bulkupdateassetsmutation)
    * [BulkUpdateBugCVEMutation](#bulkupdatebugcvemutation)
    * [BulkUpdateBugMutation](#bulkupdatebugmutation)
    * [BulkUpdateBugTagMutation](#bulkupdatebugtagmutation)
    * [BulkUpdateOrgMemberRoleMutation](#bulkupdateorgmemberrolemutation)
    * [BulkUpdateTeamMemberRoleMutation](#bulkupdateteammemberrolemutation)
    * [UpdateEngagementMutation](#updateengagementmutation)
    * [UpdateAssessmentMutation](#updateassessmentmutation)
    * [BulkAssessmentMutation](#bulkassessmentmutation)
    * [CVEType](#cvetype)
    * [CWEType](#cwetype)
    * [ConfigurationType](#configurationtype)
    * [ConnectorType](#connectortype)
    * [EngagementPaginatedType](#engagementpaginatedtype)
    * [EngagementType](#engagementtype)
    * [GroupPaginatedType](#grouppaginatedtype)
    * [GroupsType](#groupstype)
    * [MemberType](#membertype)
    * [ScanLog](#scanlog)
    * [TagType](#tagtype)
    * [TeamType](#teamtype)
    * [TenantOrganizationType](#tenantorganizationtype)
    * [UpdateGroupMutation](#updategroupmutation)
    * [UserType](#usertype)
    * [EngagementCommentPaginatedType](#engagementcommentpaginatedtype)
    * [EngagementActivityType](#engagementactivitytype)
    * [EngagementCommentType](#engagementcommenttype)
    * [AssessmentPaginatedType](#assessmentpaginatedtype)
    * [AssessmentType](#assessmenttype)
    * [ApprovalUserType](#approvalusertype)
    * [ApprovalType](#approvaltype)
    * [AttachmentType](#attachmenttype)
  * [Enums](#enums)
    * [ParentConnectorsType](#parentconnectorstype)
  * [Scalars](#scalars)
    * [Boolean](#boolean)
    * [DateTime](#datetime)
    * [Date](#date)
    * [Float](#float)
    * [ID](#id)
    * [Int](#int)
    * [JSONString](#jsonstring)
    * [String](#string)
    * [UUID](#uuid)

</details>

## Query
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>allGroups</strong></td>
<td valign="top"><a href="#grouppaginatedtype">GroupPaginatedType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">page</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pageSize</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCurrentTenant</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>allEngagements</strong></td>
<td valign="top"><a href="#engagementpaginatedtype">EngagementPaginatedType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">searchQuery</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">orderBy</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">assetId</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">page</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pageSize</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>allAssets</strong></td>
<td valign="top"><a href="#assetcursorpaginatedtype">AssetCursorPaginatedType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">searchQuery</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">orderBy</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupId</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">page</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pageSize</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">exportReportType</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>allBugs</strong></td>
<td valign="top"><a href="#bugcursorpaginatedtype">BugCursorPaginatedType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">searchQuery</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">orderBy</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">page</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pageSize</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">exportReportType</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>

<tr>
<td colspan="2" valign="top"><strong>allEngagementActivities</strong></td>
<td valign="top"><a href="#engagementcommentpaginatedtype">EngagementCommentPaginatedType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">engagementId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">searchQuery</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">orderBy</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">page</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pageSize</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>



<tr>
<td colspan="2" valign="top"><strong>allAssessments</strong></td>
<td valign="top"><a href="#assessmentpaginatedtype">AssessmentPaginatedType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">engagementId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">searchQuery</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">orderBy</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">assetId</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">page</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pageSize</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>€

</tbody>
</table>

## Mutation
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>addGroup</strong></td>
<td valign="top"><a href="#addgroupmutation">AddGroupMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">assetIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">name</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateGroup</strong></td>
<td valign="top"><a href="#updategroupmutation">UpdateGroupMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">assetIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupId</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">name</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>groupBulkDelete</strong></td>
<td valign="top"><a href="#bulkdeletegroupmutation">BulkDeleteGroupMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>orgMemberRoleBulkUpdate</strong></td>
<td valign="top"><a href="#bulkupdateorgmemberrolemutation">BulkUpdateOrgMemberRoleMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">role</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>teamMemberRoleBulkUpdate</strong></td>
<td valign="top"><a href="#bulkupdateteammemberrolemutation">BulkUpdateTeamMemberRoleMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">role</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">teamId</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>orgMemberRoleBulkDelete</strong></td>
<td valign="top"><a href="#bulkdeleteorgmemberrolemutation">BulkDeleteOrgMemberRoleMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>teamMemberRoleBulkDelete</strong></td>
<td valign="top"><a href="#bulkdeleteteammemberrolemutation">BulkDeleteTeamMemberRoleMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">teamId</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugBulkUpdate</strong></td>
<td valign="top"><a href="#bulkupdatebugmutation">BulkUpdateBugMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cvss</td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">severity</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">state</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugBulkAssignment</strong></td>
<td valign="top"><a href="#bulkbugassignmentmutation">BulkBugAssignmentMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugBulkUnassignment</strong></td>
<td valign="top"><a href="#bulkbugunassignmentmutation">BulkBugUnAssignmentMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugBulkUpdateTags</strong></td>
<td valign="top"><a href="#bulkupdatebugtagmutation">BulkUpdateBugTagMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tags</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugBulkUpdateCve</strong></td>
<td valign="top"><a href="#bulkupdatebugcvemutation">BulkUpdateBugCVEMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cves</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugBulkDelete</strong></td>
<td valign="top"><a href="#bulkdeletebugmutation">BulkDeleteBugMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addBulkComment</strong></td>
<td valign="top"><a href="#addbulkcommentsmutation">AddBulkCommentsMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">comment</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">internal</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetsBulkUpdate</strong></td>
<td valign="top"><a href="#bulkupdateassetsmutation">BulkUpdateAssetsMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">exposed</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sensitivity</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetsBulkMerge</strong></td>
<td valign="top"><a href="#bulkmergeassetsmutation">BulkMergeAssetsMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sourceAsset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetsBulkLink</strong></td>
<td valign="top"><a href="#bulklinkassetsmutation">BulkLinkAssetsMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sourceAsset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetsBulkDelete</strong></td>
<td valign="top"><a href="#bulkdeleteassetsmutation">BulkDeleteAssetsMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ids</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>


<tr>
<td colspan="2" valign="top"><strong>updateEngagement</strong></td>
<td valign="top"><a href="#updateengagementmutation">UpdateEngagementMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">addAssetIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">addDocumentIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">comment</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">commentAttachments</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deliveryDate</td>
<td valign="top"><a href="#date">Date</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">scheduledDate</td>
<td valign="top"><a href="#date">Date</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">engagementId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">instructions</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">name</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">service</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">package</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">removeAssetIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">removeDocumentIds</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">subscribedServices</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">testAccounts</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">vpnAccounts</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateAssessments</strong></td>
<td valign="top"><a href="#updateassessmentmutation">UpdateAssessmentMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">assessmentId</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">assignedTo</td>
<td valign="top">[<a href="#int">Int</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">engagementId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">instructions</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">state</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">testAccounts</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">vpnAccounts</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bulkUpdateAssessment</strong></td>
<td valign="top"><a href="#bulkassessmentmutation">BulkAssessmentMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">engagementId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">organizationId</td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">state</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">searchQuery</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

## Objects

### AddBulkCommentsMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### AddGroupMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groups</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### AssetCursorPaginatedType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>beforeCursor</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastCursor</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasNext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasPrevious</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objects</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### AssetType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>exposed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cloudType</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>disabled</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sensitivity</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>keys</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdBy</strong></td>
<td valign="top"><a href="#usertype">UserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>linkedAssets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>additionalInfo</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>scan</strong></td>
<td valign="top"><a href="#scanlog">ScanLog</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tempId</strong></td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tags</strong></td>
<td valign="top">[<a href="#tagtype">TagType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>location</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>linedAssets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>groupAssets</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagementAssets</strong></td>
<td valign="top">[<a href="#engagementtype">EngagementType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>configurationAsset</strong></td>
<td valign="top">[<a href="#configurationtype">ConfigurationType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugSet</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ipaddress</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hostname</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>macAddress</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>os</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### BugCursorPaginatedType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>beforeCursor</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastCursor</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasNext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasPrevious</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objects</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BugType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>state</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>severity</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugLevel</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>mitigation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stepsToReproduce</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objectId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hash</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>duplicate</strong></td>
<td valign="top"><a href="#bugtype">BugType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cwe</strong></td>
<td valign="top">[<a href="#cwetype">CWEType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cve</strong></td>
<td valign="top">[<a href="#cvetype">CVEType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cvss</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>attackVector</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugTags</strong></td>
<td valign="top">[<a href="#tagtype">TagType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assignedTo</strong></td>
<td valign="top">[<a href="#usertype">UserType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>asset</strong></td>
<td valign="top"><a href="#assettype">AssetType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>team</strong></td>
<td valign="top"><a href="#teamtype">TeamType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reportedBy</strong></td>
<td valign="top"><a href="#usertype">UserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>dueDate</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>slaViolated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasUserDefinedDueDate</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>exploitAvailable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>exploitInfo</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>patchAvailable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>patchInfo</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>prioritizationScore</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>prioritizationScoreCalculated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>drillDownScore</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connector</strong></td>
<td valign="top"><a href="#connectortype">ConnectorType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>configurationName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connectorConfig</strong></td>
<td valign="top"><a href="#configurationtype">ConfigurationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>scan</strong></td>
<td valign="top"><a href="#scanlog">ScanLog</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>scannerRawResponse</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>vulnerableSince</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagement</strong></td>
<td valign="top"><a href="#engagementtype">EngagementType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>originalBug</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ipaddress</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hostname</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>macAddress</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>os</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### BulkBugAssignmentMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkBugUnAssignmentMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkDeleteAssetsMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>assets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkDeleteBugMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkDeleteGroupMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groups</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkDeleteOrgMemberRoleMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>members</strong></td>
<td valign="top">[<a href="#membertype">MemberType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkDeleteTeamMemberRoleMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>members</strong></td>
<td valign="top">[<a href="#membertype">MemberType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkLinkAssetsMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>assets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkMergeAssetsMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>assets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkUpdateAssetsMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>assets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkUpdateBugCVEMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkUpdateBugMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkUpdateBugTagMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bugs</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkUpdateOrgMemberRoleMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>users</strong></td>
<td valign="top">[<a href="#membertype">MemberType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkUpdateTeamMemberRoleMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>users</strong></td>
<td valign="top">[<a href="#membertype">MemberType</a>]</td>
<td></td>
</tr>
</tbody>
</table>


### UpdateEngagementMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>engagement</strong></td>
<td valign="top">[<a href="#engagementtype">EngagementType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### UpdateAssessmentMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>assessment</strong></td>
<td valign="top">[<a href="#assessmenttype">AssessmentType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### BulkAssessmentMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>assessment</strong></td>
<td valign="top">[<a href="#assessmenttype">AssessmentType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### CVEType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cvssV2Data</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cvssV3Data</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cvss</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cveId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cveTags</strong></td>
<td valign="top">[<a href="#tagtype">TagType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relatedCwe</strong></td>
<td valign="top">[<a href="#cwetype">CWEType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>exploitAvailable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>exploitInfo</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>patchAvailable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>patchInfo</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zeroDayAvailable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isWormable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tiRawResponse</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>published</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastModified</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugCve</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### CWEType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cweId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cweTags</strong></td>
<td valign="top">[<a href="#cvetype">CVEType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugCwe</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ConfigurationType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connector</strong></td>
<td valign="top"><a href="#connectortype">ConnectorType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>asset</strong></td>
<td valign="top"><a href="#assettype">AssetType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>team</strong></td>
<td valign="top"><a href="#teamtype">TeamType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objectId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>key</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remoteAccessId</strong></td>
<td valign="top"><a href="#uuid">UUID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remoteAccessUrl</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdBy</strong></td>
<td valign="top"><a href="#usertype">UserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isDefault</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>extra</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>scanlogSet</strong></td>
<td valign="top">[<a href="#scanlog">ScanLog</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugSet</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ConnectorType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>slug</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>shortDescription</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>image</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>link</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#parentconnectorstype">ParentConnectorsType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isInternal</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isActive</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>configurationsSet</strong></td>
<td valign="top">[<a href="#configurationtype">ConfigurationType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>parentConnector</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### EngagementPaginatedType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>page</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalPages</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pageSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasNext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasPrev</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objects</strong></td>
<td valign="top">[<a href="#engagementtype">EngagementType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### EngagementType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagementCustomId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>securityPosture</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribedServices</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>checkedTermsAndConditions</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assessmentsCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagementCompletion</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assessmentsPerService</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagementAssessment</strong></td>
<td valign="top">[<a href="#assessmenttype">AssessmentType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdBy</strong></td>
<td valign="top"><a href="#approvalusertype">ApprovalUserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>scheduledDate</strong></td>
<td valign="top"><a href="#date">Date</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>deliveryDate</strong></td>
<td valign="top"><a href="#date">Date</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>documents</strong></td>
<td valign="top">[<a href="#attachmenttype">AttachmentType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugEngagement</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>activityEngagement</strong></td>
<td valign="top">[<a href="#engagementactivitytype">EngagementActivityType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>commentsEngagement</strong></td>
<td valign="top">[<a href="#engagementcommenttype">EngagementCommentType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### EngagementActivityType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#jsonstring">JSONString</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>action</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#approvalusertype">ApprovalUserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>team</strong></td>
<td valign="top"><a href="#teamtype">TeamType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bug</strong></td>
<td valign="top"><a href="#bugtype">BugType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>asset</strong></td>
<td valign="top"><a href="#assettype">AssetType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connectorConfig</strong></td>
<td valign="top"><a href="#configurationtype">ConfigurationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagement</strong></td>
<td valign="top"><a href="#engagementtype">EngagementType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connector</strong></td>
<td valign="top"><a href="#connectortype">ConnectorType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>task</strong></td>
<td valign="top"><a href="#scanlog">ScanLog</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>approval</strong></td>
<td valign="top"><a href="#approvaltype">ApprovalType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>commentSet</strong></td>
<td valign="top">[<a href="#engagementcommenttype">EngagementCommentType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>


### EngagementCommentPaginatedType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>page</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalPages</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pageSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasNext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasPrev</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objects</strong></td>
<td valign="top">[<a href="#engagementcommenttype">EngagementCommentType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### EngagementCommentType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>comment</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bug</strong></td>
<td valign="top"><a href="#bugtype">BugType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>attachments</strong></td>
<td valign="top">[<a href="#attachmenttype">AttachmentType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>internal</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>activity</strong></td>
<td valign="top"><a href="#approvalUsertype">EngagementActivityType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>commentedBy</strong></td>
<td valign="top"><a href="#approvalusertype">ApprovalUserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connectorConfig</strong></td>
<td valign="top"><a href="#configurationtype">ConfigurationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connector</strong></td>
<td valign="top"><a href="#connectortype">ConnectorType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>team</strong></td>
<td valign="top"><a href="#teamtype">TeamType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>approval</strong></td>
<td valign="top"><a href="#approvaltype">ApprovalType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagement</strong></td>
<td valign="top"><a href="#engagementtype">EngagementType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
</tbody>
</table>


### AssessmentPaginatedType
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>page</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalPages</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pageSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasNext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasPrev</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objects</strong></td>
<td valign="top">[<a href="#assessmenttype">AssessmentType</a>]</td>
<td></td>
</tr>
</tbody>
</table>


### AssessmentType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>service</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>package</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagement</strong></td>
<td valign="top"><a href="#engagementtype">EngagementType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>asset</strong></td>
<td valign="top"><a href="#assettype">AssetType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>state</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>scope</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>instructions</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>testAccounts</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>vpnAccounts</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assignedTo</strong></td>
<td valign="top">[<a href="#approvalusertype">ApprovalUserType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
</tbody>
</table>


### ApprovalUserType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isActive</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
</tbody>
</table>


### ApprovalType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>vulnerability</strong></td>
<td valign="top"><a href="#bugtype">BugType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>approvedBy</strong></td>
<td valign="top"><a href="#membertype">MemberType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>approvalState</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>raisedBy</strong></td>
<td valign="top"><a href="#membertype">MemberType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>fromState</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>toState</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isExpired</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>activityApproval</strong></td>
<td valign="top">[<a href="#engagementactivitytype">EngagementActivityType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>commentsApproval</strong></td>
<td valign="top">[<a href="#engagementcommenttype">EngagementCommentType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>


### AttachmentType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>attachment</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>attachmentName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>attachmentSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>url</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bug</strong></td>
<td valign="top"><a href="#bugtype">BugType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>attachedBy</strong></td>
<td valign="top"><a href="#approvalusertype">ApprovalUserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>documentVault</strong></td>
<td valign="top">[<a href="#engagementtype">EngagementType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugAttachments</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>commentSet</strong></td>
<td valign="top">[<a href="#engagementcommenttype">EngagementCommentType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>




### GroupPaginatedType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>page</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalPages</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pageSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasNext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasPrev</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>objects</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### GroupsType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assets</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdBy</strong></td>
<td valign="top"><a href="#usertype">UserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MemberType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#usertype">UserType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>role</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ScanLog

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>config</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>finished</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connectorName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### TagType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>slug</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetTags</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cveTags</strong></td>
<td valign="top">[<a href="#cvetype">CVEType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugTags</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### TeamType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organization</strong></td>
<td valign="top"><a href="#tenantorganizationtype">TenantOrganizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>configurationTeam</strong></td>
<td valign="top">[<a href="#configurationtype">ConfigurationType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>team</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### TenantOrganizationType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>schemaName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isPrimary</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>industry</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>members</strong></td>
<td valign="top">[<a href="#usertype">UserType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>image</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>employeeSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>purposeOfUse</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organizationmemberSet</strong></td>
<td valign="top">[<a href="#membertype">MemberType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetSet</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>groupSet</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>teamSet</strong></td>
<td valign="top">[<a href="#teamtype">TeamType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tagsSet</strong></td>
<td valign="top">[<a href="#tagtype">TagType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagementsSet</strong></td>
<td valign="top">[<a href="#engagementtype">EngagementType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>configurationOrganization</strong></td>
<td valign="top">[<a href="#configurationtype">ConfigurationType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bugSet</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>domain</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isVerified</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### UpdateGroupMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groups</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### UserType

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastLogin</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isSuperuser</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

Designates that this user has all permissions without explicitly assigning them.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>created</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isSuperadmin</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isStaff</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>isActive</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

Designates whether this user should be treated as active. Un-select this instead of deleting accounts.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>activationId</strong></td>
<td valign="top"><a href="#uuid">UUID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>orgMembers</strong></td>
<td valign="top">[<a href="#tenantorganizationtype">TenantOrganizationType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>organizationmemberSet</strong></td>
<td valign="top">[<a href="#membertype">MemberType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assetSet</strong></td>
<td valign="top">[<a href="#assettype">AssetType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>groupSet</strong></td>
<td valign="top">[<a href="#groupstype">GroupsType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>engagementsSet</strong></td>
<td valign="top">[<a href="#engagementtype">EngagementType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>configurationsSet</strong></td>
<td valign="top">[<a href="#configurationtype">ConfigurationType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>assignedTo</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reportedBy</strong></td>
<td valign="top">[<a href="#bugtype">BugType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

## Enums

### ParentConnectorsType

An enumeration.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>A_0</strong></td>
<td>

Misc

</td>
</tr>
<tr>
<td valign="top"><strong>A_1</strong></td>
<td>

SAST scanner

</td>
</tr>
<tr>
<td valign="top"><strong>A_2</strong></td>
<td>

DAST scanner

</td>
</tr>
<tr>
<td valign="top"><strong>A_3</strong></td>
<td>

Tracking

</td>
</tr>
<tr>
<td valign="top"><strong>A_4</strong></td>
<td>

Notification

</td>
</tr>
<tr>
<td valign="top"><strong>A_5</strong></td>
<td>

Import Report

</td>
</tr>
<tr>
<td valign="top"><strong>A_6</strong></td>
<td>

Network scanner

</td>
</tr>
<tr>
<td valign="top"><strong>A_7</strong></td>
<td>

Custom Connector

</td>
</tr>
<tr>
<td valign="top"><strong>A_8</strong></td>
<td>

Asset Inventory

</td>
</tr>
<tr>
<td valign="top"><strong>A_9</strong></td>
<td>

Cloud Integrations

</td>
</tr>
<tr>
<td valign="top"><strong>A_10</strong></td>
<td>

Container Integrations

</td>
</tr>
<tr>
<td valign="top"><strong>A_11</strong></td>
<td>

Import CSV

</td>
</tr>
<tr>
<td valign="top"><strong>A_12</strong></td>
<td>

Export Report

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The `Boolean` scalar type represents `true` or `false`.

### DateTime

The `DateTime` scalar type represents a DateTime
value as specified by
[iso8601](https://en.wikipedia.org/wiki/ISO_8601).

### Date

The `Date` scalar type represents a Date
value as specified by
[iso8601](https://en.wikipedia.org/wiki/ISO_8601).

### Float

The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point). 

### ID

The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

### Int

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31 - 1) and 2^31 - 1 since represented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).

### JSONString

Allows use of a JSON String for input / output from the GraphQL schema.

Use of this type is *not recommended* as you lose the benefits of having a defined, static
schema (one of the key benefits of GraphQL).

### String

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

### UUID

Leverages the internal Python implmeentation of UUID (uuid.UUID) to provide native UUID objects
in fields, resolvers and input.


## Mutations

### Bug Creation

To create a new vulnerability in Strobes, use the `bugCreate` mutation. The fields you provide depend on the bug level:


#### Bug Types

*   **Web:** Vulnerabilities in web applications (e.g., XSS, SQL injection). 
      *   Can be part of asset type: **Web Asset**, **Mobile Asset**
      *   Additional fields: `web` (`affected_endpoints`, `request`, `response`)

*   **Code:** Vulnerabilities in source code (e.g., buffer overflow, command injection).
      *   Can be part of asset type: **Web Asset**, **Mobile Asset**
      *   Additional fields: `code` (`vulnerable_code`, `start_line_number`, etc.)

*   **Package:** Vulnerabilities in third-party packages/dependencies.
      *   Can be part of asset type: **Web Asset**, **Mobile Asset**
      *   Additional fields: `package` (`package_name`, `installed_version`, etc.)

*   **Cloud:** Misconfigurations or vulnerabilities in cloud resources.
      *   Can be part of asset type: **Cloud Asset**
      *   Additional fields: `cloud` (`cloud_type`, `region`, other fields change based on `cloud_type`.)

*   **Network:** Vulnerabilities in network devices or protocols.
      *   Can be part of asset type: **Network Asset**
      *   Additional fields: `network` (`port`, `cpe`)

All bug types share these fields:


*   `title` (string): Concise title summarizing the vulnerability.
*   `description` (string): Detailed description of the vulnerability, impact, and exploitation.
*   `organization_id` (string): Your organization's unique ID.
*   `bug_level` (int): Type of bug (use `Bug level choices`: `code`, `web`, `mobile`, `network`, `cloud`, `package`).
*   `mitigation` (string): Recommended steps to fix the vulnerability.
*   `steps_to_reproduce` (string): Instructions to replicate the issue.
*   `cwe_list` (list of strings): List of relevant CWE IDs.
*   `cve_list` (list of strings): List of associated CVE IDs.
*   `cvss` (float): CVSS score indicating severity.
*   `severity` (int): Severity level (use `Severity choices`: `info`, `low`, `medium`, `high`, `critical`).
*   `tags` (list of strings): Tags for categorization.
*   `selected_assets` (list of integers): Asset IDs affected by the bug.
*   `custom_fields` (string): JSON string for additional custom fields.

#### Bug level choices
  - code = 1
  - web = 2
  - mobile = 3
  - network = 4
  - cloud = 5
  - package = 6

#### Severity choices
  - info = 1
  - low = 2
  - medium = 3
  - high = 4
  - critical = 5
 

### Asset Creation

To create a new asset in Strobes, use the `createAssest` mutation.


#### Asset Types
*   **Web Asset** (type = 1):
    *   Represents web applications or websites.
    *   **Required fields:**
        *   `url`: The URL of the web asset.
        
*   **Mobile Asset** (type = 2):
    *   Represents mobile applications.
    *   **Required fields:**
        *   `package`: The package name or bundle ID of the mobile app.
        
*   **Network Asset** (type = 3):
    *   Represents network devices or hosts.
    *   **Required fields:**
        *   Either `ipaddress` (for a single IP) or `ipaddress_list` (for multiple IPs).
    *   **Optional fields:**
        *   `mac_address`
        *   `hostname`
        *   `os`
        *   `cpe` (Common Platform Enumeration)

*   **Cloud Asset** (type = 4):
    *   Represents cloud resources.
    *   **Required fields:**
        *   `cloud_type`: The type of cloud provider (use `StrobesGQLClient` constants):
            *   `AWS = 2`
            *   `Azure = 3`
            *   `GCP = 4`
            *   `others = 1` (for other cloud providers)

All asset types share these fields:
*   `name` (string): A descriptive name or identifier for the asset.
*   `organization_id` (string): The unique ID of your organization within Strobes.
*   `sensitivity` (int): An integer from 1 to 5 indicating the asset's sensitivity (5 being the most sensitive). This is a subjective assessment based on the potential impact of a security breach.
*   `exposed` (int): A binary value (0 or 1) indicating whether the asset is exposed to the internet (1) or internal only (0).
*   `type` (int): The type of asset:
    *   1: Web
    *   2: Mobile
    *   3: Network
    *   4: Cloud
*   `tags` (list of strings): A list of descriptive tags to help you categorize and search for assets. 


#### Sensitivity choices
  - low = 1
  - medium = 2
  - high = 3
  - critical = 4
