"""Exact primitive and guarded-boundary tests below the registered tuple."""

from __future__ import annotations

import pytest


def test_generalized_binomial_negative_upper_and_endpoints(r_engine):
    for lower in range(7):
        assert r_engine.generalized_binomial(-1, lower) == (-1) ** lower
        assert r_engine.generalized_binomial(-2, lower) == ((-1) ** lower) * (lower + 1)
    assert r_engine.generalized_binomial(-17, 0) == 1
    assert r_engine.generalized_binomial(5, -1) == 0
    assert r_engine.generalized_binomial(5, 6) == 0
    assert r_engine._r_rho(0, 0, 5) == 2


@pytest.mark.parametrize("upper,lower", [(True, 0), (0, False), (1, 0), (0, 1)])
def test_boolean_is_not_an_integer_input(r_engine, upper, lower):
    if type(upper) is bool or type(lower) is bool:
        with pytest.raises(TypeError):
            r_engine.generalized_binomial(upper, lower)
    else:
        assert type(r_engine.generalized_binomial(upper, lower)) is int


def test_track_private_binomials_are_distinct_and_exact(q_engine, r_engine):
    assert q_engine._q_choose(8, 0) == 1
    assert q_engine._q_choose(8, 9) == 0
    assert r_engine._r_binomial(8, 0) == 1
    assert r_engine._r_binomial(8, 9) == 0
    with pytest.raises(TypeError):
        q_engine._q_choose(True, 0)
    with pytest.raises(TypeError):
        r_engine._r_binomial(8, False)


def test_guarded_empty_range_without_registered_evaluation(r_engine):
    assert r_engine.A_value(5, 2) == 0
    assert r_engine.H_value(3, 0) == 1
