#!/usr/bin/env python3
"""Analyze the pre-frozen R051 subdivided-strip cover sweep."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SUBDIVISIONS = (1, 2, 4, 8, 16)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--input-stem", default="subdivided_cover_r051")
    parser.add_argument("--output-stem", default="subdivided_cover_analysis_r051")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.results_dir / f"{args.input_stem}.json"
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    records = list(payload["records"])
    groups: dict[tuple[str, int, float], list[dict[str, object]]] = {}
    for record in records:
        key = (
            str(record["box"]),
            int(record["grid"]),
            float(record["grid_offset"]),
        )
        groups.setdefault(key, []).append(record)

    summaries: list[dict[str, object]] = []
    for key, group in sorted(groups.items()):
        box, grid, offset = key
        by_k = {int(record["subdivisions"]): record for record in group}
        if set(by_k) != set(SUBDIVISIONS):
            raise ValueError(f"subdivision set mismatch for {key}: {sorted(by_k)}")
        forward_medians = [
            float(by_k[k]["forward_enclosure_area_ratio_median"])
            for k in SUBDIVISIONS
        ]
        backward_medians = [
            float(by_k[k]["backward_enclosure_area_ratio_median"])
            for k in SUBDIVISIONS
        ]
        two_sided = [
            float(by_k[k]["two_sided_in_box_fraction"]) for k in SUBDIVISIONS
        ]
        forward_monotone = all(
            later <= earlier + 1.0e-12
            for earlier, later in zip(forward_medians, forward_medians[1:])
        )
        backward_monotone = all(
            later <= earlier + 1.0e-12
            for earlier, later in zip(backward_medians, backward_medians[1:])
        )
        summaries.append(
            {
                "box": box,
                "grid": grid,
                "grid_offset": offset,
                "forward_medians": forward_medians,
                "backward_medians": backward_medians,
                "two_sided_fractions": two_sided,
                "forward_k16_median": forward_medians[-1],
                "backward_k16_median": backward_medians[-1],
                "two_sided_k8_k16_difference": abs(two_sided[3] - two_sided[4]),
                "forward_monotone": forward_monotone,
                "backward_monotone": backward_monotone,
                "k16_practical": forward_medians[-1] < 1.5
                and backward_medians[-1] < 1.5,
                "in_box_stable": abs(two_sided[3] - two_sided[4]) <= 0.02,
            }
        )

    decisions = {
        "T1_tightening_all": bool(
            all(s["forward_monotone"] and s["backward_monotone"] for s in summaries)
        ),
        "T2_practical_all": bool(all(s["k16_practical"] for s in summaries)),
        "T3_geometric_stability_all": bool(all(s["in_box_stable"] for s in summaries)),
        "configuration_count": len(summaries),
    }
    output = {
        "run_id": "R051_STRIP_COVER_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "subdivisions": list(SUBDIVISIONS),
        "decisions": decisions,
        "summaries": summaries,
        "scope": (
            "finite-resolution subdivided-strip tightening diagnostic; no outward "
            "rounding and no invariant-set or convergence certificate"
        ),
    }
    output_json = args.results_dir / f"{args.output_stem}.json"
    output_csv = args.results_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "decisions": decisions}, indent=2))


if __name__ == "__main__":
    main()
