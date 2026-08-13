"""Exact algebra for the source-locked PCF Markov--baker candidate.

This module deliberately contains no file I/O and no numerical target data.
All identities are evaluated in ``QQ[u] / (p(u))`` or in exact SymPy
arithmetic.  Floating-point approximations are presentation helpers only.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import sympy as sp


U: Final = sp.Symbol("u", real=True)
PARAMETER_POLYNOMIAL: Final = U**3 - 2 * U**2 + 2 * U - 2
ROOT_LOWER: Final = sp.Rational(3859, 2500)
ROOT_UPPER: Final = sp.Rational(15437, 10000)
PARAMETER_ROOT: Final = sp.CRootOf(PARAMETER_POLYNOMIAL, 0)
D: Final = U - 1

ADJACENCY: Final = sp.ImmutableMatrix(
    (
        (0, 0, 1),
        (0, 0, 1),
        (1, 1, 0),
    )
)
FACTOR_ORIENTATION: Final = sp.ImmutableMatrix(
    (
        (0, 0, 1),
        (0, 0, -1),
        (-1, -1, 0),
    )
)
PF_EIGENVALUE: Final = sp.sqrt(2)
RIGHT_PF_VECTOR: Final = sp.ImmutableMatrix(
    (sp.Rational(1, 2), sp.Rational(1, 2), 1 / sp.sqrt(2))
)
LEFT_PF_VECTOR: Final = RIGHT_PF_VECTOR
RECTANGLE_AREAS: Final = tuple(
    sp.simplify(LEFT_PF_VECTOR[i] * RIGHT_PF_VECTOR[i]) for i in range(3)
)
SYMPLECTIC_FORM: Final = sp.ImmutableMatrix(((0, 1), (-1, 0)))
ALLOWED_EDGES: Final = tuple(
    (i, j) for i in range(ADJACENCY.rows) for j in range(ADJACENCY.cols) if ADJACENCY[i, j]
)


@dataclass(frozen=True, slots=True)
class RootIsolationCertificate:
    """An exact sign-change and root-count certificate."""

    lower: sp.Rational
    upper: sp.Rational
    polynomial_at_lower: sp.Rational
    polynomial_at_upper: sp.Rational
    open_interval_root_count: int

    @property
    def certified(self) -> bool:
        return (
            self.polynomial_at_lower < 0
            and self.polynomial_at_upper > 0
            and self.open_interval_root_count == 1
        )


def reduce_mod_parameter(expr: sp.Expr) -> sp.Expr:
    """Return the canonical degree-at-most-two representative modulo ``p(u)``."""

    numerator, denominator = sp.fraction(sp.cancel(sp.sympify(expr)))
    if denominator != 1:
        # This candidate's identities are polynomial.  Rejecting rational
        # functions avoids silently clearing a denominator that could vanish.
        raise ValueError("reduction expects a polynomial expression in u")
    remainder = sp.rem(
        sp.Poly(sp.expand(numerator), U, domain=sp.QQ),
        sp.Poly(PARAMETER_POLYNOMIAL, U, domain=sp.QQ),
    )
    return sp.factor(remainder.as_expr())


def root_isolation_certificate() -> RootIsolationCertificate:
    """Certify the frozen isolating interval without decimal root finding."""

    polynomial = sp.Poly(PARAMETER_POLYNOMIAL, U, domain=sp.QQ)
    return RootIsolationCertificate(
        lower=ROOT_LOWER,
        upper=ROOT_UPPER,
        polynomial_at_lower=sp.factor(PARAMETER_POLYNOMIAL.subs(U, ROOT_LOWER)),
        polynomial_at_upper=sp.factor(PARAMETER_POLYNOMIAL.subs(U, ROOT_UPPER)),
        open_interval_root_count=int(polynomial.count_roots(ROOT_LOWER, ROOT_UPPER)),
    )


def parent_map(x: sp.Expr) -> sp.Expr:
    """The quadratic parent ``f_u(x)=1-u*x**2``."""

    return 1 - U * sp.sympify(x) ** 2


def postcritical_orbit() -> tuple[sp.Expr, ...]:
    """Return ``0 -> 1 -> -d -> d -> d`` reduced modulo the PCF polynomial."""

    orbit: list[sp.Expr] = [sp.Integer(0)]
    for _ in range(4):
        orbit.append(reduce_mod_parameter(parent_map(orbit[-1])))
    return tuple(orbit)


def postcritical_residuals() -> tuple[sp.Expr, ...]:
    """Residuals against the five frozen postcritical entries."""

    expected = (sp.Integer(0), sp.Integer(1), -D, D, D)
    return tuple(reduce_mod_parameter(actual - target) for actual, target in zip(postcritical_orbit(), expected))


def markov_endpoint_images() -> tuple[tuple[sp.Expr, sp.Expr], ...]:
    """Images of the ordered endpoints of I0, I1, and I2.

    The interval endpoints are ``(-d,0)``, ``(0,d)``, and ``(d,1)``.
    Their ordered image pairs encode both the image interval and orientation.
    """

    endpoints = ((-D, 0), (0, D), (D, 1))
    return tuple(
        tuple(reduce_mod_parameter(parent_map(x)) for x in pair)  # type: ignore[misc]
        for pair in endpoints
    )


def branch_orientation(source: int) -> int:
    """Return the one-dimensional parent orientation on an interval interior."""

    if source not in (0, 1, 2):
        raise IndexError("source label must be 0, 1, or 2")
    return 1 if source == 0 else -1


def branch_jacobian(source: int, target: int) -> sp.ImmutableMatrix:
    """Exact derivative of an allowed affine baker branch."""

    if (source, target) not in ALLOWED_EDGES:
        raise ValueError(f"edge {source}->{target} is not allowed")
    sign = FACTOR_ORIENTATION[source, target]
    return sp.ImmutableMatrix(
        ((sign * PF_EIGENVALUE, 0), (0, sign / PF_EIGENVALUE))
    )


def branch_symplectic_residual(source: int, target: int) -> sp.ImmutableMatrix:
    """Return ``J.T*Omega*J-Omega`` for an allowed edge."""

    jacobian = branch_jacobian(source, target)
    return sp.ImmutableMatrix(sp.simplify(jacobian.T * SYMPLECTIC_FORM * jacobian - SYMPLECTIC_FORM))


def strip_tiling_residuals() -> dict[str, tuple[sp.Expr, ...] | sp.Expr]:
    """Exact source-width, destination-height, and area-normalization residuals."""

    source_widths = tuple(
        sp.simplify(
            sum(ADJACENCY[i, j] * RIGHT_PF_VECTOR[j] / PF_EIGENVALUE for j in range(3))
            - RIGHT_PF_VECTOR[i]
        )
        for i in range(3)
    )
    destination_heights = tuple(
        sp.simplify(
            sum(LEFT_PF_VECTOR[i] * ADJACENCY[i, j] / PF_EIGENVALUE for i in range(3))
            - LEFT_PF_VECTOR[j]
        )
        for j in range(3)
    )
    return {
        "source_widths": source_widths,
        "destination_heights": destination_heights,
        "area_normalization": sp.simplify(sum(RECTANGLE_AREAS) - 1),
    }


def exact_identity_audit() -> dict[str, bool]:
    """Run the algebraic portion of the predeclared exact audit."""

    isolation = root_isolation_certificate()
    tiling = strip_tiling_residuals()
    expected_images = ((D, 1), (1, D), (D, -D))
    endpoint_residuals = tuple(
        reduce_mod_parameter(actual - expected)
        for actual_pair, expected_pair in zip(markov_endpoint_images(), expected_images)
        for actual, expected in zip(actual_pair, expected_pair)
    )
    orientation_matches = all(
        FACTOR_ORIENTATION[i, j] == branch_orientation(i) for i, j in ALLOWED_EDGES
    )
    return {
        "root_isolation": isolation.certified,
        "pcf_orbit": all(residual == 0 for residual in postcritical_residuals()),
        "markov_endpoint_images": all(residual == 0 for residual in endpoint_residuals),
        "adjacency_right_pf": ADJACENCY * RIGHT_PF_VECTOR == PF_EIGENVALUE * RIGHT_PF_VECTOR,
        "adjacency_left_pf": LEFT_PF_VECTOR.T * ADJACENCY == PF_EIGENVALUE * LEFT_PF_VECTOR.T,
        "pf_normalization": sp.simplify((LEFT_PF_VECTOR.T * RIGHT_PF_VECTOR)[0] - 1) == 0,
        "rectangle_areas": RECTANGLE_AREAS == (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2)),
        "source_strip_tiling": all(value == 0 for value in tiling["source_widths"]),
        "destination_strip_tiling": all(value == 0 for value in tiling["destination_heights"]),
        "area_normalization": tiling["area_normalization"] == 0,
        "factor_orientation": orientation_matches,
        "branch_determinants": all(sp.simplify(branch_jacobian(i, j).det() - 1) == 0 for i, j in ALLOWED_EDGES),
        "branch_symplecticity": all(branch_symplectic_residual(i, j) == sp.zeros(2) for i, j in ALLOWED_EDGES),
    }


__all__ = [
    "ADJACENCY",
    "ALLOWED_EDGES",
    "D",
    "FACTOR_ORIENTATION",
    "LEFT_PF_VECTOR",
    "PARAMETER_POLYNOMIAL",
    "PARAMETER_ROOT",
    "PF_EIGENVALUE",
    "RECTANGLE_AREAS",
    "RIGHT_PF_VECTOR",
    "ROOT_LOWER",
    "ROOT_UPPER",
    "SYMPLECTIC_FORM",
    "U",
    "RootIsolationCertificate",
    "branch_jacobian",
    "branch_orientation",
    "branch_symplectic_residual",
    "exact_identity_audit",
    "markov_endpoint_images",
    "parent_map",
    "postcritical_orbit",
    "postcritical_residuals",
    "reduce_mod_parameter",
    "root_isolation_certificate",
    "strip_tiling_residuals",
]
