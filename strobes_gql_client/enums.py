import os

USER_AGENT = 'strobes-python-gql-client'
APP_PORT = 443
APP_SCHEME = "https"
# Copy of the APP_HOST API token and organization ID from the Strobes web application.
APP_HOST = "automate.in.strobes.co"
API_TOKEN = os.getenv('STROBES_API_TOKEN')
ORGANIZATION_ID = os.getenv('STROBES_ORGANIZATION_ID')

