#!/usr/bin/env python3
"""Analyze the R053 exact-rational closed-cell cover outputs."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "exact_closed_cover_r053.json",
    )
    parser.add_argument(
        "--independent-input",
        type=Path,
        default=(
            PROJECT_ROOT
            / "results"
            / "exact_closed_cover_independent_check_r053.json"
        ),
    )
    parser.add_argument(
        "--output-stem", default="exact_closed_cover_analysis_r053"
    )
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    records = list(payload["records"])
    independent = json.loads(args.independent_input.read_text(encoding="utf-8"))
    by_name = {record["configuration"]: record for record in records}

    exact_object_integrity = all(
        bool(record["exact_rational_geometry"])
        and bool(record["closed_target_intersection_semantics"])
        and record["radius_fraction"] == "3190032397181517/5000000000000000"
        and record["a_fraction"] == "6"
        and record["adaptive_eta_fraction"] == "1/4"
        for record in records
    )
    x2_edge_cap = all(
        bool(record["exact_edge_and_cap_integrity_pass"])
        and int(record["adaptive_k_uncapped_max"]) <= int(
            record["maximum_subdivisions"]
        )
        for record in records
    )
    x3_bounds = all(bool(record["x3_exact_local_global_bound_pass"]) for record in records)
    x4_fixed = all(
        bool(record["exact_adaptive_no_worse_than_fixed_k16_median_pass"])
        for record in records
    )
    x5_closed = all(
        bool(record["closed_cover_dominance_pass"])
        and bool(record["positive_area_subset_of_half_open_reference_pass"])
        for record in records
    )
    x6_reversibility = all(
        bool(record["forward_inverse_exact_area_multisets_equal"])
        for record in records
    )
    shifted_minus = by_name.get("n160_dm1q")
    shifted_plus = by_name.get("n160_dp1q")
    x6_reflection = bool(shifted_minus and shifted_plus) and all(
        shifted_minus[field] == shifted_plus[field]
        for field in (
            "adaptive_k_exact_multiset_sha256",
            "forward_exact_area_ratio_multiset_sha256",
            "backward_exact_area_ratio_multiset_sha256",
        )
    )
    x7_independent = bool(independent["all_configurations_match"])
    b1_failures = sum(
        int(record["b1_one_ulp_binary_exact_violation_count"]) for record in records
    )
    b1_comparisons = sum(
        int(record["b1_one_ulp_binary_exact_comparison_count"]) for record in records
    )
    decisions = {
        "configuration_count": len(records),
        "x1_exact_object_integrity_pass": exact_object_integrity,
        "x2_exact_edge_and_cap_pass": x2_edge_cap,
        "x3_exact_local_global_bound_pass": x3_bounds,
        "x4_exact_fixed_k16_median_pass": x4_fixed,
        "x5_closed_index_and_dominance_pass": x5_closed,
        "x6_forward_inverse_multiset_pass": x6_reversibility,
        "x6_shifted_reflection_multiset_pass": x6_reflection,
        "x7_independent_reconstruction_pass": x7_independent,
        "all_exact_core_checks_pass": all(
            (
                exact_object_integrity,
                x2_edge_cap,
                x3_bounds,
                x4_fixed,
                x5_closed,
                x6_reversibility,
                x6_reflection,
                x7_independent,
            )
        ),
        "b1_one_ulp_binary_exact_contains_all": all(
            bool(record["b1_one_ulp_binary_exact_containment_pass"])
            for record in records
        ),
        "b1_total_endpoint_comparisons": b1_comparisons,
        "b1_total_endpoint_violations": b1_failures,
        "b1_violation_fraction": b1_failures / b1_comparisons,
        "maximum_uncapped_k": max(
            int(record["adaptive_k_uncapped_max"]) for record in records
        ),
        "minimum_cap_headroom": min(
            int(record["adaptive_k_cap_headroom"]) for record in records
        ),
        "maximum_exact_area_ratio": max(
            float(record["forward_exact_area_ratio_max"]) for record in records
        ),
        "minimum_two_sided_exact_in_box_fraction": min(
            float(record["two_sided_exact_in_box_fraction"]) for record in records
        ),
        "maximum_two_sided_exact_in_box_fraction": max(
            float(record["two_sided_exact_in_box_fraction"]) for record in records
        ),
    }
    output = {
        "run_id": "R053_EXACT_CLOSED_COVER_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "decisions": decisions,
        "records": records,
        "independent_check": independent,
        "scope": (
            "exact enumeration of rational rectangle-enclosure/closed-cell "
            "intersections; finite outer-cover diagnostic, not a Markov, "
            "invariant-set, or operator-convergence certificate"
        ),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(
        json.dumps(
            {"json": str(output_json), "csv": str(output_csv), "decisions": decisions},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
