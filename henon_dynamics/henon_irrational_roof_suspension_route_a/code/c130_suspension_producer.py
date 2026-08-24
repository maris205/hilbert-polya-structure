#!/usr/bin/env python3
"""Produce the exact C130 irrational-roof suspension certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results" / "c130_suspension_evidence.json"
PREFIX = 10


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[k:] + word[:k] for k in range(len(word)))


def primitive_representatives(n: int) -> list[str]:
    reps = {
        least_rotation(word)
        for word in itertools.product(range(2), repeat=n)
        if primitive(word)
    }
    return ["".join(str(bit) for bit in word) for word in sorted(reps)]


def canonical_payload(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    u, v = sp.symbols("u v")
    B = sp.ones(2)
    M = B * sp.diag(u, v)
    delta = sp.expand((sp.eye(2) - M).det())
    assert M == sp.Matrix([[u, v], [u, v]])
    assert delta == 1 - u - v
    assert all(entry > 0 for entry in B)

    rows = []
    primitive_total = 0
    rooted_total = 0
    representatives: dict[str, list[str]] = {}
    for n in range(1, PREFIX + 1):
        reps = primitive_representatives(n)
        representatives[str(n)] = reps
        primitive_total += len(reps)
        rooted_total += 2**n
        trace_poly = sp.Poly(sp.expand(sp.trace(M**n)), u, v)
        sectors = []
        for n1 in range(n + 1):
            n0 = n - n1
            coefficient = math.comb(n, n1)
            assert trace_poly.coeff_monomial(u**n0 * v**n1) == coefficient
            sectors.append({"N0": n0, "N1": n1, "multiplicity": coefficient, "roof": f"{n0}+{n1}*sqrt(2)"})
        rows.append({
            "period": n,
            "rooted_closed_words": 2**n,
            "primitive_cycles": len(reps),
            "clock_sector_count": n + 1,
            "trace_sectors": sectors,
        })

    same_sector = ["000111", "001011"]
    for word in same_sector:
        assert word in representatives["6"]
        assert word.count("0") == word.count("1") == 3

    data = {
        "schema": "HCS-C130-v1",
        "candidate_id": "HCS-C130",
        "date_utc": "2026-08-24",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "base": "two-sided full binary shift Sigma_B with B=[[1,1],[1,1]]",
            "mixing_certificate": "B is positive, hence primitive with mixing exponent 1",
            "roof": "tau(x)=1 on symbol 0 and sqrt(2) on symbol 1",
            "suspension": "(Sigma_B x R)/((x,t+tau(x))~(sigma(x),t))",
            "clock": "continuous suspension time; base return count remains explicit",
            "normalization": "unweighted full-shift transitions and the literal roof pair (1,sqrt(2))",
            "determinant_convention": "d_tau(s)=det(I-M(exp(-s),exp(-sqrt(2)*s)))",
            "prefix": "periods 1 through 10 are replay only; theorem has no cutoff",
            "precision": "exact integers, formal bivariate polynomials, and the algebraic basis {1,sqrt(2)}",
            "allowed_data": "the frozen adjacency matrix and roof pair only",
            "forbidden_data": "external zero tables, prime tables, arithmetic local factors, root numbers, and Route-B inputs",
        },
        "frozen_model": {
            "adjacency_B": [[1, 1], [1, 1]],
            "roof_values": ["1", "sqrt(2)"],
            "bivariate_transfer_matrix": [["u", "v"], ["u", "v"]],
            "bivariate_determinant": "Delta(u,v)=det(I-M(u,v))=1-u-v",
            "one_variable_specialization": "u=exp(-s), v=exp(-sqrt(2)*s)",
            "exponential_polynomial": "d_tau(s)=1-exp(-s)-exp(-sqrt(2)*s)",
            "zeta_specialization": "zeta_tau(s)=1/d_tau(s)",
            "entropy_characterization": "h is the unique positive root of exp(-h)+exp(-sqrt(2)*h)=1",
        },
        "all_period_identity": {
            "trace_formula_bivariate": "Tr(M(u,v)^n)=(u+v)^n=sum_{k=0}^n binom(n,k)u^(n-k)v^k",
            "trace_formula_specialized": "Tr(M(s)^n)=sum_{k=0}^n binom(n,k)exp(-s*((n-k)+k*sqrt(2)))",
            "log_determinant": "-log Delta(u,v)=sum_{n>=1} Tr(M(u,v)^n)/n",
            "primitive_euler_identity": "Delta(u,v)=product_[gamma primitive](1-u^N0(gamma)*v^N1(gamma))",
            "suspension_euler_identity": "d_tau(s)=product_[gamma primitive](1-exp(-s*ell(gamma)))",
            "primitive_length": "ell(gamma)=N0(gamma)+sqrt(2)*N1(gamma)",
            "convergence_domain": "absolute for Re(s)>h; d_tau is entire and zeta_tau is meromorphic by the explicit specialization",
            "all_period": True,
            "replay_cutoff_is_not_theorem_cutoff": True,
        },
        "clock_sector_separation": {
            "basis": ["1", "sqrt(2)"],
            "q_linear_independence": True,
            "sector_injectivity": "a+b*sqrt(2)=c+d*sqrt(2) for integers implies (a,b)=(c,d)",
            "consequence": "different population vectors (N0,N1) never collide in suspension time, even across base periods",
            "not_orbit_injectivity": "distinct primitive necklaces can share one population vector and therefore one roof length",
            "same_sector_primitive_example_period_6": same_sector,
            "same_sector_counts": {"N0": 3, "N1": 3},
            "same_sector_roof": "3+3*sqrt(2)",
            "imaginary_period_statement": "d_tau(s+iT)=d_tau(s) for all s forces T=0",
            "imaginary_period_proof": "coefficient separation gives exp(-iT)=exp(-i*sqrt(2)*T)=1; irrationality of sqrt(2) leaves only T=0",
        },
        "rational_roof_control": {
            "roof_values": ["1", "2"],
            "specialized_determinant": "d_rat(s)=1-exp(-s)-exp(-2*s)",
            "lattice_variable": "q=exp(-s)",
            "lattice_polynomial": "d_rat=1-q-q^2",
            "cross_sector_collision": {
                "orbit_a": "second repetition of primitive fixed orbit [0]",
                "counts_a": {"N0": 2, "N1": 0},
                "orbit_b": "primitive fixed orbit [1]",
                "counts_b": {"N0": 0, "N1": 1},
                "common_roof_time": 2,
            },
            "periodicity": "d_rat(s+2*pi*i)=d_rat(s)",
            "periodicity_recovered": True,
            "control_scope": "changes only the roof pair; base shift and determinant convention stay fixed",
        },
        "replay_prefix": {
            "period_limit": PREFIX,
            "rows": rows,
            "primitive_representatives": representatives,
            "rooted_closed_words_total": rooted_total,
            "primitive_cycles_total": primitive_total,
            "clock_sectors_total": sum(n + 1 for n in range(1, PREFIX + 1)),
        },
        "progress_and_boundary": {
            "progress": "an all-period primitive-orbit determinant now carries an intrinsically nonlattice continuous clock with exact sector separation",
            "internal_obstruction": "the determinant aggregates distinct primitive necklaces that have the same symbol counts",
            "target_obstruction": "no frozen external divisor, functional equation, counting law, or arithmetic interpretation is compared",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_SUSPENSION_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2_qualification": "EXACT_SOURCE DETERMINANT AND EULER_TRACE IDENTITY BUT NO FROZEN TARGET DIVISOR MATCH",
            "A3_qualification": "NO TARGET FUNCTIONAL EQUATION GAMMA FACTOR COUNTING LAW OR CONTINUATION COMPARISON",
            "A4_qualification": "NO NATURAL SELF_ADJOINT UNITARY SCATTERING OR HAMILTONIAN LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "an arithmetic Euler product or local factorization",
            "a root number, automorphy statement, or functional equation",
            "a match to any target zero or pole divisor",
            "orbit-level injectivity inside a fixed population sector",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = hashlib.sha256(canonical_payload(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C130_EXACT_EVIDENCE_PASS",
        "evidence_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "payload_sha256": data["payload_sha256"],
        "rooted_words_through_10": data["replay_prefix"]["rooted_closed_words_total"],
        "primitive_cycles_through_10": data["replay_prefix"]["primitive_cycles_total"],
        "clock_sectors_through_10": data["replay_prefix"]["clock_sectors_total"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
