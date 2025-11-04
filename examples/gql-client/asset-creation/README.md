# Asset Creation Scripts

This folder contains scripts for creating different types of assets in the Strobes GraphQL API.

## Files

### 1. `create_web_asset_no_duplicates.py`
- **Purpose**: Creates web assets (type 1) with duplicate checking
- **Features**:
  - Creates single web assets with URLs
  - Creates multiple web assets with URL lists
  - Checks for existing assets to avoid duplicates
  - Supports custom web assets with specific configurations
- **Usage**: `python3 create_web_asset_no_duplicates.py`

### 2. `create_code_asset_no_duplicates.py`
- **Purpose**: Creates code assets (type 7) with duplicate checking
- **Features**:
  - Creates code assets with repository URLs
  - Supports different code asset types (GitHub, GitLab, etc.)
  - Checks for existing assets to avoid duplicates
  - Configurable sensitivity and exposure settings
- **Usage**: `python3 create_code_asset_no_duplicates.py`

### 3. `create_network_asset_no_duplicates.py`
- **Purpose**: Creates network assets (type 3) with duplicate checking
- **Features**:
  - Creates single IP network assets
  - Creates multiple IP network assets with IP lists
  - Creates firewall and custom network assets
  - Supports OS, CPE, hostname, and MAC address configuration
  - Checks for existing assets to avoid duplicates
- **Usage**: `python3 create_network_asset_no_duplicates.py`

## Asset Types

- **Web Assets (type 1)**: Web applications and websites
- **Code Assets (type 7)**: Source code repositories
- **Network Assets (type 3)**: Network devices and hosts

## Common Features

All scripts include:
- Duplicate checking to prevent creating existing assets
- Configurable sensitivity levels (1-5)
- Exposure settings (internal/external)
- Tagging support
- Organization ID configuration
- Error handling and logging

## Prerequisites

- Strobes GraphQL API access
- Valid API token
- Python 3.x with required dependencies
- Network connectivity to the Strobes server 