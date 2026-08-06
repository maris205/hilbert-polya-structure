#!/usr/bin/env python3
"""Run the frozen R056 held-out true-image graph refinement audit.

The production geometry is exact over :class:`fractions.Fraction`.  NumPy is
used only to persist canonical integer edge arrays and to perform finite set
bookkeeping after the exact edge decisions have been made.

R056 remains an exact *finite cell-incidence* audit.  It does not certify an
invariant set, Markov partition, covering relation, graph limit, or operator
convergence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_exact_closed_cover import (  # noqa: E402
    A_VALUE,
    ETA,
    MAX_SUBDIVISIONS,
    RADIUS,
    _direction_metrics,
    exact_edge_vector,
    exact_slab_bounds,
    fraction_text,
    rectangle_target_classes,
    uncapped_adaptive_subdivisions_exact,
)
from scripts.audit_outer_graph_r054 import (  # noqa: E402
    graph_stats,
    node_hash,
    strongly_connected_components,
)
from scripts.audit_true_image_graph_r055 import (  # noqa: E402
    closed_target_indices,
    edge_hash,
    forward_image_hull,
    forward_true_class,
    inverse_image_hull,
    inverse_true_class,
    mutual_adjacency,
    transpose_match,
    unlabelled_edge_hash,
)


PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R056_TRUE_IMAGE_REFINEMENT_PROTOCOL.json"
)
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "results"
DEFAULT_EDGE_DIR = DEFAULT_OUTPUT_DIR / "true_image_refinement_r056_edges"
AREA_BOUND = Fraction(5, 4)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="true_image_refinement_r056")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--edge-dir", type=Path, default=DEFAULT_EDGE_DIR)
    parser.add_argument(
        "--workers",
        type=int,
        default=6,
        help="Configuration-level processes for each locked batch.",
    )
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def fraction_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": fraction_text(value), "float": float(value)}


def _fraction(value: object) -> Fraction:
    return Fraction(str(value))


def load_and_validate_protocol() -> dict[str, Any]:
    payload = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    constants = payload.get("constants", {})
    anchors = payload.get("development_anchors", [])
    heldouts = payload.get("heldout_configurations", [])
    refinements = payload.get("nested_refinements", [])
    checks = {
        "run_id": payload.get("run_id") == "R056_TRUE_IMAGE_REFINEMENT",
        "status": payload.get("status") == "FROZEN_BEFORE_HELDOUT_PRODUCTION",
        "a": _fraction(constants.get("a")) == A_VALUE,
        "radius": _fraction(constants.get("radius")) == RADIUS,
        "eta": _fraction(constants.get("eta")) == ETA,
        "maximum_subdivisions": int(constants.get("maximum_subdivisions", -1))
        == MAX_SUBDIVISIONS,
        "anchor_count": len(anchors) == 4,
        "heldout_count": len(heldouts) == 6,
        "refinement_count": len(refinements) == 3,
        "anchor_order": [item.get("configuration_id") for item in anchors]
        == ["n96_d0", "n160_d0", "n160_dm1q", "n160_dp1q"],
        "heldout_order": [item.get("configuration_id") for item in heldouts]
        == [
            "n127_d0",
            "n192_d0",
            "n254_d0",
            "n320_d0",
            "n254_dm1_3",
            "n254_dp1_3",
        ],
    }
    if not all(checks.values()):
        raise SystemExit(f"R056 code/protocol mismatch: {checks}")
    return payload


def validate_parent_artifacts(protocol: dict[str, Any]) -> dict[str, str]:
    observed: dict[str, str] = {}
    mismatches: dict[str, dict[str, str]] = {}
    for item in protocol["parent_artifacts"]:
        path = PROJECT_ROOT / str(item["path"])
        actual = sha256_file(path)
        expected = str(item["sha256"])
        role = str(item["role"])
        observed[role] = actual
        if actual != expected:
            mismatches[role] = {"expected": expected, "actual": actual}
    if mismatches:
        raise SystemExit(f"R056 immutable parent artifact mismatch: {mismatches}")
    return observed


def configuration_tuple(item: dict[str, Any], evidence_role: str) -> dict[str, Any]:
    return {
        "configuration": str(item["configuration_id"]),
        "grid": int(item["grid"]),
        "offset": _fraction(item["grid_offset"]),
        "evidence_role": evidence_role,
        "protocol_role": str(item["role"]),
        "pre_freeze_uncapped_k_max": item.get("pre_freeze_uncapped_k_max"),
    }


def adjacency_to_packed_edges(
    adjacency: Sequence[set[int]], positive: Sequence[set[int]]
) -> np.ndarray:
    count = sum(len(targets) for targets in adjacency)
    packed = np.empty((count, 3), dtype=np.int64)
    position = 0
    for source, targets in enumerate(adjacency):
        positive_targets = positive[source]
        for target in sorted(targets):
            packed[position] = (source, target, int(target in positive_targets))
            position += 1
    return packed


def packed_edge_hash(packed: np.ndarray, direction: str) -> str:
    records = (
        (int(source), int(target), "P" if int(positive) else "T")
        for source, target, positive in packed
    )
    return edge_hash(records, direction)


def packed_unlabelled_hash(packed: np.ndarray, *, positive_only: bool = False) -> str:
    digest = hashlib.sha256()
    for source, target, positive in packed:
        if positive_only and not int(positive):
            continue
        digest.update(f"{int(source)},{int(target)}\n".encode("ascii"))
    return digest.hexdigest()


def save_npz_atomic(path: Path, **arrays: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".tmp-{os.getpid()}.npz")
    np.savez_compressed(temporary, **arrays)
    os.replace(temporary, path)


def cell_area(edges: Sequence[Fraction], grid: int, node: int) -> Fraction:
    x_index = node % grid
    y_index = node // grid
    return (edges[x_index + 1] - edges[x_index]) * (
        edges[y_index + 1] - edges[y_index]
    )


def node_union_area(
    edges: Sequence[Fraction], grid: int, nodes: Iterable[int]
) -> Fraction:
    return sum((cell_area(edges, grid, int(node)) for node in set(nodes)), Fraction(0))


def canonical_global_components(
    adjacency: Sequence[set[int]], active: set[int]
) -> list[list[int]]:
    active_ids = sorted(active)
    local_index = {node: index for index, node in enumerate(active_ids)}
    restricted = [
        {local_index[target] for target in adjacency[node] if target in local_index}
        for node in active_ids
    ]
    components = strongly_connected_components(restricted)
    global_components = [
        sorted(active_ids[local] for local in component) for component in components
    ]
    global_components.sort(key=lambda nodes: (-len(nodes), tuple(nodes)))
    return global_components


def exact_graph_stats(
    adjacency: list[set[int]], active: set[int], edges: Sequence[Fraction], grid: int
) -> tuple[dict[str, object], np.ndarray]:
    stats = graph_stats(adjacency, active)
    components = canonical_global_components(adjacency, active)
    multi_node = [component for component in components if len(component) > 1]
    singleton_self_loop = [
        component
        for component in components
        if len(component) == 1 and component[0] in adjacency[component[0]]
    ]
    recurrent_multi_nodes = sorted(
        {node for component in multi_node for node in component}
    )
    active_area = node_union_area(edges, grid, active)
    largest_ids = [int(node) for node in stats["largest_scc_node_ids"]]
    largest_area = node_union_area(edges, grid, largest_ids)
    recurrent_area = node_union_area(edges, grid, recurrent_multi_nodes)
    full_box_area = (2 * RADIUS) ** 2
    stats.update(
        {
            "multi_node_scc_count": len(multi_node),
            "multi_node_recurrent_node_count": len(recurrent_multi_nodes),
            "singleton_self_loop_scc_count": len(singleton_self_loop),
            "multi_node_scc_exists": bool(multi_node),
            "multi_node_recurrent_node_ids_sha256": node_hash(recurrent_multi_nodes),
            "active_union_area": fraction_payload(active_area),
            "largest_scc_union_area": fraction_payload(largest_area),
            "multi_node_recurrent_union_area": fraction_payload(recurrent_area),
            "active_area_fraction_of_box": fraction_payload(active_area / full_box_area),
            "largest_scc_area_fraction_of_active": fraction_payload(
                largest_area / active_area if active_area else Fraction(0)
            ),
            "largest_scc_area_fraction_of_box": fraction_payload(
                largest_area / full_box_area
            ),
            "multi_node_recurrent_area_fraction_of_active": fraction_payload(
                recurrent_area / active_area if active_area else Fraction(0)
            ),
            "multi_node_recurrent_area_fraction_of_box": fraction_payload(
                recurrent_area / full_box_area
            ),
            "active_induced_mean_out_degree": (
                int(stats["induced_edge_count"]) / len(active) if active else 0.0
            ),
        }
    )
    return stats, np.asarray(recurrent_multi_nodes, dtype=np.int64)


def analytic_active_from_hulls(
    edges: Sequence[Fraction], grid: int
) -> set[int]:
    active: set[int] = set()
    lower_box, upper_box = edges[0], edges[-1]
    for source_y_index in range(grid):
        source_y = (edges[source_y_index], edges[source_y_index + 1])
        for source_x_index in range(grid):
            source_x = (edges[source_x_index], edges[source_x_index + 1])
            forward = forward_image_hull(source_x, source_y)
            backward = inverse_image_hull(source_x, source_y)
            forward_inside = (
                forward[0] >= lower_box
                and forward[1] <= upper_box
                and forward[2] >= lower_box
                and forward[3] <= upper_box
            )
            backward_inside = (
                backward[0] >= lower_box
                and backward[1] <= upper_box
                and backward[2] >= lower_box
                and backward[3] <= upper_box
            )
            if forward_inside and backward_inside:
                active.add(source_y_index * grid + source_x_index)
    return active


def _interval_payload(interval: tuple[Fraction, Fraction]) -> list[str]:
    return [fraction_text(interval[0]), fraction_text(interval[1])]


def mismatch_diagnostic(
    *,
    mismatch_class: str,
    direction: str,
    source_id: int,
    target_id: int,
    grid: int,
    edges: Sequence[Fraction],
    k_values: Sequence[int],
    true_adjacency: Sequence[set[int]],
    true_positive: Sequence[set[int]],
    outer_adjacency: Sequence[set[int]],
    outer_positive: Sequence[set[int]],
) -> dict[str, object]:
    sx, sy = source_id % grid, source_id // grid
    tx, ty = target_id % grid, target_id // grid
    source_x = (edges[sx], edges[sx + 1])
    source_y = (edges[sy], edges[sy + 1])
    target_x = (edges[tx], edges[tx + 1])
    target_y = (edges[ty], edges[ty + 1])
    if direction == "F":
        parameter = source_x
        target_parameter = target_y
        coefficient = (1 - target_x[1] - source_y[1], 1 - target_x[0] - source_y[0])
        adaptive_k = k_values[sx]
        inverse = False
    else:
        parameter = source_y
        target_parameter = target_x
        coefficient = (1 - target_y[1] - source_x[1], 1 - target_y[0] - source_x[0])
        adaptive_k = k_values[sy]
        inverse = True
    restricted = (max(parameter[0], target_parameter[0]), min(parameter[1], target_parameter[1]))
    if restricted[1] >= restricted[0]:
        candidates = [restricted[0] ** 2, restricted[1] ** 2]
        if restricted[0] <= 0 <= restricted[1]:
            candidates.append(Fraction(0))
        quadratic = (A_VALUE * min(candidates), A_VALUE * max(candidates))
    else:
        quadratic = None
    relevant_slabs: list[dict[str, object]] = []
    for slab_index in range(adaptive_k):
        bounds = exact_slab_bounds(source_x, source_y, slab_index, adaptive_k, inverse)
        classes = rectangle_target_classes(edges, bounds)
        if target_id in classes:
            relevant_slabs.append(
                {
                    "slab_index": slab_index,
                    "bounds": [fraction_text(value) for value in bounds],
                    "positive": bool(classes[target_id]),
                }
            )
    return {
        "mismatch_class": mismatch_class,
        "direction": direction,
        "source_id": source_id,
        "target_id": target_id,
        "exact_source_bounds": {
            "x": _interval_payload(source_x),
            "y": _interval_payload(source_y),
        },
        "exact_target_bounds": {
            "x": _interval_payload(target_x),
            "y": _interval_payload(target_y),
        },
        "adaptive_k": adaptive_k,
        "relevant_outer_slabs": relevant_slabs,
        "restricted_parameter_interval": (
            _interval_payload(restricted) if restricted[1] >= restricted[0] else None
        ),
        "quadratic_range": _interval_payload(quadratic) if quadratic else None,
        "coefficient_interval": _interval_payload(coefficient),
        "positive_or_touch_label": {
            "true": (
                "P" if target_id in true_positive[source_id] else "T"
            )
            if target_id in true_adjacency[source_id]
            else None,
            "outer": (
                "P" if target_id in outer_positive[source_id] else "T"
            )
            if target_id in outer_adjacency[source_id]
            else None,
        },
    }


def first_symmetric_difference(
    left: Sequence[set[int]], right: Sequence[set[int]]
) -> tuple[int, int] | None:
    for source in range(len(left)):
        difference = left[source] ^ right[source]
        if difference:
            return source, min(difference)
    return None


def build_configuration(job: dict[str, Any]) -> dict[str, Any]:
    name = str(job["configuration"])
    grid = int(job["grid"])
    offset = Fraction(job["offset"])
    edge_path = Path(str(job["edge_path"]))
    edges = exact_edge_vector(RADIUS, grid, offset)
    widths = [upper - lower for lower, upper in zip(edges, edges[1:])]
    minimum_width = min(widths)
    uncapped_k = [
        uncapped_adaptive_subdivisions_exact(edges[index], edges[index + 1], minimum_width)
        for index in range(grid)
    ]
    if max(uncapped_k) >= MAX_SUBDIVISIONS:
        raise AssertionError(
            f"R056 {name}: uncapped K={max(uncapped_k)} reaches frozen cap"
        )
    k_values = uncapped_k

    total = grid * grid
    outer_forward: list[set[int]] = [set() for _ in range(total)]
    outer_backward: list[set[int]] = [set() for _ in range(total)]
    outer_forward_positive: list[set[int]] = [set() for _ in range(total)]
    outer_backward_positive: list[set[int]] = [set() for _ in range(total)]
    true_forward: list[set[int]] = [set() for _ in range(total)]
    true_backward: list[set[int]] = [set() for _ in range(total)]
    true_forward_positive: list[set[int]] = [set() for _ in range(total)]
    true_backward_positive: list[set[int]] = [set() for _ in range(total)]
    forward_candidates: list[set[int]] = [set() for _ in range(total)]
    backward_candidates: list[set[int]] = [set() for _ in range(total)]
    active: set[int] = set()
    local_variation_pass = True
    maximum_area_ratio = Fraction(0)
    forward_candidate_count = 0
    backward_candidate_count = 0

    for source_y_index in range(grid):
        source_y = (edges[source_y_index], edges[source_y_index + 1])
        for source_x_index in range(grid):
            source_x = (edges[source_x_index], edges[source_x_index + 1])
            source_id = source_y_index * grid + source_x_index
            forward_outer = _direction_metrics(
                edges,
                source_x,
                source_y,
                k_values[source_x_index],
                minimum_width,
                False,
            )
            backward_outer = _direction_metrics(
                edges,
                source_x,
                source_y,
                k_values[source_y_index],
                minimum_width,
                True,
            )
            local_variation_pass = local_variation_pass and bool(
                forward_outer["local_bound_pass"]
            ) and bool(backward_outer["local_bound_pass"])
            maximum_area_ratio = max(
                maximum_area_ratio,
                Fraction(forward_outer["area_ratio"]),
                Fraction(backward_outer["area_ratio"]),
            )
            outer_forward[source_id] = set(forward_outer["target_classes"])
            outer_backward[source_id] = set(backward_outer["target_classes"])
            outer_forward_positive[source_id] = {
                target
                for target, positive in forward_outer["target_classes"].items()
                if positive
            }
            outer_backward_positive[source_id] = {
                target
                for target, positive in backward_outer["target_classes"].items()
                if positive
            }
            if forward_outer["inside"] and backward_outer["inside"]:
                active.add(source_id)

            forward_hull = forward_image_hull(source_x, source_y)
            target_x_indices = closed_target_indices(edges, forward_hull[0], forward_hull[1])
            target_y_indices = closed_target_indices(edges, forward_hull[2], forward_hull[3])
            forward_candidate_count += len(target_x_indices) * len(target_y_indices)
            for target_y_index in target_y_indices:
                target_y = (edges[target_y_index], edges[target_y_index + 1])
                for target_x_index in target_x_indices:
                    target_x = (edges[target_x_index], edges[target_x_index + 1])
                    target_id = target_y_index * grid + target_x_index
                    forward_candidates[source_id].add(target_id)
                    positive = forward_true_class(source_x, source_y, target_x, target_y)
                    if positive is not None:
                        true_forward[source_id].add(target_id)
                        if positive:
                            true_forward_positive[source_id].add(target_id)

            inverse_hull = inverse_image_hull(source_x, source_y)
            target_x_indices = closed_target_indices(edges, inverse_hull[0], inverse_hull[1])
            target_y_indices = closed_target_indices(edges, inverse_hull[2], inverse_hull[3])
            backward_candidate_count += len(target_x_indices) * len(target_y_indices)
            for target_y_index in target_y_indices:
                target_y = (edges[target_y_index], edges[target_y_index + 1])
                for target_x_index in target_x_indices:
                    target_x = (edges[target_x_index], edges[target_x_index + 1])
                    target_id = target_y_index * grid + target_x_index
                    backward_candidates[source_id].add(target_id)
                    positive = inverse_true_class(source_x, source_y, target_x, target_y)
                    if positive is not None:
                        true_backward[source_id].add(target_id)
                        if positive:
                            true_backward_positive[source_id].add(target_id)

    analytic_active = analytic_active_from_hulls(edges, grid)
    outer_mutual_forward = mutual_adjacency(outer_forward, outer_backward)
    outer_mutual_backward = mutual_adjacency(outer_backward, outer_forward)
    true_forward_packed = adjacency_to_packed_edges(true_forward, true_forward_positive)
    true_backward_packed = adjacency_to_packed_edges(true_backward, true_backward_positive)
    outer_forward_packed = adjacency_to_packed_edges(outer_forward, outer_forward_positive)
    outer_backward_packed = adjacency_to_packed_edges(outer_backward, outer_backward_positive)

    true_closed_stats, true_closed_recurrent = exact_graph_stats(
        true_forward, active, edges, grid
    )
    true_positive_stats, true_positive_recurrent = exact_graph_stats(
        true_forward_positive, active, edges, grid
    )

    save_npz_atomic(
        edge_path,
        true_forward_edges=true_forward_packed,
        true_backward_edges=true_backward_packed,
        outer_forward_edges=outer_forward_packed,
        outer_backward_edges=outer_backward_packed,
        active_node_ids=np.asarray(sorted(active), dtype=np.int64),
        analytic_active_node_ids=np.asarray(sorted(analytic_active), dtype=np.int64),
        k_values=np.asarray(k_values, dtype=np.int64),
        true_closed_recurrent_multi_node_ids=true_closed_recurrent,
        true_positive_recurrent_multi_node_ids=true_positive_recurrent,
    )

    true_subset_outer = all(
        true_forward[source] <= outer_forward[source]
        and true_backward[source] <= outer_backward[source]
        for source in range(total)
    )
    true_positive_subset = all(
        true_forward_positive[source] <= outer_forward_positive[source]
        and true_backward_positive[source] <= outer_backward_positive[source]
        for source in range(total)
    )
    candidate_contains = all(
        true_forward[source] <= forward_candidates[source]
        and true_backward[source] <= backward_candidates[source]
        for source in range(total)
    )
    forward_closed_difference = first_symmetric_difference(true_forward, outer_mutual_forward)
    backward_closed_difference = first_symmetric_difference(true_backward, outer_mutual_backward)
    forward_positive_difference = first_symmetric_difference(
        true_forward_positive, outer_forward_positive
    )
    backward_positive_difference = first_symmetric_difference(
        true_backward_positive, outer_backward_positive
    )
    mismatches: list[dict[str, object]] = []
    mismatch_specs = (
        (
            "true_closed_vs_mutual_outer",
            "F",
            forward_closed_difference,
            true_forward,
            true_forward_positive,
            outer_mutual_forward,
            outer_forward_positive,
        ),
        (
            "true_closed_vs_mutual_outer",
            "B",
            backward_closed_difference,
            true_backward,
            true_backward_positive,
            outer_mutual_backward,
            outer_backward_positive,
        ),
        (
            "true_positive_vs_outer_positive",
            "F",
            forward_positive_difference,
            true_forward_positive,
            true_forward_positive,
            outer_forward_positive,
            outer_forward_positive,
        ),
        (
            "true_positive_vs_outer_positive",
            "B",
            backward_positive_difference,
            true_backward_positive,
            true_backward_positive,
            outer_backward_positive,
            outer_backward_positive,
        ),
    )
    for mismatch_class, direction, difference, true_graph, true_positive_graph, outer_graph, outer_positive_graph in mismatch_specs:
        if difference is not None:
            source_id, target_id = difference
            mismatches.append(
                mismatch_diagnostic(
                    mismatch_class=mismatch_class,
                    direction=direction,
                    source_id=source_id,
                    target_id=target_id,
                    grid=grid,
                    edges=edges,
                    k_values=k_values,
                    true_adjacency=true_graph,
                    true_positive=true_positive_graph,
                    outer_adjacency=outer_graph,
                    outer_positive=outer_positive_graph,
                )
            )

    record: dict[str, Any] = {
        "configuration": name,
        "evidence_role": str(job["evidence_role"]),
        "protocol_role": str(job["protocol_role"]),
        "grid": grid,
        "grid_offset_fraction": fraction_text(offset),
        "state_count": total,
        "edge_array_path": portable_path(edge_path),
        "edge_array_sha256": sha256_file(edge_path),
        "edge_array_schema": {
            "edge_columns": ["source_id", "target_id", "positive_flag"],
            "edge_dtype": "int64",
            "node_dtype": "int64",
            "allow_pickle": False,
        },
        "exact_edge_integrity_pass": (
            edges[0] == -RADIUS
            and edges[-1] == RADIUS
            and all(upper > lower for lower, upper in zip(edges, edges[1:]))
        ),
        "uncapped_k_max": max(k_values),
        "uncapped_k_min": min(k_values),
        "cap_active_count": sum(value >= MAX_SUBDIVISIONS for value in k_values),
        "pre_freeze_uncapped_k_max_match": (
            job.get("pre_freeze_uncapped_k_max") is None
            or max(k_values) == int(job["pre_freeze_uncapped_k_max"])
        ),
        "local_variation_bound_pass": local_variation_pass,
        "maximum_outer_area_ratio": fraction_payload(maximum_area_ratio),
        "outer_area_ratio_bound_pass": maximum_area_ratio <= AREA_BOUND,
        "forward_candidate_pair_count": forward_candidate_count,
        "backward_candidate_pair_count": backward_candidate_count,
        "candidate_hull_contains_true_pass": candidate_contains,
        "active_node_count": len(active),
        "active_node_ids_sha256": node_hash(active),
        "analytic_active_node_count": len(analytic_active),
        "analytic_active_node_ids_sha256": node_hash(analytic_active),
        "slab_active_equals_analytic_hull_active_pass": active == analytic_active,
        "true_forward_closed_edge_count": len(true_forward_packed),
        "true_backward_closed_edge_count": len(true_backward_packed),
        "true_forward_positive_edge_count": int(true_forward_packed[:, 2].sum()),
        "true_backward_positive_edge_count": int(true_backward_packed[:, 2].sum()),
        "outer_forward_closed_edge_count": len(outer_forward_packed),
        "outer_backward_closed_edge_count": len(outer_backward_packed),
        "outer_forward_positive_edge_count": int(outer_forward_packed[:, 2].sum()),
        "outer_backward_positive_edge_count": int(outer_backward_packed[:, 2].sum()),
        "outer_mutual_forward_edge_count": sum(len(row) for row in outer_mutual_forward),
        "outer_mutual_backward_edge_count": sum(len(row) for row in outer_mutual_backward),
        "true_forward_labelled_edge_hash": packed_edge_hash(true_forward_packed, "F"),
        "true_backward_labelled_edge_hash": packed_edge_hash(true_backward_packed, "B"),
        "outer_forward_labelled_edge_hash": packed_edge_hash(outer_forward_packed, "F"),
        "outer_backward_labelled_edge_hash": packed_edge_hash(outer_backward_packed, "B"),
        "true_forward_unlabelled_edge_hash": packed_unlabelled_hash(true_forward_packed),
        "true_backward_unlabelled_edge_hash": packed_unlabelled_hash(true_backward_packed),
        "true_forward_positive_unlabelled_edge_hash": packed_unlabelled_hash(
            true_forward_packed, positive_only=True
        ),
        "true_backward_positive_unlabelled_edge_hash": packed_unlabelled_hash(
            true_backward_packed, positive_only=True
        ),
        "outer_forward_unlabelled_edge_hash": packed_unlabelled_hash(outer_forward_packed),
        "outer_backward_unlabelled_edge_hash": packed_unlabelled_hash(outer_backward_packed),
        "outer_forward_positive_unlabelled_edge_hash": packed_unlabelled_hash(
            outer_forward_packed, positive_only=True
        ),
        "outer_backward_positive_unlabelled_edge_hash": packed_unlabelled_hash(
            outer_backward_packed, positive_only=True
        ),
        "outer_mutual_forward_unlabelled_edge_hash": unlabelled_edge_hash(outer_mutual_forward),
        "outer_mutual_backward_unlabelled_edge_hash": unlabelled_edge_hash(outer_mutual_backward),
        "true_edge_subset_outer_pass": true_subset_outer,
        "true_positive_subset_outer_positive_pass": true_positive_subset,
        "true_forward_inverse_labelled_transpose_pass": transpose_match(
            true_forward,
            true_backward,
            true_forward_positive,
            true_backward_positive,
        ),
        "true_closed_equals_mutual_outer_forward_pass": forward_closed_difference is None,
        "true_closed_equals_mutual_outer_backward_pass": backward_closed_difference is None,
        "true_positive_equals_outer_positive_forward_pass": forward_positive_difference is None,
        "true_positive_equals_outer_positive_backward_pass": backward_positive_difference is None,
        "true_closed_mutual_outer_forward_symmetric_difference_count": sum(
            len(true_forward[source] ^ outer_mutual_forward[source])
            for source in range(total)
        ),
        "true_closed_mutual_outer_backward_symmetric_difference_count": sum(
            len(true_backward[source] ^ outer_mutual_backward[source])
            for source in range(total)
        ),
        "true_positive_outer_positive_forward_symmetric_difference_count": sum(
            len(true_forward_positive[source] ^ outer_forward_positive[source])
            for source in range(total)
        ),
        "true_positive_outer_positive_backward_symmetric_difference_count": sum(
            len(true_backward_positive[source] ^ outer_backward_positive[source])
            for source in range(total)
        ),
        "true_closed_graph": true_closed_stats,
        "true_positive_graph": true_positive_stats,
        "first_counterexamples": mismatches,
    }
    return record


ANCHOR_COMPARISON_FIELDS: tuple[tuple[str, str], ...] = (
    ("active_node_count", "two_sided_in_box_node_count"),
    ("active_node_ids_sha256", "two_sided_in_box_node_ids_sha256"),
    ("true_forward_closed_edge_count", "true_forward_closed_edge_count"),
    ("true_backward_closed_edge_count", "true_backward_closed_edge_count"),
    ("true_forward_positive_edge_count", "true_forward_positive_edge_count"),
    ("true_backward_positive_edge_count", "true_backward_positive_edge_count"),
    ("outer_forward_closed_edge_count", "outer_forward_closed_edge_count"),
    ("outer_backward_closed_edge_count", "outer_backward_closed_edge_count"),
    ("outer_forward_positive_edge_count", "outer_forward_positive_edge_count"),
    ("outer_backward_positive_edge_count", "outer_backward_positive_edge_count"),
    ("true_forward_labelled_edge_hash", "true_forward_closed_edge_hash"),
    ("true_backward_labelled_edge_hash", "true_backward_closed_edge_hash"),
    ("outer_forward_labelled_edge_hash", "outer_forward_closed_edge_hash"),
    ("outer_backward_labelled_edge_hash", "outer_backward_closed_edge_hash"),
    ("true_forward_unlabelled_edge_hash", "true_forward_unlabelled_edge_hash"),
    ("true_backward_unlabelled_edge_hash", "true_backward_unlabelled_edge_hash"),
    (
        "true_forward_positive_unlabelled_edge_hash",
        "true_forward_positive_unlabelled_edge_hash",
    ),
    (
        "outer_forward_positive_unlabelled_edge_hash",
        "outer_forward_positive_unlabelled_edge_hash",
    ),
)


def align_anchor_record(
    record: dict[str, Any], parent: dict[str, Any]
) -> dict[str, object]:
    field_matches = {
        producer_field: record.get(producer_field) == parent.get(parent_field)
        for producer_field, parent_field in ANCHOR_COMPARISON_FIELDS
    }
    field_matches.update(
        {
            "true_closed_largest_scc_size": record["true_closed_graph"][
                "largest_scc_size"
            ]
            == parent["true_closed_graph"]["largest_scc_size"],
            "true_positive_largest_scc_size": record["true_positive_graph"][
                "largest_scc_size"
            ]
            == parent["true_positive_area_graph"]["largest_scc_size"],
            "true_closed_identity": record[
                "true_closed_equals_mutual_outer_forward_pass"
            ]
            == parent["true_equals_outer_mutual_pass"],
            "true_positive_identity": record[
                "true_positive_equals_outer_positive_forward_pass"
            ]
            == parent["true_positive_equals_outer_positive_pass"],
        }
    )
    return {
        "configuration": record["configuration"],
        "field_matches": field_matches,
        "all_fields_match": all(field_matches.values()),
    }


def _run_jobs(jobs: list[dict[str, Any]], workers: int) -> list[dict[str, Any]]:
    if workers <= 0:
        raise SystemExit("--workers must be positive")
    worker_count = min(workers, len(jobs))
    if worker_count == 1:
        return [build_configuration(job) for job in jobs]
    with ProcessPoolExecutor(max_workers=worker_count) as executor:
        return list(executor.map(build_configuration, jobs))


def load_edge_arrays(record: dict[str, Any]) -> dict[str, np.ndarray]:
    path = PROJECT_ROOT / str(record["edge_array_path"])
    if sha256_file(path) != record["edge_array_sha256"]:
        raise AssertionError(f"edge artifact hash mismatch: {path}")
    with np.load(path, allow_pickle=False) as payload:
        return {key: np.asarray(payload[key]) for key in payload.files}


def canonical_pairs(pairs: np.ndarray) -> np.ndarray:
    pairs = np.asarray(pairs, dtype=np.int64).reshape((-1, 2))
    if len(pairs) == 0:
        return np.empty((0, 2), dtype=np.int64)
    return np.unique(pairs, axis=0)


def graph_pairs(packed: np.ndarray, positive: bool) -> np.ndarray:
    if positive:
        return canonical_pairs(packed[packed[:, 2] == 1, :2])
    return canonical_pairs(packed[:, :2])


def pair_hash(pairs: np.ndarray) -> str:
    digest = hashlib.sha256()
    for source, target in canonical_pairs(pairs):
        digest.update(f"{int(source)},{int(target)}\n".encode("ascii"))
    return digest.hexdigest()


def pair_set(pairs: np.ndarray) -> set[tuple[int, int]]:
    return {(int(source), int(target)) for source, target in pairs}


def project_nodes(nodes: Iterable[int], child_grid: int, parent_grid: int) -> set[int]:
    projected: set[int] = set()
    for node in nodes:
        child = int(node)
        x_index = child % child_grid
        y_index = child // child_grid
        projected.add((y_index // 2) * parent_grid + (x_index // 2))
    return projected


def lift_nodes(nodes: Iterable[int], parent_grid: int, child_grid: int) -> set[int]:
    lifted: set[int] = set()
    for node in nodes:
        parent = int(node)
        x_index = parent % parent_grid
        y_index = parent // parent_grid
        for dy in (0, 1):
            for dx in (0, 1):
                lifted.add((2 * y_index + dy) * child_grid + (2 * x_index + dx))
    return lifted


def project_pairs(
    pairs: np.ndarray, child_grid: int, parent_grid: int
) -> np.ndarray:
    if len(pairs) == 0:
        return np.empty((0, 2), dtype=np.int64)
    projected = np.empty_like(pairs, dtype=np.int64)
    for column in (0, 1):
        ids = pairs[:, column]
        x_index = ids % child_grid
        y_index = ids // child_grid
        projected[:, column] = (y_index // 2) * parent_grid + (x_index // 2)
    return canonical_pairs(projected)


def induced_pairs(pairs: np.ndarray, active: set[int]) -> np.ndarray:
    return canonical_pairs(
        np.asarray(
            [
                (int(source), int(target))
                for source, target in pairs
                if int(source) in active and int(target) in active
            ],
            dtype=np.int64,
        ).reshape((-1, 2))
    )


def components_from_pairs(
    pairs: np.ndarray, active: set[int]
) -> list[list[int]]:
    active_ids = sorted(active)
    index = {node: position for position, node in enumerate(active_ids)}
    adjacency: list[set[int]] = [set() for _ in active_ids]
    for source, target in pairs:
        source_id, target_id = int(source), int(target)
        if source_id in index and target_id in index:
            adjacency[index[source_id]].add(index[target_id])
    components = strongly_connected_components(adjacency)
    global_components = [
        sorted(active_ids[local] for local in component) for component in components
    ]
    global_components.sort(key=lambda nodes: (-len(nodes), tuple(nodes)))
    return global_components


def exact_ratio(numerator: Fraction, denominator: Fraction) -> dict[str, object]:
    return fraction_payload(numerator / denominator if denominator else Fraction(0))


def refinement_variant_metrics(
    *,
    variant: str,
    positive: bool,
    parent_record: dict[str, Any],
    child_record: dict[str, Any],
    parent_arrays: dict[str, np.ndarray],
    child_arrays: dict[str, np.ndarray],
    parent_edges: Sequence[Fraction],
    child_edges: Sequence[Fraction],
    parent_active: set[int],
    child_active: set[int],
    lifted_active: set[int],
) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    parent_grid = int(parent_record["grid"])
    child_grid = int(child_record["grid"])
    parent_full = graph_pairs(parent_arrays["true_forward_edges"], positive)
    child_full = graph_pairs(child_arrays["true_forward_edges"], positive)
    parent_full_backward = graph_pairs(
        parent_arrays["true_backward_edges"], positive
    )
    child_full_backward = graph_pairs(child_arrays["true_backward_edges"], positive)
    projected_full = project_pairs(child_full, child_grid, parent_grid)
    projected_full_backward = project_pairs(
        child_full_backward, child_grid, parent_grid
    )
    parent_induced = induced_pairs(parent_full, parent_active)
    child_matched = induced_pairs(child_full, lifted_active)
    projected_matched = project_pairs(child_matched, child_grid, parent_grid)
    parent_induced_backward = induced_pairs(parent_full_backward, parent_active)
    child_matched_backward = induced_pairs(child_full_backward, lifted_active)
    projected_matched_backward = project_pairs(
        child_matched_backward, child_grid, parent_grid
    )

    parent_stats_key = "true_positive_graph" if positive else "true_closed_graph"
    parent_dominant = {
        int(node)
        for node in parent_record[parent_stats_key]["largest_scc_node_ids"]
    }
    lifted_parent_dominant = lift_nodes(parent_dominant, parent_grid, child_grid)
    matched_components = components_from_pairs(child_matched, lifted_active)
    descendants = [
        component
        for component in matched_components
        if component
        and project_nodes(component, child_grid, parent_grid) <= parent_dominant
    ]
    multi_descendants = [component for component in descendants if len(component) > 1]
    largest_descendant = multi_descendants[0] if multi_descendants else []
    descendant_union = {
        node for component in multi_descendants for node in component
    }

    parent_core_area = node_union_area(parent_edges, parent_grid, parent_dominant)
    lifted_core_area = node_union_area(child_edges, child_grid, lifted_parent_dominant)
    descendant_union_area = node_union_area(child_edges, child_grid, descendant_union)
    largest_descendant_area = node_union_area(child_edges, child_grid, largest_descendant)
    largest_descendant_set = set(largest_descendant)
    intersection = largest_descendant_set & lifted_parent_dominant
    union = largest_descendant_set | lifted_parent_dominant
    intersection_area = node_union_area(child_edges, child_grid, intersection)
    union_area = node_union_area(child_edges, child_grid, union)

    child_full_largest = {
        int(node)
        for node in child_record[parent_stats_key]["largest_scc_node_ids"]
    }
    matched_largest = set(matched_components[0]) if matched_components else set()
    full_matched_intersection = child_full_largest & matched_largest
    full_matched_union = child_full_largest | matched_largest

    parent_edge_set = pair_set(parent_induced)
    projected_child_edge_set = pair_set(projected_matched)
    multiplicities: dict[tuple[int, int], int] = {}
    for source, target in child_matched:
        source_id, target_id = int(source), int(target)
        source_x, source_y = source_id % child_grid, source_id // child_grid
        target_x, target_y = target_id % child_grid, target_id // child_grid
        projected = (
            (source_y // 2) * parent_grid + source_x // 2,
            (target_y // 2) * parent_grid + target_x // 2,
        )
        multiplicities[projected] = multiplicities.get(projected, 0) + 1
    realized = parent_edge_set & projected_child_edge_set
    realized_multiplicities = [multiplicities[edge] for edge in sorted(realized)]

    result: dict[str, Any] = {
        "variant": variant,
        "complete_projected_edge_count": len(projected_full),
        "parent_complete_edge_count": len(parent_full),
        "complete_projection_symmetric_difference_count": len(
            pair_set(projected_full) ^ pair_set(parent_full)
        ),
        "complete_projection_equals_parent_pass": np.array_equal(
            projected_full, parent_full
        ),
        "complete_backward_projected_edge_count": len(projected_full_backward),
        "parent_complete_backward_edge_count": len(parent_full_backward),
        "complete_backward_projection_symmetric_difference_count": len(
            pair_set(projected_full_backward) ^ pair_set(parent_full_backward)
        ),
        "complete_backward_projection_equals_parent_pass": np.array_equal(
            projected_full_backward, parent_full_backward
        ),
        "complete_projected_edge_sha256": pair_hash(projected_full),
        "parent_complete_edge_sha256": pair_hash(parent_full),
        "complete_backward_projected_edge_sha256": pair_hash(
            projected_full_backward
        ),
        "parent_complete_backward_edge_sha256": pair_hash(parent_full_backward),
        "matched_support_child_edge_count": len(child_matched),
        "matched_support_projected_edge_count": len(projected_matched),
        "parent_active_induced_edge_count": len(parent_induced),
        "matched_support_projection_symmetric_difference_count": len(
            pair_set(projected_matched) ^ pair_set(parent_induced)
        ),
        "matched_support_projection_equals_parent_active_graph_pass": np.array_equal(
            projected_matched, parent_induced
        ),
        "matched_support_child_backward_edge_count": len(child_matched_backward),
        "matched_support_projected_backward_edge_count": len(
            projected_matched_backward
        ),
        "parent_active_induced_backward_edge_count": len(parent_induced_backward),
        "matched_support_backward_projection_symmetric_difference_count": len(
            pair_set(projected_matched_backward) ^ pair_set(parent_induced_backward)
        ),
        "matched_support_backward_projection_equals_parent_active_graph_pass": np.array_equal(
            projected_matched_backward, parent_induced_backward
        ),
        "matched_support_projected_edge_sha256": pair_hash(projected_matched),
        "parent_active_induced_edge_sha256": pair_hash(parent_induced),
        "matched_support_projected_backward_edge_sha256": pair_hash(
            projected_matched_backward
        ),
        "parent_active_induced_backward_edge_sha256": pair_hash(
            parent_induced_backward
        ),
        "parent_dominant_scc_node_count": len(parent_dominant),
        "parent_dominant_scc_node_ids_sha256": node_hash(parent_dominant),
        "parent_dominant_scc_area": fraction_payload(parent_core_area),
        "lifted_parent_dominant_node_count": len(lifted_parent_dominant),
        "lifted_parent_dominant_node_ids_sha256": node_hash(lifted_parent_dominant),
        "lifted_parent_dominant_area": fraction_payload(lifted_core_area),
        "matched_support_scc_count": len(matched_components),
        "matched_support_largest_scc_size": len(matched_components[0])
        if matched_components
        else 0,
        "matched_support_largest_scc_node_ids_sha256": node_hash(matched_largest),
        "descendant_scc_count": len(descendants),
        "multi_node_descendant_scc_count": len(multi_descendants),
        "nontrivial_descendant_exists_pass": bool(multi_descendants),
        "descendant_union_node_count": len(descendant_union),
        "descendant_union_node_ids_sha256": node_hash(descendant_union),
        "descendant_union_area": fraction_payload(descendant_union_area),
        "descendant_union_coverage_of_lifted_parent": exact_ratio(
            descendant_union_area, lifted_core_area
        ),
        "largest_descendant_node_count": len(largest_descendant),
        "largest_descendant_node_ids_sha256": node_hash(largest_descendant),
        "largest_descendant_area": fraction_payload(largest_descendant_area),
        "largest_descendant_intersection_over_parent": exact_ratio(
            intersection_area, lifted_core_area
        ),
        "largest_descendant_intersection_over_child": exact_ratio(
            intersection_area, largest_descendant_area
        ),
        "largest_descendant_jaccard": exact_ratio(intersection_area, union_area),
        "recurrent_child_coverage_of_lifted_parent_core": exact_ratio(
            descendant_union_area, lifted_core_area
        ),
        "parent_edge_realization_count": len(realized),
        "parent_edge_realization_fraction": (
            len(realized) / len(parent_edge_set) if parent_edge_set else 1.0
        ),
        "child_edge_multiplicity_min": min(realized_multiplicities)
        if realized_multiplicities
        else None,
        "child_edge_multiplicity_max": max(realized_multiplicities)
        if realized_multiplicities
        else None,
        "child_edge_multiplicity_mean": (
            sum(realized_multiplicities) / len(realized_multiplicities)
            if realized_multiplicities
            else None
        ),
        "full_child_largest_scc_size": len(child_full_largest),
        "full_child_largest_scc_node_ids_sha256": node_hash(child_full_largest),
        "full_vs_matched_largest_intersection_count": len(full_matched_intersection),
        "full_vs_matched_largest_jaccard": (
            len(full_matched_intersection) / len(full_matched_union)
            if full_matched_union
            else 1.0
        ),
    }
    arrays = {
        f"{variant}_complete_projected_edges": projected_full,
        f"{variant}_complete_projected_backward_edges": projected_full_backward,
        f"{variant}_matched_support_projected_edges": projected_matched,
        f"{variant}_matched_support_projected_backward_edges": projected_matched_backward,
        f"{variant}_parent_active_induced_edges": parent_induced,
        f"{variant}_parent_active_induced_backward_edges": parent_induced_backward,
        f"{variant}_largest_descendant_node_ids": np.asarray(
            largest_descendant, dtype=np.int64
        ),
        f"{variant}_descendant_union_node_ids": np.asarray(
            sorted(descendant_union), dtype=np.int64
        ),
        f"{variant}_matched_support_largest_node_ids": np.asarray(
            sorted(matched_largest), dtype=np.int64
        ),
    }
    return result, arrays


def build_refinement_record(
    specification: dict[str, Any],
    records_by_name: dict[str, dict[str, Any]],
    edge_dir: Path,
) -> dict[str, Any]:
    parent_name = str(specification["parent_configuration_id"])
    child_name = str(specification["child_configuration_id"])
    parent = records_by_name[parent_name]
    child = records_by_name[child_name]
    parent_grid = int(parent["grid"])
    child_grid = int(child["grid"])
    if child_grid != 2 * parent_grid:
        raise AssertionError(f"non-2x refinement: {parent_name}->{child_name}")
    parent_offset = Fraction(str(parent["grid_offset_fraction"]))
    child_offset = Fraction(str(child["grid_offset_fraction"]))
    parent_edges = exact_edge_vector(RADIUS, parent_grid, parent_offset)
    child_edges = exact_edge_vector(RADIUS, child_grid, child_offset)
    nested_edges_pass = all(
        parent_edges[index] == child_edges[2 * index]
        for index in range(parent_grid + 1)
    )
    parent_arrays = load_edge_arrays(parent)
    child_arrays = load_edge_arrays(child)
    parent_active = {int(value) for value in parent_arrays["active_node_ids"]}
    child_active = {int(value) for value in child_arrays["active_node_ids"]}
    lifted_active = lift_nodes(parent_active, parent_grid, child_grid)
    active_lift_difference = lifted_active - child_active

    closed, closed_arrays = refinement_variant_metrics(
        variant="true_closed",
        positive=False,
        parent_record=parent,
        child_record=child,
        parent_arrays=parent_arrays,
        child_arrays=child_arrays,
        parent_edges=parent_edges,
        child_edges=child_edges,
        parent_active=parent_active,
        child_active=child_active,
        lifted_active=lifted_active,
    )
    positive, positive_arrays = refinement_variant_metrics(
        variant="true_positive",
        positive=True,
        parent_record=parent,
        child_record=child,
        parent_arrays=parent_arrays,
        child_arrays=child_arrays,
        parent_edges=parent_edges,
        child_edges=child_edges,
        parent_active=parent_active,
        child_active=child_active,
        lifted_active=lifted_active,
    )
    artifact_path = edge_dir / f"refinement_{parent_name}_to_{child_name}.npz"
    save_npz_atomic(
        artifact_path,
        lift_parent_active_node_ids=np.asarray(sorted(lifted_active), dtype=np.int64),
        active_lift_missing_child_node_ids=np.asarray(
            sorted(active_lift_difference), dtype=np.int64
        ),
        **closed_arrays,
        **positive_arrays,
    )
    return {
        "parent_configuration": parent_name,
        "child_configuration": child_name,
        "ratio": 2,
        "exact_nested_edge_vectors_pass": nested_edges_pass,
        "parent_active_node_count": len(parent_active),
        "lifted_parent_active_node_count": len(lifted_active),
        "child_active_node_count": len(child_active),
        "lift_parent_active_subset_child_active_pass": not active_lift_difference,
        "active_lift_missing_child_node_count": len(active_lift_difference),
        "active_lift_missing_child_node_ids_sha256": node_hash(active_lift_difference),
        "refinement_array_path": portable_path(artifact_path),
        "refinement_array_sha256": sha256_file(artifact_path),
        "true_closed": closed,
        "true_positive": positive,
    }


def geometric_intersection_area(
    nodes_a: set[int],
    edges_a: Sequence[Fraction],
    grid_a: int,
    nodes_b: set[int],
    edges_b: Sequence[Fraction],
    grid_b: int,
) -> Fraction:
    intersection = Fraction(0)
    for node_a in nodes_a:
        ax, ay = node_a % grid_a, node_a // grid_a
        x_indices = closed_target_indices(edges_b, edges_a[ax], edges_a[ax + 1])
        y_indices = closed_target_indices(edges_b, edges_a[ay], edges_a[ay + 1])
        for by in y_indices:
            y_width = min(edges_a[ay + 1], edges_b[by + 1]) - max(
                edges_a[ay], edges_b[by]
            )
            if y_width <= 0:
                continue
            for bx in x_indices:
                node_b = by * grid_b + bx
                if node_b not in nodes_b:
                    continue
                x_width = min(edges_a[ax + 1], edges_b[bx + 1]) - max(
                    edges_a[ax], edges_b[bx]
                )
                if x_width > 0:
                    intersection += x_width * y_width
    return intersection


def shifted_core_comparisons(
    records_by_name: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    names = ("n254_d0", "n254_dm1_3", "n254_dp1_3")
    pairs = ((names[0], names[1]), (names[0], names[2]), (names[1], names[2]))
    output: list[dict[str, Any]] = []
    for first_name, second_name in pairs:
        first = records_by_name[first_name]
        second = records_by_name[second_name]
        first_grid, second_grid = int(first["grid"]), int(second["grid"])
        first_edges = exact_edge_vector(
            RADIUS, first_grid, Fraction(str(first["grid_offset_fraction"]))
        )
        second_edges = exact_edge_vector(
            RADIUS, second_grid, Fraction(str(second["grid_offset_fraction"]))
        )
        variants: dict[str, Any] = {}
        for key in ("true_closed_graph", "true_positive_graph"):
            first_nodes = {int(node) for node in first[key]["largest_scc_node_ids"]}
            second_nodes = {int(node) for node in second[key]["largest_scc_node_ids"]}
            first_area = node_union_area(first_edges, first_grid, first_nodes)
            second_area = node_union_area(second_edges, second_grid, second_nodes)
            intersection = geometric_intersection_area(
                first_nodes,
                first_edges,
                first_grid,
                second_nodes,
                second_edges,
                second_grid,
            )
            union = first_area + second_area - intersection
            variants[key] = {
                "first_node_count": len(first_nodes),
                "second_node_count": len(second_nodes),
                "first_area": fraction_payload(first_area),
                "second_area": fraction_payload(second_area),
                "intersection_area": fraction_payload(intersection),
                "intersection_over_first": exact_ratio(intersection, first_area),
                "intersection_over_second": exact_ratio(intersection, second_area),
                "geometric_jaccard": exact_ratio(intersection, union),
            }
        output.append(
            {
                "first_configuration": first_name,
                "second_configuration": second_name,
                "variants": variants,
            }
        )
    return output


def serial_parallel_match(
    parallel: dict[str, Any], serial: dict[str, Any]
) -> dict[str, Any]:
    fields = (
        "active_node_ids_sha256",
        "analytic_active_node_ids_sha256",
        "true_forward_labelled_edge_hash",
        "true_backward_labelled_edge_hash",
        "outer_forward_labelled_edge_hash",
        "outer_backward_labelled_edge_hash",
        "true_forward_unlabelled_edge_hash",
        "true_forward_positive_unlabelled_edge_hash",
        "outer_mutual_forward_unlabelled_edge_hash",
        "outer_forward_positive_unlabelled_edge_hash",
    )
    matches = {field: parallel[field] == serial[field] for field in fields}
    return {
        "configuration": parallel["configuration"],
        "parallel_edge_array_path": parallel["edge_array_path"],
        "serial_edge_array_path": serial["edge_array_path"],
        "field_matches": matches,
        "all_hashes_match": all(matches.values()),
    }


def write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    if not records:
        return
    flat_rows: list[dict[str, object]] = []
    for record in records:
        flat_rows.append(
            {
                "configuration": record["configuration"],
                "evidence_role": record["evidence_role"],
                "grid": record["grid"],
                "grid_offset_fraction": record["grid_offset_fraction"],
                "active_node_count": record["active_node_count"],
                "uncapped_k_max": record["uncapped_k_max"],
                "maximum_outer_area_ratio": record["maximum_outer_area_ratio"]["float"],
                "true_forward_closed_edge_count": record[
                    "true_forward_closed_edge_count"
                ],
                "true_forward_positive_edge_count": record[
                    "true_forward_positive_edge_count"
                ],
                "closed_largest_scc_size": record["true_closed_graph"][
                    "largest_scc_size"
                ],
                "positive_largest_scc_size": record["true_positive_graph"][
                    "largest_scc_size"
                ],
                "closed_multi_node_scc_count": record["true_closed_graph"][
                    "multi_node_scc_count"
                ],
                "positive_multi_node_scc_count": record["true_positive_graph"][
                    "multi_node_scc_count"
                ],
                "closed_identity_pass": record[
                    "true_closed_equals_mutual_outer_forward_pass"
                ]
                and record["true_closed_equals_mutual_outer_backward_pass"],
                "positive_identity_pass": record[
                    "true_positive_equals_outer_positive_forward_pass"
                ]
                and record["true_positive_equals_outer_positive_backward_pass"],
            }
        )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(flat_rows[0]))
        writer.writeheader()
        writer.writerows(flat_rows)


def main() -> None:
    args = parse_args()
    protocol = load_and_validate_protocol()
    parent_hashes = validate_parent_artifacts(protocol)
    protocol_sha256 = sha256_file(PROTOCOL)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.edge_dir.mkdir(parents=True, exist_ok=True)

    parent_payload = json.loads(
        (PROJECT_ROOT / "results" / "true_image_graph_r055.json").read_text(
            encoding="utf-8"
        )
    )
    parent_by_name = {
        str(record["configuration"]): record for record in parent_payload["records"]
    }

    anchor_jobs: list[dict[str, Any]] = []
    for item in protocol["development_anchors"]:
        job = configuration_tuple(item, "development_anchor")
        job["edge_path"] = args.edge_dir / f"{job['configuration']}.npz"
        anchor_jobs.append(job)
    anchor_records = _run_jobs(anchor_jobs, min(args.workers, 4))
    anchor_alignment = [
        align_anchor_record(record, parent_by_name[str(record["configuration"])])
        for record in anchor_records
    ]
    if not all(bool(row["all_fields_match"]) for row in anchor_alignment):
        raise SystemExit(f"R056 anchor reconstruction failed: {anchor_alignment}")

    heldout_jobs: list[dict[str, Any]] = []
    for item in protocol["heldout_configurations"]:
        job = configuration_tuple(item, "heldout")
        job["edge_path"] = args.edge_dir / f"{job['configuration']}.npz"
        heldout_jobs.append(job)
    heldout_records = _run_jobs(heldout_jobs, min(args.workers, 6))

    replay_source = next(
        job for job in heldout_jobs if job["configuration"] == "n127_d0"
    )
    replay_job = dict(replay_source)
    replay_job["evidence_role"] = "serial_replay"
    replay_job["edge_path"] = args.edge_dir / "n127_d0_serial_replay.npz"
    serial_record = build_configuration(replay_job)
    parallel_record = next(
        record for record in heldout_records if record["configuration"] == "n127_d0"
    )
    replay = serial_parallel_match(parallel_record, serial_record)
    if not replay["all_hashes_match"]:
        raise SystemExit(f"R056 serial/parallel replay failed: {replay}")

    records = anchor_records + heldout_records
    records_by_name = {str(record["configuration"]): record for record in records}
    refinement_records = [
        build_refinement_record(item, records_by_name, args.edge_dir)
        for item in protocol["nested_refinements"]
    ]
    shifted_comparisons = shifted_core_comparisons(records_by_name)

    output = {
        "run_id": "R056_TRUE_IMAGE_REFINEMENT",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": str(PROTOCOL.relative_to(PROJECT_ROOT)),
        "protocol_sha256": protocol_sha256,
        "parent_artifact_sha256": parent_hashes,
        "anchor_alignment": anchor_alignment,
        "serial_parallel_replay": replay,
        "records": records,
        "refinements": refinement_records,
        "shifted_core_comparisons": shifted_comparisons,
        "scope": protocol["scope"],
    }
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
                "edge_dir": str(args.edge_dir),
                "anchor_count": len(anchor_records),
                "heldout_count": len(heldout_records),
                "refinement_count": len(refinement_records),
                "workers": min(args.workers, 6),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
