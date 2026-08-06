#!/usr/bin/env python3
"""Run the frozen R058 true-positive filament replication.

The heavy geometry is reused from the already audited R056 exact producer.
R058 changes the evidence object: three new locked 4x chains are followed by
an explicit multilevel true-positive descendant lineage.  Closed graphs are
computed as side products but cannot rescue a positive-lineage failure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_exact_closed_cover import (  # noqa: E402
    RADIUS,
    exact_edge_vector,
    uncapped_adaptive_subdivisions_exact,
)
from scripts.audit_outer_graph_r054 import node_hash  # noqa: E402
from scripts.audit_true_image_refinement_r056 import (  # noqa: E402
    build_configuration,
    build_refinement_record,
    components_from_pairs,
    exact_ratio,
    fraction_payload,
    geometric_intersection_area,
    graph_pairs,
    induced_pairs,
    lift_nodes,
    load_edge_arrays,
    node_union_area,
    project_nodes,
    save_npz_atomic,
    serial_parallel_match,
    sha256_file,
    write_csv,
)


PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R058_HYPERBOLIC_FILAMENT_PROTOCOL.json"
)
PROTOCOL_SHA256 = "bdd851ac14fb5cbe89ce4592b4f0e9f6cbe4fa4b76778530a2e19e7e0f1dd6f3"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "results"
DEFAULT_EDGE_DIR = DEFAULT_OUTPUT_DIR / "hyperbolic_filament_r058_edges"
DEFAULT_PREFLIGHT_OUTPUT = (
    DEFAULT_OUTPUT_DIR / "hyperbolic_filament_preflight_r058.json"
)
CHAIN_ORDER = ("centered", "positive_phase", "negative_phase")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--edge-dir", type=Path, default=DEFAULT_EDGE_DIR)
    parser.add_argument("--output-stem", default="hyperbolic_filament_r058")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument(
        "--preflight-output",
        type=Path,
        default=DEFAULT_PREFLIGHT_OUTPUT,
    )
    return parser.parse_args()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def load_protocol() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    protocol_hash = sha256_file(PROTOCOL)
    checks = {
        "sha256": protocol_hash == PROTOCOL_SHA256,
        "run_id": payload.get("run_id") == "R058_HYPERBOLIC_FILAMENT",
        "status": payload.get("status") == "FROZEN_BEFORE_R058_PRODUCTION",
        "heldout_count": len(payload.get("heldout_configurations", [])) == 9,
        "refinement_count": len(payload.get("nested_refinements", [])) == 6,
        "chain_order": list(
            dict.fromkeys(
                item["chain"] for item in payload["heldout_configurations"]
            )
        )
        == list(CHAIN_ORDER),
    }
    parent_records: dict[str, dict[str, object]] = {}
    for item in payload["parent_artifacts"]:
        path = PROJECT_ROOT / item["path"]
        actual = sha256_file(path)
        parent_records[item["role"]] = {
            "path": item["path"],
            "expected_sha256": item["sha256"],
            "actual_sha256": actual,
            "pass": actual == item["sha256"],
        }
    checks["parent_hashes"] = all(
        bool(item["pass"]) for item in parent_records.values()
    )
    if not all(checks.values()):
        raise SystemExit(f"R058 protocol integrity failure: {checks}")
    return payload, {
        "protocol_path": portable_path(PROTOCOL),
        "protocol_sha256": protocol_hash,
        "checks": checks,
        "parent_artifacts": parent_records,
        "pass": True,
    }


def heldout_job(item: dict[str, Any], edge_dir: Path) -> dict[str, Any]:
    name = str(item["configuration_id"])
    return {
        "configuration": name,
        "grid": int(item["grid"]),
        "offset": Fraction(str(item["grid_offset"])),
        "evidence_role": "r058_locked_heldout",
        "protocol_role": f"{item['chain']}_level_{item['level']}",
        "pre_freeze_uncapped_k_max": int(item["pre_freeze_uncapped_k_max"]),
        "edge_path": edge_dir / f"{name}.npz",
    }


def anchor_jobs(edge_dir: Path) -> list[dict[str, Any]]:
    return [
        {
            "configuration": "n160_d0",
            "grid": 160,
            "offset": Fraction(0),
            "evidence_role": "r058_development_anchor",
            "protocol_role": "r056_positive_lineage_parent_replay",
            "pre_freeze_uncapped_k_max": 31,
            "edge_path": edge_dir / "anchor_n160_d0.npz",
        },
        {
            "configuration": "n320_d0",
            "grid": 320,
            "offset": Fraction(0),
            "evidence_role": "r058_development_anchor",
            "protocol_role": "r056_positive_lineage_child_replay",
            "pre_freeze_uncapped_k_max": 31,
            "edge_path": edge_dir / "anchor_n320_d0.npz",
        },
    ]


def run_jobs_with_progress(
    jobs: list[dict[str, Any]],
    workers: int,
    label: str,
) -> list[dict[str, Any]]:
    if workers <= 0:
        raise SystemExit("--workers must be positive")
    worker_count = min(workers, len(jobs))
    if worker_count == 1:
        output = []
        for index, job in enumerate(jobs, start=1):
            record = build_configuration(job)
            output.append(record)
            print(
                f"[{label}] {index}/{len(jobs)} complete: "
                f"{job['configuration']}",
                flush=True,
            )
        return output

    order = {str(job["configuration"]): index for index, job in enumerate(jobs)}
    completed: list[dict[str, Any]] = []
    with ProcessPoolExecutor(max_workers=worker_count) as executor:
        futures = {
            executor.submit(build_configuration, job): str(job["configuration"])
            for job in jobs
        }
        for count, future in enumerate(as_completed(futures), start=1):
            name = futures[future]
            completed.append(future.result())
            print(
                f"[{label}] {count}/{len(jobs)} complete: {name}",
                flush=True,
            )
    return sorted(completed, key=lambda row: order[str(row["configuration"])])


def preflight_protocol(
    protocol: dict[str, Any],
    integrity: dict[str, Any],
) -> dict[str, Any]:
    configurations: list[dict[str, object]] = []
    by_name: dict[str, dict[str, object]] = {}
    for item in protocol["heldout_configurations"]:
        grid = int(item["grid"])
        offset = Fraction(str(item["grid_offset"]))
        edges = exact_edge_vector(RADIUS, grid, offset)
        minimum_width = min(
            upper - lower for lower, upper in zip(edges, edges[1:])
        )
        k_values = [
            uncapped_adaptive_subdivisions_exact(lower, upper, minimum_width)
            for lower, upper in zip(edges, edges[1:])
        ]
        observed = max(k_values)
        expected = int(item["pre_freeze_uncapped_k_max"])
        record = {
            "configuration": item["configuration_id"],
            "grid": grid,
            "offset": fraction_text(offset),
            "chain": item["chain"],
            "level": int(item["level"]),
            "uncapped_k_max": observed,
            "expected_uncapped_k_max": expected,
            "k_match": observed == expected,
            "below_cap": observed < int(
                protocol["graph_constants"]["maximum_subdivisions"]
            ),
            "edge_count": len(edges),
            "edge_sha256": hashlib.sha256(
                "\n".join(fraction_text(value) for value in edges).encode("ascii")
            ).hexdigest(),
        }
        configurations.append(record)
        by_name[str(item["configuration_id"])] = {
            **record,
            "edges": edges,
        }

    refinements: list[dict[str, object]] = []
    for parent_name, child_name in protocol["nested_refinements"]:
        parent = by_name[parent_name]
        child = by_name[child_name]
        parent_grid = int(parent["grid"])
        child_grid = int(child["grid"])
        nested = child_grid == 2 * parent_grid and all(
            parent["edges"][index] == child["edges"][2 * index]
            for index in range(parent_grid + 1)
        )
        refinements.append(
            {
                "parent": parent_name,
                "child": child_name,
                "ratio": child_grid // parent_grid,
                "exact_nested": nested,
            }
        )

    pass_value = (
        integrity["pass"]
        and all(bool(row["k_match"]) and bool(row["below_cap"]) for row in configurations)
        and all(bool(row["exact_nested"]) for row in refinements)
    )
    return {
        "run_id": "R058_HYPERBOLIC_FILAMENT_PREFLIGHT",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_integrity": integrity,
        "configurations": configurations,
        "refinements": refinements,
        "pass": pass_value,
    }


def anchor_alignment(
    anchor_records: list[dict[str, Any]],
    edge_dir: Path,
) -> dict[str, Any]:
    parent_payload = json.loads(
        (PROJECT_ROOT / "results" / "true_image_refinement_r056.json").read_text(
            encoding="utf-8"
        )
    )
    parent_by_name = {
        str(record["configuration"]): record for record in parent_payload["records"]
    }
    fields = (
        "active_node_ids_sha256",
        "true_forward_positive_unlabelled_edge_hash",
        "true_backward_positive_unlabelled_edge_hash",
        "true_forward_inverse_labelled_transpose_pass",
        "true_positive_equals_outer_positive_forward_pass",
        "true_positive_equals_outer_positive_backward_pass",
    )
    record_checks: list[dict[str, Any]] = []
    for record in anchor_records:
        parent = parent_by_name[str(record["configuration"])]
        checks = {field: record[field] == parent[field] for field in fields}
        checks.update(
            {
                "positive_largest_scc_size": record["true_positive_graph"][
                    "largest_scc_size"
                ]
                == parent["true_positive_graph"]["largest_scc_size"],
                "positive_largest_scc_hash": record["true_positive_graph"][
                    "largest_scc_node_ids_sha256"
                ]
                == parent["true_positive_graph"]["largest_scc_node_ids_sha256"],
            }
        )
        record_checks.append(
            {
                "configuration": record["configuration"],
                "checks": checks,
                "pass": all(checks.values()),
            }
        )

    by_name = {
        str(record["configuration"]): record for record in anchor_records
    }
    replay_refinement = build_refinement_record(
        {
            "parent_configuration_id": "n160_d0",
            "child_configuration_id": "n320_d0",
        },
        by_name,
        edge_dir,
    )
    parent_refinement = next(
        row
        for row in parent_payload["refinements"]
        if row["parent_configuration"] == "n160_d0"
        and row["child_configuration"] == "n320_d0"
    )
    positive_fields = (
        "complete_projection_equals_parent_pass",
        "complete_backward_projection_equals_parent_pass",
        "matched_support_projection_equals_parent_active_graph_pass",
        "matched_support_backward_projection_equals_parent_active_graph_pass",
        "nontrivial_descendant_exists_pass",
        "parent_dominant_scc_node_ids_sha256",
        "largest_descendant_node_ids_sha256",
    )
    refinement_checks = {
        "exact_nested_edge_vectors_pass": replay_refinement[
            "exact_nested_edge_vectors_pass"
        ]
        == parent_refinement["exact_nested_edge_vectors_pass"],
        "active_lift_missing_count": replay_refinement[
            "active_lift_missing_child_node_count"
        ]
        == parent_refinement["active_lift_missing_child_node_count"],
        **{
            field: replay_refinement["true_positive"][field]
            == parent_refinement["true_positive"][field]
            for field in positive_fields
        },
    }
    return {
        "records": record_checks,
        "positive_refinement_checks": refinement_checks,
        "pass": all(row["pass"] for row in record_checks)
        and all(refinement_checks.values()),
    }


def exact_fraction(payload: dict[str, object]) -> Fraction:
    return Fraction(str(payload["fraction"]))


def chain_lineage(
    chain: str,
    names: Sequence[str],
    records_by_name: dict[str, dict[str, Any]],
    edge_dir: Path,
) -> tuple[dict[str, Any], list[set[int]]]:
    root = records_by_name[names[0]]
    root_grid = int(root["grid"])
    current_nodes = {
        int(node) for node in root["true_positive_graph"]["largest_scc_node_ids"]
    }
    if len(current_nodes) <= 1:
        raise AssertionError(f"R058 root positive SCC is trivial: {names[0]}")
    root_edges = exact_edge_vector(
        RADIUS,
        root_grid,
        Fraction(str(root["grid_offset_fraction"])),
    )
    root_area = node_union_area(root_edges, root_grid, current_nodes)
    lineage_nodes = [set(current_nodes)]
    sizes = [len(current_nodes)]
    areas = [root_area]
    steps: list[dict[str, Any]] = []

    for parent_name, child_name in zip(names, names[1:]):
        parent = records_by_name[parent_name]
        child = records_by_name[child_name]
        parent_grid = int(parent["grid"])
        child_grid = int(child["grid"])
        if child_grid != 2 * parent_grid:
            raise AssertionError(f"non-2x lineage: {parent_name}->{child_name}")
        parent_edges = exact_edge_vector(
            RADIUS,
            parent_grid,
            Fraction(str(parent["grid_offset_fraction"])),
        )
        child_edges = exact_edge_vector(
            RADIUS,
            child_grid,
            Fraction(str(child["grid_offset_fraction"])),
        )
        exact_nested = all(
            parent_edges[index] == child_edges[2 * index]
            for index in range(parent_grid + 1)
        )
        lifted = lift_nodes(current_nodes, parent_grid, child_grid)
        child_arrays = load_edge_arrays(child)
        child_positive = graph_pairs(child_arrays["true_forward_edges"], True)
        matched_pairs = induced_pairs(child_positive, lifted)
        components = components_from_pairs(matched_pairs, lifted)
        descendants = [
            component
            for component in components
            if len(component) > 1
            and project_nodes(component, child_grid, parent_grid) <= current_nodes
        ]
        selected = set(descendants[0]) if descendants else set()
        parent_area = node_union_area(parent_edges, parent_grid, current_nodes)
        lifted_area = node_union_area(child_edges, child_grid, lifted)
        selected_area = node_union_area(child_edges, child_grid, selected)
        coverage = selected_area / lifted_area if lifted_area else Fraction(0)
        steps.append(
            {
                "parent": parent_name,
                "child": child_name,
                "exact_nested_edges_pass": exact_nested,
                "parent_lineage_node_count": len(current_nodes),
                "parent_lineage_node_ids_sha256": node_hash(current_nodes),
                "parent_lineage_area": fraction_payload(parent_area),
                "lifted_parent_node_count": len(lifted),
                "lifted_parent_area": fraction_payload(lifted_area),
                "matched_support_edge_count": len(matched_pairs),
                "multi_node_descendant_count": len(descendants),
                "selected_descendant_node_count": len(selected),
                "selected_descendant_node_ids_sha256": node_hash(selected),
                "selected_descendant_area": fraction_payload(selected_area),
                "selected_descendant_lifted_area_coverage": fraction_payload(
                    coverage
                ),
                "nontrivial_descendant_pass": len(selected) > 1,
            }
        )
        current_nodes = selected
        lineage_nodes.append(set(current_nodes))
        sizes.append(len(current_nodes))
        areas.append(selected_area)

    exponent = (
        math.log(sizes[-1] / sizes[0]) / math.log(4)
        if sizes[0] > 0 and sizes[-1] > 0
        else float("nan")
    )
    gate = records_by_name[names[0]]
    lower, upper = (
        float(value)
        for value in gate["_r058_exponent_interval"]
    )
    coverage_lower, coverage_upper = (
        float(value)
        for value in gate["_r058_coverage_interval"]
    )
    checks = {
        "all_three_nontrivial": all(size > 1 for size in sizes),
        "sizes_strictly_increasing": sizes[0] < sizes[1] < sizes[2],
        "areas_strictly_decreasing": areas[0] > areas[1] > areas[2],
        "four_x_exponent_in_interval": lower <= exponent <= upper,
        "both_exact_nested": all(step["exact_nested_edges_pass"] for step in steps),
        "both_nontrivial_descendants": all(
            step["nontrivial_descendant_pass"] for step in steps
        ),
        "both_coverages_in_interval": all(
            coverage_lower
            <= float(step["selected_descendant_lifted_area_coverage"]["float"])
            <= coverage_upper
            for step in steps
        ),
    }
    artifact = edge_dir / f"lineage_{chain}.npz"
    save_npz_atomic(
        artifact,
        level0_node_ids=np.asarray(sorted(lineage_nodes[0]), dtype=np.int64),
        level1_node_ids=np.asarray(sorted(lineage_nodes[1]), dtype=np.int64),
        level2_node_ids=np.asarray(sorted(lineage_nodes[2]), dtype=np.int64),
    )
    return (
        {
            "chain": chain,
            "configurations": list(names),
            "lineage_sizes": sizes,
            "lineage_areas": [fraction_payload(area) for area in areas],
            "four_x_size_exponent": exponent,
            "steps": steps,
            "artifact_path": portable_path(artifact),
            "artifact_sha256": sha256_file(artifact),
            "checks": checks,
            "pass": all(checks.values()),
        },
        lineage_nodes,
    )


def positive_overlap(
    first: tuple[Fraction, Fraction],
    second: tuple[Fraction, Fraction],
) -> bool:
    return max(first[0], second[0]) < min(first[1], second[1])


def node_states(
    node: int,
    grid: int,
    edges: Sequence[Fraction],
    state_intervals: dict[str, tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]],
) -> set[str]:
    x_index, y_index = node % grid, node // grid
    cell_x = edges[x_index], edges[x_index + 1]
    cell_y = edges[y_index], edges[y_index + 1]
    return {
        state
        for state, (state_x, state_y) in state_intervals.items()
        if positive_overlap(cell_x, state_x) and positive_overlap(cell_y, state_y)
    }


def symbolic_bridge(
    name: str,
    lineage_nodes: set[int],
    record: dict[str, Any],
    protocol: dict[str, Any],
) -> dict[str, Any]:
    grid = int(record["grid"])
    edges = exact_edge_vector(
        RADIUS,
        grid,
        Fraction(str(record["grid_offset_fraction"])),
    )
    h_sets = protocol["h_sets"]
    x_intervals = {
        "-": tuple(Fraction(value) for value in h_sets["x_negative"]),
        "+": tuple(Fraction(value) for value in h_sets["x_positive"]),
    }
    y_intervals = {
        "-": tuple(Fraction(value) for value in h_sets["y_negative"]),
        "+": tuple(Fraction(value) for value in h_sets["y_positive"]),
    }
    state_intervals = {
        state: (x_intervals[state[0]], y_intervals[state[1]])
        for state in h_sets["state_order"]
    }
    memberships = {
        node: node_states(node, grid, edges, state_intervals)
        for node in lineage_nodes
    }
    state_counts = {
        state: sum(state in values for values in memberships.values())
        for state in h_sets["state_order"]
    }
    arrays = load_edge_arrays(record)
    positive_pairs = induced_pairs(
        graph_pairs(arrays["true_forward_edges"], True),
        lineage_nodes,
    )
    observed: set[tuple[str, str]] = set()
    contributing_edges = 0
    for source, target in positive_pairs:
        source_states = memberships[int(source)]
        target_states = memberships[int(target)]
        if source_states and target_states:
            contributing_edges += 1
        for source_state in source_states:
            for target_state in target_states:
                observed.add((source_state, target_state))
    allowed = {
        tuple(edge) for edge in protocol["symbolic_graph"]["allowed_edges"]
    }
    missing = sorted(allowed - observed)
    extra = sorted(observed - allowed)
    checks = {
        "all_four_states_nonempty": all(count > 0 for count in state_counts.values()),
        "all_allowed_transitions_present": not missing,
        "all_forbidden_transitions_absent": not extra,
    }
    return {
        "configuration": name,
        "lineage_node_count": len(lineage_nodes),
        "state_cell_counts": state_counts,
        "positive_lineage_edge_count": len(positive_pairs),
        "h_set_contributing_edge_count": contributing_edges,
        "observed_state_transitions": [list(edge) for edge in sorted(observed)],
        "missing_allowed_transitions": [list(edge) for edge in missing],
        "extra_forbidden_transitions": [list(edge) for edge in extra],
        "checks": checks,
        "pass": all(checks.values()),
    }


def finest_phase_overlaps(
    final_nodes: dict[str, set[int]],
    final_records: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    pairs = (
        ("centered", "positive_phase"),
        ("centered", "negative_phase"),
        ("positive_phase", "negative_phase"),
    )
    output: list[dict[str, Any]] = []
    for first, second in pairs:
        first_record, second_record = final_records[first], final_records[second]
        first_grid, second_grid = int(first_record["grid"]), int(second_record["grid"])
        first_edges = exact_edge_vector(
            RADIUS,
            first_grid,
            Fraction(str(first_record["grid_offset_fraction"])),
        )
        second_edges = exact_edge_vector(
            RADIUS,
            second_grid,
            Fraction(str(second_record["grid_offset_fraction"])),
        )
        first_area = node_union_area(
            first_edges, first_grid, final_nodes[first]
        )
        second_area = node_union_area(
            second_edges, second_grid, final_nodes[second]
        )
        intersection = geometric_intersection_area(
            final_nodes[first],
            first_edges,
            first_grid,
            final_nodes[second],
            second_edges,
            second_grid,
        )
        union = first_area + second_area - intersection
        output.append(
            {
                "first_chain": first,
                "second_chain": second,
                "first_area": fraction_payload(first_area),
                "second_area": fraction_payload(second_area),
                "intersection_area": fraction_payload(intersection),
                "intersection_over_first": exact_ratio(intersection, first_area),
                "intersection_over_second": exact_ratio(intersection, second_area),
                "geometric_jaccard": exact_ratio(intersection, union),
            }
        )
    return output


def heldout_integrity(record: dict[str, Any]) -> dict[str, object]:
    checks = {
        "exact_edges": record["exact_edge_integrity_pass"],
        "pre_freeze_k_match": record["pre_freeze_uncapped_k_max_match"],
        "cap_inactive": record["cap_active_count"] == 0,
        "candidate_contains_true": record["candidate_hull_contains_true_pass"],
        "true_positive_subset_outer": record[
            "true_positive_subset_outer_positive_pass"
        ],
        "labelled_transpose": record[
            "true_forward_inverse_labelled_transpose_pass"
        ],
        "positive_forward_identity": record[
            "true_positive_equals_outer_positive_forward_pass"
        ],
        "positive_backward_identity": record[
            "true_positive_equals_outer_positive_backward_pass"
        ],
        "positive_multi_node_scc": record["true_positive_graph"][
            "multi_node_scc_count"
        ]
        > 0,
    }
    return {
        "configuration": record["configuration"],
        "checks": checks,
        "pass": all(checks.values()),
    }


def main() -> None:
    args = parse_args()
    protocol, integrity = load_protocol()
    preflight = preflight_protocol(protocol, integrity)
    args.preflight_output.parent.mkdir(parents=True, exist_ok=True)
    args.preflight_output.write_text(
        json.dumps(preflight, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "preflight_output": portable_path(args.preflight_output),
                "preflight_pass": preflight["pass"],
                "workers": args.workers,
            },
            indent=2,
        ),
        flush=True,
    )
    if not preflight["pass"]:
        raise SystemExit("R058 preflight failed")
    if args.preflight_only:
        return

    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.edge_dir.mkdir(parents=True, exist_ok=True)

    anchors = run_jobs_with_progress(
        anchor_jobs(args.edge_dir),
        min(args.workers, 2),
        "anchor",
    )
    anchor_check = anchor_alignment(anchors, args.edge_dir)
    if not anchor_check["pass"]:
        raise SystemExit(f"R058 anchor replay failed: {anchor_check}")

    jobs = [
        heldout_job(item, args.edge_dir)
        for item in protocol["heldout_configurations"]
    ]
    heldouts = run_jobs_with_progress(jobs, min(args.workers, 6), "heldout")
    records_by_name = {
        str(record["configuration"]): record for record in heldouts
    }

    replay_source = next(
        job for job in jobs if job["configuration"] == "n113_dp1_12"
    )
    replay_job = dict(replay_source)
    replay_job["evidence_role"] = "r058_serial_replay"
    replay_job["edge_path"] = args.edge_dir / "n113_dp1_12_serial_replay.npz"
    replay_record = build_configuration(replay_job)
    replay_parallel = records_by_name["n113_dp1_12"]
    replay = serial_parallel_match(replay_parallel, replay_record)
    print("[replay] n113_dp1_12 serial/parallel complete", flush=True)

    refinement_records = [
        build_refinement_record(
            {
                "parent_configuration_id": parent,
                "child_configuration_id": child,
            },
            records_by_name,
            args.edge_dir,
        )
        for parent, child in protocol["nested_refinements"]
    ]
    print("[refinement] six exact projections complete", flush=True)

    exponent_interval = protocol["filament_gates"][
        "each_chain_four_x_size_exponent_interval"
    ]
    coverage_interval = protocol["filament_gates"][
        "each_level_descendant_lifted_area_coverage_interval"
    ]
    for record in heldouts:
        record["_r058_exponent_interval"] = exponent_interval
        record["_r058_coverage_interval"] = coverage_interval

    chain_names = {
        chain: [
            str(item["configuration_id"])
            for item in protocol["heldout_configurations"]
            if item["chain"] == chain
        ]
        for chain in CHAIN_ORDER
    }
    lineages: list[dict[str, Any]] = []
    lineage_nodes_by_chain: dict[str, list[set[int]]] = {}
    for chain in CHAIN_ORDER:
        lineage, node_sets = chain_lineage(
            chain,
            chain_names[chain],
            records_by_name,
            args.edge_dir,
        )
        lineages.append(lineage)
        lineage_nodes_by_chain[chain] = node_sets

    bridge_records = [
        symbolic_bridge(
            chain_names[chain][-1],
            lineage_nodes_by_chain[chain][-1],
            records_by_name[chain_names[chain][-1]],
            protocol,
        )
        for chain in CHAIN_ORDER
    ]
    final_nodes = {
        chain: lineage_nodes_by_chain[chain][-1] for chain in CHAIN_ORDER
    }
    final_records = {
        chain: records_by_name[chain_names[chain][-1]]
        for chain in CHAIN_ORDER
    }
    overlaps = finest_phase_overlaps(final_nodes, final_records)

    integrity_rows = [heldout_integrity(record) for record in heldouts]
    refinement_checks = [
        {
            "parent": row["parent_configuration"],
            "child": row["child_configuration"],
            "checks": {
                "exact_nested": row["exact_nested_edge_vectors_pass"],
                "active_lift": row["active_lift_missing_child_node_count"] == 0,
                "positive_complete_projection": row["true_positive"][
                    "complete_projection_equals_parent_pass"
                ]
                and row["true_positive"][
                    "complete_backward_projection_equals_parent_pass"
                ],
                "positive_matched_projection": row["true_positive"][
                    "matched_support_projection_equals_parent_active_graph_pass"
                ]
                and row["true_positive"][
                    "matched_support_backward_projection_equals_parent_active_graph_pass"
                ],
                "positive_nontrivial_descendant": row["true_positive"][
                    "nontrivial_descendant_exists_pass"
                ],
            },
        }
        for row in refinement_records
    ]
    for row in refinement_checks:
        row["pass"] = all(row["checks"].values())

    decisions = {
        "protocol_and_preflight_pass": integrity["pass"] and preflight["pass"],
        "development_anchor_pass": anchor_check["pass"],
        "serial_parallel_replay_pass": replay["all_hashes_match"],
        "all_nine_integrity_pass": all(row["pass"] for row in integrity_rows),
        "all_six_pairwise_refinements_pass": all(
            row["pass"] for row in refinement_checks
        ),
        "all_three_lineages_pass": all(row["pass"] for row in lineages),
        "all_three_symbolic_bridges_pass": all(
            row["pass"] for row in bridge_records
        ),
    }
    decisions["all_frozen_graph_gates_pass"] = all(decisions.values())
    decisions["interpretation"] = (
        "R058_FILAMENT_REPLICATION_AND_BRIDGE_PASS"
        if decisions["all_frozen_graph_gates_pass"]
        else "R058_NEGATIVE_OR_PARTIAL_FILAMENT_REPLICATION"
    )

    for record in heldouts:
        record.pop("_r058_exponent_interval", None)
        record.pop("_r058_coverage_interval", None)

    output = {
        "run_id": "R058_HYPERBOLIC_FILAMENT",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_integrity": integrity,
        "preflight": preflight,
        "development_anchor": anchor_check,
        "serial_parallel_replay": replay,
        "records": heldouts,
        "refinements": refinement_records,
        "lineages": lineages,
        "symbolic_bridge": bridge_records,
        "finest_phase_overlaps": overlaps,
        "heldout_integrity_rows": integrity_rows,
        "refinement_gate_rows": refinement_checks,
        "decisions": decisions,
        "scope": (
            "Locked exact true-positive finite-grid lineage replication and "
            "symbolic bridge only; independent from the R058 covering theorem "
            "and not a graph-limit or operator-convergence result."
        ),
    }
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_csv(output_csv, heldouts)
    print(
        json.dumps(
            {
                "json": portable_path(output_json),
                "csv": portable_path(output_csv),
                "edge_dir": portable_path(args.edge_dir),
                "heldout_count": len(heldouts),
                "refinement_count": len(refinement_records),
                "all_frozen_graph_gates_pass": decisions[
                    "all_frozen_graph_gates_pass"
                ],
            },
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
