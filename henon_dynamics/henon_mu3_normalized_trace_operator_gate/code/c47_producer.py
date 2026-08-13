#!/usr/bin/env python3
"""Exact operator-category certificate producer for HCS-C47."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c47-certificate-v1"
CONTROL_BOUND = 499
MOMENT_CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61)
EXPECTED_C2 = (-6, -6, -6, -30, 18, -54, 18)
EXPECTED_C3 = (
    Fraction(12, 7),
    Fraction(132, 13),
    Fraction(54, 19),
    Fraction(960, 31),
    Fraction(-612, 37),
    Fraction(3054, 43),
    Fraction(3414, 61),
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


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def prime_divisors(n: int) -> list[int]:
    answer: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            answer.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        answer.append(n)
    return answer


def primitive_root(p: int) -> int:
    factors = prime_divisors(p - 1)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // q, p) != 1 for q in factors):
            return candidate
    raise AssertionError("primitive root not found")


def split_primes_through(bound: int) -> tuple[int, ...]:
    return tuple(p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p))


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def chronological_zero_count(p: int, rho: int, n: int) -> int:
    """Count the zero fibre of the ordered rho-twisted 2n-step phase.

    Dynamic programming retains the current endpoint and total phase residue;
    it is an exact rebracketing of the chronological path sum, not an averaged
    transition matrix.
    """
    length = 2 * n
    cubes = [2 * x * x * x % p for x in range(p)]
    total = 0
    for x0 in range(p):
        states = [[0] * p for _ in range(p)]
        states[x0][cubes[x0]] = 1
        for _ in range(1, length):
            next_states = [[0] * p for _ in range(p)]
            for previous in range(p):
                shifts = [
                    (previous * current + cubes[current]) % p
                    for current in range(p)
                ]
                for residue, multiplicity in enumerate(states[previous]):
                    if multiplicity:
                        for current, shift in enumerate(shifts):
                            next_states[current][(residue + shift) % p] += multiplicity
            states = next_states
        for endpoint in range(p):
            total += states[endpoint][(-rho * endpoint * x0) % p]
    return total


def traced_moment_from_zero_count(p: int, n: int, zero_count: int) -> Fraction:
    return Fraction(2 * zero_count, p ** (n - 1)) - 2 * p**n


def build_block_control(p: int) -> dict[str, Any]:
    assert is_prime(p) and p % 3 == 1
    d = (p - 1) // 2
    d0 = (p + 2) // 3
    d1 = (p - 1) // 3
    plus_dimension = 4 * d * d0
    minus_dimension = 4 * d * d1
    positive_identity_trace = Fraction(plus_dimension + minus_dimension, d)
    assert positive_identity_trace == Fraction(8 * p + 4, 3)
    return {
        "prime": p,
        "real_galois_class_count_d_p": d,
        "sector_dimension_d0": d0,
        "sector_dimensions_d1_d2": [d1, d1],
        "per_galois_class_even_block": "2*T_(a,0) plus 2*T_(-a,0)",
        "per_galois_class_odd_block": "T_(a,1),T_(a,2),T_(-a,1),T_(-a,2)",
        "total_even_dimension": plus_dimension,
        "total_odd_dimension": minus_dimension,
        "positive_normalized_trace_of_identity": fraction_record(
            positive_identity_trace
        ),
        "absolute_Lq_trace_coefficient": fraction_record(positive_identity_trace),
        "first_signed_supertrace_moment": fraction_record(Fraction(-6, d)),
    }


def build_moment_control(
    p: int, expected_c2: int, expected_c3: Fraction
) -> dict[str, Any]:
    generator = primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    n1_zero = chronological_zero_count(p, rho, 1)
    n2_zero = chronological_zero_count(p, rho, 2)
    n3_zero = chronological_zero_count(p, rho, 3)
    c1 = traced_moment_from_zero_count(p, 1, n1_zero)
    c2 = traced_moment_from_zero_count(p, 2, n2_zero)
    c3 = traced_moment_from_zero_count(p, 3, n3_zero)
    assert c1 == -6 and c2 == expected_c2 and c3 == expected_c3
    d = (p - 1) // 2
    return {
        "prime": p,
        "rho_order_3": rho,
        "chronological_zero_counts_n1_n2_n3": [n1_zero, n2_zero, n3_zero],
        "galois_traced_moments_C1_C2_C3": [
            fraction_record(value) for value in (c1, c2, c3)
        ],
        "normalized_signed_supertrace_moments_c1_c2_c3": [
            fraction_record(value / d) for value in (c1, c2, c3)
        ],
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relatives = (
        "henon_mu3_galois_norm_rank_obstruction/results/c45_certificate.json",
        "henon_mu3_normalized_root_branch_obstruction/results/c46_certificate.json",
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
    primes = split_primes_through(CONTROL_BOUND)
    blocks = [build_block_control(p) for p in primes]
    moments = [
        build_moment_control(p, c2, c3)
        for p, c2, c3 in zip(MOMENT_CONTROL_PRIMES, EXPECTED_C2, EXPECTED_C3)
    ]
    return {
        "material_passport": {
            "candidate_id": "HCS-C47",
            "project": "henon_mu3_normalized_trace_operator_gate",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact graded block algebra, exact chronological moments, and prime-series comparison; no zero-table data",
        },
        "source_lock": source_lock(project_root),
        "local_operator_algebra": {
            "algebra": "M_p=B(H_p^+) direct_sum B(H_p^-)",
            "positive_trace": "tau_p(A_+ direct_sum A_-)=(Tr A_+ + Tr A_-)/d_p",
            "grading": "Gamma_p=+I on H_p^+ and -I on H_p^-",
            "signed_supertrace": "str_p(A)=tau_p(Gamma_p*A)",
            "block_operator": "W_p in M_p acts on H_p^+ direct_sum H_p^- and is the direct sum over real Galois classes [a] of the exact even and odd Henon sector blocks",
            "moment_identity": "str_p(W_p^n)=c_p,n=C_p,n/d_p for every n>=1",
            "local_determinant_identity": "G_p(z)=exp(str_p(Log(I-z*W_p))) on the origin zero-free branch",
            "positive_trace_warning": "tau_p is positive but str_p is signed; they cannot be interchanged",
            "fuglede_kadison_warning": "a positive FK determinant sees log absolute value and loses the analytic phase of G_p",
        },
        "global_operator_algebra": {
            "algebra": "M=semifinite direct product over split primes with tau=sum_p tau_p",
            "operator": "X_s=direct_sum_p p^(-s)*W_p",
            "exact_Lq_identity": "tau(|X_s|^q)=sum_(p=1 mod 3) ((8p+4)/3)*p^(-q*Re(s))",
            "Lq_criterion": "X_s belongs to L^q(M,tau) iff q*Re(s)>2",
            "compactness_on_hilbert_direct_sum": "X_s is compact iff Re(s)>0",
            "tau_L1_threshold": "L1(M,tau) iff Re(s)>2",
            "tau_L2_threshold": "L2(M,tau) iff Re(s)>1",
            "tau_L3_threshold": "L3(M,tau) iff Re(s)>2/3",
            "tau_L4_threshold": "L4(M,tau) iff Re(s)>1/2",
            "grading_cannot_improve_positive_tau_L1": "|Gamma_p*X_s|=|X_s|",
            "classical_Hilbert_trace_identity": "Tr_H(|X_s|^q)=sum_(p=1 mod 3) d_p*((8p+4)/3)*p^(-q*Re(s))",
            "classical_Schatten_criterion": "X_s belongs to classical S^q(H) iff q*Re(s)>3",
            "classical_trace_class_threshold": "classical S1(H) iff Re(s)>3",
            "classical_Hilbert_Schmidt_threshold": "classical S2(H) iff Re(s)>3/2",
            "classical_determinant_warning": "the classical Hilbert trace does not implement the field-degree-normalized root G",
        },
        "regularized_graded_determinant": {
            "counterterms": "ell_n(s)=sum_p c_p,n*p^(-n*s), n=1,2,3",
            "det4_definition": "det4_tau_gr(I-X_s)=exp(-sum_(n>=4) str_tau(X_s^n)/n)",
            "exact_factorization": "G(s)=exp(-ell_1(s)-ell_2(s)/2-ell_3(s)/3)*det4_tau_gr(I-X_s)",
            "domain": "Re(s)>1/2",
            "minimal_fixed_schatten_order_on_full_domain": 4,
            "unregularized_tau_determinant_domain": "Re(s)>2",
            "determinant_category": "semifinite tau-associated graded regularization, not a classical Fredholm determinant",
            "counterterm_status": "three source-native chronological Galois-supertrace moments, not fitted prefactors",
        },
        "exact_block_controls": blocks,
        "exact_chronological_moment_controls": moments,
        "aggregate_control": {
            "control_bound_inclusive": CONTROL_BOUND,
            "control_primes": list(primes),
            "number_of_block_controls": len(blocks),
            "all_positive_identity_traces_equal_8p_plus_4_over_3": all(
                row["positive_normalized_trace_of_identity"]
                == fraction_record(Fraction(8 * row["prime"] + 4, 3))
                for row in blocks
            ),
            "moment_control_primes": list(MOMENT_CONTROL_PRIMES),
            "C2_ledger": list(EXPECTED_C2),
            "C3_ledger": [fraction_record(value) for value in EXPECTED_C3],
            "all_first_signed_moments_equal_minus_12_over_p_minus_1": all(
                row["normalized_signed_supertrace_moments_c1_c2_c3"][0]
                == fraction_record(Fraction(-12, row["prime"] - 1))
                for row in moments
            ),
        },
        "decisions": {
            "finite_local_normalized_trace_model": "CONSTRUCTED_EXACTLY",
            "positive_trace_and_signed_supertrace_distinguished": "YES",
            "ordinary_global_semifinite_trace_class_on_critical_half_plane": "REFUTED_BY_TAU_L1_THRESHOLD_RE_S_GREATER_THAN_2",
            "fourth_order_regularized_graded_determinant": "CONSTRUCTED_IN_SEMIFINITE_TAU_CATEGORY_ON_RE_S_GREATER_THAN_ONE_HALF",
            "positive_fuglede_kadison_equals_complex_G": "REFUTED_PHASE_IS_LOST",
            "next_large_gate": "C48_IDENTIFY_GEOMETRIC_OR_MOTIVIC_STRUCTURE_OF_c_p_2_AND_COUNTERTERMS",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "canonical L4(M,tau) regularized graded determinant with three exact source-native counterterms realizes the C45 germ on Re(s)>1/2",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_reason": "operator-category realization reaches the half-plane to the right of the Riemann critical abscissa, but no continuation, functional equation, Gamma factor, or Riemann divisor is proved",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "scoped_status": "ROUTE_A_EXPLORATORY_REGULARIZED_GRADED_DETERMINANT",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_self_adjoint_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "unregularized_tau_L1_determinant_claimed_on_Re_s_gt_one_half": False,
            "classical_Fredholm_determinant_claimed_on_Re_s_gt_one_half": False,
            "classical_Schatten_criterion_claimed_qRe_s_gt_2": False,
            "positive_FK_determinant_claimed_equal_to_complex_germ": False,
            "counterterms_claimed_arithmetic_motives": False,
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
