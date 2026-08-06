#!/usr/bin/env python3
"""Analyze the R055 exact true-image graph results."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CONFIGURATIONS = (
    ("n96_d0", 96, "0"),
    ("n160_d0", 160, "0"),
    ("n160_dm1q", 160, "-1/4"),
    ("n160_dp1q", 160, "1/4"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "true_image_graph_r055.json",
    )
    parser.add_argument(
        "--outer-input",
        type=Path,
        default=PROJECT_ROOT / "results" / "outer_graph_r054.json",
    )
    parser.add_argument(
        "--output-stem", default="true_image_graph_analysis_r055"
    )
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def _expected_order(records: list[dict[str, Any]]) -> bool:
    observed = tuple(
        (
            str(record.get("configuration")),
            int(record.get("grid", -1)),
            str(record.get("grid_offset_fraction")),
        )
        for record in records
    )
    return observed == EXPECTED_CONFIGURATIONS


def _schema_pass(record: dict[str, Any]) -> bool:
    required = {
        "configuration",
        "grid",
        "state_count",
        "two_sided_in_box_node_count",
        "two_sided_in_box_node_ids_sha256",
        "outer_reconstruction_pass",
        "true_edge_subset_outer_pass",
        "true_positive_subset_outer_positive_pass",
        "true_forward_inverse_transpose_pass",
        "true_equals_outer_mutual_pass",
        "true_positive_equals_outer_positive_pass",
        "true_forward_unlabelled_edge_hash",
        "outer_mutual_unlabelled_edge_hash",
        "true_forward_positive_unlabelled_edge_hash",
        "outer_forward_positive_unlabelled_edge_hash",
        "outer_all_closed_graph",
        "outer_positive_area_graph",
        "outer_mutual_graph",
        "true_closed_graph",
        "true_positive_area_graph",
        "true_mutual_graph",
    }
    if not required <= set(record):
        return False
    if not isinstance(record["configuration"], str):
        return False
    if not isinstance(record["grid"], int) or record["grid"] <= 0:
        return False
    if not isinstance(record["state_count"], int):
        return False
    if not isinstance(record["two_sided_in_box_node_count"], int):
        return False
    if (
        not isinstance(record["two_sided_in_box_node_ids_sha256"], str)
        or len(record["two_sided_in_box_node_ids_sha256"]) != 64
    ):
        return False
    for variant in (
        "outer_all_closed_graph",
        "outer_positive_area_graph",
        "outer_mutual_graph",
        "true_closed_graph",
        "true_positive_area_graph",
        "true_mutual_graph",
    ):
        stats = record[variant]
        if not isinstance(stats, dict):
            return False
        for key in (
            "active_node_count",
            "induced_edge_count",
            "scc_count",
            "largest_scc_size",
            "nontrivial_scc_count",
            "recurrent_node_count",
        ):
            if not isinstance(stats.get(key), int) or stats[key] < 0:
                return False
    return True


def analyze_payload(
    payload: dict[str, Any], outer_payload: dict[str, Any]
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    records = list(payload.get("records", []))
    outer_records = list(outer_payload.get("records", []))
    outer_by_name = {str(record["configuration"]): record for record in outer_records}
    protocol_pass = (
        payload.get("run_id") == "R055_TRUE_IMAGE_GRAPH"
        and payload.get("protocol")
        == "research/refine-logs/R055_TRUE_IMAGE_GRAPH_PROTOCOL.json"
        and len(records) == 4
        and _expected_order(records)
    )
    schema_pass = bool(records) and all(_schema_pass(record) for record in records)

    outer_alignment_rows: list[dict[str, Any]] = []
    for record in records:
        name = str(record.get("configuration"))
        parent = outer_by_name.get(name)
        if parent is None:
            outer_alignment_rows.append(
                {"configuration": name, "match": False, "reason": "missing outer record"}
            )
            continue
        row = {
            "configuration": name,
            "active_count_match": record.get("two_sided_in_box_node_count")
            == parent.get("two_sided_in_box_node_count"),
            "active_hash_match": record.get("two_sided_in_box_node_ids_sha256")
            == parent.get("two_sided_in_box_node_ids_sha256"),
            "outer_closed_count_match": record.get("outer_forward_closed_edge_count")
            == parent.get("forward_closed_edge_count"),
            "outer_positive_count_match": record.get("outer_forward_positive_edge_count")
            == parent.get("forward_positive_edge_count"),
            "outer_mutual_count_match": record.get("outer_mutual_edge_count")
            == parent.get("mutual_edge_count"),
            "outer_reconstruction_pass": bool(record.get("outer_reconstruction_pass")),
        }
        row["match"] = all(
            value for key, value in row.items() if key != "configuration"
        )
        outer_alignment_rows.append(row)
    outer_alignment_pass = bool(outer_alignment_rows) and all(
        bool(row.get("match")) for row in outer_alignment_rows
    )

    true_subset_pass = bool(records) and all(
        bool(record["true_edge_subset_outer_pass"])
        and bool(record["true_positive_subset_outer_positive_pass"])
        for record in records
    )
    true_transpose_pass = bool(records) and all(
        bool(record["true_forward_inverse_transpose_pass"])
        for record in records
    )
    mutual_equivalence_pass = bool(records) and all(
        bool(record["true_equals_outer_mutual_pass"])
        and bool(record["true_positive_equals_outer_positive_pass"])
        for record in records
    )
    mutual_hash_equality_pass = bool(records) and all(
        record["true_forward_unlabelled_edge_hash"]
        == record["outer_mutual_unlabelled_edge_hash"]
        for record in records
    )
    positive_hash_equality_pass = bool(records) and all(
        record["true_forward_positive_unlabelled_edge_hash"]
        == record["outer_forward_positive_unlabelled_edge_hash"]
        for record in records
    )
    count_consistency_pass = bool(records) and all(
        record["true_forward_closed_edge_count"]
        == record["true_backward_closed_edge_count"]
        and record["true_forward_positive_edge_count"]
        == record["true_backward_positive_edge_count"]
        and record["true_mutual_edge_count"]
        == record["true_forward_closed_edge_count"]
        for record in records
    )

    by_name = {str(record["configuration"]): record for record in records}
    minus = by_name.get("n160_dm1q")
    plus = by_name.get("n160_dp1q")
    shifted_control = {
        "present": bool(minus and plus),
        "true_closed_edge_count_delta": (
            abs(
                minus["true_forward_closed_edge_count"]
                - plus["true_forward_closed_edge_count"]
            )
            if minus and plus
            else None
        ),
        "true_positive_edge_count_delta": (
            abs(
                minus["true_forward_positive_edge_count"]
                - plus["true_forward_positive_edge_count"]
            )
            if minus and plus
            else None
        ),
        "true_largest_scc_size_delta": (
            abs(
                minus["true_closed_graph"]["largest_scc_size"]
                - plus["true_closed_graph"]["largest_scc_size"]
            )
            if minus and plus
            else None
        ),
    }

    decisions = {
        "configuration_count": len(records),
        "protocol_and_configuration_pass": protocol_pass,
        "schema_pass": schema_pass,
        "outer_alignment_pass": outer_alignment_pass,
        "outer_alignment_rows": outer_alignment_rows,
        "true_subset_and_positive_subset_pass": true_subset_pass,
        "true_forward_inverse_transpose_pass": true_transpose_pass,
        "true_outer_mutual_equivalence_pass": mutual_equivalence_pass,
        "true_outer_mutual_hash_equality_pass": mutual_hash_equality_pass,
        "true_outer_positive_hash_equality_pass": positive_hash_equality_pass,
        "true_count_consistency_pass": count_consistency_pass,
        "all_frozen_checks_pass": all(
            (
                protocol_pass,
                schema_pass,
                outer_alignment_pass,
                true_subset_pass,
                true_transpose_pass,
                mutual_equivalence_pass,
                mutual_hash_equality_pass,
                positive_hash_equality_pass,
                count_consistency_pass,
            )
        ),
        "shifted_control": shifted_control,
        "outer_transpose_is_expectedly_not_required": all(
            not bool(record["outer_forward_inverse_transpose_pass"])
            for record in records
        )
        if records
        else False,
        "true_false_positive_fraction_min": min(
            float(record["outer_false_positive_forward_fraction"])
            for record in records
        )
        if records
        else None,
        "true_false_positive_fraction_max": max(
            float(record["outer_false_positive_forward_fraction"])
            for record in records
        )
        if records
        else None,
        "scope_statement": (
            "R055 exactly tests analytic H_a(C) intersection with closed target "
            "rectangles on the frozen finite grids; resulting SCCs remain finite "
            "image-incidence diagnostics, not invariant-set or Markov proofs."
        ),
    }

    enriched: list[dict[str, Any]] = []
    for record in records:
        row = dict(record)
        outer_count = int(record["outer_forward_closed_edge_count"])
        true_count = int(record["true_forward_closed_edge_count"])
        positive_count = int(record["true_forward_positive_edge_count"])
        row["true_touch_only_forward_edge_count"] = true_count - positive_count
        row["true_positive_forward_fraction"] = (
            positive_count / true_count if true_count else 0.0
        )
        row["outer_false_positive_forward_count"] = outer_count - true_count
        row["outer_true_edge_retention_fraction"] = (
            true_count / outer_count if outer_count else 0.0
        )
        enriched.append(row)
    return decisions, enriched


def main() -> None:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    outer_payload = json.loads(args.outer_input.read_text(encoding="utf-8"))
    decisions, records = analyze_payload(payload, outer_payload)
    output = {
        "run_id": "R055_TRUE_IMAGE_GRAPH_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "decisions": decisions,
        "records": records,
        "scope": (
            "exact finite analytic true-image incidence graph compared with an "
            "exact rectangle outer-cover graph; no invariant-set, Markov, "
            "covering, or operator-convergence claim"
        ),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
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
