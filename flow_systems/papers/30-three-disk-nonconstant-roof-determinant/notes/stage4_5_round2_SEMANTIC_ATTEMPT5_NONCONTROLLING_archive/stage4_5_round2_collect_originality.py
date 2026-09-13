#!/usr/bin/env python3
"""Fresh public-Web originality census for P30/P31 Stage-4.5 Round 2.

Every counted paragraph has both a quoted-exact and an author/field
supplementary query with at least one parsed result card.  Search failure is
retained as unavailable and never converted into evidence of originality.
All three revision rounds are consumed when identifying changed paragraphs.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[3]
NOTES_30 = ROOT / "papers/30-three-disk-nonconstant-roof-determinant/notes"
LEGACY = NOTES_30 / "stage4_5_round1_collect_originality.py"
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
        "paper_id": 30,
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "draft_sha256": "509e9f45b798ad2257acf2f62db81f95a43e3c574da8f1ba7e654c9fa9d21ead",
        "body_start": "B0009",
        "body_end_exclusive": "B0119",
        "field_terms": "three disk physical roof transfer determinant",
    },
    {
        "paper_id": 31,
        "slug": "31-level11-conjugacy-owner-ledger",
        "draft_sha256": "733e37dfe4e7377a711ade04f7bc6d902b311e2ded48211331d70506735d2729",
        "body_start": "B0011",
        "body_end_exclusive": "B0100",
        "field_terms": "Gamma0 11 canonical conjugacy owner certificate",
    },
)
UA = "Mozilla/5.0 (Round-10 Stage-4.5 Round-2 originality integrity audit)"


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def load_legacy() -> Any:
    spec = importlib.util.spec_from_file_location("stage45_r1_originality_primitives", LEGACY)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {LEGACY}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_authority() -> None:
    for rel, (expected_sha, expected_bytes) in AUTHORITY.items():
        path = ROOT / rel
        if sha_path(path) != expected_sha or path.stat().st_size != expected_bytes:
            raise RuntimeError(f"authority mismatch: {rel}")
    receipt = json.loads((ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json").read_text(encoding="utf-8"))
    if receipt.get("status") != "AUTHORIZED_AUDIT_ONLY" or receipt.get("repairs_authorized") is not False or receipt.get("stage5_authorized") is not False:
        raise RuntimeError("receipt is not audit-only")


def one_attempt(legacy: Any, query: str, engine: str) -> dict[str, Any]:
    if engine == "Bing WebSearch":
        request_url = (
            "https://www.bing.com/search?setlang=en-US&cc=US&mkt=en-US&q=" + quote(query)
        )
        parser = legacy.parse_bing
    elif engine == "DuckDuckGo HTML Search":
        request_url = "https://html.duckduckgo.com/html/?q=" + quote(query)
        parser = legacy.parse_duckduckgo
    else:
        request_url = "https://www.google.com/search?hl=en&num=5&q=" + quote(query)
        parser = legacy.parse_google
    requested_at = legacy.stamp()
    try:
        request = Request(request_url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.8"})
        with urlopen(request, timeout=40) as response:
            raw = response.read()
            status = response.status
            final_url = response.geturl()
        results = parser(raw)
        success = status == 200 and len(raw) > 0 and bool(results)
        return {
            "engine": engine,
            "query": query,
            "requested_at": requested_at,
            "request_url": request_url,
            "final_url": final_url,
            "http_status": status,
            "response_bytes": len(raw),
            "response_sha256": sha_bytes(raw),
            "result_count_reviewed": len(results),
            "top_result_summary": results,
            "transport_status": "success" if success else "SEARCH_ACCESS_LIMITATION",
        }
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        return {
            "engine": engine,
            "query": query,
            "requested_at": requested_at,
            "request_url": request_url,
            "final_url": None,
            "http_status": getattr(error, "code", None),
            "response_bytes": 0,
            "response_sha256": None,
            "result_count_reviewed": 0,
            "top_result_summary": [],
            "transport_status": "SEARCH_ACCESS_LIMITATION",
            "error": f"{type(error).__name__}: {error}",
        }


def search_lane(legacy: Any, fragment: str, field_terms: str, lane: str) -> dict[str, Any]:
    query = f'"{fragment}"' if lane == "quoted_exact" else f'{fragment} "Liang Wang" {field_terms}'
    attempts = [one_attempt(legacy, query, "Bing WebSearch")]
    if attempts[-1]["transport_status"] != "success":
        attempts.append(one_attempt(legacy, query, "DuckDuckGo HTML Search"))
    if all(row["transport_status"] != "success" for row in attempts):
        attempts.append(one_attempt(legacy, query, "Google Web Search"))
    successful = next((row for row in attempts if row["transport_status"] == "success"), None)
    summaries = successful["top_result_summary"] if successful else []
    searchable = " ".join(f"{row['title']} {row['snippet']}" for row in summaries).casefold()
    return {
        "lane": lane,
        "query": query,
        "status": "success" if successful else "SEARCH_ACCESS_LIMITATION",
        "successful_engine": successful["engine"] if successful else None,
        "exact_fragment_in_returned_summary": fragment.casefold() in searchable if successful else None,
        "attempts": attempts,
    }


def changed_blocks(notes: Path, current: list[dict[str, Any]], legacy: Any) -> tuple[set[str], list[dict[str, Any]]]:
    changed: set[str] = set()
    operations: list[dict[str, Any]] = []
    current_by_text = {row["text"].replace("\r\n", "\n").strip(): row["block_id"] for row in current}
    patch_names = (
        (1, "stage4_revision_patch_round1.json"),
        (2, "stage4_prime_revision_patch_round2.json"),
        (3, "stage4_prime_revision_patch_round3_exact_confirmation.json"),
    )
    for round_number, name in patch_names:
        payload = json.loads((notes / name).read_text(encoding="utf-8"))
        for op_index, op in enumerate(payload["ops"], start=1):
            kind = op["op"]
            if kind == "replace_block":
                current_id = op["block_id"]
            elif kind in {"insert_after", "insert_before"}:
                current_id = current_by_text.get(op["new_text"].replace("\r\n", "\n").strip())
            else:
                current_id = None
            if current_id:
                changed.add(current_id)
            operations.append({
                "revision_round": round_number,
                "operation_index": op_index,
                "operation": kind,
                "roadmap_target_block_id": op["block_id"],
                "current_block_id": current_id,
                "current_paragraph_surface": bool(
                    current_id and legacy.is_paragraph(next(row["text"] for row in current if row["block_id"] == current_id))
                ),
            })
    return changed, operations


def build_paper(config: dict[str, Any], legacy: Any) -> tuple[Path, bytes, dict[str, Any]]:
    notes = ROOT / "papers" / config["slug"] / "notes"
    draft = notes / "stage4_prime_revision_round3.tex"
    raw = draft.read_bytes()
    if sha_bytes(raw) != config["draft_sha256"]:
        raise RuntimeError(f"P{config['paper_id']}: draft hash changed")
    text = raw.decode("utf-8")
    current = legacy.blocks(text)
    by_id = {row["block_id"]: row for row in current}
    body_start_order = by_id[config["body_start"]]["order"]
    body_end_order = by_id[config["body_end_exclusive"]]["order"]
    body = [
        row for row in current
        if body_start_order <= row["order"] < body_end_order and legacy.is_paragraph(row["text"])
    ]
    changed, revision_operations = changed_blocks(notes, current, legacy)
    changed_paragraphs = [row for row in current if row["block_id"] in changed and legacy.is_paragraph(row["text"])]

    body_ids = {row["block_id"] for row in body}
    selected_ids = {row["block_id"] for index, row in enumerate(body) if index % 2 == 0}
    selected_ids.update(row["block_id"] for row in changed_paragraphs)
    for section in dict.fromkeys(row["section"] for row in body):
        selected_ids.add(next(row["block_id"] for row in body if row["section"] == section))
    minimum = math.ceil(len(body) / 2)
    for row in body:
        if len(selected_ids & body_ids) >= minimum:
            break
        selected_ids.add(row["block_id"])
    selected = [row for row in current if row["block_id"] in selected_ids]

    samples: list[dict[str, Any]] = []
    for index, row in enumerate(selected, start=1):
        words = legacy.visible_words(row["text"])
        if len(words) < 8:
            raise RuntimeError(f"P{config['paper_id']} {row['block_id']}: insufficient words")
        offset = min(4, max(0, len(words) // 6))
        fragment = " ".join(words[offset:offset + 10])
        if len(fragment.split()) < 8:
            fragment = " ".join(words[:10])
        samples.append({
            "sample_id": f"P{config['paper_id']}-S45R2-D1-{index:03d}",
            "block_id": row["block_id"],
            "section": row["section"],
            "body_denominator_member": row["block_id"] in body_ids,
            "stage4_rounds_1_to_3_changed_surface": row["block_id"] in changed,
            "normalized_fragment": fragment,
            "word_count": len(fragment.split()),
        })

    tasks = [(index, lane) for index in range(len(samples)) for lane in ("quoted_exact", "unquoted_supplementary")]
    results: dict[tuple[int, str], dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {
            executor.submit(search_lane, legacy, samples[index]["normalized_fragment"], config["field_terms"], lane): (index, lane)
            for index, lane in tasks
        }
        for future in as_completed(futures):
            results[futures[future]] = future.result()
    for index, sample in enumerate(samples):
        lanes = [results[(index, "quoted_exact")], results[(index, "unquoted_supplementary")]]
        sample["searches"] = lanes
        sample["dual_lane_success"] = all(row["status"] == "success" for row in lanes)
        sample["provisional_grade_from_returned_top_results"] = (
            "SEARCH_ACCESS_LIMITATION" if not sample["dual_lane_success"]
            else "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW" if any(row["exact_fragment_in_returned_summary"] is True for row in lanes)
            else "NO_MATCH_IN_RECORDED_TOP_RESULT_SUMMARIES"
        )

    changed_ids = {row["block_id"] for row in changed_paragraphs}
    body_success = sum(row["dual_lane_success"] and row["block_id"] in body_ids for row in samples)
    changed_success = sum(row["dual_lane_success"] and row["block_id"] in changed_ids for row in samples)
    major_sections = list(dict.fromkeys(row["section"] for row in body))
    covered_sections = list(dict.fromkeys(row["section"] for row in samples if row["block_id"] in body_ids and row["dual_lane_success"]))
    payload = {
        "schema_version": f"p{config['paper_id']}-stage4.5-round2-originality-websearch-raw/1.0",
        "paper_id": f"P{config['paper_id']}",
        "generated_at_utc": legacy.stamp(),
        "audit_scope": "fresh dual-lane public-Web paragraph originality heuristic plus all-three-round changed-paragraph census",
        "fresh_from_scratch": True,
        "prior_round1_used_for_verdicts": False,
        "authority": {
            "author_event_sha256": AUTHORITY["BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt"][0],
            "input_lock_sha256": AUTHORITY["BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"][0],
            "authorization_receipt_sha256": AUTHORITY["BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"][0],
        },
        "draft": {"path": "notes/stage4_prime_revision_round3.tex", "sha256": sha_bytes(raw), "bytes": len(raw)},
        "paragraph_census_rule": "Blocks in the frozen body interval with at least 25 de-TeXed visible words; structural environments are excluded.",
        "paragraph_denominator": len(body),
        "body_paragraph_ids": [row["block_id"] for row in body],
        "sample_total": len(samples),
        "body_sample_total": sum(row["block_id"] in body_ids for row in samples),
        "major_body_sections": major_sections,
        "major_body_sections_covered": covered_sections,
        "successful_body_dual_lane_count": body_success,
        "successful_body_sampling_rate": body_success / len(body),
        "changed_or_new_paragraph_total": len(changed_paragraphs),
        "changed_or_new_paragraph_successful": changed_success,
        "changed_or_new_paragraph_coverage_rate": changed_success / len(changed_paragraphs) if changed_paragraphs else 1.0,
        "changed_or_new_paragraph_ids": [row["block_id"] for row in changed_paragraphs],
        "revision_operation_census": revision_operations,
        "counting_rule": "A paragraph counts only when both lanes return HTTP 200, a non-empty body, and at least one parsed result card. Empty HTTP 200, 202, 429, and parser-empty responses never count.",
        "professional_similarity_detector_used": False,
        "self_plagiarism_scope": "Every sampled supplementary query adds Liang Wang and paper-specific field terms; this is not a complete same-author corpus comparison.",
        "samples": samples,
    }
    raw_out = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return notes / "stage4_5_round2_originality_search_raw.json", raw_out, payload


def publish(candidates: list[tuple[Path, bytes]]) -> None:
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
    verify_authority()
    legacy = load_legacy()
    built = [build_paper(config, legacy) for config in CONFIGS]
    publish([(path, raw) for path, raw, _ in built])
    print(json.dumps([
        {
            "paper_id": payload["paper_id"],
            "path": str(path.relative_to(ROOT)),
            "sha256": sha_bytes(raw),
            "bytes": len(raw),
            "body": payload["paragraph_denominator"],
            "body_success": payload["successful_body_dual_lane_count"],
            "changed": payload["changed_or_new_paragraph_total"],
            "changed_success": payload["changed_or_new_paragraph_successful"],
            "samples": payload["sample_total"],
        }
        for path, raw, payload in built
    ], ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
