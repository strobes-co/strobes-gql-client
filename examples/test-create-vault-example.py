# examples/test-create-vault-example.py
"""Example script demonstrating how to create and manage vault documents
using the Strobes GraphQL client.

Run this file directly to create sample vault documents:
    python examples/test-create-vault-example.py
"""

from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
import logging
import os
from pathlib import Path
import mimetypes
import requests
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)

def add_vault_document(file_path, engagement_id=None, is_prerequisite=False):
    """Add a document to the vault
    
    Args:
        file_path (str): Path to the file to upload
        engagement_id (UUID, optional): Engagement ID to attach the document to
        is_prerequisite (bool): Whether this is a prerequisite document
    """
    client = get_client()
    
    try:
        # Verify file exists
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        # Prepare the GraphQL operation
        operations = {
            'query': '''
                mutation AddVaultAttachment($file: Upload!, $organizationId: UUID!, $engagementId: UUID, $prerequisite: Boolean) {
                    addVaultAttachment(file: $file, organizationId: $organizationId, engagementId: $engagementId, prerequisite: $prerequisite) {
                        vault {
                            id
                            documentName
                            documentSize
                        }
                    }
                }
            ''',
            'variables': {
                'file': None,  # Will be populated by the map
                'organizationId': enums.ORGANIZATION_ID,
                'engagementId': str(engagement_id) if engagement_id else None,
                'prerequisite': is_prerequisite
            }
        }
        
        # Create the map for multipart request
        map = {
            '0': ['variables.file']
        }
        
        # Prepare the multipart form data
        files = {
            '0': (
                file_path.name,
                open(file_path, 'rb'),
                mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
            )
        }
        
        # Make the request
        response = requests.post(
            f"{client.app_url}api/graphql/",
            headers={
                'Authorization': f"token {enums.API_TOKEN}",
                'user-agent': enums.USER_AGENT
            },
            data={
                'operations': json.dumps(operations),
                'map': json.dumps(map)
            },
            files=files
        )
        
        if response.status_code != 200:
            raise Exception(f"Upload failed with status {response.status_code}: {response.text}")
            
        result = response.json()
        if 'errors' in result:
            raise Exception(f"GraphQL errors: {result['errors']}")
            
        vault_data = (
            result.get('data', {})
            .get('addVaultAttachment', {})
            .get('vault', {})
        )
        
        logger.info(f"Document uploaded successfully! Vault ID: {vault_data.get('id')}")
        logger.info(f"Document name: {vault_data.get('documentName')}")
        logger.info(f"Document size: {vault_data.get('documentSize')} bytes")
        
        return vault_data.get('id')
        
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        return None
    finally:
        # Close the file if it was opened
        if 'files' in locals() and '0' in files:
            files['0'][1].close()

def demonstrate_vault_operations():
    """Demonstrate various vault operations"""
    print("\n=== Creating Sample Vault Documents ===")
    
    # Example 1: Upload a regular document
    print("\n1. Uploading a regular document")
    regular_doc_path = "examples/sample_files/requirements.txt"
    add_vault_document(regular_doc_path)
    
    # Example 2: Upload a prerequisite document with empty string engagement_id
    print("\n2. Uploading a prerequisite document with empty engagement_id")
    prereq_doc_path = "examples/sample_files/prerequisites.pdf"
    add_vault_document(
        prereq_doc_path,
        engagement_id="",  # Try with empty string
        is_prerequisite=True
    )
    
    # Example 3: Upload a prerequisite document with None engagement_id
    print("\n3. Uploading a prerequisite document with None engagement_id")
    prereq_doc_path2 = "examples/sample_files/prerequisites2.pdf"
    add_vault_document(
        prereq_doc_path2,
        engagement_id=None,  # Try with None
        is_prerequisite=True
    )

def main():
    """Main function to demonstrate vault operations"""
    print("🔐 Strobes Vault Management Examples")
    print("=" * 50)
    
    # Create sample files directory if it doesn't exist
    os.makedirs("examples/sample_files", exist_ok=True)
    
    # Create sample files for demonstration
    with open("examples/sample_files/requirements.txt", "w") as f:
        f.write("Sample requirements file for testing vault upload")
    
    with open("examples/sample_files/prerequisites.pdf", "w") as f:
        f.write("Sample prerequisites document for testing vault upload (with empty engagement_id)")
        
    with open("examples/sample_files/prerequisites2.pdf", "w") as f:
        f.write("Sample prerequisites document for testing vault upload (with None engagement_id)")
    
    # Run the demonstration
    demonstrate_vault_operations()
    
    print("\n✅ Vault management examples completed!")
    print("\n💡 Note: This example creates temporary files for demonstration.")
    print("    In real usage, you would upload your actual documents.")

if __name__ == "__main__":
    main() 