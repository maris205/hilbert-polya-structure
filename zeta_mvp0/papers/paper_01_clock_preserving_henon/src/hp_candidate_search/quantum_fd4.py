"""Independent fourth-order gauge-covariant finite-difference audit."""

from __future__ import annotations

from math import log, pi, sqrt

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

from .quantum_fd import GridSpec
from .warped_henon import TWO_PI, centered_fixed_point, henon_inverse_iterate


def _grid_geometry(
    spec: GridSpec,
) -> tuple[np.ndarray, np.ndarray, float, float, tuple[float, ...]]:
    wall_energy = spec.wall_factor * spec.target_energy
    radius = sqrt(log(wall_energy / TWO_PI) / pi)
    angles = np.linspace(0.0, TWO_PI, 8192, endpoint=False)
    boundary = np.empty((len(angles), 2), dtype=float)
    for index, angle in enumerate(angles):
        u = radius * np.array([np.cos(angle), np.sin(angle)])
        boundary[index] = henon_inverse_iterate(
            u, spec.a, spec.n, centered=spec.centered
        )
    xmin = float(boundary[:, 0].min()) - 3.0 * spec.nominal_spacing
    xmax = float(boundary[:, 0].max()) + 3.0 * spec.nominal_spacing
    ymin = float(boundary[:, 1].min()) - 3.0 * spec.nominal_spacing
    ymax = float(boundary[:, 1].max()) + 3.0 * spec.nominal_spacing
    intervals_x = max(6, int(np.ceil((xmax - xmin) / spec.nominal_spacing)))
    intervals_y = max(6, int(np.ceil((ymax - ymin) / spec.nominal_spacing)))
    hx = (xmax - xmin) / intervals_x
    hy = (ymax - ymin) / intervals_y
    x = np.linspace(xmin, xmax, intervals_x + 1)[1:-1]
    y = np.linspace(ymin, ymax, intervals_y + 1)[1:-1]
    return x, y, hx, hy, (xmin, xmax, ymin, ymax, radius, wall_energy)


def _centered_iterate(
    x: np.ndarray, y: np.ndarray, a: float, n: int
) -> tuple[np.ndarray, np.ndarray]:
    fixed = centered_fixed_point(a)
    u0 = np.asarray(x, dtype=float)
    u1 = np.asarray(y, dtype=float)
    for _ in range(n):
        new0 = -2.0 * a * fixed * u0 - a * u0 * u0 - u1
        u0, u1 = new0, u0
    return u0, u1


def build_grid_operator_fourth(
    spec: GridSpec,
) -> tuple[sparse.csr_matrix, dict[str, object]]:
    """Build a Hermitian fourth-order Peierls operator.

    Values outside the interior lattice are set to zero.  This is a
    Dirichlet zero-extension closure; the remote exponential wall suppresses
    its effect on the retained low modes.
    """

    if spec.target_energy <= TWO_PI:
        raise ValueError("target_energy must exceed 2*pi")
    if spec.nominal_spacing <= 0.0:
        raise ValueError("nominal_spacing must be positive")
    if spec.gauge not in {"symmetric", "landau"}:
        raise ValueError("gauge must be 'symmetric' or 'landau'")

    x, y, hx, hy, bounds = _grid_geometry(spec)
    nx, ny = len(x), len(y)
    size = nx * ny
    if spec.eigenvalue_count >= size - 1:
        raise ValueError("too many requested eigenvalues for the grid")

    xx, yy = np.meshgrid(x, y, indexing="xy")
    u0, u1 = _centered_iterate(xx, yy, spec.a, spec.n)
    phi = pi * (u0 * u0 + u1 * u1)
    potential_clip = bounds[-1] * 1.0e4
    potential = np.minimum(
        TWO_PI * np.exp(np.minimum(phi, log(potential_clip / TWO_PI))),
        potential_clip,
    )

    diagonal = (
        np.full(
            size,
            1.25 / hx**2 + 1.25 / hy**2,
            dtype=complex,
        )
        + potential.ravel(order="C")
    )
    rows: list[np.ndarray] = [np.arange(size)]
    columns: list[np.ndarray] = [np.arange(size)]
    data: list[np.ndarray] = [diagonal]

    for step, coefficient in ((1, -2.0 / 3.0), (2, 1.0 / 24.0)):
        j_indices, i_indices = np.meshgrid(
            np.arange(ny), np.arange(nx - step), indexing="ij"
        )
        lower = (j_indices * nx + i_indices).ravel()
        upper = lower + step
        y_links = y[j_indices].ravel()
        displacement = step * hx
        if spec.gauge == "symmetric":
            phase = np.exp(
                0.5j * spec.magnetic_field * y_links * displacement
            )
        else:
            phase = np.ones_like(y_links, dtype=complex)
        coupling = coefficient / hx**2 * phase
        rows.extend((lower, upper))
        columns.extend((upper, lower))
        data.extend((coupling, np.conjugate(coupling)))

        j_indices, i_indices = np.meshgrid(
            np.arange(ny - step), np.arange(nx), indexing="ij"
        )
        lower = (j_indices * nx + i_indices).ravel()
        upper = lower + step * nx
        x_links = x[i_indices].ravel()
        displacement = step * hy
        if spec.gauge == "symmetric":
            phase = np.exp(
                -0.5j * spec.magnetic_field * x_links * displacement
            )
        else:
            phase = np.exp(
                -1.0j * spec.magnetic_field * x_links * displacement
            )
        coupling = coefficient / hy**2 * phase
        rows.extend((lower, upper))
        columns.extend((upper, lower))
        data.extend((coupling, np.conjugate(coupling)))

    matrix = sparse.coo_matrix(
        (np.concatenate(data), (np.concatenate(rows), np.concatenate(columns))),
        shape=(size, size),
        dtype=complex,
    ).tocsr()
    matrix.sum_duplicates()
    metadata: dict[str, object] = {
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
        "stencil_order": 4,
        "boundary_closure": "Dirichlet zero extension",
    }
    return matrix, metadata


def compute_eigenvalues_fourth(
    spec: GridSpec,
) -> tuple[np.ndarray, dict[str, object]]:
    """Compute low eigenvalues and numerical-integrity metadata."""

    matrix, metadata = build_grid_operator_fourth(spec)
    guard_modes = min(20, matrix.shape[0] - spec.eigenvalue_count - 2)
    requested_modes = spec.eigenvalue_count + max(0, guard_modes)
    index = np.arange(matrix.shape[0], dtype=float)
    v0 = np.sin((index + 1.0) * np.sqrt(2.0)) + 0.5 * np.cos(
        (index + 1.0) * np.sqrt(3.0)
    )
    v0 /= np.linalg.norm(v0)
    values, vectors = eigsh(
        matrix,
        k=requested_modes,
        sigma=0.0,
        which="LM",
        return_eigenvectors=True,
        tol=1.0e-12,
        maxiter=max(5000, 20 * requested_modes),
        v0=v0,
    )
    order = np.argsort(values.real)
    keep = order[: spec.eigenvalue_count]
    values = np.asarray(values.real[keep], dtype=float)
    vectors = vectors[:, keep]
    residual_matrix = matrix @ vectors - vectors * values[np.newaxis, :]
    residuals = np.linalg.norm(residual_matrix, axis=0) / np.maximum(
        1.0, np.abs(values)
    )
    gram = vectors.conjugate().T @ vectors
    metadata.update(
        {
            "lowest_eigenvalue": float(values[0]),
            "highest_eigenvalue": float(values[-1]),
            "monotone": bool(np.all(np.diff(values) >= 0.0)),
            "max_relative_eigen_residual": float(np.max(residuals)),
            "median_relative_eigen_residual": float(np.median(residuals)),
            "max_orthogonality_defect": float(
                np.max(np.abs(gram - np.eye(len(values))))
            ),
            "deterministic_v0": True,
            "ritz_guard_modes": int(max(0, guard_modes)),
            "ritz_pairs_requested": int(requested_modes),
            "eigsh_tolerance": 1.0e-12,
        }
    )
    return values, metadata
