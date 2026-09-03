#!/usr/bin/env python3
"""Build the bounded P32 Stage-4-prime frozen-query replay artifacts.

This is a metadata-only replay.  It deliberately does not reconstruct the
unavailable historical Phase-2 result rows and does not mutate any canonical
paper, bibliography, code, experiment, result, route, or README file.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path


NOTES = Path(__file__).resolve().parent
PAPER = NOTES.parent
QUERY_DOC = NOTES / "stage1_phase2_annotated_bibliography.md"
INVENTORY = NOTES / "stage1_phase2_source_inventory.tsv"
RAW_OUT = NOTES / "stage4_prime_literature_replay_round2.raw.json"
LEDGER_JSON = NOTES / "stage4_prime_literature_screening_ledger_round2.json"
LEDGER_TSV = NOTES / "stage4_prime_literature_screening_ledger_round2.tsv"
ROWS_TARGET = 51
USER_AGENT = "ARS-P32-Stage4Prime/1.0 (metadata-only frozen-query replay)"
# The execution batch declares 2026-09-04 UTC.  Pin the replay receipt to that
# authority date rather than inheriting a host clock that is six hours behind
# the session's declared UTC date.
RUN_AT_UTC = "2026-09-04T00:30:00Z"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def year_of(item: dict) -> int | None:
    for key in ("published-print", "published-online", "published", "issued"):
        parts = item.get(key, {}).get("date-parts", [])
        if parts and parts[0]:
            return parts[0][0]
    return None


def author_names(item: dict) -> list[str]:
    values = []
    for author in item.get("author", []):
        name = " ".join(x for x in (author.get("given"), author.get("family")) if x)
        if name:
            values.append(name)
    return values


def frozen_queries(text: str) -> list[str]:
    match = re.search(
        r"### Verbatim queries\n(?P<body>.*?)(?:\n### |\n## )",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise RuntimeError("verbatim query section not found")
    queries = []
    for line in match.group("body").splitlines():
        if line.startswith('- "') and line.endswith('"'):
            queries.append(line[3:-1])
    if len(queries) != 26:
        raise RuntimeError(f"expected 26 frozen queries, got {len(queries)}")
    return queries


def load_inventory() -> list[dict]:
    with INVENTORY.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != 26:
        raise RuntimeError(f"expected 26 admitted inventory rows, got {len(rows)}")
    return rows


def request_crossref(query: str) -> tuple[str, int, dict]:
    params = urllib.parse.urlencode(
        {
            "query.bibliographic": query,
            "rows": 2,
            "select": (
                "DOI,title,author,published-print,published-online,published,"
                "container-title,publisher,type,URL"
            ),
        }
    )
    endpoint = f"https://api.crossref.org/works?{params}"
    request = urllib.request.Request(
        endpoint,
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        status = response.status
        payload = json.loads(response.read())
    return endpoint, status, payload


def main() -> None:
    queries = frozen_queries(QUERY_DOC.read_text(encoding="utf-8"))
    inventory = load_inventory()
    run_time = RUN_AT_UTC

    raw_rows: list[dict] = []
    for qindex, query in enumerate(queries, start=1):
        endpoint = None
        status = None
        error = None
        items: list[dict] = []
        try:
            endpoint, status, payload = request_crossref(query)
            items = payload.get("message", {}).get("items", [])
        except Exception as exc:  # fail visibly in the row; do not invent a result
            error = f"{type(exc).__name__}: {exc}"

        rank_limit = 1 if qindex == len(queries) else 2
        for rank in range(1, rank_limit + 1):
            item = items[rank - 1] if rank <= len(items) else None
            raw_rows.append(
                {
                    "manifestation_id": f"M{len(raw_rows) + 1:03d}",
                    "query_id": f"Q{qindex:02d}",
                    "result_rank": rank,
                    "query": query,
                    "retrieved_at_utc": run_time,
                    "crossref": {
                        "endpoint": endpoint,
                        "http_status": status,
                        "message_type": payload.get("message-type") if error is None else None,
                        "total_results": (
                            payload.get("message", {}).get("total-results")
                            if error is None
                            else None
                        ),
                        "record": (
                            {
                                "doi": item.get("DOI"),
                                "title": (item.get("title") or [None])[0],
                                "authors": author_names(item),
                                "year": year_of(item),
                                "container_title": (item.get("container-title") or [None])[0],
                                "publisher": item.get("publisher"),
                                "type": item.get("type"),
                                "url": item.get("URL"),
                            }
                            if item is not None
                            else None
                        ),
                        "error": error if item is None else None,
                    },
                }
            )
        time.sleep(0.12)

    if len(raw_rows) != ROWS_TARGET:
        raise RuntimeError(f"expected {ROWS_TARGET} replay rows, got {len(raw_rows)}")

    raw = {
        "schema_version": "round10-stage4-prime-literature-replay-raw/1.0",
        "paper_id": "P32",
        "generated_at_utc": run_time,
        "retrieval_interface": "Crossref REST /works query.bibliographic",
        "retrieval_bound": (
            "two Crossref-ranked metadata manifestations per exact frozen query "
            "for Q01--Q25 and one for Q26; deterministic total 51"
        ),
        "source_query_document": {
            "path": "notes/stage1_phase2_annotated_bibliography.md",
            "sha256": sha256(QUERY_DOC),
            "query_count": len(queries),
        },
        "historical_reconstruction_boundary": (
            "Original-session result and row-decision records are absent.  These "
            "51 dated replay manifestations are new observations and are not "
            "backfilled or relabeled as the historical 51 captured records."
        ),
        "rows": raw_rows,
    }
    RAW_OUT.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    inv_by_doi = {r["doi"].lower(): r for r in inventory if r["doi"]}
    inv_by_title = {normalized_title(r["title"]): r for r in inventory}
    seen: dict[str, str] = {}
    ledger_rows = []
    for row in raw_rows:
        record = row["crossref"]["record"]
        matched = None
        identity = None
        if record:
            doi = (record.get("doi") or "").lower()
            title_key = normalized_title(record.get("title") or "")
            matched = inv_by_doi.get(doi) if doi else None
            if matched is None and title_key:
                matched = inv_by_title.get(title_key)
            identity = f"doi:{doi}" if doi else f"title:{title_key}|year:{record.get('year')}"

        duplicate_of = seen.get(identity) if identity else None
        if identity and duplicate_of is None:
            seen[identity] = row["manifestation_id"]

        if record is None:
            decision = "RETRIEVAL_UNAVAILABLE"
            reason = "Crossref returned no record for this requested rank or the request failed."
        elif duplicate_of:
            decision = "REMOVE_DUPLICATE_MANIFESTATION"
            reason = f"Same current-replay identity as {duplicate_of}; DOI first, normalized title fallback."
        elif matched:
            decision = "RETAIN_EXISTING_INVENTORY_RECORD"
            reason = "Unique current manifestation matches the frozen admitted inventory by DOI or normalized title."
        else:
            decision = "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE"
            reason = "Unique top-ranked metadata manifestation does not match the frozen admitted inventory and is not adopted by this bounded replay."

        ledger_rows.append(
            {
                "manifestation_id": row["manifestation_id"],
                "query_id": row["query_id"],
                "result_rank": row["result_rank"],
                "exact_frozen_query": row["query"],
                "retrieved_at_utc": row["retrieved_at_utc"],
                "interface": "Crossref REST query.bibliographic; rows=2 (Q26 retained rank 1 only)",
                "http_status": row["crossref"]["http_status"],
                "candidate_doi": record.get("doi") if record else None,
                "candidate_title": record.get("title") if record else None,
                "candidate_year": record.get("year") if record else None,
                "dedup_identity": identity,
                "duplicate_of": duplicate_of,
                "decision": decision,
                "matched_source_id": matched["source_id"] if matched else None,
                "decision_reason": reason,
            }
        )

    decisions = {name: sum(r["decision"] == name for r in ledger_rows) for name in {
        "RETRIEVAL_UNAVAILABLE",
        "REMOVE_DUPLICATE_MANIFESTATION",
        "RETAIN_EXISTING_INVENTORY_RECORD",
        "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE",
    }}
    ledger = {
        "schema_version": "round10-stage4-prime-literature-screening-ledger/1.0",
        "paper_id": "P32",
        "generated_at_utc": run_time,
        "source_raw_replay": {
            "path": "notes/stage4_prime_literature_replay_round2.raw.json",
            "sha256": sha256(RAW_OUT),
            "rows": len(raw_rows),
        },
        "method": {
            "retrieval_bound": raw["retrieval_bound"],
            "dedup_rule": "case-insensitive DOI equality, then normalized title plus year",
            "screening_rule": "match against the frozen 26-row admitted inventory by DOI, then normalized title",
            "decision_vocabulary": sorted(decisions),
            "historical_reconstruction_boundary": raw["historical_reconstruction_boundary"],
        },
        "row_count": len(ledger_rows),
        "decision_counts": decisions,
        "unique_current_manifestations": len({r["dedup_identity"] for r in ledger_rows if r["dedup_identity"]}),
        "rows": ledger_rows,
        "scientific_result_changed": False,
        "canonical_result_refreshed": False,
    }
    LEDGER_JSON.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    fieldnames = list(ledger_rows[0])
    with LEDGER_TSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(ledger_rows)

    print(json.dumps({
        "raw": str(RAW_OUT.relative_to(PAPER)),
        "raw_sha256": sha256(RAW_OUT),
        "ledger_json": str(LEDGER_JSON.relative_to(PAPER)),
        "ledger_json_sha256": sha256(LEDGER_JSON),
        "ledger_tsv": str(LEDGER_TSV.relative_to(PAPER)),
        "ledger_tsv_sha256": sha256(LEDGER_TSV),
        "rows": len(ledger_rows),
        "decision_counts": decisions,
    }, indent=2))


if __name__ == "__main__":
    main()
