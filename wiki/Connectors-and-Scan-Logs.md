# Connectors & Scan Logs

**Connector configurations** are the integrations that feed data into Strobes
(scanners like Nessus, cloud connectors, etc.). **Scan logs** are the history of
scans those connectors have run. The client exposes both as simple list methods.

> **Example script:** `test-configurations-scanlogs-example.py`

## List connector configurations

```python
payload = client.all_configurations(ORG, page=1, page_size=10)
for config in payload["objects"]:
    connector = (config.get("connector") or {}).get("name")
    print(f"[{config['id']}] {config['name']} — connector: {connector}")
```

`all_configurations` returns the offset-paginated payload directly
(`{"objects": [...], "page", "pageSize", "totalPages", "totalCount", "hasNext",
"hasPrev"}`).

### Signature

```python
client.all_configurations(organization_id, order_by=None,
                          search_query=None, page=1, page_size=10)
```

### Configuration fields

`id`, `name`, `object_id`, `key`, `remote_access_id`, `remote_access_url`,
`is_default`, `is_automated`, `auto_close_findings`, `auto_smart_merge_assets`,
`send_csv_report_with_summary`, `enable_github_webhook`,
`github_webhook_triggers`, `extra`, `created`, `updated`, plus the nested
`connector` (`id`, `name`, `slug`), `organization` (`id`, `name`), and
`created_by` (`id`, `email`, `first_name`, `last_name`).

## List scan logs

```python
payload = client.all_logs(ORG, page=1, page_size=10)

status_map = {0: "queued", 1: "running", 2: "success", 3: "failed"}
for log in payload["objects"]:
    status = status_map.get(log.get("status"), log.get("status"))
    print(f"[{log['id']}] task {log['taskId']} — "
          f"{log.get('connectorName')} — {status}")
```

`all_logs` returns the same offset-paginated payload shape as
`all_configurations`.

### Signature

```python
client.all_logs(organization_id, search_query=None,
                order_by=None, page=1, page_size=10)
```

> The public `allLogs` does **not** accept a `log_type` filter (unlike the
> internal schema) — only `organization_id`, `search_query`, `order_by`,
> `page`, and `page_size` are supported.

### Scan log fields

`id`, `task_id`, `status`, `build_status`, `type`, `finished`, `started`,
`status_last_updated`, `error_code`, `error_info`, `is_scheduled`,
`is_child_task`, `task_retry_count`, `scanner_task_id`, `scan_arguments`,
`events`, `asset`, `organization_id`, `connector_name`, `connector_slug`, plus
nested `config` (`id`, `name`) and `created_by` (`id`, `email`, `first_name`,
`last_name`).

## Polling a scan's status

`all_logs` is the usual way to watch a scan to completion — filter to the scan
you care about and poll `status` until it reaches `2` (success) or `3` (failed):

```python
import time

while True:
    payload = client.all_logs(ORG, search_query="id = 9876", page_size=1)
    log = payload["objects"][0]
    if log["status"] in (2, 3):
        print("Done:", log["status"])
        break
    time.sleep(5)
```

## Related

- [Assets](Assets) — assets carry the connector(s) that reported them
- [Exporting Data](Exporting-Data)
- [Python API Reference](Python-API-Reference)
