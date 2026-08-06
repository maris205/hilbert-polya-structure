#!/usr/bin/env python3
"""Independent exact checker for the frozen R056 refinement audit.

This module intentionally does not import any R053--R056 producer geometry,
target-indexing, incidence, candidate-hull, or SCC helper.  It reconstructs
the Hénon true-image predicate and the adaptive slab outer rectangles from the
frozen JSON protocol using :class:`fractions.Fraction`, exhaustively checks two
microgrids, and brute-forces every target cell for the protocol-fixed 64
sources in each held-out configuration.

The persisted compressed arrays are loaded with ``allow_pickle=False``.  Their
canonical set differences are recomputed here rather than trusting producer
counts or hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R056_TRUE_IMAGE_REFINEMENT_PROTOCOL.json"
)
DEFAULT_INPUT = PROJECT_ROOT / "results" / "true_image_refinement_r056.json"
DEFAULT_OUTPUT = (
    PROJECT_ROOT
    / "results"
    / "true_image_refinement_independent_check_r056.json"
)

EDGE_ARRAY_KEYS = (
    "true_forward_edges",
    "true_backward_edges",
    "outer_forward_edges",
    "outer_backward_edges",
)
NODE_ARRAY_KEYS = ("active_node_ids", "analytic_active_node_ids", "k_values")
LCG_MULTIPLIER = 2_654_435_761
LCG_INCREMENT = 1_013_904_223


@dataclass(frozen=True)
class Constants:
    a: Fraction
    radius: Fraction
    eta: Fraction
    maximum_subdivisions: int


@dataclass
class EdgeArtifact:
    path: Path
    arrays: dict[str, np.ndarray]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--protocol", type=Path, default=PROTOCOL_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--serial-artifact",
        type=Path,
        default=None,
        help="Optional workers=1 n127_d0 NPZ or result JSON replay artifact.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Independent fixed-source worker processes (default: 1).",
    )
    return parser.parse_args()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def parse_fraction(value: object) -> Fraction:
    return Fraction(str(value))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def node_hash(nodes: Iterable[int]) -> str:
    digest = hashlib.sha256()
    for node in sorted(nodes):
        digest.update(f"{node}\n".encode("ascii"))
    return digest.hexdigest()


def labelled_edge_hash(edges: Iterable[tuple[int, int, int]], direction: str) -> str:
    if direction not in {"F", "B"}:
        raise ValueError("direction must be F or B")
    digest = hashlib.sha256()
    for source, target, positive in sorted(edges):
        label = "P" if positive else "T"
        digest.update(f"{direction},{source},{target},{label}\n".encode("ascii"))
    return digest.hexdigest()


def load_protocol(path: Path = PROTOCOL_PATH) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("run_id") != "R056_TRUE_IMAGE_REFINEMENT":
        raise AssertionError("unexpected R056 protocol run_id")
    if payload.get("status") != "FROZEN_BEFORE_HELDOUT_PRODUCTION":
        raise AssertionError("R056 protocol is not frozen before production")
    heldouts = payload.get("heldout_configurations")
    if not isinstance(heldouts, list) or len(heldouts) != 6:
        raise AssertionError("R056 protocol must contain exactly six held-outs")
    checker = payload.get("independent_checker")
    if not isinstance(checker, dict):
        raise AssertionError("R056 independent-checker block is missing")
    if checker.get("may_import_producer_geometry_or_scc_helpers") is not False:
        raise AssertionError("R056 independent checker import policy changed")
    if int(checker.get("heldout_source_sweep_count_per_configuration", -1)) != 64:
        raise AssertionError("R056 fixed-source sweep count changed")
    microgrids = checker.get("microgrid_full_sweeps")
    if not isinstance(microgrids, list):
        raise AssertionError("R056 microgrid schedule is missing")
    observed_microgrids = [
        (int(item["grid"]), parse_fraction(item["grid_offset"]))
        for item in microgrids
    ]
    if observed_microgrids != [(7, Fraction(0)), (8, Fraction(1, 3))]:
        raise AssertionError("R056 frozen microgrid schedule changed")
    schedule = checker.get("source_id_schedule")
    if not isinstance(schedule, Mapping):
        raise AssertionError("R056 fixed-source schedule is missing")
    expected_coordinates = [
        ["0", "0"],
        ["N-1", "0"],
        ["0", "N-1"],
        ["N-1", "N-1"],
        ["floor(N/2)", "0"],
        ["floor(N/2)", "N-1"],
        ["0", "floor(N/2)"],
        ["N-1", "floor(N/2)"],
        ["floor(N/2)", "floor(N/2)"],
        ["floor(N/2)-1", "floor(N/2)"],
        ["floor(N/2)", "floor(N/2)-1"],
        ["floor(N/2)-1", "floor(N/2)-1"],
    ]
    if schedule.get("mandatory_xy_coordinates") != expected_coordinates:
        raise AssertionError("R056 mandatory fixed-source coordinates changed")
    expected_fill = (
        "Starting at k=0, append unseen row-major IDs "
        "(2654435761*k + 1013904223) mod N^2 until 64 unique IDs are present."
    )
    if schedule.get("fill_rule") != expected_fill:
        raise AssertionError("R056 fixed-source LCG fill rule changed")
    return payload


def constants_from_protocol(protocol: Mapping[str, object]) -> Constants:
    raw = protocol.get("constants")
    if not isinstance(raw, Mapping):
        raise AssertionError("protocol constants block is missing")
    constants = Constants(
        a=parse_fraction(raw["a"]),
        radius=parse_fraction(raw["radius"]),
        eta=parse_fraction(raw["eta"]),
        maximum_subdivisions=int(raw["maximum_subdivisions"]),
    )
    if constants.a < 0 or constants.radius <= 0 or constants.eta <= 0:
        raise AssertionError("invalid frozen exact constants")
    return constants


def make_edges(radius: Fraction, grid: int, offset: Fraction) -> tuple[Fraction, ...]:
    """Construct the clipped shifted partition independently."""

    if grid <= 0:
        raise ValueError("grid must be positive")
    if not Fraction(-1, 2) <= offset <= Fraction(1, 2):
        raise ValueError("offset must lie in [-1/2,1/2]")
    width = 2 * radius / grid
    edges = [-radius]
    edges.extend(
        -radius + (Fraction(index) + offset) * width
        for index in range(1, grid)
    )
    edges.append(radius)
    if any(right <= left for left, right in zip(edges, edges[1:])):
        raise AssertionError("independent edge vector is not strictly increasing")
    return tuple(edges)


def square_range(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    if upper < lower:
        raise ValueError("reversed interval")
    values = [lower * lower, upper * upper]
    if lower <= 0 <= upper:
        values.append(Fraction(0))
    return min(values), max(values)


def overlap_class(
    parameter: tuple[Fraction, Fraction],
    target_parameter: tuple[Fraction, Fraction],
    coefficient_lower: Fraction,
    coefficient_upper: Fraction,
    a_value: Fraction,
) -> bool | None:
    """Return positive-area, touch-only, or empty for the exact image test."""

    restricted_lower = max(parameter[0], target_parameter[0])
    restricted_upper = min(parameter[1], target_parameter[1])
    if restricted_upper < restricted_lower:
        return None
    squared_lower, squared_upper = square_range(
        restricted_lower, restricted_upper
    )
    quadratic_lower = a_value * squared_lower
    quadratic_upper = a_value * squared_upper
    overlap_lower = max(quadratic_lower, coefficient_lower)
    overlap_upper = min(quadratic_upper, coefficient_upper)
    if overlap_upper < overlap_lower:
        return None
    return restricted_upper > restricted_lower and overlap_upper > overlap_lower


def forward_true_class(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
    a_value: Fraction,
) -> bool | None:
    return overlap_class(
        source_x,
        target_y,
        1 - target_x[1] - source_y[1],
        1 - target_x[0] - source_y[0],
        a_value,
    )


def inverse_true_class(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
    a_value: Fraction,
) -> bool | None:
    return overlap_class(
        source_y,
        target_x,
        1 - target_y[1] - source_x[1],
        1 - target_y[0] - source_x[0],
        a_value,
    )


def true_predicate_diagnostic(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
    a_value: Fraction,
    *,
    inverse: bool,
) -> dict[str, object]:
    """Expose the exact intervals requested for a preserved counterexample."""

    parameter = source_y if inverse else source_x
    target_parameter = target_x if inverse else target_y
    restricted_lower = max(parameter[0], target_parameter[0])
    restricted_upper = min(parameter[1], target_parameter[1])
    coefficient = (
        (1 - target_y[1] - source_x[1], 1 - target_y[0] - source_x[0])
        if inverse
        else (1 - target_x[1] - source_y[1], 1 - target_x[0] - source_y[0])
    )
    if restricted_upper < restricted_lower:
        quadratic: tuple[Fraction, Fraction] | None = None
    else:
        lower_square, upper_square = square_range(
            restricted_lower, restricted_upper
        )
        quadratic = (a_value * lower_square, a_value * upper_square)
    return {
        "restricted_parameter_interval": [
            fraction_text(restricted_lower),
            fraction_text(restricted_upper),
        ],
        "restricted_parameter_nonempty": restricted_upper >= restricted_lower,
        "quadratic_range": (
            None if quadratic is None else list(map(fraction_text, quadratic))
        ),
        "coefficient_interval": list(map(fraction_text, coefficient)),
    }


def exact_ceiling(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def adaptive_count(
    lower: Fraction,
    upper: Fraction,
    minimum_width: Fraction,
    constants: Constants,
) -> int:
    maximum_abs = max(abs(lower), abs(upper))
    numerator = 2 * constants.a * maximum_abs * (upper - lower)
    if numerator == 0:
        return 1
    return max(1, exact_ceiling(numerator / (constants.eta * minimum_width)))


def slab_bounds(
    source_x: tuple[Fraction, Fraction],
    source_y: tuple[Fraction, Fraction],
    slab_index: int,
    subdivisions: int,
    inverse: bool,
    a_value: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Independently reconstruct one exact adaptive outer rectangle."""

    split_interval = source_y if inverse else source_x
    width = (split_interval[1] - split_interval[0]) / subdivisions
    lower = split_interval[0] + slab_index * width
    upper = split_interval[0] + (slab_index + 1) * width
    squared_lower, squared_upper = square_range(lower, upper)
    if inverse:
        return (
            lower,
            upper,
            1 - a_value * squared_upper - source_x[1],
            1 - a_value * squared_lower - source_x[0],
        )
    return (
        1 - a_value * squared_upper - source_y[1],
        1 - a_value * squared_lower - source_y[0],
        lower,
        upper,
    )


def rectangle_overlap_class(
    rectangle: tuple[Fraction, Fraction, Fraction, Fraction],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
) -> bool | None:
    x_lower = max(rectangle[0], target_x[0])
    x_upper = min(rectangle[1], target_x[1])
    if x_upper < x_lower:
        return None
    y_lower = max(rectangle[2], target_y[0])
    y_upper = min(rectangle[3], target_y[1])
    if y_upper < y_lower:
        return None
    return x_upper > x_lower and y_upper > y_lower


def outer_class_from_slabs(
    slabs: Sequence[tuple[Fraction, Fraction, Fraction, Fraction]],
    target_x: tuple[Fraction, Fraction],
    target_y: tuple[Fraction, Fraction],
) -> bool | None:
    touch = False
    for rectangle in slabs:
        classification = rectangle_overlap_class(rectangle, target_x, target_y)
        if classification is True:
            return True
        if classification is False:
            touch = True
    return False if touch else None


def fixed_source_ids(grid: int, count: int = 64) -> tuple[int, ...]:
    """Evaluate the protocol's mandatory coordinates and LCG fill rule."""

    if grid * grid < count:
        raise ValueError("grid has fewer cells than the fixed-source count")
    middle = grid // 2
    mandatory_xy = (
        (0, 0),
        (grid - 1, 0),
        (0, grid - 1),
        (grid - 1, grid - 1),
        (middle, 0),
        (middle, grid - 1),
        (0, middle),
        (grid - 1, middle),
        (middle, middle),
        (middle - 1, middle),
        (middle, middle - 1),
        (middle - 1, middle - 1),
    )
    selected: list[int] = []
    seen: set[int] = set()
    for x_index, y_index in mandatory_xy:
        node = y_index * grid + x_index
        if node not in seen:
            seen.add(node)
            selected.append(node)
    k_value = 0
    modulus = grid * grid
    while len(selected) < count:
        node = (LCG_MULTIPLIER * k_value + LCG_INCREMENT) % modulus
        k_value += 1
        if node not in seen:
            seen.add(node)
            selected.append(node)
    return tuple(selected)


def _cell_intervals(edges: Sequence[Fraction]) -> tuple[tuple[Fraction, Fraction], ...]:
    return tuple(zip(edges, edges[1:]))


def brute_force_source(
    edges: Sequence[Fraction],
    source_id: int,
    constants: Constants,
) -> dict[str, object]:
    """Brute-force all N^2 targets for one source in both directions."""

    grid = len(edges) - 1
    if not 0 <= source_id < grid * grid:
        raise ValueError("source_id is outside the grid")
    cells = _cell_intervals(edges)
    source_x = cells[source_id % grid]
    source_y = cells[source_id // grid]
    minimum_width = min(upper - lower for lower, upper in cells)
    forward_k = adaptive_count(*source_x, minimum_width, constants)
    backward_k = adaptive_count(*source_y, minimum_width, constants)
    if forward_k >= constants.maximum_subdivisions:
        raise AssertionError("independent forward K reached the frozen cap")
    if backward_k >= constants.maximum_subdivisions:
        raise AssertionError("independent backward K reached the frozen cap")
    forward_slabs = tuple(
        slab_bounds(source_x, source_y, index, forward_k, False, constants.a)
        for index in range(forward_k)
    )
    backward_slabs = tuple(
        slab_bounds(source_x, source_y, index, backward_k, True, constants.a)
        for index in range(backward_k)
    )
    output: dict[str, dict[int, int]] = {
        key: {} for key in EDGE_ARRAY_KEYS
    }
    for target_y_index, target_y in enumerate(cells):
        for target_x_index, target_x in enumerate(cells):
            target_id = target_y_index * grid + target_x_index
            true_forward = forward_true_class(
                source_x, source_y, target_x, target_y, constants.a
            )
            if true_forward is not None:
                output["true_forward_edges"][target_id] = int(true_forward)
            true_backward = inverse_true_class(
                source_x, source_y, target_x, target_y, constants.a
            )
            if true_backward is not None:
                output["true_backward_edges"][target_id] = int(true_backward)

            # These cheap exact parameter-axis rejects retain a literal all-
            # target sweep while avoiding irrelevant slab comparisons.
            if min(source_x[1], target_y[1]) >= max(source_x[0], target_y[0]):
                outer_forward = outer_class_from_slabs(
                    forward_slabs, target_x, target_y
                )
                if outer_forward is not None:
                    output["outer_forward_edges"][target_id] = int(outer_forward)
            if min(source_y[1], target_x[1]) >= max(source_y[0], target_x[0]):
                outer_backward = outer_class_from_slabs(
                    backward_slabs, target_x, target_y
                )
                if outer_backward is not None:
                    output["outer_backward_edges"][target_id] = int(outer_backward)
    return {
        **output,
        "forward_k": forward_k,
        "backward_k": backward_k,
        "source_bounds": tuple(map(fraction_text, (*source_x, *source_y))),
    }


def _maps_to_arrays(
    per_source: Sequence[Mapping[str, object]],
) -> dict[str, np.ndarray]:
    rows: dict[str, list[tuple[int, int, int]]] = {key: [] for key in EDGE_ARRAY_KEYS}
    for source, result in enumerate(per_source):
        for key in EDGE_ARRAY_KEYS:
            target_map = result[key]
            if not isinstance(target_map, Mapping):
                raise AssertionError("internal brute-force result has invalid edge map")
            rows[key].extend(
                (source, int(target), int(label))
                for target, label in sorted(target_map.items())
            )
    return {
        key: np.asarray(value, dtype=np.int64).reshape((-1, 3))
        for key, value in rows.items()
    }


def edge_set(array: np.ndarray, *, positive_only: bool = False) -> set[tuple[int, int, int]]:
    return {
        (int(source), int(target), int(positive))
        for source, target, positive in array
        if not positive_only or int(positive) == 1
    }


def pair_set(array: np.ndarray, *, positive_only: bool = False) -> set[tuple[int, int]]:
    return {
        (int(source), int(target))
        for source, target, positive in array
        if not positive_only or int(positive) == 1
    }


def recompute_edge_decisions(arrays: Mapping[str, np.ndarray]) -> dict[str, object]:
    """Recompute full-array identities and every exact symmetric difference."""

    true_forward = edge_set(arrays["true_forward_edges"])
    true_backward = edge_set(arrays["true_backward_edges"])
    outer_forward = edge_set(arrays["outer_forward_edges"])
    outer_backward = edge_set(arrays["outer_backward_edges"])
    outer_backward_reverse_pairs = {
        (target, source) for source, target, _ in outer_backward
    }
    outer_forward_reverse_pairs = {
        (target, source) for source, target, _ in outer_forward
    }
    mutual_forward = {
        edge for edge in outer_forward if edge[:2] in outer_backward_reverse_pairs
    }
    mutual_backward = {
        edge for edge in outer_backward if edge[:2] in outer_forward_reverse_pairs
    }
    transpose_forward = {
        (target, source, positive) for source, target, positive in true_forward
    }
    true_forward_positive = {
        edge for edge in true_forward if edge[2] == 1
    }
    true_backward_positive = {
        edge for edge in true_backward if edge[2] == 1
    }
    outer_forward_positive = {
        edge for edge in outer_forward if edge[2] == 1
    }
    outer_backward_positive = {
        edge for edge in outer_backward if edge[2] == 1
    }
    producer_aligned_differences = {
        "true_closed_mutual_outer_forward_symmetric_difference_count": len(
            {(source, target) for source, target, _ in true_forward}
            ^ {(source, target) for source, target, _ in mutual_forward}
        ),
        "true_closed_mutual_outer_backward_symmetric_difference_count": len(
            {(source, target) for source, target, _ in true_backward}
            ^ {(source, target) for source, target, _ in mutual_backward}
        ),
        "true_positive_outer_positive_forward_symmetric_difference_count": len(
            {(source, target) for source, target, _ in true_forward_positive}
            ^ {(source, target) for source, target, _ in outer_forward_positive}
        ),
        "true_positive_outer_positive_backward_symmetric_difference_count": len(
            {(source, target) for source, target, _ in true_backward_positive}
            ^ {(source, target) for source, target, _ in outer_backward_positive}
        ),
    }

    comparisons = {
        "true_forward_inverse_labelled_transpose": (
            transpose_forward,
            true_backward,
        ),
        "true_forward_equals_mutual_outer": (true_forward, mutual_forward),
        "true_backward_equals_mutual_outer": (true_backward, mutual_backward),
        "true_forward_positive_equals_outer_positive": (
            true_forward_positive,
            outer_forward_positive,
        ),
        "true_backward_positive_equals_outer_positive": (
            true_backward_positive,
            outer_backward_positive,
        ),
    }
    symmetric_differences = {
        name: len(left ^ right) for name, (left, right) in comparisons.items()
    }
    subset_differences = {
        "true_forward_minus_outer": len(true_forward - outer_forward),
        "true_backward_minus_outer": len(true_backward - outer_backward),
        "true_forward_positive_minus_outer_positive": len(
            true_forward_positive - outer_forward_positive
        ),
        "true_backward_positive_minus_outer_positive": len(
            true_backward_positive - outer_backward_positive
        ),
    }
    return {
        "symmetric_difference_counts": symmetric_differences,
        "producer_aligned_symmetric_difference_counts": producer_aligned_differences,
        "subset_difference_counts": subset_differences,
        "all_decision_set_differences_zero": not any(
            (
                *symmetric_differences.values(),
                *producer_aligned_differences.values(),
                *subset_differences.values(),
            )
        ),
    }


def run_microgrid_sweep(
    grid: int,
    offset: Fraction,
    constants: Constants,
) -> dict[str, object]:
    """Perform the protocol-required full N^4 independent sweep."""

    edges = make_edges(constants.radius, grid, offset)
    per_source = [
        brute_force_source(edges, source, constants)
        for source in range(grid * grid)
    ]
    arrays = _maps_to_arrays(per_source)
    decisions = recompute_edge_decisions(arrays)
    return {
        "grid": grid,
        "grid_offset_fraction": fraction_text(offset),
        "source_target_pair_count": grid**4,
        "edge_counts": {key: int(len(value)) for key, value in arrays.items()},
        "edge_hashes": {
            key: labelled_edge_hash(
                edge_set(value), "B" if "backward" in key else "F"
            )
            for key, value in arrays.items()
        },
        **decisions,
        "pass": bool(decisions["all_decision_set_differences_zero"]),
    }


def _validate_edge_array(key: str, array: np.ndarray, state_count: int) -> None:
    if array.dtype != np.dtype(np.int64):
        raise AssertionError(f"{key} must have exact int64 dtype")
    if array.ndim != 2 or array.shape[1] != 3:
        raise AssertionError(f"{key} must have shape (m,3)")
    if len(array) == 0:
        return
    if np.any(array[:, :2] < 0) or np.any(array[:, :2] >= state_count):
        raise AssertionError(f"{key} contains an out-of-range node ID")
    if not np.all((array[:, 2] == 0) | (array[:, 2] == 1)):
        raise AssertionError(f"{key} labels must be 0/1")
    order = np.lexsort((array[:, 2], array[:, 1], array[:, 0]))
    if not np.array_equal(order, np.arange(len(array))):
        raise AssertionError(f"{key} is not canonically lexicographically sorted")
    if len(array) > 1 and np.any(np.all(array[1:, :2] == array[:-1, :2], axis=1)):
        raise AssertionError(f"{key} contains duplicate source-target pairs")


def _validate_node_array(key: str, array: np.ndarray, upper: int) -> None:
    if array.dtype != np.dtype(np.int64) or array.ndim != 1:
        raise AssertionError(f"{key} must be a one-dimensional int64 array")
    if len(array) and (np.any(array < 0) or np.any(array >= upper)):
        raise AssertionError(f"{key} contains out-of-range values")
    if len(array) > 1 and np.any(array[1:] <= array[:-1]):
        raise AssertionError(f"{key} must be strictly increasing")


def load_edge_artifact(path: Path, grid: int) -> EdgeArtifact:
    """Load and validate a producer NPZ without permitting Python objects."""

    with np.load(path, allow_pickle=False) as archive:
        # ``k_values`` is the frozen public schema name.  Accept the producer's
        # more explicit ``uncapped_k_values`` spelling as a compatibility alias
        # while always exposing the canonical key to the rest of this checker.
        k_source = (
            "k_values" if "k_values" in archive.files else "uncapped_k_values"
        )
        required = set((*EDGE_ARRAY_KEYS, "active_node_ids", "analytic_active_node_ids"))
        missing = required - set(archive.files)
        if k_source not in archive.files:
            missing.add("k_values")
        if missing:
            raise AssertionError(f"{path} is missing arrays: {sorted(missing)}")
        # Access every stored array under the no-pickle policy, including
        # nondecision recurrent-node arrays, so an object-dtype side channel
        # cannot hide in an otherwise valid archive.
        for archive_key in archive.files:
            if archive[archive_key].dtype.hasobject:
                raise AssertionError(f"{path}:{archive_key} has object dtype")
        arrays = {
            key: np.array(archive[key], copy=True)
            for key in (*EDGE_ARRAY_KEYS, "active_node_ids", "analytic_active_node_ids")
        }
        arrays["k_values"] = np.array(archive[k_source], copy=True)
    state_count = grid * grid
    for key in EDGE_ARRAY_KEYS:
        _validate_edge_array(key, arrays[key], state_count)
    _validate_node_array("active_node_ids", arrays["active_node_ids"], state_count)
    _validate_node_array(
        "analytic_active_node_ids", arrays["analytic_active_node_ids"], state_count
    )
    if not np.array_equal(
        arrays["active_node_ids"], arrays["analytic_active_node_ids"]
    ):
        raise AssertionError("slab and analytic active-node arrays differ")
    k_values = arrays["k_values"]
    if k_values.dtype != np.dtype(np.int64) or k_values.shape != (grid,):
        raise AssertionError("k_values must be an int64 vector of length grid")
    if np.any(k_values <= 0):
        raise AssertionError("k_values must be positive")
    return EdgeArtifact(path=path, arrays=arrays)


def _records(payload: Mapping[str, object]) -> list[dict[str, object]]:
    combined: list[dict[str, object]] = []
    for key in ("records", "heldout_records", "anchor_records"):
        value = payload.get(key)
        if isinstance(value, list):
            combined.extend(item for item in value if isinstance(item, dict))
    if not combined:
        raise AssertionError("R056 payload has no configuration records")
    return combined


def records_by_configuration(
    payload: Mapping[str, object],
) -> dict[str, dict[str, object]]:
    output: dict[str, dict[str, object]] = {}
    for record in _records(payload):
        name = record.get("configuration_id", record.get("configuration"))
        if not isinstance(name, str):
            raise AssertionError("configuration record has no ID")
        if name in output:
            # Some payloads expose ``records`` as the concatenation of named
            # anchor/held-out lists.  An identical object is harmless.
            if output[name] != record:
                raise AssertionError(f"duplicate nonidentical record {name}")
            continue
        output[name] = record
    return output


def resolve_artifact_path(record: Mapping[str, object]) -> Path:
    raw = record.get("edge_array_path")
    if not isinstance(raw, str):
        raise AssertionError("configuration record lacks edge_array_path")
    path = Path(raw)
    return path if path.is_absolute() else PROJECT_ROOT / path


def _optional_record_consistency(
    record: Mapping[str, object], artifact: EdgeArtifact
) -> dict[str, bool]:
    arrays = artifact.arrays
    checks: dict[str, bool] = {}
    count_fields = {
        "true_forward_closed_edge_count": "true_forward_edges",
        "true_backward_closed_edge_count": "true_backward_edges",
        "outer_forward_closed_edge_count": "outer_forward_edges",
        "outer_backward_closed_edge_count": "outer_backward_edges",
    }
    positive_fields = {
        "true_forward_positive_edge_count": "true_forward_edges",
        "true_backward_positive_edge_count": "true_backward_edges",
        "outer_forward_positive_edge_count": "outer_forward_edges",
        "outer_backward_positive_edge_count": "outer_backward_edges",
    }
    for field, key in count_fields.items():
        if field in record:
            checks[field] = int(record[field]) == len(arrays[key])
    for field, key in positive_fields.items():
        if field in record:
            checks[field] = int(record[field]) == int(np.count_nonzero(arrays[key][:, 2]))
    if "two_sided_in_box_node_count" in record:
        checks["two_sided_in_box_node_count"] = int(
            record["two_sided_in_box_node_count"]
        ) == len(arrays["active_node_ids"])
    if "two_sided_in_box_node_ids_sha256" in record:
        checks["two_sided_in_box_node_ids_sha256"] = (
            str(record["two_sided_in_box_node_ids_sha256"])
            == node_hash(map(int, arrays["active_node_ids"]))
        )
    if "active_node_count" in record:
        checks["active_node_count"] = int(record["active_node_count"]) == len(
            arrays["active_node_ids"]
        )
    if "active_node_ids_sha256" in record:
        checks["active_node_ids_sha256"] = str(
            record["active_node_ids_sha256"]
        ) == node_hash(map(int, arrays["active_node_ids"]))
    if "analytic_active_node_count" in record:
        checks["analytic_active_node_count"] = int(
            record["analytic_active_node_count"]
        ) == len(arrays["analytic_active_node_ids"])
    if "analytic_active_node_ids_sha256" in record:
        checks["analytic_active_node_ids_sha256"] = str(
            record["analytic_active_node_ids_sha256"]
        ) == node_hash(map(int, arrays["analytic_active_node_ids"]))
    if "uncapped_k_max" in record:
        checks["uncapped_k_max"] = int(record["uncapped_k_max"]) == int(
            arrays["k_values"].max()
        )
    if "uncapped_k_min" in record:
        checks["uncapped_k_min"] = int(record["uncapped_k_min"]) == int(
            arrays["k_values"].min()
        )
    hash_fields = {
        "true_forward_labelled_edge_hash": ("true_forward_edges", "F"),
        "true_backward_labelled_edge_hash": ("true_backward_edges", "B"),
        "outer_forward_labelled_edge_hash": ("outer_forward_edges", "F"),
        "outer_backward_labelled_edge_hash": ("outer_backward_edges", "B"),
    }
    for field, (key, direction) in hash_fields.items():
        if field in record:
            checks[field] = str(record[field]) == labelled_edge_hash(
                edge_set(arrays[key]), direction
            )
    return checks


def validate_persisted_payload(
    payload: Mapping[str, object], protocol: Mapping[str, object]
) -> tuple[dict[str, EdgeArtifact], dict[str, object]]:
    if payload.get("run_id") != "R056_TRUE_IMAGE_REFINEMENT":
        raise AssertionError("unexpected R056 result run_id")
    by_name = records_by_configuration(payload)
    expected = {
        str(item["configuration_id"]): item
        for block in ("development_anchors", "heldout_configurations")
        for item in protocol[block]  # type: ignore[index]
    }
    if not set(expected) <= set(by_name):
        raise AssertionError("R056 payload is missing frozen held-out records")
    artifacts: dict[str, EdgeArtifact] = {}
    record_checks: dict[str, object] = {}
    for name, configuration in expected.items():
        record = by_name[name]
        grid = int(configuration["grid"])
        if int(record.get("grid", -1)) != grid:
            raise AssertionError(f"{name} grid disagrees with the protocol")
        if parse_fraction(record.get("grid_offset_fraction", record.get("grid_offset"))) != parse_fraction(
            configuration["grid_offset"]
        ):
            raise AssertionError(f"{name} offset disagrees with the protocol")
        edge_schema = record.get("edge_array_schema")
        expected_schema = {
            "edge_columns": ["source_id", "target_id", "positive_flag"],
            "edge_dtype": "int64",
            "node_dtype": "int64",
            "allow_pickle": False,
        }
        if edge_schema != expected_schema:
            raise AssertionError(f"{name} edge_array_schema is not canonical")
        artifact_path = resolve_artifact_path(record)
        expected_sha = record.get("edge_array_sha256")
        if not isinstance(expected_sha, str) or sha256_file(artifact_path) != expected_sha:
            raise AssertionError(f"{name} edge artifact SHA-256 mismatch")
        artifact = load_edge_artifact(artifact_path, grid)
        consistency = _optional_record_consistency(record, artifact)
        if not all(consistency.values()):
            raise AssertionError(f"{name} persisted counts/hashes disagree with NPZ")
        decisions = recompute_edge_decisions(artifact.arrays)
        aligned = decisions["producer_aligned_symmetric_difference_counts"]
        subsets = decisions["subset_difference_counts"]
        symmetric = decisions["symmetric_difference_counts"]
        if not isinstance(aligned, Mapping) or not isinstance(subsets, Mapping):
            raise AssertionError("internal decision-difference schema failure")
        if not isinstance(symmetric, Mapping):
            raise AssertionError("internal transpose-difference schema failure")
        reported_decision_checks: dict[str, bool] = {}
        for field, expected_value in aligned.items():
            if field in record:
                reported_decision_checks[field] = int(record[field]) == int(
                    expected_value
                )
        reported_pass_expectations = {
            "true_closed_equals_mutual_outer_forward_pass": int(
                aligned[
                    "true_closed_mutual_outer_forward_symmetric_difference_count"
                ]
            )
            == 0,
            "true_closed_equals_mutual_outer_backward_pass": int(
                aligned[
                    "true_closed_mutual_outer_backward_symmetric_difference_count"
                ]
            )
            == 0,
            "true_positive_equals_outer_positive_forward_pass": int(
                aligned[
                    "true_positive_outer_positive_forward_symmetric_difference_count"
                ]
            )
            == 0,
            "true_positive_equals_outer_positive_backward_pass": int(
                aligned[
                    "true_positive_outer_positive_backward_symmetric_difference_count"
                ]
            )
            == 0,
            "true_edge_subset_outer_pass": not any(
                int(subsets[field])
                for field in ("true_forward_minus_outer", "true_backward_minus_outer")
            ),
            "true_positive_subset_outer_positive_pass": not any(
                int(subsets[field])
                for field in (
                    "true_forward_positive_minus_outer_positive",
                    "true_backward_positive_minus_outer_positive",
                )
            ),
            "true_forward_inverse_labelled_transpose_pass": int(
                symmetric["true_forward_inverse_labelled_transpose"]
            )
            == 0,
        }
        for field, expected_value in reported_pass_expectations.items():
            if field in record:
                reported_decision_checks[field] = bool(record[field]) is expected_value
        if not all(reported_decision_checks.values()):
            raise AssertionError(f"{name} reported decision fields disagree with NPZ")
        artifacts[name] = artifact
        record_checks[name] = {
            "artifact_path": str(artifact_path),
            "artifact_sha256_pass": True,
            "optional_record_fields": consistency,
            "reported_decision_fields": reported_decision_checks,
            **decisions,
        }
    all_decisions = all(
        bool(item["all_decision_set_differences_zero"])
        for item in record_checks.values()  # type: ignore[union-attr]
    )
    return artifacts, {
        "configuration_record_count": len(expected),
        "heldout_record_count": len(protocol["heldout_configurations"]),  # type: ignore[arg-type]
        "records": record_checks,
        "all_persisted_decision_set_differences_zero": all_decisions,
        "pass": all_decisions,
    }


def labels_for_source(array: np.ndarray, source_id: int) -> dict[int, int]:
    selected = array[array[:, 0] == source_id]
    return {int(row[1]): int(row[2]) for row in selected}


def _first_map_difference(
    expected: Mapping[int, int], observed: Mapping[int, int]
) -> dict[str, object] | None:
    for target in sorted(set(expected) | set(observed)):
        if expected.get(target) != observed.get(target):
            return {
                "target_id": target,
                "checker_label": expected.get(target),
                "producer_label": observed.get(target),
            }
    return None


def _fixed_source_job(
    job: tuple[str, int, Fraction, int, Constants]
) -> tuple[str, int, dict[str, object]]:
    name, grid, offset, source_id, constants = job
    edges = make_edges(constants.radius, grid, offset)
    return name, source_id, brute_force_source(edges, source_id, constants)


def check_fixed_sources(
    protocol: Mapping[str, object],
    artifacts: Mapping[str, EdgeArtifact],
    workers: int = 1,
) -> dict[str, object]:
    constants = constants_from_protocol(protocol)
    if workers <= 0:
        raise ValueError("workers must be positive")
    jobs: list[tuple[str, int, Fraction, int, Constants]] = []
    for configuration in protocol["heldout_configurations"]:  # type: ignore[index]
        name = str(configuration["configuration_id"])
        grid = int(configuration["grid"])
        offset = parse_fraction(configuration["grid_offset"])
        jobs.extend(
            (name, grid, offset, source_id, constants)
            for source_id in fixed_source_ids(grid)
        )
    if workers == 1:
        completed = [_fixed_source_job(job) for job in jobs]
    else:
        with ProcessPoolExecutor(max_workers=min(workers, len(jobs))) as executor:
            completed = list(executor.map(_fixed_source_job, jobs))
    recomputed_by_name: dict[str, dict[int, dict[str, object]]] = {}
    for name, source_id, recomputed in completed:
        recomputed_by_name.setdefault(name, {})[source_id] = recomputed

    output: dict[str, object] = {}
    all_pass = True
    for configuration in protocol["heldout_configurations"]:  # type: ignore[index]
        name = str(configuration["configuration_id"])
        grid = int(configuration["grid"])
        offset = parse_fraction(configuration["grid_offset"])
        edges = make_edges(constants.radius, grid, offset)
        source_ids = fixed_source_ids(grid)
        artifact = artifacts[name]
        first_mismatch: dict[str, object] | None = None
        for source_id in source_ids:
            recomputed = recomputed_by_name[name][source_id]
            for key in EDGE_ARRAY_KEYS:
                expected = recomputed[key]
                if not isinstance(expected, Mapping):
                    raise AssertionError("invalid independent source result")
                observed = labels_for_source(artifact.arrays[key], source_id)
                difference = _first_map_difference(expected, observed)
                if difference is not None:
                    target_id = int(difference["target_id"])
                    cells = _cell_intervals(edges)
                    source_x = cells[source_id % grid]
                    source_y = cells[source_id // grid]
                    target_x = cells[target_id % grid]
                    target_y = cells[target_id // grid]
                    first_mismatch = {
                        "configuration": name,
                        "array": key,
                        "direction": "backward" if "backward" in key else "forward",
                        "source_id": source_id,
                        **difference,
                        "exact_source_bounds": list(
                            map(fraction_text, (*source_x, *source_y))
                        ),
                        "exact_target_bounds": list(
                            map(fraction_text, (*target_x, *target_y))
                        ),
                        "adaptive_k": (
                            recomputed["backward_k"]
                            if "backward" in key
                            else recomputed["forward_k"]
                        ),
                    }
                    inverse = "backward" in key
                    adaptive_k = int(first_mismatch["adaptive_k"])
                    relevant_slabs = []
                    for slab_index in range(adaptive_k):
                        rectangle = slab_bounds(
                            source_x,
                            source_y,
                            slab_index,
                            adaptive_k,
                            inverse,
                            constants.a,
                        )
                        classification = rectangle_overlap_class(
                            rectangle, target_x, target_y
                        )
                        if classification is not None:
                            relevant_slabs.append(
                                {
                                    "slab_index": slab_index,
                                    "bounds": list(map(fraction_text, rectangle)),
                                    "positive_or_touch_label": (
                                        "P" if classification else "T"
                                    ),
                                }
                            )
                    first_mismatch["relevant_outer_slabs"] = relevant_slabs
                    first_mismatch.update(
                        true_predicate_diagnostic(
                            source_x,
                            source_y,
                            target_x,
                            target_y,
                            constants.a,
                            inverse=inverse,
                        )
                    )
                    break
            if first_mismatch is not None:
                break
        configuration_pass = first_mismatch is None
        all_pass = all_pass and configuration_pass
        output[name] = {
            "source_count": len(source_ids),
            "source_ids": list(source_ids),
            "all_targets_per_source": grid * grid,
            "first_mismatch": first_mismatch,
            "pass": configuration_pass,
        }
    return {
        "configurations": output,
        "workers": min(workers, len(jobs)),
        "all_fixed_source_checks_pass": all_pass,
        "pass": all_pass,
    }


def strongly_connected_components(adjacency: Sequence[set[int]]) -> list[list[int]]:
    """Independent iterative Kosaraju implementation used only by checker toys."""

    count = len(adjacency)
    reverse: list[list[int]] = [[] for _ in range(count)]
    for source, targets in enumerate(adjacency):
        for target in targets:
            reverse[target].append(source)
    visited = [False] * count
    order: list[int] = []
    for start in range(count):
        if visited[start]:
            continue
        visited[start] = True
        stack: list[tuple[int, object]] = [(start, iter(sorted(adjacency[start])))]
        while stack:
            node, iterator = stack[-1]
            try:
                target = next(iterator)  # type: ignore[arg-type]
            except StopIteration:
                order.append(node)
                stack.pop()
                continue
            if not visited[target]:
                visited[target] = True
                stack.append((target, iter(sorted(adjacency[target]))))
    assigned = [False] * count
    components: list[list[int]] = []
    for start in reversed(order):
        if assigned[start]:
            continue
        assigned[start] = True
        component: list[int] = []
        stack = [start]
        while stack:
            node = stack.pop()
            component.append(node)
            for predecessor in sorted(reverse[node]):
                if not assigned[predecessor]:
                    assigned[predecessor] = True
                    stack.append(predecessor)
        components.append(sorted(component))
    return components


def canonical_largest_component(adjacency: Sequence[set[int]]) -> list[int]:
    components = strongly_connected_components(adjacency)
    return min(components, key=lambda component: (-len(component), tuple(component))) if components else []


def run_scc_toy_checks() -> dict[str, object]:
    cycle_and_loop = [{1}, {2}, {0}, {3}, set()]
    components = strongly_connected_components(cycle_and_loop)
    assert sorted(components) == [[0, 1, 2], [3], [4]]
    assert canonical_largest_component(cycle_and_loop) == [0, 1, 2]
    tie = [{1}, {0}, {3}, {2}]
    assert canonical_largest_component(tie) == [0, 1]
    chain = [{1}, {2}, set()]
    assert sorted(strongly_connected_components(chain)) == [[0], [1], [2]]
    return {
        "cycle_size_three_detected": True,
        "singleton_self_loop_not_promoted": True,
        "lexicographic_tie_rule_pass": True,
        "finish_order_chain_pass": True,
        "pass": True,
    }


def project_node_id(child_node: int, parent_grid: int, ratio: int = 2) -> int:
    child_grid = parent_grid * ratio
    child_x = child_node % child_grid
    child_y = child_node // child_grid
    return (child_y // ratio) * parent_grid + child_x // ratio


def project_labelled_edges(
    child_edges: Iterable[tuple[int, int, int]],
    parent_grid: int,
    ratio: int = 2,
) -> set[tuple[int, int, int]]:
    projected: dict[tuple[int, int], int] = {}
    for source, target, positive in child_edges:
        key = (
            project_node_id(source, parent_grid, ratio),
            project_node_id(target, parent_grid, ratio),
        )
        projected[key] = max(projected.get(key, 0), int(positive))
    return {(source, target, positive) for (source, target), positive in projected.items()}


def lift_parent_nodes(
    parent_nodes: Iterable[int], parent_grid: int, ratio: int = 2
) -> set[int]:
    child_grid = parent_grid * ratio
    lifted: set[int] = set()
    for parent in parent_nodes:
        parent_x = parent % parent_grid
        parent_y = parent // parent_grid
        for delta_y in range(ratio):
            for delta_x in range(ratio):
                lifted.add(
                    (ratio * parent_y + delta_y) * child_grid
                    + ratio * parent_x
                    + delta_x
                )
    return lifted


def run_nested_projection_toy_checks() -> dict[str, object]:
    parent_grid = 2
    # Two child contacts project to 0->3; positive wins over touch-only.
    child_edges = {
        (0, 10, 0),
        (1, 11, 1),
        (12, 3, 0),
    }
    assert project_labelled_edges(child_edges, parent_grid) == {
        (0, 3, 1),
        (2, 1, 0),
    }
    lifted = lift_parent_nodes({0, 3}, parent_grid)
    assert lifted == {0, 1, 4, 5, 10, 11, 14, 15}
    assert all(project_node_id(node, parent_grid) in {0, 3} for node in lifted)
    assert len(lifted) == 4 * 2
    return {
        "node_projection_pass": True,
        "positive_label_dominance_pass": True,
        "active_lift_partition_pass": True,
        "pass": True,
    }


def compare_artifacts(left: EdgeArtifact, right: EdgeArtifact) -> dict[str, object]:
    equality = {
        key: bool(np.array_equal(left.arrays[key], right.arrays[key]))
        for key in (*EDGE_ARRAY_KEYS, *NODE_ARRAY_KEYS)
    }
    return {"array_equality": equality, "pass": all(equality.values())}


def _configuration_map(
    protocol: Mapping[str, object],
) -> dict[str, Mapping[str, object]]:
    output: dict[str, Mapping[str, object]] = {}
    for block in ("development_anchors", "heldout_configurations"):
        for item in protocol[block]:  # type: ignore[index]
            output[str(item["configuration_id"])] = item
    return output


def _labelled_edges_from_array(
    array: np.ndarray, *, positive_only: bool = False
) -> set[tuple[int, int, int]]:
    return {
        (int(source), int(target), int(positive))
        for source, target, positive in array
        if not positive_only or int(positive) == 1
    }


def _induced_labelled_edges(
    edges: Iterable[tuple[int, int, int]], active: set[int]
) -> set[tuple[int, int, int]]:
    return {
        (source, target, positive)
        for source, target, positive in edges
        if source in active and target in active
    }


def _unlabelled_pairs(
    edges: Iterable[tuple[int, int, int]],
) -> set[tuple[int, int]]:
    return {(source, target) for source, target, _ in edges}


def _pair_array(pairs: Iterable[tuple[int, int]]) -> np.ndarray:
    return np.asarray(sorted(set(pairs)), dtype=np.int64).reshape((-1, 2))


def _pair_hash(pairs: Iterable[tuple[int, int]]) -> str:
    digest = hashlib.sha256()
    for source, target in sorted(set(pairs)):
        digest.update(f"{source},{target}\n".encode("ascii"))
    return digest.hexdigest()


def _components_from_labelled_edges(
    edges: Iterable[tuple[int, int, int]], active: set[int]
) -> list[list[int]]:
    """Reconstruct canonical global-node SCCs with the checker's own code."""

    active_ids = sorted(active)
    local_id = {node: index for index, node in enumerate(active_ids)}
    adjacency: list[set[int]] = [set() for _ in active_ids]
    for source, target, _ in edges:
        if source in local_id and target in local_id:
            adjacency[local_id[source]].add(local_id[target])
    components = [
        sorted(active_ids[index] for index in component)
        for component in strongly_connected_components(adjacency)
    ]
    components.sort(key=lambda nodes: (-len(nodes), tuple(nodes)))
    return components


def _project_node_set(nodes: Iterable[int], parent_grid: int) -> set[int]:
    return {project_node_id(node, parent_grid) for node in nodes}


def _validate_pair_array(key: str, array: np.ndarray, state_count: int) -> None:
    if array.dtype != np.dtype(np.int64) or array.ndim != 2 or array.shape[1] != 2:
        raise AssertionError(f"{key} must be an int64 array of shape (m,2)")
    if len(array) and (np.any(array < 0) or np.any(array >= state_count)):
        raise AssertionError(f"{key} contains out-of-range node IDs")
    if len(array) > 1:
        order = np.lexsort((array[:, 1], array[:, 0]))
        if not np.array_equal(order, np.arange(len(array))):
            raise AssertionError(f"{key} is not canonically sorted")
        if np.any(np.all(array[1:] == array[:-1], axis=1)):
            raise AssertionError(f"{key} contains duplicate pairs")


REFINEMENT_DECISION_ARRAY_KEYS = tuple(
    key
    for variant in ("true_closed", "true_positive")
    for key in (
        f"{variant}_complete_projected_edges",
        f"{variant}_complete_projected_backward_edges",
        f"{variant}_matched_support_projected_edges",
        f"{variant}_matched_support_projected_backward_edges",
        f"{variant}_parent_active_induced_edges",
        f"{variant}_parent_active_induced_backward_edges",
    )
)
REFINEMENT_SCC_NODE_ARRAY_KEYS = tuple(
    key
    for variant in ("true_closed", "true_positive")
    for key in (
        f"{variant}_largest_descendant_node_ids",
        f"{variant}_descendant_union_node_ids",
        f"{variant}_matched_support_largest_node_ids",
    )
)
REFINEMENT_NODE_ARRAY_KEYS = (
    "lift_parent_active_node_ids",
    "active_lift_missing_child_node_ids",
    *REFINEMENT_SCC_NODE_ARRAY_KEYS,
)
REFINEMENT_ARRAY_KEYS = (
    "lift_parent_active_node_ids",
    "active_lift_missing_child_node_ids",
    *REFINEMENT_DECISION_ARRAY_KEYS,
    *REFINEMENT_SCC_NODE_ARRAY_KEYS,
)


def _reported_value_matches(observed: object, expected: object) -> bool:
    if isinstance(expected, bool):
        return observed is expected
    return observed == expected


def _direction_metric_expectations(
    *,
    direction: str,
    projected_full: set[tuple[int, int, int]],
    parent_edges: set[tuple[int, int, int]],
    child_matched: set[tuple[int, int, int]],
    projected_matched: set[tuple[int, int, int]],
    parent_induced: set[tuple[int, int, int]],
) -> dict[str, object]:
    projected_full_pairs = _unlabelled_pairs(projected_full)
    parent_pairs = _unlabelled_pairs(parent_edges)
    projected_matched_pairs = _unlabelled_pairs(projected_matched)
    parent_induced_pairs = _unlabelled_pairs(parent_induced)
    complete_difference = projected_full_pairs ^ parent_pairs
    matched_difference = projected_matched_pairs ^ parent_induced_pairs
    if direction == "forward":
        return {
            "complete_projected_edge_count": len(projected_full_pairs),
            "parent_complete_edge_count": len(parent_pairs),
            "complete_projection_symmetric_difference_count": len(
                complete_difference
            ),
            "complete_projection_equals_parent_pass": not complete_difference,
            "complete_projected_edge_sha256": _pair_hash(projected_full_pairs),
            "parent_complete_edge_sha256": _pair_hash(parent_pairs),
            "matched_support_child_edge_count": len(child_matched),
            "matched_support_projected_edge_count": len(projected_matched_pairs),
            "parent_active_induced_edge_count": len(parent_induced_pairs),
            "matched_support_projection_symmetric_difference_count": len(
                matched_difference
            ),
            "matched_support_projection_equals_parent_active_graph_pass": (
                not matched_difference
            ),
            "matched_support_projected_edge_sha256": _pair_hash(
                projected_matched_pairs
            ),
            "parent_active_induced_edge_sha256": _pair_hash(parent_induced_pairs),
        }
    if direction != "backward":
        raise ValueError("direction must be forward or backward")
    return {
        "complete_backward_projected_edge_count": len(projected_full_pairs),
        "parent_complete_backward_edge_count": len(parent_pairs),
        "complete_backward_projection_symmetric_difference_count": len(
            complete_difference
        ),
        "complete_backward_projection_equals_parent_pass": not complete_difference,
        "complete_backward_projected_edge_sha256": _pair_hash(
            projected_full_pairs
        ),
        "parent_complete_backward_edge_sha256": _pair_hash(parent_pairs),
        "matched_support_child_backward_edge_count": len(child_matched),
        "matched_support_projected_backward_edge_count": len(
            projected_matched_pairs
        ),
        "parent_active_induced_backward_edge_count": len(parent_induced_pairs),
        "matched_support_backward_projection_symmetric_difference_count": len(
            matched_difference
        ),
        "matched_support_backward_projection_equals_parent_active_graph_pass": (
            not matched_difference
        ),
        "matched_support_projected_backward_edge_sha256": _pair_hash(
            projected_matched_pairs
        ),
        "parent_active_induced_backward_edge_sha256": _pair_hash(
            parent_induced_pairs
        ),
    }


def check_refinement_projections(
    payload: Mapping[str, object],
    protocol: Mapping[str, object],
    artifacts: Mapping[str, EdgeArtifact],
) -> dict[str, object]:
    """Independently reload and recompute every frozen G4 edge projection.

    Configuration and refinement archives are read only through NumPy's
    no-pickle path.  Projection is performed on labelled edges, with positive
    dominating touch-only when several child edges map to one parent pair.
    The producer's persisted pair arrays, counts, hashes, and decision fields
    are then checked against these independently reconstructed objects.
    """

    constants = constants_from_protocol(protocol)
    configurations = _configuration_map(protocol)
    frozen_pairs = [
        (
            str(item["parent_configuration_id"]),
            str(item["child_configuration_id"]),
        )
        for item in protocol["nested_refinements"]  # type: ignore[index]
    ]
    raw_refinements = payload.get("refinements")
    if not isinstance(raw_refinements, list):
        raise AssertionError("R056 payload has no refinement records")
    observed_pairs = [
        (
            str(item.get("parent_configuration")),
            str(item.get("child_configuration")),
        )
        for item in raw_refinements
        if isinstance(item, Mapping)
    ]
    if len(observed_pairs) != len(raw_refinements) or observed_pairs != frozen_pairs:
        raise AssertionError("R056 persisted refinement order differs from protocol")
    by_pair = {
        pair: item
        for pair, item in zip(observed_pairs, raw_refinements, strict=True)
        if isinstance(item, Mapping)
    }

    pair_results: list[dict[str, object]] = []
    all_pass = True
    for parent_name, child_name in frozen_pairs:
        persisted = by_pair[(parent_name, child_name)]
        parent_config = configurations[parent_name]
        child_config = configurations[child_name]
        parent_grid = int(parent_config["grid"])
        child_grid = int(child_config["grid"])
        if child_grid != 2 * parent_grid:
            raise AssertionError("frozen refinement is not exactly 2x")
        parent_edges = make_edges(
            constants.radius,
            parent_grid,
            parse_fraction(parent_config["grid_offset"]),
        )
        child_edges = make_edges(
            constants.radius,
            child_grid,
            parse_fraction(child_config["grid_offset"]),
        )
        exact_nested = all(
            parent_edges[index] == child_edges[2 * index]
            for index in range(parent_grid + 1)
        )
        parent_arrays = artifacts[parent_name].arrays
        child_arrays = artifacts[child_name].arrays
        parent_active = {int(value) for value in parent_arrays["active_node_ids"]}
        child_active = {int(value) for value in child_arrays["active_node_ids"]}
        lifted_active = lift_parent_nodes(parent_active, parent_grid)
        missing_active = lifted_active - child_active

        independently_computed_arrays: dict[str, np.ndarray] = {
            "lift_parent_active_node_ids": np.asarray(
                sorted(lifted_active), dtype=np.int64
            ),
            "active_lift_missing_child_node_ids": np.asarray(
                sorted(missing_active), dtype=np.int64
            ),
        }
        variant_results: dict[str, object] = {}
        top_level_expectations: dict[str, object] = {
            "ratio": 2,
            "exact_nested_edge_vectors_pass": exact_nested,
            "parent_active_node_count": len(parent_active),
            "lifted_parent_active_node_count": len(lifted_active),
            "child_active_node_count": len(child_active),
            "lift_parent_active_subset_child_active_pass": not missing_active,
            "active_lift_missing_child_node_count": len(missing_active),
            "active_lift_missing_child_node_ids_sha256": node_hash(missing_active),
        }
        reported_field_checks: dict[str, bool] = {
            field: _reported_value_matches(persisted.get(field), expected)
            for field, expected in top_level_expectations.items()
        }
        for variant, positive_only in (
            ("true_closed", False),
            ("true_positive", True),
        ):
            direction_results: dict[str, object] = {}
            forward_parent_labelled: set[tuple[int, int, int]] | None = None
            forward_child_matched: set[tuple[int, int, int]] | None = None
            for direction, array_key in (
                ("forward", "true_forward_edges"),
                ("backward", "true_backward_edges"),
            ):
                parent_labelled = _labelled_edges_from_array(
                    parent_arrays[array_key], positive_only=positive_only
                )
                child_labelled = _labelled_edges_from_array(
                    child_arrays[array_key], positive_only=positive_only
                )
                projected_full = project_labelled_edges(
                    child_labelled, parent_grid
                )
                parent_induced = _induced_labelled_edges(
                    parent_labelled, parent_active
                )
                child_matched = _induced_labelled_edges(
                    child_labelled, lifted_active
                )
                projected_matched = project_labelled_edges(
                    child_matched, parent_grid
                )
                full_labelled_difference = projected_full ^ parent_labelled
                matched_labelled_difference = projected_matched ^ parent_induced
                hash_direction = "F" if direction == "forward" else "B"
                metric_expectations = _direction_metric_expectations(
                    direction=direction,
                    projected_full=projected_full,
                    parent_edges=parent_labelled,
                    child_matched=child_matched,
                    projected_matched=projected_matched,
                    parent_induced=parent_induced,
                )
                direction_results[direction] = {
                    "complete_labelled_projection_symmetric_difference_count": len(
                        full_labelled_difference
                    ),
                    "complete_labelled_projection_equals_parent_pass": (
                        not full_labelled_difference
                    ),
                    "complete_projected_labelled_edge_sha256": labelled_edge_hash(
                        projected_full, hash_direction
                    ),
                    "parent_complete_labelled_edge_sha256": labelled_edge_hash(
                        parent_labelled, hash_direction
                    ),
                    "matched_support_labelled_projection_symmetric_difference_count": len(
                        matched_labelled_difference
                    ),
                    "matched_support_labelled_projection_equals_parent_active_graph_pass": (
                        not matched_labelled_difference
                    ),
                    "matched_support_projected_labelled_edge_sha256": labelled_edge_hash(
                        projected_matched, hash_direction
                    ),
                    "parent_active_induced_labelled_edge_sha256": labelled_edge_hash(
                        parent_induced, hash_direction
                    ),
                    "positive_if_any_projection_rule_applied": True,
                    "reported_pair_metrics": metric_expectations,
                    "pass": (
                        not full_labelled_difference
                        and not matched_labelled_difference
                    ),
                }
                suffix = "" if direction == "forward" else "_backward"
                independently_computed_arrays[
                    f"{variant}_complete_projected{suffix}_edges"
                ] = _pair_array(_unlabelled_pairs(projected_full))
                independently_computed_arrays[
                    f"{variant}_matched_support_projected{suffix}_edges"
                ] = _pair_array(_unlabelled_pairs(projected_matched))
                independently_computed_arrays[
                    f"{variant}_parent_active_induced{suffix}_edges"
                ] = _pair_array(_unlabelled_pairs(parent_induced))
                if direction == "forward":
                    forward_parent_labelled = parent_labelled
                    forward_child_matched = child_matched

            metrics = persisted.get(variant)
            if not isinstance(metrics, Mapping):
                raise AssertionError(f"missing persisted {variant} refinement metrics")
            variant_reported_checks: dict[str, bool] = {}
            for direction in ("forward", "backward"):
                expectations = direction_results[direction]["reported_pair_metrics"]
                if not isinstance(expectations, Mapping):
                    raise AssertionError("internal refinement metric schema failure")
                for field, expected in expectations.items():
                    check_name = f"{variant}.{field}"
                    matches = _reported_value_matches(metrics.get(field), expected)
                    variant_reported_checks[field] = matches
                    reported_field_checks[check_name] = matches

            if (
                forward_parent_labelled is None
                or forward_child_matched is None
            ):
                raise AssertionError("forward refinement graph was not reconstructed")
            parent_components = _components_from_labelled_edges(
                forward_parent_labelled, parent_active
            )
            parent_dominant = parent_components[0] if parent_components else []
            parent_dominant_set = set(parent_dominant)
            lifted_parent_dominant = lift_parent_nodes(
                parent_dominant_set, parent_grid
            )
            matched_components = _components_from_labelled_edges(
                forward_child_matched, lifted_active
            )
            descendants = [
                component
                for component in matched_components
                if component
                and _project_node_set(component, parent_grid)
                <= parent_dominant_set
            ]
            multi_node_descendants = [
                component for component in descendants if len(component) > 1
            ]
            largest_descendant = (
                multi_node_descendants[0] if multi_node_descendants else []
            )
            descendant_union = sorted(
                {
                    node
                    for component in multi_node_descendants
                    for node in component
                }
            )
            matched_largest = matched_components[0] if matched_components else []
            supporting_expectations: dict[str, object] = {
                "parent_dominant_scc_node_count": len(parent_dominant),
                "parent_dominant_scc_node_ids_sha256": node_hash(parent_dominant),
                "lifted_parent_dominant_node_count": len(lifted_parent_dominant),
                "lifted_parent_dominant_node_ids_sha256": node_hash(
                    lifted_parent_dominant
                ),
                "matched_support_scc_count": len(matched_components),
                "matched_support_largest_scc_size": len(matched_largest),
                "matched_support_largest_scc_node_ids_sha256": node_hash(
                    matched_largest
                ),
                "descendant_scc_count": len(descendants),
                "multi_node_descendant_scc_count": len(multi_node_descendants),
                "nontrivial_descendant_exists_pass": bool(
                    multi_node_descendants
                ),
                "descendant_union_node_count": len(descendant_union),
                "descendant_union_node_ids_sha256": node_hash(descendant_union),
                "largest_descendant_node_count": len(largest_descendant),
                "largest_descendant_node_ids_sha256": node_hash(
                    largest_descendant
                ),
            }
            supporting_reported_checks = {
                field: _reported_value_matches(metrics.get(field), expected)
                for field, expected in supporting_expectations.items()
            }
            for field, matches in supporting_reported_checks.items():
                reported_field_checks[f"{variant}.{field}"] = matches
            independently_computed_arrays[
                f"{variant}_largest_descendant_node_ids"
            ] = np.asarray(largest_descendant, dtype=np.int64)
            independently_computed_arrays[
                f"{variant}_descendant_union_node_ids"
            ] = np.asarray(descendant_union, dtype=np.int64)
            independently_computed_arrays[
                f"{variant}_matched_support_largest_node_ids"
            ] = np.asarray(matched_largest, dtype=np.int64)
            supporting_pass = bool(multi_node_descendants) and all(
                supporting_reported_checks.values()
            )
            variant_results[variant] = {
                "directions": direction_results,
                "reported_pair_metric_checks": variant_reported_checks,
                "matched_support_descendant": {
                    **supporting_expectations,
                    "reported_metric_checks": supporting_reported_checks,
                    "pass": supporting_pass,
                },
                "pass": all(
                    bool(result["pass"])
                    for result in direction_results.values()  # type: ignore[union-attr]
                )
                and all(variant_reported_checks.values())
                and supporting_pass,
            }

        raw_path = persisted.get("refinement_array_path")
        expected_sha = persisted.get("refinement_array_sha256")
        if not isinstance(raw_path, str) or not isinstance(expected_sha, str):
            raise AssertionError("refinement artifact path/SHA is missing")
        refinement_path = Path(raw_path)
        if not refinement_path.is_absolute():
            refinement_path = PROJECT_ROOT / refinement_path
        artifact_sha_pass = sha256_file(refinement_path) == expected_sha
        with np.load(refinement_path, allow_pickle=False) as archive:
            for key in archive.files:
                if archive[key].dtype.hasobject:
                    raise AssertionError(f"refinement artifact {key} has object dtype")
            persisted_arrays = {
                key: np.array(archive[key], copy=True) for key in archive.files
            }
        observed_keys = set(persisted_arrays)
        expected_keys = set(REFINEMENT_ARRAY_KEYS)
        schema_errors: list[str] = []
        for key in sorted(observed_keys & expected_keys):
            observed = persisted_arrays[key]
            try:
                if key in REFINEMENT_DECISION_ARRAY_KEYS:
                    _validate_pair_array(key, observed, parent_grid * parent_grid)
                elif key in REFINEMENT_NODE_ARRAY_KEYS:
                    _validate_node_array(key, observed, child_grid * child_grid)
                else:
                    raise AssertionError(f"unexpected refinement array key {key}")
            except AssertionError as error:
                schema_errors.append(str(error))
        schema = {
            "allow_pickle": False,
            "expected_array_keys": list(REFINEMENT_ARRAY_KEYS),
            "missing_array_keys": sorted(expected_keys - observed_keys),
            "unexpected_array_keys": sorted(observed_keys - expected_keys),
            "validation_errors": schema_errors,
            "pass": (
                observed_keys == expected_keys and not schema_errors
            ),
        }
        array_equality: dict[str, bool] = {}
        for key, expected in independently_computed_arrays.items():
            observed = persisted_arrays.get(key)
            array_equality[key] = observed is not None and bool(
                np.array_equal(observed, expected)
            )
        pair_pass = (
            exact_nested
            and not missing_active
            and all(
                bool(result["pass"])
                for result in variant_results.values()  # type: ignore[union-attr]
            )
            and all(reported_field_checks.values())
            and artifact_sha_pass
            and bool(schema["pass"])
            and all(array_equality.values())
        )
        all_pass = all_pass and pair_pass
        pair_results.append(
            {
                "parent_configuration": parent_name,
                "child_configuration": child_name,
                "exact_nested_edge_vectors_pass": exact_nested,
                "active_lift": {
                    "parent_active_node_count": len(parent_active),
                    "lifted_parent_active_node_count": len(lifted_active),
                    "child_active_node_count": len(child_active),
                    "missing_child_node_count": len(missing_active),
                    "missing_child_node_ids_sha256": node_hash(missing_active),
                    "lift_parent_active_subset_child_active_pass": not missing_active,
                },
                "variants": variant_results,
                "reported_refinement_field_checks": reported_field_checks,
                "refinement_artifact": str(refinement_path),
                "refinement_artifact_sha256_pass": artifact_sha_pass,
                "refinement_artifact_schema": schema,
                "persisted_decision_array_equality": array_equality,
                "pass": pair_pass,
            }
        )
    return {
        "refinement_count": len(pair_results),
        "pairs": pair_results,
        "all_refinement_projection_checks_pass": all_pass,
        "pass": all_pass,
    }


def _discover_serial_path(
    payload: Mapping[str, object], records: Mapping[str, Mapping[str, object]]
) -> Path | None:
    candidates: list[object] = [
        payload.get("serial_edge_array_path"),
        payload.get("workers_1_edge_array_path"),
    ]
    replay = payload.get("serial_parallel_replay")
    if isinstance(replay, Mapping):
        candidates.extend(
            [replay.get("serial_edge_array_path"), replay.get("workers_1_edge_array_path")]
        )
    n127 = records.get("n127_d0")
    if n127 is not None:
        candidates.extend(
            [n127.get("serial_edge_array_path"), n127.get("workers_1_edge_array_path")]
        )
    for candidate in candidates:
        if isinstance(candidate, str):
            path = Path(candidate)
            return path if path.is_absolute() else PROJECT_ROOT / path
    return None


def check_serial_replay(
    payload: Mapping[str, object],
    artifacts: Mapping[str, EdgeArtifact],
    explicit_path: Path | None = None,
) -> dict[str, object]:
    records = records_by_configuration(payload)
    path = explicit_path or _discover_serial_path(payload, records)
    if path is None:
        return {"available": False, "pass": None}
    if path.suffix == ".json":
        replay_payload = json.loads(path.read_text(encoding="utf-8"))
        replay_record = records_by_configuration(replay_payload)["n127_d0"]
        path = resolve_artifact_path(replay_record)
    replay = load_edge_artifact(path, 127)
    comparison = compare_artifacts(artifacts["n127_d0"], replay)
    return {"available": True, "serial_artifact": str(path), **comparison}


def run_predicate_toy_checks() -> dict[str, object]:
    f = Fraction
    a_value = f(6)
    empty_source = ((f(0), f(1)), (f(0), f(1)))
    empty_target = ((f(-5), f(-4)), (f(2), f(3)))
    assert forward_true_class(*empty_source, *empty_target, a_value) is None
    point_source = ((f(0), f(1)), (f(0), f(0)))
    point_target = ((f(-5), f(-5)), (f(1), f(1)))
    assert forward_true_class(*point_source, *point_target, a_value) is False
    cross_source = ((f(-1), f(1)), (f(0), f(1)))
    cross_target = ((f(-5), f(-4)), (f(-1), f(1)))
    assert forward_true_class(*cross_source, *cross_target, a_value) is True
    source = ((f(-1, 2), f(1, 2)), (f(-1, 3), f(2, 3)))
    target = ((f(-3), f(-2)), (f(-1, 2), f(1, 2)))
    assert forward_true_class(*source, *target, a_value) == inverse_true_class(
        *target, *source, a_value
    )
    return {
        "empty_interval_pass": True,
        "touch_only_pass": True,
        "zero_crossing_pass": True,
        "transpose_pass": True,
        "pass": True,
    }


def main() -> None:
    args = parse_args()
    protocol = load_protocol(args.protocol)
    constants = constants_from_protocol(protocol)
    payload = json.loads(args.input.read_text(encoding="utf-8"))

    predicate_toys = run_predicate_toy_checks()
    scc_toys = run_scc_toy_checks()
    projection_toys = run_nested_projection_toy_checks()
    microgrids = [
        run_microgrid_sweep(7, Fraction(0), constants),
        run_microgrid_sweep(8, Fraction(1, 3), constants),
    ]
    artifacts, schema = validate_persisted_payload(payload, protocol)
    fixed_sources = check_fixed_sources(protocol, artifacts, args.workers)
    replay = check_serial_replay(payload, artifacts, args.serial_artifact)
    refinements = check_refinement_projections(payload, protocol, artifacts)
    replay_pass = replay["pass"] is not False
    all_pass = all(
        [
            predicate_toys["pass"],
            scc_toys["pass"],
            projection_toys["pass"],
            all(record["pass"] for record in microgrids),
            schema["pass"],
            fixed_sources["pass"],
            replay_pass,
            refinements["pass"],
        ]
    )
    output = {
        "run_id": "R056_TRUE_IMAGE_REFINEMENT_INDEPENDENT_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "producer_input": str(args.input),
        "protocol": str(args.protocol),
        "checker_imports_producer_geometry_or_scc_helpers": False,
        "predicate_toys": predicate_toys,
        "scc_toys": scc_toys,
        "nested_projection_toys": projection_toys,
        "microgrid_full_sweeps": microgrids,
        "persisted_schema_and_decisions": schema,
        "fixed_source_full_target_sweeps": fixed_sources,
        "serial_parallel_replay": replay,
        "persisted_refinement_projections": refinements,
        "all_checks_pass": all_pass,
        "scope": (
            "independent exact finite rational-grid implementation check; "
            "no invariant-set, covering, graph-limit, operator, zeta, or "
            "Riemann-zero claim"
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({"output": str(args.output), "all_checks_pass": all_pass}, indent=2))
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
