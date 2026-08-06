"""Form-domain-valid Galerkin solver after the exact Hénon coordinate change.

Original-coordinate Hermite functions are not admissible for the warped
potential: along one direction the potential grows like exp(c*x**4), faster
than their Gaussian tails.  R401 therefore first applies the exact unitary,
area-preserving change of variables u=Psi_a(q).  In u coordinates the
potential is radial Gaussian-exponential and the kinetic energy is a
polynomial divergence-form operator.  A second determinant-one linear
normalization makes the constant kinetic metric Euclidean.  Product Hermite
functions then lie in the quadratic-form domain for the frozen small hbar
regime, so the matrices below are genuine Ritz matrices rather than a
finite-quadrature surrogate for divergent integrals.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import pi, sqrt
from typing import Any

import numpy as np
from scipy.linalg import eigh
from scipy.special import roots_hermite

from .warped_henon import TWO_PI, centered_fixed_point


@dataclass(frozen=True)
class TransformedGalerkinSpec:
    """Frozen controls for one exact-coordinate transformed Ritz solve."""

    hbar: float
    a: float
    basis_excess_cutoff: float
    eigenvalue_excess_ceiling: float
    quadrature_order: int = 72
    n: int = 1


def transformed_metric_data(
    a: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Return singular values, u=Lz, L inverse, and c=2*a*r_a."""

    if a <= -1.0:
        raise ValueError("the centered real branch requires a > -1")
    c = 2.0 * a * centered_fixed_point(a)
    metric_at_zero = np.array(
        [[c * c + 1.0, -c], [-c, 1.0]], dtype=float
    )
    squared_singular_values, rotation = np.linalg.eigh(metric_at_zero)
    if np.linalg.det(rotation) < 0.0:
        rotation[:, 0] *= -1.0
    singular_values = np.sqrt(squared_singular_values)
    linear_map = rotation @ np.diag(singular_values)
    if not np.isclose(np.linalg.det(linear_map), 1.0, atol=2.0e-14):
        raise RuntimeError("the normalized coordinate map must preserve area")
    inverse = np.linalg.inv(linear_map)
    normalized = inverse @ metric_at_zero @ inverse.T
    if not np.allclose(normalized, np.eye(2), atol=3.0e-14):
        raise RuntimeError("the transformed kinetic metric is not normalized")
    return singular_values, linear_map, inverse, float(c)


def _hermite_polynomials(nodes: np.ndarray, count: int) -> np.ndarray:
    values = np.empty((len(nodes), count), dtype=float)
    values[:, 0] = pi ** (-0.25)
    if count > 1:
        values[:, 1] = sqrt(2.0) * nodes * values[:, 0]
    for degree in range(1, count - 1):
        values[:, degree + 1] = (
            sqrt(2.0 / (degree + 1.0)) * nodes * values[:, degree]
            - sqrt(degree / (degree + 1.0)) * values[:, degree - 1]
        )
    return values


def _basis_pairs(
    hbar: float,
    frequencies: np.ndarray,
    excess_cutoff: float,
) -> tuple[np.ndarray, np.ndarray]:
    pairs: list[tuple[int, int]] = []
    energies: list[float] = []
    maximum_first = int(
        np.floor(
            (
                excess_cutoff - 0.5 * hbar * frequencies[1]
            )
            / (hbar * frequencies[0])
            - 0.5
        )
    )
    for first in range(maximum_first + 1):
        residual = excess_cutoff - hbar * frequencies[0] * (first + 0.5)
        maximum_second = int(
            np.floor(residual / (hbar * frequencies[1]) - 0.5)
        )
        for second in range(maximum_second + 1):
            energy = hbar * (
                frequencies[0] * (first + 0.5)
                + frequencies[1] * (second + 0.5)
            )
            if energy <= excess_cutoff * (1.0 + 4.0e-15):
                pairs.append((first, second))
                energies.append(float(energy))
    if not pairs:
        raise ValueError("basis cutoff lies below the oscillator ground state")
    order = np.argsort(np.asarray(energies), kind="stable")
    return np.asarray(pairs, dtype=int)[order], np.asarray(energies)[order]


def _coefficient_and_potential_residuals(
    nodes: np.ndarray,
    *,
    hbar: float,
    a: float,
    singular_values: np.ndarray,
    linear_map: np.ndarray,
    inverse_map: np.ndarray,
    centered_slope: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return B(z)-I and V(Lz)-V_quad on the tensor quadrature grid."""

    frequencies = TWO_PI * singular_values
    z_first = sqrt(hbar / frequencies[0]) * nodes[:, np.newaxis]
    z_second = sqrt(hbar / frequencies[1]) * nodes[np.newaxis, :]
    u_first = linear_map[0, 0] * z_first + linear_map[0, 1] * z_second
    u_second = linear_map[1, 0] * z_first + linear_map[1, 1] * z_second

    radius_squared = u_first * u_first + u_second * u_second
    potential_excess = TWO_PI * np.expm1(pi * radius_squared)
    quadratic = 0.5 * (
        frequencies[0] ** 2 * z_first * z_first
        + frequencies[1] ** 2 * z_second * z_second
    )
    potential_residual = potential_excess - quadratic

    d = centered_slope + 2.0 * a * u_second
    metric = np.empty((*d.shape, 2, 2), dtype=float)
    metric[..., 0, 0] = d * d + 1.0
    metric[..., 0, 1] = -d
    metric[..., 1, 0] = -d
    metric[..., 1, 1] = 1.0
    transformed_metric = np.einsum(
        "ia,...ab,jb->...ij",
        inverse_map,
        metric,
        inverse_map,
        optimize=True,
    )
    transformed_metric[..., 0, 0] -= 1.0
    transformed_metric[..., 1, 1] -= 1.0
    return transformed_metric, potential_residual


def solve_transformed_galerkin(
    spec: TransformedGalerkinSpec,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Return genuine Ritz values below a fixed excess-energy ceiling."""

    if spec.hbar <= 0.0:
        raise ValueError("hbar must be positive")
    if spec.n != 1:
        raise ValueError("the exact R401 coordinate formula freezes n=1")
    if not 0.0 < spec.eigenvalue_excess_ceiling < spec.basis_excess_cutoff:
        raise ValueError("the retained ceiling must lie inside the basis cutoff")
    if spec.quadrature_order < 16:
        raise ValueError("quadrature_order is too small")

    singular_values, linear_map, inverse_map, centered_slope = (
        transformed_metric_data(spec.a)
    )
    if spec.hbar >= 2.0 / float(np.max(singular_values)):
        raise ValueError("Hermite functions would leave the potential form domain")
    frequencies = TWO_PI * singular_values
    pairs, harmonic_excess = _basis_pairs(
        spec.hbar, frequencies, spec.basis_excess_cutoff
    )
    maximum_degrees = np.max(pairs, axis=0)
    required_quadrature_order = int(np.max(maximum_degrees)) + 3
    if spec.quadrature_order < required_quadrature_order:
        raise ValueError(
            "quadrature_order must be at least max_degree+3 "
            f"({required_quadrature_order} for this basis)"
        )

    nodes, weights = roots_hermite(spec.quadrature_order)
    polynomial_first = _hermite_polynomials(
        nodes, int(maximum_degrees[0]) + 2
    )
    polynomial_second = _hermite_polynomials(
        nodes, int(maximum_degrees[1]) + 2
    )
    derivative_first = np.empty_like(polynomial_first[:, :-1])
    derivative_second = np.empty_like(polynomial_second[:, :-1])
    for degree in range(derivative_first.shape[1]):
        derivative_first[:, degree] = -nodes * polynomial_first[:, degree]
        if degree:
            derivative_first[:, degree] += (
                sqrt(2.0 * degree) * polynomial_first[:, degree - 1]
            )
    for degree in range(derivative_second.shape[1]):
        derivative_second[:, degree] = -nodes * polynomial_second[:, degree]
        if degree:
            derivative_second[:, degree] += (
                sqrt(2.0 * degree) * polynomial_second[:, degree - 1]
            )

    root_weights = np.sqrt(weights)[:, np.newaxis]
    basis_first = root_weights * polynomial_first[:, :-1]
    basis_second = root_weights * polynomial_second[:, :-1]
    gradient_first = root_weights * derivative_first
    gradient_second = root_weights * derivative_second

    selected_first = basis_first[:, pairs[:, 0]]
    selected_second = basis_second[:, pairs[:, 1]]
    selected_gradient_first = gradient_first[:, pairs[:, 0]]
    selected_gradient_second = gradient_second[:, pairs[:, 1]]
    values = (
        selected_first[:, np.newaxis, :]
        * selected_second[np.newaxis, :, :]
    ).reshape(spec.quadrature_order**2, len(pairs))
    derivative_z_first = sqrt(frequencies[0] / spec.hbar) * (
        selected_gradient_first[:, np.newaxis, :]
        * selected_second[np.newaxis, :, :]
    ).reshape(spec.quadrature_order**2, len(pairs))
    derivative_z_second = sqrt(frequencies[1] / spec.hbar) * (
        selected_first[:, np.newaxis, :]
        * selected_gradient_second[np.newaxis, :, :]
    ).reshape(spec.quadrature_order**2, len(pairs))

    metric_residual, potential_residual = _coefficient_and_potential_residuals(
        nodes,
        hbar=spec.hbar,
        a=spec.a,
        singular_values=singular_values,
        linear_map=linear_map,
        inverse_map=inverse_map,
        centered_slope=centered_slope,
    )
    c00 = metric_residual[..., 0, 0].ravel(order="C")
    c01 = metric_residual[..., 0, 1].ravel(order="C")
    c10 = metric_residual[..., 1, 0].ravel(order="C")
    c11 = metric_residual[..., 1, 1].ravel(order="C")

    matrix = values.T @ (potential_residual.ravel(order="C")[:, None] * values)
    matrix += 0.5 * spec.hbar**2 * (
        derivative_z_first.T @ (c00[:, None] * derivative_z_first)
        + derivative_z_first.T @ (c01[:, None] * derivative_z_second)
        + derivative_z_second.T @ (c10[:, None] * derivative_z_first)
        + derivative_z_second.T @ (c11[:, None] * derivative_z_second)
    )
    matrix[np.diag_indices_from(matrix)] += TWO_PI + harmonic_excess
    pre_symmetry_defect = float(np.max(np.abs(matrix - matrix.T)))
    matrix = 0.5 * (matrix + matrix.T)

    all_values, eigenvectors = eigh(
        matrix,
        overwrite_a=False,
        check_finite=False,
        driver="evd",
    )
    keep = all_values <= TWO_PI + spec.eigenvalue_excess_ceiling
    retained = np.asarray(all_values[keep], dtype=float)
    retained_vectors = eigenvectors[:, keep]
    if not len(retained):
        raise RuntimeError("no transformed Galerkin eigenvalues were retained")
    ritz_residuals = np.linalg.norm(
        matrix @ retained_vectors
        - retained_vectors * retained[np.newaxis, :],
        axis=0,
    )

    gram_first = basis_first.T @ basis_first
    gram_second = basis_second.T @ basis_second
    metadata: dict[str, Any] = {
        "spec": asdict(spec),
        "singular_values": singular_values.tolist(),
        "frequencies": frequencies.tolist(),
        "linear_map_u_from_z": linear_map.tolist(),
        "inverse_map_z_from_u": inverse_map.tolist(),
        "centered_slope": centered_slope,
        "basis_size": int(len(pairs)),
        "maximum_degrees": [int(value) for value in maximum_degrees],
        "retained_eigenvalues": int(len(retained)),
        "lowest_eigenvalue": float(retained[0]),
        "highest_retained_eigenvalue": float(retained[-1]),
        "quadrature_orthogonality_defect": float(
            max(
                np.max(np.abs(gram_first - np.eye(gram_first.shape[0]))),
                np.max(np.abs(gram_second - np.eye(gram_second.shape[0]))),
            )
        ),
        "max_absolute_ritz_residual": float(np.max(ritz_residuals)),
        "pre_symmetrization_defect": pre_symmetry_defect,
        "matrix_symmetry_defect": float(np.max(np.abs(matrix - matrix.T))),
        "form_domain_margin": float(
            2.0 / np.max(singular_values) - spec.hbar
        ),
        "coordinate_change": "u=Psi_a(q), u=Lz, det(DPsi)=det(L)=1",
    }
    return retained, metadata
