#!/usr/bin/env python3
"""Sequentially retry failed Round-2 originality lanes for P30/P31.

The initial dual-lane collector intentionally counts transport/parser failures
as failures.  This helper retries only those failed lanes, sequentially, and
emits a separate no-clobber receipt; it never overwrites the initial evidence.
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
COLLECTOR = NOTES_30 / "stage4_5_round2_collect_originality.py"
CONFIGS = (
    ("P30", "30-three-disk-nonconstant-roof-determinant"),
    ("P31", "31-level11-conjugacy-owner-ledger"),
)
AUTH_SHA = "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60"


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def load_collector() -> Any:
    spec = importlib.util.spec_from_file_location("stage45_r2_originality_collector", COLLECTOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {COLLECTOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def retry_lane(module: Any, legacy: Any, sample: dict[str, Any], lane: dict[str, Any]) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    queries = [lane["query"]]
    words = sample["normalized_fragment"].split()
    shorter = " ".join(words[:8])
    if lane["lane"] == "quoted_exact":
        queries.extend([f'"{shorter}"', f'"{sample["normalized_fragment"]}" research'])
    else:
        queries.extend([lane["query"] + " research", f'{shorter} "Liang Wang" research'])
    success: dict[str, Any] | None = None
    for attempt_number, query in enumerate(queries, start=1):
        row = module.one_attempt(legacy, query, "Bing WebSearch")
        row["retry_attempt_number"] = attempt_number
        attempts.append(row)
        if row["transport_status"] == "success":
            success = row
            break
        time.sleep(0.35)
    return {
        "lane": lane["lane"],
        "original_query": lane["query"],
        "retry_status": "success" if success else "SEARCH_ACCESS_LIMITATION",
        "successful_query": success["query"] if success else None,
        "successful_engine": success["engine"] if success else None,
        "attempts": attempts,
    }


def build_one(paper_id: str, slug: str, module: Any, legacy: Any) -> tuple[Path, bytes, dict[str, Any]]:
    notes = ROOT / "papers" / slug / "notes"
    source = notes / "stage4_5_round2_originality_search_raw.json"
    payload = json.loads(source.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    for sample in payload["samples"]:
        if sample["dual_lane_success"]:
            continue
        failed_lanes = [lane for lane in sample["searches"] if lane["status"] != "success"]
        retry_rows = [retry_lane(module, legacy, sample, lane) for lane in failed_lanes]
        rows.append({
            "sample_id": sample["sample_id"],
            "block_id": sample["block_id"],
            "body_denominator_member": sample["body_denominator_member"],
            "changed_surface": sample["stage4_rounds_1_to_3_changed_surface"],
            "failed_lanes_before": len(failed_lanes),
            "retried_lanes": retry_rows,
            "all_failed_lanes_recovered": all(row["retry_status"] == "success" for row in retry_rows),
        })
        time.sleep(0.20)
    changed_failed = [row for row in rows if row["changed_surface"]]
    out = {
        "schema_version": f"{paper_id.lower()}-stage4.5-round2-originality-retry/1.0",
        "paper_id": paper_id,
        "generated_at_utc": legacy.stamp(),
        "authority_receipt_sha256": AUTH_SHA,
        "source_raw": {"path": f"notes/{source.name}", "sha256": sha_path(source), "bytes": source.stat().st_size},
        "method": "Sequential Bing retries with locale/market parameters; success still requires HTTP 200, non-empty body, and at least one parsed result card.",
        "rows_retried": len(rows),
        "rows_recovered": sum(row["all_failed_lanes_recovered"] for row in rows),
        "changed_rows_retried": len(changed_failed),
        "changed_rows_recovered": sum(row["all_failed_lanes_recovered"] for row in changed_failed),
        "rows": rows,
    }
    raw = (json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return notes / "stage4_5_round2_originality_retry_raw.json", raw, out


def publish(candidates: list[tuple[Path, bytes]]) -> None:
    if any(path.exists() for path, _ in candidates):
        raise FileExistsError("Round-2 originality retry output collision")
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
    if sha_path(ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json") != AUTH_SHA:
        raise RuntimeError("authority receipt mismatch")
    module = load_collector()
    legacy = module.load_legacy()
    built = [build_one(paper_id, slug, module, legacy) for paper_id, slug in CONFIGS]
    publish([(path, raw) for path, raw, _ in built])
    print(json.dumps([
        {
            "paper_id": payload["paper_id"],
            "path": str(path.relative_to(ROOT)),
            "sha256": sha_bytes(raw),
            "bytes": len(raw),
            "rows_retried": payload["rows_retried"],
            "rows_recovered": payload["rows_recovered"],
            "changed_rows_retried": payload["changed_rows_retried"],
            "changed_rows_recovered": payload["changed_rows_recovered"],
        }
        for path, raw, payload in built
    ], ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
