"""Closed-form exact-period decompositions through the frozen cutoff three."""

from __future__ import annotations

from typing import Any

import sympy as sp

from .algebra import (
    PARAMETER_POLYNOMIAL,
    U,
    equal_mod_parameter,
    norm_over_parameter,
    parameter_basis,
    polynomial_record,
    primitive_monic,
    reduce_parameter,
)
from .dynamics import cyclic_shift, monodromy, recurrence_equations, trace_formula

T = sp.Symbol("T")
L = sp.Symbol("L")


def _coefficient_reduce(poly: sp.Poly) -> sp.Poly:
    """Reduce every coefficient of a polynomial in the cubic parameter."""

    variable = poly.gens[0]
    degree = poly.degree()
    expression = sp.Integer(0)
    for index, coefficient in enumerate(poly.all_coeffs()):
        expression += reduce_parameter(coefficient) * variable ** (degree - index)
    return sp.Poly(expression, variable, domain=sp.QQ.frac_field(U))


def trace_polynomial(period: int, parameter: sp.Expr = U) -> sp.Poly:
    """Trace equation for exact cycles, over the coefficient field."""

    if period == 1:
        expression = T**2 - 4 * T - 4 * parameter
    elif period == 2:
        expression = T - (14 - 4 * parameter)
    elif period == 3:
        expression = (T - (10 - 8 * parameter)) ** 2 - (6 - 8 * parameter) ** 2 * (
            parameter - 1
        )
    else:
        raise ValueError("the source lock permits only periods 1, 2, and 3")
    poly = sp.Poly(sp.expand(expression), T, domain=sp.QQ.frac_field(U))
    return _coefficient_reduce(poly) if parameter == U else poly


def multiplier_polynomial(period: int, parameter: sp.Expr = U) -> sp.Poly:
    """Product of ``L^2-TL+1`` over exact-cycle trace roots."""

    trace_poly = trace_polynomial(period, parameter)
    expression = sp.resultant(trace_poly.as_expr(), L**2 - T * L + 1, T)
    poly = sp.Poly(expression, L, domain=sp.QQ.frac_field(U)).monic()
    return _coefficient_reduce(poly) if parameter == U else poly


def rational_multiplier_polynomial(period: int) -> sp.Poly:
    """Norm the cubic-field multiplier polynomial down to ``QQ``."""

    return norm_over_parameter(multiplier_polynomial(period, U).as_expr(), L)


def rational_root_candidates(poly: sp.Poly) -> dict[str, Any]:
    """Use the exact rational-root theorem for a monic constant-one polynomial."""

    if poly.LC() != 1 or poly.TC() not in (1, -1):
        raise ValueError("unit-candidate shortcut requires monic constant +/-1")
    candidates = [sp.Integer(-1), sp.Integer(1)]
    roots = [value for value in candidates if poly.eval(value) == 0]
    return {
        "rational_root_theorem_candidates": [str(value) for value in candidates],
        "exact_rational_roots": [str(value) for value in roots],
        "evaluations": {str(value): str(poly.eval(value)) for value in candidates},
    }


def _groebner_strings(equations: list[sp.Expr], variables: list[sp.Symbol]) -> list[str]:
    basis = sp.groebner(equations, *variables, order="lex", domain=sp.QQ.frac_field(U))
    return [sp.sstr(sp.expand(item.as_expr())) for item in basis.polys]


def _monic_squarefree(expression: sp.Expr, variable: sp.Symbol) -> sp.Poly:
    poly = sp.Poly(expression, variable, domain=sp.QQ.frac_field(U))
    return sp.Poly(poly.sqf_part().monic(), variable, domain=sp.QQ.frac_field(U))


def _identity_zero(expression: sp.Expr, parameter: sp.Expr) -> bool:
    if parameter == U:
        return equal_mod_parameter(expression)
    return sp.expand(expression) == 0


def _polynomial_equal(
    left: sp.Expr, right: sp.Expr, variable: sp.Symbol, parameter: sp.Expr
) -> bool:
    difference = sp.Poly(sp.expand(left - right), variable)
    return all(_identity_zero(coefficient, parameter) for coefficient in difference.all_coeffs())


def exact_period_decomposition(period: int, parameter: sp.Expr = U) -> dict[str, Any]:
    """Serialize an exact branch decomposition and independent identity checks.

    The decompositions are identities in the cyclic recurrence ideal.  They
    explicitly separate the lower-period diagonal rather than assigning an
    exact period from a numerical orbit search.
    """

    variables, recurrence = recurrence_equations(period, parameter)
    coefficient_field = "QQ[u]/P" if parameter == U else "QQ"
    payload: dict[str, Any] = {
        "period": period,
        "cyclic_recurrence_variables": [str(item) for item in variables],
        "cyclic_recurrence_equations": [sp.sstr(item) for item in recurrence],
        "formal_period_warning": "period dividing n until the explicit lower-period branch is removed",
    }

    if period == 1:
        x0 = variables[0]
        defining = sp.expand(x0**2 - 2 * x0 - parameter)
        coordinates = [x0]
        matrix = monodromy(coordinates)
        direct_resultant = sp.resultant(defining, T - sp.trace(matrix), x0)
        payload.update(
            {
                "lower_periods": [],
                "exact_branch_ideals": [[sp.sstr(defining)]],
                "exact_point_count": 2,
                "exact_cycle_count": 2,
                "groebner_basis": _groebner_strings([defining], [x0]),
                "trace_formula": sp.sstr(sp.trace(matrix)),
                "trace_elimination": polynomial_record(
                    trace_polynomial(1, parameter), T, coefficient_field=coefficient_field
                ),
                "independent_trace_resultant": sp.sstr(sp.expand(direct_resultant)),
                "trace_resultant_matches": _polynomial_equal(
                    _monic_squarefree(direct_resultant, T).as_expr(),
                    trace_polynomial(1, parameter).as_expr(),
                    T,
                    parameter,
                ),
                "determinant": sp.sstr(matrix.det()),
                "cyclic_trace_check": True,
                "period_separation": "n=1 has no positive lower period",
            }
        )

    elif period == 2:
        x0, x1 = variables
        exact_branch = [x0 + x1 + 2, x0**2 + 2 * x0 + 4 - parameter]
        lower_branch = [x0 - x1, x0**2 - 2 * x0 - parameter]
        substituted = {x1: -2 - x0}
        exact_coordinates = [x0, substituted[x1]]
        matrix = monodromy(exact_coordinates)
        shifted = monodromy(cyclic_shift(exact_coordinates))
        defining = exact_branch[1]
        checks = [
            sp.rem(sp.Poly(item.subs(substituted), x0), sp.Poly(defining, x0)).as_expr()
            for item in recurrence
        ]
        separation_value = sp.expand(3 - parameter)
        direct_resultant = sp.resultant(defining, T - sp.trace(matrix), x0)
        payload.update(
            {
                "difference_factorization": [
                    "(x0-x1)*(x0+x1+2)=0",
                    "the diagonal factor is the fixed-point branch",
                ],
                "lower_periods": [1],
                "lower_period_branch_ideal": [sp.sstr(item) for item in lower_branch],
                "exact_branch_ideals": [[sp.sstr(item) for item in exact_branch]],
                "exact_point_count": 2,
                "exact_cycle_count": 1,
                "groebner_basis": _groebner_strings(exact_branch, [x1, x0]),
                "full_cyclic_groebner_basis": _groebner_strings(recurrence, [x1, x0]),
                "recurrence_remainders_on_exact_branch": [sp.sstr(item) for item in checks],
                "trace_formula_on_branch": sp.sstr(sp.rem(sp.Poly(sp.trace(matrix), x0), sp.Poly(defining, x0)).as_expr()),
                "trace_elimination": polynomial_record(
                    trace_polynomial(2, parameter), T, coefficient_field=coefficient_field
                ),
                "independent_trace_resultant_with_phase_multiplicity": sp.sstr(
                    sp.expand(direct_resultant)
                ),
                "trace_resultant_squarefree_matches": _polynomial_equal(
                    _monic_squarefree(direct_resultant, T).as_expr(),
                    trace_polynomial(2, parameter).as_expr(),
                    T,
                    parameter,
                ),
                "determinant_remainder": sp.sstr(
                    sp.rem(sp.Poly(matrix.det() - 1, x0), sp.Poly(defining, x0)).as_expr()
                ),
                "cyclic_trace_difference_remainder": sp.sstr(
                    sp.rem(
                        sp.Poly(sp.trace(matrix) - sp.trace(shifted), x0),
                        sp.Poly(defining, x0),
                    ).as_expr()
                ),
                "period_separation_resultant": sp.sstr(separation_value),
                "period_separation_pass": not _identity_zero(separation_value, parameter),
            }
        )

    elif period == 3:
        x0, x1, x2 = variables
        b = sp.Symbol("b")
        defining = b**2 - parameter + 1
        branch_coordinates = [
            [b, b, -1 - b],
            [-1 - b, b, b],
            [b, -1 - b, b],
        ]
        branch_ideals = [
            [x0 - b, x1 - b, x2 + 1 + b, defining],
            [x0 + 1 + b, x1 - b, x2 - b, defining],
            [x0 - b, x1 + 1 + b, x2 - b, defining],
        ]
        all_remainders: list[list[str]] = []
        traces: list[sp.Expr] = []
        determinants: list[str] = []
        for coordinates in branch_coordinates:
            substitution = dict(zip(variables, coordinates, strict=True))
            remainders = [
                sp.rem(sp.Poly(item.subs(substitution), b), sp.Poly(defining, b)).as_expr()
                for item in recurrence
            ]
            all_remainders.append([sp.sstr(value) for value in remainders])
            matrix = monodromy(coordinates)
            traces.append(
                sp.rem(sp.Poly(sp.trace(matrix), b), sp.Poly(defining, b)).as_expr()
            )
            determinants.append(
                sp.sstr(
                    sp.rem(sp.Poly(matrix.det() - 1, b), sp.Poly(defining, b)).as_expr()
                )
            )
        cyclic_differences = [sp.expand(value - traces[0]) for value in traces[1:]]
        separation_value = sp.expand(4 * parameter - 5)
        direct_resultant = sp.resultant(defining, T - traces[0], b)
        payload.update(
            {
                "difference_factorization": [
                    "(x0-x1)*(x0+x1+1)=0",
                    "(x1-x2)*(x1+x2+1)=0",
                    "(x2-x0)*(x2+x0+1)=0",
                ],
                "lower_periods": [1],
                "lower_period_branch_ideal": [
                    "x0-x1",
                    "x1-x2",
                    sp.sstr(x0**2 - 2 * x0 - parameter),
                ],
                "exact_branch_ideals_with_auxiliary_b": [
                    [sp.sstr(item) for item in branch] for branch in branch_ideals
                ],
                "full_cyclic_groebner_basis": _groebner_strings(
                    recurrence, [x2, x1, x0]
                ),
                "exact_point_count": 6,
                "exact_cycle_count": 2,
                "auxiliary_equation": sp.sstr(defining),
                "recurrence_remainders_on_exact_branches": all_remainders,
                "trace_formulas_after_reduction": [sp.sstr(item) for item in traces],
                "trace_elimination": polynomial_record(
                    trace_polynomial(3, parameter), T, coefficient_field=coefficient_field
                ),
                "independent_trace_resultant": sp.sstr(sp.expand(direct_resultant)),
                "trace_resultant_matches": _polynomial_equal(
                    _monic_squarefree(direct_resultant, T).as_expr(),
                    trace_polynomial(3, parameter).as_expr(),
                    T,
                    parameter,
                ),
                "determinant_remainders": determinants,
                "cyclic_trace_difference_remainders": [sp.sstr(item) for item in cyclic_differences],
                "period_separation_resultant": sp.sstr(separation_value),
                "period_separation_pass": not _identity_zero(separation_value, parameter),
            }
        )
    else:
        raise ValueError("the source lock permits only periods 1, 2, and 3")

    multiplier = multiplier_polynomial(period, parameter)
    payload["multiplier_polynomial"] = polynomial_record(
        multiplier, L, coefficient_field=coefficient_field
    )
    payload["unit_certificate"] = {
        "monic": multiplier.LC() == 1,
        "constant_term": sp.sstr(multiplier.TC()),
        "reciprocal_polynomial": sp.expand(
            L ** multiplier.degree() * multiplier.as_expr().subs(L, 1 / L) - multiplier.as_expr()
        )
        == 0,
        "conclusion": "every listed multiplier and its reciprocal are integral over the coefficient ring",
    }
    return payload


def candidate_period_record(period: int) -> dict[str, Any]:
    """Return the complete exact candidate audit record for one period."""

    decomposition = exact_period_decomposition(period, U)
    rational_poly = rational_multiplier_polynomial(period)
    decomposition["multiplier_polynomial_over_Q"] = polynomial_record(rational_poly, L)
    decomposition["galois_norm_certificate"] = {
        "monic": rational_poly.LC() == 1,
        "constant_term": str(rational_poly.TC()),
        "degree": rational_poly.degree(),
        "norm_of_each_irreducible_multiplier": "a rational unit (+/-1) because every irreducible factor is monic with constant +/-1",
    }
    factor_payload = []
    for factor, multiplicity in sp.factor_list(rational_poly)[1]:
        normalized = primitive_monic(factor)
        factor_payload.append(
            {
                "polynomial": polynomial_record(normalized, L),
                "multiplicity": multiplicity,
                "monic": normalized.LC() == 1,
                "constant_term": str(normalized.TC()),
                "algebraic_norm": str((-1) ** normalized.degree() * normalized.TC()),
            }
        )
    decomposition["irreducible_multiplier_factors_over_Q"] = factor_payload
    decomposition["galois_norm_certificate"]["all_irreducible_factor_norms_are_rational_units"] = all(
        item["monic"] and item["constant_term"] in {"-1", "1"}
        for item in factor_payload
    )
    decomposition["rational_multiplier_audit"] = rational_root_candidates(rational_poly)
    decomposition["parameter_coefficient_basis_audit"] = [
        parameter_basis(value) for value in multiplier_polynomial(period, U).all_coeffs()
    ]
    return decomposition
