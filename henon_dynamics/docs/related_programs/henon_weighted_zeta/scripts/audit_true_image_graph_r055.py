#!/usr/bin/env python3
"""Enumerate exact closed-cell incidences of the analytic Hénon image."""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_exact_closed_cover import (  # noqa: E402
    A_VALUE,
    CONFIGURATIONS,
    ETA,
    MAX_SUBDIVISIONS,
    RADIUS,
    _direction_metrics,
    exact_abs_extrema,
    exact_edge_vector,
    uncapped_adaptive_subdivisions_exact,
)
from scripts.audit_outer_graph_r054 import graph_stats, node_hash  # noqa: E402

PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R055_TRUE_IMAGE_GRAPH_PROTOCOL.json"
)
OUTER_RESULT = PROJECT_ROOT / "results" / "outer_graph_r054.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="true_image_graph_r055")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--outer-input", type=Path, default=OUTER_RESULT)
    parser.add_argument("--workers", type=int, default=1)
    return parser.parse_args()


def validate_protocol(payload: dict[str, object]) -> None:
    protocol_configurations = tuple(
        (int(item["grid"]), Fraction(str(item["grid_offset"])))
        for item in payload["configurations"]  # type: ignore[index]
    )
    code_configurations = tuple((grid, offset) for _, grid, offset in CONFIGURATIONS)
    checks = {
        "run_id": payload.get("run_id") == "R055_TRUE_IMAGE_GRAPH",
        "source_protocol": payload.get("source_protocol")
        == "R054_OUTER_GRAPH_PROTOCOL.json",
        "a": Fraction(str(payload.get("a"))) == A_VALUE,
        "radius": Fraction(str(payload.get("radius"))) == RADIUS,
        "eta": Fraction(str(payload.get("eta"))) == ETA,
        "maximum_subdivisions": int(payload.get("maximum_subdivisions"))
        == MAX_SUBDIVISIONS,
        "target_semantics": payload.get("target_semantics")
        == "closed source and target rectangles",
        "configurations": protocol_configurations == code_configurations,
    }
    if not all(checks.values()):
        raise SystemExit(f"R055 code/protocol mismatch: {checks}")


def exact_square_range(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    if upper < lower:
        raise ValueError("reversed interval")
    minimum, maximum = exact_abs_extrema(lower, upper)
    return minimum * minimum, maximum * maximum


def closed_target_indices(
    edges: tuple[Fraction, ...], lower: Fraction, upper: Fraction
) -> tuple[int, ...]:
    """Return all closed cells touching [lower, upper], clipped to the box."""

    if upper < lower or upper < edges[0] or lower > edges[-1]:
        return ()
    first = max(0, bisect.bisect_left(edges, lower) - 1)
    last = min(len(edges) - 2, bisect.bisect_right(edges, upper) - 1)
    if first > last:
        return ()
    return tuple(range(first, last + 1))


def forward_image_hull(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    x_min_sq, x_max_sq = exact_square_range(*source_x)
    return (
        1 - A_VALUE * x_max_sq - source_y[1],
        1 - A_VALUE * x_min_sq - source_y[0],
        source_x[0],
        source_x[1],
    )


def inverse_image_hull(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    y_min_sq, y_max_sq = exact_square_range(*source_y)
    return (
        source_y[0],
        source_y[1],
        1 - A_VALUE * y_max_sq - source_x[1],
        1 - A_VALUE * y_min_sq - source_x[0],
    )


def _overlap_class(
    parameter_interval: tuple[Fraction, Fraction],
    target_interval: tuple[Fraction, Fraction],
    coefficient_lower: Fraction,
    coefficient_upper: Fraction,
) -> bool | None:
    """Return positive-area flag, or None when the closed intersection is empty."""

    first_lower = max(parameter_interval[0], target_interval[0])
    first_upper = min(parameter_interval[1], target_interval[1])
    if first_upper < first_lower:
        return None
    sq_lower, sq_upper = exact_square_range(first_lower, first_upper)
    q_lower = A_VALUE * sq_lower
    q_upper = A_VALUE * sq_upper
    overlap_lower = max(q_lower, coefficient_lower)
    overlap_upper = min(q_upper, coefficient_upper)
    if overlap_upper < overlap_lower:
        return None
    positive = first_upper > first_lower and overlap_upper > overlap_lower
    return positive


def forward_true_class(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
) -> bool | None:
    # H_a(x,y)=(1-a*x^2-y,x). The target second coordinate restricts x.
    return _overlap_class(
        source_x,
        target_y,
        1 - target_x[1] - source_y[1],
        1 - target_x[0] - source_y[0],
    )


def inverse_true_class(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
) -> bool | None:
    # H_a^{-1}(x,y)=(y,1-a*y^2-x). The target first coordinate restricts y.
    return _overlap_class(
        source_y,
        target_x,
        1 - target_y[1] - source_x[1],
        1 - target_y[0] - source_x[0],
    )


def edge_hash(
    edges: Iterable[tuple[int, int, str]], direction: str
) -> str:
    if direction not in {"F", "B"}:
        raise ValueError("direction must be F or B")
    digest = hashlib.sha256()
    for source, target, label in sorted(edges):
        digest.update(f"{direction},{source},{target},{label}\n".encode("ascii"))
    return digest.hexdigest()


def unlabelled_edge_hash(adjacency: list[set[int]]) -> str:
    digest = hashlib.sha256()
    for source, targets in enumerate(adjacency):
        for target in sorted(targets):
            digest.update(f"{source},{target}\n".encode("ascii"))
    return digest.hexdigest()


def edge_records(
    adjacency: list[set[int]], positive: list[set[int]]
) -> list[tuple[int, int, str]]:
    return [
        (source, target, "P" if target in positive[source] else "T")
        for source in range(len(adjacency))
        for target in sorted(adjacency[source])
    ]


def mutual_adjacency(
    forward: list[set[int]], backward: list[set[int]]
) -> list[set[int]]:
    return [
        {target for target in forward[source] if source in backward[target]}
        for source in range(len(forward))
    ]


def transpose_match(
    forward: list[set[int]],
    backward: list[set[int]],
    forward_positive: list[set[int]],
    backward_positive: list[set[int]],
) -> bool:
    for source, targets in enumerate(forward):
        for target in targets:
            if source not in backward[target]:
                return False
            if (target in forward_positive[source]) != (
                source in backward_positive[target]
            ):
                return False
    for source, targets in enumerate(backward):
        for target in targets:
            if source not in forward[target]:
                return False
    return True


def _configuration_name(grid: int, offset: Fraction) -> str:
    if offset == 0:
        return f"n{grid}_d0"
    return f"n{grid}_d{'m1q' if offset == Fraction(-1, 4) else 'p1q'}"


def summarize_configuration(
    job: tuple[tuple[str, int, Fraction], dict[str, object] | None]
) -> dict[str, object]:
    (name, grid, offset), outer_reference = job
    edges = exact_edge_vector(RADIUS, grid, offset)
    minimum_width = min(upper - lower for lower, upper in zip(edges, edges[1:]))
    k_values = [
        uncapped_adaptive_subdivisions_exact(
            edges[index], edges[index + 1], minimum_width
        )
        for index in range(grid)
    ]
    if max(k_values) > MAX_SUBDIVISIONS:
        raise AssertionError("R055 encountered a truncated adaptive K")

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
    forward_candidate_count = 0
    backward_candidate_count = 0
    active: set[int] = set()

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
            forward_target_x = closed_target_indices(
                edges, forward_hull[0], forward_hull[1]
            )
            forward_target_y = closed_target_indices(
                edges, forward_hull[2], forward_hull[3]
            )
            forward_candidate_count += len(forward_target_x) * len(forward_target_y)
            for target_y_index in forward_target_y:
                target_y = (edges[target_y_index], edges[target_y_index + 1])
                for target_x_index in forward_target_x:
                    target_x = (edges[target_x_index], edges[target_x_index + 1])
                    target_id = target_y_index * grid + target_x_index
                    forward_candidates[source_id].add(target_id)
                    positive = forward_true_class(
                        source_x, source_y, target_x, target_y
                    )
                    if positive is not None:
                        true_forward[source_id].add(target_id)
                        if positive:
                            true_forward_positive[source_id].add(target_id)

            inverse_hull = inverse_image_hull(source_x, source_y)
            inverse_target_x = closed_target_indices(
                edges, inverse_hull[0], inverse_hull[1]
            )
            inverse_target_y = closed_target_indices(
                edges, inverse_hull[2], inverse_hull[3]
            )
            backward_candidate_count += len(inverse_target_x) * len(inverse_target_y)
            for target_y_index in inverse_target_y:
                target_y = (edges[target_y_index], edges[target_y_index + 1])
                for target_x_index in inverse_target_x:
                    target_x = (edges[target_x_index], edges[target_x_index + 1])
                    target_id = target_y_index * grid + target_x_index
                    backward_candidates[source_id].add(target_id)
                    positive = inverse_true_class(
                        source_x, source_y, target_x, target_y
                    )
                    if positive is not None:
                        true_backward[source_id].add(target_id)
                        if positive:
                            true_backward_positive[source_id].add(target_id)

    outer_forward_edges = edge_records(outer_forward, outer_forward_positive)
    outer_backward_edges = edge_records(outer_backward, outer_backward_positive)
    true_forward_edges = edge_records(true_forward, true_forward_positive)
    true_backward_edges = edge_records(true_backward, true_backward_positive)
    outer_mutual = mutual_adjacency(outer_forward, outer_backward)
    true_mutual = mutual_adjacency(true_forward, true_backward)

    outer_reference_match: bool | None
    if outer_reference is None:
        outer_reference_match = None
    else:
        outer_reference_match = (
            len(outer_forward_edges)
            == int(outer_reference["forward_closed_edge_count"])
            and len(outer_backward_edges)
            == int(outer_reference["backward_closed_edge_count"])
            and len(active) == int(outer_reference["two_sided_in_box_node_count"])
            and node_hash(active)
            == outer_reference["two_sided_in_box_node_ids_sha256"]
            and edge_hash(outer_forward_edges, "F")
            == outer_reference["forward_closed_edge_hash"]
            and edge_hash(outer_backward_edges, "B")
            == outer_reference["backward_closed_edge_hash"]
        )
    true_subset_outer = all(
        true_forward[source] <= outer_forward[source]
        and true_backward[source] <= outer_backward[source]
        for source in range(total)
    )
    true_positive_subset_outer_positive = all(
        true_forward_positive[source] <= outer_forward_positive[source]
        and true_backward_positive[source] <= outer_backward_positive[source]
        for source in range(total)
    )
    candidate_contains_true = all(
        true_forward[source] <= forward_candidates[source]
        and true_backward[source] <= backward_candidates[source]
        for source in range(total)
    )

    true_forward_count = len(true_forward_edges)
    true_backward_count = len(true_backward_edges)
    outer_forward_count = len(outer_forward_edges)
    outer_backward_count = len(outer_backward_edges)
    true_forward_positive_count = sum(
        1 for _, _, label in true_forward_edges if label == "P"
    )
    true_backward_positive_count = sum(
        1 for _, _, label in true_backward_edges if label == "P"
    )
    outer_forward_positive_count = sum(
        1 for _, _, label in outer_forward_edges if label == "P"
    )
    outer_backward_positive_count = sum(
        1 for _, _, label in outer_backward_edges if label == "P"
    )
    outer_mutual_edges = sum(len(targets) for targets in outer_mutual)
    true_mutual_edges = sum(len(targets) for targets in true_mutual)
    true_equals_outer_mutual = all(
        true_forward[source] == outer_mutual[source]
        for source in range(total)
    )
    true_positive_equals_outer_positive = all(
        true_forward_positive[source] == outer_forward_positive[source]
        for source in range(total)
    )

    return {
        "configuration": name,
        "grid": grid,
        "grid_offset": float(offset),
        "grid_offset_fraction": (
            str(offset.numerator)
            if offset.denominator == 1
            else f"{offset.numerator}/{offset.denominator}"
        ),
        "state_count": total,
        "two_sided_in_box_node_count": len(active),
        "two_sided_in_box_node_fraction": len(active) / total,
        "two_sided_in_box_node_ids_sha256": node_hash(active),
        "forward_candidate_pair_count": forward_candidate_count,
        "backward_candidate_pair_count": backward_candidate_count,
        "outer_forward_closed_edge_count": outer_forward_count,
        "outer_backward_closed_edge_count": outer_backward_count,
        "outer_forward_positive_edge_count": outer_forward_positive_count,
        "outer_backward_positive_edge_count": outer_backward_positive_count,
        "outer_mutual_edge_count": outer_mutual_edges,
        "outer_forward_closed_edge_hash": edge_hash(outer_forward_edges, "F"),
        "outer_backward_closed_edge_hash": edge_hash(outer_backward_edges, "B"),
        "outer_forward_unlabelled_edge_hash": unlabelled_edge_hash(outer_forward),
        "outer_backward_unlabelled_edge_hash": unlabelled_edge_hash(outer_backward),
        "outer_forward_positive_unlabelled_edge_hash": unlabelled_edge_hash(
            outer_forward_positive
        ),
        "outer_mutual_unlabelled_edge_hash": unlabelled_edge_hash(outer_mutual),
        "true_forward_closed_edge_count": true_forward_count,
        "true_backward_closed_edge_count": true_backward_count,
        "true_forward_positive_edge_count": true_forward_positive_count,
        "true_backward_positive_edge_count": true_backward_positive_count,
        "true_mutual_edge_count": true_mutual_edges,
        "true_forward_closed_edge_hash": edge_hash(true_forward_edges, "F"),
        "true_backward_closed_edge_hash": edge_hash(true_backward_edges, "B"),
        "true_forward_unlabelled_edge_hash": unlabelled_edge_hash(true_forward),
        "true_backward_unlabelled_edge_hash": unlabelled_edge_hash(true_backward),
        "true_forward_positive_unlabelled_edge_hash": unlabelled_edge_hash(
            true_forward_positive
        ),
        "true_mutual_unlabelled_edge_hash": unlabelled_edge_hash(true_mutual),
        "outer_minus_true_forward_edge_count": outer_forward_count
        - true_forward_count,
        "outer_minus_true_backward_edge_count": outer_backward_count
        - true_backward_count,
        "outer_minus_true_forward_positive_edge_count": outer_forward_positive_count
        - true_forward_positive_count,
        "outer_minus_true_backward_positive_edge_count": outer_backward_positive_count
        - true_backward_positive_count,
        "outer_false_positive_forward_fraction": (
            (outer_forward_count - true_forward_count) / outer_forward_count
            if outer_forward_count
            else 0.0
        ),
        "outer_false_positive_backward_fraction": (
            (outer_backward_count - true_backward_count) / outer_backward_count
            if outer_backward_count
            else 0.0
        ),
        "outer_reference_provided": outer_reference is not None,
        "outer_reconstruction_pass": outer_reference_match,
        "true_edge_subset_outer_pass": true_subset_outer,
        "true_positive_subset_outer_positive_pass": true_positive_subset_outer_positive,
        "true_equals_outer_mutual_pass": true_equals_outer_mutual,
        "true_positive_equals_outer_positive_pass": true_positive_equals_outer_positive,
        "candidate_hull_contains_true_pass": candidate_contains_true,
        "outer_forward_inverse_transpose_pass": transpose_match(
            outer_forward,
            outer_backward,
            outer_forward_positive,
            outer_backward_positive,
        ),
        "true_forward_inverse_transpose_pass": transpose_match(
            true_forward,
            true_backward,
            true_forward_positive,
            true_backward_positive,
        ),
        "outer_all_closed_graph": graph_stats(outer_forward, active),
        "outer_positive_area_graph": graph_stats(outer_forward_positive, active),
        "outer_mutual_graph": graph_stats(outer_mutual, active),
        "true_closed_graph": graph_stats(true_forward, active),
        "true_positive_area_graph": graph_stats(true_forward_positive, active),
        "true_mutual_graph": graph_stats(true_mutual, active),
    }


def require_outer_reference_matches(records: list[dict[str, object]]) -> None:
    """Enforce the R055 canonical parent-alignment invariant before writing."""

    mismatches = [
        str(record.get("configuration"))
        for record in records
        if record.get("outer_reference_provided") is not True
        or record.get("outer_reconstruction_pass") is not True
    ]
    if mismatches:
        raise AssertionError(
            "R055 canonical outer-parent reconstruction failed for: "
            + ", ".join(mismatches)
        )


def main() -> None:
    args = parse_args()
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    validate_protocol(protocol)
    outer_payload = json.loads(args.outer_input.read_text(encoding="utf-8"))
    outer_by_name = {
        str(record["configuration"]): record for record in outer_payload["records"]
    }
    configurations = [
        (
            _configuration_name(int(item["grid"]), Fraction(str(item["grid_offset"]))),
            int(item["grid"]),
            Fraction(str(item["grid_offset"])),
        )
        for item in protocol["configurations"]
    ]
    missing_outer = [
        configuration[0]
        for configuration in configurations
        if configuration[0] not in outer_by_name
    ]
    if missing_outer:
        raise SystemExit(
            "R055 canonical outer parent is missing configurations: "
            + ", ".join(missing_outer)
        )
    jobs = [(configuration, outer_by_name[configuration[0]]) for configuration in configurations]
    if args.workers <= 0:
        raise SystemExit("--workers must be positive")
    workers = min(args.workers, len(jobs))
    if workers == 1:
        records = [summarize_configuration(job) for job in jobs]
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            records = list(executor.map(summarize_configuration, jobs))
    require_outer_reference_matches(records)
    output = {
        "run_id": "R055_TRUE_IMAGE_GRAPH",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": str(PROTOCOL.relative_to(PROJECT_ROOT)),
        "parent_outer_graph": str(args.outer_input),
        "records": records,
        "scope": (
            "exact finite analytic closed-rectangle image incidences compared "
            "with the R054 rectangle outer-cover graph; no invariant-set or "
            "operator claim"
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
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "workers": workers}, indent=2))


if __name__ == "__main__":
    main()
