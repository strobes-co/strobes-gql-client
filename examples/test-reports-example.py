"""
Report automation: create a template, preview it, generate a PDF report, and
download the finished file — all via the public API token (no JWT needed).

Edit the variables below, then run:
    export STROBES_API_TOKEN="<client-api-token>"
    export STROBES_ORGANIZATION_ID="<org-id>"
    python examples/test-reports-example.py

Covers:
    Query    allTemplates(organizationId, templateId, searchQuery, page, pageSize)
    Query    previewReport(organizationId, templateId, reportName, searchQuery, assetSearchQuery)
    Query    downloadReport(organizationId, exportId)
    Mutation addReportTemplate(organizationId, templateName, htmlData, mode, type)
    Mutation generateReport(organizationId, templateId, reportName, searchQuery, assetSearchQuery)
"""

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client.enums import API_TOKEN, APP_HOST, ORGANIZATION_ID

# =============================================================================
# EDIT THESE
# =============================================================================

TEMPLATE_NAME = "GQL Client Example Template"
TEMPLATE_HTML = "<h1>{{ report_name }}</h1><p>Generated via strobes-gql-client.</p>"
# mode: 0 = portrait, 1 = landscape. type: 2 = findings.
TEMPLATE_MODE = 0
TEMPLATE_TYPE = 2

REPORT_NAME = "GQL Client Example Report"
# Restrict the report to findings matching this RQL query. Leave as None for
# every finding the token can see.
SEARCH_QUERY = None

# =============================================================================


def get_client():
    return StrobesGQLClient(host=APP_HOST, api_token=API_TOKEN)


def find_or_create_template(client, org_id):
    """Reuse an existing template with this name, or create it."""
    existing = client.execute_query(
        "all_templates",
        organization_id=org_id,
        search_query=f'template_name ~ "{TEMPLATE_NAME}"',
        page_size=1,
    )
    objects = (
        (existing or {}).get("data", {}).get("allTemplates", {}).get("objects", [])
    )
    if objects:
        print(f"Reusing existing template {objects[0]['id']}")
        return objects[0]

    created = client.execute_mutation(
        "add_report_template",
        organization_id=org_id,
        template_name=TEMPLATE_NAME,
        html_data=TEMPLATE_HTML,
        mode=TEMPLATE_MODE,
        type=TEMPLATE_TYPE,
    )
    template = (created or {}).get("templates")
    if not template:
        raise RuntimeError(f"Failed to create template: {created}")
    print(f"Created template {template['id']}")
    return template


def preview(client, org_id, template_id):
    resp = client.execute_query(
        "preview_report",
        organization_id=org_id,
        template_id=int(template_id),
        report_name=REPORT_NAME,
        search_query=SEARCH_QUERY,
    )
    html = (resp or {}).get("data", {}).get("previewReport")
    print(f"\nPreview HTML ({len(html or '')} chars):")
    print((html or "")[:500])


def generate(client, org_id, template_id):
    result = client.execute_mutation(
        "generate_report",
        organization_id=org_id,
        template_id=int(template_id),
        report_name=REPORT_NAME,
        search_query=SEARCH_QUERY,
    )
    if not result:
        raise RuntimeError("generateReport returned no data — check permissions.")
    print(f"\n{result.get('reports')}")
    if result.get("password_required"):
        print("Note: this org requires a report password — pass password=... too.")


def main():
    if not API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        sys.exit(1)
    if not ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        sys.exit(1)

    client = get_client()

    print("=== Finding or creating a report template ===")
    template = find_or_create_template(client, ORGANIZATION_ID)

    print("\n=== Previewing the report ===")
    preview(client, ORGANIZATION_ID, template["id"])

    print("\n=== Generating the report (async — runs in the background) ===")
    generate(client, ORGANIZATION_ID, template["id"])

    print(
        "\nReport generation is asynchronous. Use the Strobes UI, or poll "
        "allBugReports internally, to find the exportId once it's finished, "
        "then fetch it with:\n"
        "    client.execute_query('download_report', organization_id=ORGANIZATION_ID, "
        "export_id=<exportId>)"
    )


if __name__ == "__main__":
    main()
