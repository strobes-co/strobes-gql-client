"""Example: drive Strobes AI workspaces & agents via the public GraphQL API.

Covers the operations added for strobes-agents-mcp:
    Queries   workspaces, workspace, workspaceStats, workspaceTasks,
              workspaceTaskMessages, availableAgents, workspaceFindings,
              workspaceAssets, workspaceFiles, workflowTemplates,
              workspaceWorkflow
    Mutations createWorkspace, archiveWorkspace, createWorkspaceTask,
              cancelWorkspaceTask, retryWorkspaceTask,
              createWorkspaceFromTemplate, pause/resume/cancelWorkflow

Run:
    export STROBES_API_TOKEN="<master-key>"
    export STROBES_ORGANIZATION_ID="<org-uuid>"
    python examples/test-agents-workspaces-example.py
"""

from strobes_gql_client import enums
from strobes_gql_client.client import StrobesGQLClient


def get_client():
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def list_workspaces_and_agents():
    client = get_client()
    ws = client.execute_query(
        "workspaces", organization_id=enums.ORGANIZATION_ID, limit=5
    )["data"]["workspaces"]
    print(f"Workspaces: {len(ws)}")
    for w in ws:
        print(f"  - {w['name']} ({w['status']}) {w['id']}")

    agents = client.execute_query(
        "available_agents", organization_id=enums.ORGANIZATION_ID
    )["data"]["availableAgents"]
    print(f"Agents: {len(agents)} e.g. {[a['id'] for a in agents[:5]]}")
    return ws, agents


def spin_up_and_stop_task(workspace_id, agent_id="general_security_assistant"):
    client = get_client()
    created = client.execute_mutation(
        "create_workspace_task",
        workspace_id=workspace_id,
        title="Example agent task",
        instructions="Summarise the current findings for this workspace.",
        task_type="custom",
        agent_type=agent_id,
    )
    task_id = created["task"]["id"]
    print(f"Spun up task {task_id} ({created['task']['status']})")

    cancelled = client.execute_mutation(
        "cancel_workspace_task", workspace_id=workspace_id, task_id=task_id
    )
    print(f"Stopped task: success={cancelled['success']} "
          f"status={cancelled['task']['status']}")


def show_task_messages(workspace_id, task_id):
    """Read the conversation an agent produced while running a task."""
    client = get_client()
    msgs = client.execute_query(
        "workspace_task_messages", workspace_id=workspace_id, task_id=task_id
    )["data"]["workspaceTaskMessages"]
    print(f"Task messages: {len(msgs)}")


def view_workspace_outputs(workspace_id):
    """Read what agents produced in a workspace."""
    client = get_client()
    findings = client.execute_query(
        "workspace_findings", workspace_id=workspace_id, page_size=5
    )["data"]["workspaceFindings"]
    assets = client.execute_query(
        "workspace_assets", workspace_id=workspace_id, page_size=5
    )["data"]["workspaceAssets"]
    files = client.execute_query(
        "workspace_files", workspace_id=workspace_id, recursive=True
    )["data"]["workspaceFiles"]
    print(f"Findings: {len(findings)}  Assets: {len(assets)}  Files: {len(files)}")
    if files:
        url = client.execute_query(
            "workspace_file_download_url",
            workspace_id=workspace_id, path=files[0]["path"],
        )["data"]["workspaceFileDownloadUrl"]
        print(f"  download URL for {files[0]['name']}: {bool(url)}")


def run_a_workflow():
    """Start a workflow from a template, then control it."""
    client = get_client()
    templates = client.execute_query("workflow_templates")["data"]["workflowTemplates"]
    print(f"Templates: {[t['slug'] for t in templates[:5]]}")
    if not templates:
        return
    tpl = templates[0]
    created = client.execute_mutation(
        "create_workspace_from_template",
        organization_id=enums.ORGANIZATION_ID,
        template_slug=tpl["slug"],
        variables={},  # fill per tpl["requiredVariables"]
        name="Example workflow run",
    )
    ws_id = created["workspace"]["id"]
    print(f"Started workflow workspace {ws_id}")
    wf = client.execute_query("workspace_workflow", workspace_id=ws_id
                              )["data"]["workspaceWorkflow"]
    print(f"  workflow status: {wf and wf['status']}")
    client.execute_mutation("pause_workflow", workspace_id=ws_id)
    client.execute_mutation("resume_workflow", workspace_id=ws_id)
