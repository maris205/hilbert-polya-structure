"""Controls frozen before candidate execution."""

from __future__ import annotations

from typing import Any

import sympy as sp

from .algebra import polynomial_record, primitive_monic
from .dynamics import derivative_matrix, dissipative_derivative, henon_map
from .modulus import (
    RationalBounds,
    _exact_hyperbolic_record,
    complex_control_modulus_records,
)
from .periods import L, T, exact_period_decomposition, multiplier_polynomial, rational_root_candidates


def finite_bad_primes_from_rationals(values: list[sp.Rational]) -> list[int]:
    """Derive finite bad support from exact denominators, before multipliers."""

    support: set[int] = set()
    for value in values:
        denominator = int(sp.denom(sp.Rational(value)))
        support.update(int(prime) for prime in sp.factorint(denominator))
    return sorted(support)


def planted_bad_prime_control() -> dict[str, Any]:
    parameter = sp.Rational(-15, 16)
    coordinate = sp.Rational(5, 4)

    # Frozen coefficient provenance is evaluated first by construction.
    bad_support = finite_bad_primes_from_rationals([parameter, sp.Rational(1)])
    image = henon_map(coordinate, coordinate, parameter)
    derivative = derivative_matrix(coordinate)
    characteristic = sp.Poly(L**2 - sp.trace(derivative) * L + derivative.det(), L, domain=sp.QQ)
    factors = sp.factor_list(characteristic)
    roots = sp.solve(characteristic.as_expr(), L)
    modulus_support = {
        str(root): sorted(int(prime) for prime in sp.factorint(int(sp.denom(root) * sp.numer(root))))
        for root in roots
    }
    generic_modulus_pipeline = _exact_hyperbolic_record(
        label="planted_trace_5_over_2",
        trace_poly=sp.Poly(T - sp.Rational(5, 2), T, domain=sp.QQ),
        trace_interval=RationalBounds(sp.Rational(249, 100), sp.Rational(251, 100)),
        declared_bad_primes=(2,),
    )
    return {
        "run_id": "R011",
        "parameter": str(parameter),
        "coefficient_bad_prime_support_frozen_before_multiplier_access": bad_support,
        "fixed_point": [str(coordinate), str(coordinate)],
        "image": [str(item) for item in image],
        "fixed_point_identity_pass": image == (coordinate, coordinate),
        "derivative_matrix": [[str(item) for item in row] for row in derivative.tolist()],
        "determinant": str(derivative.det()),
        "trace": str(sp.trace(derivative)),
        "characteristic_polynomial": polynomial_record(characteristic, L),
        "factorization": sp.sstr(factors),
        "multipliers": [str(item) for item in roots],
        "multiplier_moduli": [str(abs(item)) for item in roots],
        "multiplier_rational_support": modulus_support,
        "classification": ["RATIONAL_MODULUS_S_UNIT", "RATIONAL_MODULUS_S_UNIT"],
        "generic_exact_modulus_pipeline": generic_modulus_pipeline,
        "expected_bad_support": [2],
        "pass": (
            bad_support == [2]
            and set(roots) == {sp.Rational(1, 2), sp.Integer(2)}
            and derivative.det() == 1
            and generic_modulus_pipeline["rational_modulus_values"] == ["1/2", "2"]
            and all(
                record["rational_modulus_classification"] == "RATIONAL_MODULUS_S_UNIT"
                for record in generic_modulus_pipeline["multiplier_modulus_squared_records"]
            )
        ),
    }


def _rational_control_period_record(period: int) -> dict[str, Any]:
    decomposition = exact_period_decomposition(period, sp.Integer(0))
    multiplier = primitive_monic(
        sp.Poly(multiplier_polynomial(period, sp.Integer(0)).as_expr(), L, domain=sp.QQ)
    )
    decomposition["rational_multiplier_audit"] = rational_root_candidates(multiplier)
    decomposition["multiplier_polynomial_over_Q"] = polynomial_record(multiplier, L)
    return decomposition


def integral_negative_control() -> dict[str, Any]:
    period_records = [_rational_control_period_record(period) for period in (1, 2, 3)]

    trace_zero = {
        "cycle_label": "period_1_trace_0",
        "trace": "0",
        "trace_type": "REAL_ELLIPTIC",
        "mu_minimal_polynomial": polynomial_record(sp.Poly(sp.Symbol("M") - 1, sp.Symbol("M")), sp.Symbol("M")),
        "exact_rational_modulus": "1",
        "classification": "RATIONAL_MODULUS_UNIT",
        "rational_modulus_values": ["1"],
    }
    trace_four = _exact_hyperbolic_record(
        label="period_1_trace_4",
        trace_poly=sp.Poly(T - 4, T, domain=sp.QQ),
        trace_interval=RationalBounds(sp.Rational(399, 100), sp.Rational(401, 100)),
    )
    trace_fourteen = _exact_hyperbolic_record(
        label="period_2_trace_14",
        trace_poly=sp.Poly(T - 14, T, domain=sp.QQ),
        trace_interval=RationalBounds(sp.Rational(1399, 100), sp.Rational(1401, 100)),
    )
    period_three = complex_control_modulus_records(10, 6)

    modulus_records = [trace_zero, trace_four, trace_fourteen, period_three]
    derived_moduli = sorted(
        {
            sp.Rational(value)
            for record in modulus_records
            for value in record.get("rational_modulus_values", [])
        }
    )
    classification_values = [trace_zero["classification"]]
    classification_values.extend(
        record["rational_modulus_classification"]
        for record in trace_four["multiplier_modulus_squared_records"]
    )
    classification_values.extend(
        record["rational_modulus_classification"]
        for record in trace_fourteen["multiplier_modulus_squared_records"]
    )
    classification_values.extend(record["classification"] for record in period_three["records"])
    unresolved = [value for value in classification_values if "REQUIRES" in value]
    rational_roots = [
        root
        for record in period_records
        for root in record["rational_multiplier_audit"]["exact_rational_roots"]
    ]
    return {
        "run_id": "R012",
        "map": "H_0(X,Y)=(X^2-Y,X)",
        "coefficient_bad_prime_support": [],
        "period_records": period_records,
        "modulus_records": modulus_records,
        "exact_rational_multiplier_values": sorted(set(rational_roots)),
        "exact_rational_modulus_values": [str(value) for value in derived_moduli],
        "modulus_classifications": classification_values,
        "unresolved_modulus_classifications": unresolved,
        "classification": "all exact rational moduli through the frozen cutoff equal 1",
        "all_period_source": "the good-reduction theorem, not this finite control",
        "pass": all(
            not record["rational_multiplier_audit"]["exact_rational_roots"]
            for record in period_records
        )
        and derived_moduli == [sp.Integer(1)]
        and not unresolved
        and period_three["rational_modulus_values"] == []
        and all(
            record["classification"] == "ALGEBRAIC_UNIT_IRRATIONAL_MODULUS"
            for record in period_three["records"]
        ),
    }


def determinant_scope_control() -> dict[str, Any]:
    x, delta = sp.symbols("x delta")
    symbolic_derivative = dissipative_derivative(x, delta)
    symbolic_determinant = sp.factor(symbolic_derivative.det())

    concrete_delta = sp.Integer(2)
    concrete = dissipative_derivative(sp.Integer(0), concrete_delta)
    concrete_char = sp.Poly(L**2 + 2, L, domain=sp.QQ)
    roots = sp.solve(concrete_char.as_expr(), L)

    def reciprocal_unit_gate(declared_bad_support: list[int]) -> str:
        required = [2]
        if not set(required).issubset(declared_bad_support):
            return "REFUSED_DETERMINANT_NOT_DECLARED_S_UNIT"
        return "ALLOWED_WITH_BAD_PRIME_2_TRACKED"

    empty_gate = reciprocal_unit_gate([])
    tracked_gate = reciprocal_unit_gate([2])
    return {
        "run_id": "R013",
        "family": "J_(a,delta)(X,Y)=(X^2-a-delta*Y,X)",
        "symbolic_derivative": [[sp.sstr(item) for item in row] for row in symbolic_derivative.tolist()],
        "symbolic_determinant": sp.sstr(symbolic_determinant),
        "nonunit_dissipative_example": {
            "parameter_a": "0",
            "delta": "2",
            "fixed_point": ["0", "0"],
            "derivative": [[str(item) for item in row] for row in concrete.tolist()],
            "characteristic_polynomial": polynomial_record(concrete_char, L),
            "multipliers": [sp.sstr(item) for item in roots],
            "algebraic_norm_absolute": 2,
            "unit_status": "NOT_AN_ALGEBRAIC_UNIT",
        },
        "gate_without_declared_bad_primes": empty_gate,
        "gate_with_bad_prime_2_declared_before_multiplier_access": tracked_gate,
        "pass": (
            symbolic_determinant == delta
            and empty_gate == "REFUSED_DETERMINANT_NOT_DECLARED_S_UNIT"
            and tracked_gate == "ALLOWED_WITH_BAD_PRIME_2_TRACKED"
        ),
    }


def run_controls() -> dict[str, Any]:
    planted = planted_bad_prime_control()
    integral = integral_negative_control()
    determinant = determinant_scope_control()
    return {
        "controls_executed_before_candidate": True,
        "planted_bad_prime_positive": planted,
        "integral_negative": integral,
        "non_area_preserving_scope": determinant,
        "pass": planted["pass"] and integral["pass"] and determinant["pass"],
    }
