from __future__ import annotations

import pytest

from cat_torsion.algebra import (
    CAT_MATRIX,
    LOCKED_LEDGER,
    delta_direct,
    delta_recurrence,
    factor_locked_integer,
    frozen_ledger_records,
    validate_hyperbolic_sl2,
)


def test_dual_engines_and_locked_factorizations_match_all_twelve_periods():
    records = frozen_ledger_records()
    assert [record["period"] for record in records] == list(range(1, 13))
    assert all(record["engines_agree"] for record in records)
    assert all(record["locked_record_matches"] for record in records)
    for period, delta, factors, _ in LOCKED_LEDGER:
        assert delta_direct(CAT_MATRIX, period) == delta
        assert delta_recurrence(CAT_MATRIX, period) == delta
        assert factor_locked_integer(delta) == factors


def test_period_and_factor_scope_are_closed():
    for period in (0, 13, 20):
        with pytest.raises(ValueError):
            delta_direct(CAT_MATRIX, period)
    with pytest.raises(ValueError):
        factor_locked_integer(17)


def test_hyperbolic_sl2_scope_accepts_both_trace_signs_only():
    assert validate_hyperbolic_sl2(CAT_MATRIX)["accepted"] is True
    assert validate_hyperbolic_sl2(((-2, -1), (-1, -1)))["accepted"] is True
    assert validate_hyperbolic_sl2(((1, 0), (0, 1)))["accepted"] is False
    assert validate_hyperbolic_sl2(((1, 1), (0, 1)))["accepted"] is False
    assert validate_hyperbolic_sl2(((2, 1), (1, 0)))["accepted"] is False
