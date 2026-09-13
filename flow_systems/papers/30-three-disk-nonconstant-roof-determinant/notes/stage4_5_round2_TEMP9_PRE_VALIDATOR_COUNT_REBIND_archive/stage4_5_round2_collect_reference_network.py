#!/usr/bin/env python3
"""Fresh Stage-4.5 Round-2 bibliographic network collection for P30/P31.

This helper reuses only the transport and BibTeX parsing primitives of the
historical Round-1 collector.  It performs new Semantic Scholar, Crossref, and
official-landing requests and emits new no-clobber Round-2 sidecars.  It never
modifies a manuscript, bibliography, matrix, scientific tree, Route file,
README, pipeline state, or Git state.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import tempfile
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
NOTES_30 = ROOT / "papers/30-three-disk-nonconstant-roof-determinant/notes"
LEGACY = NOTES_30 / "stage4_5_round1_collect_reference_network.py"
AUTHORITY = {
    "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt": (
        "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812", 19
    ),
    "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md": (
        "e9505895fe78e2910ff32c4c97d4e7c42abf2fc1f63b25ca7170cb17477dd06d", 1674
    ),
    "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json": (
        "11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0", 45264
    ),
    "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json": (
        "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60", 1203
    ),
}
CONFIGS = (
    {
        "paper_id": "P30",
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "bib_sha256": "5b6854540f595e83ffc4f5a6153595ff27b2e74705e9fe930a0b5d33c17b81f1",
        "entries": 28,
    },
    {
        "paper_id": "P31",
        "slug": "31-level11-conjugacy-owner-ledger",
        "bib_sha256": "02f85e29b4379280c91a5ad4258b98e9c3ab81271277fea206df030e2c3de222",
        "entries": 24,
    },
)


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def load_legacy() -> Any:
    spec = importlib.util.spec_from_file_location("stage45_r1_network_primitives", LEGACY)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {LEGACY}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.UA = "flow-systems-stage4.5-round2-integrity-audit/1.0 (fresh bibliographic verification)"
    module.TIMEOUT = 40
    return module


def verify_authority_and_inputs() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    for rel, (expected_sha, expected_bytes) in AUTHORITY.items():
        path = ROOT / rel
        actual_sha = sha_path(path)
        actual_bytes = path.stat().st_size
        checks.append({
            "path": rel,
            "expected_sha256": expected_sha,
            "actual_sha256": actual_sha,
            "expected_bytes": expected_bytes,
            "actual_bytes": actual_bytes,
            "status": "PASS" if (actual_sha, actual_bytes) == (expected_sha, expected_bytes) else "FAIL",
        })
    receipt = json.loads((ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json").read_text(encoding="utf-8"))
    if receipt.get("status") != "AUTHORIZED_AUDIT_ONLY" or receipt.get("repairs_authorized") is not False or receipt.get("stage5_authorized") is not False:
        raise RuntimeError("Round-2 receipt does not authorize audit-only execution")
    lock = json.loads((ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json").read_text(encoding="utf-8"))
    for paper_id in {"P30", "P31"}:
        paper = next(row for row in lock["papers"] if row["paper_id"] == paper_id)
        for row in paper["audit_inputs"] + paper["protected_canonical_files"]:
            path = ROOT / row["path"]
            actual_sha = sha_path(path)
            actual_bytes = path.stat().st_size
            checks.append({
                "path": row["path"],
                "expected_sha256": row["sha256"],
                "actual_sha256": actual_sha,
                "expected_bytes": row["bytes"],
                "actual_bytes": actual_bytes,
                "status": "PASS" if (actual_sha, actual_bytes) == (row["sha256"], row["bytes"]) else "FAIL",
            })
        for tree in paper["science_trees"]:
            for row in tree["files"]:
                path = ROOT / row["path"]
                actual_sha = sha_path(path)
                actual_bytes = path.stat().st_size
                checks.append({
                    "path": row["path"],
                    "expected_sha256": row["sha256"],
                    "actual_sha256": actual_sha,
                    "expected_bytes": row["bytes"],
                    "actual_bytes": actual_bytes,
                    "status": "PASS" if (actual_sha, actual_bytes) == (row["sha256"], row["bytes"]) else "FAIL",
                })
    failed = [row for row in checks if row["status"] != "PASS"]
    if failed:
        raise RuntimeError("authority/input preflight failed: " + json.dumps(failed, ensure_ascii=False))
    return {"checked": len(checks), "passed": len(checks), "failed": 0, "checks": checks}


def build_payload(config: dict[str, Any], legacy: Any, authority_audit: dict[str, Any]) -> tuple[Path, bytes, dict[str, Any]]:
    paper = ROOT / "papers" / config["slug"]
    bib = paper / "notes/stage4_prime_references_round2.bib"
    if sha_path(bib) != config["bib_sha256"]:
        raise RuntimeError(f"{config['paper_id']}: bibliography hash changed")
    entries = legacy.parse_bib(bib)
    if len(entries) != config["entries"]:
        raise RuntimeError(f"{config['paper_id']}: unexpected bibliography population")

    s2_results, s2_events = legacy.s2_batch(entries)
    rows: list[dict[str, Any]] = []
    for index, entry in enumerate(entries, start=1):
        fields = entry["fields"]
        doi = fields.get("doi")
        crossref = legacy.crossref_lookup(doi) if doi else None
        official_url = fields.get("url") or ("https://doi.org/" + doi if doi else None)
        landing = legacy.landing_lookup(official_url) if official_url and (not crossref or crossref.get("http_status") != 200) else None
        determination = legacy.assess(entry, crossref, s2_results.get(entry["ref_slug"]), landing)
        rows.append({
            "sequence": index,
            **entry,
            "query_attempts": {
                "semantic_scholar_batch": "see top-level semantic_scholar_batch_events",
                "crossref_doi": crossref,
                "official_landing_fallback": landing,
                "manual_search_template_1": f'"{legacy.simple_text(fields.get("author", "")).split(" and ")[0]}" "{legacy.simple_text(fields.get("title", ""))}" {fields.get("year", "")}',
                "manual_search_template_2": doi,
                "manual_search_template_3": f'"{legacy.simple_text(fields.get("journal", fields.get("booktitle", fields.get("publisher", ""))))}" "{fields.get("volume", "")}" {fields.get("year", "")}',
            },
            "semantic_scholar_result": s2_results.get(entry["ref_slug"]),
            "fresh_determination": determination,
        })
        time.sleep(0.10)
    verdicts: dict[str, int] = {}
    for row in rows:
        verdict = row["fresh_determination"]["verdict"]
        verdicts[verdict] = verdicts.get(verdict, 0) + 1
    payload = {
        "schema_version": "stage4.5-round2-reference-network-audit/1.0",
        "paper_id": config["paper_id"],
        "generated_at_utc": legacy.now(),
        "audit_mode": 2,
        "fresh_from_scratch": True,
        "prior_round1_used_for_verdicts": False,
        "fresh_context_role_separation": True,
        "error_independence_claimed": False,
        "authority": {
            "author_event_sha256": AUTHORITY["BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt"][0],
            "input_lock_sha256": AUTHORITY["BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"][0],
            "authorization_receipt_sha256": AUTHORITY["BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"][0],
            "preflight": {"checked": authority_audit["checked"], "passed": authority_audit["passed"], "failed": 0},
        },
        "bibliography": {"path": str(bib.relative_to(paper)), "sha256": sha_path(bib), "entry_count": len(entries)},
        "network_method": {
            "a0": "A new Semantic Scholar batch DOI/arXiv lookup was attempted first for every identifier-bearing entry; transport outcomes are retained exactly.",
            "a1_a2": "A new Crossref DOI-registry GET was the primary structured metadata request for DOI entries; a new official URL request was used when no DOI-registry record resolved.",
            "manual_query_templates": "Three deterministic audit queries are retained per item. They are not misreported as executed when structured evidence resolved the item.",
            "not_found_rule": "No reference is guessed. A missing authoritative match remains NOT_FOUND.",
            "passage_boundary": "This artifact verifies identity and bibliographic fields only. It does not create or repair a source-passage locator.",
            "response_retention": "Structured Crossref/S2 JSON is retained; HTML is bounded to a 2,000-character prefix plus raw-body SHA-256.",
        },
        "semantic_scholar_batch_events": s2_events,
        "summary": {"registered_references": len(rows), "determinations": verdicts},
        "references": rows,
    }
    raw = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return paper / "notes/stage4_5_round2_reference_network_audit.json", raw, payload


def publish_no_clobber(candidates: list[tuple[Path, bytes]]) -> None:
    collisions = [str(path) for path, _ in candidates if path.exists()]
    if collisions:
        raise FileExistsError("Round-2 output collision: " + ", ".join(collisions))
    promoted: list[Path] = []
    staged: list[Path] = []
    try:
        for target, raw in candidates:
            fd, name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
            os.close(fd)
            temp = Path(name)
            staged.append(temp)
            temp.write_bytes(raw)
            os.link(temp, target)
            promoted.append(target)
        for temp in staged:
            temp.unlink(missing_ok=True)
    except Exception:
        for target in promoted:
            target.unlink(missing_ok=True)
        for temp in staged:
            temp.unlink(missing_ok=True)
        raise


def main() -> int:
    authority_audit = verify_authority_and_inputs()
    legacy = load_legacy()
    built = [build_payload(config, legacy, authority_audit) for config in CONFIGS]
    publish_no_clobber([(path, raw) for path, raw, _ in built])
    summary = [
        {
            "paper_id": payload["paper_id"],
            "path": str(path.relative_to(ROOT)),
            "sha256": sha_bytes(raw),
            "bytes": len(raw),
            "registered_references": payload["summary"]["registered_references"],
            "determinations": payload["summary"]["determinations"],
        }
        for path, raw, payload in built
    ]
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
