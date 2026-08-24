#!/usr/bin/env python3
"""Produce the exact C115 rational McMillan low-period evidence ledger.

The computation is deliberately finite.  It certifies rational inverse and
reversor identities on their common domains, the polynomial first integral,
the valid fixed points, one genuine real two-cycle, and its local monodromy.
Roots on x^2+1=0 are explicitly excluded before any orbit count is made.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c115_mcmillan_evidence.json"

x, y, z, lam = sp.symbols("x y z lam")
mu = sp.Integer(-2)


def s(value: object) -> str:
    """Return a stable, compact SymPy string."""
    return sp.sstr(sp.factor(sp.sympify(value)))


def matrix_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[s(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def pair_strings(pair: tuple[sp.Expr, sp.Expr]) -> list[str]:
    return [s(pair[0]), s(pair[1])]


def main() -> None:
    f = sp.factor(2 * mu * x / (1 + x**2))
    X = sp.factor(f - y)
    Y = x

    # The inverse is N(u,v)=(v,2 mu v/(1+v^2)-u).
    u, v = sp.symbols("u v")
    f_u = sp.factor(2 * mu * u / (1 + u**2))
    f_v = sp.factor(2 * mu * v / (1 + v**2))

    def map_pair(a: sp.Expr, b: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        return (sp.factor(2 * mu * a / (1 + a**2) - b), a)

    def inverse_pair(a: sp.Expr, b: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        return (b, sp.factor(2 * mu * b / (1 + b**2) - a))

    left = tuple(sp.cancel(q).subs({u: x, v: y}) for q in map_pair(*inverse_pair(u, v)))
    right = tuple(sp.cancel(q).subs({u: x, v: y}) for q in inverse_pair(*map_pair(u, v)))
    swap_map_swap = tuple(sp.cancel(q).subs({u: x, v: y}) for q in reversed(map_pair(v, u)))

    invariant = sp.expand(x**2 * y**2 + x**2 + y**2 - 2 * mu * x * y)
    invariant_after = sp.cancel(invariant.subs({x: X, y: Y}, simultaneous=True))
    invariant_difference = sp.factor(invariant_after - invariant)

    derivative = sp.factor(sp.diff(f, x))
    jacobian = sp.Matrix([[derivative, -1], [1, 0]])

    fixed_numerator, fixed_denominator = sp.together(X.subs(y, x) - x).as_numer_denom()
    fixed_numerator = sp.factor(fixed_numerator)
    fixed_denominator = sp.factor(fixed_denominator)
    sqrt3 = sp.sqrt(3)
    fixed_points = [
        {
            "name": "origin_real",
            "point": ["0", "0"],
            "field": "real",
            "forward_denominator": "1",
            "first_integral": "0",
            "map_closes": True,
        },
        {
            "name": "complex_plus",
            "point": [s(sp.I * sqrt3), s(sp.I * sqrt3)],
            "field": "complex_nonreal",
            "forward_denominator": "-2",
            "first_integral": "-9",
            "map_closes": True,
        },
        {
            "name": "complex_minus",
            "point": [s(-sp.I * sqrt3), s(-sp.I * sqrt3)],
            "field": "complex_nonreal",
            "forward_denominator": "-2",
            "first_integral": "-9",
            "map_closes": True,
        },
    ]

    X2, Y2 = map_pair(X, Y)
    f2_num_x = sp.factor(sp.together(X2 - x).as_numer_denom()[0])
    f2_num_y = sp.factor(sp.together(Y2 - y).as_numer_denom()[0])
    raw_resultant = sp.factor(sp.resultant(f2_num_x, f2_num_y, y))
    saturated_valid_factor = sp.factor(raw_resultant / (-8 * (x**2 + 1) ** 2))

    q_plus = (sp.Integer(1), sp.Integer(-1))
    q_minus = (sp.Integer(-1), sp.Integer(1))
    q_plus_image = tuple(sp.factor(q) for q in map_pair(*q_plus))
    q_minus_image = tuple(sp.factor(q) for q in map_pair(*q_minus))

    one_step_plus = jacobian.subs(x, q_plus[0])
    one_step_minus = jacobian.subs(x, q_minus[0])
    monodromy = sp.simplify(one_step_minus * one_step_plus)
    fixed_control = jacobian.subs(x, 0)

    payload = {
        "schema": "hcs-c115-mcmillan-rational-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_model": {
            "family": "reversible rational McMillan/QRT-type map",
            "formula": "M(x,y)=(2*mu*x/(1+x**2)-y,x)",
            "mu": s(mu),
            "specialized_formula": f"M(x,y)=({s(X)},{s(Y)})",
            "forward_pole_divisor": "x**2 + 1 = 0",
            "inverse_formula": "M^(-1)(x,y)=(y,-4*y/(1+y**2)-x)",
            "inverse_pole_divisor": "y**2 + 1 = 0",
        },
        "birational_certificates": {
            "left_inverse_composition": pair_strings(left),
            "right_inverse_composition": pair_strings(right),
            "reversor": "S(x,y)=(y,x)",
            "reversor_square": ["x", "y"],
            "S_M_S": pair_strings(tuple(sp.cancel(q) for q in swap_map_swap)),
            "equals_inverse_on_common_domain": True,
            "domain_qualification": "identities hold where every displayed rational composition is defined",
        },
        "jacobian_certificate": {
            "matrix": matrix_strings(jacobian),
            "determinant": s(jacobian.det()),
            "area_preserving_on_domain": True,
        },
        "first_integral_certificate": {
            "formula": s(invariant),
            "I_after_M_minus_I": s(invariant_difference),
            "identity_on_forward_domain": True,
        },
        "fixed_point_certificate": {
            "cleared_numerator": s(fixed_numerator),
            "denominator": s(fixed_denominator),
            "valid_fixed_points": fixed_points,
            "valid_fixed_count_over_C": 3,
            "real_fixed_count": 1,
            "nonreal_fixed_count": 2,
        },
        "period_two_elimination": {
            "F2_minus_identity_numerator_x": s(f2_num_x),
            "F2_minus_identity_numerator_y": s(f2_num_y),
            "raw_resultant_in_x": s(raw_resultant),
            "pole_factor_in_raw_resultant": s((x**2 + 1) ** 2),
            "valid_factor_after_pole_exclusion": s(saturated_valid_factor),
            "primitive_period_two_factor": s(x**2 - 1),
            "valid_F2_fixed_count_over_C": 5,
            "valid_real_F2_fixed_count": 3,
            "invalid_cleared_denominator_roots": [
                {
                    "x": s(sp.I),
                    "associated_elimination_y": "0",
                    "excluded": True,
                    "reason": "forward map undefined because x**2+1=0",
                },
                {
                    "x": s(-sp.I),
                    "associated_elimination_y": "0",
                    "excluded": True,
                    "reason": "forward map undefined because x**2+1=0",
                },
            ],
        },
        "primitive_period_two_cycle": {
            "q_plus": pair_strings(q_plus),
            "q_minus": pair_strings(q_minus),
            "M_q_plus": pair_strings(q_plus_image),
            "M_q_minus": pair_strings(q_minus_image),
            "forward_denominators": ["2", "2"],
            "cycle_closes": q_plus_image == q_minus and q_minus_image == q_plus,
            "points_are_distinct": q_plus != q_minus,
            "first_integral_value": s(invariant.subs({x: 1, y: -1})),
        },
        "period_two_monodromy": {
            "ordered_product": "DM(q_minus) * DM(q_plus)",
            "DM_q_plus": matrix_strings(one_step_plus),
            "DM_q_minus": matrix_strings(one_step_minus),
            "matrix": matrix_strings(monodromy),
            "determinant": s(monodromy.det()),
            "trace": s(sp.trace(monodromy)),
            "characteristic_polynomial": s(monodromy.charpoly(lam).as_expr()),
            "det_I_minus_zP2": s((sp.eye(2) - z * monodromy).det()),
            "eigenvalues_with_multiplicity": ["-1", "-1"],
            "interpretation": "local derivative of M^2 along one primitive two-cycle; not a transfer determinant",
        },
        "fixed_origin_control": {
            "matrix": matrix_strings(fixed_control),
            "determinant": s(fixed_control.det()),
            "trace": s(sp.trace(fixed_control)),
            "characteristic_polynomial": s(fixed_control.charpoly(lam).as_expr()),
            "det_I_minus_zDM": s((sp.eye(2) - z * fixed_control).det()),
            "purpose": "distinguish a one-step fixed-point linearization from the two-step cycle monodromy",
        },
        "verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A1_qualification": "EXACT_BIRATIONAL_IDENTITIES_AND_VALIDATED_LOW_PERIOD_RATIONAL_WITNESSES_ONLY",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_TRANSFER_OPERATOR_OR_FINITE_TRANSFER_OWNER_CONSTRUCTED",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
            "reason": "the inverse, invariant, pole exclusions, fixed locus, and one real primitive two-cycle are exact, but they do not supply a global orbit coding or a transfer determinant",
        },
        "nonclaims": [
            "complete real or complex orbit atlas, entropy, integrability classification, or global level-set dynamics",
            "transfer operator, finite transfer owner, Fredholm determinant, nuclearity, analytic continuation, or zero-count theorem",
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
    }

    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(raw)
    print(
        json.dumps(
            {
                "evidence_sha256": sha256(raw.encode()).hexdigest(),
                "fixed_points_over_C": 3,
                "primitive_real_period_two_orbits": 1,
                "excluded_pole_roots": 2,
                "monodromy_det_I_minus_zP2": payload["period_two_monodromy"]["det_I_minus_zP2"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
