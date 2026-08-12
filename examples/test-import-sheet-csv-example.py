# examples/test-import-sheet-csv-example.py
"""Example script demonstrating how to import a CSV into a workbook sheet
using the Strobes GraphQL client.

Run this file directly:
    python examples/test-import-sheet-csv-example.py
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


def import_csv(file_path, sheet_id=None, work_book_id=None, name=None):
    client = get_client()
    try:
        result = client.import_csv(
            file_path,
            enums.ORGANIZATION_ID,
            sheet_id=sheet_id,
            work_book_id=work_book_id,
            name=name,
        )
        logger.info(f"Import result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error importing CSV: {e}")
        return None


def main():
    os.makedirs("examples/sample_files", exist_ok=True)
    sample_path = "examples/sample_files/import_sheet_sample.csv"
    with open(sample_path, "w") as f:
        f.write("column_a,column_b\nvalue1,value2\n")

    # Creates a new sheet named "Imported Sheet" (no sheet_id/work_book_id given).
    import_csv(sample_path, work_book_id=2, name="Imported Sheet")


if __name__ == "__main__":
    main()
