# Strobes GraphQL Client Examples

This directory contains examples for using the Strobes GraphQL Client with a centralized configuration system.

## Configuration

All connection details are stored in `config.py` for easy management and security:

```python
# Connection Configuration
HOST = "life.in.strobes.local"
API_TOKEN = "your_api_token_here"
SCHEME = "http"
PORT = 80
VERIFY = True

# Organization Configuration
ORGANIZATION_ID = "your_organization_id_here"
```

## Files

### `config.py`
Central configuration file containing:
- Connection parameters (host, API token, scheme, port, verify)
- Organization ID
- Pre-built dictionaries for easy import

### `test_connectivity.py`
Tests basic connectivity to the Strobes GraphQL API using the configuration.

### `test_config.py`
Simple script to verify that configuration is loaded correctly.

### `asset-fetching/`
Directory containing asset-related scripts:
- `fetch_all_assets.py` - Fetch and analyze assets with foreign key relationships
- `test_foreign_keys.py` - Test script to verify foreign key data

## Usage

### 1. Update Configuration
Edit `config.py` with your actual connection details:

```python
HOST = "your.strobes.host"
API_TOKEN = "your_actual_api_token"
ORGANIZATION_ID = "your_actual_organization_id"
```

### 2. Test Configuration
```bash
python test_config.py
```

### 3. Test Connectivity
```bash
python test_connectivity.py
```

### 4. Fetch Assets
```bash
python asset-fetching/fetch_all_assets.py
```

### 5. Test Foreign Keys
```bash
python asset-fetching/test_foreign_keys.py
```

## Benefits of This Approach

1. **Centralized Configuration**: All connection details in one place
2. **Security**: Easy to manage API tokens and sensitive data
3. **Maintainability**: Update connection details once, affects all scripts
4. **Reusability**: Import configuration in any script
5. **Version Control**: Can easily exclude sensitive data from version control

## Security Note

The `config.py` file contains sensitive information (API tokens). Consider:
- Adding `config.py` to `.gitignore` if using version control
- Using environment variables for production deployments
- Creating a `config.example.py` with dummy values for documentation

## Foreign Key Support

The updated scripts now properly handle foreign key relationships:
- `createdBy` - User who created the asset
- `organization` - Organization the asset belongs to
- `connector` - Connector used for the asset
- `tags` - Tags associated with the asset

All foreign key data is properly displayed and analyzed in the output. 