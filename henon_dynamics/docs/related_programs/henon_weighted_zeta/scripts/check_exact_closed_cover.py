#!/usr/bin/env python3
"""Independent reconstruction of the frozen R053 exact cover.

This checker deliberately does not import geometry helpers from
``audit_exact_closed_cover``.  It reconstructs the exact rational edges,
adaptive counts, slab rectangles, X2--X5 decisions, and canonical adjacency
hashes from the frozen JSON protocol, then compares them with the producer
payload.  Float64 is not used in any checker decision.
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R053_EXACT_CLOSED_COVER_PROTOCOL.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "exact_closed_cover_r053.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=(
            PROJECT_ROOT
            / "results"
            / "exact_closed_cover_independent_check_r053.json"
        ),
    )
    parser.add_argument("--workers", type=int, default=1)
    return parser.parse_args()


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def multiset_hash(values: Iterable[Fraction]) -> str:
    digest = hashlib.sha256()
    for value in sorted(values):
        digest.update(rational_text(value).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def ceiling(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def make_edges(radius: Fraction, grid: int, offset: Fraction) -> tuple[Fraction, ...]:
    width = 2 * radius / grid
    values = [-radius]
    values.extend(
        -radius + (Fraction(index) + offset) * width
        for index in range(1, grid)
    )
    values.append(radius)
    return tuple(values)


def abs_range(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    largest = max(abs(lower), abs(upper))
    smallest = Fraction(0) if lower <= 0 <= upper else min(abs(lower), abs(upper))
    return smallest, largest


def adaptive_count(
    lower: Fraction,
    upper: Fraction,
    minimum_width: Fraction,
    a_value: Fraction,
    eta: Fraction,
) -> int:
    _, largest = abs_range(lower, upper)
    numerator = 2 * a_value * largest * (upper - lower)
    return 1 if numerator == 0 else max(1, ceiling(numerator / (eta * minimum_width)))


def slab_rectangle(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    slab_index: int,
    subdivisions: int,
    inverse: bool,
    a_value: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if inverse:
        width = (source_y[1] - source_y[0]) / subdivisions
        lower = source_y[0] + slab_index * width
        upper = source_y[0] + (slab_index + 1) * width
        smallest, largest = abs_range(lower, upper)
        return (
            lower,
            upper,
            1 - a_value * largest**2 - source_x[1],
            1 - a_value * smallest**2 - source_x[0],
        )
    width = (source_x[1] - source_x[0]) / subdivisions
    lower = source_x[0] + slab_index * width
    upper = source_x[0] + (slab_index + 1) * width
    smallest, largest = abs_range(lower, upper)
    return (
        1 - a_value * largest**2 - source_y[1],
        1 - a_value * smallest**2 - source_y[0],
        lower,
        upper,
    )


def closed_indices(
    edges: Sequence[Fraction], lower: Fraction, upper: Fraction
) -> tuple[int, int] | None:
    if upper < lower or upper < edges[0] or lower > edges[-1]:
        return None
    first = max(0, bisect.bisect_left(edges, lower) - 1)
    last = min(len(edges) - 2, bisect.bisect_right(edges, upper) - 1)
    if first > last:
        return None
    for index in range(first, last + 1):
        if not (edges[index] <= upper and edges[index + 1] >= lower):
            raise AssertionError("independent closed-range predicate failure")
    if first > 0 and edges[first - 1] <= upper and edges[first] >= lower:
        raise AssertionError("independent closed range omitted its left neighbor")
    if last + 1 < len(edges) - 1:
        if edges[last + 1] <= upper and edges[last + 2] >= lower:
            raise AssertionError("independent closed range omitted its right neighbor")
    return first, last


def half_open_indices(
    edges: Sequence[Fraction], lower: Fraction, upper: Fraction
) -> tuple[int, int] | None:
    # Target cells are [e_i,e_{i+1}) except the final cell, whose right edge
    # is closed at the box boundary.  A degenerate interval at an internal
    # edge therefore belongs to the cell on its right.
    if upper < lower or upper < edges[0] or lower > edges[-1]:
        return None
    first = max(0, bisect.bisect_right(edges, lower) - 1)
    first = min(len(edges) - 2, first)
    last = min(len(edges) - 2, bisect.bisect_right(edges, upper) - 1)
    return None if first > last else (first, last)


def rectangle_classes(
    edges: Sequence[Fraction],
    bounds: tuple[Fraction, Fraction, Fraction, Fraction],
) -> dict[int, bool]:
    x_range = closed_indices(edges, bounds[0], bounds[1])
    y_range = closed_indices(edges, bounds[2], bounds[3])
    if x_range is None or y_range is None:
        return {}
    grid = len(edges) - 1
    output: dict[int, bool] = {}
    for target_y in range(y_range[0], y_range[1] + 1):
        positive_y = min(bounds[3], edges[target_y + 1]) > max(
            bounds[2], edges[target_y]
        )
        for target_x in range(x_range[0], x_range[1] + 1):
            positive_x = min(bounds[1], edges[target_x + 1]) > max(
                bounds[0], edges[target_x]
            )
            output[target_y * grid + target_x] = positive_x and positive_y
    return output


def half_open_targets(
    edges: Sequence[Fraction],
    bounds: tuple[Fraction, Fraction, Fraction, Fraction],
) -> set[int]:
    x_range = half_open_indices(edges, bounds[0], bounds[1])
    y_range = half_open_indices(edges, bounds[2], bounds[3])
    if x_range is None or y_range is None:
        return set()
    grid = len(edges) - 1
    return {
        target_y * grid + target_x
        for target_y in range(y_range[0], y_range[1] + 1)
        for target_x in range(x_range[0], x_range[1] + 1)
    }


def exact_median(values: Iterable[Fraction]) -> Fraction:
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def update_hash(
    digest: "hashlib._Hash",
    direction: str,
    source_id: int,
    classes: dict[int, bool],
) -> None:
    for target_id in sorted(classes):
        label = "P" if classes[target_id] else "T"
        digest.update(
            f"{direction},{source_id},{target_id},{label}\n".encode("ascii")
        )


def direction_record(
    edges: Sequence[Fraction],
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    subdivisions: int,
    minimum_width: Fraction,
    inverse: bool,
    a_value: Fraction,
    eta: Fraction,
) -> tuple[Fraction, dict[int, bool], bool, bool, bool]:
    source_area = (source_x[1] - source_x[0]) * (source_y[1] - source_y[0])
    area = Fraction(0)
    classes: dict[int, bool] = {}
    half_open: set[int] = set()
    local_bound_pass = True
    for slab_index in range(subdivisions):
        bounds = slab_rectangle(
            source_x, source_y, slab_index, subdivisions, inverse, a_value
        )
        area += (bounds[1] - bounds[0]) * (bounds[3] - bounds[2])
        slab_classes = rectangle_classes(edges, bounds)
        for target_id, positive in slab_classes.items():
            classes[target_id] = classes.get(target_id, False) or positive
        half_open.update(half_open_targets(edges, bounds))
        perpendicular_width = (
            source_x[1] - source_x[0]
            if inverse
            else source_y[1] - source_y[0]
        )
        nonlinear_width = (
            bounds[3] - bounds[2] if inverse else bounds[1] - bounds[0]
        )
        local_bound_pass = local_bound_pass and (
            nonlinear_width - perpendicular_width <= eta * minimum_width
        )
    positive_targets = {
        target_id for target_id, positive in classes.items() if positive
    }
    closed_dominance = half_open <= set(classes)
    positive_subset = positive_targets <= half_open
    return area / source_area, classes, local_bound_pass, closed_dominance, positive_subset


def fixed_ratio(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    inverse: bool,
    a_value: Fraction,
) -> Fraction:
    source_area = (source_x[1] - source_x[0]) * (source_y[1] - source_y[0])
    area = Fraction(0)
    for slab_index in range(16):
        bounds = slab_rectangle(source_x, source_y, slab_index, 16, inverse, a_value)
        area += (bounds[1] - bounds[0]) * (bounds[3] - bounds[2])
    return area / source_area


def reconstruct_configuration(task: dict[str, object]) -> dict[str, object]:
    radius = Fraction(str(task["radius"]))
    a_value = Fraction(str(task["a"]))
    eta = Fraction(str(task["eta"]))
    maximum_subdivisions = int(task["maximum_subdivisions"])
    grid = int(task["grid"])
    offset = Fraction(str(task["grid_offset"]))
    name = str(task["configuration"])
    producer = dict(task["producer"])

    edges = make_edges(radius, grid, offset)
    widths = [upper - lower for lower, upper in zip(edges, edges[1:])]
    minimum_width = min(widths)
    k_values = [
        adaptive_count(edges[index], edges[index + 1], minimum_width, a_value, eta)
        for index in range(grid)
    ]
    edge_pass = (
        edges[0] == -radius
        and edges[-1] == radius
        and all(lower < upper for lower, upper in zip(edges, edges[1:]))
    )
    cap_pass = max(k_values) <= maximum_subdivisions

    forward_ratios: list[Fraction] = []
    backward_ratios: list[Fraction] = []
    forward_fixed: list[Fraction] = []
    backward_fixed: list[Fraction] = []
    local_pass = True
    closed_dominance_pass = True
    positive_subset_pass = True
    forward_count = backward_count = 0
    forward_positive = backward_positive = 0
    forward_touch = backward_touch = 0
    forward_digest = hashlib.sha256()
    backward_digest = hashlib.sha256()

    for source_y_index in range(grid):
        source_y = (edges[source_y_index], edges[source_y_index + 1])
        for source_x_index in range(grid):
            source_x = (edges[source_x_index], edges[source_x_index + 1])
            source_id = source_y_index * grid + source_x_index
            forward = direction_record(
                edges,
                source_x,
                source_y,
                k_values[source_x_index],
                minimum_width,
                False,
                a_value,
                eta,
            )
            backward = direction_record(
                edges,
                source_x,
                source_y,
                k_values[source_y_index],
                minimum_width,
                True,
                a_value,
                eta,
            )
            forward_ratios.append(forward[0])
            backward_ratios.append(backward[0])
            forward_fixed.append(fixed_ratio(source_x, source_y, False, a_value))
            backward_fixed.append(fixed_ratio(source_x, source_y, True, a_value))
            local_pass = local_pass and forward[2] and backward[2]
            closed_dominance_pass = (
                closed_dominance_pass and forward[3] and backward[3]
            )
            positive_subset_pass = positive_subset_pass and forward[4] and backward[4]
            update_hash(forward_digest, "F", source_id, forward[1])
            update_hash(backward_digest, "B", source_id, backward[1])
            forward_count += len(forward[1])
            backward_count += len(backward[1])
            forward_positive += sum(forward[1].values())
            backward_positive += sum(backward[1].values())
            forward_touch += sum(not value for value in forward[1].values())
            backward_touch += sum(not value for value in backward[1].values())

    area_bound_pass = (
        max(forward_ratios) <= Fraction(5, 4)
        and max(backward_ratios) <= Fraction(5, 4)
    )
    fixed_comparison_pass = (
        exact_median(forward_ratios) <= exact_median(forward_fixed)
        and exact_median(backward_ratios) <= exact_median(backward_fixed)
    )
    forward_inverse_multiset_pass = sorted(forward_ratios) == sorted(backward_ratios)
    recomputed = {
        "exact_edge_integrity_pass": edge_pass,
        "exact_edge_and_cap_integrity_pass": edge_pass and cap_pass,
        "x3_exact_local_global_bound_pass": cap_pass and local_pass and area_bound_pass,
        "exact_adaptive_no_worse_than_fixed_k16_median_pass": fixed_comparison_pass,
        "adaptive_k_uncapped_max": max(k_values),
        "adaptive_k_exact_multiset_sha256": multiset_hash(
            Fraction(min(maximum_subdivisions, value), 1) for value in k_values
        ),
        "closed_cover_dominance_pass": closed_dominance_pass,
        "positive_area_subset_of_half_open_reference_pass": positive_subset_pass,
        "forward_inverse_exact_area_multisets_equal": forward_inverse_multiset_pass,
        "forward_closed_adjacency_count": forward_count,
        "backward_closed_adjacency_count": backward_count,
        "forward_positive_area_adjacency_count": forward_positive,
        "backward_positive_area_adjacency_count": backward_positive,
        "forward_touch_only_adjacency_count": forward_touch,
        "backward_touch_only_adjacency_count": backward_touch,
        "forward_closed_adjacency_sha256": forward_digest.hexdigest(),
        "backward_closed_adjacency_sha256": backward_digest.hexdigest(),
        "forward_exact_area_ratio_multiset_sha256": multiset_hash(forward_ratios),
        "backward_exact_area_ratio_multiset_sha256": multiset_hash(backward_ratios),
        "forward_exact_area_ratio_median_fraction": rational_text(
            exact_median(forward_ratios)
        ),
        "backward_exact_area_ratio_median_fraction": rational_text(
            exact_median(backward_ratios)
        ),
        "forward_exact_area_ratio_max_fraction": rational_text(max(forward_ratios)),
        "backward_exact_area_ratio_max_fraction": rational_text(max(backward_ratios)),
        "forward_fixed_k16_exact_area_ratio_median_fraction": rational_text(
            exact_median(forward_fixed)
        ),
        "backward_fixed_k16_exact_area_ratio_median_fraction": rational_text(
            exact_median(backward_fixed)
        ),
    }
    comparisons = {
        key: recomputed[key] == producer.get(key) for key in recomputed
    }
    return {
        "configuration": name,
        "all_recomputed_fields_match": all(comparisons.values()),
        "comparisons": comparisons,
        "recomputed": recomputed,
    }


def main() -> None:
    args = parse_args()
    if args.workers <= 0:
        raise SystemExit("--workers must be positive")
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    producer_payload = json.loads(args.input.read_text(encoding="utf-8"))
    producer_by_key = {
        (int(record["grid"]), str(record["grid_offset_fraction"])): record
        for record in producer_payload["records"]
    }
    tasks: list[dict[str, object]] = []
    for item in protocol["configurations"]:
        grid = int(item["grid"])
        offset = Fraction(str(item["grid_offset"]))
        offset_text = rational_text(offset)
        producer = producer_by_key[(grid, offset_text)]
        tasks.append(
            {
                "configuration": producer["configuration"],
                "radius": protocol["radius"],
                "a": protocol["a"],
                "eta": protocol["eta"],
                "maximum_subdivisions": protocol["maximum_subdivisions"],
                "grid": grid,
                "grid_offset": item["grid_offset"],
                "producer": producer,
            }
        )
    workers = min(args.workers, len(tasks))
    if workers == 1:
        records = [reconstruct_configuration(task) for task in tasks]
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            records = list(executor.map(reconstruct_configuration, tasks))
    output = {
        "run_id": "R053_EXACT_CLOSED_COVER_INDEPENDENT_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "producer_input": str(args.input),
        "checker_imports_producer_geometry": False,
        "all_configurations_match": all(
            record["all_recomputed_fields_match"] for record in records
        ),
        "records": records,
        "scope": (
            "independent exact-rational reconstruction of R053 X2--X5 and "
            "canonical rectangle-enclosure adjacency hashes"
        ),
    }
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "all_configurations_match": output["all_configurations_match"],
                "workers": workers,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
