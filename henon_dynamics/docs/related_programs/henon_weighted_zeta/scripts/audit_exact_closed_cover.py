#!/usr/bin/env python3
"""Audit the R053 exact-rational adaptive closed-cell strip cover.

All geometric decisions in this module are made with
``fractions.Fraction``.  The float64 path is used only for the frozen B1 bridge
diagnostic; it never determines an R053 image bound or target-cell
intersection.

The frozen protocol is documented in
``research/refine-logs/R053_EXACT_CLOSED_COVER_MANIFEST.md``.  In particular,
passing this finite-grid audit is not an invariant-set, Markov-partition, or
operator-convergence certificate.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import math
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_adaptive_rounded_cover import (  # noqa: E402
    adaptive_subdivisions as float_adaptive_subdivisions,
)
from scripts.audit_interval_cover import (  # noqa: E402
    abs_extrema as float_abs_extrema,
    edge_vector as float_edge_vector,
)


MANIFEST = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R053_EXACT_CLOSED_COVER_MANIFEST.md"
)
PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R053_EXACT_CLOSED_COVER_PROTOCOL.json"
)

A_VALUE = Fraction(6, 1)
RADIUS = Fraction("0.6380064794363034")
ETA = Fraction(1, 4)
MAX_SUBDIVISIONS = 64
AREA_RATIO_BOUND = Fraction(5, 4)

CONFIGURATIONS: tuple[tuple[str, int, Fraction], ...] = (
    ("n96_d0", 96, Fraction(0, 1)),
    ("n160_d0", 160, Fraction(0, 1)),
    ("n160_dm1q", 160, Fraction(-1, 4)),
    ("n160_dp1q", 160, Fraction(1, 4)),
)


@dataclass(frozen=True)
class ExactStatistics:
    """Exact summary statistics for a nonempty rational sample."""

    mean: Fraction
    median: Fraction
    p95: Fraction
    maximum: Fraction


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="exact_closed_cover_r053")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument(
        "--configuration",
        action="append",
        choices=[name for name, _, _ in CONFIGURATIONS],
        help=(
            "Run only the named frozen configuration; repeat to select more "
            "than one. The default is all four frozen configurations."
        ),
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of configuration-level worker processes (default: 1).",
    )
    return parser.parse_args()


def fraction_text(value: Fraction) -> str:
    """Return a lossless, JSON-friendly representation of ``value``."""

    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact_ceiling(value: Fraction) -> int:
    """Return ``ceil(value)`` without a float conversion."""

    return -((-value.numerator) // value.denominator)


def exact_edge_vector(
    radius: Fraction, grid: int, offset: Fraction
) -> tuple[Fraction, ...]:
    """Construct the clipped shifted grid using exact rational arithmetic."""

    if grid <= 0:
        raise ValueError("grid must be positive")
    if not Fraction(-1, 2) <= offset <= Fraction(1, 2):
        raise ValueError("offset must lie in [-1/2, 1/2]")
    nominal_width = 2 * radius / grid
    edges = [-radius]
    edges.extend(
        -radius + (Fraction(index, 1) + offset) * nominal_width
        for index in range(1, grid)
    )
    edges.append(radius)
    if any(upper <= lower for lower, upper in zip(edges, edges[1:])):
        raise ValueError("non-increasing exact cell edges")
    return tuple(edges)


def exact_abs_extrema(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    """Return the exact minimum and maximum of ``abs`` on a closed interval."""

    if upper < lower:
        raise ValueError("interval endpoints are reversed")
    maximum = max(abs(lower), abs(upper))
    minimum = Fraction(0, 1) if lower <= 0 <= upper else min(abs(lower), abs(upper))
    return minimum, maximum


def uncapped_adaptive_subdivisions_exact(
    lower: Fraction,
    upper: Fraction,
    target_min_width: Fraction,
    *,
    a_value: Fraction = A_VALUE,
    eta: Fraction = ETA,
) -> int:
    """Evaluate the frozen adaptive rule and its ceiling exactly."""

    if upper <= lower:
        raise ValueError("source interval must have positive width")
    if target_min_width <= 0:
        raise ValueError("target_min_width must be positive")
    if a_value < 0:
        raise ValueError("a_value must be nonnegative")
    if eta <= 0:
        raise ValueError("eta must be positive")
    _, maximum_abs = exact_abs_extrema(lower, upper)
    numerator = 2 * a_value * maximum_abs * (upper - lower)
    if numerator == 0:
        return 1
    return max(1, exact_ceiling(numerator / (eta * target_min_width)))


def adaptive_subdivisions_exact(
    lower: Fraction,
    upper: Fraction,
    target_min_width: Fraction,
    *,
    maximum_subdivisions: int = MAX_SUBDIVISIONS,
) -> int:
    """Return the exactly computed adaptive count after the frozen cap."""

    if maximum_subdivisions <= 0:
        raise ValueError("maximum_subdivisions must be positive")
    return min(
        maximum_subdivisions,
        uncapped_adaptive_subdivisions_exact(lower, upper, target_min_width),
    )


def exact_slab_bounds(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    index: int,
    subdivisions: int,
    inverse: bool,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return an exact rectangle enclosing one forward or inverse strip image."""

    if not 0 <= index < subdivisions:
        raise IndexError("slab index is outside the subdivision range")
    if subdivisions <= 0:
        raise ValueError("subdivisions must be positive")
    x_lower, x_upper = source_x
    y_lower, y_upper = source_y
    if inverse:
        width = (y_upper - y_lower) / subdivisions
        sub_lower = y_lower + index * width
        sub_upper = y_lower + (index + 1) * width
        y_abs_min, y_abs_max = exact_abs_extrema(sub_lower, sub_upper)
        image_x_lower, image_x_upper = sub_lower, sub_upper
        image_y_lower = 1 - A_VALUE * y_abs_max**2 - x_upper
        image_y_upper = 1 - A_VALUE * y_abs_min**2 - x_lower
    else:
        width = (x_upper - x_lower) / subdivisions
        sub_lower = x_lower + index * width
        sub_upper = x_lower + (index + 1) * width
        x_abs_min, x_abs_max = exact_abs_extrema(sub_lower, sub_upper)
        image_x_lower = 1 - A_VALUE * x_abs_max**2 - y_upper
        image_x_upper = 1 - A_VALUE * x_abs_min**2 - y_lower
        image_y_lower, image_y_upper = sub_lower, sub_upper
    return image_x_lower, image_x_upper, image_y_lower, image_y_upper


def closed_cell_index_range(
    edges: Sequence[Fraction], lower: Fraction, upper: Fraction
) -> tuple[int, int, bool]:
    """Return all cells whose closed intervals meet ``[lower, upper]``.

    An endpoint on an internal grid edge therefore selects both adjacent
    target cells.  Point intervals are allowed and select one or two cells.
    """

    if upper < lower:
        return 0, -1, False
    if upper < edges[0] or lower > edges[-1]:
        return 0, -1, False
    first = max(0, bisect.bisect_left(edges, lower) - 1)
    last = min(len(edges) - 2, bisect.bisect_right(edges, upper) - 1)
    return first, last, first <= last


def half_open_cell_index_range(
    edges: Sequence[Fraction], lower: Fraction, upper: Fraction
) -> tuple[int, int, bool]:
    """Return cells ``[e_i,e_{i+1})`` meeting a closed source interval.

    The final target cell is closed at the box's right endpoint.  Consequently
    an internal shared-edge point belongs to the cell on its right, while the
    right box endpoint belongs to the final cell.
    """

    if upper < lower:
        return 0, -1, False
    if upper < edges[0] or lower > edges[-1]:
        return 0, -1, False
    first = min(
        len(edges) - 2,
        max(0, bisect.bisect_right(edges, lower) - 1),
    )
    last = min(len(edges) - 2, bisect.bisect_right(edges, upper) - 1)
    return first, last, first <= last


def rectangle_target_cells(
    edges: Sequence[Fraction],
    bounds: tuple[Fraction, Fraction, Fraction, Fraction],
    *,
    closed: bool,
) -> set[int]:
    """Enumerate exact target cells meeting a rectangle under chosen semantics."""

    indexer = closed_cell_index_range if closed else half_open_cell_index_range
    first_x, last_x, nonempty_x = indexer(edges, bounds[0], bounds[1])
    first_y, last_y, nonempty_y = indexer(edges, bounds[2], bounds[3])
    if not (nonempty_x and nonempty_y):
        return set()
    grid = len(edges) - 1
    return {
        target_y * grid + target_x
        for target_y in range(first_y, last_y + 1)
        for target_x in range(first_x, last_x + 1)
    }


def closed_range_certificate(
    edges: Sequence[Fraction],
    lower: Fraction,
    upper: Fraction,
    first: int,
    last: int,
    nonempty: bool,
) -> bool:
    """Check the exact X5 predicates for an optimized closed index range."""

    if not nonempty:
        return upper < edges[0] or lower > edges[-1] or upper < lower
    if not (0 <= first <= last < len(edges) - 1):
        return False
    for index in range(first, last + 1):
        if not (edges[index] <= upper and edges[index + 1] >= lower):
            return False
    if first > 0:
        outside = first - 1
        if edges[outside] <= upper and edges[outside + 1] >= lower:
            return False
    if last + 1 < len(edges) - 1:
        outside = last + 1
        if edges[outside] <= upper and edges[outside + 1] >= lower:
            return False
    return True


def rectangle_target_classes(
    edges: Sequence[Fraction],
    bounds: tuple[Fraction, Fraction, Fraction, Fraction],
) -> dict[int, bool]:
    """Map closed target ids to positive-area (true) or touch-only (false)."""

    first_x, last_x, nonempty_x = closed_cell_index_range(
        edges, bounds[0], bounds[1]
    )
    first_y, last_y, nonempty_y = closed_cell_index_range(
        edges, bounds[2], bounds[3]
    )
    if not closed_range_certificate(
        edges, bounds[0], bounds[1], first_x, last_x, nonempty_x
    ):
        raise AssertionError("closed x-index range failed its exact certificate")
    if not closed_range_certificate(
        edges, bounds[2], bounds[3], first_y, last_y, nonempty_y
    ):
        raise AssertionError("closed y-index range failed its exact certificate")
    if not (nonempty_x and nonempty_y):
        return {}
    grid = len(edges) - 1
    classes: dict[int, bool] = {}
    for target_y in range(first_y, last_y + 1):
        positive_y = min(bounds[3], edges[target_y + 1]) > max(
            bounds[2], edges[target_y]
        )
        for target_x in range(first_x, last_x + 1):
            positive_x = min(bounds[1], edges[target_x + 1]) > max(
                bounds[0], edges[target_x]
            )
            classes[target_y * grid + target_x] = positive_x and positive_y
    return classes


def _float_slab_bounds(
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    split: np.ndarray,
    index: int,
    inverse: bool,
) -> tuple[float, float, float, float]:
    """Reproduce R052's final-one-ulp rectangle for a precomputed split."""

    sub_lower, sub_upper = float(split[index]), float(split[index + 1])
    if inverse:
        y_abs_min, y_abs_max = float_abs_extrema(sub_lower, sub_upper)
        raw = (
            sub_lower,
            sub_upper,
            1.0 - 6.0 * y_abs_max**2 - source_x[1],
            1.0 - 6.0 * y_abs_min**2 - source_x[0],
        )
    else:
        x_abs_min, x_abs_max = float_abs_extrema(sub_lower, sub_upper)
        raw = (
            1.0 - 6.0 * x_abs_max**2 - source_y[1],
            1.0 - 6.0 * x_abs_min**2 - source_y[0],
            sub_lower,
            sub_upper,
        )
    return (
        float(np.nextafter(raw[0], -math.inf)),
        float(np.nextafter(raw[1], math.inf)),
        float(np.nextafter(raw[2], -math.inf)),
        float(np.nextafter(raw[3], math.inf)),
    )


def _binary_exact_slab_bounds(
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    split: np.ndarray,
    index: int,
    inverse: bool,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Evaluate a float-grid slab polynomial exactly as a binary rational.

    This is the exact comparison object specified by bridge diagnostic B1.  It
    deliberately uses the binary values produced by R052's grid and
    ``numpy.linspace``, rather than the separate decimal-rational R053 grid.
    """

    exact_source_x = tuple(Fraction.from_float(value) for value in source_x)
    exact_source_y = tuple(Fraction.from_float(value) for value in source_y)
    sub_lower = Fraction.from_float(float(split[index]))
    sub_upper = Fraction.from_float(float(split[index + 1]))
    if inverse:
        y_abs_min, y_abs_max = exact_abs_extrema(sub_lower, sub_upper)
        return (
            sub_lower,
            sub_upper,
            1 - A_VALUE * y_abs_max**2 - exact_source_x[1],
            1 - A_VALUE * y_abs_min**2 - exact_source_x[0],
        )
    x_abs_min, x_abs_max = exact_abs_extrema(sub_lower, sub_upper)
    return (
        1 - A_VALUE * x_abs_max**2 - exact_source_y[1],
        1 - A_VALUE * x_abs_min**2 - exact_source_y[0],
        sub_lower,
        sub_upper,
    )


def _endpoint_containment_margins(
    exact: tuple[Fraction, Fraction, Fraction, Fraction],
    rounded_float: tuple[float, float, float, float],
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return exact signed margins; nonnegative means float encloses exact."""

    float_fraction = tuple(Fraction.from_float(value) for value in rounded_float)
    return (
        exact[0] - float_fraction[0],
        float_fraction[1] - exact[1],
        exact[2] - float_fraction[2],
        float_fraction[3] - exact[3],
    )


def binary_float_endpoint_audit(
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    subdivisions: int,
    inverse: bool,
) -> dict[str, object]:
    """Run B1 for one R052 binary-float source cell and direction."""

    split_interval = source_y if inverse else source_x
    split = np.linspace(split_interval[0], split_interval[1], subdivisions + 1)
    margins: list[Fraction] = []
    for index in range(subdivisions):
        binary_exact = _binary_exact_slab_bounds(
            source_x, source_y, split, index, inverse
        )
        rounded_float = _float_slab_bounds(
            source_x, source_y, split, index, inverse
        )
        margins.extend(_endpoint_containment_margins(binary_exact, rounded_float))
    minimum = min(margins)
    return {
        "minimum_margin": minimum,
        "contains": minimum >= 0,
        "violation_count": sum(value < 0 for value in margins),
        "comparison_count": len(margins),
    }


def exact_statistics(values: Iterable[Fraction]) -> ExactStatistics:
    """Compute mean, median, NumPy-style type-7 p95, and maximum exactly."""

    ordered = sorted(values)
    if not ordered:
        raise ValueError("exact_statistics requires at least one value")
    count = len(ordered)
    mean = sum(ordered, Fraction(0, 1)) / count
    middle = count // 2
    median = (
        ordered[middle]
        if count % 2
        else (ordered[middle - 1] + ordered[middle]) / 2
    )
    position = Fraction(19, 20) * (count - 1)
    lower_index = position.numerator // position.denominator
    weight = position - lower_index
    upper_index = min(count - 1, lower_index + 1)
    p95 = ordered[lower_index] * (1 - weight) + ordered[upper_index] * weight
    return ExactStatistics(mean=mean, median=median, p95=p95, maximum=ordered[-1])


def _statistics_fields(prefix: str, stats: ExactStatistics) -> dict[str, object]:
    fields: dict[str, object] = {}
    for name, value in (
        ("mean", stats.mean),
        ("median", stats.median),
        ("p95", stats.p95),
        ("max", stats.maximum),
    ):
        fields[f"{prefix}_{name}"] = float(value)
        fields[f"{prefix}_{name}_fraction"] = fraction_text(value)
    return fields


def exact_area_ratio(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    subdivisions: int,
    inverse: bool,
) -> Fraction:
    """Compute a strip rectangle-area ratio exactly, without target indexing."""

    source_area = (source_x[1] - source_x[0]) * (source_y[1] - source_y[0])
    rectangle_area = Fraction(0, 1)
    for index in range(subdivisions):
        bounds = exact_slab_bounds(source_x, source_y, index, subdivisions, inverse)
        rectangle_area += (bounds[1] - bounds[0]) * (bounds[3] - bounds[2])
    return rectangle_area / source_area


def exact_multiset_hash(values: Iterable[Fraction]) -> str:
    """Hash a rational multiset canonically, retaining multiplicities."""

    digest = hashlib.sha256()
    for value in sorted(values):
        digest.update(fraction_text(value).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def update_adjacency_hash(
    digest: "hashlib._Hash",
    direction: str,
    source_id: int,
    target_classes: dict[int, bool],
) -> None:
    """Append canonical adjacency records in increasing target-id order."""

    for target_id in sorted(target_classes):
        incidence_class = "P" if target_classes[target_id] else "T"
        digest.update(
            f"{direction},{source_id},{target_id},{incidence_class}\n".encode(
                "ascii"
            )
        )


def validate_frozen_protocol() -> dict[str, object]:
    """Refuse production if code constants diverge from the frozen JSON."""

    if not PROTOCOL.is_file():
        raise SystemExit(
            "R053 production is disabled until the frozen protocol exists at "
            f"{PROTOCOL}"
        )
    payload = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    protocol_configurations = tuple(
        (
            int(item["grid"]),
            Fraction(str(item["grid_offset"])),
        )
        for item in payload["configurations"]
    )
    code_configurations = tuple((grid, offset) for _, grid, offset in CONFIGURATIONS)
    checks = {
        "run_id": payload.get("run_id") == "R053_EXACT_CLOSED_COVER",
        "a": Fraction(str(payload["a"])) == A_VALUE,
        "radius": Fraction(str(payload["radius"])) == RADIUS,
        "eta": Fraction(str(payload["eta"])) == ETA,
        "maximum_subdivisions": int(payload["maximum_subdivisions"])
        == MAX_SUBDIVISIONS,
        "configurations": protocol_configurations == code_configurations,
        "output_stem": payload.get("output_stem") == "exact_closed_cover_r053",
    }
    if not all(checks.values()):
        raise SystemExit(f"R053 code/protocol mismatch: {checks}")
    return payload


def _direction_metrics(
    exact_edges: Sequence[Fraction],
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    subdivisions: int,
    target_min_width: Fraction,
    inverse: bool,
) -> dict[str, object]:
    """Compute exact metrics for one source cell and one map direction."""

    source_area = (source_x[1] - source_x[0]) * (source_y[1] - source_y[0])
    exact_area = Fraction(0, 1)
    exact_inside = True
    target_classes: dict[int, bool] = {}
    half_open_targets: set[int] = set()
    maximum_outward = Fraction(0, 1)
    maximum_quadratic_variation = Fraction(0, 1)
    local_bound_pass = True

    for index in range(subdivisions):
        exact = exact_slab_bounds(source_x, source_y, index, subdivisions, inverse)
        rectangle_area = (exact[1] - exact[0]) * (exact[3] - exact[2])
        if rectangle_area < 0:
            raise AssertionError("exact image rectangle has negative area")
        exact_area += rectangle_area
        exact_inside = exact_inside and (
            exact[0] >= -RADIUS
            and exact[1] <= RADIUS
            and exact[2] >= -RADIUS
            and exact[3] <= RADIUS
        )
        maximum_outward = max(
            maximum_outward,
            -RADIUS - exact[0],
            exact[1] - RADIUS,
            -RADIUS - exact[2],
            exact[3] - RADIUS,
            Fraction(0, 1),
        )
        slab_classes = rectangle_target_classes(exact_edges, exact)
        for target_id, positive_area in slab_classes.items():
            target_classes[target_id] = target_classes.get(target_id, False) or positive_area
        half_open_targets.update(
            rectangle_target_cells(exact_edges, exact, closed=False)
        )
        cross_width = (
            source_x[1] - source_x[0]
            if inverse
            else source_y[1] - source_y[0]
        )
        image_nonlinear_width = (
            exact[3] - exact[2] if inverse else exact[1] - exact[0]
        )
        quadratic_variation = image_nonlinear_width - cross_width
        if quadratic_variation < 0:
            raise AssertionError("negative exact quadratic variation")
        maximum_quadratic_variation = max(
            maximum_quadratic_variation, quadratic_variation
        )
        local_bound_pass = local_bound_pass and (
            quadratic_variation <= ETA * target_min_width
        )

    closed_targets = set(target_classes)
    positive_area_targets = {
        target_id for target_id, positive in target_classes.items() if positive
    }
    touch_only_targets = closed_targets - positive_area_targets
    closed_dominates = half_open_targets <= closed_targets
    if not closed_dominates:
        raise AssertionError("closed target set failed to contain half-open control")
    positive_area_dominates = positive_area_targets <= half_open_targets
    if not positive_area_dominates:
        raise AssertionError("half-open target set omitted a positive-area incidence")
    return {
        "area_ratio": exact_area / source_area,
        "inside": exact_inside,
        "closed_target_count": len(closed_targets),
        "positive_area_target_count": len(positive_area_targets),
        "touch_only_target_count": len(touch_only_targets),
        "target_classes": target_classes,
        "half_open_target_count": len(half_open_targets),
        "closed_minus_half_open_target_count": len(closed_targets - half_open_targets),
        "closed_dominates_half_open": closed_dominates,
        "half_open_minus_positive_area_target_count": len(
            half_open_targets - positive_area_targets
        ),
        "positive_area_subset_half_open": positive_area_dominates,
        "maximum_outward_excursion": maximum_outward,
        "maximum_quadratic_variation": maximum_quadratic_variation,
        "local_bound_pass": local_bound_pass,
    }


def summarize_configuration(
    name: str, grid: int, offset: Fraction
) -> dict[str, object]:
    """Evaluate one frozen R053 configuration entirely over rational geometry."""

    exact_edges = exact_edge_vector(RADIUS, grid, offset)
    float_edges = float_edge_vector(float(RADIUS), grid, float(offset))
    exact_widths = [upper - lower for lower, upper in zip(exact_edges, exact_edges[1:])]
    exact_min_width = min(exact_widths)
    float_min_width = float(np.min(np.diff(float_edges)))
    edge_integrity_pass = (
        exact_edges[0] == -RADIUS
        and exact_edges[-1] == RADIUS
        and all(upper > lower for lower, upper in zip(exact_edges, exact_edges[1:]))
    )

    exact_uncapped_k = [
        uncapped_adaptive_subdivisions_exact(
            exact_edges[index], exact_edges[index + 1], exact_min_width
        )
        for index in range(grid)
    ]
    exact_k = [min(MAX_SUBDIVISIONS, value) for value in exact_uncapped_k]
    float_k = [
        float_adaptive_subdivisions(
            float(float_edges[index]),
            float(float_edges[index + 1]),
            float_min_width,
        )
        for index in range(grid)
    ]
    k_mismatch_indices = [
        index
        for index, (exact_value, float_value) in enumerate(zip(exact_k, float_k))
        if exact_value != float_value
    ]

    forward_ratios: list[Fraction] = []
    backward_ratios: list[Fraction] = []
    forward_fixed_k16_ratios: list[Fraction] = []
    backward_fixed_k16_ratios: list[Fraction] = []
    forward_closed_counts: list[Fraction] = []
    backward_closed_counts: list[Fraction] = []
    forward_half_open_counts: list[Fraction] = []
    backward_half_open_counts: list[Fraction] = []
    forward_inside = 0
    backward_inside = 0
    two_sided_inside = 0
    closed_dominance_pass = True
    positive_area_half_open_subset_pass = True
    local_bound_pass = True
    maximum_quadratic_variation = Fraction(0, 1)
    b1_contains_exact = True
    b1_violation_count = 0
    b1_comparison_count = 0
    b1_minimum_margin: Fraction | None = None
    maximum_outward = Fraction(0, 1)
    closed_extra_total = 0
    closed_extra_max = 0
    half_open_touch_total = 0
    half_open_touch_max = 0
    forward_closed_adjacency_count = 0
    backward_closed_adjacency_count = 0
    forward_positive_area_adjacency_count = 0
    backward_positive_area_adjacency_count = 0
    forward_touch_only_adjacency_count = 0
    backward_touch_only_adjacency_count = 0
    forward_adjacency_digest = hashlib.sha256()
    backward_adjacency_digest = hashlib.sha256()

    for y_index in range(grid):
        source_y = (exact_edges[y_index], exact_edges[y_index + 1])
        float_source_y = (float(float_edges[y_index]), float(float_edges[y_index + 1]))
        for x_index in range(grid):
            source_id = y_index * grid + x_index
            source_x = (exact_edges[x_index], exact_edges[x_index + 1])
            float_source_x = (
                float(float_edges[x_index]),
                float(float_edges[x_index + 1]),
            )
            forward = _direction_metrics(
                exact_edges,
                source_x,
                source_y,
                exact_k[x_index],
                exact_min_width,
                False,
            )
            backward = _direction_metrics(
                exact_edges,
                source_x,
                source_y,
                exact_k[y_index],
                exact_min_width,
                True,
            )
            forward_ratios.append(forward["area_ratio"])
            backward_ratios.append(backward["area_ratio"])
            forward_fixed_k16_ratios.append(
                exact_area_ratio(source_x, source_y, 16, False)
            )
            backward_fixed_k16_ratios.append(
                exact_area_ratio(source_x, source_y, 16, True)
            )
            forward_closed_counts.append(Fraction(forward["closed_target_count"], 1))
            backward_closed_counts.append(Fraction(backward["closed_target_count"], 1))
            forward_half_open_counts.append(
                Fraction(forward["half_open_target_count"], 1)
            )
            backward_half_open_counts.append(
                Fraction(backward["half_open_target_count"], 1)
            )
            forward_inside += int(forward["inside"])
            backward_inside += int(backward["inside"])
            two_sided_inside += int(forward["inside"] and backward["inside"])
            closed_dominance_pass = closed_dominance_pass and bool(
                forward["closed_dominates_half_open"]
                and backward["closed_dominates_half_open"]
            )
            positive_area_half_open_subset_pass = (
                positive_area_half_open_subset_pass
                and bool(forward["positive_area_subset_half_open"])
                and bool(backward["positive_area_subset_half_open"])
            )
            for metrics in (forward, backward):
                maximum_outward = max(
                    maximum_outward, metrics["maximum_outward_excursion"]
                )
                maximum_quadratic_variation = max(
                    maximum_quadratic_variation,
                    metrics["maximum_quadratic_variation"],
                )
                local_bound_pass = local_bound_pass and bool(
                    metrics["local_bound_pass"]
                )
                extra = int(metrics["closed_minus_half_open_target_count"])
                closed_extra_total += extra
                closed_extra_max = max(closed_extra_max, extra)
                half_open_touch = int(
                    metrics["half_open_minus_positive_area_target_count"]
                )
                half_open_touch_total += half_open_touch
                half_open_touch_max = max(half_open_touch_max, half_open_touch)

            forward_classes = forward["target_classes"]
            backward_classes = backward["target_classes"]
            update_adjacency_hash(
                forward_adjacency_digest, "F", source_id, forward_classes
            )
            update_adjacency_hash(
                backward_adjacency_digest, "B", source_id, backward_classes
            )
            forward_closed_adjacency_count += len(forward_classes)
            backward_closed_adjacency_count += len(backward_classes)
            forward_positive_area_adjacency_count += sum(forward_classes.values())
            backward_positive_area_adjacency_count += sum(backward_classes.values())
            forward_touch_only_adjacency_count += sum(
                not positive for positive in forward_classes.values()
            )
            backward_touch_only_adjacency_count += sum(
                not positive for positive in backward_classes.values()
            )

            forward_b1 = binary_float_endpoint_audit(
                float_source_x, float_source_y, float_k[x_index], False
            )
            backward_b1 = binary_float_endpoint_audit(
                float_source_x, float_source_y, float_k[y_index], True
            )
            for bridge in (forward_b1, backward_b1):
                b1_contains_exact = b1_contains_exact and bool(bridge["contains"])
                b1_violation_count += int(bridge["violation_count"])
                b1_comparison_count += int(bridge["comparison_count"])
                margin = bridge["minimum_margin"]
                b1_minimum_margin = (
                    margin
                    if b1_minimum_margin is None
                    else min(b1_minimum_margin, margin)
                )

    forward_ratio_stats = exact_statistics(forward_ratios)
    backward_ratio_stats = exact_statistics(backward_ratios)
    forward_fixed_stats = exact_statistics(forward_fixed_k16_ratios)
    backward_fixed_stats = exact_statistics(backward_fixed_k16_ratios)
    total = grid * grid
    cap_active_count = sum(value > MAX_SUBDIVISIONS for value in exact_uncapped_k)
    at_cap_count = sum(value == MAX_SUBDIVISIONS for value in exact_uncapped_k)
    exact_k_stats = exact_statistics(Fraction(value, 1) for value in exact_k)
    area_bound_pass = (
        forward_ratio_stats.maximum <= AREA_RATIO_BOUND
        and backward_ratio_stats.maximum <= AREA_RATIO_BOUND
    )
    cap_integrity_pass = cap_active_count == 0
    x3_exact_bound_pass = cap_integrity_pass and local_bound_pass and area_bound_pass
    fixed_k16_comparison_pass = (
        forward_ratio_stats.median <= forward_fixed_stats.median
        and backward_ratio_stats.median <= backward_fixed_stats.median
    )
    reversibility_multiset_pass = sorted(forward_ratios) == sorted(backward_ratios)
    forward_ratio_hash = exact_multiset_hash(forward_ratios)
    backward_ratio_hash = exact_multiset_hash(backward_ratios)
    exact_k_hash = exact_multiset_hash(Fraction(value, 1) for value in exact_k)

    record: dict[str, object] = {
        "configuration": name,
        "box": "main",
        "radius": float(RADIUS),
        "radius_fraction": fraction_text(RADIUS),
        "a": int(A_VALUE),
        "a_fraction": fraction_text(A_VALUE),
        "grid": grid,
        "grid_offset": float(offset),
        "grid_offset_fraction": fraction_text(offset),
        "state_count": total,
        "minimum_cell_width": float(exact_min_width),
        "minimum_cell_width_fraction": fraction_text(exact_min_width),
        "adaptive_eta": float(ETA),
        "adaptive_eta_fraction": fraction_text(ETA),
        "maximum_subdivisions": MAX_SUBDIVISIONS,
        "adaptive_k_float_agreement_pass": not k_mismatch_indices,
        "adaptive_k_float_mismatch_count": len(k_mismatch_indices),
        "adaptive_k_float_mismatch_indices": k_mismatch_indices,
        "adaptive_k_cap_active_count_1d": cap_active_count,
        "adaptive_k_cap_active_fraction_1d": cap_active_count / grid,
        "adaptive_k_cap_contact_count_1d": at_cap_count,
        "adaptive_k_cap_contact_fraction_1d": at_cap_count / grid,
        "adaptive_k_uncapped_max": max(exact_uncapped_k),
        "adaptive_k_cap_headroom": MAX_SUBDIVISIONS - max(exact_uncapped_k),
        "exact_edge_integrity_pass": edge_integrity_pass,
        "exact_edge_and_cap_integrity_pass": edge_integrity_pass
        and cap_integrity_pass,
        "forward_exact_in_box_fraction": forward_inside / total,
        "backward_exact_in_box_fraction": backward_inside / total,
        "two_sided_exact_in_box_fraction": two_sided_inside / total,
        "exact_area_ratio_bound": float(AREA_RATIO_BOUND),
        "exact_area_ratio_bound_fraction": fraction_text(AREA_RATIO_BOUND),
        "exact_area_ratio_bound_pass": area_bound_pass,
        "exact_local_slab_bound_pass": local_bound_pass,
        "exact_local_slab_bound": float(ETA * exact_min_width),
        "exact_local_slab_bound_fraction": fraction_text(ETA * exact_min_width),
        "maximum_exact_slab_quadratic_variation": float(
            maximum_quadratic_variation
        ),
        "maximum_exact_slab_quadratic_variation_fraction": fraction_text(
            maximum_quadratic_variation
        ),
        "x3_exact_local_global_bound_pass": x3_exact_bound_pass,
        "exact_adaptive_no_worse_than_fixed_k16_median_pass": fixed_k16_comparison_pass,
        "forward_exact_adaptive_minus_fixed_k16_median": float(
            forward_ratio_stats.median - forward_fixed_stats.median
        ),
        "forward_exact_adaptive_minus_fixed_k16_median_fraction": fraction_text(
            forward_ratio_stats.median - forward_fixed_stats.median
        ),
        "backward_exact_adaptive_minus_fixed_k16_median": float(
            backward_ratio_stats.median - backward_fixed_stats.median
        ),
        "backward_exact_adaptive_minus_fixed_k16_median_fraction": fraction_text(
            backward_ratio_stats.median - backward_fixed_stats.median
        ),
        "closed_cover_dominance_pass": closed_dominance_pass,
        "positive_area_subset_of_half_open_reference_pass": positive_area_half_open_subset_pass,
        "closed_minus_half_open_target_count_total": closed_extra_total,
        "closed_minus_half_open_target_count_max": closed_extra_max,
        "half_open_minus_positive_area_target_count_total": half_open_touch_total,
        "half_open_minus_positive_area_target_count_max": half_open_touch_max,
        "forward_closed_adjacency_count": forward_closed_adjacency_count,
        "backward_closed_adjacency_count": backward_closed_adjacency_count,
        "forward_positive_area_adjacency_count": forward_positive_area_adjacency_count,
        "backward_positive_area_adjacency_count": backward_positive_area_adjacency_count,
        "forward_touch_only_adjacency_count": forward_touch_only_adjacency_count,
        "backward_touch_only_adjacency_count": backward_touch_only_adjacency_count,
        "forward_closed_adjacency_sha256": forward_adjacency_digest.hexdigest(),
        "backward_closed_adjacency_sha256": backward_adjacency_digest.hexdigest(),
        "adjacency_hash_format": "ASCII direction,source_id,target_id,P|T\\n; source and target row-major",
        "b1_one_ulp_binary_exact_containment_pass": b1_contains_exact,
        "b1_one_ulp_binary_exact_violation_count": b1_violation_count,
        "b1_one_ulp_binary_exact_comparison_count": b1_comparison_count,
        "b1_minimum_one_ulp_binary_exact_margin": (
            float(b1_minimum_margin)
            if b1_minimum_margin is not None
            else None
        ),
        "b1_minimum_one_ulp_binary_exact_margin_fraction": (
            fraction_text(b1_minimum_margin)
            if b1_minimum_margin is not None
            else None
        ),
        "maximum_exact_outward_excursion": float(maximum_outward),
        "maximum_exact_outward_excursion_fraction": fraction_text(maximum_outward),
        "forward_inverse_exact_area_multisets_equal": reversibility_multiset_pass,
        "forward_exact_area_ratio_multiset_sha256": forward_ratio_hash,
        "backward_exact_area_ratio_multiset_sha256": backward_ratio_hash,
        "adaptive_k_exact_multiset_sha256": exact_k_hash,
        "exact_rational_geometry": True,
        "closed_target_intersection_semantics": True,
    }
    record.update(_statistics_fields("adaptive_k_exact", exact_k_stats))
    record.update(_statistics_fields("forward_exact_area_ratio", forward_ratio_stats))
    record.update(_statistics_fields("backward_exact_area_ratio", backward_ratio_stats))
    record.update(
        _statistics_fields("forward_fixed_k16_exact_area_ratio", forward_fixed_stats)
    )
    record.update(
        _statistics_fields("backward_fixed_k16_exact_area_ratio", backward_fixed_stats)
    )
    record.update(
        _statistics_fields(
            "forward_closed_target_count", exact_statistics(forward_closed_counts)
        )
    )
    record.update(
        _statistics_fields(
            "backward_closed_target_count", exact_statistics(backward_closed_counts)
        )
    )
    record.update(
        _statistics_fields(
            "forward_half_open_target_count",
            exact_statistics(forward_half_open_counts),
        )
    )
    record.update(
        _statistics_fields(
            "backward_half_open_target_count",
            exact_statistics(backward_half_open_counts),
        )
    )
    return record


def _selected_configurations(names: Sequence[str] | None) -> list[tuple[str, int, Fraction]]:
    if not names:
        return list(CONFIGURATIONS)
    requested = set(names)
    return [configuration for configuration in CONFIGURATIONS if configuration[0] in requested]


def main() -> None:
    args = parse_args()
    if not MANIFEST.is_file():
        raise SystemExit(
            "R053 production is disabled until the frozen manifest exists at "
            f"{MANIFEST}"
        )
    protocol = validate_frozen_protocol()
    if args.workers <= 0:
        raise SystemExit("--workers must be positive")
    configurations = _selected_configurations(args.configuration)
    if args.configuration and args.output_stem == "exact_closed_cover_r053":
        selected_names = {name for name, _, _ in configurations}
        frozen_names = {name for name, _, _ in CONFIGURATIONS}
        if selected_names != frozen_names:
            raise SystemExit(
                "refusing to overwrite the canonical R053 output with a "
                "partial configuration selection; pass a distinct --output-stem"
            )
    workers = min(args.workers, len(configurations))
    if workers == 1:
        records = [summarize_configuration(*configuration) for configuration in configurations]
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            records = list(executor.map(_summarize_tuple, configurations))

    payload = {
        "run_id": "R053_EXACT_CLOSED_COVER",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "manifest": str(MANIFEST.relative_to(PROJECT_ROOT)),
        "protocol": str(PROTOCOL.relative_to(PROJECT_ROOT)),
        "protocol_frozen_utc": protocol["frozen_utc"],
        "a_fraction": fraction_text(A_VALUE),
        "radius_fraction": fraction_text(RADIUS),
        "eta_fraction": fraction_text(ETA),
        "maximum_subdivisions": MAX_SUBDIVISIONS,
        "records": records,
        "scope": (
            "exact finite-resolution rational strip-image enclosures with "
            "closed-cell target enumeration; not an invariant-set, Markov, "
            "or transfer-operator convergence certificate"
        ),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
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
                "configurations": [record["configuration"] for record in records],
                "workers": workers,
            },
            indent=2,
        )
    )


def _summarize_tuple(configuration: tuple[str, int, Fraction]) -> dict[str, object]:
    """Pickle-friendly adapter for configuration-level multiprocessing."""

    return summarize_configuration(*configuration)


if __name__ == "__main__":
    main()
