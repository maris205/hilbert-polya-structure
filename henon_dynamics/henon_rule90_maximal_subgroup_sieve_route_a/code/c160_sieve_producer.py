#!/usr/bin/env python3
"""Produce the exact HCS-C160 Rule-90 maximal-subgroup certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c160_rule90_sieve_evidence.json"
SOURCE_COMMIT = "63f75cf476711de93e6096ef74ac16969e1127d0"
MIN_R = 2
MAX_R = 10


def degree(polynomial: int) -> int:
    return polynomial.bit_length() - 1


def multiply(left: int, right: int) -> int:
    value = 0
    while right:
        if right & 1:
            value ^= left
        right >>= 1
        left <<= 1
    return value


def power(base: int, exponent: int) -> int:
    value = 1
    while exponent:
        if exponent & 1:
            value = multiply(value, base)
        base = multiply(base, base)
        exponent >>= 1
    return value


def remainder(dividend: int, divisor: int) -> int:
    divisor_degree = degree(divisor)
    while dividend and degree(dividend) >= divisor_degree:
        dividend ^= divisor << (degree(dividend) - divisor_degree)
    return dividend


def polynomial_gcd(left: int, right: int) -> int:
    while right:
        left, right = right, remainder(left, right)
    return left


def gcd_dimension(length: int, time: int) -> int:
    spatial = (1 << length) | 1
    temporal = power(0b101, time) ^ (1 << time)
    return degree(polynomial_gcd(spatial, temporal))


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


def distinct_prime_factors(n: int) -> list[int]:
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    family = []
    subset_cells = 0
    divisor_cells = 0
    prime_rows = []
    for r in range(MIN_R, MAX_R + 1):
        length = (1 << r) - 1
        primes = distinct_prime_factors(length)
        subset_rows = []
        nonfull = 0
        singleton_sum = 0
        pair_sum = 0
        for size in range(1, len(primes) + 1):
            for chosen in combinations(primes, size):
                product = 1
                for factor in chosen:
                    product *= factor
                time = length // product
                dimension = gcd_dimension(length, time)
                points = 1 << dimension
                sign = 1 if size & 1 else -1
                nonfull += sign * points
                if size == 1:
                    singleton_sum += points
                elif size == 2:
                    pair_sum += points
                subset_rows.append({
                    "prime_subset": list(chosen),
                    "subset_size": size,
                    "intersection_time": time,
                    "fixed_dimension": dimension,
                    "fixed_points": points,
                    "inclusion_exclusion_sign": sign,
                    "signed_term": sign * points,
                })
        subset_cells += len(subset_rows)

        divisor_rows = []
        exact_full = 0
        for d in divisors(length):
            dimension = gcd_dimension(length, d)
            fixed = 1 << dimension
            divisor_rows.append({"divisor": d, "fixed_dimension": dimension, "fixed_points": fixed, "mobius_weight_for_full_period": mobius(length // d)})
            exact_full += mobius(length // d) * fixed
        divisor_cells += len(divisor_rows)
        periodic_points = 1 << (length - 1)
        assert exact_full == periodic_points - nonfull
        assert singleton_sum - pair_sum <= nonfull <= singleton_sum
        row = {
            "exponent_r": r,
            "ring_length_L": length,
            "distinct_source_length_prime_factors": primes,
            "periodic_image_dimension": length - 1,
            "periodic_image_points": periodic_points,
            "maximal_subgroup_rows": subset_rows,
            "divisor_rows": divisor_rows,
            "nonfull_periodic_points": nonfull,
            "full_period_points": exact_full,
            "singleton_bonferroni_upper": singleton_sum,
            "singleton_minus_pair_lower": singleton_sum - pair_sum,
            "exact_sieve_matches_mobius": True,
        }
        family.append(row)

        if is_prime(length) and length > 3:
            assert primes == [length]
            assert gcd_dimension(length, 1) == 0
            assert nonfull == 1
            cycles = (periodic_points - 1) // length
            assert cycles * length == periodic_points - 1
            prime_rows.append({
                "exponent_r": r,
                "mersenne_prime_L": length,
                "fixed_points_at_time_one": 1,
                "exact_period_one_points": 1,
                "exact_period_L_points": periodic_points - 1,
                "primitive_L_cycles": cycles,
                "short_period_probability": {"numerator": 1, "denominator": periodic_points},
                "finite_zeta": f"1/((1-z)(1-z^{length})^{cycles})",
            })

    l3_dimension = gcd_dimension(3, 1)
    assert l3_dimension == 2
    data = {
        "schema": "HCS-C160-v1",
        "candidate_id": "HCS-C160",
        "date_utc": "2026-08-25",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "cyclic Rule 90, multiplication by a=x+x^(-1) on R_L=F_2[x,x^(-1)]/(x^L-1)",
            "family": "every Mersenne circumference L=2^r-1, r>=2; exact Mersenne-prime corollary for every such L>3 that is prime",
            "clock": "one Rule-90 update restricted to the periodic image im(a); exact temporal period is the least positive return",
            "normalization": "uniform labeled states on im(a), exact-period state counts, and geometric primitive cycles",
            "cutoff": "the maximal-subgroup sieve is all-r and the prime corollary is for every Mersenne prime L>3; finite ledgers use 2<=r<=10",
            "precision": "exact F_2 polynomial arithmetic and arbitrary-precision integers",
            "allowed_data": "the frozen Rule-90 rule and source-derived factorization of the finite circumference L only",
            "forbidden_data": "external target prime or zero tables, arithmetic/local factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "hard_gate_record": {
            "requested_advance": "an exact all-parameter refinement beyond the C155 proper-clock union bound",
            "passed_by": "an exact maximal-subgroup inclusion--exclusion for every Mersenne L and a closed cycle law for every Mersenne-prime L>3",
            "model_pivot_required": False,
            "no_infinitude_claim": "the theorem is conditional on a source circumference being Mersenne prime and does not assert infinitely many such lengths",
        },
        "periodic_image_theorem": {
            "identity": "a^(L+1)=a and im(a) is the complete periodic set of dimension L-1",
            "restriction": "g=a|_im(a) satisfies g^L=I, so every exact period divides L",
            "fixed_dimension": "D_L(d)=deg gcd(x^L+1,(x^2+1)^d+x^d)",
            "fixed_count": "|Fix(g^d)|=2^(D_L(d))",
        },
        "maximal_subgroup_sieve_theorem": {
            "prime_set": "P(L) is the set of distinct ordinary integer prime divisors of the source circumference L",
            "nonfull_union": "{v:per(v)<L}=union_{p in P(L)} Fix(g^(L/p))",
            "intersection": "intersection_{p in Q}Fix(g^(L/p))=Fix(g^(L/product_{p in Q}p))",
            "exact_formula": "N_<L=sum_{empty!=Q subset P(L)}(-1)^(|Q|+1)2^(D_L(L/product(Q)))",
            "bonferroni": "sum_p 2^(D_L(L/p))-sum_{p<q}2^(D_L(L/(pq))) <= N_<L <= sum_p 2^(D_L(L/p))",
            "source_only_factorization": "P(L) indexes maximal subgroups of the finite time group C_L; it is not target arithmetic-local data or an Euler product",
        },
        "mersenne_prime_cycle_theorem": {
            "range": "every L=2^r-1>3 that is prime; no infinitude is assumed or claimed",
            "period_support": [1, "L"],
            "fixed_one_proof": "a=1 gives x^2+x+1=0, whose nontrivial roots have order 3; because 3 does not divide prime L>3, Fix(g)={0}",
            "exact_counts": "P_L(1)=1 and P_L(L)=2^(L-1)-1",
            "cycle_count": "C_L(L)=(2^(L-1)-1)/L",
            "short_probability": "Pr(period<L)=2^(-(L-1)) exactly",
            "finite_zeta": "zeta_g(z)=1/((1-z)(1-z^L)^((2^(L-1)-1)/L))",
        },
        "finite_replay": {
            "r_min": MIN_R,
            "r_max": MAX_R,
            "family_rows": family,
            "maximal_subgroup_subset_cell_count": subset_cells,
            "divisor_cell_count": divisor_cells,
            "mersenne_prime_rows": prime_rows,
            "L3_exception": {"L": 3, "fixed_dimension_at_one": l3_dimension, "fixed_points_at_one": 1 << l3_dimension, "reason": "3 divides L, so the order-three roots occur and g is the identity on im(a)"},
        },
        "progress_and_boundary": {
            "progress": "upgrades C155's all-clock union bound to an exact maximal-subgroup sieve for every Mersenne length and to a closed two-period cycle law on every Mersenne-prime source size",
            "route_a_obstruction": "the exact finite-volume law has no target divisor, analytic target comparison, arithmetic factorization, or natural operator lift",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_R_MAXIMAL_SUBGROUP_PERIOD_SIEVE_AND_EXACT_MERSENNE_PRIME_CYCLE_LAW",
            "A2_qualification": "FINITE_SOURCE_ZETAS_WITH_NO_TARGET_DIVISOR_COMPARISON",
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
            "that infinitely many Mersenne primes exist",
            "that the ordinary divisors of L are arithmetic local factors or an Euler product",
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
    replay = data["finite_replay"]
    print(json.dumps({"status": "C160_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "family_rows": len(replay["family_rows"]), "subset_cells": replay["maximal_subgroup_subset_cell_count"], "prime_rows": len(replay["mersenne_prime_rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
