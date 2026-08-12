# examples/test-update-bugs-fields-csv-example.py
"""Example script demonstrating how to bulk-update finding custom fields
from a CSV file using the Strobes GraphQL client.

Run this file directly:
    python examples/test-update-bugs-fields-csv-example.py
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


def update_bugs_fields_with_csv(file_path):
    client = get_client()
    try:
        result = client.update_bugs_fields_with_csv(file_path, enums.ORGANIZATION_ID)
        logger.info(f"Update result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error updating bug fields from CSV: {e}")
        return None


def main():
    os.makedirs("examples/sample_files", exist_ok=True)
    # The backend requires a .csv extension, an "id" column (the finding's
    # numeric primary key) plus one column per custom field slug to update.
    sample_path = "examples/sample_files/update_bugs_fields_sample.csv"
    with open(sample_path, "w") as f:
        f.write("id,custom_field_example\n123456,updated-value\n")

    update_bugs_fields_with_csv(sample_path)


if __name__ == "__main__":
    main()
