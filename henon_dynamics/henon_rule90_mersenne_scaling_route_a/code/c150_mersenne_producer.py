#!/usr/bin/env python3
"""Produce the exact HCS-C150 Mersenne Rule-90 scaling certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c150_rule90_mersenne_evidence.json"
MAX_R = 8
POWER_CONTROL_MAX_S = 8


def degree(polynomial: int) -> int:
    return polynomial.bit_length() - 1


def multiply(left: int, right: int) -> int:
    result = 0
    while right:
        if right & 1:
            result ^= left
        right >>= 1
        left <<= 1
    return result


def power(base: int, exponent: int) -> int:
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def remainder(dividend: int, divisor: int) -> int:
    divisor_degree = degree(divisor)
    while dividend and degree(dividend) >= divisor_degree:
        dividend ^= divisor << (degree(dividend) - divisor_degree)
    return dividend


def polynomial_gcd(left: int, right: int) -> int:
    while right:
        left, right = right, remainder(left, right)
    return left


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    count = 0
    p = 2
    remaining = n
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        if exponent > 1:
            return 0
        if exponent == 1:
            count += 1
        p += 1
    if remaining > 1:
        count += 1
    return -1 if count & 1 else 1


def gcd_degree(length: int, time: int) -> int:
    spatial = (1 << length) | 1
    cleared = power((1 << 2) | 1, time) ^ (1 << time)
    return degree(polynomial_gcd(spatial, cleared))


def fixed_count(length: int, time: int) -> int:
    return 1 << gcd_degree(length, time)


def exact_points(length: int, time: int) -> int:
    return sum(mobius(time // d) * fixed_count(length, d) for d in divisors(time))


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    family = []
    divisor_cells = 0
    for r in range(1, MAX_R + 1):
        length = (1 << r) - 1
        period_rows = []
        for n in divisors(length):
            fixed = fixed_count(length, n)
            exact = exact_points(length, n)
            assert exact >= 0 and exact % n == 0
            period_rows.append({
                "period_n": n,
                "gcd_degree": fixed.bit_length() - 1,
                "fixed_points": fixed,
                "exact_period_points": exact,
                "primitive_cycles": exact // n,
            })
        divisor_cells += len(period_rows)
        periodic_total = sum(row["exact_period_points"] for row in period_rows)
        assert periodic_total == 1 << (length - 1)
        family.append({
            "exponent_r": r,
            "ring_length_L": length,
            "state_space_size": 1 << length,
            "kernel_dimension": 1,
            "image_dimension": length - 1,
            "periodic_points": periodic_total,
            "periodic_fraction_numerator": 1,
            "periodic_fraction_denominator": 2,
            "transient_points": 1 << (length - 1),
            "entry_time_bound": 1,
            "restriction_order_divides": length,
            "divisor_period_rows": period_rows,
        })

    controls = []
    for s in range(1, POWER_CONTROL_MAX_S + 1):
        length = 1 << s
        exponent = length // 2
        fixed = [fixed_count(length, n) for n in range(1, 17)]
        assert fixed == [1] * 16
        controls.append({
            "exponent_s": s,
            "ring_length_L": length,
            "annihilating_iterate": exponent,
            "identity": f"a^(2^{s-1})=x^(2^{s-1})+x^(-2^{s-1})=0 modulo x^{length}-1",
            "only_periodic_state": "zero",
            "fixed_counts_period_1_through_16": fixed,
        })

    data = {
        "schema": "HCS-C150-v1",
        "candidate_id": "HCS-C150",
        "date_utc": "2026-08-25",
        "source_commit": "2d4e6211a254ef49d87718569d23466f4c6dcf4c",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "Rule 90, multiplication by a=x+x^{-1} on R_L=F_2[x,x^{-1}]/(x^L-1)",
            "family": "Mersenne circumferences L_r=2^r-1 for every r>=1",
            "clock": "one Rule-90 update; temporal period n is measured in update ticks",
            "normalization": "fixed configurations, exact-period configurations by Mobius inversion, then primitive cycles by division by n",
            "cutoff": "the structural theorem holds for every r>=1; exact divisor ledgers use 1<=r<=8 and power-of-two controls 1<=s<=8",
            "precision": "exact F_2 polynomial arithmetic and exact integers",
            "allowed_data": "the Rule-90 local rule and family lengths derived from powers of two",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, Hilbert--Polya operators, and Route-B inputs",
        },
        "mersenne_theorem": {
            "frobenius_identity": "a^(2^r)=x^(2^r)+x^(-2^r)=x+x^(-1)=a in R_(2^r-1)",
            "equivalent_identity": "a^(L_r+1)=a",
            "kernel_statement": "ker(a) has dimension one and im(a) has dimension L_r-1",
            "kernel_proof": "x*a=x^2+1=(x+1)^2; x^L+1 is squarefree for odd L and has x+1 as a simple factor, so gcd has degree one",
            "image_periodicity": "for y=a u, a^L y=a^(L+1)u=a u=y; hence a restricts to a permutation of order dividing L on im(a)",
            "eventual_image": "every state enters im(a) after one update, and a periodic state already belongs to im(a)",
            "periodic_set_equals_image": True,
            "periodic_fraction": "exactly 1/2 for every r>=1",
            "all_cycle_periods_divide_L": True,
        },
        "fixed_and_primitive_formula": {
            "fixed_count": "Fix_L(n)=2^deg(gcd(x^L+1,(x^2+1)^n+x^n))",
            "exact_period": "P_L(n)=sum_(d|n) mu(n/d) Fix_L(d)",
            "primitive_cycles": "C_L(n)=P_L(n)/n",
            "support": "P_L(n)=C_L(n)=0 unless n divides L for L=2^r-1",
        },
        "mersenne_replay": {
            "r_limit": MAX_R,
            "family_rows": family,
            "divisor_period_cell_count": divisor_cells,
            "periodic_point_sum": sum(row["periodic_points"] for row in family),
            "primitive_cycle_sum": sum(cell["primitive_cycles"] for row in family for cell in row["divisor_period_rows"]),
        },
        "power_of_two_negative_control": {
            "statement": "for L=2^s, a^(2^(s-1))=0, so Rule 90 is nilpotent and zero is its only periodic state",
            "proof": "Frobenius gives a^(2^(s-1))=x^(2^(s-1))+x^(-2^(s-1)); the two monomials coincide modulo x^(2^s)-1 and cancel in F_2",
            "rows": controls,
        },
        "progress_and_boundary": {
            "progress": "upgrades a bounded two-clock ledger to an all-r Mersenne scaling theorem with exact one-step transient/periodic decomposition and divisor-resolved cycles",
            "matched_control": "the neighboring power-of-two scaling family is nilpotent, demonstrating arithmetic sensitivity of circumference without importing arithmetic local data",
            "route_a_obstruction": "the family supplies exact finite-volume dynamics but no frozen target divisor, analytic comparison, arithmetic factorization, or natural operator lift",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_R_EXACT_MERSENNE_PERIODIC_IMAGE_WITH_DIVISOR_RESOLVED_PRIMITIVE_CYCLES",
            "A2_qualification": "SCALING_FAMILY_OF_FINITE_POLYNOMIAL_COUNTS_WITH_NO_TARGET_DIVISOR_COMPARISON",
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
            "that every divisor of L occurs as a cycle period",
            "an infinite-volume determinant or thermodynamic limit",
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
    print(json.dumps({"status": "C150_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "family_rows": len(data["mersenne_replay"]["family_rows"]), "divisor_cells": data["mersenne_replay"]["divisor_period_cell_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
