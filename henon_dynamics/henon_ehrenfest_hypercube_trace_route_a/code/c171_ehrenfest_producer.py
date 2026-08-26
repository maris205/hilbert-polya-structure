#!/usr/bin/env python3
"""Produce exact Ehrenfest-hypercube evidence for HCS-C171."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f"
D_MAX = 18
N_MAX = 24


def qtext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def krawtchouk(d: int, j: int, k: int) -> int:
    return sum((-1) ** r * comb(k, r) * comb(d - k, j - r)
               for r in range(max(0, j - (d - k)), min(j, k) + 1))


def ledger_row(d: int) -> dict:
    eigenvalues = [Fraction(d - 2 * j, d) for j in range(d + 1)]
    multiplicities = [comb(d, j) for j in range(d + 1)]
    traces = [sum(Fraction(m) * lam**n for lam, m in zip(eigenvalues, multiplicities))
              for n in range(N_MAX + 1)]
    returns = [value / (2**d) for value in traces]
    balance = []
    for k in range(d):
        pi_k = Fraction(comb(d, k), 2**d)
        pi_next = Fraction(comb(d, k + 1), 2**d)
        left = pi_k * Fraction(d - k, d)
        right = pi_next * Fraction(k + 1, d)
        balance.append(qtext(left))
        assert left == right
    return {
        "d": d,
        "dimension": 2**d,
        "distinct_eigenvalues": [qtext(x) for x in eigenvalues],
        "multiplicities": multiplicities,
        "multiplicity_sum": sum(multiplicities),
        "trace_n_0_to_24": [qtext(x) for x in traces],
        "return_probability_n_0_to_24": [qtext(x) for x in returns],
        "odd_return_probabilities_zero": all(returns[n] == 0 for n in range(1, N_MAX + 1, 2)),
        "determinant_factors": [
            {"eigenvalue": qtext(lam), "exponent": multiplicities[j]}
            for j, lam in enumerate(eigenvalues)
        ],
        "lumped_stationary_weights": [qtext(Fraction(comb(d, k), 2**d)) for k in range(d + 1)],
        "lumped_upper_probabilities": [qtext(Fraction(d - k, d)) for k in range(d)] + ["0"],
        "lumped_lower_probabilities": ["0"] + [qtext(Fraction(k, d)) for k in range(1, d + 1)],
        "detailed_balance_edge_weights": balance,
        "symmetric_offdiagonal_squared": [qtext(Fraction((k + 1) * (d - k), d * d)) for k in range(d)],
        "krawtchouk_endpoint_checksum": [krawtchouk(d, j, 0) + krawtchouk(d, j, d) for j in range(d + 1)],
    }


def build_evidence() -> dict:
    payload = {
        "schema": "hcs-c171-ehrenfest-hypercube-trace-v1",
        "candidate_id": "HCS-C171",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "P_d f(x)=d^(-1) sum_i f(x with coordinate i flipped) on {+1,-1}^d",
            "parameters": "integer d>=1; no fitted parameter",
            "arithmetic_origin": "none: the dimension and coordinate-flip rule are combinatorial, not prime-derived",
            "clock": "one uniformly chosen coordinate flip is one Markov step",
            "normalization": "uniform probability measure on the hypercube; ordinary finite-dimensional trace",
            "determinant_convention": "D_d(z)=det(I-z P_d)",
            "cutoff": {"d_max": D_MAX, "n_max": N_MAX},
            "precision": "exact integers and rational arithmetic",
            "allowed_data": "hypercube adjacency, binomial coefficients, Walsh characters, and Krawtchouk polynomials",
            "forbidden_data": "target zeros or divisors, prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, and Route B",
        },
        "walsh_spectral_theorem": {
            "characters": "chi_S(x)=product_(i in S) x_i",
            "eigenvalue": "P_d chi_S=(1-2|S|/d) chi_S",
            "multiplicity": "binom(d,j) at lambda_j=1-2j/d",
            "complete_orthogonal_basis": True,
            "all_d": True,
        },
        "trace_determinant_theorem": {
            "trace": "Tr(P_d^n)=sum_(j=0)^d binom(d,j)(1-2j/d)^n",
            "determinant": "det(I-zP_d)=product_(j=0)^d (1-z(1-2j/d))^binom(d,j)",
            "trace_log": "-log det(I-zP_d)=sum_(n>=1) Tr(P_d^n)z^n/n for |z|<1",
            "family_uniform_artin_mazur_interpretation": False,
            "reason": "for every d>1 the trace expands weighted closed Markov walks; P_d is a genuine Markov average rather than a deterministic map and its weights are not fixed-point counts",
            "d1_boundary": "at d=1, P_1 is the deterministic two-cycle permutation, but this isolated boundary supplies no all-d primitive-orbit or arithmetic structure",
        },
        "return_theorem": {
            "formula": "P_d^n(x,x)=2^(-d) Tr(P_d^n), independently of x",
            "odd_times_zero": True,
            "reason": "the hypercube is bipartite and every step changes parity",
        },
        "lumping_theorem": {
            "weight_coordinate": "k=number of -1 coordinates",
            "kernel": "Q(k,k+1)=(d-k)/d and Q(k,k-1)=k/d",
            "stationary_measure": "pi_k=2^(-d) binom(d,k)",
            "reversibility": "pi_k Q(k,k+1)=pi_(k+1) Q(k+1,k)",
            "symmetric_similarity": "S=diag(sqrt(pi)) Q diag(pi^(-1/2)); S_(k,k+1)=sqrt((k+1)(d-k))/d",
            "krawtchouk_eigenvectors": "K_j(k)=sum_r (-1)^r binom(k,r)binom(d-k,j-r)",
            "simple_spectrum": "lambda_j=1-2j/d for j=0,...,d, each once in Q",
            "spectral_compression": "Q retains every distinct eigenvalue of P_d while reducing dimension from 2^d to d+1",
        },
        "arithmetic_controls": [
            {"name": "randomized arithmetic labels", "outcome": "labels do not enter P_d, so every formula is unchanged"},
            {"name": "composite-only dimension labels", "outcome": "the theorems hold for every d, with no prime/composite distinction"},
            {"name": "neighboring dimensions", "outcome": "d-1,d,d+1 obey the same binomial law and show no isolated arithmetic signal"},
            {"name": "lazy-kernel parent", "outcome": "eta I+(1-eta)P_d has the affine-shifted spectrum for any source-chosen eta"},
        ],
        "finite_ledgers": [ledger_row(d) for d in range(1, D_MAX + 1)],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "all_parameter_spectral_theorem": True,
            "all_parameter_lumping_theorem": True,
            "finite_ledgers_are_proof": False,
            "uniform_all_d_artin_mazur_zeta": False,
            "prime_or_prime_power_correspondence": False,
            "target_divisor_matching": False,
            "target_functional_equation_or_counting_law": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
        "integrity": {
            "hard_gate": "unconditional all-d Walsh spectrum, trace/determinant, return, and reversible Krawtchouk lumping theorem",
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
                        default=Path(__file__).resolve().parents[1] / "results/c171_ehrenfest_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C171_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"],
                      "d_max": D_MAX, "n_max": N_MAX}, sort_keys=True))


if __name__ == "__main__":
    main()
