"""Small exact binary-field checks for the local coefficient obstruction."""

from __future__ import annotations

from typing import Any

import sympy as sp

from .algebra import iterate_polynomial


def _degree(value: int) -> int:
    return value.bit_length() - 1


def _remainder(dividend: int, divisor: int) -> int:
    if divisor <= 0:
        raise ValueError("binary polynomial divisor must be nonzero")
    value = dividend
    divisor_degree = _degree(divisor)
    while value and _degree(value) >= divisor_degree:
        value ^= divisor << (_degree(value) - divisor_degree)
    return value


def _is_irreducible(value: int) -> bool:
    degree = _degree(value)
    if degree < 1 or not (value & 1) or not (value & (1 << degree)):
        return False
    for divisor_degree in range(1, degree // 2 + 1):
        for middle in range(1 << (divisor_degree - 1)):
            divisor = (1 << divisor_degree) | (middle << 1) | 1
            if _remainder(value, divisor) == 0:
                return False
    return True


def irreducible_monic_binary(degree: int) -> tuple[int, ...]:
    """Enumerate monic irreducibles with nonzero constant term over ``F_2``."""

    if type(degree) is not int or degree < 1:
        raise ValueError("degree must be a positive integer")
    values = []
    for middle in range(1 << (degree - 1)):
        candidate = (1 << degree) | (middle << 1) | 1
        if _is_irreducible(candidate):
            values.append(candidate)
    return tuple(values)


def polynomial_string(value: int, variable: str = "T") -> str:
    """Render an integer-bit binary polynomial deterministically."""

    terms: list[str] = []
    for exponent in range(_degree(value), -1, -1):
        if not (value >> exponent) & 1:
            continue
        if exponent == 0:
            terms.append("1")
        elif exponent == 1:
            terms.append(variable)
        else:
            terms.append(f"{variable}^{exponent}")
    return "+".join(terms) if terms else "0"


def _filter_row(value: int, degree: int) -> dict[str, Any]:
    e_n_minus_1 = (value >> 1) & 1
    e_n_minus_2 = (value >> 2) & 1
    return {
        "polynomial": polynomial_string(value),
        "degree": degree,
        "coefficient_T": e_n_minus_1,
        "coefficient_T2": e_n_minus_2,
        "two_coefficient_filter_passes": e_n_minus_1 == 0 and e_n_minus_2 == 0,
    }


def frobenius_reduction_audit(*, maximum_period: int = 7) -> dict[str, Any]:
    """Verify ``g^n-X = X^(2^n)-X`` after reduction modulo ``u``."""

    if type(maximum_period) is not int or maximum_period < 1:
        raise ValueError("maximum_period must be positive")
    X = sp.Symbol("X")
    reduced_map = sp.Poly(X**2, X, modulus=2)
    records = []
    for period in range(1, maximum_period + 1):
        equation = iterate_polynomial(reduced_map, period) - sp.Poly(X, X, modulus=2)
        expected = sp.Poly(X ** (2**period) - X, X, modulus=2)
        derivative = equation.diff()
        squarefree = sp.gcd(equation, derivative).degree() == 0
        records.append(
            {
                "period": period,
                "degree": int(equation.degree()),
                "frobenius_formula": equation == expected,
                "derivative": sp.sstr(derivative.as_expr()),
                "squarefree": squarefree,
            }
        )
    passed = all(record["frobenius_formula"] and record["squarefree"] for record in records)
    return {
        "identity": "g^n-X == X^(2^n)-X modulo u and 2",
        "periods": records,
        "pass": passed,
    }


def mod2_lift_audit() -> dict[str, Any]:
    """Check the coefficient tuple of ``z_alpha=alpha+u+u^2 (mod 2,u^3)``."""

    alpha, u = sp.symbols("alpha u")

    def truncate_u3(expression: sp.Expr) -> sp.Poly:
        expanded = sp.Poly(expression, alpha, u, modulus=2)
        kept = sum(
            coefficient * alpha**alpha_degree * u**u_degree
            for (alpha_degree, u_degree), coefficient in expanded.terms()
            if u_degree < 3
        )
        return sp.Poly(kept, alpha, u, modulus=2)

    lift = alpha + u + u**2
    sigma_lift = truncate_u3(alpha**2 + u + u**2)
    mapped_lift = truncate_u3(lift**2 - u)
    identity = sigma_lift == mapped_lift
    return {
        "quotient_ring": "F_(2^n)[u]/(u^3)",
        "lift_coefficients_in_1_u_u2": ["alpha", "1", "1"],
        "sigma_lift": sp.sstr(sigma_lift.as_expr()),
        "lift_squared_minus_u": sp.sstr(mapped_lift.as_expr()),
        "identity": "sigma(z_alpha)=z_alpha^2-u",
        "pass": identity,
    }


def two_coefficient_filter_audit() -> dict[str, Any]:
    """Enumerate the source-locked degree 2/3 obstruction and degree 4 witness."""

    records = {
        degree: [_filter_row(value, degree) for value in irreducible_monic_binary(degree)]
        for degree in (2, 3, 4)
    }
    expected_degree_two = {"T^2+T+1"}
    expected_degree_three = {"T^3+T+1", "T^3+T^2+1"}
    degree_two_names = {row["polynomial"] for row in records[2]}
    degree_three_names = {row["polynomial"] for row in records[3]}
    witness = (1 << 4) | (1 << 3) | 1
    reciprocal = (1 << 4) | (1 << 1) | 1
    witness_row = _filter_row(witness, 4)
    reciprocal_high_coefficients_zero = ((reciprocal >> 3) & 1) == 0 and ((reciprocal >> 2) & 1) == 0
    small_period_obstruction = all(
        not row["two_coefficient_filter_passes"]
        for degree in (2, 3)
        for row in records[degree]
    )
    degree_four_insufficient = (
        _is_irreducible(witness)
        and _is_irreducible(reciprocal)
        and witness_row["two_coefficient_filter_passes"]
        and reciprocal_high_coefficients_zero
    )
    return {
        "filter": "e_(n-1)=e_(n-2)=0, equivalently low T and T^2 coefficients vanish",
        "irreducibles": {str(degree): rows for degree, rows in records.items()},
        "degree_two_exact_list": degree_two_names == expected_degree_two,
        "degree_three_exact_list": degree_three_names == expected_degree_three,
        "n2_n3_obstructed": small_period_obstruction,
        "degree_four_witness": witness_row,
        "degree_four_reciprocal": polynomial_string(reciprocal),
        "degree_four_filter_insufficient": degree_four_insufficient,
        "all_period_inference_allowed": False,
        "pass": (
            degree_two_names == expected_degree_two
            and degree_three_names == expected_degree_three
            and small_period_obstruction
            and degree_four_insufficient
        ),
    }
