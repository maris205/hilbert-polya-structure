#!/usr/bin/env python3
"""Evaluate the frozen gates and descriptive metrics for R056."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R056_TRUE_IMAGE_REFINEMENT_PROTOCOL.json"
)
EXPECTED_ANCHORS = ("n96_d0", "n160_d0", "n160_dm1q", "n160_dp1q")
EXPECTED_HELDOUTS = (
    "n127_d0",
    "n192_d0",
    "n254_d0",
    "n320_d0",
    "n254_dm1_3",
    "n254_dp1_3",
)
EXPECTED_REFINEMENTS = (
    ("n96_d0", "n192_d0"),
    ("n127_d0", "n254_d0"),
    ("n160_d0", "n320_d0"),
)
CENTERED_SCALING_ORDER = (
    "n96_d0",
    "n127_d0",
    "n160_d0",
    "n192_d0",
    "n254_d0",
    "n320_d0",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "true_image_refinement_r056.json",
    )
    parser.add_argument(
        "--independent-input",
        type=Path,
        default=PROJECT_ROOT
        / "results"
        / "true_image_refinement_independent_check_r056.json",
    )
    parser.add_argument("--output-stem", default="true_image_refinement_analysis_r056")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _all_true(values: Iterable[object]) -> bool:
    return all(value is True for value in values)


def _record_schema_pass(record: dict[str, Any]) -> bool:
    required = {
        "configuration",
        "evidence_role",
        "grid",
        "grid_offset_fraction",
        "edge_array_path",
        "edge_array_sha256",
        "exact_edge_integrity_pass",
        "uncapped_k_max",
        "cap_active_count",
        "local_variation_bound_pass",
        "maximum_outer_area_ratio",
        "outer_area_ratio_bound_pass",
        "candidate_hull_contains_true_pass",
        "active_node_count",
        "active_node_ids_sha256",
        "slab_active_equals_analytic_hull_active_pass",
        "true_edge_subset_outer_pass",
        "true_positive_subset_outer_positive_pass",
        "true_forward_inverse_labelled_transpose_pass",
        "true_closed_equals_mutual_outer_forward_pass",
        "true_closed_equals_mutual_outer_backward_pass",
        "true_positive_equals_outer_positive_forward_pass",
        "true_positive_equals_outer_positive_backward_pass",
        "true_closed_graph",
        "true_positive_graph",
    }
    if not required <= set(record):
        return False
    if not isinstance(record["configuration"], str):
        return False
    if not isinstance(record["grid"], int) or record["grid"] <= 0:
        return False
    if not isinstance(record["edge_array_sha256"], str) or len(
        record["edge_array_sha256"]
    ) != 64:
        return False
    for graph_key in ("true_closed_graph", "true_positive_graph"):
        graph = record[graph_key]
        if not isinstance(graph, dict):
            return False
        graph_required = {
            "active_node_count",
            "induced_edge_count",
            "scc_count",
            "largest_scc_size",
            "largest_scc_node_ids",
            "largest_scc_node_ids_sha256",
            "multi_node_scc_count",
            "multi_node_recurrent_node_count",
            "singleton_self_loop_scc_count",
            "active_union_area",
            "largest_scc_union_area",
            "multi_node_recurrent_union_area",
        }
        if not graph_required <= set(graph):
            return False
        if len(graph["largest_scc_node_ids"]) != graph["largest_scc_size"]:
            return False
    return True


def loglog_fit(records_by_name: dict[str, dict[str, Any]], graph_key: str) -> dict[str, Any]:
    rows = [records_by_name[name] for name in CENTERED_SCALING_ORDER]
    grids = np.asarray([int(row["grid"]) for row in rows], dtype=float)
    sizes = np.asarray(
        [int(row[graph_key]["largest_scc_size"]) for row in rows], dtype=float
    )
    if np.any(sizes <= 0):
        return {
            "configuration_order": list(CENTERED_SCALING_ORDER),
            "grids": grids.tolist(),
            "largest_scc_sizes": sizes.tolist(),
            "fit_available": False,
        }
    x_values = np.log(grids)
    y_values = np.log(sizes)
    slope, intercept = np.polyfit(x_values, y_values, 1)
    predicted = slope * x_values + intercept
    residual = float(np.sum((y_values - predicted) ** 2))
    total = float(np.sum((y_values - y_values.mean()) ** 2))
    r_squared = 1.0 - residual / total if total else 1.0
    return {
        "configuration_order": list(CENTERED_SCALING_ORDER),
        "grids": [int(value) for value in grids],
        "largest_scc_sizes": [int(value) for value in sizes],
        "largest_scc_size_over_grid": [
            float(size / grid) for size, grid in zip(sizes, grids)
        ],
        "fit_available": True,
        "loglog_slope": float(slope),
        "loglog_intercept": float(intercept),
        "r_squared": r_squared,
        "implied_cell_union_area_exponent": float(slope - 2.0),
        "interpretation": (
            "descriptive filament-compatible finite-grid scaling only; the "
            "slope and slope-minus-two area exponent are not a dimension or "
            "graph-limit claim"
        ),
    }


def analyze_payload(
    payload: dict[str, Any],
    independent: dict[str, Any],
    protocol: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    records = list(payload.get("records", []))
    records_by_name = {str(record.get("configuration")): record for record in records}
    observed_order = tuple(str(record.get("configuration")) for record in records)
    expected_order = EXPECTED_ANCHORS + EXPECTED_HELDOUTS
    protocol_sha = sha256_file(PROTOCOL)
    protocol_integrity = (
        payload.get("run_id") == "R056_TRUE_IMAGE_REFINEMENT"
        and payload.get("protocol")
        == "research/refine-logs/R056_TRUE_IMAGE_REFINEMENT_PROTOCOL.json"
        and payload.get("protocol_sha256") == protocol_sha
        and observed_order == expected_order
        and protocol.get("run_id") == "R056_TRUE_IMAGE_REFINEMENT"
        and protocol.get("status") == "FROZEN_BEFORE_HELDOUT_PRODUCTION"
    )
    schema_pass = len(records) == 10 and all(_record_schema_pass(record) for record in records)

    parent_hashes = {
        str(item["role"]): str(item["sha256"])
        for item in protocol["parent_artifacts"]
    }
    parent_hash_alignment = payload.get("parent_artifact_sha256") == parent_hashes
    anchor_alignment = list(payload.get("anchor_alignment", []))
    anchor_reconstruction = (
        len(anchor_alignment) == 4
        and tuple(str(row.get("configuration")) for row in anchor_alignment)
        == EXPECTED_ANCHORS
        and all(bool(row.get("all_fields_match")) for row in anchor_alignment)
    )
    replay = payload.get("serial_parallel_replay", {})
    serial_parallel = bool(replay.get("all_hashes_match"))
    independent_refinements = independent.get("persisted_refinement_projections")
    independent_pass = (
        independent.get("run_id")
        == "R056_TRUE_IMAGE_REFINEMENT_INDEPENDENT_CHECK"
        and independent.get("checker_imports_producer_geometry_or_scc_helpers") is False
        and independent.get("all_checks_pass") is True
        and isinstance(independent_refinements, dict)
        and independent_refinements.get("pass") is True
    )
    g0 = all(
        (
            protocol_integrity,
            schema_pass,
            parent_hash_alignment,
            anchor_reconstruction,
            serial_parallel,
            independent_pass,
        )
    )

    heldout_rows: list[dict[str, Any]] = []
    for name in EXPECTED_HELDOUTS:
        record = records_by_name.get(name, {})
        g1_checks = {
            "exact_edge_integrity": record.get("exact_edge_integrity_pass") is True,
            "uncapped_k_below_cap": int(record.get("uncapped_k_max", 10**9)) < 64,
            "cap_inactive": int(record.get("cap_active_count", -1)) == 0,
            "pre_freeze_k_match": record.get("pre_freeze_uncapped_k_max_match") is True,
            "local_variation_bound": record.get("local_variation_bound_pass") is True,
            "outer_area_ratio_bound": record.get("outer_area_ratio_bound_pass") is True,
            "candidate_hull_contains_true": record.get(
                "candidate_hull_contains_true_pass"
            )
            is True,
            "true_subset_outer": record.get("true_edge_subset_outer_pass") is True,
            "true_positive_subset_outer_positive": record.get(
                "true_positive_subset_outer_positive_pass"
            )
            is True,
            "labelled_transpose": record.get(
                "true_forward_inverse_labelled_transpose_pass"
            )
            is True,
            "active_rule_identity": record.get(
                "slab_active_equals_analytic_hull_active_pass"
            )
            is True,
        }
        g2_checks = {
            "closed_forward": record.get(
                "true_closed_equals_mutual_outer_forward_pass"
            )
            is True,
            "closed_backward": record.get(
                "true_closed_equals_mutual_outer_backward_pass"
            )
            is True,
            "positive_forward": record.get(
                "true_positive_equals_outer_positive_forward_pass"
            )
            is True,
            "positive_backward": record.get(
                "true_positive_equals_outer_positive_backward_pass"
            )
            is True,
            "all_symmetric_differences_zero": all(
                int(record.get(field, -1)) == 0
                for field in (
                    "true_closed_mutual_outer_forward_symmetric_difference_count",
                    "true_closed_mutual_outer_backward_symmetric_difference_count",
                    "true_positive_outer_positive_forward_symmetric_difference_count",
                    "true_positive_outer_positive_backward_symmetric_difference_count",
                )
            ),
        }
        g3_checks = {
            "closed_multi_node_scc": int(
                record.get("true_closed_graph", {}).get("multi_node_scc_count", 0)
            )
            > 0,
            "positive_multi_node_scc": int(
                record.get("true_positive_graph", {}).get("multi_node_scc_count", 0)
            )
            > 0,
        }
        heldout_rows.append(
            {
                "configuration": name,
                "g1_checks": g1_checks,
                "g1_pass": all(g1_checks.values()),
                "g2_checks": g2_checks,
                "g2_pass": all(g2_checks.values()),
                "g3_checks": g3_checks,
                "g3_pass": all(g3_checks.values()),
            }
        )
    g1 = len(heldout_rows) == 6 and all(row["g1_pass"] for row in heldout_rows)
    g2 = len(heldout_rows) == 6 and all(row["g2_pass"] for row in heldout_rows)
    heldout_scc = len(heldout_rows) == 6 and all(
        row["g3_pass"] for row in heldout_rows
    )

    refinements = list(payload.get("refinements", []))
    observed_refinements = tuple(
        (str(row.get("parent_configuration")), str(row.get("child_configuration")))
        for row in refinements
    )
    refinement_rows: list[dict[str, Any]] = []
    for refinement in refinements:
        variant_checks: dict[str, dict[str, bool]] = {}
        for variant in ("true_closed", "true_positive"):
            metrics = refinement.get(variant, {})
            variant_checks[variant] = {
                "complete_forward_projection": metrics.get(
                    "complete_projection_equals_parent_pass"
                )
                is True,
                "complete_backward_projection": metrics.get(
                    "complete_backward_projection_equals_parent_pass"
                )
                is True,
                "matched_forward_projection": metrics.get(
                    "matched_support_projection_equals_parent_active_graph_pass"
                )
                is True,
                "matched_backward_projection": metrics.get(
                    "matched_support_backward_projection_equals_parent_active_graph_pass"
                )
                is True,
                "nontrivial_descendant": metrics.get(
                    "nontrivial_descendant_exists_pass"
                )
                is True,
            }
        exact_checks = {
            "exact_nested_edges": refinement.get("exact_nested_edge_vectors_pass")
            is True,
            "active_lift_subset": refinement.get(
                "lift_parent_active_subset_child_active_pass"
            )
            is True,
            "closed_exact_projection": all(
                value
                for key, value in variant_checks["true_closed"].items()
                if key != "nontrivial_descendant"
            ),
            "positive_exact_projection": all(
                value
                for key, value in variant_checks["true_positive"].items()
                if key != "nontrivial_descendant"
            ),
        }
        descendant_checks = {
            "closed_nontrivial_descendant": variant_checks["true_closed"][
                "nontrivial_descendant"
            ],
            "positive_nontrivial_descendant": variant_checks["true_positive"][
                "nontrivial_descendant"
            ],
        }
        refinement_rows.append(
            {
                "parent_configuration": refinement.get("parent_configuration"),
                "child_configuration": refinement.get("child_configuration"),
                "exact_checks": exact_checks,
                "exact_refinement_pass": all(exact_checks.values()),
                "descendant_checks": descendant_checks,
                "descendant_pass": all(descendant_checks.values()),
            }
        )
    g4 = (
        observed_refinements == EXPECTED_REFINEMENTS
        and len(refinement_rows) == 3
        and all(row["exact_refinement_pass"] for row in refinement_rows)
    )
    descendant_scc = len(refinement_rows) == 3 and all(
        row["descendant_pass"] for row in refinement_rows
    )
    g3 = heldout_scc and descendant_scc

    primary_pass = g0 and g1 and g2
    supporting_pass = g3 and g4
    all_frozen = primary_pass and supporting_pass
    if not g0:
        interpretation = "INVALID_AUDIT_INTEGRITY_FAILURE"
    elif not g2:
        interpretation = "PRIMARY_IDENTITY_FAILED_R055_REMAINS_DEVELOPMENT_ONLY"
    elif not g3:
        interpretation = "PRIMARY_REPLICATED_BUT_RECURRENT_CORE_ROUTE_WEAKENED"
    elif not g4:
        interpretation = "PRIMARY_REPLICATED_BUT_REFINEMENT_CONSISTENCY_FAILED"
    else:
        interpretation = "PRIMARY_AND_SUPPORTING_FINITE_GATES_PASS"

    decisions: dict[str, Any] = {
        "configuration_count": len(records),
        "anchor_count": len(EXPECTED_ANCHORS),
        "heldout_count": len(EXPECTED_HELDOUTS),
        "protocol_integrity_pass": protocol_integrity,
        "schema_pass": schema_pass,
        "parent_artifact_hash_alignment_pass": parent_hash_alignment,
        "anchor_reconstruction_pass": anchor_reconstruction,
        "serial_parallel_replay_pass": serial_parallel,
        "independent_checker_pass": independent_pass,
        "g0_anchor_and_integrity_pass": g0,
        "g1_exact_integrity_pass": g1,
        "g2_primary_identity_6_of_6_pass": g2,
        "g3_nontrivial_scc_and_descendant_pass": g3,
        "g4_exact_refinement_pass": g4,
        "primary_claim_pass": primary_pass,
        "supporting_claim_pass": supporting_pass,
        "all_frozen_checks_pass": all_frozen,
        "heldout_gate_rows": heldout_rows,
        "refinement_gate_rows": refinement_rows,
        "interpretation": interpretation,
        "centered_largest_scc_scaling": {
            "true_closed": loglog_fit(records_by_name, "true_closed_graph"),
            "true_positive": loglog_fit(records_by_name, "true_positive_graph"),
            "threshold_used": None,
        },
        "shifted_core_comparisons": payload.get("shifted_core_comparisons", []),
        "scope_statement": protocol.get("scope"),
    }

    enriched: list[dict[str, Any]] = []
    heldout_gate_by_name = {row["configuration"]: row for row in heldout_rows}
    for record in records:
        row = dict(record)
        name = str(record["configuration"])
        if name in heldout_gate_by_name:
            row["heldout_g1_pass"] = heldout_gate_by_name[name]["g1_pass"]
            row["heldout_g2_pass"] = heldout_gate_by_name[name]["g2_pass"]
            row["heldout_g3_pass"] = heldout_gate_by_name[name]["g3_pass"]
        enriched.append(row)
    return decisions, enriched


def write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    rows: list[dict[str, object]] = []
    for record in records:
        rows.append(
            {
                "configuration": record["configuration"],
                "evidence_role": record["evidence_role"],
                "grid": record["grid"],
                "grid_offset_fraction": record["grid_offset_fraction"],
                "uncapped_k_max": record["uncapped_k_max"],
                "active_node_count": record["active_node_count"],
                "true_closed_edge_count": record["true_forward_closed_edge_count"],
                "true_positive_edge_count": record[
                    "true_forward_positive_edge_count"
                ],
                "true_closed_largest_scc_size": record["true_closed_graph"][
                    "largest_scc_size"
                ],
                "true_positive_largest_scc_size": record["true_positive_graph"][
                    "largest_scc_size"
                ],
                "true_closed_recurrent_multi_node_count": record[
                    "true_closed_graph"
                ]["multi_node_recurrent_node_count"],
                "true_positive_recurrent_multi_node_count": record[
                    "true_positive_graph"
                ]["multi_node_recurrent_node_count"],
                "heldout_g1_pass": record.get("heldout_g1_pass"),
                "heldout_g2_pass": record.get("heldout_g2_pass"),
                "heldout_g3_pass": record.get("heldout_g3_pass"),
            }
        )
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    independent = json.loads(args.independent_input.read_text(encoding="utf-8"))
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    decisions, records = analyze_payload(payload, independent, protocol)
    output = {
        "run_id": "R056_TRUE_IMAGE_REFINEMENT_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "producer_input": str(args.input),
        "independent_checker_input": str(args.independent_input),
        "decisions": decisions,
        "records": records,
        "scope": protocol.get("scope"),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_csv(output_csv, records)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "decisions": decisions,
            },
            indent=2,
        )
    )
    if not decisions["all_frozen_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
