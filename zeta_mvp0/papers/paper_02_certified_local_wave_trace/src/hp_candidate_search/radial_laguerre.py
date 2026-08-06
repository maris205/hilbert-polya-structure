"""Independent angular-momentum solver for the radial R401 reference."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import lgamma, pi
from typing import Any

import numpy as np
from scipy.linalg import eigh
from scipy.special import eval_genlaguerre, roots_genlaguerre

from .warped_henon import TWO_PI


@dataclass(frozen=True)
class RadialLaguerreSpec:
    """Frozen radial-oscillator basis and quadrature controls."""

    hbar: float
    basis_excess_cutoff: float
    eigenvalue_excess_ceiling: float
    quadrature_order: int = 96


def _basis_size(
    hbar: float,
    angular_momentum: int,
    excess_cutoff: float,
) -> int:
    maximum = int(
        np.floor(
            0.5
            * (
                excess_cutoff / (hbar * TWO_PI)
                - angular_momentum
                - 1.0
            )
        )
    )
    return max(0, maximum + 1)


def solve_radial_laguerre(
    spec: RadialLaguerreSpec,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Compute the radial-control spectrum in independent |m| blocks.

    The radial potential grows like exp(pi*r**2).  For the R401 hbar values,
    the oscillator/Laguerre basis lies in the quadratic-form domain; unlike
    original-q Hermites for the warped exp(c*x**4) tail, these matrix
    elements are genuine finite integrals.
    """

    if spec.hbar <= 0.0 or spec.hbar >= 2.0:
        raise ValueError("the Laguerre form-domain implementation requires 0<hbar<2")
    if not 0.0 < spec.eigenvalue_excess_ceiling < spec.basis_excess_cutoff:
        raise ValueError("the retained ceiling must lie inside the basis cutoff")
    if spec.quadrature_order < 16:
        raise ValueError("quadrature_order is too small")

    maximum_momentum = int(
        np.floor(spec.basis_excess_cutoff / (spec.hbar * TWO_PI) - 1.0)
    )
    required_quadrature_order = _basis_size(
        spec.hbar, 0, spec.basis_excess_cutoff
    ) + 2
    if spec.quadrature_order < required_quadrature_order:
        raise ValueError(
            "quadrature_order must be at least max_radial_degree+3 "
            f"({required_quadrature_order} for this basis)"
        )
    spectrum: list[float] = []
    block_records: list[dict[str, Any]] = []
    maximum_orthogonality_defect = 0.0
    maximum_ritz_residual = 0.0

    for momentum in range(maximum_momentum + 1):
        count = _basis_size(spec.hbar, momentum, spec.basis_excess_cutoff)
        if count == 0:
            continue
        nodes, weights = roots_genlaguerre(spec.quadrature_order, momentum)
        polynomial = np.empty((len(nodes), count), dtype=float)
        for radial_index in range(count):
            log_normalization = 0.5 * (
                lgamma(radial_index + 1.0)
                - lgamma(radial_index + momentum + 1.0)
            )
            polynomial[:, radial_index] = (
                np.exp(log_normalization)
                * eval_genlaguerre(radial_index, momentum, nodes)
            )
        evaluation = np.sqrt(weights)[:, np.newaxis] * polynomial
        radius_squared = spec.hbar * nodes / TWO_PI
        potential_excess = TWO_PI * np.expm1(pi * radius_squared)
        quadratic = 0.5 * TWO_PI**2 * radius_squared
        residual = potential_excess - quadratic
        matrix = evaluation.T @ (residual[:, np.newaxis] * evaluation)
        harmonic_excess = spec.hbar * TWO_PI * (
            2.0 * np.arange(count) + momentum + 1.0
        )
        matrix[np.diag_indices_from(matrix)] += TWO_PI + harmonic_excess
        pre_symmetry_defect = float(np.max(np.abs(matrix - matrix.T)))
        matrix = 0.5 * (matrix + matrix.T)
        values, vectors = eigh(
            matrix,
            overwrite_a=False,
            check_finite=False,
            driver="evd",
        )
        keep = values <= TWO_PI + spec.eigenvalue_excess_ceiling
        retained = np.asarray(values[keep], dtype=float)
        degeneracy = 1 if momentum == 0 else 2
        for value in retained:
            spectrum.extend([float(value)] * degeneracy)
        retained_vectors = vectors[:, keep]
        if retained.size:
            residual_norm = np.linalg.norm(
                matrix @ retained_vectors
                - retained_vectors * retained[np.newaxis, :],
                axis=0,
            )
            maximum_ritz_residual = max(
                maximum_ritz_residual, float(np.max(residual_norm))
            )
        gram = evaluation.T @ evaluation
        orthogonality_defect = float(
            np.max(np.abs(gram - np.eye(gram.shape[0])))
        )
        maximum_orthogonality_defect = max(
            maximum_orthogonality_defect, orthogonality_defect
        )
        block_records.append(
            {
                "absolute_momentum": momentum,
                "basis_size": count,
                "retained_distinct_values": int(len(retained)),
                "degeneracy": degeneracy,
                "quadrature_orthogonality_defect": orthogonality_defect,
                "pre_symmetrization_defect": pre_symmetry_defect,
            }
        )

    values = np.sort(np.asarray(spectrum, dtype=float))
    if not len(values):
        raise RuntimeError("no radial eigenvalues were retained")
    metadata: dict[str, Any] = {
        "spec": asdict(spec),
        "angular_frequency": TWO_PI,
        "maximum_absolute_momentum": int(maximum_momentum),
        "block_count": int(len(block_records)),
        "basis_size_with_signed_degeneracy": int(
            sum(
                record["basis_size"] * record["degeneracy"]
                for record in block_records
            )
        ),
        "retained_eigenvalues_with_multiplicity": int(len(values)),
        "lowest_eigenvalue": float(values[0]),
        "highest_retained_eigenvalue": float(values[-1]),
        "maximum_quadrature_orthogonality_defect": maximum_orthogonality_defect,
        "max_absolute_ritz_residual": maximum_ritz_residual,
        "blocks": block_records,
    }
    return values, metadata
