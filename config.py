#!/usr/bin/env python3
"""
Configuration file for Strobes GraphQL Client
Contains connection details and organization ID
"""

# Connection Configuration
HOST = "life.in.strobes.local"
API_TOKEN = "75c39a1cab111ec3bfaecf781b33ec7b81d59624"
SCHEME = "http"
PORT = 80
VERIFY = True

# Organization Configuration
ORGANIZATION_ID = "3c5d440c-2b62-4446-bf99-24c492d6a0f5"

# GraphQL URL (constructed from above settings)
GRAPHQL_URL = f"{SCHEME}://{HOST}:{PORT}/graphql/"

# Connection parameters as a dictionary for easy use
CONNECTION_CONFIG = {
    "host": HOST,
    "api_token": API_TOKEN,
    "scheme": SCHEME,
    "port": PORT,
    "verify": VERIFY,
}

# Query parameters as a dictionary
QUERY_CONFIG = {
    "organization_id": ORGANIZATION_ID,
} 