"""Substochastic finite-volume/Ulam operators for the open Hénon map."""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from numpy.typing import NDArray
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs
from scipy.stats import qmc

from .geometry import fixed_points


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class UlamAssembly:
    matrix: csr_matrix
    a: float
    radius: float
    cells_per_axis: int
    quadrature_order: int
    active_cells: NDArray[np.bool_]
    cell_centers: FloatArray
    row_sums: FloatArray
    hole_center: tuple[float, float] | None
    hole_radius: float
    method: str = "tensor_gauss_legendre"
    samples_per_cell: int | None = None
    seed: int | None = None
    survivor_horizon: int = 0
    survivor_rule: str = "box_center_mask_horizon_0"
    grid_offset: float = 0.0


@dataclass(frozen=True)
class EigenpairAudit:
    eigenvalue: complex
    modulus: float
    right_residual: float
    left_residual: float
    condition_estimate: float


@dataclass(frozen=True)
class SpectrumAudit:
    eigenpairs: tuple[EigenpairAudit, ...]
    leading_eigenvalue: complex
    escape_rate: float
    elliptic_mass_fraction_r03: float
    reference_fixed_point_stability: str


def uniform_cell_centers(radius: float, cells_per_axis: int) -> FloatArray:
    if radius <= 0.0:
        raise ValueError("radius must be positive")
    if cells_per_axis < 2:
        raise ValueError("cells_per_axis must be at least two")
    width = 2.0 * float(radius) / cells_per_axis
    axis = -float(radius) + (np.arange(cells_per_axis, dtype=float) + 0.5) * width
    x_grid, y_grid = np.meshgrid(axis, axis, indexing="xy")
    return np.column_stack((x_grid.ravel(), y_grid.ravel()))


def _point_is_in_domain(
    points: FloatArray,
    radius: float,
    hole_radius: float,
    hole_center: tuple[float, float] | None,
) -> NDArray[np.bool_]:
    valid = (
        (points[:, 0] >= -radius)
        & (points[:, 0] < radius)
        & (points[:, 1] >= -radius)
        & (points[:, 1] < radius)
    )
    if hole_radius > 0.0 and hole_center is not None:
        distances_squared = (
            (points[:, 0] - hole_center[0]) ** 2
            + (points[:, 1] - hole_center[1]) ** 2
        )
        valid &= distances_squared >= hole_radius**2
    return valid


def finite_time_survivor_mask(
    a: float,
    radius: float,
    cells_per_axis: int,
    horizon: int,
    hole_radius: float = 0.0,
    hole_center: tuple[float, float] | None = None,
) -> NDArray[np.bool_]:
    """Return a center-sampled forward/backward finite-time survivor mask.

    A cell is active when its center and its images under ``H_a`` and
    ``H_a^{-1}`` through ``horizon`` steps stay in the open box and outside the
    optional hole.  This is a reproducible finite-resolution mask, not a proof
    of invariance of the full cells or of the exact survivor set.
    """

    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if hole_radius < 0.0:
        raise ValueError("hole_radius must be nonnegative")
    centers = uniform_cell_centers(radius, cells_per_axis)
    if hole_radius > 0.0 and hole_center is None:
        elliptic = fixed_points(a)[0].coordinate
        hole_center = (elliptic, elliptic)
    active = np.ones(centers.shape[0], dtype=bool)
    forward = centers.copy()
    backward = centers.copy()
    for step in range(horizon + 1):
        active &= _point_is_in_domain(forward, radius, hole_radius, hole_center)
        active &= _point_is_in_domain(backward, radius, hole_radius, hole_center)
        if step == horizon:
            break
        if not np.any(active):
            break
        with np.errstate(over="ignore", invalid="ignore"):
            forward = np.column_stack(
                (
                    1.0 - float(a) * forward[:, 0] ** 2 - forward[:, 1],
                    forward[:, 0],
                )
            )
            backward = np.column_stack(
                (
                    backward[:, 1],
                    1.0 - float(a) * backward[:, 1] ** 2 - backward[:, 0],
                )
            )
    return active


def assemble_absorbing_ulam(
    a: float,
    radius: float,
    cells_per_axis: int,
    quadrature_order: int = 4,
    hole_radius: float = 0.0,
    hole_center: tuple[float, float] | None = None,
    survivor_horizon: int = 0,
) -> UlamAssembly:
    """Assemble a row-substochastic quadrature Ulam matrix.

    Rows are source cells and columns are target cells. Mass mapped outside the
    square or into a grid-cell hole is discarded; rows are deliberately not
    normalized back to one.
    """

    if quadrature_order < 1:
        raise ValueError("quadrature_order must be positive")
    if hole_radius < 0.0:
        raise ValueError("hole_radius must be nonnegative")
    centers = uniform_cell_centers(radius, cells_per_axis)
    total_cells = cells_per_axis**2
    width = 2.0 * float(radius) / cells_per_axis

    if hole_radius > 0.0 and hole_center is None:
        elliptic = fixed_points(a)[0].coordinate
        hole_center = (elliptic, elliptic)
    active = np.ones(total_cells, dtype=bool)
    if hole_radius > 0.0 and hole_center is not None:
        distances_squared = (
            (centers[:, 0] - hole_center[0]) ** 2
            + (centers[:, 1] - hole_center[1]) ** 2
        )
        active = distances_squared >= hole_radius**2

    if survivor_horizon:
        active &= finite_time_survivor_mask(
            a,
            radius,
            cells_per_axis,
            survivor_horizon,
            hole_radius,
            hole_center,
        )
    source_indices = np.flatnonzero(active)
    source_x = centers[source_indices, 0]
    source_y = centers[source_indices, 1]
    nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)

    row_chunks: list[NDArray[np.int64]] = []
    column_chunks: list[NDArray[np.int64]] = []
    value_chunks: list[FloatArray] = []
    for x_node, x_weight in zip(nodes, weights):
        x = source_x + 0.5 * width * x_node
        for y_node, y_weight in zip(nodes, weights):
            y = source_y + 0.5 * width * y_node
            image_x = 1.0 - float(a) * x * x - y
            image_y = x
            valid = (
                (image_x >= -radius)
                & (image_x < radius)
                & (image_y >= -radius)
                & (image_y < radius)
            )
            target_x = np.floor((image_x[valid] + radius) / width).astype(np.int64)
            target_y = np.floor((image_y[valid] + radius) / width).astype(np.int64)
            target = target_y * cells_per_axis + target_x
            valid_targets = active[target]
            if not np.any(valid_targets):
                continue
            selected_sources = source_indices[valid][valid_targets]
            selected_targets = target[valid_targets]
            quadrature_weight = float(x_weight * y_weight / 4.0)
            row_chunks.append(selected_sources.astype(np.int64, copy=False))
            column_chunks.append(selected_targets.astype(np.int64, copy=False))
            value_chunks.append(np.full(selected_sources.size, quadrature_weight, dtype=float))

    if row_chunks:
        rows = np.concatenate(row_chunks)
        columns = np.concatenate(column_chunks)
        values = np.concatenate(value_chunks)
    else:
        rows = np.empty(0, dtype=np.int64)
        columns = np.empty(0, dtype=np.int64)
        values = np.empty(0, dtype=float)
    matrix = csr_matrix((values, (rows, columns)), shape=(total_cells, total_cells))
    matrix.sum_duplicates()
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    if np.max(row_sums, initial=0.0) > 1.0 + 1.0e-12:
        raise RuntimeError("sub-stochastic assembly produced a row sum above one")
    return UlamAssembly(
        matrix=matrix,
        a=float(a),
        radius=float(radius),
        cells_per_axis=int(cells_per_axis),
        quadrature_order=int(quadrature_order),
        active_cells=active,
        cell_centers=centers,
        row_sums=row_sums,
        hole_center=hole_center,
        hole_radius=float(hole_radius),
        method="tensor_gauss_legendre",
        samples_per_cell=int(quadrature_order**2),
        seed=None,
        survivor_horizon=int(survivor_horizon),
        survivor_rule=f"box_center_mask_horizon_{int(survivor_horizon)}",
    )


def assemble_sobol_ulam(
    a: float,
    radius: float,
    cells_per_axis: int,
    samples_per_cell: int = 64,
    seed: int = 20260801,
    hole_radius: float = 0.0,
    hole_center: tuple[float, float] | None = None,
    survivor_horizon: int = 0,
) -> UlamAssembly:
    """Assemble an independent randomized quasi-Monte Carlo Ulam matrix.

    Each active source cell receives the same scrambled Sobol base rule with an
    independent reproducible Cranley--Patterson shift.  This is intentionally a
    different cell-integration route from tensor Gauss--Legendre quadrature.
    ``samples_per_cell`` must be a power of two so the Sobol balance properties
    are retained.
    """

    if samples_per_cell < 1 or samples_per_cell & (samples_per_cell - 1):
        raise ValueError("samples_per_cell must be a positive power of two")
    if hole_radius < 0.0:
        raise ValueError("hole_radius must be nonnegative")
    centers = uniform_cell_centers(radius, cells_per_axis)
    total_cells = cells_per_axis**2
    width = 2.0 * float(radius) / cells_per_axis

    if hole_radius > 0.0 and hole_center is None:
        elliptic = fixed_points(a)[0].coordinate
        hole_center = (elliptic, elliptic)
    active = np.ones(total_cells, dtype=bool)
    if hole_radius > 0.0 and hole_center is not None:
        distances_squared = (
            (centers[:, 0] - hole_center[0]) ** 2
            + (centers[:, 1] - hole_center[1]) ** 2
        )
        active = distances_squared >= hole_radius**2

    if survivor_horizon:
        active &= finite_time_survivor_mask(
            a,
            radius,
            cells_per_axis,
            survivor_horizon,
            hole_radius,
            hole_center,
        )
    source_indices = np.flatnonzero(active)
    source_centers = centers[source_indices]
    exponent = int(round(math.log2(samples_per_cell)))
    sampler = qmc.Sobol(d=2, scramble=True, seed=int(seed))
    base_points = sampler.random_base2(exponent)
    generator = np.random.default_rng(int(seed) + 1_000_003)
    cell_shifts = generator.random((source_indices.size, 2))

    row_chunks: list[NDArray[np.int64]] = []
    column_chunks: list[NDArray[np.int64]] = []
    value_chunks: list[FloatArray] = []
    for base_point in base_points:
        unit_points = np.mod(base_point + cell_shifts, 1.0)
        points = source_centers + width * (unit_points - 0.5)
        image_x = 1.0 - float(a) * points[:, 0] ** 2 - points[:, 1]
        image_y = points[:, 0]
        valid = (
            (image_x >= -radius)
            & (image_x < radius)
            & (image_y >= -radius)
            & (image_y < radius)
        )
        if not np.any(valid):
            continue
        target_x = np.floor((image_x[valid] + radius) / width).astype(np.int64)
        target_y = np.floor((image_y[valid] + radius) / width).astype(np.int64)
        target = target_y * cells_per_axis + target_x
        valid_targets = active[target]
        if not np.any(valid_targets):
            continue
        selected_sources = source_indices[valid][valid_targets]
        selected_targets = target[valid_targets]
        row_chunks.append(selected_sources.astype(np.int64, copy=False))
        column_chunks.append(selected_targets.astype(np.int64, copy=False))
        value_chunks.append(
            np.full(selected_sources.size, 1.0 / samples_per_cell, dtype=float)
        )

    if row_chunks:
        rows = np.concatenate(row_chunks)
        columns = np.concatenate(column_chunks)
        values = np.concatenate(value_chunks)
    else:
        rows = np.empty(0, dtype=np.int64)
        columns = np.empty(0, dtype=np.int64)
        values = np.empty(0, dtype=float)
    matrix = csr_matrix((values, (rows, columns)), shape=(total_cells, total_cells))
    matrix.sum_duplicates()
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    if np.max(row_sums, initial=0.0) > 1.0 + 1.0e-12:
        raise RuntimeError("sub-stochastic assembly produced a row sum above one")
    return UlamAssembly(
        matrix=matrix,
        a=float(a),
        radius=float(radius),
        cells_per_axis=int(cells_per_axis),
        quadrature_order=0,
        active_cells=active,
        cell_centers=centers,
        row_sums=row_sums,
        hole_center=hole_center,
        hole_radius=float(hole_radius),
        method="random_shift_sobol",
        samples_per_cell=int(samples_per_cell),
        seed=int(seed),
        survivor_horizon=int(survivor_horizon),
        survivor_rule=f"box_center_mask_horizon_{int(survivor_horizon)}",
    )


def quadratic_strip_overlap_area(
    a: float,
    x_lower: float,
    x_upper: float,
    y_lower: float,
    y_upper: float,
    target_x_lower: float,
    target_x_upper: float,
) -> float:
    """Return the exact one-dimensional slice integral for one cell overlap.

    For ``Y=x`` and ``X=1-a*x^2-y``, the target-X condition restricts
    ``y`` to a quadratic interval.  Its overlap with the source-y interval is
    piecewise quadratic in ``x``.  All branch-change roots are inserted as
    breakpoints and each polynomial piece is integrated analytically.
    """

    if x_upper <= x_lower or y_upper <= y_lower:
        return 0.0
    if target_x_upper <= target_x_lower:
        return 0.0
    breakpoints = [float(x_lower), float(x_upper)]
    if x_lower < 0.0 < x_upper:
        breakpoints.append(0.0)
    if a != 0.0:
        for target_boundary in (target_x_lower, target_x_upper):
            for source_boundary in (y_lower, y_upper):
                squared = (1.0 - target_boundary - source_boundary) / float(a)
                if squared < 0.0:
                    continue
                root = math.sqrt(max(0.0, squared))
                for candidate in (-root, root):
                    if x_lower < candidate < x_upper:
                        breakpoints.append(float(candidate))
    breakpoints = sorted(set(breakpoints))
    contributions: list[float] = []
    for lower, upper in zip(breakpoints[:-1], breakpoints[1:]):
        if upper <= lower:
            continue
        midpoint = 0.5 * (lower + upper)
        image_interval_lower = 1.0 - float(a) * midpoint**2 - target_x_upper
        image_interval_upper = 1.0 - float(a) * midpoint**2 - target_x_lower

        if y_upper <= image_interval_upper:
            top_constant, top_quadratic = y_upper, 0.0
        else:
            top_constant, top_quadratic = 1.0 - target_x_lower, -float(a)
        if y_lower >= image_interval_lower:
            bottom_constant, bottom_quadratic = y_lower, 0.0
        else:
            bottom_constant, bottom_quadratic = 1.0 - target_x_upper, -float(a)
        value_midpoint = (
            top_constant
            - bottom_constant
            + (top_quadratic - bottom_quadratic) * midpoint**2
        )
        if value_midpoint <= 0.0:
            continue
        constant = top_constant - bottom_constant
        quadratic = top_quadratic - bottom_quadratic
        interval_width = upper - lower
        second_moment = (
            upper * upper + upper * lower + lower * lower
        ) / 3.0
        contributions.append(
            interval_width * (constant + quadratic * second_moment)
        )
    cell_area = (x_upper - x_lower) * (y_upper - y_lower)
    area = math.fsum(contributions)
    return float(min(max(area, 0.0), cell_area))


def assemble_overlap_ulam(
    a: float,
    radius: float,
    cells_per_axis: int,
    survivor_horizon: int = 0,
) -> UlamAssembly:
    """Assemble a semi-analytic cell-overlap Ulam matrix.

    The Hénon map sends ``(x,y)`` to ``(X,Y)=(1-a*x^2-y,x)``.  Because the
    target Y-coordinate equals the source x-coordinate, a source cell can
    overlap only the target-cell row with the matching y index.  Transition
    areas are then computed by :func:`quadratic_strip_overlap_area` without
    two-dimensional point sampling.

    Circular holes are intentionally unsupported here because their exact cell
    intersections require a separate geometric treatment.
    """

    if radius <= 0.0:
        raise ValueError("radius must be positive")
    if a < 0.0:
        raise ValueError(
            "semi-analytic overlap assembly currently requires nonnegative a"
        )
    if cells_per_axis < 2:
        raise ValueError("cells_per_axis must be at least two")
    if survivor_horizon < 0:
        raise ValueError("survivor_horizon must be nonnegative")
    centers = uniform_cell_centers(radius, cells_per_axis)
    total_cells = cells_per_axis**2
    width = 2.0 * float(radius) / cells_per_axis
    edges = np.linspace(-float(radius), float(radius), cells_per_axis + 1)
    active = finite_time_survivor_mask(
        a,
        radius,
        cells_per_axis,
        survivor_horizon,
    )

    rows: list[int] = []
    columns: list[int] = []
    values: list[float] = []
    cell_area = width**2
    for source_y_index in range(cells_per_axis):
        y_lower = float(edges[source_y_index])
        y_upper = float(edges[source_y_index + 1])
        for source_x_index in range(cells_per_axis):
            source = source_y_index * cells_per_axis + source_x_index
            if not active[source]:
                continue
            x_lower = float(edges[source_x_index])
            x_upper = float(edges[source_x_index + 1])
            maximum_abs_x = max(abs(x_lower), abs(x_upper))
            minimum_abs_x = (
                0.0
                if x_lower <= 0.0 <= x_upper
                else min(abs(x_lower), abs(x_upper))
            )
            image_minimum = 1.0 - float(a) * maximum_abs_x**2 - y_upper
            image_maximum = 1.0 - float(a) * minimum_abs_x**2 - y_lower
            clipped_minimum = max(image_minimum, -float(radius))
            clipped_maximum = min(image_maximum, float(radius))
            if clipped_maximum <= clipped_minimum:
                continue
            first_target_x = max(
                0,
                int(math.floor((clipped_minimum + radius) / width)),
            )
            last_target_x = min(
                cells_per_axis - 1,
                int(math.floor((np.nextafter(clipped_maximum, -np.inf) + radius) / width)),
            )
            target_y_index = source_x_index
            for target_x_index in range(first_target_x, last_target_x + 1):
                target = target_y_index * cells_per_axis + target_x_index
                if not active[target]:
                    continue
                area = quadratic_strip_overlap_area(
                    a,
                    x_lower,
                    x_upper,
                    y_lower,
                    y_upper,
                    float(edges[target_x_index]),
                    float(edges[target_x_index + 1]),
                )
                if area <= 1.0e-16 * cell_area:
                    continue
                rows.append(source)
                columns.append(target)
                values.append(area / cell_area)

    matrix = csr_matrix(
        (
            np.asarray(values, dtype=float),
            (np.asarray(rows, dtype=np.int64), np.asarray(columns, dtype=np.int64)),
        ),
        shape=(total_cells, total_cells),
    )
    matrix.sum_duplicates()
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    maximum_row_sum = float(np.max(row_sums, initial=0.0))
    if maximum_row_sum > 1.0 + 5.0e-12:
        raise RuntimeError(
            "overlap assembly produced a row sum above one: "
            f"maximum={maximum_row_sum:.17g}"
        )
    return UlamAssembly(
        matrix=matrix,
        a=float(a),
        radius=float(radius),
        cells_per_axis=int(cells_per_axis),
        quadrature_order=0,
        active_cells=active,
        cell_centers=centers,
        row_sums=row_sums,
        hole_center=None,
        hole_radius=0.0,
        method="semi_analytic_overlap",
        samples_per_cell=None,
        seed=None,
        survivor_horizon=int(survivor_horizon),
        survivor_rule=f"box_center_mask_horizon_{int(survivor_horizon)}",
    )


def _assemble_overlap_from_edges(
    a: float,
    radius: float,
    cells_per_axis: int,
    edges: FloatArray,
    active: NDArray[np.bool_],
    survivor_horizon: int,
    method: str,
    grid_offset: float,
) -> UlamAssembly:
    """Assemble overlap transitions for a common x/y edge tessellation."""

    if edges.shape != (cells_per_axis + 1,):
        raise ValueError("edges must contain cells_per_axis + 1 entries")
    if np.any(np.diff(edges) <= 0.0):
        raise ValueError("edges must be strictly increasing")
    widths = np.diff(edges)
    centers_axis = 0.5 * (edges[:-1] + edges[1:])
    x_centers, y_centers = np.meshgrid(centers_axis, centers_axis, indexing="xy")
    centers = np.column_stack((x_centers.ravel(), y_centers.ravel()))
    total_cells = cells_per_axis**2

    rows: list[int] = []
    columns: list[int] = []
    values: list[float] = []
    for source_y_index in range(cells_per_axis):
        y_lower = float(edges[source_y_index])
        y_upper = float(edges[source_y_index + 1])
        for source_x_index in range(cells_per_axis):
            source = source_y_index * cells_per_axis + source_x_index
            if not active[source]:
                continue
            x_lower = float(edges[source_x_index])
            x_upper = float(edges[source_x_index + 1])
            source_cell_area = float(
                widths[source_x_index] * widths[source_y_index]
            )
            maximum_abs_x = max(abs(x_lower), abs(x_upper))
            minimum_abs_x = (
                0.0
                if x_lower <= 0.0 <= x_upper
                else min(abs(x_lower), abs(x_upper))
            )
            image_minimum = 1.0 - float(a) * maximum_abs_x**2 - y_upper
            image_maximum = 1.0 - float(a) * minimum_abs_x**2 - y_lower
            clipped_minimum = max(image_minimum, -float(radius))
            clipped_maximum = min(image_maximum, float(radius))
            if clipped_maximum <= clipped_minimum:
                continue
            first_target_x = max(
                0,
                int(np.searchsorted(edges, clipped_minimum, side="right") - 1),
            )
            last_target_x = min(
                cells_per_axis - 1,
                int(
                    np.searchsorted(
                        edges,
                        np.nextafter(clipped_maximum, -np.inf),
                        side="right",
                    )
                    - 1
                ),
            )
            target_y_index = source_x_index
            for target_x_index in range(first_target_x, last_target_x + 1):
                target = target_y_index * cells_per_axis + target_x_index
                if not active[target]:
                    continue
                area = quadratic_strip_overlap_area(
                    a,
                    x_lower,
                    x_upper,
                    y_lower,
                    y_upper,
                    float(edges[target_x_index]),
                    float(edges[target_x_index + 1]),
                )
                if area <= 1.0e-16 * source_cell_area:
                    continue
                rows.append(source)
                columns.append(target)
                values.append(area / source_cell_area)

    matrix = csr_matrix(
        (
            np.asarray(values, dtype=float),
            (np.asarray(rows, dtype=np.int64), np.asarray(columns, dtype=np.int64)),
        ),
        shape=(total_cells, total_cells),
    )
    matrix.sum_duplicates()
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    maximum_row_sum = float(np.max(row_sums, initial=0.0))
    if maximum_row_sum > 1.0 + 5.0e-12:
        raise RuntimeError(
            "overlap assembly produced a row sum above one: "
            f"maximum={maximum_row_sum:.17g}"
        )
    return UlamAssembly(
        matrix=matrix,
        a=float(a),
        radius=float(radius),
        cells_per_axis=int(cells_per_axis),
        quadrature_order=0,
        active_cells=active,
        cell_centers=centers,
        row_sums=row_sums,
        hole_center=None,
        hole_radius=0.0,
        method=method,
        samples_per_cell=None,
        seed=None,
        survivor_horizon=int(survivor_horizon),
        survivor_rule=f"box_center_mask_horizon_{int(survivor_horizon)}",
        grid_offset=float(grid_offset),
    )


def assemble_shifted_overlap_ulam(
    a: float,
    radius: float,
    cells_per_axis: int,
    grid_offset: float,
) -> UlamAssembly:
    """Assemble overlap transitions with clipped shifted boundary cells.

    The offset is measured in nominal cell widths and must lie in
    [-0.5, 0.5]. The outer box boundaries remain fixed, producing two clipped
    boundary cells. This diagnostic supports only H=0 and no holes.
    """

    if radius <= 0.0:
        raise ValueError("radius must be positive")
    if a < 0.0:
        raise ValueError(
            "shifted overlap assembly currently requires nonnegative a"
        )
    if cells_per_axis < 2:
        raise ValueError("cells_per_axis must be at least two")
    if not -0.5 <= float(grid_offset) <= 0.5:
        raise ValueError("grid_offset must lie in [-0.5, 0.5]")
    nominal_width = 2.0 * float(radius) / cells_per_axis
    interior = -float(radius) + (
        np.arange(1, cells_per_axis, dtype=float) + float(grid_offset)
    ) * nominal_width
    edges = np.concatenate(
        (
            np.asarray([-float(radius)]),
            interior,
            np.asarray([float(radius)]),
        )
    )
    active = np.ones(cells_per_axis**2, dtype=bool)
    return _assemble_overlap_from_edges(
        a,
        radius,
        cells_per_axis,
        edges,
        active,
        survivor_horizon=0,
        method="semi_analytic_overlap_shifted",
        grid_offset=float(grid_offset),
    )


def _dominant_eigenvectors(matrix: csr_matrix, count: int) -> tuple[np.ndarray, np.ndarray]:
    size = matrix.shape[0]
    if matrix.nnz == 0 or not np.any(matrix.data):
        effective_count = min(max(count, 1), size)
        return (
            np.zeros(effective_count, dtype=np.complex128),
            np.zeros((size, effective_count), dtype=np.complex128),
        )
    if size <= 128:
        values, vectors = np.linalg.eig(matrix.toarray())
        order = np.argsort(-np.abs(values))[:count]
        return values[order], vectors[:, order]
    effective_count = min(count, size - 2)
    values, vectors = eigs(
        matrix,
        k=effective_count,
        which="LM",
        tol=1.0e-11,
        maxiter=max(20_000, 20 * size),
    )
    order = np.argsort(-np.abs(values))
    return values[order], vectors[:, order]


def dominant_spectrum(
    assembly: UlamAssembly,
    eigenvalue_count: int = 8,
) -> SpectrumAudit:
    """Compute dominant density-operator eigenpairs with residuals."""

    density_operator = assembly.matrix.transpose().tocsr()
    if density_operator.nnz == 0 or not np.any(density_operator.data):
        reference_fixed_point = fixed_points(assembly.a)[0]
        zero_audit = EigenpairAudit(
            eigenvalue=0.0j,
            modulus=0.0,
            right_residual=0.0,
            left_residual=0.0,
            condition_estimate=float("inf"),
        )
        return SpectrumAudit(
            eigenpairs=(zero_audit,),
            leading_eigenvalue=0.0j,
            escape_rate=float("inf"),
            elliptic_mass_fraction_r03=0.0,
            reference_fixed_point_stability=reference_fixed_point.stability,
        )
    right_values, right_vectors = _dominant_eigenvectors(density_operator, eigenvalue_count)
    left_values, left_vectors = _dominant_eigenvectors(density_operator.getH().tocsr(), eigenvalue_count)
    audits: list[EigenpairAudit] = []
    for index, value_raw in enumerate(right_values):
        value = complex(value_raw)
        right = right_vectors[:, index]
        right /= np.linalg.norm(right)
        left_index = int(np.argmin(np.abs(left_values - np.conjugate(value))))
        left_value = complex(left_values[left_index])
        left = left_vectors[:, left_index]
        left /= np.linalg.norm(left)
        right_residual = float(np.linalg.norm(density_operator.dot(right) - value * right))
        left_residual = float(np.linalg.norm(density_operator.getH().dot(left) - left_value * left))
        overlap = abs(np.vdot(left, right))
        condition = math.inf if overlap == 0.0 else float(1.0 / overlap)
        audits.append(
            EigenpairAudit(
                eigenvalue=value,
                modulus=abs(value),
                right_residual=right_residual,
                left_residual=left_residual,
                condition_estimate=condition,
            )
        )

    # Select a Perron candidate by modulus and then real part to avoid arbitrary
    # ordering among cyclic peripheral modes.
    spectral_radius = max(item.modulus for item in audits)
    peripheral = [
        index
        for index, item in enumerate(audits)
        if abs(item.modulus - spectral_radius)
        <= 1.0e-8 * max(1.0, spectral_radius)
    ]
    leading_index = max(
        peripheral,
        key=lambda index: (
            audits[index].eigenvalue.real,
            -abs(audits[index].eigenvalue.imag),
        ),
    )
    leading = audits[leading_index].eigenvalue
    leading_modulus = abs(leading)
    escape_rate = 0.0 if leading_modulus >= 1.0 else -math.log(max(leading_modulus, np.finfo(float).tiny))

    density = np.abs(right_vectors[:, leading_index])
    density_sum = float(np.sum(density))
    if density_sum > 0.0:
        density /= density_sum
    reference_fixed_point = fixed_points(assembly.a)[0]
    center = (
        assembly.hole_center
        if assembly.hole_center is not None
        else (reference_fixed_point.coordinate, reference_fixed_point.coordinate)
    )
    near = (
        (assembly.cell_centers[:, 0] - center[0]) ** 2
        + (assembly.cell_centers[:, 1] - center[1]) ** 2
    ) <= 0.3**2
    mass_fraction = float(np.sum(density[near]))
    return SpectrumAudit(
        eigenpairs=tuple(audits),
        leading_eigenvalue=leading,
        escape_rate=escape_rate,
        elliptic_mass_fraction_r03=mass_fraction,
        reference_fixed_point_stability=reference_fixed_point.stability,
    )
