#!/usr/bin/env python3
"""Example script demonstrating how to fetch comments and add comments to a
finding / an engagement using the Strobes GraphQL client.

Run this file directly:
    python examples/test-comments-example.py

Covers:
    Query    allComments(organizationId, bugId | engagementId, internal,
                         searchQuery, orderBy, page, pageSize)
    Mutation addBugComment(organizationId, bugId, comment, internal, attachments)
    Mutation addEngagementComment(organizationId, engagementId, comment, attachments)
"""

import logging

from strobes_gql_client import enums
from strobes_gql_client.client import StrobesGQLClient

logger = logging.getLogger(__name__)


def get_client():
    """Get a configured client instance"""
    return StrobesGQLClient(host=enums.APP_HOST, api_token=enums.API_TOKEN)


def _first_bug_id(client):
    """Pick a finding to comment on so the example is self-contained."""
    resp = client.execute_query(
        "all_bugs", organization_id=enums.ORGANIZATION_ID, page_size=1
    )
    objects = (resp or {}).get("data", {}).get("allBugs", {}).get("objects", [])
    return int(objects[0]["id"]) if objects else None


def _first_engagement_id(client):
    """Pick an engagement to comment on so the example is self-contained."""
    resp = client.execute_query(
        "all_engagements", organization_id=enums.ORGANIZATION_ID, page_size=1
    )
    objects = (resp or {}).get("data", {}).get("allEngagements", {}).get("objects", [])
    return objects[0]["id"] if objects else None


def fetch_finding_comments(bug_id, page=1, page_size=10):
    """Fetch the comments on a single finding."""
    client = get_client()
    resp = client.execute_query(
        "all_comments",
        organization_id=enums.ORGANIZATION_ID,
        bug_id=bug_id,
        page=page,
        page_size=page_size,
        order_by=["-created"],
    )
    if not resp or resp.get("errors"):
        logger.error(f"GraphQL errors: {(resp or {}).get('errors')}")
        return

    result = resp.get("data", {}).get("allComments", {})
    print(f"\nComments on finding {bug_id}: {result.get('totalCount')}")
    print(f"Total pages: {result.get('totalPages')} (page {result.get('page')})")
    for comment in result.get("objects", []):
        author = comment.get("commentedBy") or {}
        print(f"\n  [{comment.get('id')}] {comment.get('comment')}")
        print(f"  internal: {comment.get('internal')}  created: {comment.get('created')}")
        print(f"  by: {author.get('email')}")
        for attachment in comment.get("attachments") or []:
            print(f"    attachment: {attachment.get('attachmentName')}")


def fetch_engagement_comments(engagement_id, page=1, page_size=10):
    """Fetch the comments on a single engagement."""
    client = get_client()
    resp = client.execute_query(
        "all_comments",
        organization_id=enums.ORGANIZATION_ID,
        engagement_id=engagement_id,
        page=page,
        page_size=page_size,
    )
    if not resp or resp.get("errors"):
        logger.error(f"GraphQL errors: {(resp or {}).get('errors')}")
        return

    result = resp.get("data", {}).get("allComments", {})
    print(f"\nComments on engagement {engagement_id}: {result.get('totalCount')}")
    for comment in result.get("objects", []):
        print(f"  [{comment.get('id')}] {comment.get('comment')}")


def add_finding_comment(bug_id, comment, internal=False, attachments=None):
    """Add a comment to a finding.

    ``internal=True`` is honoured only for organization owners/managers —
    everyone else gets an external comment, mirroring the Strobes UI.
    """
    client = get_client()
    fields = {
        "organization_id": enums.ORGANIZATION_ID,
        "bug_id": bug_id,
        "comment": comment,
        "internal": internal,
    }
    if attachments:
        fields["attachments"] = attachments
    return client.execute_mutation("add_bug_comment", **fields)


def add_engagement_comment(engagement_id, comment, attachments=None):
    """Add a comment to an engagement."""
    client = get_client()
    fields = {
        "organization_id": enums.ORGANIZATION_ID,
        "engagement_id": engagement_id,
        "comment": comment,
    }
    if attachments:
        fields["attachments"] = attachments
    return client.execute_mutation("add_engagement_comment", **fields)


def demonstrate_comment_operations():
    """Demonstrate the comment query + both comment mutations."""
    client = get_client()

    bug_id = _first_bug_id(client)
    if bug_id:
        print("\n=== Adding a comment to a finding ===")
        created = add_finding_comment(bug_id, "Triaged via the Strobes GQL client.")
        print(created)

        print("\n=== Fetching comments on that finding ===")
        fetch_finding_comments(bug_id)
    else:
        print("No findings available to comment on — skipping finding comments.")

    engagement_id = _first_engagement_id(client)
    if engagement_id:
        print("\n=== Adding a comment to an engagement ===")
        created = add_engagement_comment(
            engagement_id, "Scope confirmed via the Strobes GQL client."
        )
        print(created)

        print("\n=== Fetching comments on that engagement ===")
        fetch_engagement_comments(engagement_id)
    else:
        print("No engagements available to comment on — skipping engagement comments.")


def main():
    """Main function"""
    demonstrate_comment_operations()


if __name__ == "__main__":
    main()
