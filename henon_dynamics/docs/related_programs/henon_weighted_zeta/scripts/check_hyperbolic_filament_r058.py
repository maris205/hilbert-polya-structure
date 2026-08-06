#!/usr/bin/env python3
"""Independent checker for the frozen R058 graph replication.

The checker imports only the previously independent R056 checker primitives.
It imports no R053--R058 producer incidence, SCC, covering, or cone helper.
All nine edge artifacts are loaded without pickle, 32 frozen sources per
configuration are swept against every target cell, all six refinement
projections are rebuilt, and the multilevel positive lineages and symbolic
bridges are reconstructed independently.
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
from typing import Any, Iterable, Mapping, Sequence

import numpy as np
import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import scripts.check_true_image_refinement_r056 as independent  # noqa: E402


PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R058_HYPERBOLIC_FILAMENT_PROTOCOL.json"
)
PROTOCOL_SHA256 = "bdd851ac14fb5cbe89ce4592b4f0e9f6cbe4fa4b76778530a2e19e7e0f1dd6f3"
DEFAULT_INPUT = PROJECT_ROOT / "results" / "hyperbolic_filament_r058.json"
DEFAULT_THEORY = PROJECT_ROOT / "results" / "hyperbolic_covering_r058.json"
DEFAULT_OUTPUT = (
    PROJECT_ROOT
    / "results"
    / "hyperbolic_filament_independent_check_r058.json"
)
CHAIN_ORDER = ("centered", "positive_phase", "negative_phase")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--theory", type=Path, default=DEFAULT_THEORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=12)
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


def fraction_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": fraction_text(value), "float": float(value)}


def load_inputs(
    result_path: Path,
    theory_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    result = json.loads(result_path.read_text(encoding="utf-8"))
    theory = json.loads(theory_path.read_text(encoding="utf-8"))
    checks = {
        "protocol_sha256": independent.sha256_file(PROTOCOL) == PROTOCOL_SHA256,
        "protocol_run_id": protocol.get("run_id") == "R058_HYPERBOLIC_FILAMENT",
        "protocol_status": protocol.get("status")
        == "FROZEN_BEFORE_R058_PRODUCTION",
        "result_run_id": result.get("run_id") == "R058_HYPERBOLIC_FILAMENT",
        "result_protocol_sha256": result.get("protocol_integrity", {}).get(
            "protocol_sha256"
        )
        == PROTOCOL_SHA256,
        "theory_run_id": theory.get("run_id") == "R058_HYPERBOLIC_COVERING",
        "theory_protocol_sha256": theory.get("protocol_integrity", {}).get(
            "protocol_sha256"
        )
        == PROTOCOL_SHA256,
        "record_count": len(result.get("records", [])) == 9,
        "refinement_count": len(result.get("refinements", [])) == 6,
        "lineage_count": len(result.get("lineages", [])) == 3,
    }
    if not all(checks.values()):
        raise SystemExit(f"R058 checker input mismatch: {checks}")
    return protocol, result, theory


def constants(protocol: Mapping[str, Any]) -> independent.Constants:
    return independent.Constants(
        a=Fraction(str(protocol["map"]["a"])),
        radius=Fraction(str(protocol["map"]["ambient_radius"])),
        eta=Fraction(str(protocol["graph_constants"]["eta"])),
        maximum_subdivisions=int(
            protocol["graph_constants"]["maximum_subdivisions"]
        ),
    )


def records_by_name(
    result: Mapping[str, Any],
) -> dict[str, Mapping[str, Any]]:
    return {
        str(record["configuration"]): record
        for record in result["records"]
    }


def load_artifacts(
    protocol: Mapping[str, Any],
    result: Mapping[str, Any],
) -> tuple[dict[str, independent.EdgeArtifact], dict[str, Any]]:
    records = records_by_name(result)
    artifacts: dict[str, independent.EdgeArtifact] = {}
    rows: list[dict[str, Any]] = []
    all_pass = True
    expected_order = [
        str(item["configuration_id"])
        for item in protocol["heldout_configurations"]
    ]
    if list(records) != expected_order:
        raise AssertionError("R058 result record order differs from protocol")
    for item in protocol["heldout_configurations"]:
        name = str(item["configuration_id"])
        grid = int(item["grid"])
        record = records[name]
        path = PROJECT_ROOT / str(record["edge_array_path"])
        hash_pass = independent.sha256_file(path) == record["edge_array_sha256"]
        artifact = independent.load_edge_artifact(path, grid)
        artifacts[name] = artifact
        arrays = artifact.arrays
        decisions = independent.recompute_edge_decisions(arrays)
        positive_forward_pairs = independent.pair_set(
            arrays["true_forward_edges"], positive_only=True
        )
        positive_backward_pairs = independent.pair_set(
            arrays["true_backward_edges"], positive_only=True
        )
        checks = {
            "artifact_sha256": hash_pass,
            "active_node_hash": independent.node_hash(
                int(value) for value in arrays["active_node_ids"]
            )
            == record["active_node_ids_sha256"],
            "k_max": int(np.max(arrays["k_values"]))
            == int(item["pre_freeze_uncapped_k_max"]),
            "cap_inactive": int(np.max(arrays["k_values"]))
            < int(protocol["graph_constants"]["maximum_subdivisions"]),
            "positive_forward_count": len(positive_forward_pairs)
            == int(record["true_forward_positive_edge_count"]),
            "positive_backward_count": len(positive_backward_pairs)
            == int(record["true_backward_positive_edge_count"]),
            "positive_forward_hash": independent._pair_hash(  # noqa: SLF001
                positive_forward_pairs
            )
            == record["true_forward_positive_unlabelled_edge_hash"],
            "positive_backward_hash": independent._pair_hash(  # noqa: SLF001
                positive_backward_pairs
            )
            == record["true_backward_positive_unlabelled_edge_hash"],
            "all_full_array_decisions_zero": decisions[
                "all_decision_set_differences_zero"
            ],
        }
        row_pass = all(checks.values())
        all_pass = all_pass and row_pass
        rows.append(
            {
                "configuration": name,
                "artifact_path": portable_path(path),
                "checks": checks,
                "pass": row_pass,
            }
        )
    return artifacts, {
        "configuration_count": len(rows),
        "rows": rows,
        "pass": all_pass,
    }


def _fixed_source_job(
    job: tuple[str, int, Fraction, int, independent.Constants],
) -> tuple[str, int, dict[str, object]]:
    name, grid, offset, source_id, frozen = job
    edges = independent.make_edges(frozen.radius, grid, offset)
    return name, source_id, independent.brute_force_source(
        edges, source_id, frozen
    )


def fixed_source_sweep(
    protocol: Mapping[str, Any],
    artifacts: Mapping[str, independent.EdgeArtifact],
    workers: int,
) -> dict[str, Any]:
    frozen = constants(protocol)
    jobs: list[tuple[str, int, Fraction, int, independent.Constants]] = []
    expected_sources: dict[str, tuple[int, ...]] = {}
    grids: dict[str, int] = {}
    for item in protocol["heldout_configurations"]:
        name = str(item["configuration_id"])
        grid = int(item["grid"])
        offset = Fraction(str(item["grid_offset"]))
        source_ids = independent.fixed_source_ids(grid, count=32)
        expected_sources[name] = source_ids
        grids[name] = grid
        jobs.extend(
            (name, grid, offset, source_id, frozen)
            for source_id in source_ids
        )
    if workers <= 0:
        raise ValueError("workers must be positive")
    mismatch_by_name: dict[str, dict[str, object] | None] = {
        name: None for name in expected_sources
    }
    completed_by_name = {name: 0 for name in expected_sources}
    worker_count = min(workers, len(jobs))
    with ProcessPoolExecutor(max_workers=worker_count) as executor:
        futures = {
            executor.submit(_fixed_source_job, job): (job[0], job[3])
            for job in jobs
        }
        for total_completed, future in enumerate(as_completed(futures), start=1):
            name, source_id = futures[future]
            _, _, recomputed = future.result()
            completed_by_name[name] += 1
            if mismatch_by_name[name] is None:
                for key in independent.EDGE_ARRAY_KEYS:
                    expected = recomputed[key]
                    observed = independent.labels_for_source(
                        artifacts[name].arrays[key], source_id
                    )
                    difference = independent._first_map_difference(  # noqa: SLF001
                        expected, observed
                    )
                    if difference is not None:
                        mismatch_by_name[name] = {
                            "configuration": name,
                            "source_id": source_id,
                            "array": key,
                            **difference,
                        }
                        break
            if total_completed % 16 == 0 or total_completed == len(jobs):
                print(
                    f"[fixed-source] {total_completed}/{len(jobs)} complete",
                    flush=True,
                )

    rows: list[dict[str, Any]] = []
    total_pairs = 0
    for name, source_ids in expected_sources.items():
        grid = grids[name]
        pair_count = len(source_ids) * grid * grid
        total_pairs += pair_count
        rows.append(
            {
                "configuration": name,
                "source_count": len(source_ids),
                "source_ids": list(source_ids),
                "source_target_pair_count": pair_count,
                "completed_source_count": completed_by_name[name],
                "first_mismatch": mismatch_by_name[name],
                "pass": (
                    completed_by_name[name] == len(source_ids)
                    and mismatch_by_name[name] is None
                ),
            }
        )
    return {
        "workers": worker_count,
        "configuration_count": len(rows),
        "total_source_count": len(jobs),
        "total_source_target_pair_count": total_pairs,
        "rows": rows,
        "pass": all(row["pass"] for row in rows),
    }


def microgrid_checks(protocol: Mapping[str, Any]) -> dict[str, Any]:
    frozen = constants(protocol)
    rows = [
        independent.run_microgrid_sweep(7, Fraction(0), frozen),
        independent.run_microgrid_sweep(8, Fraction(1, 3), frozen),
    ]
    return {
        "rows": rows,
        "total_source_target_pair_count": sum(
            int(row["source_target_pair_count"]) for row in rows
        ),
        "pass": all(bool(row["pass"]) for row in rows),
    }


def adapter_protocol(protocol: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "constants": {
            "a": protocol["map"]["a"],
            "radius": protocol["map"]["ambient_radius"],
            "eta": protocol["graph_constants"]["eta"],
            "maximum_subdivisions": protocol["graph_constants"][
                "maximum_subdivisions"
            ],
        },
        "development_anchors": [],
        "heldout_configurations": [
            {
                "configuration_id": item["configuration_id"],
                "grid": item["grid"],
                "grid_offset": item["grid_offset"],
            }
            for item in protocol["heldout_configurations"]
        ],
        "nested_refinements": [
            {
                "parent_configuration_id": parent,
                "child_configuration_id": child,
            }
            for parent, child in protocol["nested_refinements"]
        ],
    }


def serial_replay_check(
    result: Mapping[str, Any],
    artifacts: Mapping[str, independent.EdgeArtifact],
) -> dict[str, Any]:
    record = records_by_name(result)["n113_dp1_12"]
    serial_path = (
        PROJECT_ROOT
        / "results"
        / "hyperbolic_filament_r058_edges"
        / "n113_dp1_12_serial_replay.npz"
    )
    serial_hash = independent.sha256_file(serial_path)
    serial = independent.load_edge_artifact(serial_path, int(record["grid"]))
    comparison = independent.compare_artifacts(
        artifacts["n113_dp1_12"], serial
    )
    return {
        "serial_path": portable_path(serial_path),
        "serial_sha256": serial_hash,
        "comparison": comparison,
        "reported_replay_pass": result["serial_parallel_replay"][
            "all_hashes_match"
        ],
        "pass": comparison["pass"]
        and result["serial_parallel_replay"]["all_hashes_match"],
    }


def cell_union_area(
    edges: Sequence[Fraction],
    grid: int,
    nodes: Iterable[int],
) -> Fraction:
    area = Fraction(0)
    for node in set(int(value) for value in nodes):
        x_index, y_index = node % grid, node // grid
        area += (edges[x_index + 1] - edges[x_index]) * (
            edges[y_index + 1] - edges[y_index]
        )
    return area


def positive_edges(
    artifact: independent.EdgeArtifact,
) -> set[tuple[int, int, int]]:
    return independent._labelled_edges_from_array(  # noqa: SLF001
        artifact.arrays["true_forward_edges"],
        positive_only=True,
    )


def lineage_checks(
    protocol: Mapping[str, Any],
    result: Mapping[str, Any],
    artifacts: Mapping[str, independent.EdgeArtifact],
) -> tuple[dict[str, Any], dict[str, list[set[int]]]]:
    configs = {
        str(item["configuration_id"]): item
        for item in protocol["heldout_configurations"]
    }
    reported = {
        str(row["chain"]): row for row in result["lineages"]
    }
    nodes_by_chain: dict[str, list[set[int]]] = {}
    rows: list[dict[str, Any]] = []
    all_pass = True
    exponent_interval = protocol["filament_gates"][
        "each_chain_four_x_size_exponent_interval"
    ]
    coverage_interval = protocol["filament_gates"][
        "each_level_descendant_lifted_area_coverage_interval"
    ]
    for chain in CHAIN_ORDER:
        names = [
            str(item["configuration_id"])
            for item in protocol["heldout_configurations"]
            if item["chain"] == chain
        ]
        root_name = names[0]
        root_config = configs[root_name]
        root_grid = int(root_config["grid"])
        root_active = {
            int(value)
            for value in artifacts[root_name].arrays["active_node_ids"]
        }
        root_components = independent._components_from_labelled_edges(  # noqa: SLF001
            independent._induced_labelled_edges(  # noqa: SLF001
                positive_edges(artifacts[root_name]), root_active
            ),
            root_active,
        )
        current = set(root_components[0]) if root_components else set()
        node_levels = [set(current)]
        root_edges = independent.make_edges(
            constants(protocol).radius,
            root_grid,
            Fraction(str(root_config["grid_offset"])),
        )
        sizes = [len(current)]
        areas = [cell_union_area(root_edges, root_grid, current)]
        step_rows: list[dict[str, Any]] = []
        for parent_name, child_name in zip(names, names[1:]):
            parent_grid = int(configs[parent_name]["grid"])
            child_grid = int(configs[child_name]["grid"])
            lifted = independent.lift_parent_nodes(current, parent_grid)
            matched = independent._induced_labelled_edges(  # noqa: SLF001
                positive_edges(artifacts[child_name]), lifted
            )
            components = independent._components_from_labelled_edges(  # noqa: SLF001
                matched, lifted
            )
            descendants = [
                set(component)
                for component in components
                if len(component) > 1
                and independent._project_node_set(  # noqa: SLF001
                    component, parent_grid
                )
                <= current
            ]
            selected = descendants[0] if descendants else set()
            child_edges = independent.make_edges(
                constants(protocol).radius,
                child_grid,
                Fraction(str(configs[child_name]["grid_offset"])),
            )
            lifted_area = cell_union_area(child_edges, child_grid, lifted)
            selected_area = cell_union_area(child_edges, child_grid, selected)
            coverage = (
                selected_area / lifted_area if lifted_area else Fraction(0)
            )
            step_rows.append(
                {
                    "parent": parent_name,
                    "child": child_name,
                    "selected_node_count": len(selected),
                    "selected_node_ids_sha256": independent.node_hash(selected),
                    "selected_area": fraction_payload(selected_area),
                    "coverage": fraction_payload(coverage),
                    "nontrivial": len(selected) > 1,
                }
            )
            current = selected
            node_levels.append(set(current))
            sizes.append(len(current))
            areas.append(selected_area)

        exponent = (
            math.log(sizes[-1] / sizes[0]) / math.log(4)
            if sizes[0] and sizes[-1]
            else float("nan")
        )
        artifact_path = PROJECT_ROOT / reported[chain]["artifact_path"]
        artifact_hash_pass = (
            independent.sha256_file(artifact_path)
            == reported[chain]["artifact_sha256"]
        )
        with np.load(artifact_path, allow_pickle=False) as archive:
            artifact_arrays = [
                set(int(value) for value in archive[f"level{level}_node_ids"])
                for level in range(3)
            ]
        artifact_nodes_pass = all(
            observed == expected
            for observed, expected in zip(artifact_arrays, node_levels, strict=True)
        )
        report_checks = {
            "sizes": sizes == reported[chain]["lineage_sizes"],
            "areas": all(
                fraction_text(area)
                == reported_area["fraction"]
                for area, reported_area in zip(
                    areas, reported[chain]["lineage_areas"], strict=True
                )
            ),
            "exponent": abs(
                exponent - float(reported[chain]["four_x_size_exponent"])
            )
            < 1e-14,
            "step_hashes": all(
                observed["selected_node_ids_sha256"]
                == expected["selected_descendant_node_ids_sha256"]
                for observed, expected in zip(
                    step_rows, reported[chain]["steps"], strict=True
                )
            ),
            "artifact_sha256": artifact_hash_pass,
            "artifact_nodes": artifact_nodes_pass,
            "sizes_increasing": sizes[0] < sizes[1] < sizes[2],
            "areas_decreasing": areas[0] > areas[1] > areas[2],
            "exponent_gate": float(exponent_interval[0])
            <= exponent
            <= float(exponent_interval[1]),
            "coverage_gate": all(
                float(coverage_interval[0])
                <= float(step["coverage"]["float"])
                <= float(coverage_interval[1])
                for step in step_rows
            ),
        }
        row_pass = all(report_checks.values())
        all_pass = all_pass and row_pass
        rows.append(
            {
                "chain": chain,
                "configurations": names,
                "sizes": sizes,
                "areas": [fraction_payload(area) for area in areas],
                "four_x_size_exponent": exponent,
                "steps": step_rows,
                "checks": report_checks,
                "pass": row_pass,
            }
        )
        nodes_by_chain[chain] = node_levels
    return {
        "rows": rows,
        "pass": all_pass,
    }, nodes_by_chain


def positive_overlap(
    first: tuple[Fraction, Fraction],
    second: tuple[Fraction, Fraction],
) -> bool:
    return max(first[0], second[0]) < min(first[1], second[1])


def symbolic_bridge_checks(
    protocol: Mapping[str, Any],
    result: Mapping[str, Any],
    artifacts: Mapping[str, independent.EdgeArtifact],
    lineage_nodes: Mapping[str, list[set[int]]],
) -> dict[str, Any]:
    configs = {
        str(item["configuration_id"]): item
        for item in protocol["heldout_configurations"]
    }
    reported = {
        str(row["configuration"]): row for row in result["symbolic_bridge"]
    }
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
    allowed = {
        tuple(edge) for edge in protocol["symbolic_graph"]["allowed_edges"]
    }
    rows: list[dict[str, Any]] = []
    all_pass = True
    for chain in CHAIN_ORDER:
        name = [
            str(item["configuration_id"])
            for item in protocol["heldout_configurations"]
            if item["chain"] == chain
        ][-1]
        grid = int(configs[name]["grid"])
        edges = independent.make_edges(
            constants(protocol).radius,
            grid,
            Fraction(str(configs[name]["grid_offset"])),
        )
        nodes = lineage_nodes[chain][-1]
        memberships: dict[int, set[str]] = {}
        for node in nodes:
            x_index, y_index = node % grid, node // grid
            cell_x = edges[x_index], edges[x_index + 1]
            cell_y = edges[y_index], edges[y_index + 1]
            memberships[node] = {
                state
                for state, (state_x, state_y) in state_intervals.items()
                if positive_overlap(cell_x, state_x)
                and positive_overlap(cell_y, state_y)
            }
        state_counts = {
            state: sum(state in member for member in memberships.values())
            for state in h_sets["state_order"]
        }
        matched = independent._induced_labelled_edges(  # noqa: SLF001
            positive_edges(artifacts[name]), nodes
        )
        observed: set[tuple[str, str]] = set()
        for source, target, _ in matched:
            for source_state in memberships[source]:
                for target_state in memberships[target]:
                    observed.add((source_state, target_state))
        missing = sorted(allowed - observed)
        extra = sorted(observed - allowed)
        report = reported[name]
        checks = {
            "state_counts": state_counts == report["state_cell_counts"],
            "observed_transitions": [
                list(edge) for edge in sorted(observed)
            ]
            == report["observed_state_transitions"],
            "all_states_nonempty": all(count > 0 for count in state_counts.values()),
            "all_allowed_present": not missing,
            "forbidden_absent": not extra,
        }
        row_pass = all(checks.values())
        all_pass = all_pass and row_pass
        rows.append(
            {
                "configuration": name,
                "state_counts": state_counts,
                "observed_transitions": [
                    list(edge) for edge in sorted(observed)
                ],
                "missing": [list(edge) for edge in missing],
                "extra": [list(edge) for edge in extra],
                "checks": checks,
                "pass": row_pass,
            }
        )
    return {"rows": rows, "pass": all_pass}


def theory_checks(
    protocol: Mapping[str, Any],
    theory: Mapping[str, Any],
) -> dict[str, Any]:
    states = list(protocol["h_sets"]["state_order"])
    allowed = {
        tuple(edge) for edge in protocol["symbolic_graph"]["allowed_edges"]
    }
    matrix = sp.Matrix(
        [
            [int((source, target) in allowed) for target in states]
            for source in states
        ]
    )
    variable = sp.symbols("lambda")
    characteristic = sp.factor(matrix.charpoly(variable).as_expr())
    expected = (variable**2 - variable - 1) * (variable**2 + 1)
    x_half = Fraction(protocol["cone"]["x_half_width"])
    y_half = Fraction(protocol["cone"]["y_half_width"])
    kappa = Fraction(protocol["cone"]["kappa"])
    forward_denominator = Fraction(4) - (y_half / x_half) * kappa
    forward_slope = (x_half / y_half) / forward_denominator
    backward_denominator = Fraction(15, 4) - (x_half / y_half) * kappa
    backward_slope = (y_half / x_half) / backward_denominator
    integer_matrix = [
        [int(value) for value in row]
        for row in matrix.tolist()
    ]
    checks = {
        "matrix": integer_matrix
        == protocol["symbolic_graph"]["adjacency_matrix"],
        "characteristic": sp.expand(characteristic - expected) == 0,
        "forward_slope": fraction_text(forward_slope)
        == protocol["cone"]["forward_unstable_slope_upper_bound"],
        "backward_slope": fraction_text(backward_slope)
        == protocol["cone"]["backward_stable_slope_upper_bound"],
        "forward_strict": forward_slope < kappa,
        "backward_strict": backward_slope < kappa,
        "producer_local_exact": theory["decisions"][
            "local_exact_certificate_pass"
        ],
        "theorem_audit": theory["decisions"][
            "bi_infinite_itinerary_realization_theorem_audit_pass"
        ],
        "full_claim": theory["decisions"]["full_primary_claim_enabled"],
        "entropy_claim": theory["decisions"]["entropy_claim_enabled"],
    }
    return {
        "adjacency_matrix": integer_matrix,
        "characteristic_polynomial": str(characteristic),
        "forward_slope": fraction_text(forward_slope),
        "backward_slope": fraction_text(backward_slope),
        "checks": checks,
        "pass": all(checks.values()),
    }


def main() -> None:
    args = parse_args()
    protocol, result, theory = load_inputs(args.input, args.theory)
    artifacts, artifact_audit = load_artifacts(protocol, result)
    microgrids = microgrid_checks(protocol)
    print("[microgrid] two complete sweeps passed", flush=True)
    fixed_sources = fixed_source_sweep(
        protocol, artifacts, workers=args.workers
    )
    refinements = independent.check_refinement_projections(
        result,
        adapter_protocol(protocol),
        artifacts,
    )
    for pair in refinements["pairs"]:
        pair["refinement_artifact"] = portable_path(
            Path(pair["refinement_artifact"])
        )
    print("[refinement] six independent projections complete", flush=True)
    replay = serial_replay_check(result, artifacts)
    lineages, lineage_nodes = lineage_checks(protocol, result, artifacts)
    bridges = symbolic_bridge_checks(
        protocol, result, artifacts, lineage_nodes
    )
    theory_audit = theory_checks(protocol, theory)

    checks = {
        "artifact_audit": artifact_audit["pass"],
        "microgrids": microgrids["pass"],
        "fixed_sources": fixed_sources["pass"],
        "refinements": refinements["pass"],
        "serial_replay": replay["pass"],
        "lineages": lineages["pass"],
        "symbolic_bridges": bridges["pass"],
        "theory": theory_audit["pass"],
        "producer_reported_all_graph_gates": result["decisions"][
            "all_frozen_graph_gates_pass"
        ],
    }
    output = {
        "run_id": "R058_HYPERBOLIC_FILAMENT_INDEPENDENT_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable_path(PROTOCOL),
        "protocol_sha256": PROTOCOL_SHA256,
        "input_path": portable_path(args.input),
        "input_sha256": independent.sha256_file(args.input),
        "theory_path": portable_path(args.theory),
        "theory_sha256": independent.sha256_file(args.theory),
        "checker_imports_producer_incidence_scc_covering_or_cone_helpers": False,
        "artifact_audit": artifact_audit,
        "microgrid_checks": microgrids,
        "fixed_source_checks": fixed_sources,
        "refinement_checks": refinements,
        "serial_replay": replay,
        "lineage_checks": lineages,
        "symbolic_bridge_checks": bridges,
        "theory_checks": theory_audit,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scope": (
            "Independent exact finite-artifact and arithmetic replay. The "
            "checker validates the theorem inputs but does not replace the "
            "separate covering-chain theorem proof."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": portable_path(args.output),
                "fixed_source_target_pairs": fixed_sources[
                    "total_source_target_pair_count"
                ],
                "all_checks_pass": output["all_checks_pass"],
            },
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
