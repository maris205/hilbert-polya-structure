"""Gauge-covariant finite differences for warped-Hénon quantum pilots."""

from __future__ import annotations

from dataclasses import dataclass
from math import log, pi, sqrt

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

from .warped_henon import TWO_PI, centered_fixed_point, henon_inverse_iterate

PRODUCTION_DISCARD_LOW = 25
PRODUCTION_DISCARD_HIGH = 15


@dataclass(frozen=True)
class GridSpec:
    a: float
    n: int
    magnetic_field: float
    target_energy: float
    nominal_spacing: float
    eigenvalue_count: int
    wall_factor: float = 100.0
    centered: bool = True
    gauge: str = "symmetric"


def classical_smooth_count(energy: np.ndarray | float) -> np.ndarray:
    """Exact classical Riemann--von Mangoldt clock for energies above 2*pi."""

    values = np.asarray(energy, dtype=float)
    return values / TWO_PI * np.log(values / TWO_PI) - values / TWO_PI + 1.0


def preimage_disk_bounds(
    a: float,
    n: int,
    radius: float,
    *,
    centered: bool = True,
    samples: int = 8192,
) -> tuple[float, float, float, float]:
    """Bound the preimage of a disk using its polynomial Jordan boundary."""

    points = np.empty((samples, 2), dtype=float)
    for index, angle in enumerate(np.linspace(0.0, TWO_PI, samples, endpoint=False)):
        u = radius * np.array([np.cos(angle), np.sin(angle)])
        points[index] = henon_inverse_iterate(u, a, n, centered=centered)
    return (
        float(points[:, 0].min()),
        float(points[:, 0].max()),
        float(points[:, 1].min()),
        float(points[:, 1].max()),
    )


def _grid_geometry(spec: GridSpec) -> tuple[np.ndarray, np.ndarray, float, float, tuple[float, ...]]:
    wall_energy = spec.wall_factor * spec.target_energy
    radius = sqrt(log(wall_energy / TWO_PI) / pi)
    xmin, xmax, ymin, ymax = preimage_disk_bounds(
        spec.a, spec.n, radius, centered=spec.centered
    )
    padding = 3.0 * spec.nominal_spacing
    xmin -= padding
    xmax += padding
    ymin -= padding
    ymax += padding
    intervals_x = max(4, int(np.ceil((xmax - xmin) / spec.nominal_spacing)))
    intervals_y = max(4, int(np.ceil((ymax - ymin) / spec.nominal_spacing)))
    hx = (xmax - xmin) / intervals_x
    hy = (ymax - ymin) / intervals_y
    x = np.linspace(xmin, xmax, intervals_x + 1)[1:-1]
    y = np.linspace(ymin, ymax, intervals_y + 1)[1:-1]
    return x, y, hx, hy, (xmin, xmax, ymin, ymax, radius, wall_energy)


def _centered_iterate_arrays(
    x: np.ndarray, y: np.ndarray, a: float, n: int
) -> tuple[np.ndarray, np.ndarray]:
    fixed = centered_fixed_point(a)
    u0 = np.asarray(x, dtype=float)
    u1 = np.asarray(y, dtype=float)
    for _ in range(n):
        new0 = -2.0 * a * fixed * u0 - a * u0 * u0 - u1
        u0, u1 = new0, u0
    return u0, u1


def build_grid_operator(
    spec: GridSpec,
) -> tuple[sparse.csr_matrix, dict[str, float | int | tuple[float, ...]]]:
    """Build a Hermitian Peierls finite-difference matrix with Dirichlet walls."""

    if spec.target_energy <= TWO_PI:
        raise ValueError("target_energy must exceed 2*pi")
    if spec.nominal_spacing <= 0.0:
        raise ValueError("nominal_spacing must be positive")
    if spec.gauge not in {"symmetric", "landau"}:
        raise ValueError("gauge must be 'symmetric' or 'landau'")
    x, y, hx, hy, bounds = _grid_geometry(spec)
    nx, ny = len(x), len(y)
    if spec.eigenvalue_count >= nx * ny - 1:
        raise ValueError("too many requested eigenvalues for the grid")
    xx, yy = np.meshgrid(x, y, indexing="xy")
    u0, u1 = _centered_iterate_arrays(xx, yy, spec.a, spec.n)
    phi = pi * (u0 * u0 + u1 * u1)
    potential_clip = bounds[-1] * 1.0e4
    potential = np.minimum(TWO_PI * np.exp(np.minimum(phi, log(potential_clip / TWO_PI))), potential_clip)

    size = nx * ny
    diagonal = (
        np.full(size, 1.0 / hx**2 + 1.0 / hy**2, dtype=complex)
        + potential.ravel(order="C")
    )
    rows: list[np.ndarray] = [np.arange(size)]
    columns: list[np.ndarray] = [np.arange(size)]
    data: list[np.ndarray] = [diagonal]

    # Links use U=exp(-i integral A.dq).  Midpoint quadrature is exact for
    # both supported linear gauges.
    j_indices, i_indices = np.meshgrid(np.arange(ny), np.arange(nx - 1), indexing="ij")
    lower = (j_indices * nx + i_indices).ravel()
    upper = lower + 1
    y_links = y[j_indices].ravel()
    if spec.gauge == "symmetric":
        phase_x = np.exp(0.5j * spec.magnetic_field * y_links * hx)
    else:  # Landau gauge A=(0,Bx)
        phase_x = np.ones_like(y_links, dtype=complex)
    coupling_x = -0.5 / hx**2 * phase_x
    rows.extend((lower, upper))
    columns.extend((upper, lower))
    data.extend((coupling_x, np.conjugate(coupling_x)))

    # y links: A_y=B*x/2.
    j_indices, i_indices = np.meshgrid(np.arange(ny - 1), np.arange(nx), indexing="ij")
    lower = (j_indices * nx + i_indices).ravel()
    upper = lower + nx
    x_links = x[i_indices].ravel()
    if spec.gauge == "symmetric":
        phase_y = np.exp(-0.5j * spec.magnetic_field * x_links * hy)
    else:
        phase_y = np.exp(-1.0j * spec.magnetic_field * x_links * hy)
    coupling_y = -0.5 / hy**2 * phase_y
    rows.extend((lower, upper))
    columns.extend((upper, lower))
    data.extend((coupling_y, np.conjugate(coupling_y)))

    matrix = sparse.coo_matrix(
        (np.concatenate(data), (np.concatenate(rows), np.concatenate(columns))),
        shape=(size, size),
        dtype=complex,
    ).tocsr()
    matrix.sum_duplicates()
    metadata: dict[str, float | int | tuple[float, ...]] = {
        "nx": nx,
        "ny": ny,
        "matrix_size": size,
        "hx": float(hx),
        "hy": float(hy),
        "bounds": tuple(float(value) for value in bounds[:4]),
        "preimage_wall_radius": float(bounds[4]),
        "wall_energy": float(bounds[5]),
        "potential_min": float(potential.min()),
        "potential_max_clipped": float(potential.max()),
    }
    return matrix, metadata


def compute_eigenvalues(spec: GridSpec) -> tuple[np.ndarray, dict[str, object]]:
    """Compute the requested low spectrum by Hermitian shift-invert Lanczos."""

    matrix, metadata = build_grid_operator(spec)
    index = np.arange(matrix.shape[0], dtype=float)
    v0 = np.sin((index + 1.0) * np.sqrt(2.0)) + 0.5 * np.cos(
        (index + 1.0) * np.sqrt(3.0)
    )
    v0 /= np.linalg.norm(v0)
    values, vectors = eigsh(
        matrix,
        k=spec.eigenvalue_count,
        sigma=0.0,
        which="LM",
        return_eigenvectors=True,
        tol=2.0e-10,
        maxiter=max(5000, 20 * spec.eigenvalue_count),
        v0=v0,
    )
    order = np.argsort(values.real)
    values = np.asarray(values.real[order], dtype=float)
    vectors = vectors[:, order]
    residual_matrix = matrix @ vectors - vectors * values[np.newaxis, :]
    residuals = np.linalg.norm(residual_matrix, axis=0) / np.maximum(1.0, np.abs(values))
    gram = vectors.conjugate().T @ vectors
    orthogonality_defect = np.max(np.abs(gram - np.eye(len(values))))
    residual_metadata: dict[str, object] = {
        **metadata,
        "lowest_eigenvalue": float(values[0]),
        "highest_eigenvalue": float(values[-1]),
        "monotone": bool(np.all(np.diff(values) >= 0.0)),
        "max_relative_eigen_residual": float(np.max(residuals)),
        "median_relative_eigen_residual": float(np.median(residuals)),
        "max_orthogonality_defect": float(orthogonality_defect),
        "deterministic_v0": True,
    }
    return values, residual_metadata


def spectral_window(
    eigenvalues: np.ndarray,
    *,
    discard_low: int = PRODUCTION_DISCARD_LOW,
    discard_high: int = PRODUCTION_DISCARD_HIGH,
) -> np.ndarray:
    """Return the sorted frozen interior spectral window."""

    # Extrapolated nearly degenerate pairs can cross by roundoff.  Sorting is
    # part of the definition of spectral spacing, not a change to the data.
    values = np.sort(np.asarray(eigenvalues, dtype=float))
    if discard_low + discard_high + 3 >= len(values):
        raise ValueError("not enough eigenvalues after edge discards")
    return values[discard_low : len(values) - discard_high]


def spacing_diagnostics(
    eigenvalues: np.ndarray,
    *,
    discard_low: int = PRODUCTION_DISCARD_LOW,
    discard_high: int = PRODUCTION_DISCARD_HIGH,
) -> dict[str, float | int]:
    """Return zero-free spacing diagnostics using the exact smooth clock."""

    core = spectral_window(
        eigenvalues, discard_low=discard_low, discard_high=discard_high
    )
    raw_spacings = np.diff(core)
    numerator = np.minimum(raw_spacings[:-1], raw_spacings[1:])
    denominator = np.maximum(raw_spacings[:-1], raw_spacings[1:])
    ratios = np.divide(
        numerator,
        denominator,
        out=np.zeros_like(numerator),
        where=denominator > 0.0,
    )
    unfolded = classical_smooth_count(core)
    unfolded_spacings = np.diff(unfolded)
    return {
        "levels_used": int(len(core)),
        "energy_min_used": float(core[0]),
        "energy_max_used": float(core[-1]),
        "mean_spacing_ratio": float(np.mean(ratios)),
        "median_spacing_ratio": float(np.median(ratios)),
        "mean_unfolded_spacing": float(np.mean(unfolded_spacings)),
        "std_unfolded_spacing": float(np.std(unfolded_spacings)),
        "fraction_near_degenerate_1e-3": float(
            np.mean(raw_spacings < 1.0e-3 * np.median(raw_spacings))
        ),
    }
