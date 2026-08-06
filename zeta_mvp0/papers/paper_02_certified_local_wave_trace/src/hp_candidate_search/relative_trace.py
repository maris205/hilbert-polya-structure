"""Common-grid relative spectral diagnostics for the R200 pilot.

The routines in this module deliberately construct the radial reference and
the Hénon-warped operator on one finite-dimensional Hilbert space.  The
resulting matrix diagnostics are finite-box quantities; in particular they
must not be used to infer full-space trace-class membership of the first
resolvent difference.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from math import log, pi, sqrt
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from scipy import sparse
from scipy.signal import find_peaks
from scipy.sparse.linalg import eigsh, splu

from .quantum_fd import _centered_iterate_arrays, preimage_disk_bounds
from .warped_henon import TWO_PI


@dataclass(frozen=True)
class CommonGridSpec:
    """Frozen construction parameters for a common-grid operator pair."""

    a: float = 1.02
    n: int = 1
    magnetic_field: float = 0.0
    target_energy: float = 180.0
    nominal_spacing: float = 0.14
    eigenvalue_count: int = 96
    wall_factor: float = 100.0
    box_scale: float = 1.0
    boundary_padding: float = 0.20
    cap_multiplier: float = 100.0
    centered: bool = True
    gauge: str = "symmetric"
    boundary_samples: int = 8192


@dataclass
class CommonGridPair:
    """Two Schrödinger matrices sharing a grid, kinetic term, and boundary."""

    spec: CommonGridSpec
    h0: sparse.csr_matrix
    h1: sparse.csr_matrix
    kinetic: sparse.csr_matrix
    potential0: np.ndarray
    potential1: np.ndarray
    x: np.ndarray
    y: np.ndarray
    metadata: dict[str, Any]


def file_sha256(path: str | Path) -> str:
    """Return the SHA-256 digest of one source or protocol file."""

    digest = sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _validate_spec(spec: CommonGridSpec) -> None:
    if spec.n < 0:
        raise ValueError("n must be nonnegative")
    if spec.target_energy <= TWO_PI:
        raise ValueError("target_energy must exceed 2*pi")
    if spec.nominal_spacing <= 0.0:
        raise ValueError("nominal_spacing must be positive")
    if spec.eigenvalue_count < 2:
        raise ValueError("eigenvalue_count must be at least two")
    if spec.wall_factor <= 1.0:
        raise ValueError("wall_factor must exceed one")
    if spec.box_scale < 1.0:
        raise ValueError("box_scale must be at least one")
    if spec.boundary_padding < 0.0:
        raise ValueError("boundary_padding must be nonnegative")
    if spec.cap_multiplier < 1.0:
        raise ValueError("cap_multiplier must be at least one")
    if spec.gauge not in {"symmetric", "landau"}:
        raise ValueError("gauge must be 'symmetric' or 'landau'")
    if spec.boundary_samples < 64:
        raise ValueError("boundary_samples must be at least 64")


def common_grid_geometry(
    spec: CommonGridSpec,
) -> tuple[np.ndarray, np.ndarray, float, float, dict[str, Any]]:
    """Construct one nested rectangle containing both allowed regions."""

    _validate_spec(spec)
    wall_energy = spec.wall_factor * spec.target_energy
    radius = sqrt(log(wall_energy / TWO_PI) / pi)
    bounds0 = preimage_disk_bounds(
        0.0,
        spec.n,
        radius,
        centered=spec.centered,
        samples=spec.boundary_samples,
    )
    bounds1 = preimage_disk_bounds(
        spec.a,
        spec.n,
        radius,
        centered=spec.centered,
        samples=spec.boundary_samples,
    )
    union = (
        min(bounds0[0], bounds1[0]),
        max(bounds0[1], bounds1[1]),
        min(bounds0[2], bounds1[2]),
        max(bounds0[3], bounds1[3]),
    )
    cx = 0.5 * (union[0] + union[1])
    cy = 0.5 * (union[2] + union[3])
    half_x = 0.5 * (union[1] - union[0]) * spec.box_scale
    half_y = 0.5 * (union[3] - union[2]) * spec.box_scale
    # Padding is a physical box parameter, independent of mesh spacing, so
    # coarse/fine comparisons use the same rectangle.
    padding = spec.boundary_padding
    rectangle = (
        cx - half_x - padding,
        cx + half_x + padding,
        cy - half_y - padding,
        cy + half_y + padding,
    )
    intervals_x = max(
        4, int(np.ceil((rectangle[1] - rectangle[0]) / spec.nominal_spacing))
    )
    intervals_y = max(
        4, int(np.ceil((rectangle[3] - rectangle[2]) / spec.nominal_spacing))
    )
    hx = (rectangle[1] - rectangle[0]) / intervals_x
    hy = (rectangle[3] - rectangle[2]) / intervals_y
    x = np.linspace(rectangle[0], rectangle[1], intervals_x + 1)[1:-1]
    y = np.linspace(rectangle[2], rectangle[3], intervals_y + 1)[1:-1]
    metadata: dict[str, Any] = {
        "reference_allowed_bounds": [float(v) for v in bounds0],
        "warped_allowed_bounds": [float(v) for v in bounds1],
        "union_allowed_bounds": [float(v) for v in union],
        "common_rectangle": [float(v) for v in rectangle],
        "rectangle_center": [float(cx), float(cy)],
        "padding": float(padding),
        "preimage_wall_radius": float(radius),
        "wall_energy": float(wall_energy),
        "nx": int(len(x)),
        "ny": int(len(y)),
        "matrix_size": int(len(x) * len(y)),
        "hx": float(hx),
        "hy": float(hy),
        "boundary_condition": "Dirichlet",
        "boundary_samples": int(spec.boundary_samples),
    }
    return x, y, hx, hy, metadata


def assemble_kinetic(
    x: np.ndarray,
    y: np.ndarray,
    hx: float,
    hy: float,
    *,
    magnetic_field: float = 0.0,
    gauge: str = "symmetric",
) -> sparse.csr_matrix:
    """Assemble the common Peierls kinetic matrix with Dirichlet walls."""

    if gauge not in {"symmetric", "landau"}:
        raise ValueError("gauge must be 'symmetric' or 'landau'")
    nx, ny = len(x), len(y)
    size = nx * ny
    real_valued = magnetic_field == 0.0
    matrix_dtype = float if real_valued else complex
    diagonal = np.full(
        size, 1.0 / hx**2 + 1.0 / hy**2, dtype=matrix_dtype
    )
    rows: list[np.ndarray] = [np.arange(size)]
    columns: list[np.ndarray] = [np.arange(size)]
    data: list[np.ndarray] = [diagonal]

    j_indices, i_indices = np.meshgrid(
        np.arange(ny), np.arange(nx - 1), indexing="ij"
    )
    lower = (j_indices * nx + i_indices).ravel()
    upper = lower + 1
    if gauge == "symmetric":
        phase_x = np.exp(0.5j * magnetic_field * y[j_indices].ravel() * hx)
    else:
        phase_x = np.ones_like(lower, dtype=complex)
    if real_valued:
        phase_x = np.ones_like(lower, dtype=float)
    coupling_x = -0.5 / hx**2 * phase_x
    rows.extend((lower, upper))
    columns.extend((upper, lower))
    data.extend((coupling_x, np.conjugate(coupling_x)))

    j_indices, i_indices = np.meshgrid(
        np.arange(ny - 1), np.arange(nx), indexing="ij"
    )
    lower = (j_indices * nx + i_indices).ravel()
    upper = lower + nx
    if gauge == "symmetric":
        phase_y = np.exp(-0.5j * magnetic_field * x[i_indices].ravel() * hy)
    else:
        phase_y = np.exp(-1.0j * magnetic_field * x[i_indices].ravel() * hy)
    if real_valued:
        phase_y = np.ones_like(lower, dtype=float)
    coupling_y = -0.5 / hy**2 * phase_y
    rows.extend((lower, upper))
    columns.extend((upper, lower))
    data.extend((coupling_y, np.conjugate(coupling_y)))

    matrix = sparse.coo_matrix(
        (np.concatenate(data), (np.concatenate(rows), np.concatenate(columns))),
        shape=(size, size),
        dtype=matrix_dtype,
    ).tocsr()
    matrix.sum_duplicates()
    return matrix


def _capped_potential(
    xx: np.ndarray,
    yy: np.ndarray,
    *,
    a: float,
    n: int,
    cap: float,
) -> tuple[np.ndarray, float, float]:
    u0, u1 = _centered_iterate_arrays(xx, yy, a, n)
    phi = pi * (u0 * u0 + u1 * u1)
    log_cap = log(cap / TWO_PI)
    clipped = phi > log_cap
    potential = TWO_PI * np.exp(np.minimum(phi, log_cap))
    return potential.ravel(order="C"), float(np.mean(clipped)), float(np.max(phi))


def build_common_grid_pair(spec: CommonGridSpec) -> CommonGridPair:
    """Build the radial and warped matrices on exactly the same grid."""

    x, y, hx, hy, geometry = common_grid_geometry(spec)
    size = len(x) * len(y)
    if spec.eigenvalue_count >= size - 1:
        raise ValueError("too many requested eigenvalues for the common grid")
    kinetic = assemble_kinetic(
        x,
        y,
        hx,
        hy,
        magnetic_field=spec.magnetic_field,
        gauge=spec.gauge,
    )
    xx, yy = np.meshgrid(x, y, indexing="xy")
    potential_cap = geometry["wall_energy"] * spec.cap_multiplier
    potential0, clipped0, max_phi0 = _capped_potential(
        xx, yy, a=0.0, n=spec.n, cap=potential_cap
    )
    potential1, clipped1, max_phi1 = _capped_potential(
        xx, yy, a=spec.a, n=spec.n, cap=potential_cap
    )
    h0 = kinetic + sparse.diags(potential0, format="csr")
    h1 = kinetic + sparse.diags(potential1, format="csr")
    metadata: dict[str, Any] = {
        **geometry,
        "spec": asdict(spec),
        "common_grid": True,
        "same_kinetic_matrix": True,
        "potential_cap": float(potential_cap),
        "potential0_min": float(np.min(potential0)),
        "potential0_max": float(np.max(potential0)),
        "potential1_min": float(np.min(potential1)),
        "potential1_max": float(np.max(potential1)),
        "potential0_clipped_fraction": clipped0,
        "potential1_clipped_fraction": clipped1,
        "potential0_max_uncapped_exponent": max_phi0,
        "potential1_max_uncapped_exponent": max_phi1,
        "matrix_dtype": str(h0.dtype),
        "matrix_nnz": int(h0.nnz),
    }
    return CommonGridPair(
        spec=spec,
        h0=h0.tocsr(),
        h1=h1.tocsr(),
        kinetic=kinetic,
        potential0=potential0,
        potential1=potential1,
        x=x,
        y=y,
        metadata=metadata,
    )


def deterministic_start(size: int) -> np.ndarray:
    """Return the deterministic Lanczos start vector used throughout R200."""

    index = np.arange(size, dtype=float)
    vector = np.sin((index + 1.0) * np.sqrt(2.0)) + 0.5 * np.cos(
        (index + 1.0) * np.sqrt(3.0)
    )
    return vector / np.linalg.norm(vector)


def low_eigensystem(
    matrix: sparse.spmatrix,
    count: int,
    *,
    tolerance: float = 2.0e-10,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, Any]]:
    """Compute a deterministic low eigensystem and explicit residuals."""

    if count >= matrix.shape[0] - 1:
        raise ValueError("count must be smaller than matrix dimension minus one")
    values, vectors = eigsh(
        matrix,
        k=count,
        sigma=0.0,
        which="LM",
        return_eigenvectors=True,
        tol=tolerance,
        maxiter=max(5000, 20 * count),
        v0=deterministic_start(matrix.shape[0]),
    )
    order = np.argsort(values.real)
    values = np.asarray(values.real[order], dtype=float)
    vectors = np.asarray(vectors[:, order])
    residual_matrix = matrix @ vectors - vectors * values[np.newaxis, :]
    residuals = np.linalg.norm(residual_matrix, axis=0) / np.maximum(
        1.0, np.abs(values)
    )
    gram = vectors.conjugate().T @ vectors
    metadata = {
        "count": int(count),
        "lowest_eigenvalue": float(values[0]),
        "highest_eigenvalue": float(values[-1]),
        "monotone": bool(np.all(np.diff(values) >= 0.0)),
        "max_relative_eigen_residual": float(np.max(residuals)),
        "median_relative_eigen_residual": float(np.median(residuals)),
        "max_orthogonality_defect": float(
            np.max(np.abs(gram - np.eye(count)))
        ),
        "deterministic_v0": True,
        "solver": "scipy.sparse.linalg.eigsh shift-invert sigma=0",
        "solver_tolerance": float(tolerance),
    }
    return values, vectors, residuals, metadata


def _solve_resolvent_powers(
    matrix: sparse.spmatrix,
    basis: np.ndarray,
    *,
    shift: float,
    powers: Iterable[int],
) -> tuple[dict[int, np.ndarray], dict[int, float]]:
    requested = sorted(set(int(power) for power in powers))
    if not requested or requested[0] < 1:
        raise ValueError("resolvent powers must be positive integers")
    shifted = (
        matrix + shift * sparse.identity(matrix.shape[0], dtype=matrix.dtype)
    ).tocsc()
    factor = splu(shifted)
    previous = np.asarray(basis, dtype=matrix.dtype)
    solutions: dict[int, np.ndarray] = {}
    residuals: dict[int, float] = {}
    for power in range(1, requested[-1] + 1):
        solution = factor.solve(previous)
        residual = shifted @ solution - previous
        denominator = max(np.linalg.norm(previous), np.finfo(float).tiny)
        residuals[power] = float(np.linalg.norm(residual) / denominator)
        if power in requested:
            solutions[power] = solution
        previous = solution
    return solutions, residuals


def compressed_resolvent_differences(
    h0: sparse.spmatrix,
    h1: sparse.spmatrix,
    eigenvalues0: np.ndarray,
    eigenvectors0: np.ndarray,
    cutoffs: Iterable[int],
    *,
    shift: float = TWO_PI,
    powers: Iterable[int] = (1, 2, 3),
    repeat: bool = True,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Compress finite-box resolvent differences into the H0 eigenbasis."""

    cutoffs_tuple = tuple(sorted(set(int(value) for value in cutoffs)))
    powers_tuple = tuple(sorted(set(int(value) for value in powers)))
    if not cutoffs_tuple or cutoffs_tuple[0] < 1:
        raise ValueError("cutoffs must contain positive integers")
    max_cutoff = cutoffs_tuple[-1]
    if not powers_tuple or powers_tuple[0] < 1:
        raise ValueError("powers must contain positive integers")
    solve_powers = tuple(range(1, powers_tuple[-1] + 1))
    if max_cutoff > len(eigenvalues0) or max_cutoff > eigenvectors0.shape[1]:
        raise ValueError("largest cutoff exceeds the available H0 eigensystem")
    basis = np.asarray(eigenvectors0[:, :max_cutoff], dtype=h0.dtype)

    h1_solutions, h1_residuals = _solve_resolvent_powers(
        h1, basis, shift=shift, powers=solve_powers
    )
    h0_solutions, h0_residuals = _solve_resolvent_powers(
        h0, basis, shift=shift, powers=solve_powers
    )
    delta_basis = (h1 - h0) @ basis
    identity_solutions, identity_residuals = _solve_resolvent_powers(
        h1, delta_basis, shift=shift, powers=solve_powers
    )

    arrays: dict[str, np.ndarray] = {}
    summary: dict[str, Any] = {
        "shift": float(shift),
        "cutoffs": list(cutoffs_tuple),
        "powers": list(powers_tuple),
        "h1_linear_solve_relative_residuals": {
            str(key): float(value) for key, value in h1_residuals.items()
        },
        "h0_null_linear_solve_relative_residuals": {
            str(key): float(value) for key, value in h0_residuals.items()
        },
        "identity_linear_solve_relative_residuals": {
            str(key): float(value) for key, value in identity_residuals.items()
        },
        "nuclear_norms": {},
        "null_nuclear_norms": {},
        "repeat_relative_differences": {},
        "repeat_absolute_differences": {},
        "compressed_hermiticity_defects": {},
        "direct_identity_relative_discrepancies": {},
        "direct_identity_absolute_discrepancies": {},
        "cutoff_gaps": {},
        "finite_box_only": True,
        "analytic_input_not_tested": (
            "Full-space Schatten membership is not inferable from finite matrices"
        ),
    }

    compressed_h1: dict[int, np.ndarray] = {}
    identity_q = {
        power: basis.conjugate().T @ identity_solutions[power]
        for power in solve_powers
    }
    for power in powers_tuple:
        compressed_h1[power] = basis.conjugate().T @ h1_solutions[power]
        compressed_h0_solve = basis.conjugate().T @ h0_solutions[power]
        exact_h0 = np.diag((eigenvalues0[:max_cutoff] + shift) ** (-power))
        d = (eigenvalues0[:max_cutoff] + shift) ** (-1)
        identity_difference = np.zeros_like(compressed_h1[power])
        for j in range(power):
            # D_m = -sum_j R1^(m-j) (H1-H0) R0^(j+1).
            identity_difference -= identity_q[power - j] * d[np.newaxis, :] ** (
                j + 1
            )
        direct_difference = compressed_h1[power] - exact_h0
        arrays[f"compressed_h1_power{power}_M{max_cutoff}"] = compressed_h1[power]
        arrays[f"compressed_h0_null_power{power}_M{max_cutoff}"] = compressed_h0_solve
        arrays[f"compressed_identity_difference_power{power}_M{max_cutoff}"] = (
            identity_difference
        )
        arrays[f"compressed_direct_difference_power{power}_M{max_cutoff}"] = (
            direct_difference
        )
        for cutoff in cutoffs_tuple:
            difference = identity_difference[:cutoff, :cutoff]
            direct = direct_difference[:cutoff, :cutoff]
            null_difference = (
                compressed_h0_solve[:cutoff, :cutoff]
                - exact_h0[:cutoff, :cutoff]
            )
            singular_values = np.linalg.svd(difference, compute_uv=False)
            direct_singular_values = np.linalg.svd(direct, compute_uv=False)
            null_singular_values = np.linalg.svd(
                null_difference, compute_uv=False
            )
            key = f"power{power}_M{cutoff}"
            arrays[f"singular_values_{key}"] = singular_values
            arrays[f"direct_singular_values_{key}"] = direct_singular_values
            arrays[f"null_singular_values_{key}"] = null_singular_values
            summary["nuclear_norms"][key] = float(np.sum(singular_values))
            summary["null_nuclear_norms"][key] = float(
                np.sum(null_singular_values)
            )
            summary["compressed_hermiticity_defects"][key] = float(
                np.linalg.norm(difference - difference.conjugate().T)
                / max(np.linalg.norm(difference), np.finfo(float).tiny)
            )
            discrepancy = direct - difference
            summary["direct_identity_relative_discrepancies"][key] = float(
                np.linalg.norm(discrepancy)
                / max(np.linalg.norm(difference), np.finfo(float).tiny)
            )
            summary["direct_identity_absolute_discrepancies"][key] = float(
                np.max(np.abs(discrepancy))
            )
            if cutoff < len(eigenvalues0):
                gap = float(eigenvalues0[cutoff] - eigenvalues0[cutoff - 1])
                summary["cutoff_gaps"][f"M{cutoff}"] = {
                    "lambda_below": float(eigenvalues0[cutoff - 1]),
                    "lambda_above": float(eigenvalues0[cutoff]),
                    "absolute_gap": gap,
                    "relative_gap": float(
                        gap / max(abs(eigenvalues0[cutoff - 1]), 1.0)
                    ),
                }

    if repeat:
        repeated, repeated_residuals = _solve_resolvent_powers(
            h1, delta_basis, shift=shift, powers=solve_powers
        )
        summary["repeat_linear_solve_relative_residuals"] = {
            str(key): float(value) for key, value in repeated_residuals.items()
        }
        for power in powers_tuple:
            repeat_q = {
                q: basis.conjugate().T @ repeated[q]
                for q in solve_powers
                if q <= power
            }
            d = (eigenvalues0[:max_cutoff] + shift) ** (-1)
            repeat_compressed = np.zeros_like(compressed_h1[power])
            for j in range(power):
                repeat_compressed -= repeat_q[power - j] * d[np.newaxis, :] ** (
                    j + 1
                )
            for cutoff in cutoffs_tuple:
                repeat_difference = repeat_compressed[:cutoff, :cutoff]
                repeat_singular_values = np.linalg.svd(
                    repeat_difference, compute_uv=False
                )
                key = f"power{power}_M{cutoff}"
                original = arrays[f"singular_values_{key}"]
                denominator = max(np.linalg.norm(original), np.finfo(float).tiny)
                summary["repeat_relative_differences"][key] = float(
                    np.linalg.norm(repeat_singular_values - original) / denominator
                )
                summary["repeat_absolute_differences"][key] = float(
                    np.max(np.abs(repeat_singular_values - original))
                )
                arrays[f"repeat_singular_values_{key}"] = repeat_singular_values

    return arrays, summary


def truncated_resolvent_trace_diagnostics(
    eigenvalues0: np.ndarray,
    eigenvalues1: np.ndarray,
    *,
    shift: float = TWO_PI,
    powers: Iterable[int] = (1, 2, 3),
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Cross-check finite spectral resolvent traces against the staircase.

    This identity concerns two equally truncated eigenvalue lists.  It is not
    the trace of the full finite-difference matrix and is not a tail bound.
    """

    values0 = np.sort(np.asarray(eigenvalues0, dtype=float))
    values1 = np.sort(np.asarray(eigenvalues1, dtype=float))
    if len(values0) != len(values1):
        raise ValueError("the two truncated spectra must have equal lengths")
    events, xi = relative_counting_staircase(values0, values1)
    upper = np.concatenate((events[1:], np.array([np.inf])))
    arrays: dict[str, np.ndarray] = {
        "resolvent_trace_events": events,
        "resolvent_trace_xi": xi,
    }
    summary: dict[str, Any] = {
        "finite_equal_truncation_only": True,
        "direct_traces": {},
        "staircase_traces": {},
        "absolute_identity_errors": {},
    }
    for power in sorted(set(int(value) for value in powers)):
        if power < 1:
            raise ValueError("powers must be positive")
        direct = float(
            np.sum((values1 + shift) ** (-power))
            - np.sum((values0 + shift) ** (-power))
        )
        # Integral of -m*xi(E)/(E+c)^(m+1) over every constant interval.
        left = (events + shift) ** (-power)
        right = np.where(np.isinf(upper), 0.0, (upper + shift) ** (-power))
        staircase = float(-np.sum(xi * (left - right)))
        key = str(power)
        summary["direct_traces"][key] = direct
        summary["staircase_traces"][key] = staircase
        summary["absolute_identity_errors"][key] = abs(direct - staircase)
        arrays[f"truncated_resolvent_trace_power{power}"] = np.array(
            [direct, staircase], dtype=float
        )
    return arrays, summary


def relative_counting_staircase(
    eigenvalues0: np.ndarray, eigenvalues1: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return right-continuous event energies and xi=N0-N1."""

    values0 = np.sort(np.asarray(eigenvalues0, dtype=float))
    values1 = np.sort(np.asarray(eigenvalues1, dtype=float))
    events = np.unique(np.concatenate((values0, values1)))
    xi = np.searchsorted(values0, events, side="right") - np.searchsorted(
        values1, events, side="right"
    )
    return events, np.asarray(xi, dtype=int)


def integrate_counting_staircase(
    events: np.ndarray, xi: np.ndarray, times: np.ndarray
) -> np.ndarray:
    """Evaluate -t integral exp(-tE) xi(E)dE exactly between events."""

    energies = np.asarray(events, dtype=float)
    values = np.asarray(xi, dtype=float)
    t_values = np.asarray(times, dtype=float)
    if len(energies) != len(values):
        raise ValueError("events and xi must have equal lengths")
    if np.any(t_values <= 0.0):
        raise ValueError("heat times must be positive")
    if len(energies) == 0:
        return np.zeros_like(t_values)
    # The finite spectra have equal cardinality in R200, hence xi=0 after
    # the final event.  Appending infinity makes that endpoint convention
    # explicit without adding a numerical tail.
    upper = np.concatenate((energies[1:], np.array([np.inf])))
    output = np.empty_like(t_values)
    for index, time in enumerate(t_values):
        left_exp = np.exp(-time * energies)
        right_exp = np.exp(-time * upper)
        integral = np.sum(values * (left_exp - right_exp)) / time
        output[index] = -time * integral
    return output


def heat_trace_diagnostics(
    eigenvalues0: np.ndarray,
    eigenvalues1: np.ndarray,
    times: np.ndarray,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Compute direct and exact finite-staircase relative heat traces."""

    values0 = np.sort(np.asarray(eigenvalues0, dtype=float))
    values1 = np.sort(np.asarray(eigenvalues1, dtype=float))
    if len(values0) != len(values1):
        raise ValueError("finite heat traces require equal spectrum lengths")
    t_values = np.asarray(times, dtype=float)
    events, xi = relative_counting_staircase(values0, values1)
    direct_naive = np.array(
        [
            np.sum(np.exp(-time * values1))
            - np.sum(np.exp(-time * values0))
            for time in t_values
        ],
        dtype=float,
    )
    direct = np.array(
        [
            np.sum(
                np.exp(-time * values0)
                * np.expm1(-time * (values1 - values0))
            )
            for time in t_values
        ],
        dtype=float,
    )
    integral = integrate_counting_staircase(events, xi, t_values)
    half = len(values0) // 2
    half_direct = np.array(
        [
            np.sum(np.exp(-time * values1[:half]))
            - np.sum(np.exp(-time * values0[:half]))
            for time in t_values
        ],
        dtype=float,
    )
    scale = np.maximum.reduce(
        (np.ones_like(direct), np.abs(direct), np.abs(integral))
    )
    arrays = {
        "counting_events": events,
        "counting_xi": xi,
        "heat_times": t_values,
        "heat_direct": direct,
        "heat_direct_naive": direct_naive,
        "heat_from_staircase": integral,
        "heat_half_spectrum": half_direct,
        "heat_half_difference": direct - half_direct,
    }
    summary = {
        "spectrum_count": int(len(values0)),
        "half_spectrum_count": int(half),
        "endpoint_convention": (
            "right-continuous xi=N0-N1; xi=0 above the largest event because "
            "the two finite spectra have equal cardinality"
        ),
        "max_scaled_identity_error": float(
            np.max(np.abs(direct - integral) / scale)
        ),
        "max_absolute_identity_error": float(np.max(np.abs(direct - integral))),
        "max_stable_naive_difference": float(
            np.max(np.abs(direct - direct_naive))
        ),
        "truncation_quantity_label": (
            "full-minus-half finite-spectrum comparison; not a rigorous tail bound"
        ),
    }
    return arrays, summary


def frozen_window_definitions(
    eigenvalues0: np.ndarray,
    eigenvalues1: np.ndarray,
    *,
    center_fractions: Iterable[float] = (0.3, 0.5, 0.7),
    base_sigma_fraction: float = 0.08,
    width_multipliers: Iterable[float] = (0.8, 1.0, 1.2),
) -> list[dict[str, float | int]]:
    """Set windows from spectral coverage without inspecting a time trace."""

    values0 = np.sort(np.asarray(eigenvalues0, dtype=float))
    values1 = np.sort(np.asarray(eigenvalues1, dtype=float))
    lower = max(float(values0[0]), float(values1[0]))
    upper = min(float(values0[-1]), float(values1[-1]))
    if not upper > lower:
        raise ValueError("the two finite spectra have no common coverage")
    span = upper - lower
    definitions: list[dict[str, float | int]] = []
    for window_index, fraction in enumerate(center_fractions):
        if not 0.0 < fraction < 1.0:
            raise ValueError("center fractions must lie strictly between zero and one")
        center = lower + fraction * span
        for width_index, multiplier in enumerate(width_multipliers):
            if multiplier <= 0.0:
                raise ValueError("width multipliers must be positive")
            definitions.append(
                {
                    "window_index": int(window_index),
                    "width_index": int(width_index),
                    "center_fraction": float(fraction),
                    "width_multiplier": float(multiplier),
                    "center": float(center),
                    "sigma": float(base_sigma_fraction * multiplier * span),
                    "coverage_lower": float(lower),
                    "coverage_upper": float(upper),
                    "coverage_span": float(span),
                }
            )
    return definitions


def _complex_spectral_trace(
    eigenvalues: np.ndarray,
    weights: np.ndarray,
    times: np.ndarray,
    phases: np.ndarray | None = None,
) -> np.ndarray:
    phase_factor = 1.0 if phases is None else np.exp(1.0j * phases)
    coefficients = np.asarray(weights, dtype=float) * phase_factor
    return np.exp(-1.0j * np.outer(times, eigenvalues)) @ coefficients


def extract_nonzero_peaks(
    times: np.ndarray,
    magnitude: np.ndarray,
    *,
    minimum_time: float = 0.05,
    relative_prominence: float = 0.05,
    maximum_peaks: int = 10,
) -> list[dict[str, float]]:
    """Apply the preregistered descriptive nonzero-time peak rule."""

    t_values = np.asarray(times, dtype=float)
    amplitudes = np.asarray(magnitude, dtype=float)
    mask = t_values >= minimum_time
    if not np.any(mask):
        return []
    selected = amplitudes[mask]
    prominence = relative_prominence * max(float(np.max(selected)), np.finfo(float).tiny)
    peak_indices, properties = find_peaks(selected, prominence=prominence)
    global_indices = np.flatnonzero(mask)[peak_indices]
    records = [
        {
            "time": float(t_values[index]),
            "amplitude": float(amplitudes[index]),
            "prominence": float(properties["prominences"][local]),
        }
        for local, index in enumerate(global_indices)
    ]
    records.sort(key=lambda item: (-item["prominence"], item["time"]))
    return records[:maximum_peaks]


def wave_trace_diagnostics(
    eigenvalues0: np.ndarray,
    eigenvalues1: np.ndarray,
    times: np.ndarray,
    window: dict[str, float | int],
    *,
    surrogate_seed: int,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Compute a zero-input smoothed relative spectral-propagator trace."""

    values0 = np.asarray(eigenvalues0, dtype=float)
    values1 = np.asarray(eigenvalues1, dtype=float)
    t_values = np.asarray(times, dtype=float)
    center = float(window["center"])
    sigma = float(window["sigma"])
    weights0 = np.exp(-0.5 * ((values0 - center) / sigma) ** 2)
    weights1 = np.exp(-0.5 * ((values1 - center) / sigma) ** 2)
    trace0 = _complex_spectral_trace(values0, weights0, t_values)
    trace1 = _complex_spectral_trace(values1, weights1, t_values)
    relative = trace1 - trace0
    null = trace0 - trace0.copy()

    rng = np.random.default_rng(surrogate_seed)
    # Rademacher phases (0 or pi) retain real spectral coefficients and thus
    # preserve W(-t)=conj(W(t)), unlike arbitrary complex phase multipliers.
    phases0 = pi * rng.integers(0, 2, len(values0))
    phases1 = pi * rng.integers(0, 2, len(values1))
    surrogate = _complex_spectral_trace(
        values1, weights1, t_values, phases1
    ) - _complex_spectral_trace(values0, weights0, t_values, phases0)

    if center <= TWO_PI:
        raise ValueError("window center must exceed 2*pi for natural-time scaling")
    natural_time_scale = sqrt(log(center / TWO_PI) / center)
    events, xi = relative_counting_staircase(values0, values1)
    upper = np.concatenate((events[1:], np.array([np.inf])))
    f_left = np.exp(-0.5 * ((events - center) / sigma) ** 2)[None, :] * np.exp(
        -1.0j * np.outer(t_values, events)
    )
    finite_upper = np.isfinite(upper)
    f_right = np.zeros_like(f_left)
    f_right[:, finite_upper] = np.exp(
        -0.5 * ((upper[finite_upper] - center) / sigma) ** 2
    )[None, :] * np.exp(-1.0j * np.outer(t_values, upper[finite_upper]))
    wave_from_staircase = np.sum(
        xi[None, :] * (f_right - f_left), axis=1
    )
    dt = float(np.max(np.diff(t_values))) if len(t_values) > 1 else 0.0
    nyquist_ratio = dt * max(float(values0[-1]), float(values1[-1])) / pi
    amplitude_bound = float(np.sum(weights0) + np.sum(weights1))
    identity_scale = np.maximum(1.0, np.abs(relative))
    phase_threshold = 100.0 * np.finfo(float).eps * max(amplitude_bound, 1.0)
    phase_valid = np.abs(relative) > phase_threshold
    reported_phase = np.full(len(relative), np.nan, dtype=float)
    reported_phase[phase_valid] = np.angle(relative[phase_valid])
    arrays = {
        "wave_times": t_values,
        "wave_natural_times": t_values / natural_time_scale,
        "wave_relative_real": relative.real,
        "wave_relative_imag": relative.imag,
        "wave_relative_magnitude": np.abs(relative),
        "wave_relative_phase": reported_phase,
        "wave_phase_valid": phase_valid,
        "wave_relative_demodulated_real": (
            np.exp(1.0j * t_values * center) * relative
        ).real,
        "wave_relative_demodulated_imag": (
            np.exp(1.0j * t_values * center) * relative
        ).imag,
        "wave_from_staircase_real": wave_from_staircase.real,
        "wave_from_staircase_imag": wave_from_staircase.imag,
        "wave_h0_h0_null_real": null.real,
        "wave_h0_h0_null_imag": null.imag,
        "wave_surrogate_real": surrogate.real,
        "wave_surrogate_imag": surrogate.imag,
        "window_weights0": weights0,
        "window_weights1": weights1,
    }
    summary = {
        "window": dict(window),
        "surrogate_seed": int(surrogate_seed),
        "surrogate_definition": (
            "independent deterministic Rademacher (0 or pi) phase multipliers "
            "on the two windowed finite spectra; conjugacy is preserved"
        ),
        "natural_time_scale": float(natural_time_scale),
        "natural_time_label": (
            "energy-dependent diagnostic; not the time of one fixed generator"
        ),
        "t0_amplitude": float(np.abs(relative[0])),
        "max_h0_h0_null": float(np.max(np.abs(null))),
        "max_scaled_staircase_identity_error": float(
            np.max(np.abs(relative - wave_from_staircase) / identity_scale)
        ),
        "amplitude_bound": amplitude_bound,
        "phase_validity_threshold": float(phase_threshold),
        "max_amplitude_bound_ratio": float(
            np.max(np.abs(relative)) / max(amplitude_bound, np.finfo(float).tiny)
        ),
        "nyquist_ratio_dt_lambda_max_over_pi": float(nyquist_ratio),
        "upper_edge_weight_max": float(max(weights0[-1], weights1[-1])),
        "lower_edge_weight_max": float(max(weights0[0], weights1[0])),
        "window_tail_label": (
            "edge weights and larger-cutoff comparison are empirical sensitivity "
            "diagnostics, not certified full-space tail bounds"
        ),
        "nonzero_peaks": extract_nonzero_peaks(t_values, np.abs(relative)),
        "surrogate_nonzero_peaks": extract_nonzero_peaks(
            t_values, np.abs(surrogate)
        ),
    }
    return arrays, summary
