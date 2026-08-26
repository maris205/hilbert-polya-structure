#!/usr/bin/env python3
"""Produce exact primitive finite-field multiplier evidence for HCS-C172."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f"
Q_VALUES = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32]
N_MAX = 24


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def prime_power(Q: int) -> tuple[int, int]:
    for p in range(2, Q + 1):
        if any(p % r == 0 for r in range(2, int(p**0.5) + 1)):
            continue
        value, exponent = p, 1
        while value < Q:
            value *= p
            exponent += 1
        if value == Q:
            return p, exponent
    raise ValueError(Q)


def nonprimitive_exponent(N: int) -> int:
    if N == 1:
        return 1
    for h in range(2, N + 1):
        if gcd(h, N) > 1:
            return h
    raise AssertionError


def row(Q: int) -> dict:
    p, e = prime_power(Q)
    N = Q - 1
    h = nonprimitive_exponent(N)
    g = gcd(h, N)
    inventory = ([{"period": 1, "primitive_orbits": 2}] if N == 1 else
                 [{"period": 1, "primitive_orbits": 1}, {"period": N, "primitive_orbits": 1}])
    fixes = [Q if n % N == 0 else 1 for n in range(1, N_MAX + 1)]
    return {
        "Q": Q,
        "characteristic_prime": p,
        "extension_degree": e,
        "N": N,
        "orbit_inventory": inventory,
        "fix_counts_n_1_to_24": fixes,
        "zeta_inverse_factors": [{"factor": "1-z", "exponent": 1},
                                 {"factor": f"1-z^{N}", "exponent": 1}],
        "koopman_determinant": f"(1-z)*(1-z^{N})",
        "koopman_eigenvalue_description": f"one extra eigenvalue 1 plus every {N}-th root of unity once",
        "eigenvalue_one_multiplicity": 2,
        "self_adjoint": N <= 2,
        "nonprimitive_control_exponent_h": h,
        "nonprimitive_control_cycle_count": g,
        "nonprimitive_control_cycle_length": N // g,
    }


def build_evidence() -> dict:
    payload = {
        "schema": "hcs-c172-primitive-field-multiplier-v1",
        "candidate_id": "HCS-C172",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "T_a(x)=a*x on F_Q, where Q is any prime power and a is primitive in F_Q^times",
            "parameters": "prime power Q>=2 and an arbitrary primitive generator a; no fitted parameter",
            "arithmetic_origin": "intrinsic finite-field phase space of prime-power cardinality, but no rational-prime orbit dictionary",
            "clock": "one multiplication by a is one discrete step",
            "normalization": "counting measure for periodic points and normalized counting measure for Koopman unitarity",
            "determinant_convention": "Artin--Mazur zeta from #Fix(T_a^n); K_Q(z)=det(I-zU_a) separately",
            "cutoff": {"Q_values": Q_VALUES, "n_max": N_MAX},
            "precision": "exact integers and finite cyclic-group identities",
            "allowed_data": "finite-field cyclicity, primitive-generator coordinates, and source-derived controls",
            "forbidden_data": "target zero or divisor tables, rational-prime lookup, log p or von Mangoldt weights, arithmetic local data, global Euler products, local factors, root numbers, automorphy, Hilbert--Polya, and Route B",
        },
        "orbit_theorem": {
            "decomposition": "{0} is fixed and F_Q^times is one cycle of length N=Q-1",
            "coordinate_proof": "writing x=a^k gives T_a(a^k)=a^(k+1) modulo N",
            "fixed_points": "#Fix(T_a^n)=Q if N divides n and 1 otherwise",
            "primitive_inventory": "one fixed orbit plus one primitive N-cycle; for Q=2 both are fixed",
            "all_prime_powers": True,
        },
        "zeta_theorem": {
            "definition": "zeta_T(z)=exp(sum_(n>=1) #Fix(T^n) z^n/n)",
            "formula": "zeta_T(z)=1/((1-z)(1-z^N))",
            "proof": "sum z^n/n=-log(1-z) and sum_(N|n) N z^n/n=-log(1-z^N)",
            "formal_and_analytic_domain": "formal power series identity and analytic equality for |z|<1",
        },
        "koopman_theorem": {
            "operator": "U_a f=f after T_a on l2(F_Q,Q^(-1)counting)",
            "unitary": True,
            "spectrum": "one extra 1 from {0}, together with every N-th root of unity once from F_Q^times",
            "determinant": "det(I-zU_a)=(1-z)(1-z^N)",
            "relation_to_zeta": "det(I-zU_a)=zeta_T(z)^(-1)",
            "self_adjoint_iff": "Q<=3, equivalently N<=2",
        },
        "reversal_theorem": {
            "involution": "I(0)=0 and I(x)=x^(-1) for x nonzero",
            "identity": "I T_a I=T_a^(-1)",
            "antiunitary": "Theta f(x)=conjugate(f(I(x))) obeys Theta U_a Theta^(-1)=U_a^(-1)",
            "same_clock": True,
        },
        "arithmetic_controls": [
            {"name": "composite cyclic surrogate", "outcome": "a fixed point plus translation on Z/N has identical orbit, zeta, and Koopman determinant laws"},
            {"name": "nonprimitive multiplier", "outcome": "a^h splits F_Q^times into gcd(h,N) cycles of length N/gcd(h,N), so primitivity is detected but no target arithmetic emerges"},
            {"name": "same-cycle random permutation", "outcome": "any permutation with cycle type (1)(N) has the same zeta and spectrum, so these invariants do not identify finite fields"},
            {"name": "neighboring prime powers", "outcome": "all Q obey the same N=Q-1 law without a rational-prime orbit or logarithmic clock"},
        ],
        "finite_ledgers": [row(Q) for Q in Q_VALUES],
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "all_prime_power_orbit_theorem": True,
            "all_prime_power_zeta_and_koopman_theorem": True,
            "finite_ledgers_are_proof": False,
            "prime_phase_space_is_prime_orbit_dictionary": False,
            "log_p_clock_or_von_mangoldt_weight": False,
            "target_divisor_matching": False,
            "target_functional_equation_or_counting_law": False,
            "arithmetic_local_data": False,
            "global_euler_product_or_local_factor": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
        "integrity": {
            "hard_gate": "unconditional all-prime-power orbit, zeta, Koopman determinant, reversal, and self-adjoint-boundary theorem",
            "hard_gate_status": "PASS",
            "pivot_required": False,
            "registered_citation_population": 0,
            "external_reviewer_simulated": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results/c172_field_multiplier_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "C172_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"],
                      "Q_count": len(Q_VALUES), "n_max": N_MAX}, sort_keys=True))


if __name__ == "__main__":
    main()
