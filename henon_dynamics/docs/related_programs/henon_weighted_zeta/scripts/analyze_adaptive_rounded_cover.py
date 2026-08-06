#!/usr/bin/env python3
"""Analyze R052 adaptive outward-rounded strip records."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENDPOINT_TOLERANCE = 1.0e-15
COMPARISON_TOLERANCE = 1.0e-12
ROUNDING_INFLATION_TOLERANCE = 1.0e-10


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--input-stem", default="adaptive_rounded_cover_r052")
    parser.add_argument("--fixed-input-stem", default="subdivided_cover_r051")
    parser.add_argument("--output-stem", default="adaptive_rounded_cover_analysis_r052")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads((args.results_dir / f"{args.input_stem}.json").read_text(encoding="utf-8"))
    records = list(payload["records"])
    fixed_payload = json.loads(
        (args.results_dir / f"{args.fixed_input_stem}.json").read_text(encoding="utf-8")
    )
    fixed_k16 = {
        (int(r["grid"]), float(r["grid_offset"])): r
        for r in fixed_payload["records"]
        if int(r["subdivisions"]) == 16 and r["box"] == "main"
    }
    rounded_containment = all(
        bool(r["sample_forward_containment_pass"])
        and bool(r["sample_backward_containment_pass"])
        for r in records
    )
    minimum_endpoint_margin = min(
        float(r["minimum_endpoint_margin"]) for r in records
    )
    endpoint_contains_unrounded = minimum_endpoint_margin >= 0.0
    endpoint_margin_within_tolerance = (
        minimum_endpoint_margin >= -ENDPOINT_TOLERANCE
    )
    cap_free = all(float(r["adaptive_k_cap_fraction"]) == 0.0 for r in records)
    practical = all(
        float(r["forward_rounded_ratio_median"]) < 1.5
        and float(r["backward_rounded_ratio_median"]) < 1.5
        for r in records
    )
    maximum_rounding_area_delta = max(
        float(r["maximum_rounding_area_delta"]) for r in records
    )
    maximum_median_ratio_inflation = max(
        max(
            abs(float(r["rounded_minus_raw_forward_median"])),
            abs(float(r["rounded_minus_raw_backward_median"])),
        )
        for r in records
    )
    maximum_area_delta_small = all(
        float(r["maximum_rounding_area_delta"])
        < ROUNDING_INFLATION_TOLERANCE
        for r in records
    )
    median_ratio_inflation_small = all(
        abs(float(r["rounded_minus_raw_forward_median"]))
        < ROUNDING_INFLATION_TOLERANCE
        and abs(float(r["rounded_minus_raw_backward_median"]))
        < ROUNDING_INFLATION_TOLERANCE
        for r in records
    )
    fixed_k16_excesses: list[float] = []
    for record in records:
        key = (int(record["grid"]), float(record["grid_offset"]))
        if key not in fixed_k16:
            fixed_k16_excesses.append(float("inf"))
            continue
        fixed = fixed_k16[key]
        fixed_k16_excesses.append(
            max(
                float(record["forward_rounded_ratio_median"])
                - float(fixed["forward_enclosure_area_ratio_median"]),
                float(record["backward_rounded_ratio_median"])
                - float(fixed["backward_enclosure_area_ratio_median"]),
            )
        )
    literal_no_worse_count = sum(excess <= 0.0 for excess in fixed_k16_excesses)
    adaptive_no_worse_literal = literal_no_worse_count == len(records)
    adaptive_within_tolerance = all(
        excess <= COMPARISON_TOLERANCE for excess in fixed_k16_excesses
    )
    maximum_positive_fixed_k16_excess = max(
        0.0, max(fixed_k16_excesses)
    )
    maximum_rounded_ratio = max(
        max(
            float(r["forward_rounded_ratio_max"]),
            float(r["backward_rounded_ratio_max"]),
        )
        for r in records
    )
    cap_fraction = max(float(r["adaptive_k_cap_fraction"]) for r in records)
    decisions = {
        "final_endpoint_contains_unrounded_all": endpoint_contains_unrounded,
        "endpoint_margin_within_roundoff_tolerance": endpoint_margin_within_tolerance,
        "minimum_endpoint_margin": minimum_endpoint_margin,
        "endpoint_roundoff_tolerance": ENDPOINT_TOLERANCE,
        "sampled_containment_all": rounded_containment,
        "adaptive_rounded_practical_all": practical,
        "median_rounding_ratio_inflation_small_all": median_ratio_inflation_small,
        "maximum_rounding_area_delta_small_all": maximum_area_delta_small,
        "maximum_median_ratio_inflation": maximum_median_ratio_inflation,
        "maximum_rounding_area_delta": maximum_rounding_area_delta,
        "rounding_inflation_tolerance": ROUNDING_INFLATION_TOLERANCE,
        "adaptive_cap_free_all": cap_free,
        "adaptive_no_worse_than_fixed_k16_literal_all": adaptive_no_worse_literal,
        "adaptive_no_worse_than_fixed_k16_literal_pass_count": literal_no_worse_count,
        "adaptive_within_1e_12_of_fixed_k16_all": adaptive_within_tolerance,
        "fixed_k16_maximum_positive_excess": maximum_positive_fixed_k16_excess,
        "fixed_k16_post_analysis_comparison_tolerance": COMPARISON_TOLERANCE,
        "maximum_adaptive_rounded_ratio": maximum_rounded_ratio,
        "maximum_cap_fraction": cap_fraction,
        "configuration_count": len(records),
    }
    output = {
        "run_id": "R052_ADAPTIVE_ROUNDED_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "decisions": decisions,
        "records": records,
        "scope": (
            "adaptive float64 one-ulp endpoint-expansion diagnostic with "
            "deterministic containment smoke tests; no interval proof"
        ),
    }
    output_json = args.results_dir / f"{args.output_stem}.json"
    output_csv = args.results_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "decisions": decisions}, indent=2))


if __name__ == "__main__":
    main()
