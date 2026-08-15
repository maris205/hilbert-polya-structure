import sympy as sp

from base2_clock.algebra import quadratic_map
from base2_clock.dynatomic import (
    audit_period,
    certificate_passes,
    exact_set_component,
    formal_dynatomic,
    normalized_cycle_product,
    radical,
)


def test_radical_exact_set_uses_proper_divisor_set_difference():
    base = quadratic_map(0)
    component = exact_set_component(base, 2)
    z = base.gens[0]
    assert component.exact_set == sp.Poly(z**2 + z + 1, z, domain=sp.QQ)
    assert component.exact_set == component.iterate_radical.exquo(component.lower_overlap).monic()
    assert component.formal_radical == component.exact_set


def test_formal_period_pollution_is_not_misreported_as_exact():
    base = quadratic_map(sp.Rational(-3, 4))
    component = exact_set_component(base, 2)
    assert component.formal_dynatomic.degree() == 2
    assert component.exact_set.degree() == 0
    assert component.formal_radical != component.exact_set
    assert component.lower_overlap == component.iterate_radical


def test_chebyshev_period_two_has_B_minus_one():
    base = quadratic_map(-2)
    z = base.gens[0]
    certificate = audit_period(base, 2)
    assert certificate.component.exact_set == sp.Poly(z**2 + z - 1, z, domain=sp.QQ)
    assert normalized_cycle_product(base, 2).rem(certificate.component.exact_set) == sp.Poly(
        -1, z, domain=sp.QQ
    )
    assert {item.target: item.hit for item in certificate.targets} == {
        sp.Rational(1): False,
        sp.Rational(-1): True,
    }
    assert certificate_passes(certificate)


def test_power_map_positive_and_negative_targets_are_distinguished():
    certificate = audit_period(quadratic_map(0), 2, targets=(1, -1, 2))
    hits = {item.target: item.hit for item in certificate.targets}
    assert hits == {sp.Rational(1): True, sp.Rational(-1): False, sp.Rational(2): False}
    assert all(item.engines_agree for item in certificate.targets)


def test_formal_dynatomic_exact_division_and_radical_are_monic():
    base = quadratic_map(1)
    formal = formal_dynatomic(base, 3)
    assert formal.degree() == 6
    assert formal.LC() == 1
    assert radical(formal).LC() == 1
