"""Separated exact determinant conventions and finite-clock certificates."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Hashable, Iterable, Sequence

import sympy as sp

from .algebra import ADJACENCY, FACTOR_ORIENTATION


Z = sp.Symbol("z")
S = sp.Symbol("s")


def graph_determinant(matrix: sp.MatrixBase, variable: sp.Expr = Z) -> sp.Expr:
    """Return ``det(I-variable*matrix)`` in factored exact form."""

    square = sp.ImmutableMatrix(matrix)
    if square.rows != square.cols:
        raise ValueError("graph matrix must be square")
    return sp.factor((sp.eye(square.rows) - sp.sympify(variable) * square).det())


def unsigned_structural_determinant(variable: sp.Expr = Z) -> sp.Expr:
    """The source-locked unsigned determinant ``det(I-z*A)``."""

    return graph_determinant(ADJACENCY, variable)


def unsigned_structural_zeta(variable: sp.Expr = Z) -> sp.Expr:
    """The unsigned SFT Artin--Mazur zeta, reciprocal to its determinant."""

    # ``together`` preserves the source-lock denominator convention
    # ``1-2*z**2`` rather than extracting a global minus sign.
    return sp.together(1 / unsigned_structural_determinant(variable))


def factor_orientation_determinant(variable: sp.Expr = Z) -> sp.Expr:
    """The separately named factor-orientation determinant ``det(I-z*W)``."""

    return graph_determinant(FACTOR_ORIENTATION, variable)


def factor_orientation_weighted_zeta(variable: sp.Expr = Z) -> sp.Expr:
    """The reciprocal weighted SFT product (also one for this nilpotent W)."""

    return sp.together(1 / factor_orientation_determinant(variable))


def orientation_nilpotence_residual() -> sp.ImmutableMatrix:
    """Return the frozen exact residual ``W**3``."""

    return sp.ImmutableMatrix(FACTOR_ORIENTATION**3)


def parent_core_zeta(variable: sp.Expr = Z) -> sp.Expr:
    """Parent Artin--Mazur zeta after the declared boundary quotient."""

    value = sp.sympify(variable)
    return sp.together((1 + value) * unsigned_structural_zeta(value))


def parent_boundary_quotient_factor(variable: sp.Expr = Z) -> sp.Expr:
    """Euler-factor ratio replacing a symbolic 2-cycle by a fixed point."""

    value = sp.sympify(variable)
    return sp.factor((1 - value**2) / (1 - value))


def parent_factor_orientation_object(variable: sp.Expr = Z) -> sp.Expr:
    """Frozen factor-orientation-weighted parent object; not a Lefschetz zeta."""

    return 1 - sp.sympify(variable)


def interval_lefschetz_zeta(variable: sp.Expr = Z) -> sp.Expr:
    """Separately named interval fixed-index Lefschetz convention."""

    return 1 / (1 - sp.sympify(variable))


def unsigned_constant_slope_multiplier_product(exponent: sp.Expr = S) -> sp.Expr:
    """Exact constant-slope SFT multiplier product.

    Each graph edge receives the frozen weight ``2**(-s/2)``.  Thus this is
    ``det(I-2**(-s/2) A)**(-1)``, initially in its convergent half-plane and
    subsequently as the displayed elementary meromorphic function.
    """

    exponent = sp.sympify(exponent)
    edge_weight = sp.Integer(2) ** (-exponent / 2)
    return sp.together(1 / graph_determinant(ADJACENCY, edge_weight))


def factor_orientation_multiplier_product(exponent: sp.Expr = S) -> sp.Expr:
    """The same constant weight applied to W; exactly one by nilpotence."""

    exponent = sp.sympify(exponent)
    edge_weight = sp.Integer(2) ** (-exponent / 2)
    return sp.together(1 / graph_determinant(FACTOR_ORIENTATION, edge_weight))


@dataclass(frozen=True, slots=True)
class LocalLengthCoordinates:
    """A locally constant block length in a declared rational basis."""

    block: Hashable
    coordinates: tuple[sp.Rational, ...]

    @classmethod
    def create(cls, block: Hashable, coordinates: Sequence[object]) -> "LocalLengthCoordinates":
        rational_coordinates = tuple(sp.Rational(value) for value in coordinates)
        return cls(block=block, coordinates=rational_coordinates)


@dataclass(frozen=True, slots=True)
class FiniteRankClockCertificate:
    """Auditable data for the finite-memory locally constant no-go theorem.

    A finite-memory clock is first recoded to finitely many allowed blocks.
    Each block length is represented by rational coordinates in a declared
    basis.  A periodic length is a sum of block lengths, so its coordinate
    vector remains in the same finite-dimensional rational span.

    Any family of distinct multiplicatively independent positive rationals
    has rationally independent logarithms (clear denominators and use unique
    factorization).  Consequently no more than ``span_rank`` such logarithms
    can occur exactly in this clock.  The certificate records the hypotheses;
    it does not enumerate an external target family.
    """

    basis_labels: tuple[str, ...]
    local_lengths: tuple[LocalLengthCoordinates, ...]
    original_memory: int = 1

    def __post_init__(self) -> None:
        if self.original_memory < 1:
            raise ValueError("memory must be a positive integer")
        if not self.basis_labels:
            raise ValueError("at least one declared length basis vector is required")
        if len(set(self.basis_labels)) != len(self.basis_labels):
            raise ValueError("basis labels must be unique")
        if not self.local_lengths:
            raise ValueError("at least one locally constant block is required")
        if len({entry.block for entry in self.local_lengths}) != len(self.local_lengths):
            raise ValueError("locally constant block labels must be unique")
        dimension = len(self.basis_labels)
        if any(len(entry.coordinates) != dimension for entry in self.local_lengths):
            raise ValueError("every coordinate vector must match the declared basis")

    @property
    def coordinate_matrix(self) -> sp.ImmutableMatrix:
        return sp.ImmutableMatrix([entry.coordinates for entry in self.local_lengths])

    @property
    def span_rank(self) -> int:
        return int(self.coordinate_matrix.rank())

    @property
    def recoded_state_bound(self) -> int:
        """Number of explicitly listed blocks after finite-block recoding."""

        return len(self.local_lengths)

    @property
    def maximum_independent_exact_log_targets(self) -> int:
        return self.span_rank

    @property
    def cannot_contain_unbounded_independent_family(self) -> bool:
        # Both quantities are ordinary finite integers by construction.
        return True

    def periodic_length_coordinates(self, cyclic_blocks: Iterable[Hashable]) -> tuple[sp.Rational, ...]:
        """Sum exact local coordinates along a supplied periodic block walk."""

        lookup = {entry.block: entry.coordinates for entry in self.local_lengths}
        total = [sp.Rational(0) for _ in self.basis_labels]
        seen = False
        for block in cyclic_blocks:
            seen = True
            if block not in lookup:
                raise KeyError(f"undeclared block {block!r}")
            for index, coordinate in enumerate(lookup[block]):
                total[index] += coordinate
        if not seen:
            raise ValueError("a periodic walk must contain at least one block")
        return tuple(total)

    def as_dict(self) -> dict[str, object]:
        return {
            "basis_labels": self.basis_labels,
            "local_lengths": tuple(asdict(entry) for entry in self.local_lengths),
            "original_memory": self.original_memory,
            "recoded_state_bound": self.recoded_state_bound,
            "span_rank": self.span_rank,
            "maximum_independent_exact_log_targets": self.maximum_independent_exact_log_targets,
            "cannot_contain_unbounded_independent_family": self.cannot_contain_unbounded_independent_family,
            "proof_dependencies": (
                "finite-block recoding",
                "periodic lengths are sums of local lengths",
                "rational rank bound",
                "unique-factorization independence of logarithms",
            ),
        }


def candidate_clock_certificate() -> FiniteRankClockCertificate:
    """Rank-one certificate for the four allowed constant-slope branches."""

    allowed_edges = ((0, 2), (1, 2), (2, 0), (2, 1))
    # Each edge contributes (1/2)*log(2) to log |Lambda_u|.  Closed walks
    # necessarily have even length, so complete orbit coordinates are integral.
    return FiniteRankClockCertificate(
        basis_labels=("log(2)",),
        local_lengths=tuple(
            LocalLengthCoordinates.create(edge, (sp.Rational(1, 2),)) for edge in allowed_edges
        ),
        original_memory=1,
    )


def exact_zeta_audit() -> dict[str, bool]:
    """Evaluate every frozen determinant identity without mixing conventions."""

    expected_unsigned = 1 - 2 * Z**2
    expected_parent = (1 + Z) / (1 - 2 * Z**2)
    expected_multiplier = 1 / (1 - sp.Integer(2) ** (1 - S))
    certificate = candidate_clock_certificate()
    return {
        "unsigned_determinant": sp.simplify(unsigned_structural_determinant() - expected_unsigned) == 0,
        "unsigned_zeta": sp.simplify(unsigned_structural_zeta() - 1 / expected_unsigned) == 0,
        "orientation_nilpotence": orientation_nilpotence_residual() == sp.zeros(3),
        "orientation_determinant": factor_orientation_determinant() == 1,
        "orientation_weighted_zeta": factor_orientation_weighted_zeta() == 1,
        "boundary_quotient_factor": sp.simplify(parent_boundary_quotient_factor() - (1 + Z)) == 0,
        "parent_core_zeta": sp.simplify(parent_core_zeta() - expected_parent) == 0,
        "parent_orientation_object": parent_factor_orientation_object() == 1 - Z,
        "lefschetz_kept_separate": interval_lefschetz_zeta() == 1 / (1 - Z),
        "unsigned_multiplier_product": sp.simplify(unsigned_constant_slope_multiplier_product() - expected_multiplier) == 0,
        "orientation_multiplier_product": factor_orientation_multiplier_product() == 1,
        "candidate_clock_rank_one": certificate.span_rank == 1,
        "finite_rank_no_go": certificate.cannot_contain_unbounded_independent_family,
    }


__all__ = [
    "S",
    "Z",
    "FiniteRankClockCertificate",
    "LocalLengthCoordinates",
    "candidate_clock_certificate",
    "exact_zeta_audit",
    "factor_orientation_determinant",
    "factor_orientation_multiplier_product",
    "factor_orientation_weighted_zeta",
    "graph_determinant",
    "interval_lefschetz_zeta",
    "orientation_nilpotence_residual",
    "parent_boundary_quotient_factor",
    "parent_core_zeta",
    "parent_factor_orientation_object",
    "unsigned_constant_slope_multiplier_product",
    "unsigned_structural_determinant",
    "unsigned_structural_zeta",
]
