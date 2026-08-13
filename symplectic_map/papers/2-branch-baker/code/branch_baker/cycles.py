"""Exact periodic-orbit ledgers for finite directed graphs.

Two independent paths are intentionally provided:

* traces plus Möbius inversion;
* direct closed-word enumeration plus canonical rotation.

Agreement between them is a verification target rather than an assumption.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Iterable, Sequence

import sympy as sp

from .algebra import ADJACENCY


FROZEN_PRIMITIVE_COUNTS_1_TO_20 = (
    0,
    2,
    0,
    1,
    0,
    2,
    0,
    3,
    0,
    6,
    0,
    9,
    0,
    18,
    0,
    30,
    0,
    56,
    0,
    99,
)
FROZEN_PRIMITIVE_TOTAL_THROUGH_20 = 226
FROZEN_DYADIC_TOTAL_THROUGH_12 = 747
DYADIC_ADJACENCY = sp.ImmutableMatrix(((1, 1), (1, 1)))


def _as_square_integer_matrix(matrix: sp.MatrixBase | Sequence[Sequence[int]]) -> sp.ImmutableMatrix:
    result = sp.ImmutableMatrix(matrix)
    if result.rows != result.cols:
        raise ValueError("adjacency matrix must be square")
    if any(entry not in (0, 1) for entry in result):
        raise ValueError("adjacency matrix entries must be zero or one")
    return result


def periodic_point_counts(
    matrix: sp.MatrixBase | Sequence[Sequence[int]], max_period: int
) -> tuple[int, ...]:
    """Return ``trace(A**n)`` for ``1 <= n <= max_period``."""

    adjacency = _as_square_integer_matrix(matrix)
    if max_period < 0:
        raise ValueError("max_period must be nonnegative")
    return tuple(int(sp.trace(adjacency**period)) for period in range(1, max_period + 1))


def primitive_orbit_counts_from_periodic_points(
    fixed_point_counts: Sequence[int],
) -> tuple[int, ...]:
    """Möbius-invert periodic-point counts into primitive orbit counts.

    If ``N_n`` is the number of points fixed by the nth iterate and ``P_n``
    is the number of primitive *orbits* of length n, then
    ``N_n = sum_{d|n} d*P_d``.
    """

    counts = tuple(int(value) for value in fixed_point_counts)
    if any(value < 0 for value in counts):
        raise ValueError("fixed-point counts must be nonnegative")
    primitive: list[int] = []
    for period in range(1, len(counts) + 1):
        numerator = sum(
            int(sp.mobius(divisor)) * counts[period // divisor - 1]
            for divisor in sp.divisors(period)
        )
        quotient, remainder = divmod(numerator, period)
        if remainder or quotient < 0:
            raise ValueError("counts are not a valid finite-orbit ledger")
        primitive.append(quotient)
    return tuple(primitive)


def primitive_orbit_counts(
    matrix: sp.MatrixBase | Sequence[Sequence[int]], max_period: int
) -> tuple[int, ...]:
    """Primitive graph-orbit counts obtained by traces and Möbius inversion."""

    return primitive_orbit_counts_from_periodic_points(periodic_point_counts(matrix, max_period))


def canonical_rotation(word: Sequence[Any]) -> tuple[Any, ...]:
    """Lexicographically least cyclic rotation of a nonempty word."""

    values = tuple(word)
    if not values:
        raise ValueError("a cyclic word must be nonempty")
    return min(values[offset:] + values[:offset] for offset in range(len(values)))


def is_primitive_word(word: Sequence[Any]) -> bool:
    """Whether a cyclic word has no smaller rotational period."""

    values = tuple(word)
    if not values:
        return False
    period = len(values)
    return all(
        values != values[block:] + values[:block]
        for block in sp.divisors(period)
        if block < period
    )


def _closed_words_of_length(adjacency: sp.ImmutableMatrix, period: int) -> Iterable[tuple[int, ...]]:
    if period <= 0:
        return
    states = range(adjacency.rows)
    for start in states:
        path = [start]

        def extend() -> Iterable[tuple[int, ...]]:
            if len(path) == period:
                if adjacency[path[-1], start]:
                    yield tuple(path)
                return
            for target in states:
                if adjacency[path[-1], target]:
                    path.append(target)
                    yield from extend()
                    path.pop()

        yield from extend()


def direct_primitive_cycles(
    matrix: sp.MatrixBase | Sequence[Sequence[int]], max_period: int
) -> dict[int, tuple[tuple[int, ...], ...]]:
    """Enumerate primitive closed graph words, quotienting cyclic rotations."""

    adjacency = _as_square_integer_matrix(matrix)
    if max_period < 0:
        raise ValueError("max_period must be nonnegative")
    ledger: dict[int, tuple[tuple[int, ...], ...]] = {}
    for period in range(1, max_period + 1):
        representatives = {
            word
            for word in _closed_words_of_length(adjacency, period)
            if is_primitive_word(word) and word == canonical_rotation(word)
        }
        ledger[period] = tuple(sorted(representatives))
    return ledger


def direct_primitive_count_vector(
    matrix: sp.MatrixBase | Sequence[Sequence[int]], max_period: int
) -> tuple[int, ...]:
    """Primitive counts from direct enumeration, independent of traces."""

    ledger = direct_primitive_cycles(matrix, max_period)
    return tuple(len(ledger[period]) for period in range(1, max_period + 1))


def dyadic_primitive_counts(max_period: int = 12) -> tuple[int, ...]:
    """Primitive necklace counts for the two-symbol full shift."""

    return primitive_orbit_counts(DYADIC_ADJACENCY, max_period)


def parent_core_periodic_point_count(period: int) -> int:
    """Frozen boundary-quotient fixed-point formula for the parent core."""

    if period <= 0:
        raise ValueError("period must be positive")
    if period % 2:
        return 1
    half_period = period // 2
    return 2 ** (half_period + 1) - 1


def parent_core_periodic_point_counts(max_period: int) -> tuple[int, ...]:
    if max_period < 0:
        raise ValueError("max_period must be nonnegative")
    return tuple(parent_core_periodic_point_count(period) for period in range(1, max_period + 1))


@dataclass(frozen=True, slots=True)
class BoundaryQuotientLedger:
    """Auditable replacement of one symbolic 2-cycle by one fixed point."""

    max_period: int
    symbolic_periodic_point_counts: tuple[int, ...]
    parent_periodic_point_counts: tuple[int, ...]
    symbolic_primitive_orbit_counts: tuple[int, ...]
    parent_primitive_orbit_counts: tuple[int, ...]
    removed_symbolic_cycle: tuple[int, int] = (1, 2)
    added_parent_fixed_label: str = "d"

    @property
    def primitive_count_delta(self) -> tuple[int, ...]:
        return tuple(
            parent - symbolic
            for parent, symbolic in zip(
                self.parent_primitive_orbit_counts, self.symbolic_primitive_orbit_counts
            )
        )

    @property
    def sole_declared_collapse_verified(self) -> bool:
        expected = (1, -1) + (0,) * max(0, self.max_period - 2)
        return self.primitive_count_delta == expected[: self.max_period]

    def as_dict(self) -> dict[str, object]:
        return asdict(self) | {
            "primitive_count_delta": self.primitive_count_delta,
            "sole_declared_collapse_verified": self.sole_declared_collapse_verified,
        }


def boundary_quotient_ledger(max_period: int = 20) -> BoundaryQuotientLedger:
    """Construct the exact parent/SFT periodic quotient ledger."""

    symbolic_periodic = periodic_point_counts(ADJACENCY, max_period)
    parent_periodic = parent_core_periodic_point_counts(max_period)
    return BoundaryQuotientLedger(
        max_period=max_period,
        symbolic_periodic_point_counts=symbolic_periodic,
        parent_periodic_point_counts=parent_periodic,
        symbolic_primitive_orbit_counts=primitive_orbit_counts_from_periodic_points(symbolic_periodic),
        parent_primitive_orbit_counts=primitive_orbit_counts_from_periodic_points(parent_periodic),
    )


@dataclass(frozen=True, slots=True)
class ExactCycleAudit:
    max_period: int
    trace_mobius_counts: tuple[int, ...]
    direct_enumeration_counts: tuple[int, ...]
    frozen_counts: tuple[int, ...]

    @property
    def passed(self) -> bool:
        return self.trace_mobius_counts == self.direct_enumeration_counts == self.frozen_counts

    def as_dict(self) -> dict[str, object]:
        return asdict(self) | {"passed": self.passed}


def exact_candidate_cycle_audit(max_period: int = 20) -> ExactCycleAudit:
    """Compare the two exact ledgers with the frozen prediction."""

    if not 0 <= max_period <= len(FROZEN_PRIMITIVE_COUNTS_1_TO_20):
        raise ValueError("the frozen candidate audit is declared only through period 20")
    frozen = FROZEN_PRIMITIVE_COUNTS_1_TO_20[:max_period]
    return ExactCycleAudit(
        max_period=max_period,
        trace_mobius_counts=primitive_orbit_counts(ADJACENCY, max_period),
        direct_enumeration_counts=direct_primitive_count_vector(ADJACENCY, max_period),
        frozen_counts=frozen,
    )


def multiplier_moduli(period: int) -> tuple[sp.Expr, sp.Expr]:
    """Unstable/stable moduli for a frozen constant-slope primitive orbit."""

    if period <= 0 or period % 2:
        raise ValueError("the unquotiented graph has only positive even periods")
    half_period = period // 2
    return sp.Integer(2) ** half_period, sp.Rational(1, 2) ** half_period


__all__ = [
    "BoundaryQuotientLedger",
    "DYADIC_ADJACENCY",
    "ExactCycleAudit",
    "FROZEN_DYADIC_TOTAL_THROUGH_12",
    "FROZEN_PRIMITIVE_COUNTS_1_TO_20",
    "FROZEN_PRIMITIVE_TOTAL_THROUGH_20",
    "boundary_quotient_ledger",
    "canonical_rotation",
    "direct_primitive_count_vector",
    "direct_primitive_cycles",
    "dyadic_primitive_counts",
    "exact_candidate_cycle_audit",
    "is_primitive_word",
    "multiplier_moduli",
    "parent_core_periodic_point_count",
    "parent_core_periodic_point_counts",
    "periodic_point_counts",
    "primitive_orbit_counts",
    "primitive_orbit_counts_from_periodic_points",
]
