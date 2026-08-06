from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


CODE_ROOT = Path(__file__).resolve().parents[1]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from henon_roof import (  # noqa: E402
    CycleSection,
    build_orbit_catalog,
    contraction_lipschitz_bound,
    exact_clock_audit,
    lift_cycle_by_contraction,
    mp_cycle_coefficients,
    mp_determinant,
    primitive_counts,
    primitive_state_cycles,
    symbolic_fixed_point_counts,
    weighted_orbits,
)


def test_neighbor_contraction_bound_is_parameter_dependent() -> None:
    with mp.workdps(60):
        bound_59 = contraction_lipschitz_bound("5.9")
        bound_60 = contraction_lipschitz_bound("6")
        bound_61 = contraction_lipschitz_bound("6.1")
        assert bound_59 > bound_60 > bound_61
        assert abs(bound_60 - 2 / mp.sqrt(17)) < mp.mpf("1e-55")
        assert abs(bound_59 - (2 / mp.sqrt(17)) * mp.sqrt(mp.mpf(6) / mp.mpf("5.9"))) < mp.mpf(
            "1e-55"
        )


def test_exact_primitive_counts_and_fixed_point_identity() -> None:
    expected = {
        1: 1,
        2: 0,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 4,
        8: 5,
        9: 8,
        10: 11,
        11: 18,
        12: 25,
    }
    assert primitive_counts(12) == expected
    assert [len(primitive_state_cycles(period)) for period in range(1, 13)] == list(
        expected.values()
    )
    fixed = symbolic_fixed_point_counts(12)
    for period in range(1, 13):
        assert fixed[period] == sum(
            divisor * expected[divisor]
            for divisor in range(1, period + 1)
            if period % divisor == 0
        )


def test_exact_clock_polynomials_and_unit_clock_factorization() -> None:
    audit = exact_clock_audit()
    x, u = sp.symbols("X u")
    assert sp.expand(sp.sympify(audit["fixed_orbit_multiplier_minimal_polynomial"], locals={"X": x})) == (
        x**4 - 4 * x**3 - 22 * x**2 - 4 * x + 1
    )
    assert sp.expand(sp.sympify(audit["period4_multiplier_minimal_polynomial"], locals={"X": x})) == (
        x**2 - 578 * x + 1
    )
    assert sp.expand((1 - u**2) * (1 - u + u**2)) == 1 - u + u**3 - u**4
    assert audit["normalized_unstable_expansion_lower_bound"] == "773/224"
    assert audit["roof_positive"] is True
    assert audit["unit_clock_periodicity"] == "2*pi*i"


def test_zero_action_period4_orbit_is_exactly_recovered() -> None:
    # State word -- -> +- -> ++ -> -+ -> -- gives signs -++-.
    record = lift_cycle_by_contraction((0, 2, 3, 1), parameter=6, dps=60)
    assert record.canonical_word == "--|+-|++|-+"
    assert record.sign_word == "-++-"
    assert mp.mpf(record.action) == 0
    with mp.workdps(70):
        expected = 1 / mp.sqrt(6)
        coordinates = [mp.mpf(value) for value in record.coordinates]
        assert max(
            abs(left - right)
            for left, right in zip(
                coordinates, (-expected, expected, expected, -expected), strict=True
            )
        ) < mp.mpf("1e-50")
        assert abs(mp.mpf(record.monodromy_trace) - 578) < mp.mpf("1e-50")


def test_multiplier_polynomials_supply_nonlattice_ingredients() -> None:
    audit = exact_clock_audit()
    x = sp.symbols("X")
    fixed = sp.Poly(
        sp.sympify(audit["fixed_orbit_multiplier_minimal_polynomial"], locals={"X": x}),
        x,
    )
    period4 = sp.Poly(
        sp.sympify(audit["period4_multiplier_minimal_polynomial"], locals={"X": x}),
        x,
    )
    fixed_multiplier = sp.sympify(audit["fixed_orbit_multiplier"])
    period4_multiplier = sp.sympify(audit["period4_multiplier"])
    assert sp.simplify(fixed.as_expr().subs(x, fixed_multiplier)) == 0
    assert sp.simplify(period4.as_expr().subs(x, period4_multiplier)) == 0
    assert fixed.degree() == 4
    assert period4.degree() == 2
    moduli = audit["fixed_multiplier_conjugate_moduli"]
    assert len(moduli) == 4
    assert all(abs(left - right) > 1e-12 for left, right in zip(moduli[:-1], moduli[1:], strict=True))
    assert audit["fixed_multiplier_all_conjugate_moduli_distinct"] is True
    assert audit["nonlattice_proof_inputs_pass"] is True


def test_cycle_section_exact_zero_clock_coefficients() -> None:
    records = build_orbit_catalog(max_period=4, parameter=6, dps=50)
    orbits = weighted_orbits(records)
    untwisted = CycleSection(orbits, cutoff=4, kappa=0).product_coefficients(0)
    twisted = CycleSection(orbits, cutoff=4, kappa=1).product_coefficients(0)
    np.testing.assert_allclose(untwisted, [1, -1, 0, -1, -1], atol=1e-14)
    np.testing.assert_allclose(twisted, [1, -1, 0, 1, -1], atol=1e-14)
    assert abs(np.sum(twisted)) < 1e-14


def test_product_and_trace_determinant_implementations_agree() -> None:
    records = build_orbit_catalog(max_period=6, parameter=6, dps=55)
    orbits = weighted_orbits(records)
    probes = (0.0 + 0.0j, 0.11 + 1.37j, -0.07 + 3.21j)
    for kappa in (0, 1):
        section = CycleSection(orbits, cutoff=6, kappa=kappa)
        for probe in probes:
            np.testing.assert_allclose(
                section.product_coefficients(probe),
                section.trace_coefficients(probe),
                rtol=1e-11,
                atol=1e-12,
            )
            product = mp_cycle_coefficients(
                orbits, 6, probe, kappa, dps=60, method="product"
            )
            trace = mp_cycle_coefficients(
                orbits, 6, probe, kappa, dps=60, method="trace"
            )
            with mp.workdps(70):
                assert max(
                    abs(left - right)
                    for left, right in zip(product, trace, strict=True)
                ) < mp.mpf("1e-50")
                assert abs(
                    mp.fsum(product)
                    - mp_determinant(orbits, 6, probe, kappa, dps=60)
                ) < mp.mpf("1e-50")
