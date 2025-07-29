#!/usr/bin/env python3
"""Example script demonstrating how to fetch vault documents
using the Strobes GraphQL client.

Run this file directly to fetch vault documents:
    python examples/test-fetch-vaults-example.py
"""

import logging
from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums
from sgqlc.operation import Operation
from strobes_gql_client.schema import Query

logger = logging.getLogger(__name__)

def get_client():
    """Get a configured client instance"""
    return StrobesGQLClient(
        host=enums.APP_HOST,
        api_token=enums.API_TOKEN
    )

def fetch_all_vault_attachments(page=1, page_size=10, search_query="", order_by=None):
    """Fetch all vault attachments with pagination and filtering
    
    Args:
        page (int): Page number (default: 1)
        page_size (int): Number of items per page (default: 10)
        search_query (str): Search query string (default: "")
        order_by (list): List of fields to order by (default: ["-created"])
    """
    client = get_client()
    
    if order_by is None:
        order_by = ["-created"]
    
    # Create the operation
    op = Operation(Query)
    
    # Get the vault attachments query
    vault_attachments = op.all_vault_attachments(
        organization_id=enums.ORGANIZATION_ID,
        page=page,
        page_size=page_size,
        search_query=search_query,
        order_by=order_by
    )
    
    # Select the fields we want
    vault_attachments.total_pages()
    vault_attachments.total_count()
    
    # Select fields for each object
    objects = vault_attachments.objects()
    objects.id()
    objects.document()
    objects.document_name()
    objects.url()
    
    attached_by = objects.attached_by()
    attached_by.id()
    attached_by.first_name()
    attached_by.last_name()
    attached_by.email()
    
    doc_vault = objects.document_vault()
    doc_vault.id()
    doc_vault.name()
    
    prereqs = objects.prerequisites_attachments()
    prereqs.id()
    
    objects.created()
    objects.updated()
    
    # Execute the query
    response = client.endpoint(op)
    
    if response.get('errors'):
        logger.error(f"GraphQL query failed with {len(response['errors'])} errors")
        logger.error(f"GraphQL errors: {response['errors']}")
        return
    
    result = response.get("data", {}).get("allVaultAttachments", {})
    attachments = result.get("objects", [])
    total_pages = result.get("totalPages", 0)
    total_count = result.get("totalCount", 0)
    
    print(f"\nTotal vault attachments: {total_count}")
    print(f"Total pages: {total_pages}")
    print(f"Current page: {page}")
    
    for attachment in attachments:
        print(f"\nAttachment ID: {attachment.get('id')}")
        print(f"Name: {attachment.get('documentName')}")
        print(f"URL: {attachment.get('url')}")
        
        attached_by = attachment.get('attachedBy', {})
        if attached_by:
            print(f"Attached by: {attached_by.get('firstName')} {attached_by.get('lastName')} ({attached_by.get('email')})")
        
        doc_vault = attachment.get('documentVault', {})
        if doc_vault:
            print(f"Document Vault: {doc_vault.get('name')} (ID: {doc_vault.get('id')})")
        
        print(f"Created: {attachment.get('created')}")
        print(f"Updated: {attachment.get('updated')}")

def demonstrate_vault_attachment_operations():
    """Demonstrate various vault attachment operations"""
    print("\n=== Fetching All Vault Attachments (Default Page) ===")
    fetch_all_vault_attachments()
    
    print("\n=== Fetching Vault Attachments with Custom Parameters ===")
    fetch_all_vault_attachments(
        page=1,  # Changed to page 1 since we only have 7 attachments
        page_size=5,
        search_query="",  # Removed search query since it might be too restrictive
        order_by=["-updated"]
    )

def main():
    """Main function"""
    demonstrate_vault_attachment_operations()

if __name__ == "__main__":
    main() 