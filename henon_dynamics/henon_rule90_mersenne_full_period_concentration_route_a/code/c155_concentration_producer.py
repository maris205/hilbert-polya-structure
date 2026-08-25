#!/usr/bin/env python3
"""Produce the exact HCS-C155 Rule-90 concentration certificate."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c155_rule90_concentration_evidence.json"
SOURCE_COMMIT = "506dead810d67fa58fa7c42b2d9a09bfae161059"
MIN_R = 2
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


def integer_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    signs = 0
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent > 1:
            return 0
        signs += exponent
        p += 1
    if n > 1:
        signs += 1
    return -1 if signs & 1 else 1


def gcd_degree(length: int, time: int) -> int:
    spatial = (1 << length) | 1
    cleared = power((1 << 2) | 1, time) ^ (1 << time)
    return degree(polynomial_gcd(spatial, cleared))


def fixed_count(length: int, time: int) -> int:
    return 1 << gcd_degree(length, time)


def exact_points(length: int, time: int) -> int:
    return sum(mobius(time // d) * fixed_count(length, d) for d in divisors(time))


def fraction_record(numerator: int, denominator: int) -> dict:
    value = Fraction(numerator, denominator)
    return {"numerator": value.numerator, "denominator": value.denominator}


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    family = []
    divisor_cells = 0
    proper_time_cells = 0
    for r in range(MIN_R, MAX_R + 1):
        length = (1 << r) - 1
        period_rows = []
        for n in divisors(length):
            fixed = fixed_count(length, n)
            exact = exact_points(length, n)
            assert exact >= 0 and exact % n == 0
            period_rows.append({
                "period_n": n,
                "gcd_degree": gcd_degree(length, n),
                "fixed_points": fixed,
                "exact_period_points": exact,
                "primitive_cycles": exact // n,
            })
        divisor_cells += len(period_rows)
        periodic_points = 1 << (length - 1)
        assert sum(row["exact_period_points"] for row in period_rows) == periodic_points

        dimension_rows = []
        spectrum = Counter()
        for time in range(1, length):
            d = integer_gcd(time, length)
            dimension = gcd_degree(length, time)
            divisor_dimension = gcd_degree(length, d)
            assert dimension == divisor_dimension and dimension <= 2 * d
            dimension_rows.append({
                "time_j": time,
                "gcd_j_L": d,
                "fixed_dimension": dimension,
                "divisor_fixed_dimension": divisor_dimension,
                "two_d_bound": 2 * d,
            })
            spectrum[dimension] += 1
        proper_time_cells += len(dimension_rows)

        largest_proper_divisor = divisors(length)[-2]
        max_dimension = max(row["fixed_dimension"] for row in dimension_rows)
        union_bound_points = sum(1 << row["fixed_dimension"] for row in dimension_rows)
        crude_union_bound_points = (length - 1) * (1 << (2 * largest_proper_divisor))
        assert largest_proper_divisor * 3 <= length
        assert max_dimension <= 2 * largest_proper_divisor
        assert union_bound_points <= crude_union_bound_points

        full_period_points = period_rows[-1]["exact_period_points"]
        nonfull_points = periodic_points - full_period_points
        assert nonfull_points <= union_bound_points
        total_cycles = sum(row["primitive_cycles"] for row in period_rows)
        burnside_numerator = periodic_points + union_bound_points
        assert burnside_numerator % length == 0
        assert total_cycles == burnside_numerator // length

        family.append({
            "exponent_r": r,
            "ring_length_L": length,
            "periodic_image_points": periodic_points,
            "image_dimension": length - 1,
            "restriction_order_divides_L": True,
            "divisor_period_rows": period_rows,
            "proper_time_dimension_rows": dimension_rows,
            "fixed_dimension_spectrum": [{"dimension": dimension, "proper_times": count} for dimension, count in sorted(spectrum.items())],
            "largest_proper_divisor": largest_proper_divisor,
            "maximum_proper_fixed_dimension": max_dimension,
            "uniform_dimension_bound": 2 * largest_proper_divisor,
            "full_period_points": full_period_points,
            "nonfull_periodic_points": nonfull_points,
            "full_period_state_probability": fraction_record(full_period_points, periodic_points),
            "proper_fixed_union_bound_points": union_bound_points,
            "crude_union_bound_points": crude_union_bound_points,
            "total_periodic_cycles": total_cycles,
            "burnside_fixed_sum": burnside_numerator,
            "normalized_cycle_excess": fraction_record(length * total_cycles - periodic_points, periodic_points),
            "mean_cycle_length": fraction_record(periodic_points, total_cycles),
            "mean_cycle_length_over_L": fraction_record(periodic_points, length * total_cycles),
        })

    controls = []
    for s in range(2, POWER_CONTROL_MAX_S + 1):
        length = 1 << s
        fixed = [fixed_count(length, n) for n in range(1, 17)]
        assert fixed == [1] * 16
        controls.append({
            "exponent_s": s,
            "ring_length_L": length,
            "annihilating_iterate": length // 2,
            "only_periodic_state": "zero",
            "fixed_counts_period_1_through_16": fixed,
        })

    data = {
        "schema": "HCS-C155-v1",
        "candidate_id": "HCS-C155",
        "date_utc": "2026-08-25",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "Rule 90, multiplication by a=x+x^{-1} on R_L=F_2[x,x^{-1}]/(x^L-1)",
            "family": "Mersenne circumferences L=2^r-1 for every r>=2",
            "clock": "one Rule-90 update; exact temporal period is measured on the periodic image",
            "normalization": "uniform probability on im(a); fixed states, exact-period states, cycles, then cycle-averaged length",
            "cutoff": "the concentration theorem holds for every r>=2; exact ledgers use 2<=r<=8 and power-of-two controls 2<=s<=8",
            "precision": "exact F_2 polynomial arithmetic, integers, and reduced rational numbers",
            "allowed_data": "the frozen Rule-90 local rule and source-derived Mersenne/power-of-two circumference families",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, Hilbert--Polya operators, and Route-B inputs",
        },
        "periodic_image_theorem": {
            "frobenius_identity": "a^(L+1)=a for L=2^r-1",
            "periodic_set": "im(a), of dimension L-1 and cardinality 2^(L-1)",
            "restriction_identity": "g=a|_im(a) satisfies g^L=I",
            "period_support": "every exact cycle period divides L",
            "fixed_count": "Fix_L(n)=2^deg(gcd(x^L+1,(x^2+1)^n+x^n))",
            "mobius_ledger": "P_L(n)=sum_(d|n)mu(n/d)Fix_L(d), C_L(n)=P_L(n)/n",
        },
        "full_period_concentration_theorem": {
            "gcd_dependence": "for 1<=j<L and d=gcd(j,L), ker(g^j-I)=ker(g^d-I)",
            "bezout_proof": "g^L=I and gcd(U^j-1,U^L-1)=U^d-1 give equal kernels by polynomial Bezout identities",
            "dimension_bound": "dim ker(g^j-I)<=2d<=2L/3 for every 1<=j<L",
            "proper_divisor_reason": "L is odd, so every proper divisor d of L satisfies d<=L/3",
            "nonfull_state_bound": "Pr_im(a)[exact period < L] <= 2L*2^(-L/3)",
            "full_period_limit": "Pr_im(a)[exact period L] tends to 1 as r tends to infinity",
            "burnside_formula": "C_L=(1/L)sum_(j=0)^(L-1)|Fix_im(a)(g^j)|",
            "cycle_count_bound": "abs(L*C_L/2^(L-1)-1)<=2L*2^(-L/3)",
            "mean_period_limit": "the mean primitive-cycle length divided by L tends to 1",
            "mean_definition": "mean primitive-cycle length=number of periodic states divided by number of periodic cycles",
        },
        "finite_replay": {
            "r_min": MIN_R,
            "r_max": MAX_R,
            "family_rows": family,
            "divisor_period_cell_count": divisor_cells,
            "proper_time_cell_count": proper_time_cells,
        },
        "power_of_two_negative_control": {
            "statement": "for L=2^s, a^(L/2)=0, so zero is the only periodic state",
            "rows": controls,
        },
        "progress_and_boundary": {
            "progress": "upgrades exact Mersenne periodic-image structure to an all-r concentration theorem: almost every periodic state and the cycle-average scale have full period L",
            "matched_control": "the neighboring power-of-two family remains nilpotent, so the concentration is specific to the frozen Mersenne family",
            "route_a_obstruction": "the normalized finite-volume law has no frozen target divisor, analytic continuation comparison, arithmetic factorization, or natural operator lift",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_R_FULL_PERIOD_CONCENTRATION_AND_CYCLE_AVERAGE_SCALING_ON_MERSENNE_RULE90_IMAGES",
            "A2_qualification": "FINITE_VOLUME_NORMALIZED_ORBIT_STATISTICS_WITH_NO_TARGET_DIVISOR_COMPARISON",
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
            "that every divisor of L occurs as an exact period",
            "an infinite-volume determinant or thermodynamic orbit measure",
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
    print(json.dumps({"status": "C155_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "family_rows": len(data["finite_replay"]["family_rows"]), "divisor_cells": data["finite_replay"]["divisor_period_cell_count"], "proper_time_cells": data["finite_replay"]["proper_time_cell_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
