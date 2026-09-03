#!/usr/bin/env python3
"""Sequentially retry recorded originality access limitations without erasing history."""

from __future__ import annotations

import importlib.util
import json
import time
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("collector", HERE / "stage4_5_round1_collect_originality.py")
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load originality collector")
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


def stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> int:
    summaries = []
    for config in collector.CONFIGS:
        notes = collector.ROOT / "papers" / config["directory"] / "notes"
        path = notes / "stage4_5_round1_originality_search_raw.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        for pass_number in range(1, 4):
            pending = [
                (sample, lane)
                for sample in payload["samples"]
                for lane in sample["searches"]
                if lane["status"] != "success"
            ]
            if not pending:
                break
            for sample, lane in pending:
                retry = collector.search_lane(
                    sample["normalized_fragment"], config["field_terms"], lane["lane"]
                )
                lane["attempts"].extend(retry["attempts"])
                lane["retry_passes"] = pass_number
                if retry["status"] == "success":
                    lane.update(
                        {
                            "status": "success",
                            "successful_engine": retry["successful_engine"],
                            "exact_fragment_in_returned_summary": retry["exact_fragment_in_returned_summary"],
                        }
                    )
                time.sleep(0.35)
        for sample in payload["samples"]:
            sample["dual_lane_success"] = all(lane["status"] == "success" for lane in sample["searches"])
            sample["provisional_grade_from_returned_top_results"] = (
                "SEARCH_ACCESS_LIMITATION"
                if not sample["dual_lane_success"]
                else "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
                if any(lane["exact_fragment_in_returned_summary"] is True for lane in sample["searches"])
                else "NO_MATCH_IN_RECORDED_TOP_RESULT_SUMMARIES"
            )
        body_ids = set(payload["body_paragraph_ids"])
        body_success = sum(s["dual_lane_success"] and s["block_id"] in body_ids for s in payload["samples"])
        changed = [s for s in payload["samples"] if s["stage4_or_stage4_prime_changed_surface"]]
        changed_success = sum(s["dual_lane_success"] for s in changed)
        payload.update(
            {
                "last_retry_at_utc": stamp(),
                "successful_body_dual_lane_count": body_success,
                "successful_body_sampling_rate": body_success / payload["paragraph_denominator"],
                "changed_or_new_paragraph_successful": changed_success,
                "changed_or_new_paragraph_coverage_rate": changed_success / len(changed),
                "retry_rule": "Up to three sequential retries per still-failing lane; every prior attempt is retained in order.",
            }
        )
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        summaries.append(
            {
                "paper": config["paper_id"],
                "body": f"{body_success}/{payload['paragraph_denominator']}",
                "changed": f"{changed_success}/{len(changed)}",
                "remaining_failed_samples": sum(not s["dual_lane_success"] for s in payload["samples"]),
            }
        )
    print(json.dumps(summaries, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
