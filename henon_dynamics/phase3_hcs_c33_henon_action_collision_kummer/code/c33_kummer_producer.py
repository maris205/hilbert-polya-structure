#!/usr/bin/env python3
"""Exact producer for the HCS-C33 Hénon action-node/Hill-Kummer gate.

All promoted algebra is reconstructed from the chronological Hénon map and
the frozen cyclic action.  The script uses exact SymPy arithmetic only; it
does not read the Phase-1 pilot coefficients as computational input.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import warnings
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning

warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


SCHEMA = "HCS-C33-PHASE3-KUMMER-1"
CANDIDATE = "HCS-C33_HENON_ACTION_COLLISION_KUMMER"
A, Q, P, C = sp.symbols("A q p c")
QQ = sp.QQ

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent.parent

SOURCE_PATHS = (
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/RESEARCH_QUESTION_BRIEF.md",
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/METHODOLOGY_BLUEPRINT.md",
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/PILOT_LEDGER.md",
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/DEVILS_ADVOCATE_CHECKPOINT1.md",
    "henon_dynamics/phase2_hcs_c33_henon_action_collision_kummer/SEARCH_STRATEGY.md",
    "henon_dynamics/phase2_hcs_c33_henon_action_collision_kummer/SOURCE_CORPUS_AND_ANNOTATED_BIBLIOGRAPHY.md",
    "henon_dynamics/phase2_hcs_c33_henon_action_collision_kummer/SOURCE_VERIFICATION_REPORT.md",
    "henon_dynamics/henon_frobenius_scheme_obstruction/code/c12a_producer.py",
    "henon_dynamics/phase3_hcs_c32_artin_schreier_quantum_trace/results/c32_morse_gate_certificate.json",
    "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def encode_rational(value: sp.Expr) -> dict[str, int]:
    value = sp.Rational(value)
    return {"numerator": int(value.p), "denominator": int(value.q)}


def encode_poly(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> dict[str, Any]:
    poly = sp.Poly(sp.expand(expr), *variables, domain=QQ)
    return {
        "variables": [str(variable) for variable in variables],
        "terms": [
            {
                "exponents": list(monomial),
                **encode_rational(coefficient),
            }
            for monomial, coefficient in poly.terms()
        ],
    }


def primitive_integer(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    numerator, _ = sp.fraction(sp.cancel(expr))
    poly = sp.Poly(sp.expand(numerator), *variables, domain=sp.ZZ)
    _, primitive = poly.primitive()
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive.as_expr()


def exact_integer(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    poly = sp.Poly(sp.expand(expr), *variables, domain=QQ)
    if any(sp.denom(coefficient) != 1 for coefficient in poly.coeffs()):
        raise AssertionError("expected integral polynomial coefficients")
    return poly.as_expr()


def derive_marker() -> tuple[sp.Expr, list[sp.Expr]]:
    x, y = Q, P
    for _ in range(5):
        x, y = sp.expand(1 - A * x**2 - y), x
    domain = QQ.frac_field(A)
    equation_5 = sp.Poly(sp.expand((x - Q).subs(P, Q)), Q, domain=domain)
    equation_4 = sp.Poly(sp.expand((y - Q).subs(P, Q)), Q, domain=domain)
    common = sp.monic(sp.gcd(equation_5, equation_4)).as_expr()
    fixed = A * Q**2 + 2 * Q - 1
    marker = primitive_integer(sp.cancel(common / fixed), (Q, A))

    coordinates: list[sp.Expr] = []
    previous = current = Q
    for _ in range(5):
        coordinates.append(current)
        previous, current = current, sp.expand(1 - A * current**2 - previous)
    return marker, coordinates


def derive_action(marker: sp.Expr, coordinates: list[sp.Expr]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    action = sum(
        coordinates[i] * coordinates[(i + 1) % 5]
        - coordinates[i]
        + A * coordinates[i] ** 3 / sp.Integer(3)
        for i in range(5)
    )
    domain = QQ.frac_field(A)
    remainder = sp.rem(
        sp.Poly(sp.together(3 * A**2 * action), Q, domain=domain),
        sp.Poly(marker, Q, domain=domain),
    ).as_expr()
    remainder = exact_integer(remainder, (Q, A))

    raw_resultant = sp.resultant(marker, 3 * A**2 * C - remainder, Q)
    raw_poly = sp.Poly(raw_resultant, C, domain=QQ[A])
    resultant_content, primitive = raw_poly.primitive()
    action_curve = primitive_integer(primitive.as_expr(), (C, A))
    return remainder, action_curve, sp.factor(resultant_content)


def derive_birational_inverse(marker: sp.Expr, remainder: sp.Expr, action_curve: sp.Expr) -> dict[str, Any]:
    subresultants = sp.subresultants(marker, 3 * A**2 * C - remainder, Q)
    linear = [item for item in subresultants if sp.degree(item, Q) == 1]
    if len(linear) != 1:
        raise AssertionError("normalization inverse subresultant is not linear")
    polynomial = sp.Poly(linear[0], Q, domain=QQ[A, C])
    coefficient_q = polynomial.nth(1)
    constant = polynomial.nth(0)
    gcd_with_curve = sp.gcd(
        sp.Poly(coefficient_q, C, domain=QQ.frac_field(A)),
        sp.Poly(action_curve, C, domain=QQ.frac_field(A)),
    )
    if gcd_with_curve.degree() != 0:
        raise AssertionError("inverse-subresultant coefficient is not generically invertible")
    return {
        "linear_subresultant_coefficient_q": encode_poly(coefficient_q, (C, A)),
        "linear_subresultant_constant": encode_poly(constant, (C, A)),
        "coefficient_q_coprime_to_W_over_QQ_A": True,
        "inverse_formula": "q=-V(A,c)/U(A,c)",
        "conclusion": "QQ(A,q)=QQ(A,c)",
    }


def factor_by_degree(factorization: tuple[sp.Expr, list[tuple[sp.Expr, int]]], degree: int, exponent: int) -> sp.Expr:
    matches = [
        primitive_integer(factor, (A,))
        for factor, power in factorization[1]
        if sp.degree(factor, A) == degree and power == exponent
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one degree-{degree}, exponent-{exponent} factor")
    return matches[0]


class QuotientRing:
    """Exact arithmetic in QQ[A]/(modulus), represented by SymPy Poly."""

    def __init__(self, modulus: sp.Expr):
        self.modulus = sp.Poly(modulus, A, domain=QQ)
        self.degree = self.modulus.degree()

    def reduce(self, value: sp.Expr | sp.Poly) -> sp.Poly:
        expr = value.as_expr() if isinstance(value, sp.Poly) else value
        return sp.Poly(sp.cancel(expr), A, domain=QQ).rem(self.modulus)

    def add(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.reduce(left.as_expr() + right.as_expr())

    def neg(self, value: sp.Poly) -> sp.Poly:
        return self.reduce(-value.as_expr())

    def mul(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.reduce(left.as_expr() * right.as_expr())

    def inverse(self, value: sp.Poly) -> sp.Poly:
        value = self.reduce(value)
        if value.is_zero:
            raise ZeroDivisionError("zero in quotient field")
        return sp.invert(value, self.modulus)

    def divide(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.mul(left, self.inverse(right))

    def encode(self, value: sp.Poly) -> dict[str, Any]:
        value = self.reduce(value)
        coefficients = value.all_coeffs()
        denominator = 1
        for coefficient in coefficients:
            denominator = sp.ilcm(denominator, int(sp.denom(coefficient)))
        numerators = [int(coefficient * denominator) for coefficient in reversed(coefficients)]
        numerators += [0] * (self.degree - len(numerators))
        divisor = abs(int(denominator))
        for numerator in numerators:
            divisor = math.gcd(divisor, abs(numerator))
        if divisor > 1:
            numerators = [numerator // divisor for numerator in numerators]
            denominator //= divisor
        if denominator < 0:
            denominator = -denominator
            numerators = [-numerator for numerator in numerators]
        return {
            "basis": [f"A^{index}" for index in range(self.degree)],
            "numerators_low_to_high": numerators,
            "denominator": int(denominator),
        }

    def evaluate_in_c(self, expr: sp.Expr, value: sp.Poly) -> sp.Poly:
        poly = sp.Poly(expr, C, domain=QQ[A])
        result = self.reduce(0)
        for index in range(poly.degree(), -1, -1):
            result = self.add(self.mul(result, value), self.reduce(poly.nth(index)))
        return result


def reduced_q_coefficients(expr: sp.Expr, ring: QuotientRing) -> list[sp.Poly]:
    poly = sp.Poly(expr, Q, domain=QQ[A])
    return [ring.reduce(poly.nth(index)) for index in range(poly.degree() + 1)]


def reduced_degree(coefficients: list[sp.Poly]) -> int:
    return max((index for index, value in enumerate(coefficients) if not value.is_zero), default=-1)


def trim_kpoly(coefficients: list[sp.Poly]) -> list[sp.Poly]:
    result = list(coefficients)
    while result and result[-1].is_zero:
        result.pop()
    return result


def divide_kpoly(
    dividend: list[sp.Poly],
    divisor: list[sp.Poly],
    ring: QuotientRing,
) -> tuple[list[sp.Poly], list[sp.Poly]]:
    remainder = trim_kpoly([ring.reduce(value) for value in dividend])
    divisor = trim_kpoly([ring.reduce(value) for value in divisor])
    if not divisor:
        raise ZeroDivisionError("zero quotient polynomial")
    quotient = [ring.reduce(0) for _ in range(max(0, len(remainder) - len(divisor) + 1))]
    inverse_lead = ring.inverse(divisor[-1])
    while len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        factor = ring.mul(remainder[-1], inverse_lead)
        quotient[shift] = factor
        for index, coefficient in enumerate(divisor):
            position = index + shift
            remainder[position] = ring.add(
                remainder[position], ring.neg(ring.mul(factor, coefficient))
            )
        remainder = trim_kpoly(remainder)
    return trim_kpoly(quotient), remainder


def gcd_kpoly(
    left: list[sp.Poly],
    right: list[sp.Poly],
    ring: QuotientRing,
) -> list[sp.Poly]:
    left = trim_kpoly(left)
    right = trim_kpoly(right)
    while right:
        _, remainder = divide_kpoly(left, right, ring)
        left, right = right, remainder
    if not left:
        return []
    inverse_lead = ring.inverse(left[-1])
    return [ring.mul(value, inverse_lead) for value in left]


def multiply_quadratic_elements(
    left: tuple[sp.Poly, sp.Poly],
    right: tuple[sp.Poly, sp.Poly],
    quadratic: list[sp.Poly],
    ring: QuotientRing,
) -> tuple[sp.Poly, sp.Poly]:
    a, b = left
    c, d = right
    bd = ring.mul(b, d)
    constant = ring.add(ring.mul(a, c), ring.neg(ring.mul(bd, quadratic[0])))
    linear = ring.add(
        ring.add(ring.mul(a, d), ring.mul(b, c)),
        ring.neg(ring.mul(bd, quadratic[1])),
    )
    return constant, linear


def inverse_quadratic_element(
    value: tuple[sp.Poly, sp.Poly],
    quadratic: list[sp.Poly],
    ring: QuotientRing,
) -> tuple[tuple[sp.Poly, sp.Poly], sp.Poly]:
    a, b = value
    norm = ring.add(
        ring.add(ring.mul(a, a), ring.neg(ring.mul(quadratic[1], ring.mul(a, b)))),
        ring.mul(quadratic[0], ring.mul(b, b)),
    )
    inverse_norm = ring.inverse(norm)
    conjugate = (
        ring.add(a, ring.neg(ring.mul(b, quadratic[1]))),
        ring.neg(b),
    )
    return (
        ring.mul(conjugate[0], inverse_norm),
        ring.mul(conjugate[1], inverse_norm),
    ), norm


def derive_node_data(
    marker: sp.Expr,
    remainder: sp.Expr,
    action_curve: sp.Expr,
    p9: sp.Expr,
) -> tuple[dict[str, Any], QuotientRing, sp.Poly, list[sp.Poly]]:
    ring = QuotientRing(p9)

    c_subresultants = sp.subresultants(action_curve, sp.diff(action_curve, C), C)
    linear = [item for item in c_subresultants if sp.degree(item, C) == 1]
    if len(linear) != 1:
        raise AssertionError("action singular value was not uniquely recovered")
    linear_poly = sp.Poly(linear[0], C, domain=QQ[A])
    c0 = ring.divide(ring.neg(ring.reduce(linear_poly.nth(0))), ring.reduce(linear_poly.nth(1)))

    branch_equation = sp.expand(3 * A**2 * c0.as_expr() - remainder)
    q_subresultants = sp.subresultants(marker, branch_equation, Q)
    quadratic: list[sp.Poly] | None = None
    reduced_tail_degrees: list[int] = []
    for item in q_subresultants:
        coefficients = reduced_q_coefficients(item, ring)
        degree = reduced_degree(coefficients)
        reduced_tail_degrees.append(degree)
        if degree == 2:
            inverse_lead = ring.inverse(coefficients[2])
            quadratic = [ring.mul(coefficient, inverse_lead) for coefficient in coefficients[:2]]
            quadratic.append(ring.reduce(1))
    if quadratic is None:
        raise AssertionError("two-point branch fiber was not recovered")
    if reduced_tail_degrees[-2:] != [-1, -1]:
        raise AssertionError("branch gcd has degree larger than two")

    values = {
        name: ring.evaluate_in_c(expr, c0)
        for name, expr in (
            ("W", action_curve),
            ("W_A", sp.diff(action_curve, A)),
            ("W_c", sp.diff(action_curve, C)),
            ("W_AA", sp.diff(action_curve, A, 2)),
            ("W_Ac", sp.diff(action_curve, A, C)),
            ("W_cc", sp.diff(action_curve, C, 2)),
        )
    }
    tangent_discriminant = ring.add(
        ring.mul(values["W_Ac"], values["W_Ac"]),
        ring.neg(ring.mul(values["W_AA"], values["W_cc"])),
    )
    branch_discriminant = ring.add(
        ring.mul(quadratic[1], quadratic[1]),
        ring.neg(ring.mul(ring.reduce(4), quadratic[0])),
    )
    marker_coefficients = reduced_q_coefficients(marker, ring)
    quotient, marker_remainder = divide_kpoly(marker_coefficients, quadratic, ring)
    quotient_coprime = gcd_kpoly(quadratic, quotient, ring)

    if not all(values[key].is_zero for key in ("W", "W_A", "W_c")):
        raise AssertionError("action-image point is not singular")
    if marker_remainder or len(quotient_coprime) != 1:
        raise AssertionError("branch pair is not a reduced two-point normalization fiber")
    if values["W_cc"].is_zero or tangent_discriminant.is_zero or branch_discriminant.is_zero:
        raise AssertionError("ordinary-node certificate failed")

    g_a_coefficients = reduced_q_coefficients(sp.diff(marker, A), ring)
    g_q_coefficients = reduced_q_coefficients(sp.diff(marker, Q), ring)
    r_a_coefficients = reduced_q_coefficients(sp.diff(remainder, A), ring)
    r_q_coefficients = reduced_q_coefficients(sp.diff(remainder, Q), ring)

    def remainder_pair(coefficients: list[sp.Poly]) -> tuple[sp.Poly, sp.Poly]:
        polynomial = sum(coefficient.as_expr() * Q**index for index, coefficient in enumerate(coefficients))
        return quotient_polynomial_remainder(polynomial, quadratic, ring)

    g_a_pair = remainder_pair(g_a_coefficients)
    g_q_pair = remainder_pair(g_q_coefficients)
    r_a_pair = remainder_pair(r_a_coefficients)
    r_q_pair = remainder_pair(r_q_coefficients)
    r_pair = quotient_polynomial_remainder(remainder, quadratic, ring)
    alpha = ring.reduce(A)
    alpha_squared = ring.mul(alpha, alpha)
    alpha_cubed = ring.mul(alpha_squared, alpha)
    two_r = (ring.mul(ring.reduce(2), r_pair[0]), ring.mul(ring.reduce(2), r_pair[1]))
    a_ra = (ring.mul(alpha, r_a_pair[0]), ring.mul(alpha, r_a_pair[1]))
    a_rq = (ring.mul(alpha, r_q_pair[0]), ring.mul(alpha, r_q_pair[1]))
    numerator_left = (ring.add(a_ra[0], ring.neg(two_r[0])), ring.add(a_ra[1], ring.neg(two_r[1])))
    numerator = multiply_quadratic_elements(numerator_left, g_q_pair, quadratic, ring)
    correction = multiply_quadratic_elements(a_rq, g_a_pair, quadratic, ring)
    numerator = (
        ring.add(numerator[0], ring.neg(correction[0])),
        ring.add(numerator[1], ring.neg(correction[1])),
    )
    denominator = (
        ring.mul(ring.mul(ring.reduce(3), alpha_cubed), g_q_pair[0]),
        ring.mul(ring.mul(ring.reduce(3), alpha_cubed), g_q_pair[1]),
    )
    inverse_denominator, denominator_norm = inverse_quadratic_element(denominator, quadratic, ring)
    slope = multiply_quadratic_elements(numerator, inverse_denominator, quadratic, ring)
    slope_difference_square = ring.mul(ring.mul(slope[1], slope[1]), branch_discriminant)
    if denominator_norm.is_zero or slope[1].is_zero or slope_difference_square.is_zero:
        raise AssertionError("normalization-branch tangent separation failed")

    node = {
        "collision_field": "K9=QQ[A]/(P9)",
        "double_action_value_c0": ring.encode(c0),
        "branch_pair_polynomial": {
            "variable": "q",
            "coefficients_low_to_high": [ring.encode(value) for value in quadratic],
        },
        "branch_pair_discriminant": ring.encode(branch_discriminant),
        "branch_pair_divides_marker": not marker_remainder,
        "branch_pair_coprime_to_marker_quotient": len(quotient_coprime) == 1,
        "action_image_derivatives": {key: ring.encode(value) for key, value in values.items()},
        "tangent_cone_discriminant_WAc_squared_minus_WAA_Wcc": ring.encode(tangent_discriminant),
        "normalization_branch_slope": {
            "formula": "((A*R_A-2*R)*G_q-A*R_q*G_Aparam)/(3*A^3*G_q)",
            "constant": ring.encode(slope[0]),
            "linear_q": ring.encode(slope[1]),
            "denominator_norm": ring.encode(denominator_norm),
            "slope_difference_square": ring.encode(slope_difference_square),
        },
        "zero_gates": {key: values[key].is_zero for key in ("W", "W_A", "W_c")},
        "nonzero_gates": {
            "W_cc": not values["W_cc"].is_zero,
            "tangent_cone_discriminant": not tangent_discriminant.is_zero,
            "branch_pair_discriminant": not branch_discriminant.is_zero,
            "normalization_slope_linear_coefficient": not slope[1].is_zero,
            "normalization_slope_difference_square": not slope_difference_square.is_zero,
        },
        "conclusion": "TWO_DISTINCT_NORMALIZATION_POINTS_WITH_TRANSVERSE_ORDINARY_ACTION_IMAGE_NODE",
    }
    return node, ring, c0, quadratic


def derive_hill(marker: sp.Expr, coordinates: list[sp.Expr]) -> tuple[sp.Expr, dict[str, Any]]:
    monodromy = sp.eye(2)
    for coordinate in coordinates:
        derivative = sp.Matrix([[-2 * A * coordinate, -1], [1, 0]])
        monodromy = derivative * monodromy
    domain = QQ.frac_field(A)
    hill = sp.rem(
        sp.Poly(sp.expand((sp.eye(2) - monodromy).det()), Q, domain=domain),
        sp.Poly(marker, Q, domain=domain),
    ).as_expr()
    hill = exact_integer(hill, (Q, A))

    action_hessian = sp.zeros(5)
    for index, coordinate in enumerate(coordinates):
        action_hessian[index, index] = 2 * A * coordinate
        action_hessian[index, (index + 1) % 5] += 1
        action_hessian[(index + 1) % 5, index] += 1
    hessian_det = sp.rem(
        sp.Poly(sp.expand(action_hessian.det()), Q, domain=domain),
        sp.Poly(marker, Q, domain=domain),
    ).as_expr()
    hill_identity = sp.expand(hessian_det - hill) == 0
    if not hill_identity:
        raise AssertionError("period-five Hill identity failed")

    fixed = A * Q**2 + 2 * Q - 1
    fixed_resultant = sp.factor(sp.resultant(marker, fixed, Q))
    plus_resultant = sp.factor(sp.resultant(marker, hill, Q))
    minus_resultant = sp.factor(sp.resultant(marker, 4 - hill, Q))
    data = {
        "chronology": "DH_A^5=D_4*D_3*D_2*D_1*D_0, later factors on the left",
        "hill_polynomial_det_I_minus_DH5": encode_poly(hill, (Q, A)),
        "cyclic_action_hessian_equals_hill": hill_identity,
        "fixed_point_collision_resultant": encode_poly(fixed_resultant, (A,)),
        "multiplier_plus_one_resultant": encode_poly(plus_resultant, (A,)),
        "multiplier_minus_one_resultant_det_I_plus_DH5": encode_poly(minus_resultant, (A,)),
        "identity_det_I_plus_M_equals_4_minus_det_I_minus_M": True,
    }
    return hill, data


def quotient_polynomial_remainder(
    polynomial: sp.Expr,
    quadratic: list[sp.Poly],
    ring: QuotientRing,
) -> tuple[sp.Poly, sp.Poly]:
    poly = sp.Poly(polynomial, Q, domain=QQ[A])
    constant = ring.reduce(0)
    linear = ring.reduce(0)
    power_constant = ring.reduce(1)
    power_linear = ring.reduce(0)
    for exponent in range(poly.degree() + 1):
        coefficient = ring.reduce(poly.nth(exponent))
        constant = ring.add(constant, ring.mul(coefficient, power_constant))
        linear = ring.add(linear, ring.mul(coefficient, power_linear))
        power_constant, power_linear = (
            ring.neg(ring.mul(power_linear, quadratic[0])),
            ring.add(power_constant, ring.neg(ring.mul(power_linear, quadratic[1]))),
        )
    return constant, linear


def derive_kummer(
    hill: sp.Expr,
    quadratic: list[sp.Poly],
    ring: QuotientRing,
    p9: sp.Expr,
) -> dict[str, Any]:
    constant, linear = quotient_polynomial_remainder(hill, quadratic, ring)
    norm = ring.add(
        ring.add(
            ring.mul(constant, constant),
            ring.neg(ring.mul(quadratic[1], ring.mul(linear, constant))),
        ),
        ring.mul(quadratic[0], ring.mul(linear, linear)),
    )
    encoded_norm = ring.encode(norm)
    numerator_poly = sp.Poly(
        sum(
            sp.Integer(value) * A**index
            for index, value in enumerate(encoded_norm["numerators_low_to_high"])
        ),
        A,
        domain=sp.ZZ,
    )
    scalar = sp.Rational(1, encoded_norm["denominator"])
    p9_poly = sp.Poly(p9, A, domain=sp.ZZ)
    field_norm = sp.factor(
        scalar**9
        * sp.Rational(
            sp.resultant(p9_poly.as_expr(), numerator_poly.as_expr(), A),
            p9_poly.LC() ** numerator_poly.degree(),
        )
    )
    numerator_factors = {str(prime): exponent for prime, exponent in sp.factorint(abs(sp.numer(field_norm))).items()}
    denominator_factors = {str(prime): exponent for prime, exponent in sp.factorint(sp.denom(field_norm)).items()}
    odd_valuations = {
        prime: exponent
        for prime, exponent in {**numerator_factors, **{key: -value for key, value in denominator_factors.items()}}.items()
        if exponent % 2
    }
    if not odd_valuations:
        raise AssertionError("field norm did not prove nonsquareness")
    return {
        "hill_remainder_mod_branch_pair": {
            "constant": ring.encode(constant),
            "linear_q": ring.encode(linear),
        },
        "symmetric_branch_norm_NH": encoded_norm,
        "field_norm": encode_rational(field_norm),
        "field_norm_factorization": {
            "numerator": numerator_factors,
            "denominator": denominator_factors,
            "odd_valuations": odd_valuations,
        },
        "branch_exchange_invariant": True,
        "square_class_identity": "[h/sigma(h)]=[h*sigma(h)] in E^x/E^(x2) because (h/sigma(h))/(h*sigma(h))=sigma(h)^(-2)",
        "common_hill_normalization": "h_i -> mu(A)*h_i multiplies N_H by mu(A)^2",
        "action_gauge": {
            "parameter_constant": "c -> c+5*kappa(A); equal-action locus unchanged",
            "cyclic_coboundary": "sum_i(F(x_(i+1))-F(x_i))=0 on every closed orbit",
            "common_nonzero_rescaling": "c -> lambda(A)*c is a local coordinate change where lambda!=0",
            "hill_intrinsic": "det(I-DH_A^5) is unchanged by action-coordinate gauges",
        },
        "conclusion": "NONTRIVIAL_QUADRATIC_KUMMER_CLASS_OVER_K9",
    }


def factor_degrees_mod(poly: sp.Expr, prime: int) -> tuple[list[int], list[dict[str, Any]]]:
    factors = sp.factor_list(sp.Poly(poly, A, modulus=prime))[1]
    encoded: list[dict[str, Any]] = []
    degrees: list[int] = []
    for factor, exponent in factors:
        monic = factor.monic()
        coefficients = [int(coefficient) % prime for coefficient in monic.all_coeffs()]
        encoded.append({"coefficients_high_to_low": coefficients, "exponent": int(exponent)})
        degrees.extend([monic.degree()] * int(exponent))
    encoded.sort(key=lambda item: (len(item["coefficients_high_to_low"]), item["coefficients_high_to_low"]))
    return sorted(degrees, reverse=True), encoded


def legendre(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    return 1 if pow(value, (prime - 1) // 2, prime) == 1 else -1


def evaluate_mod(expr: sp.Expr, parameter: int, coordinate: int, prime: int) -> int:
    return int(expr.subs({A: parameter, Q: coordinate})) % prime


def state_step(state: tuple[int, int], parameter: int, prime: int) -> tuple[int, int]:
    q_value, previous = state
    return ((1 - parameter * q_value * q_value - previous) % prime, q_value)


def least_period(state: tuple[int, int], parameter: int, prime: int, limit: int = 5) -> int | None:
    current = state
    for period in range(1, limit + 1):
        current = state_step(current, parameter, prime)
        if current == state:
            return period
    return None


def finite_controls(marker: sp.Expr, remainder: sp.Expr, hill: sp.Expr, p9: sp.Expr) -> dict[str, Any]:
    value = int(sp.Poly(p9, A, domain=sp.ZZ).eval(6))
    factorization = sp.factorint(value)
    expected_primes = [61, 157, 3203, 21943]
    if sorted(factorization) != expected_primes or any(power != 1 for power in factorization.values()):
        raise AssertionError("structurally selected prime ledger changed")
    labels = {
        61: "POST_HOC_C32_REGRESSION",
        157: "STRUCTURAL_SQUARE_CONTROL",
        3203: "ADVERSARIAL_NONSQUARE_CONTROL",
        21943: "STRUCTURAL_SQUARE_CONTROL",
    }
    rows: list[dict[str, Any]] = []
    for prime in expected_primes:
        roots = [value for value in range(prime) if evaluate_mod(marker, 6, value, prime) == 0]
        by_action: dict[int, list[dict[str, int]]] = {}
        for root in roots:
            action = evaluate_mod(remainder, 6, root, prime) * pow(3 * 6**2, -1, prime) % prime
            hill_value = evaluate_mod(hill, 6, root, prime)
            by_action.setdefault(action, []).append(
                {
                    "q": root,
                    "hill": hill_value,
                    "least_state_period": int(least_period((root, root), 6, prime) or 0),
                }
            )
        collisions = [(action, branches) for action, branches in by_action.items() if len(branches) == 2]
        if len(collisions) != 1:
            raise AssertionError(f"prime {prime} did not have one two-branch action collision")
        action, branches = collisions[0]
        branches.sort(key=lambda branch: branch["q"])
        if any(branch["least_state_period"] != 5 for branch in branches):
            raise AssertionError("finite control admitted lower period")
        h1, h2 = (branch["hill"] for branch in branches)
        nh = h1 * h2 % prime
        ratio = h1 * pow(h2, -1, prime) % prime
        rows.append(
            {
                "prime": prime,
                "selection_status": labels[prime],
                "all_marker_roots": roots,
                "common_action": action,
                "branches": branches,
                "hill_product": nh,
                "hill_ratio": ratio,
                "hill_product_character": legendre(nh, prime),
                "hill_ratio_character": legendre(ratio, prime),
                "multiplier_plus_one_excluded": all(h not in (0,) for h in (h1, h2)),
                "multiplier_minus_one_excluded": all((4 - h) % prime != 0 for h in (h1, h2)),
            }
        )
    return {
        "selection_rule": "all prime divisors of P9(6), frozen before Phase 3",
        "P9_at_6": value,
        "factorization": {str(prime): int(power) for prime, power in factorization.items()},
        "rows": rows,
    }


def build_payload() -> dict[str, Any]:
    marker, coordinates = derive_marker()
    remainder, action_curve, resultant_content = derive_action(marker, coordinates)
    birational_inverse = derive_birational_inverse(marker, remainder, action_curve)
    irreducibility_rows: list[dict[str, Any]] = []
    for name, expression, variable in (
        ("G_at_A6", marker.subs(A, 6), Q),
        ("W_at_A6", action_curve.subs(A, 6), C),
    ):
        polynomial = sp.Poly(expression, variable, modulus=37)
        factors = sp.factor_list(polynomial)[1]
        factor_degrees = sorted(
            [factor.degree() for factor, exponent in factors for _ in range(exponent)],
            reverse=True,
        )
        if polynomial.degree() != 6 or factor_degrees != [6]:
            raise AssertionError(f"{name} is not an irreducible degree-six specialization")
        irreducibility_rows.append(
            {
                "polynomial": name,
                "variable": str(variable),
                "degree": polynomial.degree(),
                "coefficients_high_to_low_mod_p": [
                    int(coefficient) % 37 for coefficient in polynomial.all_coeffs()
                ],
                "factor_degrees": factor_degrees,
                "irreducible": True,
            }
        )

    marker_disc_factorization = sp.factor_list(sp.discriminant(marker, Q))
    action_disc_factorization = sp.factor_list(sp.discriminant(action_curve, C))
    p2 = factor_by_degree(action_disc_factorization, 2, 5)
    p5 = factor_by_degree(action_disc_factorization, 5, 3)
    p9 = factor_by_degree(action_disc_factorization, 9, 2)
    if sp.rem(sp.Poly(p9, A), sp.Poly(p2 * p5, A)).is_zero:
        raise AssertionError("invalid collision-factor coprimality test")
    if sp.gcd(sp.Poly(p9, A), sp.Poly(p2 * p5, A)).degree() != 0:
        raise AssertionError("P9 intersects old ramification identically")

    node, ring, _, quadratic = derive_node_data(marker, remainder, action_curve, p9)
    hill, hill_data = derive_hill(marker, coordinates)
    kummer = derive_kummer(hill, quadratic, ring, p9)

    p9_poly = sp.Poly(p9, A, domain=sp.ZZ)
    p9_discriminant = int(sp.discriminant(p9, A))
    modular_rows = []
    for prime in (7, 17, 23):
        degrees, factors = factor_degrees_mod(p9, prime)
        modular_rows.append(
            {
                "prime": prime,
                "unramified": p9_discriminant % prime != 0 and int(p9_poly.LC()) % prime != 0,
                "factor_degrees": degrees,
                "monic_factors": factors,
            }
        )
    if [row["factor_degrees"] for row in modular_rows] != [[9], [5, 2, 1, 1], [8, 1]]:
        raise AssertionError("P9 modular cycle-type certificate changed")

    source_lock = {
        relative: sha256_file(REPO / relative)
        for relative in SOURCE_PATHS
    }

    marker_factor_list = sp.factor_list(sp.discriminant(marker, Q))
    action_factor_list = sp.factor_list(sp.discriminant(action_curve, C))
    payload = {
        "material_passport": {
            "candidate_id": CANDIDATE,
            "phase": 3,
            "date_utc": "2026-08-12",
            "ai_assistance_disclosed": True,
            "evidence_mode": "exact symbolic computation plus theorem audit",
        },
        "source_lock": source_lock,
        "conventions": {
            "map": "H_A(q,p)=(1-A*q^2-p,q)",
            "reversor_line": "p=q",
            "chronological_recurrence": "x_(i+1)=1-A*x_i^2-x_(i-1)",
            "cyclic_action": "Phi_5A=sum_i(x_i*x_(i+1)-x_i+(A/3)*x_i^3)",
            "action_coordinate": "c=Phi_5A; elimination uses 3*A^2*c-R_A(q)",
            "hill_value": "h_A(q)=det(I-DH_A^5), chronological later factors on the left",
        },
        "derived_polynomials": {
            "exact_period_five_marker_G": encode_poly(marker, (Q, A)),
            "reduced_action_numerator_R": encode_poly(remainder, (Q, A)),
            "action_curve_W": encode_poly(action_curve, (C, A)),
            "raw_resultant_content_removed": encode_poly(resultant_content, (A,)),
            "marker_discriminant": encode_poly(sp.factor(sp.discriminant(marker, Q)), (A,)),
            "action_curve_discriminant": encode_poly(sp.factor(sp.discriminant(action_curve, C)), (A,)),
            "P2": encode_poly(p2, (A,)),
            "P5": encode_poly(p5, (A,)),
            "P9": encode_poly(p9, (A,)),
            "marker_discriminant_factor_degrees_and_powers": [
                [int(sp.degree(factor, A)), int(power)] for factor, power in marker_factor_list[1]
            ],
            "action_discriminant_factor_degrees_and_powers": [
                [int(sp.degree(factor, A)), int(power)] for factor, power in action_factor_list[1]
            ],
            "P9_coprime_to_P2P5": sp.gcd(sp.Poly(p9, A), sp.Poly(p2 * p5, A)).degree() == 0,
            "normalization_birational_inverse": birational_inverse,
            "generic_irreducibility_certificate": {
                "parameter_value": 6,
                "prime": 37,
                "rows": irreducibility_rows,
                "degree_preserved": True,
                "conclusion": "G_and_W_irreducible_over_QQ(A)",
            },
        },
        "node_gate": node,
        "exact_period_and_nonparabolic_gate": {
            **hill_data,
            "P9_coprime_to_fixed_collision_resultant": sp.gcd(
                sp.Poly(p9, A), sp.Poly(sp.resultant(marker, A * Q**2 + 2 * Q - 1, Q), A)
            ).degree() == 0,
            "P9_coprime_to_multiplier_plus_one_resultant": sp.gcd(
                sp.Poly(p9, A), sp.Poly(sp.resultant(marker, hill, Q), A)
            ).degree() == 0,
            "P9_coprime_to_multiplier_minus_one_resultant": sp.gcd(
                sp.Poly(p9, A), sp.Poly(sp.resultant(marker, 4 - hill, Q), A)
            ).degree() == 0,
            "conclusion": "GENERIC_P9_BRANCHES_HAVE_EXACT_PERIOD_FIVE_AND_NO_MULTIPLIER_PLUS_OR_MINUS_ONE",
        },
        "collision_parameter_galois_gate": {
            "P9_primitive": int(sp.gcd_list(p9_poly.all_coeffs())) == 1,
            "P9_discriminant": p9_discriminant,
            "P9_discriminant_factorization": {
                str(prime): int(power) for prime, power in sp.factorint(abs(p9_discriminant)).items()
            },
            "modular_factorizations": modular_rows,
            "argument": [
                "degree-9 factor modulo 7 proves irreducibility and a 9-cycle",
                "type (8,1) modulo 23 plus transitivity gives 2-transitivity and primitivity",
                "squaring type (5,2,1,1) modulo 17 gives a pure 5-cycle",
                "Jordan gives A9; the 8-cycle is odd; hence S9",
            ],
            "conclusion": "Gal(P9/QQ)=S9",
        },
        "hill_kummer_gate": kummer,
        "finite_prime_controls": finite_controls(marker, remainder, hill, p9),
        "route_a_evaluation": {
            "testability": "NOT_TESTABLE_AS_ROUTE_A_DETERMINANT",
            "tuple_ceiling": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "reason": "one fixed-period arithmetic cover supplies neither an all-length clock nor a dynamical determinant",
            "route_b_invocation_allowed": False,
        },
        "decisions": {
            "phase3_exact_gate": "GO",
            "main_conclusion": "NONTRIVIAL_HENON_ACTION_IMAGE_NODE_HILL_KUMMER_CLASS",
            "normalization_cover_novelty": "REJECTED_PRIOR_WORK",
            "generic_maxwell_mechanism_novelty": "REJECTED_PRIOR_WORK",
            "full_wreath_group": "OPEN_NOT_CLAIMED",
            "picard_lefschetz": "OPEN_NOT_CLAIMED",
            "dynamical_zeta_or_HP": "NOT_CONSTRUCTED",
        },
        "scope": {
            "periods": [5],
            "family": "area-preserving Hénon H_A",
            "characteristic_zero_primary": True,
            "finite_primes_are_controls_not_primary_proof": True,
            "prime_61_is_post_hoc": True,
            "no_period_extension": True,
            "no_prime_or_zero_fitting": True,
            "no_full_wreath_claim": True,
            "no_picard_lefschetz_claim": True,
            "no_zeta_claim": True,
            "no_hilbert_polya_claim": True,
        },
    }
    return payload


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": sha256_bytes(canonical_json(payload).encode("utf-8")),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    print(f"payload_sha256={certificate['payload_sha256']}")


if __name__ == "__main__":
    main()
