from __future__ import annotations

import sympy as sp
import pytest

from branch_baker.algebra import ADJACENCY
from branch_baker.cycles import (
    DYADIC_ADJACENCY,
    FROZEN_DYADIC_TOTAL_THROUGH_12,
    FROZEN_PRIMITIVE_COUNTS_1_TO_20,
    FROZEN_PRIMITIVE_TOTAL_THROUGH_20,
    boundary_quotient_ledger,
    canonical_rotation,
    direct_primitive_count_vector,
    direct_primitive_cycles,
    dyadic_primitive_counts,
    exact_candidate_cycle_audit,
    is_primitive_word,
    multiplier_moduli,
    parent_core_periodic_point_counts,
    periodic_point_counts,
    primitive_orbit_counts,
    primitive_orbit_counts_from_periodic_points,
)


def test_candidate_periodic_point_counts_have_only_even_periods() -> None:
    counts = periodic_point_counts(ADJACENCY, 20)
    expected = tuple(0 if period % 2 else 2 ** (period // 2 + 1) for period in range(1, 21))
    assert counts == expected


def test_mobius_counts_match_frozen_vector_and_total() -> None:
    counts = primitive_orbit_counts(ADJACENCY, 20)
    assert counts == FROZEN_PRIMITIVE_COUNTS_1_TO_20
    assert sum(counts) == FROZEN_PRIMITIVE_TOTAL_THROUGH_20 == 226


def test_direct_enumeration_is_independent_and_matches_mobius() -> None:
    direct = direct_primitive_cycles(ADJACENCY, 20)
    assert direct[1] == ()
    assert direct[2] == ((0, 2), (1, 2))
    assert tuple(len(direct[period]) for period in range(1, 21)) == FROZEN_PRIMITIVE_COUNTS_1_TO_20
    assert direct_primitive_count_vector(ADJACENCY, 20) == primitive_orbit_counts(ADJACENCY, 20)
    audit = exact_candidate_cycle_audit()
    assert audit.passed
    assert audit.as_dict()["passed"] is True


def test_rotation_and_primitivity_helpers() -> None:
    assert canonical_rotation((2, 0, 2, 1)) == (0, 2, 1, 2)
    assert is_primitive_word((0, 2))
    assert not is_primitive_word((0, 2, 0, 2))
    assert not is_primitive_word(())
    with pytest.raises(ValueError, match="nonempty"):
        canonical_rotation(())


def test_dyadic_positive_control_recovers_747_necklaces() -> None:
    expected = (2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335)
    counts = dyadic_primitive_counts(12)
    assert DYADIC_ADJACENCY == sp.ones(2)
    assert counts == expected
    assert sum(counts) == FROZEN_DYADIC_TOTAL_THROUGH_12 == 747
    assert direct_primitive_count_vector(DYADIC_ADJACENCY, 12) == expected


def test_boundary_quotient_replaces_exactly_one_cycle() -> None:
    ledger = boundary_quotient_ledger(20)
    assert ledger.removed_symbolic_cycle == (1, 2)
    assert ledger.added_parent_fixed_label == "d"
    assert ledger.primitive_count_delta == (1, -1) + (0,) * 18
    assert ledger.sole_declared_collapse_verified
    record = ledger.as_dict()
    assert record["primitive_count_delta"] == (1, -1) + (0,) * 18
    assert record["sole_declared_collapse_verified"] is True
    assert sum(ledger.symbolic_primitive_orbit_counts) == 226
    assert sum(ledger.parent_primitive_orbit_counts) == 226
    assert parent_core_periodic_point_counts(8) == (1, 3, 1, 7, 1, 15, 1, 31)


def test_multiplier_moduli_follow_even_period_clock() -> None:
    for period in range(2, 22, 2):
        half_period = period // 2
        assert multiplier_moduli(period) == (2**half_period, sp.Rational(1, 2) ** half_period)
    with pytest.raises(ValueError, match="even"):
        multiplier_moduli(3)


def test_cycle_input_validation() -> None:
    with pytest.raises(ValueError, match="square"):
        periodic_point_counts(((1, 0, 1), (0, 1, 0)), 2)
    with pytest.raises(ValueError, match="zero or one"):
        primitive_orbit_counts(((2,),), 2)
    with pytest.raises(ValueError, match="nonnegative"):
        primitive_orbit_counts_from_periodic_points((-1,))
    with pytest.raises(ValueError, match="period 20"):
        exact_candidate_cycle_audit(21)
