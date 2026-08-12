#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C34."""

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


class GateFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def strict_equal(left: object, right: object) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(strict_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return bool(left == right)


def exact_keys(value: dict, expected: set[str], label: str) -> None:
    require(type(value) is dict, f"{label} is not an object")
    require(set(value) == expected, f"{label} keys changed")


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def decode_poly(encoded: dict, variable: sp.Symbol) -> sp.Poly:
    expr = 0
    for row in encoded["terms"]:
        expr += sp.Rational(row["numerator"], row["denominator"]) * variable ** row["exponents"][0]
    return sp.Poly(expr, variable, domain=sp.QQ)


def valuation(value: int, prime: int) -> int:
    value = abs(int(value))
    require(value != 0, "unexpected zero valuation")
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def factors(value: int) -> dict[str, int]:
    return {str(p): int(e) for p, e in sorted(sp.factorint(abs(int(value))).items())}


def square_class(value: Fraction) -> int:
    exponents: Counter[int] = Counter(sp.factorint(abs(value.numerator)))
    exponents.subtract(sp.factorint(value.denominator))
    answer = 1
    for prime, exponent in sorted(exponents.items()):
        if exponent % 2:
            answer *= prime
    return answer


def primitive_coefficients(poly: sp.Poly) -> list[int]:
    coefficients = poly.all_coeffs()
    common = math.lcm(*(int(sp.denom(c)) for c in coefficients))
    integers = [int(c * common) for c in coefficients]
    content = abs(math.gcd(*integers))
    integers = [c // content for c in integers]
    return integers if integers[0] > 0 else [-c for c in integers]


def factor_degrees(poly: sp.Poly, prime: int) -> list[int]:
    degrees = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SymPyDeprecationWarning)
        factors_mod_prime = sp.factor_list(poly, modulus=prime)[1]
    for factor, exponent in factors_mod_prime:
        degrees.extend([factor.degree()] * exponent)
    return sorted(degrees, reverse=True)


def modular_factor_ledger(poly: sp.Poly, prime: int) -> dict:
    """Independently canonicalize a complete modular factorization."""
    variable = poly.gens[0]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SymPyDeprecationWarning)
        unit, modular_factors = sp.factor_list(poly, modulus=prime)
    rows = []
    for factor, exponent in modular_factors:
        monic = factor.monic()
        derivative = sp.Poly(sp.diff(monic.as_expr(), variable), variable, modulus=prime)
        rows.append(
            {
                "degree": monic.degree(),
                "exponent": int(exponent),
                "monic_coefficients_high_to_low": [
                    int(coefficient) % prime for coefficient in monic.all_coeffs()
                ],
                "derivative_gcd_degree": sp.gcd(monic, derivative).degree(),
            }
        )
    rows.sort(key=lambda row: (row["degree"], row["monic_coefficients_high_to_low"]))
    return {"unit": int(unit) % prime, "factors": rows}


def power_x(exponent: int, modulus: sp.Poly, prime: int) -> sp.Poly:
    x = modulus.gens[0]
    out = sp.Poly(1, x, modulus=prime)
    base = sp.Poly(x, x, modulus=prime)
    while exponent:
        if exponent & 1:
            out = (out * base).rem(modulus)
        base = (base * base).rem(modulus)
        exponent >>= 1
    return out


def gf2_rank(rows: set[int]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def module_census() -> dict[str, int]:
    by_weight = {
        weight: {x for x in range(512) if x.bit_count() == weight}
        for weight in range(10)
    }
    census: Counter[int] = Counter()
    for vector in range(512):
        census[gf2_rank(by_weight[vector.bit_count()])] += 1
    return {str(rank): count for rank, count in sorted(census.items())}


def source_data() -> tuple[dict, sp.Poly, sp.Poly, int, Fraction]:
    for relative, digest in SOURCE_LOCK.items():
        require(sha256_path(REPO / relative) == digest, f"source drift: {relative}")
    cert = json.loads((REPO / C33_REL).read_text(encoding="utf-8"))
    require(cert["schema"] == "HCS-C33-PHASE3-KUMMER-1", "C33 schema")
    payload = cert["payload"]
    require(payload["collision_parameter_galois_gate"]["conclusion"] == "Gal(P9/QQ)=S9", "C33 S9")
    require(payload["hill_kummer_gate"]["conclusion"] == "NONTRIVIAL_QUADRATIC_KUMMER_CLASS_OVER_K9", "C33 Kummer")
    A = sp.Symbol("A")
    p9 = decode_poly(payload["derived_polynomials"]["P9"], A)
    beta = payload["hill_kummer_gate"]["symmetric_branch_norm_NH"]
    numerator = sp.Poly(
        sum(int(c) * A**i for i, c in enumerate(beta["numerators_low_to_high"])), A, domain=sp.ZZ
    )
    norm_row = payload["hill_kummer_gate"]["field_norm"]
    norm = Fraction(norm_row["numerator"], norm_row["denominator"])
    return payload, p9, numerator, int(beta["denominator"]), norm


def audit_certificate(certificate: dict) -> list[dict[str, str]]:
    gates: list[dict[str, str]] = []

    def gate(name: str, fn) -> None:
        try:
            fn()
            gates.append({"gate": name, "status": "PASS"})
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:  # unexpected checker errors are distinguishable
            gates.append({"gate": name, "status": "ERROR", "detail": f"{type(exc).__name__}: {exc}"})

    state: dict[str, object] = {}

    def g0() -> None:
        exact_keys(certificate, {"schema", "payload", "payload_sha256"}, "certificate")
        require(certificate["schema"] == SCHEMA, "schema")
        payload = certificate["payload"]
        require(type(payload) is dict, "payload type")
        require(
            certificate["payload_sha256"] == hashlib.sha256(canonical_bytes(payload)).hexdigest(),
            "payload hash",
        )
        exact_keys(
            payload,
            {
                "material_passport", "source_lock", "inherited_object",
                "degree_eighteen_polynomial_gate", "rational_squareclass_gate",
                "local_newton_gate", "permutation_relation_module_gate",
                "relation_elimination_gate", "wreath_monodromy_gate",
                "route_a_evaluation", "decisions", "scope",
            },
            "payload",
        )
        expected = {
            "candidate_id": "HCS-C34", "date_utc": "2026-08-12",
            "phase": "full Maxwell--Hill Kummer monodromy",
            "evidence_mode": "exact characteristic-zero algebra and local Newton polygon",
            "ai_assistance_disclosed": True,
        }
        require(strict_equal(payload["material_passport"], expected), "passport")
        state["payload"] = payload

    gate("G0_SCHEMA_HASH_PASSPORT", g0)

    def g1() -> None:
        payload = state["payload"]
        require(strict_equal(payload["source_lock"], dict(sorted(SOURCE_LOCK.items()))), "source-lock ledger")
        source, p9, beta, denominator, norm = source_data()
        expected = {
            "family": "area-preserving H6 Henon map with cyclic period-five action",
            "collision_field": "K=QQ[A]/(P9)",
            "P9_coefficients_high_to_low": [int(c) for c in p9.all_coeffs()],
            "beta_name": "symmetric Maxwell--Hill product N_H",
            "beta_numerator_coefficients_low_to_high": [int(beta.nth(i)) for i in range(9)],
            "beta_denominator": denominator,
            "inherited_galois_group": "Gal(L/QQ)=S9",
            "inherited_norm": {"numerator": norm.numerator, "denominator": norm.denominator},
            "c33_scope_reopened": "C33 explicitly left the full Kummer wreath group unclaimed",
        }
        require(strict_equal(payload["inherited_object"], expected), "inherited object")
        state.update({"p9": p9, "beta": beta, "denominator": denominator, "norm": norm})

    gate("G1_SOURCE_AND_C33_OBJECT", g1)

    def g2() -> None:
        payload = state["payload"]
        A, U = sp.symbols("A U")
        p9: sp.Poly = state["p9"]
        beta: sp.Poly = state["beta"]
        denominator: int = state["denominator"]
        leading = int(p9.LC())
        replay_norm = Fraction(
            int(sp.resultant(p9.as_expr(), beta.as_expr(), A)),
            leading ** beta.degree() * denominator**p9.degree(),
        )
        require(replay_norm == state["norm"], "norm resultant")
        resultant = sp.resultant(p9.as_expr(), denominator * U**2 - beta.as_expr(), A)
        monic = sp.Poly(
            sp.cancel(resultant / (leading ** beta.degree() * denominator**p9.degree())),
            U,
            domain=sp.QQ,
        )
        coefficients = primitive_coefficients(monic)
        f18 = sp.Poly.from_list(coefficients, gens=U, domain=sp.ZZ)
        mod7 = sp.Poly(f18, U, modulus=7)
        final = power_x(7**18, mod7, 7) - sp.Poly(U, U, modulus=7)
        gcds = {}
        for divisor in (2, 3):
            probe = power_x(7 ** (18 // divisor), mod7, 7) - sp.Poly(U, U, modulus=7)
            gcds[str(divisor)] = sp.gcd(mod7, probe).degree()
        expected = {
            "definition": "F18(U)=primitive_integer_part Norm_K/QQ(U^2-beta)",
            "degree": 18,
            "coefficients_high_to_low": coefficients,
            "even_polynomial": all(f18.nth(i) == 0 for i in range(1, 19, 2)),
            "modular_irreducibility": {
                "prime": 7, "factor_degrees": factor_degrees(f18, 7),
                "rabin_prime_divisors_of_degree": [2, 3],
                "rabin_gcd_degrees": gcds,
                "frobenius_final_remainder_zero": final.is_zero,
            },
            "conclusion": "F18_IS_IRREDUCIBLE_OVER_QQ",
        }
        require(strict_equal(payload["degree_eighteen_polynomial_gate"], expected), "F18 gate")

    gate("G2_NORM_POLYNOMIAL_AND_IRREDUCIBILITY", g2)

    def g3() -> None:
        payload = state["payload"]
        A = sp.Symbol("A")
        p9: sp.Poly = state["p9"]
        norm: Fraction = state["norm"]
        disc = int(sp.discriminant(p9.as_expr(), A))
        expected = {
            "P9_discriminant": disc,
            "P9_discriminant_factorization": factors(disc),
            "sign_field_squarefree_class": square_class(Fraction(disc, 1)),
            "beta_field_norm": {"numerator": norm.numerator, "denominator": norm.denominator},
            "beta_field_norm_numerator_factorization": factors(norm.numerator),
            "beta_field_norm_denominator_factorization": factors(norm.denominator),
            "norm_squarefree_class": square_class(norm),
            "norm_over_discriminant_squarefree_class": square_class(norm / disc),
            "unique_quadratic_subfield_test": {
                "norm_is_rational_square": False,
                "norm_matches_S9_sign_field": False,
                "all_ones_relation_excluded": True,
            },
        }
        require(strict_equal(payload["rational_squareclass_gate"], expected), "squareclass gate")
        require(expected["sign_field_squarefree_class"] == 597493, "sign squareclass")
        require(expected["norm_squarefree_class"] == 1792479, "norm squareclass")
        require(expected["norm_over_discriminant_squarefree_class"] == 3, "class ratio")
        state["disc"] = disc

    gate("G3_RATIONAL_SQUARECLASSES", g3)

    def g4() -> None:
        payload = state["payload"]
        A, T = sp.symbols("A T")
        p9: sp.Poly = state["p9"]
        beta: sp.Poly = state["beta"]
        denominator: int = state["denominator"]
        prime, shift = 19, 1802
        shifted_p9 = sp.Poly(sp.expand(p9.as_expr().subs(A, shift + T)), T, domain=sp.ZZ)
        shifted_beta = sp.Poly(sp.expand(beta.as_expr().subs(A, shift + T)), T, domain=sp.ZZ)
        pv = [valuation(shifted_p9.nth(i), prime) for i in range(10)]
        bv = [valuation(shifted_beta.nth(i), prime) for i in range(9)]
        pu = [(int(shifted_p9.nth(i)) // 19 ** pv[i]) % 19 for i in range(10)]
        bu = [(int(shifted_beta.nth(i)) // 19 ** bv[i]) % 19 for i in range(9)]
        common = sp.gcd(sp.Poly(p9, A, modulus=19), sp.Poly(beta, A, modulus=19)).monic()
        p9_factor_ledger = modular_factor_ledger(p9, 19)
        beta_factor_ledger = modular_factor_ledger(beta, 19)
        repeated = [
            row
            for row in p9_factor_ledger["factors"]
            if row["monic_coefficients_high_to_low"] == [1, 3]
        ]
        noncluster = [
            row
            for row in p9_factor_ledger["factors"]
            if row["monic_coefficients_high_to_low"] != [1, 3]
        ]
        require(len(repeated) == 1 and repeated[0]["exponent"] == 2, "repeated residue factor")
        require(
            all(row["exponent"] == 1 and row["derivative_gcd_degree"] == 0 for row in noncluster),
            "noncluster residue factors",
        )
        expected = {
            "prime": 19, "parameter_shift_A_equals": "1802+T", "shift_integer": 1802,
            "P9_leading_coefficient_is_p_unit": int(p9.LC()) % 19 != 0,
            "P9_shifted_coefficient_valuations_low_to_high": pv,
            "P9_shifted_unit_residues_low_to_high": pu,
            "newton_cluster_segment": {
                "left_point": [0, 5], "right_point": [2, 0],
                "intermediate_point": [1, 3], "slope": "-5/2",
                "horizontal_length": 2, "ramification_index": 2, "residual_degree": 1,
                "residual_polynomial_coefficients_low_to_high": [pu[0], pu[2]],
                "residual_polynomial_separable": True,
            },
            "beta_denominator_is_p_unit": denominator % 19 != 0,
            "beta_numerator_shifted_coefficient_valuations_low_to_high": bv,
            "beta_numerator_shifted_unit_residues_low_to_high": bu,
            "residue_factor_degrees_with_multiplicity": {
                "P9_mod_19": factor_degrees(p9, 19),
                "beta_numerator_mod_19": factor_degrees(beta, 19),
            },
            "residue_factorization_ledger": {
                "P9_mod_19": p9_factor_ledger,
                "beta_numerator_mod_19": beta_factor_ledger,
            },
            "gcd_P9_beta_numerator_mod_19_coefficients_high_to_low": [
                int(c) % 19 for c in common.all_coeffs()
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
                "v_P(beta)": 5, "v_P(Norm_K_QQ_beta)": 10,
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
        }
        require(pv == [5, 3, 0, 0, 0, 0, 0, 0, 0, 0], "Newton valuations")
        require(bv == [3, 0, 0, 0, 0, 0, 0, 0, 0], "Hill valuations")
        require(pu == [18, 6, 5, 6, 13, 7, 15, 12, 5, 12], "Newton unit residues")
        require(bu == [18, 6, 10, 13, 14, 11, 9, 8, 9], "Hill unit residues")
        require(Fraction(0 - 5, 2 - 0) == Fraction(-5, 2), "Newton slope")
        require(Fraction(5, 2) < 3, "middle point must lie above the edge")
        require(strict_equal(payload["local_newton_gate"], expected), "local Newton gate")

    gate("G4_LOCAL_NEWTON_ODD_VALUATION", g4)

    def g5() -> None:
        payload = state["payload"]
        census = module_census()
        expected = {
            "ambient_module": "F2^9 with S9 permuting coordinates",
            "orbit_span_rank_census_over_all_512_vectors": census,
            "invariant_submodules": ["0", "<all-ones>", "augmentation W", "F2^9"],
            "elementary_proof": (
                "a nonconstant vector minus a transposition contains e_i+e_j; "
                "its S9 orbit spans W, and for odd 9 any odd nonconstant vector adds a complement"
            ),
            "relation_module_is_S9_invariant": True,
        }
        require(census == {"0": 1, "1": 1, "8": 255, "9": 255}, "module census")
        require(strict_equal(payload["permutation_relation_module_gate"], expected), "module gate")

    gate("G5_PERMUTATION_RELATION_MODULE", g5)

    def g6() -> None:
        payload = state["payload"]
        expected = {
            "local_annihilator": "every square relation is orthogonal to e_1+e_2 and all its S9 conjugates",
            "pair_orbit_consequence": "orthogonality to every e_i+e_j forces all nine relation coordinates equal",
            "remaining_relation_candidates": ["0", "all-ones"],
            "all_ones_case": "product beta_i=Norm(beta) is neither a rational square nor the S9 sign-field class",
            "relation_module": "0", "kummer_rank": 9,
        }
        require(strict_equal(payload["relation_elimination_gate"], expected), "relation elimination")
        # The 36 pair vectors span the even-weight augmentation module.  Their
        # orthogonal complement is exactly the all-ones line.
        pair_rows = {(1 << i) | (1 << j) for i in range(9) for j in range(i + 1, 9)}
        require(gf2_rank(pair_rows) == 8, "pair orbit span")

    gate("G6_RELATION_ELIMINATION", g6)

    def g7() -> None:
        payload = state["payload"]
        expected = {
            "quadratic_extension": "K(sqrt(beta))/K",
            "normal_closure_over_L": "L(sqrt(beta_1),...,sqrt(beta_9))",
            "kernel_over_L": "C2^9", "quotient_over_QQ": "S9",
            "wreath_embedding": "Gal(M/QQ) embeds in C2 wr S9 by the quadratic Kummer embedding theorem",
            "group_order": 185794560,
            "galois_group": "C2^9 semidirect S9 = C2 wr S9",
            "conclusion": "FULL_MAXWELL_HILL_WREATH_MONODROMY_PROVED",
        }
        require(2**9 * math.factorial(9) == expected["group_order"], "group order")
        require(strict_equal(payload["wreath_monodromy_gate"], expected), "wreath gate")

    gate("G7_FULL_WREATH_GROUP", g7)

    def g8() -> None:
        payload = state["payload"]
        route = {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "reason": "full fixed-period arithmetic monodromy is proved, but there is no prime law, all-period determinant, critical-line theorem, or self-adjoint operator",
        }
        decisions = {
            "C34_exact_gate": "GO_THEOREM", "C33_no_full_wreath_scope": "CLOSED_POSITIVELY",
            "standard_kummer_or_wreath_embedding_is_novel": False,
            "Henon_specific_full_rank_finding_is_new_in_locked_search": True,
            "Hilbert_Polya_construction": False,
        }
        scope = {
            "period": 5, "collision_divisor": "P9(A)=0",
            "decorated_object": "nine conjugates of the two-branch Hill product beta=N_H",
            "not_eighteen_individual_branch_Hill_classes": True,
            "no_all_period_claim": True, "no_dynamical_zeta_claim": True,
            "no_RH_zero_claim": True, "no_self_adjoint_operator_claim": True,
            "finite_primes_are_proof_certificates_not_fitted_data": True,
        }
        require(strict_equal(payload["route_a_evaluation"], route), "Route-A")
        require(strict_equal(payload["decisions"], decisions), "decisions")
        require(strict_equal(payload["scope"], scope), "scope")

    gate("G8_ROUTE_A_DECISIONS_SCOPE", g8)
    return gates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
        gates = audit_certificate(certificate)
    except Exception as exc:
        gates = [{"gate": "CHECKER_TOP_LEVEL", "status": "ERROR", "detail": f"{type(exc).__name__}: {exc}"}]
    passed = sum(row["status"] == "PASS" for row in gates)
    report = {
        "schema": "hcs-c34-independent-check-v1",
        "certificate_sha256": sha256_path(args.certificate),
        "gates": gates,
        "summary": {"passed": passed, "total": len(gates), "all_pass": passed == len(gates)},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{passed}/{len(gates)} gates PASS")
    raise SystemExit(0 if passed == len(gates) else 1)


if __name__ == "__main__":
    main()
