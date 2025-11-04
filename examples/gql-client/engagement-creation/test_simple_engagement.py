import logging
import sys
import os
from datetime import datetime, timedelta
from strobes_gql_client.client import StrobesGQLClient

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CONNECTION_CONFIG, QUERY_CONFIG

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def get_client():
    return StrobesGQLClient(**CONNECTION_CONFIG)


def create_simple_engagement():
    """Create a simple engagement with minimal fields"""
    client = get_client()
    
    engagement_name = "Simple Test Engagement"
    
    # Calculate dates
    scheduled_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    delivery_date = (datetime.now() + timedelta(days=21)).strftime("%Y-%m-%d")
    
    engagement_create_fields = {
        "name": engagement_name,
        "organization_id": QUERY_CONFIG["organization_id"],
        "scheduled_date": scheduled_date,
        "delivery_date": delivery_date,
        "plans": 1,
        "subscribed_services": ["test engagement"],
        "document_ids": [],
        "assessment_data": "{}",
        "prerequisites_data": "[]",
        "fields": "{}",
        "vendor_code": "",
        "is_self_managed": True
    }
    
    try:
        result = client.execute_mutation("create_engagement", **engagement_create_fields)
        print('')
        # logger.info(f"Raw result: {result}")
        # logger.info(f"Result type: {type(result)}")
        # if result:
        #     logger.info(f":white_check_mark: Successfully created engagement: {engagement_name}")
        #     logger.info(f"   Engagement ID: {result.get('id', 'N/A')}")
        #     return result
        # else:
        #     logger.error(f":x: Failed to create engagement: {engagement_name}")
        #     return None
    except Exception as e:
        # logger.error(f":x: Error creating engagement '{engagement_name}': {str(e)}")
        # logger.error(f"Full error details: {type(e).__name__}: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return None


if __name__ == "__main__":
    logger.info("Creating simple test engagement...")
    create_simple_engagement()
    logger.info("Test completed!")