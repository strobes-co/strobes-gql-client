# Installation

## Requirements

- **Python 3.6 or higher** (3.7+ recommended)
- `pip`
- Network access to your Strobes platform host

Check your Python version:

```bash
python3 --version
```

<details>
<summary>Installing Python</summary>

- **Windows** — download from [python.org](https://python.org) and run the installer (tick *Add Python to PATH*).
- **macOS** — `brew install python3`, or download from python.org.
- **Linux (Debian/Ubuntu)** — `sudo apt update && sudo apt install python3 python3-pip`
- **Linux (RHEL/CentOS)** — `sudo yum install python3 python3-pip`
</details>

## Install the client

### 1. Clone the repository

```bash
git clone https://github.com/strobes-co/strobes-gql-client.git
cd strobes-gql-client
```

### 2. Create a virtual environment (recommended)

A virtual environment keeps the client's dependencies isolated from the rest of
your system.

```bash
python3 -m venv venv

# Activate it:
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

When active, your prompt shows a `(venv)` prefix.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This pulls in the three runtime dependencies:

| Package | Purpose |
|---|---|
| `requests` | HTTP transport (and multipart file uploads) |
| `sgqlc` | Builds and validates GraphQL operations from the schema |
| `websockets` | Transport support |

### 4. Install the package

```bash
python setup.py install
```

Now `from strobes_gql_client.client import StrobesGQLClient` works from anywhere
in the environment.

## Development install

If you're editing files under `strobes_gql_client/`, install in **editable
mode** instead of step 4:

```bash
pip install -e .
```

This links the installed package to your working tree, so your changes take
effect immediately — no need to re-run `setup.py` after every edit.

## Verify it works

```python
from strobes_gql_client.client import StrobesGQLClient
print(StrobesGQLClient)   # <class 'strobes_gql_client.client.StrobesGQLClient'>
```

To verify you can actually reach your platform and authenticate, continue to
**[Configuration & Authentication](Configuration-and-Authentication)** and then
the **[Quickstart](Quickstart)**.

## Next steps

- [Configuration & Authentication](Configuration-and-Authentication)
- [Quickstart](Quickstart)
