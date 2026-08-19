# examples/test-add-report-attachment-example.py
"""Example script demonstrating how to upload a report attachment (e.g. a
logo/cover image an `addReportTemplate` template can reference by ID) using
the Strobes GraphQL client.

Note: `ReportAttachment` is only linked to the organization and the
uploading user — it is NOT attached to a bug/finding. Report templates
reference the returned attachment `id` via a `*_attachment` custom-data key
to resolve it to a signed URL at render time.

Run this file directly:
    python examples/test-add-report-attachment-example.py
"""

import logging
import os

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_client():
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def add_report_attachment(file_path, organization_id):
    client = get_client()
    try:
        result = client.add_report_attachment(file_path, organization_id)
        logger.info(f"Add report attachment result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error adding report attachment: {e}")
        return None


def main():
    if not enums.API_TOKEN:
        print("Error: set the STROBES_API_TOKEN environment variable.")
        return
    if not enums.ORGANIZATION_ID:
        print("Error: set the STROBES_ORGANIZATION_ID environment variable.")
        return

    os.makedirs("examples/sample_files", exist_ok=True)
    sample_path = "examples/sample_files/report_attachment_sample.txt"
    with open(sample_path, "w") as f:
        f.write("Sample file for testing report attachment upload.")

    add_report_attachment(sample_path, enums.ORGANIZATION_ID)


if __name__ == "__main__":
    main()
