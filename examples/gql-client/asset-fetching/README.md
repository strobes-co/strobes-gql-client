# Asset Fetching Scripts

This folder contains scripts for fetching and analyzing assets from the Strobes GraphQL API.

## Files

### 1. `fetch_all_assets.py` (Main Script)
- **Purpose**: Comprehensive asset fetching with multiple filtering options
- **Features**:
  - Fetch all assets from the organization
  - Filter assets by type (web, code, network, etc.)
  - Filter assets by sensitivity level
  - Filter assets by exposure (internal/external)
  - Filter assets by name pattern
  - Filter assets by specific ID list
  - Analyze and display asset statistics
  - Export assets to JSON format
- **Usage**: `python3 fetch_all_assets.py`

### 2. `check_assets.py` (Simple Asset Checker)
- **Purpose**: Simple script to check and display all assets
- **Features**:
  - Fetch all assets from the organization
  - Group assets by type
  - Display asset counts and IDs
- **Usage**: `python3 check_assets.py`

### 3. `fetch_examples_with_searchqs.py` (Search Query Examples)
- **Purpose**: Examples of advanced search queries for assets and bugs
- **Features**:
  - Various search query examples for assets
  - Search query examples for bugs
  - Complex filtering combinations
- **Usage**: Import functions or run specific examples

## Asset Fetching Functions

### Basic Fetching
- `fetch_all_assets()` - Get all assets from the organization
- `fetch_assets_by_type(asset_type)` - Get assets by specific type
- `fetch_assets_by_id_list(asset_ids)` - Get assets by specific IDs

### Filtering Options
- `fetch_assets_by_sensitivity(sensitivity_levels)` - Filter by sensitivity (1-5)
- `fetch_assets_by_exposure(exposed)` - Filter by exposure (internal/external)
- `fetch_assets_by_name_pattern(pattern)` - Filter by name pattern

### Analysis and Export
- `analyze_assets(assets)` - Display detailed asset statistics
- `export_assets_to_json(assets, filename)` - Export assets to JSON file

### Flexible Search Query
- `fetch_assets_with_search_query(search_query, description)` - Fetch assets using any custom search query

## Asset Types

- **Type 1**: Web Assets (web applications, websites)
- **Type 2**: Mobile Assets (mobile applications)
- **Type 3**: Network Assets (network devices, hosts)
- **Type 4**: Cloud Assets (cloud resources)
- **Type 7**: Code Assets (source code repositories)

## Sensitivity Levels

- **Level 1**: Low sensitivity
- **Level 2**: Medium sensitivity
- **Level 3**: High sensitivity
- **Level 4**: Critical sensitivity
- **Level 5**: Critical sensitivity

## Usage Examples

### Fetch All Assets
```python
from fetch_all_assets import fetch_all_assets, analyze_assets

assets = fetch_all_assets()
analyze_assets(assets)
```

### Fetch Specific Asset Types
```python
from fetch_all_assets import fetch_assets_by_type

web_assets = fetch_assets_by_type(1)      # Web assets
code_assets = fetch_assets_by_type(7)     # Code assets
network_assets = fetch_assets_by_type(3)  # Network assets
```

### Filter by Sensitivity
```python
from fetch_all_assets import fetch_assets_by_sensitivity

high_sensitivity = fetch_assets_by_sensitivity([3, 4, 5])  # High and Critical
low_sensitivity = fetch_assets_by_sensitivity([1, 2])      # Low and Medium
```

### Filter by Exposure
```python
from fetch_all_assets import fetch_assets_by_exposure

external_assets = fetch_assets_by_exposure(True)   # External assets
internal_assets = fetch_assets_by_exposure(False)  # Internal assets
```

### Search by Name Pattern
```python
from fetch_all_assets import fetch_assets_by_name_pattern

web_assets = fetch_assets_by_name_pattern("web")
server_assets = fetch_assets_by_name_pattern("server")
```

### Export to JSON
```python
from fetch_all_assets import fetch_all_assets, export_assets_to_json

assets = fetch_all_assets()
export_assets_to_json(assets, "my_assets.json")
```

### Flexible Search Query
```python
from fetch_all_assets import fetch_assets_with_search_query

# Complex query combining multiple criteria
assets = fetch_assets_with_search_query(
    "type in (1, 7) and sensitivity in (3, 4) and exposed in (1)",
    "high sensitivity external web and code assets"
)

# Name pattern matching
web_assets = fetch_assets_with_search_query(
    'name ~ "web" or name ~ "api"',
    "assets with 'web' or 'api' in name"
)

# Custom ID range
specific_assets = fetch_assets_with_search_query(
    "id in (332, 333, 334)",
    "specific asset IDs"
)
```

## Search Query Examples

### Asset Search Queries
- `type in (1, 7)` - Web and code assets
- `sensitivity in (3, 4, 5)` - High/critical sensitivity assets
- `exposed in (1)` - External assets only
- `name contains "web"` - Assets with "web" in name
- `id in (1, 2, 3)` - Specific asset IDs

### Complex Queries
- `type in (1) and sensitivity in (3, 4) and exposed in (1)` - High sensitivity external web assets
- `name contains "server" or name contains "api"` - Assets with "server" or "api" in name

## Output Examples

### Asset Analysis Output
```
📊 ASSET ANALYSIS:
==================================================
📋 Asset Types:
  • Web Asset (Type 1): 2 assets
    - ID: 332, Name: E-commerce Web Application
    - ID: 333, Name: REST API Service
  • Code Asset (Type 7): 2 assets
    - ID: 334, Name: Main Application Repository
    - ID: 335, Name: API Backend Repository
  • Network Asset (Type 3): 5 assets
    - ID: 336, Name: Network Asset - Single IP
    - ID: 337, Name: Network Asset - Multiple IPs
    ...

🔒 Sensitivity Levels:
  • Medium (Level 3): 8 assets
  • High (Level 4): 1 assets

🌐 Exposure:
  • Internal: 0 assets
  • External: 9 assets
==================================================
```

## Prerequisites

- Strobes GraphQL API access
- Valid API token
- Python 3.x with required dependencies
- Network connectivity to the Strobes server

## Configuration

All scripts use the following configuration:
- **Host**: `life.in.strobes.local`
- **API Token**: `75c39a1cab111ec3bfaecf781b33ec7b81d59624`
- **Scheme**: `http`
- **Port**: `80`
- **Organization ID**: `3c5d440c-2b62-4446-bf99-24c492d6a0f5` 