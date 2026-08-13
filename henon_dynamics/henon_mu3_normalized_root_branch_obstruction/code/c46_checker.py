#!/usr/bin/env python3
"""Independent exact checker for the HCS-C46 p=7 branch obstruction.

The checker does not import the producer or SymPy.  It implements bivariate
integer polynomial arithmetic, cyclotomic reduction, a Sylvester determinant
for resultants, and finite-field Euclidean gcds from scratch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c46-certificate-v1"
P18_HIGH = (
    49, 147, 147, -14, -133, -63, 71, 104, 50, 13,
    50, 104, 71, -63, -133, -14, 147, 147, 49,
)
P12_HIGH = (7, 0, -21, 0, 35, 0, -41, 0, 35, 0, -21, 0, 7)
D0_ROWS = (
    (7, 0, 0, 0, 0, 0),
    (1, -2, -9, 1, 0, -5),
    (3, 2, -3, 2, 3, -7),
    (7, 0, 0, 0, 0, 0),
)
D1_ROWS = (
    (7, 0, 0, 0, 0, 0),
    (2, 4, 6, 1, 3, -2),
    (-7, 0, 0, 0, 0, 0),
)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


# z-polynomials are low-to-high lists of integers/Fractions.
def z_trim(poly: list[Any]) -> list[Any]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def z_add(left: list[Any], right: list[Any]) -> list[Any]:
    output = [0] * max(len(left), len(right))
    for index in range(len(output)):
        output[index] = (left[index] if index < len(left) else 0) + (
            right[index] if index < len(right) else 0
        )
    return z_trim(output)


def z_neg(poly: list[Any]) -> list[Any]:
    return [-value for value in poly]


def z_mul(left: list[Any], right: list[Any]) -> list[Any]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return z_trim(output)


def z_scale(poly: list[Any], scalar: Any) -> list[Any]:
    return z_trim([scalar * value for value in poly])


def z_equal(left: list[Any], right: list[Any]) -> bool:
    return z_trim(left[:]) == z_trim(right[:])


# X-polynomials have z-polynomial coefficients, low-to-high in X.
def x_reduce(poly: list[list[Any]]) -> list[list[Any]]:
    poly = [row[:] for row in poly]
    while len(poly) > 6:
        coefficient = poly[-1]
        degree = len(poly) - 1
        shift = degree - 6
        # X^6=-(1+X+...+X^5) modulo Phi_7.
        for index in range(6):
            poly[index + shift] = z_add(
                poly[index + shift], z_neg(coefficient)
            )
        poly.pop()
    while len(poly) < 6:
        poly.append([0])
    return poly


def x_mul(left: list[list[Any]], right: list[list[Any]]) -> list[list[Any]]:
    output = [[0] for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = z_add(output[i + j], z_mul(a, b))
    return x_reduce(output)


def rows_to_x_poly(rows: tuple[tuple[int, ...], ...]) -> list[list[int]]:
    # Input is z-degree outer, X-degree inner; transpose to X outer.
    return [
        [rows[z_degree][x_degree] for z_degree in range(len(rows))]
        for x_degree in range(6)
    ]


def conjugate_x(poly: list[list[Any]]) -> list[list[Any]]:
    # X^j -> X^(7-j), followed by Phi_7 reduction.
    maximum = 7
    output = [[0] for _ in range(maximum)]
    output[0] = poly[0][:]
    for exponent in range(1, 6):
        output[7 - exponent] = z_add(output[7 - exponent], poly[exponent])
    return x_reduce(output)


def theta_expression_to_x(theta_rows: list[list[int]]) -> list[list[int]]:
    # row entries [theta^2, theta, constant], z degree outer.
    theta = [[0], [1], [0], [0], [0], [0], [1]]  # X+X^6
    theta = x_reduce(theta)
    theta2 = x_mul(theta, theta)
    one = [[1], [0], [0], [0], [0], [0]]
    answer = [[0] for _ in range(6)]
    for z_degree, (a2, a1, a0) in enumerate(theta_rows):
        for x_degree in range(6):
            coefficient = a2 * theta2[x_degree][0] + a1 * theta[x_degree][0] + a0 * one[x_degree][0]
            if coefficient:
                term = [0] * z_degree + [coefficient]
                answer[x_degree] = z_add(answer[x_degree], term)
    return answer


def determinant(matrix: list[list[list[Fraction]]]) -> list[Fraction]:
    """Fraction-free in spirit, exact Gaussian determinant over Q(z)'s field.

    Rather than implement rational functions, the C46 resultant has a cubic
    first polynomial.  We use the identity Res(m,q)=det(multiplication by q)
    on Q(z)[theta]/m and build the 3x3 multiplication matrix directly.
    This function is the ordinary 3x3 determinant in the polynomial ring.
    """
    require(len(matrix) == 3 and all(len(row) == 3 for row in matrix), "determinant shape")
    a = matrix
    positive = z_add(
        z_mul(a[0][0], z_mul(a[1][1], a[2][2])),
        z_add(
            z_mul(a[0][1], z_mul(a[1][2], a[2][0])),
            z_mul(a[0][2], z_mul(a[1][0], a[2][1])),
        ),
    )
    negative = z_add(
        z_mul(a[0][2], z_mul(a[1][1], a[2][0])),
        z_add(
            z_mul(a[0][1], z_mul(a[1][0], a[2][2])),
            z_mul(a[0][0], z_mul(a[1][2], a[2][1])),
        ),
    )
    return z_add(positive, z_neg(negative))


def theta_reduce(coefficients: list[list[Fraction]]) -> list[list[Fraction]]:
    coefficients = [row[:] for row in coefficients]
    while len(coefficients) > 3:
        value = coefficients[-1]
        degree = len(coefficients) - 1
        shift = degree - 3
        # theta^3=-theta^2+2theta+1.
        coefficients[shift] = z_add(coefficients[shift], value)
        coefficients[shift + 1] = z_add(coefficients[shift + 1], z_scale(value, 2))
        coefficients[shift + 2] = z_add(coefficients[shift + 2], z_neg(value))
        coefficients.pop()
    while len(coefficients) < 3:
        coefficients.append([Fraction(0)])
    return coefficients


def resultant_from_theta_rows(rows: list[list[int]], common_denominator: int) -> list[Fraction]:
    # q=a0+a1 theta+a2 theta^2, including common denominator.
    q = [[Fraction(0)] for _ in range(3)]
    for z_degree, (a2, a1, a0) in enumerate(rows):
        monomial = [Fraction(0)] * z_degree + [Fraction(1, common_denominator)]
        q[0] = z_add(q[0], z_scale(monomial, a0))
        q[1] = z_add(q[1], z_scale(monomial, a1))
        q[2] = z_add(q[2], z_scale(monomial, a2))
    columns: list[list[list[Fraction]]] = []
    for power in range(3):
        shifted = [[Fraction(0)] for _ in range(power)] + [row[:] for row in q]
        columns.append(theta_reduce(shifted))
    matrix = [[columns[column][row] for column in range(3)] for row in range(3)]
    return determinant(matrix)


def finite_poly_trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def finite_derivative(poly: list[int], modulus: int) -> list[int]:
    return finite_poly_trim([index * poly[index] % modulus for index in range(1, len(poly))])


def finite_divmod(left: list[int], right: list[int], modulus: int) -> tuple[list[int], list[int]]:
    left = finite_poly_trim([value % modulus for value in left])
    right = finite_poly_trim([value % modulus for value in right])
    require(right != [0], "division by zero polynomial")
    if len(left) < len(right):
        return [0], left
    quotient = [0] * (len(left) - len(right) + 1)
    inverse = pow(right[-1], -1, modulus)
    while left != [0] and len(left) >= len(right):
        shift = len(left) - len(right)
        coefficient = left[-1] * inverse % modulus
        quotient[shift] = coefficient
        for index, value in enumerate(right):
            left[index + shift] = (left[index + shift] - coefficient * value) % modulus
        left = finite_poly_trim(left)
    return finite_poly_trim(quotient), left


def finite_gcd(left: list[int], right: list[int], modulus: int) -> list[int]:
    while right != [0]:
        _, remainder = finite_divmod(left, right, modulus)
        left, right = right, remainder
    inverse = pow(left[-1], -1, modulus)
    return [value * inverse % modulus for value in left]


def expected_source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relatives = (
        "henon_mu3_augmented_euler_superproduct/results/c43_certificate.json",
        "henon_mu3_fixed_coefficient_field_obstruction/results/c44_certificate.json",
        "henon_mu3_galois_norm_rank_obstruction/results/c45_certificate.json",
    )
    return [
        {
            "path": f"henon_dynamics/{relative}",
            "sha256": sha256_file(henon_root / relative),
        }
        for relative in relatives
    ]


def expected_payload(project_root: Path) -> dict[str, Any]:
    q0_rows = [
        [0, 0, 7], [-15, -3, 31], [-26, -10, 61], [-26, -19, 72],
        [-26, -10, 61], [-15, -3, 31], [0, 0, 7],
    ]
    q1_rows = [[0, 0, 7], [0, 0, 0], [4, 5, -12], [0, 0, 0], [0, 0, 7]]
    res0 = resultant_from_theta_rows(q0_rows, 7)
    res1 = resultant_from_theta_rows(q1_rows, 7)
    expected_res0 = [Fraction(value, 49) for value in reversed(P18_HIGH)]
    expected_res1 = [Fraction(value, 7) for value in reversed(P12_HIGH)]
    require(z_equal(res0, expected_res0), "independent q0 resultant mismatch")
    require(z_equal(res1, expected_res1), "independent q1 resultant mismatch")

    modulus = 5
    p18 = [value % modulus for value in reversed(P18_HIGH)]
    p12 = [value % modulus for value in reversed(P12_HIGH)]
    gcd_cross = finite_gcd(p18[:], p12[:], modulus)
    gcd18 = finite_gcd(p18[:], finite_derivative(p18, modulus), modulus)
    gcd12 = finite_gcd(p12[:], finite_derivative(p12, modulus), modulus)
    require(gcd_cross == gcd18 == gcd12 == [1], "independent mod-5 gcd mismatch")

    return {
        "material_passport": {
            "candidate_id": "HCS-C46",
            "project": "henon_mu3_normalized_root_branch_obstruction",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact cyclotomic reduction, symbolic resultants, and good-prime gcd certificates; no zero-table data",
        },
        "source_lock": expected_source_lock(project_root),
        "p7_conventions": {
            "prime": 7,
            "rho_order_3": 2,
            "cyclotomic_variable": "X=zeta_7 with Phi_7(X)=1+X+...+X^6",
            "real_generator": "theta=X+X^(-1)",
            "real_field_degree_d7": 3,
            "sector_dimensions": [3, 2, 2],
            "local_variable": "z",
            "sector_determinants": "D_k(z)=det(I-z*T_(7,k))",
        },
        "exact_sector_polynomials": {
            "common_denominator": 7,
            "D0_numerator_X0_through_X5_by_z_low_to_high": [list(row) for row in D0_ROWS],
            "D1_numerator_X0_through_X5_by_z_low_to_high": [list(row) for row in D1_ROWS],
            "D2_equals_D1": True,
            "paired_q0": "q0=D0*conjugate(D0)",
            "paired_q1": "q1=D1*conjugate(D1)",
            "paired_factor_E": "E=(q0/q1)^2",
        },
        "resultant_and_norm_control": {
            "theta_minimal_polynomial_high_to_low": [1, 1, -2, -1],
            "q0_numerator_theta2_theta1_theta0_by_z_low_to_high": q0_rows,
            "q1_numerator_theta2_theta1_theta0_by_z_low_to_high": q1_rows,
            "raw_resultant_q0_numerator_content": 7,
            "raw_resultant_q1_numerator_content": 49,
            "P18_coefficients_high_to_low": list(P18_HIGH),
            "P12_coefficients_high_to_low": list(P12_HIGH),
            "norm_q0": "P18/49",
            "norm_q1": "P12/7",
            "ordinary_norm_E": "P18^2/(49*P12^2)",
            "ordinary_norm_at_zero": 1,
            "ordinary_norm_numerator_degree": 36,
            "ordinary_norm_denominator_degree": 24,
            "ordinary_norm_virtual_degree": 12,
        },
        "good_reduction_control": {
            "modulus": 5,
            "P18_coefficients_high_to_low_mod_5": [value % 5 for value in P18_HIGH],
            "P12_coefficients_high_to_low_mod_5": [value % 5 for value in P12_HIGH],
            "P18_degree_retained": 18,
            "P12_degree_retained": 12,
            "gcd_P18_P12_coefficients_low_to_high": gcd_cross,
            "gcd_P18_derivative_coefficients_low_to_high": gcd18,
            "gcd_P12_derivative_coefficients_low_to_high": gcd12,
            "P18_and_P12_coprime_over_Q": True,
            "P18_squarefree_over_Q": True,
            "P12_squarefree_over_Q": True,
        },
        "branch_theorem": {
            "ordinary_norm_reduced": "N_7(z)=P18(z)^2/(49*P12(z)^2)",
            "coprime_squarefree_divisor_multiplicities": "every finite zero has order +2 and every finite pole has order -2",
            "normalizing_root_degree": 3,
            "multiplicity_divisibility": "2 mod 3 is nonzero",
            "normalized_root_local_orders": ["+2/3 at every P18 zero", "-2/3 at every P12 zero"],
            "normalized_root_is_rational": False,
            "normalized_root_is_single_valued_meromorphic_across_divisor": False,
            "normalized_root_monodromy": "nontrivial cubic monodromy exp(+/- 4*pi*i/3)",
            "p7_counterexample_closes_all_prime_determinant_claim": True,
        },
        "decisions": {
            "C45_normalized_euler_germ": "RETAINED_ON_SIMPLY_CONNECTED_ZERO_FREE_LOG_DOMAIN",
            "normalized_root_as_rational_local_factor": "REFUTED_EXACTLY_AT_p_7",
            "normalized_root_as_meromorphic_fredholm_determinant": "REFUTED_EXACTLY_AT_p_7",
            "ordinary_galois_norm": "REMAINS_RATIONAL_BUT_UNBOUNDED_RANK",
            "next_large_gate": "TEST_NORMALIZED_TRACE_OR_VON_NEUMANN_DETERMINANT_ALGEBRA_OR_CHANGE_DYNAMICAL_FORM",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "the C45 normalized Log_0 Euler germ survives on its zero-free branch domain, but is not a global meromorphic determinant",
            "A3": "A3_FAIL",
            "A3_reason": "exact p=7 divisor orders are not divisible by the cubic normalization degree",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "normalized_root_claimed_rational": False,
            "normalized_root_claimed_single_valued_meromorphic": False,
            "branch_germ_discarded": False,
            "normalized_trace_or_von_neumann_determinant_refuted": False,
        },
    }


def verify_sector_to_theta(payload: dict[str, Any]) -> None:
    sector = payload["exact_sector_polynomials"]
    require(sector["common_denominator"] == 7, "sector denominator mismatch")
    d0 = rows_to_x_poly(tuple(tuple(row) for row in sector["D0_numerator_X0_through_X5_by_z_low_to_high"]))
    d1 = rows_to_x_poly(tuple(tuple(row) for row in sector["D1_numerator_X0_through_X5_by_z_low_to_high"]))
    product0 = x_mul(d0, conjugate_x(d0))
    product1 = x_mul(d1, conjugate_x(d1))
    resultants = payload["resultant_and_norm_control"]
    theta0 = theta_expression_to_x(resultants["q0_numerator_theta2_theta1_theta0_by_z_low_to_high"])
    theta1 = theta_expression_to_x(resultants["q1_numerator_theta2_theta1_theta0_by_z_low_to_high"])
    # D*bar(D)=numerator product /49, while q expression has denominator 7.
    for x_degree in range(6):
        require(
            z_equal(product0[x_degree], z_scale(theta0[x_degree], 7)),
            f"D0 conjugate product/theta reduction mismatch at X^{x_degree}",
        )
        require(
            z_equal(product1[x_degree], z_scale(theta1[x_degree], 7)),
            f"D1 conjugate product/theta reduction mismatch at X^{x_degree}",
        )


def audit_certificate(certificate: Any, project_root: Path) -> tuple[list[dict[str, str]], bool]:
    gates: list[dict[str, str]] = []

    def run(name: str, check: Callable[[], None]) -> None:
        try:
            check()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:
            gates.append({"gate": name, "status": "ERROR", "detail": f"{type(exc).__name__}: {exc}"})
        else:
            gates.append({"gate": name, "status": "PASS", "detail": "verified"})

    def schema_gate() -> None:
        require(type(certificate) is dict, "certificate must be dictionary")
        require(set(certificate) == {"schema", "payload", "payload_sha256"}, "top-level keys mismatch")
        require(certificate["schema"] == SCHEMA, "schema mismatch")
        require(type(certificate["payload"]) is dict, "payload must be dictionary")
        require(type(certificate["payload_sha256"]) is str, "digest must be string")

    def digest_gate() -> None:
        digest = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == digest, "payload digest mismatch")

    def source_gate() -> None:
        require(strict_equal(certificate["payload"]["source_lock"], expected_source_lock(project_root)), "source lock mismatch")

    def convention_gate() -> None:
        conventions = certificate["payload"]["p7_conventions"]
        require(type(conventions["prime"]) is int and conventions["prime"] == 7, "p=7 convention mismatch")
        require(conventions["rho_order_3"] == 2, "rho convention mismatch")
        require(conventions["real_field_degree_d7"] == 3, "field degree mismatch")
        require(conventions["sector_dimensions"] == [3, 2, 2], "sector dimensions mismatch")

    def sector_gate() -> None:
        verify_sector_to_theta(certificate["payload"])
        require(certificate["payload"]["exact_sector_polynomials"]["D2_equals_D1"] is True, "sector pairing changed")

    def resultant_gate() -> None:
        control = certificate["payload"]["resultant_and_norm_control"]
        require(
            control["theta_minimal_polynomial_high_to_low"] == [1, 1, -2, -1],
            "theta minimal polynomial mismatch",
        )
        rows0 = control["q0_numerator_theta2_theta1_theta0_by_z_low_to_high"]
        rows1 = control["q1_numerator_theta2_theta1_theta0_by_z_low_to_high"]
        res0 = resultant_from_theta_rows(rows0, 7)
        res1 = resultant_from_theta_rows(rows1, 7)
        require(z_equal(res0, [Fraction(v, 49) for v in reversed(P18_HIGH)]), "q0 norm resultant mismatch")
        require(z_equal(res1, [Fraction(v, 7) for v in reversed(P12_HIGH)]), "q1 norm resultant mismatch")

    def norm_gate() -> None:
        control = certificate["payload"]["resultant_and_norm_control"]
        require(control["P18_coefficients_high_to_low"] == list(P18_HIGH), "P18 mismatch")
        require(control["P12_coefficients_high_to_low"] == list(P12_HIGH), "P12 mismatch")
        require(control["ordinary_norm_at_zero"] == 1, "norm constant mismatch")
        require(control["ordinary_norm_numerator_degree"] == 36, "numerator degree mismatch")
        require(control["ordinary_norm_denominator_degree"] == 24, "denominator degree mismatch")
        require(control["ordinary_norm_virtual_degree"] == 12, "virtual degree mismatch")

    def gcd_gate() -> None:
        control = certificate["payload"]["good_reduction_control"]
        require(type(control["modulus"]) is int and control["modulus"] == 5, "good prime mismatch")
        p18 = [v % 5 for v in reversed(P18_HIGH)]
        p12 = [v % 5 for v in reversed(P12_HIGH)]
        require(len(finite_poly_trim(p18[:])) - 1 == control["P18_degree_retained"] == 18, "P18 degree drop")
        require(len(finite_poly_trim(p12[:])) - 1 == control["P12_degree_retained"] == 12, "P12 degree drop")
        require(finite_gcd(p18[:], p12[:], 5) == control["gcd_P18_P12_coefficients_low_to_high"] == [1], "cross gcd mismatch")
        require(finite_gcd(p18[:], finite_derivative(p18, 5), 5) == control["gcd_P18_derivative_coefficients_low_to_high"] == [1], "P18 squarefree gcd mismatch")
        require(finite_gcd(p12[:], finite_derivative(p12, 5), 5) == control["gcd_P12_derivative_coefficients_low_to_high"] == [1], "P12 squarefree gcd mismatch")

    def branch_gate() -> None:
        theorem = certificate["payload"]["branch_theorem"]
        require(theorem["normalizing_root_degree"] == 3, "root degree mismatch")
        require(theorem["multiplicity_divisibility"] == "2 mod 3 is nonzero", "divisibility verdict changed")
        require(theorem["normalized_root_local_orders"] == ["+2/3 at every P18 zero", "-2/3 at every P12 zero"], "fractional orders changed")
        require(theorem["normalized_root_is_rational"] is False, "rationality upgraded")
        require(theorem["normalized_root_is_single_valued_meromorphic_across_divisor"] is False, "meromorphicity upgraded")

    def decision_gate() -> None:
        decisions = certificate["payload"]["decisions"]
        require(decisions["C45_normalized_euler_germ"] == "RETAINED_ON_SIMPLY_CONNECTED_ZERO_FREE_LOG_DOMAIN", "C45 germ incorrectly discarded")
        require(decisions["normalized_root_as_rational_local_factor"] == "REFUTED_EXACTLY_AT_p_7", "rational verdict changed")
        require(decisions["normalized_root_as_meromorphic_fredholm_determinant"] == "REFUTED_EXACTLY_AT_p_7", "Fredholm verdict changed")

    def route_scope_gate() -> None:
        route = certificate["payload"]["route_a"]
        require(route["A1"] == "A1_WEAK", "A1 changed")
        require(route["A2"] == "A2_ANALYTIC_DETERMINANT", "A2 changed")
        require(route["A3"] == "A3_FAIL", "A3 changed")
        require(route["A4"] == "A4_NATURAL_QUANTIZATION", "A4 changed")
        require(route["overall"] == "ROUTE_A_REJECTED", "overall changed")
        require(route["route_b_invocation_allowed"] is False, "Route B enabled")
        scope = certificate["payload"]["scope"]
        require(all(type(value) is bool for value in scope.values()), "scope types invalid")
        require(not any(scope.values()), "prohibited scope claim true")

    def full_payload_gate() -> None:
        require(strict_equal(certificate["payload"], expected_payload(project_root)), "full payload mismatch")

    run("G01_SCHEMA_AND_TYPES", schema_gate)
    run("G02_PAYLOAD_DIGEST", digest_gate)
    run("G03_SOURCE_LOCK", source_gate)
    run("G04_P7_CONVENTIONS", convention_gate)
    run("G05_SECTOR_TO_REAL_FIELD_REDUCTION", sector_gate)
    run("G06_INDEPENDENT_RESULTANTS", resultant_gate)
    run("G07_REDUCED_NORM_AND_DEGREES", norm_gate)
    run("G08_GOOD_REDUCTION_COPRIME_SQUAREFREE", gcd_gate)
    run("G09_FRACTIONAL_BRANCH_ORDERS", branch_gate)
    run("G10_LOCAL_FACTOR_DECISIONS", decision_gate)
    run("G11_ROUTE_A_AND_SCOPE", route_scope_gate)
    run("G12_FULL_PAYLOAD_REPLAY", full_payload_gate)
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    parser.add_argument("--output")
    arguments = parser.parse_args()
    certificate_path = Path(arguments.certificate)
    project_root = Path(__file__).resolve().parents[1]
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, project_root)
    report = {
        "schema": "hcs-c46-independent-check-v1",
        "certificate_sha256": sha256_file(certificate_path),
        "gates": gates,
        "passed": passed,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        Path(arguments.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
