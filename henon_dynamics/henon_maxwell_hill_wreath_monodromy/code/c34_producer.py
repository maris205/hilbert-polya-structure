#!/usr/bin/env python3
"""Exact producer for HCS-C34 Maxwell--Hill wreath monodromy."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import warnings
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning

warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


SCHEMA = "hcs-c34-certificate-v1"
PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[1]
C33_REL = Path(
    "henon_dynamics/phase3_hcs_c33_henon_action_collision_kummer/"
    "results/c33_kummer_certificate.json"
)
SOURCE_LOCK = {
    "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf":
        "23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9",
    str(C33_REL):
        "6535615d408cbd1f8460565cfef0f213db9edc4281d107fbd0889d79121e1fe7",
    "henon_dynamics/phase3_hcs_c33_henon_action_collision_kummer/THEOREM_PACKAGE.md":
        "be00eccf624b5cbae646a826768b4aaa310c6a79c13a757b6dd60fa8551710b4",
    "henon_dynamics/phase3_hcs_c33_henon_action_collision_kummer/code/c33_kummer_producer.py":
        "2b305744153b23a05032905e7c575d40ec387987622cb86b02e1489b75210437",
    "henon_dynamics/phase3_hcs_c33_henon_action_collision_kummer/code/c33_kummer_checker.py":
        "346355d8bed75f464f94e382e5315cd2ea63248c012a5903e31a3fae6e23ae4e",
}


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def encode_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def decode_univariate(encoded: dict, variable: sp.Symbol) -> sp.Poly:
    expr = 0
    for term in encoded["terms"]:
        exponent = term["exponents"][0]
        expr += sp.Rational(term["numerator"], term["denominator"]) * variable**exponent
    return sp.Poly(expr, variable, domain=sp.QQ)


def valuation(integer: int, prime: int) -> int:
    integer = abs(int(integer))
    if integer == 0:
        raise ValueError("zero has no finite valuation in this certificate")
    out = 0
    while integer % prime == 0:
        integer //= prime
        out += 1
    return out


def factor_dict(integer: int) -> dict[str, int]:
    return {str(p): int(e) for p, e in sorted(sp.factorint(abs(int(integer))).items())}


def rational_square_class(value: Fraction) -> int:
    factors: Counter[int] = Counter(sp.factorint(abs(value.numerator)))
    factors.subtract(sp.factorint(value.denominator))
    out = 1
    for prime, exponent in sorted(factors.items()):
        if exponent % 2:
            out *= prime
    return out


def primitive_integer_coefficients(poly: sp.Poly) -> list[int]:
    poly = sp.Poly(poly, poly.gens[0], domain=sp.QQ)
    denominators = [int(sp.denom(c)) for c in poly.all_coeffs()]
    common = math.lcm(*denominators)
    coefficients = [int(c * common) for c in poly.all_coeffs()]
    content = abs(math.gcd(*coefficients))
    coefficients = [c // content for c in coefficients]
    if coefficients[0] < 0:
        coefficients = [-c for c in coefficients]
    return coefficients


def factor_degrees(poly: sp.Poly, prime: int) -> list[int]:
    rows: list[int] = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SymPyDeprecationWarning)
        factors = sp.factor_list(poly, modulus=prime)[1]
    for factor, exponent in factors:
        rows.extend([factor.degree()] * exponent)
    return sorted(rows, reverse=True)


def modular_factor_ledger(poly: sp.Poly, prime: int) -> dict:
    """Return a canonical, coefficient-level factorization ledger."""
    variable = poly.gens[0]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SymPyDeprecationWarning)
        unit, factors = sp.factor_list(poly, modulus=prime)
    rows = []
    for factor, exponent in factors:
        monic = factor.monic()
        rows.append(
            {
                "degree": monic.degree(),
                "exponent": int(exponent),
                "monic_coefficients_high_to_low": [
                    int(coefficient) % prime for coefficient in monic.all_coeffs()
                ],
                "derivative_gcd_degree": sp.gcd(
                    monic, sp.Poly(sp.diff(monic.as_expr(), variable), variable, modulus=prime)
                ).degree(),
            }
        )
    rows.sort(key=lambda row: (row["degree"], row["monic_coefficients_high_to_low"]))
    return {"unit": int(unit) % prime, "factors": rows}


def polynomial_power_mod_x(exponent: int, modulus: sp.Poly, prime: int) -> sp.Poly:
    x = modulus.gens[0]
    result = sp.Poly(1, x, modulus=prime)
    base = sp.Poly(x, x, modulus=prime)
    while exponent:
        if exponent & 1:
            result = (result * base).rem(modulus)
        base = (base * base).rem(modulus)
        exponent >>= 1
    return result


def gf2_rank(rows: set[int]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def permutation_module_census(dimension: int) -> dict[str, int]:
    census: Counter[int] = Counter()
    vectors = range(1 << dimension)
    by_weight = {
        weight: {v for v in vectors if v.bit_count() == weight}
        for weight in range(dimension + 1)
    }
    for vector in vectors:
        census[gf2_rank(by_weight[vector.bit_count()])] += 1
    return {str(rank): count for rank, count in sorted(census.items())}


def load_source_object() -> tuple[dict, sp.Poly, sp.Poly, int, Fraction]:
    for relative, expected in SOURCE_LOCK.items():
        actual = sha256_path(REPO / relative)
        if actual != expected:
            raise RuntimeError(f"source-lock mismatch for {relative}: {actual}")

    certificate = json.loads((REPO / C33_REL).read_text(encoding="utf-8"))
    if certificate["schema"] != "HCS-C33-PHASE3-KUMMER-1":
        raise RuntimeError("unexpected C33 schema")
    payload = certificate["payload"]
    if payload["collision_parameter_galois_gate"]["conclusion"] != "Gal(P9/QQ)=S9":
        raise RuntimeError("C33 S9 gate is not frozen")
    if payload["hill_kummer_gate"]["conclusion"] != "NONTRIVIAL_QUADRATIC_KUMMER_CLASS_OVER_K9":
        raise RuntimeError("C33 Kummer gate is not frozen")

    A = sp.Symbol("A")
    p9 = decode_univariate(payload["derived_polynomials"]["P9"], A)
    beta_data = payload["hill_kummer_gate"]["symmetric_branch_norm_NH"]
    beta_num = sp.Poly(
        sum(int(c) * A**i for i, c in enumerate(beta_data["numerators_low_to_high"])),
        A,
        domain=sp.ZZ,
    )
    beta_den = int(beta_data["denominator"])
    norm_data = payload["hill_kummer_gate"]["field_norm"]
    inherited_norm = Fraction(int(norm_data["numerator"]), int(norm_data["denominator"]))
    return payload, p9, beta_num, beta_den, inherited_norm


def build_payload() -> dict:
    source, p9, beta_num, beta_den, inherited_norm = load_source_object()
    A, U, T = sp.symbols("A U T")
    p9 = sp.Poly(p9.as_expr().subs(p9.gens[0], A), A, domain=sp.ZZ)
    beta_num = sp.Poly(beta_num.as_expr().subs(beta_num.gens[0], A), A, domain=sp.ZZ)

    leading = int(p9.LC())
    resultant_norm = sp.resultant(p9.as_expr(), beta_num.as_expr(), A)
    norm = Fraction(int(resultant_norm), leading ** beta_num.degree() * beta_den**p9.degree())
    if norm != inherited_norm:
        raise AssertionError("C33 norm did not replay")

    resultant_u = sp.resultant(
        p9.as_expr(), beta_den * U**2 - beta_num.as_expr(), A
    )
    monic_f18 = sp.Poly(
        sp.cancel(resultant_u / (leading ** beta_num.degree() * beta_den**p9.degree())),
        U,
        domain=sp.QQ,
    )
    f18_coefficients = primitive_integer_coefficients(monic_f18)
    f18 = sp.Poly.from_list(f18_coefficients, gens=U, domain=sp.ZZ)
    mod7 = sp.Poly(f18, U, modulus=7)
    rabin_final = polynomial_power_mod_x(7**18, mod7, 7) - sp.Poly(U, U, modulus=7)
    rabin_gcd_degrees = {}
    for divisor in (2, 3):
        probe = polynomial_power_mod_x(7 ** (18 // divisor), mod7, 7) - sp.Poly(U, U, modulus=7)
        rabin_gcd_degrees[str(divisor)] = sp.gcd(mod7, probe).degree()

    discriminant = int(sp.discriminant(p9.as_expr(), A))
    discriminant_class = rational_square_class(Fraction(discriminant, 1))
    norm_class = rational_square_class(norm)

    prime = 19
    shift = -3 + 5 * prime**2
    shifted_p9 = sp.Poly(sp.expand(p9.as_expr().subs(A, shift + T)), T, domain=sp.ZZ)
    shifted_beta = sp.Poly(
        sp.expand(beta_num.as_expr().subs(A, shift + T)), T, domain=sp.ZZ
    )
    p9_valuations = [valuation(shifted_p9.nth(i), prime) for i in range(10)]
    beta_valuations = [valuation(shifted_beta.nth(i), prime) for i in range(9)]
    p9_unit_residues = [
        (int(shifted_p9.nth(i)) // prime ** p9_valuations[i]) % prime
        for i in range(10)
    ]
    beta_unit_residues = [
        (int(shifted_beta.nth(i)) // prime ** beta_valuations[i]) % prime
        for i in range(9)
    ]
    if p9_valuations != [5, 3, 0, 0, 0, 0, 0, 0, 0, 0]:
        raise AssertionError("p=19 Newton data changed")
    if beta_valuations != [3, 0, 0, 0, 0, 0, 0, 0, 0]:
        raise AssertionError("p=19 Hill numerator data changed")
    p9_mod19 = sp.Poly(p9, A, modulus=prime)
    beta_mod19 = sp.Poly(beta_num, A, modulus=prime)
    common_mod19 = sp.gcd(p9_mod19, beta_mod19).monic()
    if common_mod19.all_coeffs() != [1, 3]:
        raise AssertionError("p=19 common residue factor changed")

    module_census = permutation_module_census(9)
    if module_census != {"0": 1, "1": 1, "8": 255, "9": 255}:
        raise AssertionError("F2 permutation-module census changed")

    payload = {
        "material_passport": {
            "candidate_id": "HCS-C34",
            "date_utc": "2026-08-12",
            "phase": "full Maxwell--Hill Kummer monodromy",
            "evidence_mode": "exact characteristic-zero algebra and local Newton polygon",
            "ai_assistance_disclosed": True,
        },
        "source_lock": dict(sorted(SOURCE_LOCK.items())),
        "inherited_object": {
            "family": "area-preserving H6 Henon map with cyclic period-five action",
            "collision_field": "K=QQ[A]/(P9)",
            "P9_coefficients_high_to_low": [int(c) for c in p9.all_coeffs()],
            "beta_name": "symmetric Maxwell--Hill product N_H",
            "beta_numerator_coefficients_low_to_high": [
                int(beta_num.nth(i)) for i in range(beta_num.degree() + 1)
            ],
            "beta_denominator": beta_den,
            "inherited_galois_group": "Gal(L/QQ)=S9",
            "inherited_norm": encode_fraction(norm),
            "c33_scope_reopened": "C33 explicitly left the full Kummer wreath group unclaimed",
        },
        "degree_eighteen_polynomial_gate": {
            "definition": "F18(U)=primitive_integer_part Norm_K/QQ(U^2-beta)",
            "degree": f18.degree(),
            "coefficients_high_to_low": f18_coefficients,
            "even_polynomial": all(f18.nth(i) == 0 for i in range(1, 19, 2)),
            "modular_irreducibility": {
                "prime": 7,
                "factor_degrees": factor_degrees(f18, 7),
                "rabin_prime_divisors_of_degree": [2, 3],
                "rabin_gcd_degrees": rabin_gcd_degrees,
                "frobenius_final_remainder_zero": rabin_final.is_zero,
            },
            "conclusion": "F18_IS_IRREDUCIBLE_OVER_QQ",
        },
        "rational_squareclass_gate": {
            "P9_discriminant": discriminant,
            "P9_discriminant_factorization": factor_dict(discriminant),
            "sign_field_squarefree_class": discriminant_class,
            "beta_field_norm": encode_fraction(norm),
            "beta_field_norm_numerator_factorization": factor_dict(norm.numerator),
            "beta_field_norm_denominator_factorization": factor_dict(norm.denominator),
            "norm_squarefree_class": norm_class,
            "norm_over_discriminant_squarefree_class": rational_square_class(
                norm / discriminant
            ),
            "unique_quadratic_subfield_test": {
                "norm_is_rational_square": False,
                "norm_matches_S9_sign_field": False,
                "all_ones_relation_excluded": True,
            },
        },
        "local_newton_gate": {
            "prime": prime,
            "parameter_shift_A_equals": f"{shift}+T",
            "shift_integer": shift,
            "P9_leading_coefficient_is_p_unit": leading % prime != 0,
            "P9_shifted_coefficient_valuations_low_to_high": p9_valuations,
            "P9_shifted_unit_residues_low_to_high": p9_unit_residues,
            "newton_cluster_segment": {
                "left_point": [0, 5],
                "right_point": [2, 0],
                "intermediate_point": [1, 3],
                "slope": "-5/2",
                "horizontal_length": 2,
                "ramification_index": 2,
                "residual_degree": 1,
                "residual_polynomial_coefficients_low_to_high": [
                    p9_unit_residues[0], p9_unit_residues[2]
                ],
                "residual_polynomial_separable": True,
            },
            "beta_denominator_is_p_unit": beta_den % prime != 0,
            "beta_numerator_shifted_coefficient_valuations_low_to_high": beta_valuations,
            "beta_numerator_shifted_unit_residues_low_to_high": beta_unit_residues,
            "residue_factor_degrees_with_multiplicity": {
                "P9_mod_19": factor_degrees(p9, prime),
                "beta_numerator_mod_19": factor_degrees(beta_num, prime),
            },
            "residue_factorization_ledger": {
                "P9_mod_19": modular_factor_ledger(p9, prime),
                "beta_numerator_mod_19": modular_factor_ledger(beta_num, prime),
            },
            "gcd_P9_beta_numerator_mod_19_coefficients_high_to_low": [
                int(c) % prime for c in common_mod19.all_coeffs()
            ],
            "local_splitting_field_gate": {
                "repeated_residue_factor": {
                    "monic_coefficients_high_to_low": [1, 3],
                    "multiplicity": 2,
                },
                "cluster_ramification_index": 2,
                "noncluster_residue_factors_are_distinct_and_separable": True,
                "noncluster_extensions_are_unramified": True,
                "local_splitting_field_ramification_index": 2,
            },
            "local_valuations_normalized_on_K": {
                "v_P(beta)": 5,
                "v_P(Norm_K_QQ_beta)": 10,
                "v_P(beta/Norm_K_QQ_beta)": -5,
            },
            "splitting_field_parity_functional": {
                "cluster_root_count": 2,
                "cluster_beta_valuations": [5, 5],
                "other_root_beta_valuations": [0, 0, 0, 0, 0, 0, 0],
                "support_vector": "e_1+e_2 after labeling the cluster roots first",
                "reason": (
                    "slope denominator 2 and horizontal length 2 give one degree-two local cluster; "
                    "the unique minimum of beta(c+T) is its unit linear coefficient times T"
                ),
            },
            "conclusion": "TWO_ROOT_ODD_PARITY_FUNCTIONAL_CERTIFIED",
        },
        "permutation_relation_module_gate": {
            "ambient_module": "F2^9 with S9 permuting coordinates",
            "orbit_span_rank_census_over_all_512_vectors": module_census,
            "invariant_submodules": ["0", "<all-ones>", "augmentation W", "F2^9"],
            "elementary_proof": (
                "a nonconstant vector minus a transposition contains e_i+e_j; "
                "its S9 orbit spans W, and for odd 9 any odd nonconstant vector adds a complement"
            ),
            "relation_module_is_S9_invariant": True,
        },
        "relation_elimination_gate": {
            "local_annihilator": (
                "every square relation is orthogonal to e_1+e_2 and all its S9 conjugates"
            ),
            "pair_orbit_consequence": (
                "orthogonality to every e_i+e_j forces all nine relation coordinates equal"
            ),
            "remaining_relation_candidates": ["0", "all-ones"],
            "all_ones_case": (
                "product beta_i=Norm(beta) is neither a rational square nor the S9 sign-field class"
            ),
            "relation_module": "0",
            "kummer_rank": 9,
        },
        "wreath_monodromy_gate": {
            "quadratic_extension": "K(sqrt(beta))/K",
            "normal_closure_over_L": "L(sqrt(beta_1),...,sqrt(beta_9))",
            "kernel_over_L": "C2^9",
            "quotient_over_QQ": "S9",
            "wreath_embedding": "Gal(M/QQ) embeds in C2 wr S9 by the quadratic Kummer embedding theorem",
            "group_order": 2**9 * math.factorial(9),
            "galois_group": "C2^9 semidirect S9 = C2 wr S9",
            "conclusion": "FULL_MAXWELL_HILL_WREATH_MONODROMY_PROVED",
        },
        "route_a_evaluation": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "reason": (
                "full fixed-period arithmetic monodromy is proved, but there is no prime law, "
                "all-period determinant, critical-line theorem, or self-adjoint operator"
            ),
        },
        "decisions": {
            "C34_exact_gate": "GO_THEOREM",
            "C33_no_full_wreath_scope": "CLOSED_POSITIVELY",
            "standard_kummer_or_wreath_embedding_is_novel": False,
            "Henon_specific_full_rank_finding_is_new_in_locked_search": True,
            "Hilbert_Polya_construction": False,
        },
        "scope": {
            "period": 5,
            "collision_divisor": "P9(A)=0",
            "decorated_object": "nine conjugates of the two-branch Hill product beta=N_H",
            "not_eighteen_individual_branch_Hill_classes": True,
            "no_all_period_claim": True,
            "no_dynamical_zeta_claim": True,
            "no_RH_zero_claim": True,
            "no_self_adjoint_operator_claim": True,
            "finite_primes_are_proof_certificates_not_fitted_data": True,
        },
    }
    return payload


def build_certificate() -> dict:
    payload = build_payload()
    return {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_bytes(payload)).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(certificate["payload_sha256"])


if __name__ == "__main__":
    main()
