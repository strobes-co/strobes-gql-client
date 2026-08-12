# examples/test-upload-workspace-file-example.py
"""Example script demonstrating how to upload a file to an AI agent workspace
using the Strobes GraphQL client.

Run this file directly:
    python examples/test-upload-workspace-file-example.py <workspace_id>
"""

import logging
import os
import sys

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_client():
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def upload_workspace_file(workspace_id, file_path, path=None):
    client = get_client()
    try:
        result = client.upload_workspace_file(workspace_id, file_path, path=path)
        logger.info(f"Upload result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error uploading workspace file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python examples/test-upload-workspace-file-example.py <workspace_id>"
        )
        sys.exit(1)

    workspace_id = sys.argv[1]

    os.makedirs("examples/sample_files", exist_ok=True)
    sample_path = "examples/sample_files/workspace_upload_sample.txt"
    with open(sample_path, "w") as f:
        f.write("Sample file for testing workspace file upload.")

    upload_workspace_file(
        workspace_id, sample_path, path="notes/workspace_upload_sample.txt"
    )


if __name__ == "__main__":
    main()
