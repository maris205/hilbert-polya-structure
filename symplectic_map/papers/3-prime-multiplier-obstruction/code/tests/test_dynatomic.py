import sympy as sp

from prime_multiplier.controls import quadratic_map
from prime_multiplier.dynatomic import (
    exact_period_component,
    expected_formal_degree_quadratic,
    formal_dynatomic,
)


def test_frozen_formal_degrees():
    assert [expected_formal_degree_quadratic(n) for n in range(1, 5)] == [2, 2, 6, 12]


def test_power_map_has_no_low_period_contamination():
    base = quadratic_map(sp.Rational(0))
    for period in range(1, 5):
        component = exact_period_component(base, period)
        assert component.formal_degree == expected_formal_degree_quadratic(period)
        assert component.exact_degree == component.formal_degree
        assert not component.has_formal_period_contamination


def test_nonintegral_control_saturates_double_period_two_collision():
    base = quadratic_map(sp.Rational(-3, 4))
    component = exact_period_component(base, 2)
    z = base.gens[0]
    assert component.formal == sp.Poly((z + sp.Rational(1, 2)) ** 2, z, domain=sp.QQ)
    assert component.exact_degree == 0
    assert component.contamination_degree == 2
    assert [factor.degree() for factor in component.removed_factors] == [1, 1]


def test_dynatomic_rejects_nonpositive_period():
    base = quadratic_map(sp.Rational(0))
    for period in (0, -1):
        try:
            formal_dynatomic(base, period)
        except ValueError:
            pass
        else:
            raise AssertionError("nonpositive period was accepted")

