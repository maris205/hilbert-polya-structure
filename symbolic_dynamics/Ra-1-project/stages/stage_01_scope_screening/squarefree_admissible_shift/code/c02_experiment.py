#!/usr/bin/env python3
"""Exact periodic census and preregistered controls for SD-C02."""

from __future__ import annotations

import csv
import json
import math
import random
from collections import Counter
from itertools import product
from pathlib import Path
from typing import Iterable, Sequence


SESSION_ID = "SD-S4-2026-08-12"
CANDIDATE_ID = "SD-C02"
MASTER_SEED = 20260812
SHUFFLE_SEED = 20260816
EXACT_PERIOD_CUTOFF = 30
BRUTE_PERIOD_CUTOFF = 14
FINITE_MODULUS_PRIME_COUNTS = (1, 2, 3)
WINDOW_CUTOFF = 4096
BLOCK_LENGTHS = (4, 6, 8, 10, 12)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes(count: int) -> list[int]:
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def least_prime_not_dividing(n: int) -> int:
    candidate = 2
    while True:
        if is_prime(candidate) and n % candidate != 0:
            return candidate
        candidate += 1


def support_covers_modulus(word: Sequence[int], modulus: int) -> bool:
    """Whether the support of the bi-infinite periodic word covers Z/modulus."""
    n = len(word)
    common_divisor = math.gcd(n, modulus)
    occupied_classes = {index % common_divisor for index, bit in enumerate(word) if bit}
    return len(occupied_classes) == common_divisor


def candidate_periodic_word_is_admissible(word: Sequence[int]) -> tuple[bool, int | None]:
    """Exact infinite-modulus decision, returning a prime-square witness."""
    if not any(word):
        return True, None
    witness_prime = least_prime_not_dividing(len(word))
    assert support_covers_modulus(word, witness_prime * witness_prime)
    return False, witness_prime


def brute_candidate_fixed_points(period: int) -> dict[str, int | bool]:
    accepted = 0
    rejected = 0
    witness_failures = 0
    witness_primes: Counter[int] = Counter()
    for word in product((0, 1), repeat=period):
        admissible, witness = candidate_periodic_word_is_admissible(word)
        if admissible:
            accepted += 1
        else:
            rejected += 1
            assert witness is not None
            witness_primes[witness] += 1
            if not support_covers_modulus(word, witness * witness):
                witness_failures += 1
    return {
        "period": period,
        "fixed_points": accepted,
        "rejected_nonzero_words": rejected,
        "witness_failures": witness_failures,
        "all_witnesses_valid": witness_failures == 0,
        "distinct_witness_primes": len(witness_primes),
    }


def _selected_residue_subsets(class_count: int) -> Iterable[tuple[int, int]]:
    """Yield (bit mask, union-indicator coefficient)."""
    for mask in range(1, 1 << class_count):
        size = mask.bit_count()
        yield mask, (-1) ** (size + 1)


def finite_modulus_fixed_points(period: int, primes: Sequence[int]) -> int:
    """Exact inclusion-exclusion count for a finite set of p^2 constraints.

    For each p, admissibility is the union over residue classes modulo
    gcd(period,p^2) of the event that the class is absent from the word's
    support.  Expanding the product of these unions gives this finite exact
    sum; it never enumerates 2^period words.
    """
    gcds = [math.gcd(period, p * p) for p in primes]
    # A single gcd-one modulus forces every nonempty periodic support to cover
    # that modulus, so only the empty support remains.  Besides making the
    # theorem transparent, this avoids expanding a needlessly large union for
    # other moduli.
    if any(class_count == 1 for class_count in gcds):
        return 1
    choices = [list(_selected_residue_subsets(class_count)) for class_count in gcds]
    total = 0
    for selected in product(*choices):
        coefficient = math.prod(item[1] for item in selected)
        unavailable = 0
        for index in range(period):
            if any((mask >> (index % class_count)) & 1 for (mask, _), class_count in zip(selected, gcds, strict=True)):
                unavailable += 1
        total += coefficient * (2 ** (period - unavailable))
    return total


def brute_finite_modulus_fixed_points(period: int, primes: Sequence[int]) -> int:
    return sum(
        all(not support_covers_modulus(word, p * p) for p in primes)
        for word in product((0, 1), repeat=period)
    )


def matrix_multiply_2x2(left: tuple[tuple[int, int], tuple[int, int]], right: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_power_2x2(matrix: tuple[tuple[int, int], tuple[int, int]], exponent: int) -> tuple[tuple[int, int], tuple[int, int]]:
    result = ((1, 0), (0, 1))
    power = matrix
    e = exponent
    while e:
        if e & 1:
            result = matrix_multiply_2x2(result, power)
        power = matrix_multiply_2x2(power, power)
        e >>= 1
    return result


def golden_mean_fixed_points(period: int) -> int:
    adjacency = ((1, 1), (1, 0))
    power = matrix_power_2x2(adjacency, period)
    return power[0][0] + power[1][1]


def mobius(n: int) -> int:
    factors = 0
    m = n
    divisor = 2
    while divisor * divisor <= m:
        if m % divisor == 0:
            m //= divisor
            factors += 1
            if m % divisor == 0:
                return 0
            while m % divisor == 0:
                m //= divisor
        divisor += 1
    if m > 1:
        factors += 1
    return -1 if factors % 2 else 1


def primitive_orbits_from_fixed_counts(fixed_counts: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for n in sorted(fixed_counts):
        primitive_points = sum(mobius(d) * fixed_counts[n // d] for d in range(1, n + 1) if n % d == 0)
        assert primitive_points % n == 0
        result[n] = primitive_points // n
    return result


def is_squarefree_integer(n: int) -> bool:
    divisor = 2
    while divisor * divisor <= n:
        if n % (divisor * divisor) == 0:
            return False
        divisor += 1
    return True


def block_statistics(bits: Sequence[int], block_length: int) -> dict[str, float | int]:
    counts = Counter(tuple(bits[start : start + block_length]) for start in range(len(bits) - block_length + 1))
    total = sum(counts.values())
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return {
        "block_length": block_length,
        "distinct_blocks": len(counts),
        "max_possible_distinct_blocks": 2**block_length,
        "empirical_block_entropy_bits": entropy,
        "entropy_per_symbol": entropy / block_length,
        "samples": total,
    }


def shuffled_window_control() -> dict[str, object]:
    original = [int(is_squarefree_integer(n)) for n in range(1, WINDOW_CUTOFF + 1)]
    shuffled = list(original)
    rng = random.Random(SHUFFLE_SEED)
    rng.shuffle(shuffled)
    return {
        "evidence_status": "NUMERICAL_OBSERVATION",
        "seed": SHUFFLE_SEED,
        "window": [1, WINDOW_CUTOFF],
        "ones_original": sum(original),
        "ones_shuffled": sum(shuffled),
        "density_preserved_exactly": sum(original) == sum(shuffled),
        "original_block_statistics": [block_statistics(original, length) for length in BLOCK_LENGTHS],
        "shuffled_block_statistics": [block_statistics(shuffled, length) for length in BLOCK_LENGTHS],
        "interpretation": "Finite-window word complexity is a local statistic and cannot replace the exact primitive periodic-orbit ledger.",
    }


def build_results() -> dict[str, object]:
    brute_rows = [brute_candidate_fixed_points(n) for n in range(1, BRUTE_PERIOD_CUTOFF + 1)]
    candidate_fixed = {n: 1 for n in range(1, EXACT_PERIOD_CUTOFF + 1)}
    primitive_candidate = primitive_orbits_from_fixed_counts(candidate_fixed)

    finite_primes = first_primes(max(FINITE_MODULUS_PRIME_COUNTS))
    approximant_rows: list[dict[str, object]] = []
    all_brute_validations_pass = True
    for prime_count in FINITE_MODULUS_PRIME_COUNTS:
        primes = finite_primes[:prime_count]
        for period in range(1, EXACT_PERIOD_CUTOFF + 1):
            exact_count = finite_modulus_fixed_points(period, primes)
            brute_count = None
            brute_matches = None
            if period <= BRUTE_PERIOD_CUTOFF:
                brute_count = brute_finite_modulus_fixed_points(period, primes)
                brute_matches = brute_count == exact_count
                all_brute_validations_pass &= bool(brute_matches)
            approximant_rows.append(
                {
                    "prime_count": prime_count,
                    "primes": primes,
                    "period": period,
                    "fixed_points_inclusion_exclusion": exact_count,
                    "fixed_points_brute": brute_count,
                    "brute_matches": brute_matches,
                }
            )

    parent_rows = [
        {
            "period": n,
            "full_binary_fixed_points": 2**n,
            "golden_mean_fixed_points": golden_mean_fixed_points(n),
            "candidate_fixed_points": 1,
        }
        for n in range(1, EXACT_PERIOD_CUTOFF + 1)
    ]

    return {
        "schema_version": "1.0.0",
        "session_id": SESSION_ID,
        "candidate_id": CANDIDATE_ID,
        "run_id": "SD-C02-frozen-v1",
        "source_lock": {
            "family": "symbolic dynamics / squarefree admissible subshift",
            "alphabet": [0, 1],
            "clock": "unit roof",
            "potential": 0,
            "determinant_convention": "inverse Artin-Mazur zeta",
            "arithmetic_definition": "B={p^2 : p rational prime}; primes are generated from the definition, not imported as a fitted table",
            "forbidden_data_respected": True,
            "riemann_zero_data_used": False,
        },
        "reproducibility": {
            "master_seed": MASTER_SEED,
            "shuffled_window_seed": SHUFFLE_SEED,
            "precision": {"exact": "Python arbitrary-precision integers", "numerical": "IEEE-754 binary64 entropy summaries"},
            "cutoff": {
                "exact_period": EXACT_PERIOD_CUTOFF,
                "brute_period": BRUTE_PERIOD_CUTOFF,
                "finite_modulus_prime_counts": list(FINITE_MODULUS_PRIME_COUNTS),
                "window_length": WINDOW_CUTOFF,
                "block_lengths": list(BLOCK_LENGTHS),
            },
        },
        "exact": {
            "evidence_status": "PROVED",
            "periodic_point_theorem": {
                "statement": "The all-zero point is the only periodic point of X_sf.",
                "proof_ledger": [
                    "Let a nonzero point have period n and choose a supported residue in its period word.",
                    "Choose a rational prime p not dividing n (the algorithm uses the least such p).",
                    "Translation by n is invertible modulo p^2, so that supported arithmetic progression visits every residue modulo p^2.",
                    "This violates p^2-admissibility; hence no nonzero periodic point exists.",
                ],
                "brute_census": brute_rows,
                "all_brute_counts_equal_one": all(row["fixed_points"] == 1 for row in brute_rows),
                "all_witnesses_valid": all(bool(row["all_witnesses_valid"]) for row in brute_rows),
            },
            "primitive_orbit_ledger": [
                {"period": period, "primitive_orbits": count} for period, count in primitive_candidate.items()
            ],
            "artin_mazur_zeta": "zeta(z)=exp(sum_{n>=1} z^n/n)=1/(1-z)",
            "inverse_determinant": "D(z)=1-z",
            "finite_modulus_approximants": {
                "method": "exact inclusion-exclusion; independently brute-validated through the brute cutoff",
                "rows": approximant_rows,
                "all_brute_validations_pass": all_brute_validations_pass,
            },
            "parent_controls": {
                "full_binary_shift": "Fix(sigma^n)=2^n and zeta(z)=1/(1-2z)",
                "golden_mean_shift": "Fix(sigma^n)=tr([[1,1],[1,0]]^n)",
                "rows": parent_rows,
            },
        },
        "numerical": {"shuffled_finite_window_control": shuffled_window_control()},
        "controls_used": [
            "full binary parent shift",
            "golden-mean shift",
            "finite-prime-square modulus approximants",
            "seeded shuffled squarefree finite window",
        ],
        "stop_rule": {
            "triggered": True,
            "route_a_layer": "A1",
            "reason": "Only the all-zero periodic point survives, so high local word entropy cannot supply a primitive/repetition ledger.",
        },
        "route_b_invocation_allowed": False,
    }


def write_results(output_dir: Path) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = build_results()
    (output_dir / "sd_c02_results.json").write_text(
        json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    csv_path = output_dir / "sd_c02_periodic_census.csv"
    fields = [
        "candidate_id",
        "system",
        "prime_count",
        "period",
        "fixed_points",
        "method",
        "evidence_status",
        "seed",
        "precision",
        "cutoff",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in results["exact"]["parent_controls"]["rows"]:  # type: ignore[index]
            for system, key in (
                ("SD-C02", "candidate_fixed_points"),
                ("full_binary", "full_binary_fixed_points"),
                ("golden_mean", "golden_mean_fixed_points"),
            ):
                writer.writerow(
                    {
                        "candidate_id": CANDIDATE_ID,
                        "system": system,
                        "prime_count": "",
                        "period": row["period"],
                        "fixed_points": row[key],
                        "method": "exact theorem" if system == "SD-C02" else "exact matrix/formula",
                        "evidence_status": "PROVED",
                        "seed": MASTER_SEED,
                        "precision": "exact_integer",
                        "cutoff": EXACT_PERIOD_CUTOFF,
                    }
                )
        for row in results["exact"]["finite_modulus_approximants"]["rows"]:  # type: ignore[index]
            writer.writerow(
                {
                    "candidate_id": CANDIDATE_ID,
                    "system": "finite_modulus_approximant",
                    "prime_count": row["prime_count"],
                    "period": row["period"],
                    "fixed_points": row["fixed_points_inclusion_exclusion"],
                    "method": "exact inclusion-exclusion",
                    "evidence_status": "PROVED",
                    "seed": MASTER_SEED,
                    "precision": "exact_integer",
                    "cutoff": EXACT_PERIOD_CUTOFF,
                }
            )
    return results


if __name__ == "__main__":
    default_output = Path(__file__).resolve().parents[1] / "results"
    built = write_results(default_output)
    theorem = built["exact"]["periodic_point_theorem"]
    print(json.dumps({"candidate_id": CANDIDATE_ID, "passed": theorem["all_brute_counts_equal_one"]}))
