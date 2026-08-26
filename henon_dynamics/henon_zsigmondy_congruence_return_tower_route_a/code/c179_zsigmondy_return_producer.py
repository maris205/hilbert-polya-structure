#!/usr/bin/env python3
"""Produce the exact HCS-C179 congruence-return certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
from math import gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c179_zsigmondy_return_evidence.json"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PAIR_A_MAX = 14
FIBER_A_MAX = 10
TIME_MAX = 10
MODULUS_MAX = 120
FIXED_PREFIX_MAX = 12
LIFT_PRIME_MAX = 257
LIFT_K_MAX = 4


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()


def factor_integer(value: int) -> list[tuple[int, int]]:
    """Deterministic trial-division factorization for the frozen sentinel range."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors: list[tuple[int, int]] = []
    remaining = value
    for prime in (2, 3):
        exponent = 0
        while remaining % prime == 0:
            exponent += 1
            remaining //= prime
        if exponent:
            factors.append((prime, exponent))
    divisor = 5
    step = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            exponent += 1
            remaining //= divisor
        if exponent:
            factors.append((divisor, exponent))
        divisor += step
        step = 6 - step
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def totient(value: int) -> int:
    if value == 1:
        return 1
    result = value
    for prime, _ in factor_integer(value):
        result -= result // prime
    return result


def mobius(value: int) -> int:
    if value == 1:
        return 1
    factors = factor_integer(value)
    if any(exponent > 1 for _, exponent in factors):
        return 0
    return -1 if len(factors) % 2 else 1


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factor_integer(value):
        result = [base * prime**power for base in result for power in range(exponent + 1)]
    return sorted(result)


def multiplicative_order(value: int, modulus: int) -> int:
    if modulus < 2 or gcd(value, modulus) != 1:
        raise ValueError("order requires a unit modulo N>=2")
    order = totient(modulus)
    for prime, _ in factor_integer(order):
        while order % prime == 0 and pow(value, order // prime, modulus) == 1:
            order //= prime
    return order


def parameter_pairs(limit: int) -> list[tuple[int, int]]:
    return [
        (a, b)
        for a in range(2, limit + 1)
        for b in range(1, a)
        if gcd(a, b) == 1
    ]


def is_power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def zsigmondy_exception(a: int, b: int, n: int) -> str | None:
    if (a, b, n) == (2, 1, 6):
        return "exceptional_triple_2_1_6"
    if n == 2 and is_power_of_two(a + b):
        return "n_2_and_a_plus_b_power_of_two"
    return None


def primitive_cycle_count(a: int, b: int, n: int) -> int:
    numerator = sum(
        mobius(n // divisor) * (a**divisor - b**divisor)
        for divisor in divisors(n)
    )
    if numerator % n:
        raise AssertionError("Möbius orbit numerator is not divisible by n")
    return numerator // n


def cycle_lengths_for_multiplier(multiplier: int, modulus: int) -> list[int]:
    units = [value for value in range(modulus) if gcd(value, modulus) == 1]
    unseen = set(units)
    lengths: list[int] = []
    while unseen:
        start = min(unseen)
        cursor = start
        length = 0
        while cursor in unseen:
            unseen.remove(cursor)
            cursor = multiplier * cursor % modulus
            length += 1
        if cursor != start:
            raise AssertionError("unit permutation did not close at its start")
        lengths.append(length)
    return sorted(lengths)


def build() -> dict:
    pairs = parameter_pairs(PAIR_A_MAX)
    factor_cache: dict[tuple[int, int, int], list[tuple[int, int]]] = {}

    def difference_factors(a: int, b: int, n: int) -> list[tuple[int, int]]:
        key = (a, b, n)
        if key not in factor_cache:
            factor_cache[key] = factor_integer(a**n - b**n)
        return factor_cache[key]

    zsigmondy_rows = []
    for a, b in pairs:
        for n in range(2, TIME_MAX + 1):
            difference = a**n - b**n
            factors = difference_factors(a, b, n)
            factor_rows = []
            primitive_primes: list[int] = []
            for prime, exponent in factors:
                ratio = a * pow(b, -1, prime) % prime
                order = multiplicative_order(ratio, prime) if prime > 2 else 1
                primitive = order == n
                if primitive:
                    primitive_primes.append(prime)
                factor_rows.append(
                    {
                        "prime": prime,
                        "exponent": exponent,
                        "multiplicative_order": order,
                        "primitive_at_n": primitive,
                    }
                )
            exception = zsigmondy_exception(a, b, n)
            zsigmondy_rows.append(
                {
                    "a": a,
                    "b": b,
                    "n": n,
                    "difference": difference,
                    "factors": factor_rows,
                    "primitive_primes": primitive_primes,
                    "exception": exception,
                    "existence_expected": exception is None,
                    "existence_observed": bool(primitive_primes),
                }
            )

    global_rows = []
    for a, b in pairs:
        for n in range(1, TIME_MAX + 1):
            difference = a**n - b**n
            factors = difference_factors(a, b, n)
            divisor_phi_sum = sum(totient(divisor) for divisor in divisors(difference))
            global_rows.append(
                {
                    "a": a,
                    "b": b,
                    "n": n,
                    "difference": difference,
                    "factorization": [
                        {"prime": prime, "exponent": exponent}
                        for prime, exponent in factors
                    ],
                    "disjoint_union_fixed_count": divisor_phi_sum,
                    "profinite_fixed_count": 0,
                    "primitive_cycle_count": primitive_cycle_count(a, b, n),
                }
            )

    fiber_pairs = parameter_pairs(FIBER_A_MAX)
    finite_fiber_rows = []
    for a, b in fiber_pairs:
        for modulus in range(2, MODULUS_MAX + 1):
            if gcd(modulus, a * b) != 1:
                continue
            multiplier = a * pow(b, -1, modulus) % modulus
            order = multiplicative_order(multiplier, modulus)
            phi = totient(modulus)
            lengths = cycle_lengths_for_multiplier(multiplier, modulus)
            units = [value for value in range(modulus) if gcd(value, modulus) == 1]
            reverse_ok = all(
                pow((multiplier * pow(value, -1, modulus)) % modulus, -1, modulus)
                == (pow(multiplier, -1, modulus) * value) % modulus
                for value in units
            )
            finite_fiber_rows.append(
                {
                    "a": a,
                    "b": b,
                    "modulus": modulus,
                    "multiplier": multiplier,
                    "phi": phi,
                    "order": order,
                    "cycle_count": len(lengths),
                    "cycle_length_set": sorted(set(lengths)),
                    "zeta_factor": f"(1-z^{order})^(-{phi // order})",
                    "koopman_determinant_factor": f"(1-z^{order})^{phi // order}",
                    "fixed_prefix": [
                        phi if time % order == 0 else 0
                        for time in range(1, FIXED_PREFIX_MAX + 1)
                    ],
                    "inversion_reversor_verified": reverse_ok,
                }
            )

    lift_rows = []
    for row in zsigmondy_rows:
        a, b, n = row["a"], row["b"], row["n"]
        exponent_by_prime = {
            entry["prime"]: entry["exponent"] for entry in row["factors"]
        }
        for prime in row["primitive_primes"]:
            if prime > LIFT_PRIME_MAX:
                continue
            exponent = exponent_by_prime[prime]
            for k in range(1, LIFT_K_MAX + 1):
                modulus = prime**k
                ratio = a * pow(b, -1, modulus) % modulus
                predicted = n * prime ** max(0, k - exponent)
                observed = multiplicative_order(ratio, modulus)
                lift_rows.append(
                    {
                        "a": a,
                        "b": b,
                        "n": n,
                        "prime": prime,
                        "base_valuation": exponent,
                        "k": k,
                        "modulus": modulus,
                        "predicted_order": predicted,
                        "observed_order": observed,
                        "phi": totient(modulus),
                        "cycle_count": totient(modulus) // observed,
                    }
                )

    references = [
        {
            "id": "zsigmondy1892",
            "claim_scope": "classical primitive-divisor existence theorem and exact exceptions",
            "status": "EXTERNAL_THEOREM_ATTRIBUTED_NOT_NEW",
            "author": "Karl Zsigmondy",
            "title": "Zur Theorie der Potenzreste",
            "year": 1892,
            "venue": "Monatshefte fuer Mathematik und Physik 3, 265--284",
            "doi": "10.1007/BF01692444",
        },
        {
            "id": "birkhoff_vandiver1904",
            "claim_scope": "classical arithmetic of integral and primitive divisors of a^n-b^n",
            "status": "HISTORICAL_CONTEXT_ATTRIBUTED",
            "author": "George D. Birkhoff and Harry S. Vandiver",
            "title": "On the Integral Divisors of a^n-b^n",
            "year": 1904,
            "venue": "Annals of Mathematics 5(4), 173--180",
            "doi": "10.2307/2007263",
        },
        {
            "id": "artin_mazur1965",
            "claim_scope": "Artin--Mazur fixed-point zeta convention",
            "status": "DEFINITIONAL_SOURCE_ATTRIBUTED",
            "author": "Michael Artin and Barry Mazur",
            "title": "On Periodic Points",
            "year": 1965,
            "venue": "Annals of Mathematics 81(1), 82--99",
            "doi": "10.2307/1970384",
        },
        {
            "id": "silverman2013",
            "claim_scope": "modern arithmetic-dynamics context for dynamical Zsigmondy sets",
            "status": "CONTEXT_ONLY_NOT_USED_AS_PROOF",
            "author": "Joseph H. Silverman",
            "title": "Primitive Divisors, Dynamical Zsigmondy Sets, and Vojta's Conjecture",
            "year": 2013,
            "venue": "Journal of Number Theory 133(9), 2948--2963",
            "doi": "10.1016/j.jnt.2013.03.005",
        },
    ]

    data = {
        "schema": "hcs-c179-zsigmondy-congruence-return-v1",
        "candidate_id": "HCS-C179",
        "evaluation_date": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "skill": "route-a-evaluator",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "for coprime integers a>b>=1 and N>=2 with gcd(N,ab)=1, R_(a,b,N)(x)=a*b^(-1)*x on U_N=(Z/NZ)^times, marked at x=1",
            "arithmetic_origin": "the integer divisibility sequence a^n-b^n and its congruence first-return moduli",
            "parameter_domain": "all coprime integers a>b>=1; every admissible finite modulus N; odd primitive primes and all their powers",
            "clock": "one multiplication by a*b^(-1) is one discrete source step; no log-prime roof is assigned",
            "normalization": "finite-fiber fixed-point cardinality and unweighted Artin--Mazur convention",
            "determinant_convention": "zeta_N=exp(sum_(t>=1)#Fix(R_N^t)z^t/t) and the finite Koopman determinant det(I-zU_N)",
            "globalizations": "the disjoint union over finite unit fibers and the profinite inverse limit are kept as distinct constructions",
            "precision": "exact integer factorization, modular order, valuation, permutation, and formal power-series algebra",
            "training_data": "none",
            "allowed_data": "integers generated from a,b; exact congruence reductions and factorization used only as deterministic sentinels",
            "forbidden_data": "target zero or prime tables, local Euler factors, root numbers, automorphy, prime-weighted global products, log-p roofs, fitted target data, Hilbert--Polya claims, and Route B",
        },
        "attribution_registry": references,
        "theorem_ledger": {
            "primitive_return_equivalence": "p is primitive for a^n-b^n iff the marked point 1 has least return n under R_(a,b,p)",
            "zsigmondy_scope": "for n>=2 a primitive return prime exists except (2,1,6) and n=2 with a+b a power of two; this is the attributed classical theorem",
            "prime_power_lift": "for an odd primitive p with e=v_p(a^n-b^n), ord_(p^k)(a*b^(-1))=n*p^max(0,k-e)",
            "finite_fiber": "with L_N=ord_N(a*b^(-1)), U_N is phi(N)/L_N cycles of length L_N, zeta_N=(1-z^L_N)^(-phi(N)/L_N), and inversion reverses time",
            "disjoint_union": "including the singleton N=1 fiber, the finite-fiber disjoint union has #Fix at time n equal to sum_(N|a^n-b^n)phi(N)=a^n-b^n and zeta=(1-bz)/(1-az)",
            "profinite_limit": "translation by a/b on the inverse limit of the U_N has no positive-time fixed point and source zeta 1",
            "owner_nonuniqueness": "finite congruence fibers admit two source-natural globalizations with incompatible fixed ledgers, so the fiber data do not select a single global determinant owner",
        },
        "finite_regression_sentinels": {
            "sentinels_are_proof": False,
            "pair_a_max": PAIR_A_MAX,
            "fiber_a_max": FIBER_A_MAX,
            "time_max": TIME_MAX,
            "modulus_max": MODULUS_MAX,
            "fixed_prefix_max": FIXED_PREFIX_MAX,
            "lift_prime_max": LIFT_PRIME_MAX,
            "lift_k_max": LIFT_K_MAX,
            "parameter_pair_count": len(pairs),
            "fiber_pair_count": len(fiber_pairs),
            "zsigmondy_rows": zsigmondy_rows,
            "global_rows": global_rows,
            "finite_fiber_rows": finite_fiber_rows,
            "prime_power_lift_rows": lift_rows,
        },
        "route_a": {
            "tuple": [
                "A0_WEAK_ARITHMETIC_RELATION",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
            "A0_qualification": "RATIONAL_PRIMES_EMERGE_AS_FIRST_RETURN_MODULI_BUT_NO_SINGLE_GLOBAL_PRIME_ORBIT_OWNER_OR_LOG_P_CLOCK",
            "A1_qualification": "EVERY_FINITE_FIBER_IS_EXACT_BUT_THE_TWO_NATURAL_GLOBALIZATIONS_HAVE_INCOMPATIBLE_PRIMITIVE_LEDGERS",
            "A2_qualification": "SOURCE_ZETAS_ARE_EXACT_BUT_NO_TARGET_DIVISOR_OR_FROZEN_VALIDATION_PROTOCOL_EXISTS",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
            "A4_qualification": "FINITE_PERMUTATION_AND_PROFINITE_HAAR_KOOPMAN_LIFTS_ARE_NATURAL_SAME_CLOCK_UNITARIES",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "assigned_log_p_roof": False,
            "built_prime_weighted_global_product": False,
            "claimed_local_euler_factor": False,
            "claimed_root_number": False,
            "claimed_automorphy": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_target_counting_law": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "integrity": {
            "finite_ledgers_are_proof": False,
            "zsigmondy_theorem_claimed_new": False,
            "order_lift_proved_in_package": True,
            "citation_population": len(references),
            "reference_population": len(references),
            "external_reviewer_simulated": False,
            "model_rejected_as_primary_route_a_candidate": False,
            "global_owner_uniqueness_claimed": False,
        },
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        json.dumps(
            {
                "status": "C179_PRODUCER_PASS",
                "payload_sha256": data["payload_sha256"],
                "zsigmondy_rows": len(data["finite_regression_sentinels"]["zsigmondy_rows"]),
                "global_rows": len(data["finite_regression_sentinels"]["global_rows"]),
                "finite_fiber_rows": len(data["finite_regression_sentinels"]["finite_fiber_rows"]),
                "prime_power_lift_rows": len(data["finite_regression_sentinels"]["prime_power_lift_rows"]),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
