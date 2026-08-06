"""Finite-volume operators on the frozen R059 four-h-set domain.

The ordinary :mod:`henon_zeta.operator` helpers use one square grid (and, in
some modes, a finite-time survivor mask).  R059 needs a different object: four
rectangles are indexed separately, with all mass outside their union discarded.
This module keeps that indexing and the sampling rules explicit so that the
producer and the independent checker can bind the same serialized schema.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import numpy as np
from numpy.typing import NDArray
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import ArpackNoConvergence, eigs
from scipy.stats import qmc


FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]

STATE_ORDER: tuple[str, ...] = ("--", "-+", "+-", "++")
# (x_lower, x_upper, y_lower, y_upper); decimal values are only used for
# floating-point quadrature, while the exact rational values are persisted by
# the producer schema.
HSET_BOUNDS: dict[str, tuple[float, float, float, float]] = {
    "--": (-5.0 / 8.0, -1.0 / 3.0, -81.0 / 128.0, -5.0 / 16.0),
    "-+": (-5.0 / 8.0, -1.0 / 3.0, 5.0 / 16.0, 81.0 / 128.0),
    "+-": (1.0 / 3.0, 5.0 / 8.0, -81.0 / 128.0, -5.0 / 16.0),
    "++": (1.0 / 3.0, 5.0 / 8.0, 5.0 / 16.0, 81.0 / 128.0),
}
HSET_BOUNDS_RATIONAL: dict[str, tuple[str, ...]] = {
    "--": ("-5/8", "-1/3", "-81/128", "-5/16"),
    "-+": ("-5/8", "-1/3", "5/16", "81/128"),
    "+-": ("1/3", "5/8", "-81/128", "-5/16"),
    "++": ("1/3", "5/8", "5/16", "81/128"),
}


@dataclass(frozen=True)
class RestrictedAssembly:
    """Sparse row-substochastic map and deterministic assembly diagnostics."""

    matrix: csr_matrix
    cells_per_axis: int
    method: str
    quadrature_order: int
    samples_per_cell: int
    seed: int | None
    boundary_hits: int
    hset_boundary_hits: int
    cell_boundary_hits: int
    source_sample_count: int
    target_hit_count: int
    row_sums: FloatArray
    source_centers: FloatArray


def _grid_centers(state: str, cells_per_axis: int) -> tuple[FloatArray, float, float]:
    x_lower, x_upper, y_lower, y_upper = HSET_BOUNDS[state]
    x_width = (x_upper - x_lower) / cells_per_axis
    y_width = (y_upper - y_lower) / cells_per_axis
    x_axis = x_lower + (np.arange(cells_per_axis, dtype=float) + 0.5) * x_width
    y_axis = y_lower + (np.arange(cells_per_axis, dtype=float) + 0.5) * y_width
    x_grid, y_grid = np.meshgrid(x_axis, y_axis, indexing="xy")
    return np.column_stack((x_grid.ravel(), y_grid.ravel())), x_width, y_width


def restricted_source_grid(cells_per_axis: int) -> tuple[FloatArray, IntArray]:
    """Return source centers and their contiguous four-h-set global indices."""

    if cells_per_axis < 2:
        raise ValueError("cells_per_axis must be at least two")
    chunks: list[FloatArray] = []
    for state in STATE_ORDER:
        centers, _, _ = _grid_centers(state, cells_per_axis)
        chunks.append(centers)
    centers = np.concatenate(chunks, axis=0)
    indices = np.arange(centers.shape[0], dtype=np.int64)
    return centers, indices


def _target_lookup(
    image_x: FloatArray,
    image_y: FloatArray,
    cells_per_axis: int,
) -> tuple[IntArray, NDArray[np.bool_], int, int]:
    """Map image points to target cells, excluding all exact boundaries.

    The returned target indices are global indices in the same state-major,
    y-major/x-minor order as :func:`restricted_source_grid`.  Points on an
    h-set boundary or an internal target-cell boundary are counted and
    excluded, making the half-open convention explicit rather than relying on
    ``floor`` at an endpoint.
    """

    n = image_x.size
    target = np.full(n, -1, dtype=np.int64)
    valid = np.zeros(n, dtype=bool)
    hset_hits = 0
    cell_hits = 0
    for state_index, state in enumerate(STATE_ORDER):
        x_lower, x_upper, y_lower, y_upper = HSET_BOUNDS[state]
        # Closed membership is used only to identify boundary hits.  Interior
        # membership is the actual transfer-domain target.
        closed = (
            (image_x >= x_lower)
            & (image_x <= x_upper)
            & (image_y >= y_lower)
            & (image_y <= y_upper)
        )
        if not np.any(closed):
            continue
        interior = (
            (image_x > x_lower)
            & (image_x < x_upper)
            & (image_y > y_lower)
            & (image_y < y_upper)
        )
        state_hset = closed & ~interior
        hset_hits += int(np.count_nonzero(state_hset))
        if not np.any(interior):
            continue
        x_width = (x_upper - x_lower) / cells_per_axis
        y_width = (y_upper - y_lower) / cells_per_axis
        ux = (image_x[interior] - x_lower) / x_width
        uy = (image_y[interior] - y_lower) / y_width
        ix = np.floor(ux).astype(np.int64)
        iy = np.floor(uy).astype(np.int64)
        # Exact floating-point hits are the only points counted here.  The
        # source rules use interior quadrature/Sobol points, so this diagnostic
        # remains zero unless the map lands exactly on a frozen boundary.
        on_cell_boundary = (ux == np.floor(ux)) | (uy == np.floor(uy))
        cell_hits += int(np.count_nonzero(on_cell_boundary))
        accepted = ~on_cell_boundary & (ix >= 0) & (ix < cells_per_axis) & (iy >= 0) & (iy < cells_per_axis)
        positions = np.flatnonzero(interior)
        accepted_positions = positions[accepted]
        target[accepted_positions] = (
            state_index * cells_per_axis * cells_per_axis
            + iy[accepted] * cells_per_axis
            + ix[accepted]
        )
        valid[accepted_positions] = True
    return target, valid, hset_hits, cell_hits


def _assemble_from_samples(
    a: float,
    cells_per_axis: int,
    sample_batches: Iterable[tuple[FloatArray, float]],
    source_centers: FloatArray,
    source_indices: IntArray,
    samples_per_cell: int,
    method: str,
    quadrature_order: int,
    seed: int | None,
) -> RestrictedAssembly:
    n_cells = source_centers.shape[0]
    row_chunks: list[IntArray] = []
    col_chunks: list[IntArray] = []
    value_chunks: list[FloatArray] = []
    boundary_hits = 0
    hset_boundary_hits = 0
    cell_boundary_hits = 0
    target_hit_count = 0
    source_sample_count = 0
    for points, sample_weight in sample_batches:
        if points.shape != source_centers.shape:
            raise ValueError("sample batch shape does not match source grid")
        source_sample_count += points.shape[0]
        image_x = 1.0 - float(a) * points[:, 0] ** 2 - points[:, 1]
        image_y = points[:, 0]
        target, valid, hset_hits, cell_hits = _target_lookup(
            image_x, image_y, cells_per_axis
        )
        hset_boundary_hits += hset_hits
        cell_boundary_hits += cell_hits
        boundary_hits += hset_hits + cell_hits
        target_hit_count += int(np.count_nonzero(valid))
        if not np.any(valid):
            continue
        valid_sources = source_indices[valid]
        row_chunks.append(valid_sources)
        col_chunks.append(target[valid])
        value_chunks.append(np.full(valid_sources.size, sample_weight, dtype=float))
    if row_chunks:
        rows = np.concatenate(row_chunks)
        columns = np.concatenate(col_chunks)
        values = np.concatenate(value_chunks)
    else:
        rows = np.empty(0, dtype=np.int64)
        columns = np.empty(0, dtype=np.int64)
        values = np.empty(0, dtype=float)
    matrix = csr_matrix(
        (values, (rows, columns)), shape=(4 * cells_per_axis * cells_per_axis,) * 2
    )
    matrix.sum_duplicates()
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    if np.max(row_sums, initial=0.0) > 1.0 + 1.0e-12:
        raise RuntimeError("restricted operator row sum exceeds one")
    return RestrictedAssembly(
        matrix=matrix,
        cells_per_axis=cells_per_axis,
        method=method,
        quadrature_order=quadrature_order,
        samples_per_cell=samples_per_cell,
        seed=seed,
        boundary_hits=boundary_hits,
        hset_boundary_hits=hset_boundary_hits,
        cell_boundary_hits=cell_boundary_hits,
        source_sample_count=source_sample_count,
        target_hit_count=target_hit_count,
        row_sums=row_sums,
        source_centers=source_centers,
    )


def assemble_restricted_gauss(
    a: float = 6.0,
    cells_per_axis: int = 24,
    quadrature_order: int = 8,
) -> RestrictedAssembly:
    """Assemble tensor Gauss--Legendre order ``quadrature_order``."""

    if quadrature_order < 1:
        raise ValueError("quadrature_order must be positive")
    source_centers, source_indices = restricted_source_grid(cells_per_axis)
    nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)
    batches: list[tuple[FloatArray, float]] = []
    # Build state-major arrays so source-cell local widths are respected.
    for x_node, x_weight in zip(nodes, weights):
        for y_node, y_weight in zip(nodes, weights):
            points = np.empty_like(source_centers)
            offset = 0
            for state in STATE_ORDER:
                centers, x_width, y_width = _grid_centers(state, cells_per_axis)
                count = centers.shape[0]
                points[offset : offset + count, 0] = centers[:, 0] + 0.5 * x_width * x_node
                points[offset : offset + count, 1] = centers[:, 1] + 0.5 * y_width * y_node
                offset += count
            batches.append((points, float(x_weight * y_weight / 4.0)))
    return _assemble_from_samples(
        a,
        cells_per_axis,
        batches,
        source_centers,
        source_indices,
        quadrature_order**2,
        "tensor_gauss_legendre",
        quadrature_order,
        None,
    )


def assemble_restricted_sobol(
    a: float = 6.0,
    cells_per_axis: int = 24,
    samples_per_cell: int = 64,
    seed: int = 20260801,
) -> RestrictedAssembly:
    """Assemble randomized-shift Sobol samples with a frozen seed."""

    if samples_per_cell < 1 or samples_per_cell & (samples_per_cell - 1):
        raise ValueError("samples_per_cell must be a positive power of two")
    source_centers, source_indices = restricted_source_grid(cells_per_axis)
    # Per-state widths are repeated in the source-major ordering.
    widths = np.concatenate(
        [
            np.tile(
                np.asarray([_grid_centers(state, cells_per_axis)[1], _grid_centers(state, cells_per_axis)[2]]),
                (cells_per_axis * cells_per_axis, 1),
            )
            for state in STATE_ORDER
        ],
        axis=0,
    )
    exponent = int(round(math.log2(samples_per_cell)))
    sampler = qmc.Sobol(d=2, scramble=True, seed=int(seed))
    base_points = sampler.random_base2(exponent)
    generator = np.random.default_rng(int(seed) + 1_000_003)
    shifts = generator.random((source_centers.shape[0], 2))
    batches: list[tuple[FloatArray, float]] = []
    for base_point in base_points:
        unit = np.mod(base_point + shifts, 1.0)
        points = source_centers + (unit - 0.5) * widths
        batches.append((points, 1.0 / samples_per_cell))
    return _assemble_from_samples(
        a,
        cells_per_axis,
        batches,
        source_centers,
        source_indices,
        samples_per_cell,
        "random_shift_sobol",
        0,
        int(seed),
    )


def _eigs_with_retry(matrix: csr_matrix, count: int) -> tuple[np.ndarray, np.ndarray]:
    n = matrix.shape[0]
    k = min(count, max(1, n - 2))
    kwargs = dict(which="LM", tol=1.0e-10, maxiter=max(20_000, 20 * n))
    try:
        return eigs(matrix, k=k, **kwargs)
    except ArpackNoConvergence as exc:
        if exc.eigenvalues is not None and len(exc.eigenvalues) >= min(2, k):
            return exc.eigenvalues, exc.eigenvectors
        if k > 1:
            return eigs(matrix, k=1, **kwargs)
        raise


def restricted_spectrum(
    matrix: csr_matrix,
    eigenvalue_count: int = 8,
) -> dict[str, object]:
    """Return dominant eigenpairs and residuals for the density transpose."""

    density = matrix.transpose().tocsr()
    if density.nnz == 0 or not np.any(density.data):
        return {
            "eigenpairs": [],
            "leading_eigenvalue": [0.0, 0.0],
            "leading_modulus": 0.0,
            "maximum_residual": 0.0,
        }
    values, vectors = _eigs_with_retry(density, eigenvalue_count)
    order = np.argsort(-np.abs(values))
    values = values[order]
    vectors = vectors[:, order]
    pairs: list[dict[str, object]] = []
    for index, raw in enumerate(values):
        value = complex(raw)
        vector = vectors[:, index]
        norm = np.linalg.norm(vector)
        if norm:
            vector = vector / norm
        residual = float(np.linalg.norm(density.dot(vector) - value * vector))
        pairs.append(
            {
                "eigenvalue": [float(value.real), float(value.imag)],
                "modulus": float(abs(value)),
                "residual": residual,
            }
        )
    leading = pairs[0]
    maximum_residual = max(float(row["residual"]) for row in pairs)
    return {
        "eigenpairs": pairs,
        "leading_eigenvalue": leading["eigenvalue"],
        "leading_modulus": float(leading["modulus"]),
        "maximum_residual": maximum_residual,
    }
