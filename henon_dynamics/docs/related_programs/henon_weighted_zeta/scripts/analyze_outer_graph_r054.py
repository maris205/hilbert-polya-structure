#!/usr/bin/env python3
"""Analyze the exploratory R054 graph built from the exact R053 cover."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
R053_RESULT = PROJECT_ROOT / "results" / "exact_closed_cover_r053.json"

EXPECTED_CONFIGURATIONS = (
    ("n96_d0", 96, "0"),
    ("n160_d0", 160, "0"),
    ("n160_dm1q", 160, "-1/4"),
    ("n160_dp1q", 160, "1/4"),
)
GRAPH_VARIANTS = ("all_closed_graph", "positive_area_graph", "mutual_graph")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "outer_graph_r054.json",
    )
    parser.add_argument(
        "--parent-input", type=Path, default=R053_RESULT
    )
    parser.add_argument(
        "--output-stem", default="outer_graph_analysis_r054"
    )
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _expected_record_order(records: list[dict[str, Any]]) -> bool:
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
        "two_sided_in_box_node_fraction",
        "two_sided_in_box_node_ids_sha256",
        "forward_closed_edge_count",
        "backward_closed_edge_count",
        "forward_positive_edge_count",
        "backward_positive_edge_count",
        "mutual_edge_count",
        "forward_closed_edge_hash",
        "backward_closed_edge_hash",
        "closed_contains_positive",
        "mutual_subset_closed",
        *GRAPH_VARIANTS,
    }
    if not required <= set(record):
        return False
    active = record["two_sided_in_box_node_count"]
    total = record["state_count"]
    if not isinstance(active, int) or not isinstance(total, int) or not (0 <= active <= total):
        return False
    if not _finite_number(record["two_sided_in_box_node_fraction"]):
        return False
    if (
        not isinstance(record["two_sided_in_box_node_ids_sha256"], str)
        or len(record["two_sided_in_box_node_ids_sha256"]) != 64
    ):
        return False
    for variant in GRAPH_VARIANTS:
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
        for key in (
            "largest_scc_fraction_of_active",
            "recurrent_node_fraction_of_active",
        ):
            if not _finite_number(stats.get(key)):
                return False
    return True


def analyze_payload(
    payload: dict[str, Any], parent_payload: dict[str, Any]
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    records = list(payload.get("records", []))
    parent_records = list(parent_payload.get("records", []))
    parent_by_name = {
        str(record.get("configuration")): record for record in parent_records
    }

    protocol_pass = (
        payload.get("run_id") == "R054_OUTER_GRAPH"
        and payload.get("protocol")
        == "research/refine-logs/R054_OUTER_GRAPH_PROTOCOL.json"
        and len(records) == len(EXPECTED_CONFIGURATIONS)
        and _expected_record_order(records)
    )
    schema_pass = bool(records) and all(_schema_pass(record) for record in records)

    parent_alignment_rows: list[dict[str, Any]] = []
    for record in records:
        name = str(record.get("configuration"))
        parent = parent_by_name.get(name)
        if parent is None:
            parent_alignment_rows.append(
                {"configuration": name, "match": False, "reason": "missing R053 record"}
            )
            continue
        row = {
            "configuration": name,
            "state_count_match": record.get("state_count") == parent.get("state_count"),
            "forward_closed_count_match": record.get("forward_closed_edge_count")
            == parent.get("forward_closed_adjacency_count"),
            "backward_closed_count_match": record.get("backward_closed_edge_count")
            == parent.get("backward_closed_adjacency_count"),
            "forward_positive_count_match": record.get("forward_positive_edge_count")
            == parent.get("forward_positive_area_adjacency_count"),
            "backward_positive_count_match": record.get("backward_positive_edge_count")
            == parent.get("backward_positive_area_adjacency_count"),
            "forward_hash_match": record.get("forward_closed_edge_hash")
            == parent.get("forward_closed_adjacency_sha256"),
            "backward_hash_match": record.get("backward_closed_edge_hash")
            == parent.get("backward_closed_adjacency_sha256"),
        }
        row["match"] = all(value for key, value in row.items() if key != "configuration")
        parent_alignment_rows.append(row)
    parent_alignment_pass = bool(parent_alignment_rows) and all(
        bool(row.get("match")) for row in parent_alignment_rows
    )

    active_node_consistency_pass = bool(records) and all(
        all(
            record[variant]["active_node_count"]
            == record["two_sided_in_box_node_count"]
            for variant in GRAPH_VARIANTS
        )
        for record in records
    )
    graph_subset_pass = bool(records) and all(
        bool(record.get("closed_contains_positive"))
        and bool(record.get("mutual_subset_closed"))
        for record in records
    )
    graph_count_sanity_pass = bool(records) and all(
        record["forward_closed_edge_count"]
        == record["backward_closed_edge_count"]
        and record["forward_positive_edge_count"]
        == record["backward_positive_edge_count"]
        and record["forward_positive_edge_count"]
        <= record["forward_closed_edge_count"]
        and record["mutual_edge_count"]
        <= record["forward_closed_edge_count"]
        for record in records
    )

    by_name = {str(record["configuration"]): record for record in records}
    minus = by_name.get("n160_dm1q")
    plus = by_name.get("n160_dp1q")
    shifted_sign_control = {
        "present": bool(minus and plus),
        "same_state_count": bool(minus and plus and minus["state_count"] == plus["state_count"]),
        "two_sided_node_count_delta": (
            abs(minus["two_sided_in_box_node_count"] - plus["two_sided_in_box_node_count"])
            if minus and plus
            else None
        ),
        "forward_closed_edge_count_delta": (
            abs(minus["forward_closed_edge_count"] - plus["forward_closed_edge_count"])
            if minus and plus
            else None
        ),
        "forward_positive_edge_count_delta": (
            abs(minus["forward_positive_edge_count"] - plus["forward_positive_edge_count"])
            if minus and plus
            else None
        ),
        "mutual_edge_count_delta": (
            abs(minus["mutual_edge_count"] - plus["mutual_edge_count"])
            if minus and plus
            else None
        ),
    }
    if minus and plus:
        for variant in GRAPH_VARIANTS:
            shifted_sign_control[f"{variant}_largest_scc_size_delta"] = abs(
                minus[variant]["largest_scc_size"] - plus[variant]["largest_scc_size"]
            )
            shifted_sign_control[f"{variant}_recurrent_fraction_delta"] = abs(
                minus[variant]["recurrent_node_fraction_of_active"]
                - plus[variant]["recurrent_node_fraction_of_active"]
            )

    all_stats = [record["all_closed_graph"] for record in records]
    positive_stats = [record["positive_area_graph"] for record in records]
    mutual_stats = [record["mutual_graph"] for record in records]
    decisions: dict[str, Any] = {
        "configuration_count": len(records),
        "protocol_and_configuration_pass": protocol_pass,
        "schema_pass": schema_pass,
        "parent_r053_alignment_pass": parent_alignment_pass,
        "parent_r053_alignment_rows": parent_alignment_rows,
        "active_node_consistency_pass": active_node_consistency_pass,
        "graph_subset_invariants_pass": graph_subset_pass,
        "graph_count_sanity_pass": graph_count_sanity_pass,
        "all_frozen_checks_pass": all(
            (
                protocol_pass,
                schema_pass,
                parent_alignment_pass,
                active_node_consistency_pass,
                graph_subset_pass,
                graph_count_sanity_pass,
            )
        ),
        "shifted_sign_control": shifted_sign_control,
        "two_sided_node_fraction_min": min(
            float(record["two_sided_in_box_node_fraction"]) for record in records
        )
        if records
        else None,
        "two_sided_node_fraction_max": max(
            float(record["two_sided_in_box_node_fraction"]) for record in records
        )
        if records
        else None,
        "all_closed_largest_scc_size_min": min(
            int(stats["largest_scc_size"]) for stats in all_stats
        )
        if all_stats
        else None,
        "all_closed_largest_scc_size_max": max(
            int(stats["largest_scc_size"]) for stats in all_stats
        )
        if all_stats
        else None,
        "positive_area_largest_scc_size_min": min(
            int(stats["largest_scc_size"]) for stats in positive_stats
        )
        if positive_stats
        else None,
        "positive_area_largest_scc_size_max": max(
            int(stats["largest_scc_size"]) for stats in positive_stats
        )
        if positive_stats
        else None,
        "mutual_largest_scc_size_min": min(
            int(stats["largest_scc_size"]) for stats in mutual_stats
        )
        if mutual_stats
        else None,
        "mutual_largest_scc_size_max": max(
            int(stats["largest_scc_size"]) for stats in mutual_stats
        )
        if mutual_stats
        else None,
        "scope_statement": (
            "SCCs are finite graph cores of exact rectangle outer-cover incidences; "
            "they are not invariant sets, Markov partitions, covering relations, "
            "or true-image graph certificates."
        ),
    }

    # Add flat, report-friendly fields to each row without discarding raw graph stats.
    enriched: list[dict[str, Any]] = []
    for record in records:
        row = dict(record)
        closed_edges = int(record["forward_closed_edge_count"])
        positive_edges = int(record["forward_positive_edge_count"])
        row["forward_touch_only_edge_count"] = closed_edges - positive_edges
        row["forward_positive_edge_fraction"] = positive_edges / closed_edges
        row["all_closed_induced_edge_density"] = record["all_closed_graph"][
            "induced_edge_count"
        ] / record["all_closed_graph"]["active_node_count"]
        row["positive_area_induced_edge_density"] = record["positive_area_graph"][
            "induced_edge_count"
        ] / record["positive_area_graph"]["active_node_count"]
        row["mutual_induced_edge_density"] = record["mutual_graph"][
            "induced_edge_count"
        ] / record["mutual_graph"]["active_node_count"]
        enriched.append(row)
    return decisions, enriched


def main() -> None:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    parent_payload = json.loads(args.parent_input.read_text(encoding="utf-8"))
    decisions, records = analyze_payload(payload, parent_payload)
    output = {
        "run_id": "R054_OUTER_GRAPH_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "decisions": decisions,
        "records": records,
        "scope": (
            "exploratory finite directed graphs induced by exact R053 rectangle "
            "outer-cover contacts; no invariant-set, Markov, covering, or "
            "operator-convergence claim"
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
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "decisions": decisions,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
