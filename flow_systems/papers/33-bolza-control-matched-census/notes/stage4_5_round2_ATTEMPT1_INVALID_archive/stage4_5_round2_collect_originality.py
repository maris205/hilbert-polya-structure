#!/usr/bin/env python3
"""Collect fresh dual-lane originality-search evidence for P33 Stage 4.5 R2."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = Path(__file__).resolve().parent
DRAFT = NOTES / "stage4_prime_revision_round2.tex"
DRAFT_SHA = "40ff6a91c311e7bdd01d6a37bfdd3bd351073311d7781bd4074f0975362e60ce"
OUTPUT = NOTES / "stage4_5_round2_originality_search_raw.json"


def load_helpers():
    path = ROOT / "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round1_collect_originality.py"
    spec = importlib.util.spec_from_file_location("round10_originality_transport", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


H = load_helpers()


def stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> int:
    raw = DRAFT.read_bytes()
    if hashlib.sha256(raw).hexdigest() != DRAFT_SHA:
        raise RuntimeError("P33 successor drifted")
    current = H.blocks(raw.decode("utf-8"))
    by_id = {row["block_id"]: row for row in current}
    start = by_id["B0014"]["order"]
    end = by_id["B0118"]["order"]
    body = [row for row in current if start <= row["order"] < end and H.is_paragraph(row["text"])]

    changed: set[str] = set()
    revision_operations = []
    for round_number, name in (
        (1, "stage4_revision_patch_round1.json"),
        (2, "stage4_prime_revision_patch_round6_exact_confirmation.json"),
    ):
        patch = json.loads((NOTES / name).read_text(encoding="utf-8"))
        for operation_index, op in enumerate(patch["ops"], start=1):
            block_id = op["block_id"]
            changed.add(block_id)
            revision_operations.append(
                {
                    "revision_round": round_number,
                    "operation_index": operation_index,
                    "operation": op["op"],
                    "current_block_id": block_id,
                    "current_paragraph_surface": block_id in by_id and H.is_paragraph(by_id[block_id]["text"]),
                }
            )

    changed_paragraphs = [row for row in current if row["block_id"] in changed and H.is_paragraph(row["text"])]
    selected_ids = {row["block_id"] for index, row in enumerate(body) if index % 2 == 0}
    selected_ids.update(row["block_id"] for row in changed_paragraphs)
    sections = list(dict.fromkeys(row["section"] for row in body))
    for section in sections:
        selected_ids.add(next(row["block_id"] for row in body if row["section"] == section))
    minimum = math.ceil(len(body) / 2)
    for row in body:
        if len(selected_ids & {item["block_id"] for item in body}) >= minimum:
            break
        selected_ids.add(row["block_id"])
    selected = [row for row in current if row["block_id"] in selected_ids]

    samples = []
    for index, row in enumerate(selected, start=1):
        words = H.visible_words(row["text"])
        offset = min(4, max(0, len(words) // 6))
        fragment = " ".join(words[offset : offset + 10])
        if len(fragment.split()) < 8:
            fragment = " ".join(words[:10])
        samples.append(
            {
                "sample_id": f"P33-S45R2-D1-{index:03d}",
                "block_id": row["block_id"],
                "section": row["section"],
                "body_denominator_member": row in body,
                "stage4_or_stage4_prime_changed_surface": row["block_id"] in changed,
                "normalized_fragment": fragment,
                "word_count": len(fragment.split()),
            }
        )

    tasks = [(index, lane) for index in range(len(samples)) for lane in ("quoted_exact", "unquoted_supplementary")]
    results = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {
            executor.submit(
                H.search_lane,
                samples[index]["normalized_fragment"],
                "Bolza genus two geodesic owner certificate",
                lane,
            ): (index, lane)
            for index, lane in tasks
        }
        for future in as_completed(futures):
            results[futures[future]] = future.result()

    for index, sample in enumerate(samples):
        sample["tracks"] = [results[(index, lane)] for lane in ("quoted_exact", "unquoted_supplementary")]
        sample["dual_lane_success"] = all(track["status"] == "success" for track in sample["tracks"])
        sample["provisional_grade_from_returned_top_results"] = (
            "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
            if any(track.get("exact_fragment_in_returned_summary") for track in sample["tracks"])
            else "NO_COPYING_INFERENCE_FROM_RETURNED_SUMMARIES"
        )

    successful_body = sum(row["body_denominator_member"] and row["dual_lane_success"] for row in samples)
    changed_rows = [row for row in samples if row["stage4_or_stage4_prime_changed_surface"]]
    changed_success = sum(row["dual_lane_success"] for row in changed_rows)
    payload = {
        "schema_version": "p33-stage4.5-round2-originality-search-raw/1.0",
        "generated_at_utc": stamp(),
        "fresh_from_scratch": True,
        "draft": {"path": "notes/stage4_prime_revision_round2.tex", "sha256": DRAFT_SHA, "bytes": len(raw)},
        "paragraph_denominator": len(body),
        "successful_body_dual_lane_count": successful_body,
        "successful_body_sampling_rate": successful_body / len(body),
        "changed_or_new_paragraph_total": len(changed_rows),
        "changed_or_new_paragraph_successful": changed_success,
        "changed_or_new_paragraph_coverage_rate": changed_success / len(changed_rows) if changed_rows else 1.0,
        "major_body_sections": sections,
        "major_body_sections_covered": sorted({row["section"] for row in samples if row["body_denominator_member"]}),
        "revision_operations": revision_operations,
        "samples": samples,
        "boundary": "Public-Web search heuristic only; no professional similarity detector or global originality certificate.",
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in (
        "paragraph_denominator", "successful_body_dual_lane_count", "successful_body_sampling_rate",
        "changed_or_new_paragraph_total", "changed_or_new_paragraph_successful",
        "changed_or_new_paragraph_coverage_rate")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
