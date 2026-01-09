from strobes_gql_client.client import StrobesGQLClient
from strobes_gql_client import enums, schema
from sgqlc.operation import Operation
import time
import json
from datetime import datetime
from pathlib import Path

"""
Fetch Findings (allBugs) Example

This script mirrors `examples/test_fetch_asset.py`, but for findings.

It fetches (paginated):
- id
- title
- description
- severity
- asset { name }
- mitigation

Note: We also request a minimal `connector { id name slug }` selection as a client-side
workaround for a common backend issue:
  "Field Bug.connector cannot be both deferred and traversed using select_related..."
"""


# Configuration
HOST = enums.APP_HOST
ORG_ID = enums.ORGANIZATION_ID
API_KEY = enums.API_TOKEN


def get_client():
    """Initialize and return the GraphQL client"""
    return StrobesGQLClient(host=HOST, api_token=API_KEY)


def fetch_findings(page_size=200, search_query=None, max_pages=5000, max_total=None):
    """Fetch findings using pagination"""
    print("=" * 60)
    print("Fetching Findings")
    print("=" * 60)

    client = get_client()
    all_findings = []
    seen_ids = set()
    page = 1
    after_cursor = None
    last_cursor_seen = None

    try:
        while True:
            print(f"\nFetching page {page} (after: {after_cursor!r}, limit: {page_size})...")

            variables = {
                "organization_id": ORG_ID,
                "page_size": page_size,
                # Prefer cursor-based pagination for allBugs to avoid servers that ignore `page`.
                "after": after_cursor,
            }
            if search_query:
                variables["search_query"] = search_query

            # Build query manually so we can control selected fields (without modifying client.py)
            op = Operation(schema.Query)
            result = op.all_bugs(**variables)

            # pagination/meta
            result.has_next()
            result.last_cursor()

            # requested fields
            #
            # IMPORTANT:
            # GraphQL only returns fields you SELECT. If you want "all fields" in the dump,
            # you must select them here. Below is a broad selection of common finding fields
            # + a few nested objects (kept minimal to avoid huge payloads).
            result.objects.__fields__(
                "id",
                "state",
                "severity",
                "bug_level",
                "alert_category",
                "title",
                "description",
                "mitigation",
                "steps_to_reproduce",
                "evidence",
                "object_id",
                "hash",
                "cvss",
                "attack_vector",
                "due_date",
                "sla_violated",
                "has_user_defined_due_date",
                "exploit_available",
                "exploit_info",
                "patch_available",
                "patch_info",
                "prioritization_score",
                "prioritization_score_calculated",
                "drill_down_score",
                "vulnerable_since",
                "priority_last_updated",
                "zero_day_available",
                "is_wormable",
                "trend",
                "advisories_seen",
                "epss_score",
                "cisa_due_date",
                "nist",
                "owasp",
                "records_at_risk",
                "records_type",
                "fields",
                "links",
                "metadata",
                "asm_last_updated",
                "is_misconfiguration",
                "created",
                "updated",
                "is_active",
                "is_alert",
                "is_reopened",
                "last_smart_closed_on",
                "last_reopened_on",
                "last_resolved_on",
                "cost_of_risk",
                "port",
                "ipaddress",
                "hostname",
                "mac_address",
                "os",
                "configuration_name",
                "batch_id",
                "temp_id",
                "recently_rediscovered_batch_id",
                "last_data_enriched",
                "is_data_enriched",
                "ai_title",
                "ai_description",
                "ai_mitigation",
            )

            # Minimal nested selections (add more if you need them)
            result.objects.asset.__fields__(
                "id",
                "name",
                "type",
                "target",
                "is_active",
                "created",
                "updated",
            )
            result.objects.engagements.__fields__("id", "name", "state", "created", "updated")
            result.objects.assigned_to.__fields__("id", "email", "first_name", "last_name")
            result.objects.reported_by.__fields__("id", "email", "first_name", "last_name")
            result.objects.team.__fields__("id", "name")
            result.objects.bug_tags.__fields__("id", "slug", "name")
            result.objects.cwe.__fields__("id", "cwe_id", "type", "description")
            result.objects.cve.__fields__(
                "id",
                "cve_id",
                "title",
                "cvss",
                "summary",
                "exploit_available",
                "patch_available",
                "zero_day_available",
                "is_wormable",
                "epss_score",
                "cisa_due_date",
            )

            # backend workaround: ensure connector is explicitly selected
            result.objects.connector.__fields__("id", "name", "slug")

            response = client.endpoint(op)
            if response is None:
                print("  ✗ Error: No response received from API")
                break

            if isinstance(response, dict) and response.get("errors"):
                print("  ✗ GraphQL error(s) returned:")
                for err in response["errors"]:
                    print(f"    - {err.get('message')}")
                break

            data = response.get("data", {}) if isinstance(response, dict) else {}
            all_bugs = data.get("allBugs", {}) if isinstance(data, dict) else {}
            findings = all_bugs.get("objects", []) if isinstance(all_bugs, dict) else []
            has_next = all_bugs.get("hasNext", None)
            last_cursor = all_bugs.get("lastCursor", None)

            # De-dupe by id to avoid infinite loops if the backend repeats pages/cursors.
            new_count = 0
            for f in findings:
                fid = f.get("id")
                if fid is None or fid in seen_ids:
                    continue
                seen_ids.add(fid)
                all_findings.append(f)
                new_count += 1

            total_fetched = len(all_findings)
            print(
                f"  Retrieved {len(findings)} findings (New: {new_count}, Total unique: {total_fetched}, hasNext: {has_next}, lastCursor: {last_cursor!r})"
            )

            # Hard stop(s) to avoid infinite pagination if backend misbehaves.
            if max_total is not None and total_fetched >= max_total:
                all_findings = all_findings[:max_total]
                print(f"\n✓ Stopping: reached max_total={max_total}")
                break

            if page >= max_pages:
                print(f"\n✓ Stopping: reached max_pages={max_pages} (safety brake)")
                break

            # Safety: if server returns no results, stop
            if not findings:
                print("\n✓ Finished! No more findings returned")
                break

            # Cursor safety brakes: if we're not making progress, stop.
            if new_count == 0:
                print(
                    "\n✓ Stopping: backend returned only duplicates (cursor/page likely repeating)"
                )
                break

            if last_cursor is None:
                print("\n✓ Stopping: no lastCursor returned by API")
                break

            if last_cursor == last_cursor_seen:
                print("\n✓ Stopping: lastCursor repeated (pagination loop detected)")
                break

            # Advance cursor
            last_cursor_seen = last_cursor
            after_cursor = last_cursor

            # Normal cursor end condition
            if has_next is False:
                print(f"\n✓ Finished! Fetched all {total_fetched} findings")
                break

            page += 1
            time.sleep(0.1)

    except Exception as e:
        print(f"\n✗ Error fetching findings: {e}")
        import traceback

        traceback.print_exc()

    return all_findings


def _truncate(s, max_len=120):
    if s is None:
        return ""
    s = str(s).replace("\n", " ").strip()
    return s if len(s) <= max_len else s[: max_len - 3] + "..."


def dump_findings(findings, out_path=None):
    """
    Dump all fetched findings into a single file ("one page").

    By default, writes next to this script:
      examples/findings_dump_<timestamp>.json
    """
    if out_path is None:
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        out_path = Path(__file__).resolve().parent / f"findings_dump_{ts}.json"
    else:
        out_path = Path(out_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Dumped {len(findings)} findings to: {out_path}")


def display_findings(findings, max_rows=50):
    """Display findings in a simple table format (with truncated text fields)"""
    print("\n" + "=" * 60)
    print("Findings List")
    print("=" * 60)

    if not findings:
        print("No findings found")
        return

    print(f"\nTotal Findings: {len(findings)}")
    if len(findings) > max_rows:
        print(f"Showing first {max_rows} rows (use max_rows to change).")

    severity_map = {
        1: "Info",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Critical",
    }

    print(
        "\n"
        + f"{'ID':<10} {'Severity':<10} {'Asset':<30} {'Title':<45} {'Mitigation':<60}"
    )
    print("-" * 160)

    for finding in findings[:max_rows]:
        fid = str(finding.get("id", "N/A"))
        sev_raw = finding.get("severity", None)
        sev = severity_map.get(sev_raw, str(sev_raw if sev_raw is not None else "N/A"))
        asset = finding.get("asset") or {}
        asset_name = _truncate(asset.get("name", "N/A"), 28)
        title = _truncate(finding.get("title", "N/A"), 43)
        mitigation = _truncate(finding.get("mitigation", "N/A"), 58)

        print(f"{fid:<10} {sev:<10} {asset_name:<30} {title:<45} {mitigation:<60}")

    # Optional: print a small detail section for the first few findings
    print("\n" + "=" * 60)
    print("Sample Details (first 5)")
    print("=" * 60)
    for finding in findings[:5]:
        fid = finding.get("id", "N/A")
        title = finding.get("title", "N/A")
        desc = _truncate(finding.get("description", ""), 500)
        mitigation = _truncate(finding.get("mitigation", ""), 500)
        asset_name = (finding.get("asset") or {}).get("name", "N/A")
        print(f"\nID: {fid}")
        print(f"Title: {title}")
        print(f"Severity: {finding.get('severity', 'N/A')}")
        print(f"Asset: {asset_name}")
        print(f"Description: {desc}")
        print(f"Mitigation: {mitigation}")


def main():
    """Main function"""
    print("\nStrobes Findings Fetcher")
    print("=" * 60)

    # Optional filters:
    # - Only open findings: search_query='state = 1'
    # - High severity+: search_query='severity >= 4'
    findings = fetch_findings(page_size=200, search_query='severity >= 4', max_pages=5000)
    dump_findings(findings)
    display_findings(findings, max_rows=50)

    print("\n" + "=" * 60)
    print("Completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

