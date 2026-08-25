#!/usr/bin/env python3
"""Produce the exact HCS-C149 finite-skeleton certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c149_skeleton_evidence.json"
CYCLE_LENGTHS = (1, 2, 3, 5)
MAX_PERIOD = 60
ZETA_DEGREE = 30


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    factors = 0
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            factors += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        factors += 1
    return -1 if factors & 1 else 1


def fixed_count(n: int) -> int:
    return sum(length for length in CYCLE_LENGTHS if n % length == 0)


def exact_points(n: int) -> int:
    return sum(mobius(n // d) * fixed_count(d) for d in divisors(n))


def zeta_coefficients(limit: int) -> list[int]:
    coefficients = [0] * (limit + 1)
    coefficients[0] = 1
    for length in CYCLE_LENGTHS:
        updated = [0] * (limit + 1)
        for degree, value in enumerate(coefficients):
            if not value:
                continue
            for copies in range((limit - degree) // length + 1):
                updated[degree + copies * length] += value
        coefficients = updated
    return coefficients


def period_certificate(period: int) -> dict:
    k = period.bit_length() + 1
    if k % 2 == 0:
        k += 1
    d = period * ((1 << k) - 1)
    b = d.bit_length()
    assert d % period == 0 and d.bit_count() == k and k % 2 == 1
    return {
        "putative_period": period,
        "odd_exponent_k": k,
        "multiple_d": d,
        "popcount_d": d.bit_count(),
        "tm_bit_at_zero": 0,
        "tm_bit_at_d": d.bit_count() & 1,
        "forbidden_window_length": 1 << (b + 1),
    }


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    cycle_rows = []
    transition = {}
    for length in CYCLE_LENGTHS:
        labels = [f"tag_{length}:{j}" for j in range(length)]
        for j, label in enumerate(labels):
            transition[label] = labels[(j + 1) % length]
        cycle_rows.append({
            "length": length,
            "tag": f"tag_{length}",
            "point_labels": labels,
            "least_periods": [length] * length,
            "primitive_cycles": 1,
        })

    ledger = []
    for n in range(1, MAX_PERIOD + 1):
        exact = exact_points(n)
        assert exact >= 0 and exact % n == 0
        fixed_labels = [
            f"tag_{length}:{j}"
            for length in CYCLE_LENGTHS if n % length == 0
            for j in range(length)
        ]
        ledger.append({
            "period_n": n,
            "fixed_points": len(fixed_labels),
            "fixed_point_labels": fixed_labels,
            "exact_period_points": exact,
            "primitive_cycles": exact // n,
        })

    primitive = [
        {"least_period": n, "exact_period_points": exact_points(n), "primitive_cycles": exact_points(n) // n}
        for n in range(1, max(CYCLE_LENGTHS) + 1)
        if exact_points(n)
    ]
    assert [(r["least_period"], r["primitive_cycles"]) for r in primitive] == [(1, 1), (2, 1), (3, 1), (5, 1)]

    data = {
        "schema": "HCS-C149-v1",
        "candidate_id": "HCS-C149",
        "date_utc": "2026-08-25",
        "source_commit": "2d4e6211a254ef49d87718569d23466f4c6dcf4c",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "compact topological disjoint union Y=X_TM sqcup C_1 sqcup C_2 sqcup C_3 sqcup C_5 with tagged finite cycles",
            "map": "the shift on X_TM and cyclic successor on each tagged C_ell",
            "clock": "one iterate of the componentwise map",
            "normalization": "Fix_Y(n) counts fixed points; primitive cycles are exact-period points divided by their least period",
            "zeta_convention": "zeta_Y(z)=exp(sum_(n>=1) Fix_Y(n) z^n/n)",
            "cutoff": "theorems hold for every n>=1; explicit replay ledger uses 1<=n<=60 and zeta degree<=30",
            "allowed_data": "the Thue--Morse substitution and the declared tagged cycles of lengths 1,2,3,5",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, Hilbert--Polya operators, and Route-B inputs",
        },
        "thue_morse_component": {
            "substitution": {"0": "01", "1": "10"},
            "status": "NONEMPTY_MINIMAL_UNIFORMLY_RECURRENT_APERIODIC_COMPONENT",
            "periodic_points": 0,
            "all_positive_fixed_counts_zero": True,
            "proof_certificate": "for each p choose odd k>bit_length(p), d=p(2^k-1), and b=bit_length(d); popcount(d)=k, and every length-2^(b+1) interval contains a full b-aligned block whose offsets 0,d are p-congruent and have opposite Thue--Morse bits",
            "period_certificate_limit": 32,
            "period_certificates": [period_certificate(p) for p in range(1, 33)],
        },
        "finite_skeleton": {
            "cycle_lengths": list(CYCLE_LENGTHS),
            "total_points": sum(CYCLE_LENGTHS),
            "cycle_rows": cycle_rows,
            "successor_table": transition,
            "topology": "finite tagged discrete union, disjoint from X_TM",
        },
        "all_period_theorem": {
            "fixed_count_formula": "Fix_Y(n)=sum_(ell in {1,2,3,5}, ell|n) ell for every n>=1",
            "primitive_skeleton": [{"least_period": length, "primitive_cycles": 1} for length in CYCLE_LENGTHS],
            "no_other_primitive_cycles": True,
            "artin_mazur_zeta": "1/((1-z)(1-z^2)(1-z^3)(1-z^5))",
            "formal_derivation": "sum_(n>=1) Fix_Y(n)z^n/n=sum_ell sum_(q>=1) z^(ell q)/q=-sum_ell log(1-z^ell)",
            "minimality_obstruction": "every nonempty attached tagged cycle is a nonempty proper closed invariant subset of Y, so Y is not minimal",
            "general_finite_attachment_statement": "attaching any nonempty finite union of periodic cycles by topological disjoint union to a nonempty aperiodic component destroys minimality",
        },
        "finite_replay": {
            "period_limit": MAX_PERIOD,
            "rows": ledger,
            "fixed_count_sum": sum(row["fixed_points"] for row in ledger),
            "exact_period_point_sum": sum(row["exact_period_points"] for row in ledger),
            "primitive_cycle_sum": sum(row["primitive_cycles"] for row in ledger),
            "zeta_degree_limit": ZETA_DEGREE,
            "zeta_coefficients": zeta_coefficients(ZETA_DEGREE),
        },
        "progress_and_boundary": {
            "progress": "replaces the Thue--Morse periodic-orbit vacuum by a completely controlled nonempty finite primitive skeleton with an all-period source zeta",
            "structural_cost": "the finite attachment necessarily destroys minimality; it is a declared disjoint-union design, not an intrinsic orbit creation mechanism inside X_TM",
            "route_a_obstruction": "a freely attached finite rational factor has no target divisor, global analytic comparison, arithmetic content, or natural operator lift",
        },
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "A1_qualification": "DECLARED_FINITE_DISJOINT_ATTACHMENT_NOT_INTRINSIC_TO_THE_MINIMAL_THUE_MORSE_COMPONENT",
            "A2_qualification": "ELEMENTARY_FINITE_RATIONAL_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
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
            "that the attached periodic cycles belong to the Thue--Morse subshift",
            "that the disjoint union remains minimal or almost minimal",
            "an arithmetic Euler product or local factorization",
            "a target divisor, functional equation, or counting-law match",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = sha256(payload_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C149_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "period_rows": len(data["finite_replay"]["rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
