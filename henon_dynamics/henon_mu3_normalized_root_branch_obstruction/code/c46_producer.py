#!/usr/bin/env python3
"""Exact p=7 normalized-root obstruction certificate for HCS-C46."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import sympy as sp


SCHEMA = "hcs-c46-certificate-v1"
MODULAR_CONTROL_PRIME = 5

P18_HIGH = (
    49, 147, 147, -14, -133, -63, 71, 104, 50, 13,
    50, 104, 71, -63, -133, -14, 147, 147, 49,
)
P12_HIGH = (7, 0, -21, 0, 35, 0, -41, 0, 35, 0, -21, 0, 7)

# Low-to-high z-polynomial coefficients in Q[X]/Phi_7, represented as rows
# [coefficient of X^0,...,coefficient of X^5].  The common 1/7 is separate.
D0_NUMERATOR_BY_Z_DEGREE = (
    (7, 0, 0, 0, 0, 0),
    (1, -2, -9, 1, 0, -5),
    (3, 2, -3, 2, 3, -7),
    (7, 0, 0, 0, 0, 0),
)
D1_NUMERATOR_BY_Z_DEGREE = (
    (7, 0, 0, 0, 0, 0),
    (2, 4, 6, 1, 3, -2),
    (-7, 0, 0, 0, 0, 0),
)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def primitive_integer_poly(poly: sp.Poly) -> tuple[int, list[int]]:
    content, primitive = sp.polys.polytools.primitive(poly)
    coefficients = [int(value) for value in primitive.all_coeffs()]
    if coefficients[0] < 0:
        content = -content
        coefficients = [-value for value in coefficients]
    return int(content), coefficients


def poly_mod_high(coefficients: tuple[int, ...], modulus: int) -> list[int]:
    return [coefficient % modulus for coefficient in coefficients]


def trim_low(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def derivative_low(poly: list[int], modulus: int) -> list[int]:
    return trim_low([index * poly[index] % modulus for index in range(1, len(poly))])


def divmod_low(left: list[int], right: list[int], modulus: int) -> tuple[list[int], list[int]]:
    left = trim_low([value % modulus for value in left])
    right = trim_low([value % modulus for value in right])
    assert right != [0]
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
        left = trim_low(left)
    return trim_low(quotient), left


def gcd_low(left: list[int], right: list[int], modulus: int) -> list[int]:
    left = trim_low(left)
    right = trim_low(right)
    while right != [0]:
        _, remainder = divmod_low(left, right, modulus)
        left, right = right, remainder
    inverse = pow(left[-1], -1, modulus)
    return [value * inverse % modulus for value in left]


def modular_gcd_controls() -> dict[str, Any]:
    modulus = MODULAR_CONTROL_PRIME
    p18 = list(reversed(poly_mod_high(P18_HIGH, modulus)))
    p12 = list(reversed(poly_mod_high(P12_HIGH, modulus)))
    gcd_cross = gcd_low(p18, p12, modulus)
    gcd_p18_derivative = gcd_low(p18, derivative_low(p18, modulus), modulus)
    gcd_p12_derivative = gcd_low(p12, derivative_low(p12, modulus), modulus)
    assert gcd_cross == gcd_p18_derivative == gcd_p12_derivative == [1]
    assert len(trim_low(p18)) - 1 == 18
    assert len(trim_low(p12)) - 1 == 12
    return {
        "modulus": modulus,
        "P18_coefficients_high_to_low_mod_5": poly_mod_high(P18_HIGH, modulus),
        "P12_coefficients_high_to_low_mod_5": poly_mod_high(P12_HIGH, modulus),
        "P18_degree_retained": 18,
        "P12_degree_retained": 12,
        "gcd_P18_P12_coefficients_low_to_high": gcd_cross,
        "gcd_P18_derivative_coefficients_low_to_high": gcd_p18_derivative,
        "gcd_P12_derivative_coefficients_low_to_high": gcd_p12_derivative,
        "P18_and_P12_coprime_over_Q": True,
        "P18_squarefree_over_Q": True,
        "P12_squarefree_over_Q": True,
    }


def resultant_controls() -> dict[str, Any]:
    theta, z = sp.symbols("theta z")
    minimal = theta**3 + theta**2 - 2 * theta - 1
    q0_numerator = (
        -15 * theta**2 * z**5
        - 26 * theta**2 * z**4
        - 26 * theta**2 * z**3
        - 26 * theta**2 * z**2
        - 15 * theta**2 * z
        - 3 * theta * z**5
        - 10 * theta * z**4
        - 19 * theta * z**3
        - 10 * theta * z**2
        - 3 * theta * z
        + 7 * z**6
        + 31 * z**5
        + 61 * z**4
        + 72 * z**3
        + 61 * z**2
        + 31 * z
        + 7
    )
    q1_numerator = (
        4 * theta**2 * z**2
        + 5 * theta * z**2
        + 7 * z**4
        - 12 * z**2
        + 7
    )
    resultant0 = sp.Poly(sp.resultant(minimal, q0_numerator, theta), z)
    resultant1 = sp.Poly(sp.resultant(minimal, q1_numerator, theta), z)
    content0, primitive0 = primitive_integer_poly(resultant0)
    content1, primitive1 = primitive_integer_poly(resultant1)
    assert content0 == 7 and tuple(primitive0) == P18_HIGH
    assert content1 == 49 and tuple(primitive1) == P12_HIGH
    # q_k has a factor 1/7.  A cubic norm therefore divides each raw
    # numerator resultant by 7^3, yielding P18/49 and P12/7.
    return {
        "theta_minimal_polynomial_high_to_low": [1, 1, -2, -1],
        "q0_numerator_theta2_theta1_theta0_by_z_low_to_high": [
            [0, 0, 7],
            [-15, -3, 31],
            [-26, -10, 61],
            [-26, -19, 72],
            [-26, -10, 61],
            [-15, -3, 31],
            [0, 0, 7],
        ],
        "q1_numerator_theta2_theta1_theta0_by_z_low_to_high": [
            [0, 0, 7],
            [0, 0, 0],
            [4, 5, -12],
            [0, 0, 0],
            [0, 0, 7],
        ],
        "raw_resultant_q0_numerator_content": content0,
        "raw_resultant_q1_numerator_content": content1,
        "P18_coefficients_high_to_low": primitive0,
        "P12_coefficients_high_to_low": primitive1,
        "norm_q0": "P18/49",
        "norm_q1": "P12/7",
        "ordinary_norm_E": "P18^2/(49*P12^2)",
        "ordinary_norm_at_zero": 1,
        "ordinary_norm_numerator_degree": 36,
        "ordinary_norm_denominator_degree": 24,
        "ordinary_norm_virtual_degree": 12,
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relatives = (
        "henon_mu3_augmented_euler_superproduct/results/c43_certificate.json",
        "henon_mu3_fixed_coefficient_field_obstruction/results/c44_certificate.json",
        "henon_mu3_galois_norm_rank_obstruction/results/c45_certificate.json",
    )
    answer: list[dict[str, str]] = []
    for relative in relatives:
        source = henon_root / relative
        if not source.is_file():
            raise FileNotFoundError(source)
        answer.append(
            {"path": f"henon_dynamics/{relative}", "sha256": sha256_file(source)}
        )
    return answer


def build_payload(project_root: Path) -> dict[str, Any]:
    resultants = resultant_controls()
    modular = modular_gcd_controls()
    return {
        "material_passport": {
            "candidate_id": "HCS-C46",
            "project": "henon_mu3_normalized_root_branch_obstruction",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact cyclotomic reduction, symbolic resultants, and good-prime gcd certificates; no zero-table data",
        },
        "source_lock": source_lock(project_root),
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
            "D0_numerator_X0_through_X5_by_z_low_to_high": [
                list(row) for row in D0_NUMERATOR_BY_Z_DEGREE
            ],
            "D1_numerator_X0_through_X5_by_z_low_to_high": [
                list(row) for row in D1_NUMERATOR_BY_Z_DEGREE
            ],
            "D2_equals_D1": True,
            "paired_q0": "q0=D0*conjugate(D0)",
            "paired_q1": "q1=D1*conjugate(D1)",
            "paired_factor_E": "E=(q0/q1)^2",
        },
        "resultant_and_norm_control": resultants,
        "good_reduction_control": modular,
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


def build_certificate(project_root: Path) -> dict[str, Any]:
    payload = build_payload(project_root)
    return {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    certificate = build_certificate(project_root)
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {output}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
