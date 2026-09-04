#!/usr/bin/env python3
"""Canonical exact finite evidence for HCS-C374.

The all-level field and density statements are proved in THEOREM_PACKAGE.md.
This program exhausts the affine images through level 12 and independently
enumerates the declared finite prime grid as regression evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c374_kummer_arboreal_evidence.json"
SOURCE_COMMIT = "f58422d8f03235329863f946654981ecb5d4dc97"
EVALUATOR_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
LEVEL_MIN = 3
LEVEL_MAX = 12
PRIME_BOUND = 100000


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def payload_digest(value: dict) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def chi2(a: int) -> int:
    """The conductor-eight character (2/a), for odd a."""
    if a % 2 != 1:
        raise ValueError("chi2 expects an odd integer")
    return 1 if a % 8 in (1, 7) else -1


def expected_histogram(n: int) -> dict[int, int]:
    order = 1 << (2 * n - 2)
    out = {2: 1 << (2 * n - 4), 1 << n: 1}
    for k in range(3, n):
        out[1 << k] = 1 << (2 * n - 2 * k - 1)
    out[0] = order - sum(out.values())
    return dict(sorted(out.items()))


def enumerate_image(n: int) -> Counter[int]:
    modulus = 1 << n
    counts: Counter[int] = Counter()
    for a in range(1, modulus, 2):
        parity = 0 if chi2(a) == 1 else 1
        g = math.gcd(a - 1, modulus)
        for b in range(parity, modulus, 2):
            roots = g if b % g == 0 else 0
            counts[roots] += 1
    return counts


def enumerate_full_affine(n: int) -> Counter[int]:
    """Fixed-root control histogram for the uncut ambient affine group."""
    modulus = 1 << n
    counts: Counter[int] = Counter()
    for a in range(1, modulus, 2):
        g = math.gcd(a - 1, modulus)
        for b in range(modulus):
            roots = g if b % g == 0 else 0
            counts[roots] += 1
    return counts


def primes_upto(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(bound) + 1):
        if sieve[p]:
            sieve[p * p : bound + 1 : p] = b"\x00" * (((bound - p * p) // p) + 1)
    return [p for p in range(3, bound + 1, 2) if sieve[p]]


def factorization(value: int) -> list[tuple[int, int]]:
    factors = []
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime += 1
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def roots_mod_prime(p: int, n: int) -> int:
    degree = 1 << n
    d = math.gcd(degree, p - 1)
    return d if pow(2, (p - 1) // d, p) == 1 else 0


def prime_ledger() -> tuple[list[dict], str, int]:
    primes = primes_upto(PRIME_BOUND)
    stream = hashlib.sha256()
    levels = []
    for n in range(LEVEL_MIN, LEVEL_MAX + 1):
        hist: Counter[int] = Counter()
        first: dict[str, int] = {}
        for p in primes:
            roots = roots_mod_prime(p, n)
            hist[roots] += 1
            first.setdefault(str(roots), p)
            stream.update(canonical([p, n, roots]) + b"\n")
        positive = len(primes) - hist[0]
        levels.append(
            {
                "n": n,
                "prime_count": len(primes),
                "with_root": positive,
                "empirical_fraction": f"{positive}/{len(primes)}",
                "root_histogram": {str(k): v for k, v in sorted(hist.items())},
                "first_witness": dict(sorted(first.items(), key=lambda item: int(item[0]))),
            }
        )
    return levels, stream.hexdigest(), len(primes)


def arithmetic_controls() -> dict[str, object]:
    full_affine = []
    for n in range(LEVEL_MIN, LEVEL_MAX + 1):
        histogram = dict(sorted(enumerate_full_affine(n).items()))
        expected_four = 1 << (2 * n - 5)
        if histogram.get(4, 0) != expected_four:
            raise AssertionError(f"full-affine four-root control failed at level {n}")
        full_affine.append({
            "n": n,
            "group_order": 1 << (2 * n - 1),
            "fixed_point_histogram": {str(k): value for k, value in histogram.items()},
            "four_fixed_elements": histogram[4],
            "four_fixed_formula": "2^(2n-5)",
        })
    primes_under_100 = set(primes_upto(100))
    composites = [value for value in range(9, 100, 2) if value not in primes_under_100]
    prime_powers = []
    mixed_composites = []
    for value in composites:
        factors = factorization(value)
        if len(factors) == 1:
            prime, exponent = factors[0]
            if exponent < 2:
                raise AssertionError("composite prime-power classification failed")
            prime_powers.append({"value": value, "prime": prime, "exponent": exponent})
        else:
            mixed_composites.append({
                "value": value,
                "distinct_prime_factors": [prime for prime, _ in factors],
            })
    return {
        "neighboring_basepoint_3": {
            "status": "PROVED_BY_VALUATION_AND_CAPELLI",
            "radical_cyclotomic_intersection": "Q(3^(1/2^n)) intersect Q(zeta_(2^n)) = Q for every n>=3",
            "reason": "a prime above 3 has valuation one on 3 in the unramified 2-power cyclotomic field, so 3 is not a square and Capelli gives degree 2^n over the cyclotomic field",
            "affine_image": "full AGL_1(Z/2^n)",
            "shared_Q_sqrt_2_character_entanglement": False,
        },
        "simpler_parent_full_affine": {
            "status": "EXECUTED_EXACT",
            "role": "ambient affine control without the basepoint-two character cut",
            "level_ledger": full_affine,
            "total_pairs": sum(row["group_order"] for row in full_affine),
            "restores_four_fixed_roots": True,
        },
        "composite_label_decomposition": {
            "status": "EXECUTED_EXACT",
            "odd_composite_count_below_100": len(composites),
            "prime_power_labels": prime_powers,
            "prime_power_count": len(prime_powers),
            "prime_power_owner": "p^r is retained as the conjugacy class of Frob_p^r and as a repetition control",
            "mixed_composite_labels": mixed_composites,
            "mixed_composite_count": len(mixed_composites),
            "mixed_composite_has_single_prime_frobenius_owner": False,
            "role": "prime powers retain Frobenius repetition ownership; only mixed composites are rejected as single-prime owners",
        },
        "empirical_density_earns_a0_credit": False,
    }


def make_evidence() -> dict:
    group_levels = []
    for n in range(LEVEL_MIN, LEVEL_MAX + 1):
        observed = dict(sorted(enumerate_image(n).items()))
        predicted = expected_histogram(n)
        if observed != predicted:
            raise AssertionError(f"level-{n} histogram mismatch")
        order = 1 << (2 * n - 2)
        positive = order - observed[0]
        density = Fraction(7, 24) + Fraction(1, 3 * (4 ** (n - 1)))
        if density != Fraction(positive, order):
            raise AssertionError(f"level-{n} density mismatch")
        group_levels.append(
            {
                "n": n,
                "modulus": 1 << n,
                "group_order": order,
                "ambient_affine_order": 1 << (2 * n - 1),
                "image_index": 2,
                "exhaustive_pairs": sum(observed.values()),
                "fixed_point_histogram": {str(k): v for k, v in observed.items()},
                "positive_fixed_elements": positive,
                "root_prime_density": f"{density.numerator}/{density.denominator}",
                "restriction_to_previous": None
                if n == LEVEL_MIN
                else {"map": "(a,b) modulo 2^(n-1)", "surjective": True, "kernel_order": 4},
            }
        )
    prime_levels, prime_stream, prime_count = prime_ledger()
    evidence = {
        "schema": "hcs-c374-kummer-arboreal-evidence-v1",
        "candidate_id": "HCS-C374",
        "obstruction_id": "HEN-O358",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": 1788480000,
        "scope_literal": SCOPE,
        "model": {
            "map": "f(z)=z^2",
            "basepoint": 2,
            "level_roots": "R_n={z:z^(2^n)=2}",
            "splitting_field": "K_n=Q(2^(1/2^n),zeta_(2^n))",
            "level_range_theorem": "all n>=3",
            "level_range_evidence": [LEVEL_MIN, LEVEL_MAX],
        },
        "analytic_theorem": {
            "radical_cyclotomic_intersection": "Q(2^(1/2^n)) intersect Q(zeta_(2^n)) = Q(sqrt(2)) for every n>=3",
            "relative_irreducibility": "X^(2^(n-1))-sqrt(2) is irreducible over Q(zeta_(2^n))",
            "degree": "[K_n:Q]=2^(2n-2)",
            "image": "H_n={(a,b) in (Z/2^n)^times semidirect Z/2^n : (-1)^b=(2/a)}",
            "action": "j maps to a*j+b on R_n indexed by zeta_(2^n)^j 2^(1/2^n)",
            "restriction": "H_(n+1)->H_n is coordinate reduction, surjective with kernel order 4",
            "inverse_limit": "H_infinity={(a,b) in Z_2^times semidirect Z_2 : (-1)^(b mod 2)=chi_2(a)}",
            "inverse_limit_index": 2,
            "density": "delta_n=7/24+1/(3*4^(n-1)); limit 7/24",
            "forbidden_root_counts": [1, 4],
        },
        "group_ledger": group_levels,
        "prime_regression": {
            "prime_bound": PRIME_BOUND,
            "odd_prime_count": prime_count,
            "cell_count": prime_count * (LEVEL_MAX - LEVEL_MIN + 1),
            "row_stream_sha256": prime_stream,
            "levels": prime_levels,
            "role": "finite exact regression, not proof of the all-level group or Chebotarev density theorem",
        },
        "arithmetic_controls": arithmetic_controls(),
        "quantization_boundary": {
            "finite_hilbert_spaces": "l2(R_n)",
            "operator": "the real basis-permutation unitary attached to each finite Galois element",
            "same_level_and_iterate_clock": True,
            "canonical_global_time_reversal_to_inverse": False,
            "nontrivial_orbit_phase_or_weight_package": False,
            "global_self_adjoint_hamiltonian_owner": False,
            "route_a_verdict": "A4_FORMAL_HINT",
        },
        "sources": [
            {"key": "Jones2013", "doi": "10.5802/pmb.a-154", "url": "https://doi.org/10.5802/pmb.a-154"},
            {"key": "Lang2002", "doi": "10.1007/978-1-4613-0041-0", "url": "https://doi.org/10.1007/978-1-4613-0041-0"},
            {"key": "Washington1997", "doi": "10.1007/978-1-4612-1934-7", "url": "https://doi.org/10.1007/978-1-4612-1934-7"},
            {"key": "Neukirch1999", "doi": "10.1007/978-3-662-03983-0", "url": "https://doi.org/10.1007/978-3-662-03983-0"},
        ],
        "ownership_boundary": {
            "inherited": "HCS-C12A owns the universal finite-permutation fixed-point and reciprocal determinant identity",
            "c374_owner": "the basepoint-two radical-cyclotomic entanglement, exact all-level index-two affine arboreal image, compatible restriction tower, fixed-root law, and Chebotarev root-density formula",
            "nonownership": "no claim to the universal C12A finite determinant mechanism or to classical Capelli and Chebotarev theorems",
        },
        "collision_boundary": {
            "nearest_C12A": "universal zero-dimensional Frobenius permutation and determinant mechanism; C374 owns a specific infinite Kummer preimage tower and its entangled image",
            "nearest_C33_C34_C38_C40": "Hill square-class and cubic Kummer channels, not an arboreal Galois tower of iterated preimages",
            "nearest_C56": "one degree-27 finite-etale W(E6) fiber rather than a compatible infinite radical tower",
            "nearest_C179": "congruence-return and Zsigmondy tower rather than splitting fields and Frobenius fixed-root densities",
            "nearest_C369": "one quartic S4 all-good-prime atlas rather than all levels of a single quadratic preimage tree",
        },
        "route_a": {
            "tuple": [
                "A0_STRUCTURAL_ARITHMETIC_RELATION",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FORMAL_HINT",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
            "a1_scope": "the proved affine action and fixed-root law are source-local and do not constitute a complete arithmetic primitive-orbit atlas",
            "a1_missing_requirements": [
                "no all-level primitive-cycle and repetition enumeration with completeness control",
                "no orbit orientation, phase, multiplicity-weight, or monodromy and stability atlas",
                "no intrinsic prime-to-orbit, prime-power, or log(p) period correspondence",
                "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are not completed at the A1 orbit layer",
            ],
        },
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "nonclaims": [
            "no target Euler factor, target root number, or automorphy statement",
            "no target analytic continuation, functional equation, divisor, or zero match",
            "no Hilbert-Polya operator and no Route-B invocation",
            "no inference of an all-level theorem from the finite ledger",
        ],
    }
    evidence["payload_sha256"] = payload_digest(evidence)
    return evidence


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C374 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    evidence = make_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(
        "C374_PRODUCER_PASS "
        f"levels={LEVEL_MAX-LEVEL_MIN+1} group_pairs={sum(x['group_order'] for x in evidence['group_ledger'])} "
        f"prime_cells={evidence['prime_regression']['cell_count']} payload_sha256={evidence['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
