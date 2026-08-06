#!/usr/bin/env python3
"""Exact finite-field census for HCS-C03.

The experiment is intentionally elementary and exact: H_6 is represented as
a permutation of p^2 integer labels, all cycles are enumerated, and every
identity used in the local zeta factor is checked.  See c03_PROTOCOL.md for
the frozen experiment and decision rules.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import statistics
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence


A_VALUE = 6
DEFAULT_MAX_PRIME = 251
DEFAULT_FIX_N_MAX = 64
DEFAULT_DIRECT_FIX_N_MAX = 12
DEFAULT_RANDOM_REPLICATES = 16
DEFAULT_MASTER_SEED = 20260805
BAD_REDUCTION_PRIMES = {2, 3}
PRIMARY_UNIFORM_METRICS = (
    "num_cycles",
    "fixed_points",
    "largest_cycle_fraction",
    "short_point_mass_fraction",
)
PRIMARY_REVERSIBLE_METRICS = PRIMARY_UNIFORM_METRICS + (
    "symmetric_cycle_count",
    "symmetric_degree_fraction",
)
MASK64 = (1 << 64) - 1


class SplitMix64:
    """Small, fully specified 64-bit generator used only for controls."""

    def __init__(self, seed: int):
        self.state = seed & MASK64

    def next_u64(self) -> int:
        self.state = (self.state + 0x9E3779B97F4A7C15) & MASK64
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
        return (z ^ (z >> 31)) & MASK64

    def randbelow(self, upper: int) -> int:
        if upper <= 0:
            raise ValueError("upper must be positive")
        threshold = (1 << 64) % upper
        while True:
            value = self.next_u64()
            if value >= threshold:
                return value % upper

    def shuffle(self, values: list[int]) -> None:
        for i in range(len(values) - 1, 0, -1):
            j = self.randbelow(i + 1)
            values[i], values[j] = values[j], values[i]


def derived_seed(master_seed: int, prime: int, kind: str, replicate: int) -> int:
    payload = f"HCS-C03|{master_seed}|{prime}|{kind}|{replicate}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : limit + 1 : q] = b"\x00" * (
                ((limit - start) // q) + 1
            )
    return [q for q in range(2, limit + 1) if sieve[q]]


def state_index(q: int, r: int, prime: int) -> int:
    return q * prime + r


def state_pair(index: int, prime: int) -> tuple[int, int]:
    return divmod(index, prime)


def henon_image_index(index: int, prime: int, a_value: int = A_VALUE) -> int:
    q, r = state_pair(index, prime)
    return state_index((1 - a_value * q * q - r) % prime, q, prime)


def henon_inverse_index(index: int, prime: int, a_value: int = A_VALUE) -> int:
    capital_q, capital_p = state_pair(index, prime)
    return state_index(
        capital_p,
        (1 - a_value * capital_p * capital_p - capital_q) % prime,
        prime,
    )


def swap_index(index: int, prime: int) -> int:
    q, r = state_pair(index, prime)
    return state_index(r, q, prime)


def build_henon_permutation(prime: int, a_value: int = A_VALUE) -> list[int]:
    return [henon_image_index(i, prime, a_value) for i in range(prime * prime)]


def validate_henon_permutation(
    permutation: Sequence[int], prime: int, a_value: int = A_VALUE
) -> dict[str, bool]:
    n_points = prime * prime
    if len(permutation) != n_points:
        raise AssertionError("wrong permutation size")
    seen = bytearray(n_points)
    inverse_ok = True
    for source, target in enumerate(permutation):
        if not (0 <= target < n_points) or seen[target]:
            raise AssertionError("map is not a permutation")
        seen[target] = 1
        if henon_inverse_index(target, prime, a_value) != source:
            inverse_ok = False
    if not all(seen):
        raise AssertionError("permutation is not onto")
    if not inverse_ok:
        raise AssertionError("inverse formula failed")

    reversibility_ok = True
    for source in range(n_points):
        lhs = swap_index(permutation[swap_index(source, prime)], prime)
        rhs = henon_inverse_index(source, prime, a_value)
        if lhs != rhs:
            reversibility_ok = False
            break
    if not reversibility_ok:
        raise AssertionError("R H R = H^{-1} failed")
    return {
        "bijection": True,
        "inverse_formula": True,
        "reversibility": True,
    }


def inverse_permutation(permutation: Sequence[int]) -> list[int]:
    inverse = [-1] * len(permutation)
    for source, target in enumerate(permutation):
        if not (0 <= target < len(permutation)) or inverse[target] != -1:
            raise AssertionError("not a permutation")
        inverse[target] = source
    return inverse


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    result = 1
    remaining = n
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            if remaining % factor == 0:
                return 0
            result = -result
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        result = -result
    return result


def totient(n: int) -> int:
    result = n
    remaining = n
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            while remaining % factor == 0:
                remaining //= factor
            result -= result // factor
        factor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def decompose_permutation(
    permutation: Sequence[int],
    short_threshold: int,
    reversor: Sequence[int] | None = None,
) -> dict:
    n_points = len(permutation)
    visited = bytearray(n_points)
    cycle_id = [-1] * n_points
    cycle_lengths: list[int] = []
    representatives: list[int] = []

    for start in range(n_points):
        if visited[start]:
            continue
        cid = len(cycle_lengths)
        current = start
        length = 0
        while not visited[current]:
            visited[current] = 1
            cycle_id[current] = cid
            length += 1
            current = permutation[current]
        if current != start:
            raise AssertionError("cycle did not close at its unvisited start")
        cycle_lengths.append(length)
        representatives.append(start)

    counts = Counter(cycle_lengths)
    if sum(length * count for length, count in counts.items()) != n_points:
        raise AssertionError("cycle point total failed")
    metrics = basic_cycle_metrics(cycle_lengths, short_threshold)
    answer = {
        "cycle_lengths": cycle_lengths,
        "cycle_counts": counts,
        "metrics": metrics,
    }

    if reversor is None:
        return answer
    if len(reversor) != n_points:
        raise AssertionError("wrong reversor size")
    inverse = inverse_permutation(permutation)
    for source in range(n_points):
        if reversor[reversor[source]] != source:
            raise AssertionError("R is not an involution")
        if reversor[permutation[reversor[source]]] != inverse[source]:
            raise AssertionError("R P R = P^{-1} failed")

    symmetric_counts: Counter[int] = Counter()
    paired_pair_counts: Counter[int] = Counter()
    symmetric_ids: set[int] = set()
    partner_ids: list[int] = []
    for cid, representative in enumerate(representatives):
        partner = cycle_id[reversor[representative]]
        partner_ids.append(partner)
        if cycle_lengths[partner] != cycle_lengths[cid]:
            raise AssertionError("reversor changed cycle length")
        if partner == cid:
            symmetric_ids.add(cid)
            symmetric_counts[cycle_lengths[cid]] += 1
        elif cid < partner:
            paired_pair_counts[cycle_lengths[cid]] += 1
    for cid, partner in enumerate(partner_ids):
        if partner_ids[partner] != cid:
            raise AssertionError("cycle pairing is not involutive")
    all_lengths = set(counts) | set(symmetric_counts) | set(paired_pair_counts)
    for length in all_lengths:
        if counts[length] != symmetric_counts[length] + 2 * paired_pair_counts[length]:
            raise AssertionError("symmetric/paired cycle identity failed")

    second_involution = [permutation[reversor[i]] for i in range(n_points)]
    if any(second_involution[second_involution[i]] != i for i in range(n_points)):
        raise AssertionError("P R is not an involution")
    r_hits = [0] * len(cycle_lengths)
    i_hits = [0] * len(cycle_lengths)
    for state in range(n_points):
        cid = cycle_id[state]
        if reversor[state] == state:
            r_hits[cid] += 1
        if second_involution[state] == state:
            i_hits[cid] += 1

    pattern_counts: Counter[str] = Counter()
    for cid, length in enumerate(cycle_lengths):
        r_count = r_hits[cid]
        i_count = i_hits[cid]
        if cid not in symmetric_ids:
            if r_count or i_count:
                raise AssertionError("non-symmetric cycle met a fixed locus")
            continue
        if length % 2 == 1 and (r_count, i_count) == (1, 1):
            pattern_counts["odd_R1_I1"] += 1
        elif length % 2 == 0 and (r_count, i_count) == (2, 0):
            pattern_counts["even_R2_I0"] += 1
        elif length % 2 == 0 and (r_count, i_count) == (0, 2):
            pattern_counts["even_R0_I2"] += 1
        else:
            pattern_counts[f"other_R{r_count}_I{i_count}_parity{length % 2}"] += 1
    if any(key.startswith("other_") for key in pattern_counts):
        raise AssertionError("unexpected symmetric-cycle fixed-locus pattern")

    r_fixed_total = sum(r_hits)
    i_fixed_total = sum(i_hits)
    if 2 * len(symmetric_ids) != r_fixed_total + i_fixed_total:
        raise AssertionError("symmetric-cycle/fixed-locus count identity failed")

    symmetric_degree = sum(
        length * count for length, count in symmetric_counts.items()
    )
    paired_base_degree = sum(
        length * count for length, count in paired_pair_counts.items()
    )
    if symmetric_degree + 2 * paired_base_degree != n_points:
        raise AssertionError("symmetric/paired zeta degree failed")

    metrics.update(
        {
            "symmetric_cycle_count": sum(symmetric_counts.values()),
            "symmetric_degree": symmetric_degree,
            "symmetric_degree_fraction": symmetric_degree / n_points,
            "paired_cycle_pair_count": sum(paired_pair_counts.values()),
            "paired_base_degree": paired_base_degree,
        }
    )
    answer.update(
        {
            "symmetric_cycle_counts": symmetric_counts,
            "paired_pair_cycle_counts": paired_pair_counts,
            "symmetric_pattern_counts": pattern_counts,
            "second_involution_fixed_points": sum(
                1 for i, image in enumerate(second_involution) if i == image
            ),
        }
    )
    return answer


def basic_cycle_metrics(cycle_lengths: Sequence[int], short_threshold: int) -> dict:
    n_points = sum(cycle_lengths)
    counts = Counter(cycle_lengths)
    largest = max(cycle_lengths, default=0)
    short_mass = sum(length for length in cycle_lengths if length <= short_threshold)
    return {
        "num_cycles": len(cycle_lengths),
        "fixed_points": counts.get(1, 0),
        "largest_cycle": largest,
        "largest_cycle_fraction": largest / n_points if n_points else 0.0,
        "short_threshold": short_threshold,
        "short_cycle_count": sum(
            count for length, count in counts.items() if length <= short_threshold
        ),
        "short_point_mass": short_mass,
        "short_point_mass_fraction": short_mass / n_points if n_points else 0.0,
        "cycle_length_gcd": math.gcd(*cycle_lengths) if cycle_lengths else 0,
    }


def fixed_counts_from_cycles(
    cycle_counts: Counter[int], maximum_iterate: int
) -> list[int]:
    return [
        sum(length * cycle_counts.get(length, 0) for length in divisors(n))
        for n in range(1, maximum_iterate + 1)
    ]


def direct_fixed_counts(
    permutation: Sequence[int], maximum_iterate: int
) -> list[int]:
    n_points = len(permutation)
    current = list(range(n_points))
    answer: list[int] = []
    for _ in range(maximum_iterate):
        current = [permutation[state] for state in current]
        answer.append(sum(state == image for state, image in enumerate(current)))
    return answer


def cyclotomic_multiplicities(cycle_counts: Counter[int]) -> Counter[int]:
    answer: Counter[int] = Counter()
    for length, count in cycle_counts.items():
        for divisor in divisors(length):
            answer[divisor] += count
    return answer


def fixed_point_prediction(prime: int) -> dict:
    if prime == 2:
        return {"predicted_count": 0, "legendre_28": None, "case": "bad_p2"}
    if prime == 3:
        return {"predicted_count": 1, "legendre_28": None, "case": "bad_p3"}
    residue = 28 % prime
    if residue == 0:
        symbol = 0
    else:
        value = pow(residue, (prime - 1) // 2, prime)
        symbol = 1 if value == 1 else -1
    return {
        "predicted_count": 1 + symbol,
        "legendre_28": symbol,
        "case": "good_discriminant_zero" if symbol == 0 else "good_generic",
    }


def harmonic_cycle_theory(n_points: int) -> dict[str, float]:
    harmonic_1 = math.fsum(1.0 / k for k in range(1, n_points + 1))
    harmonic_2 = math.fsum(1.0 / (k * k) for k in range(1, n_points + 1))
    variance = harmonic_1 - harmonic_2
    return {
        "mean_num_cycles": harmonic_1,
        "variance_num_cycles": variance,
        "sd_num_cycles": math.sqrt(variance),
    }


def random_permutation(n_points: int, seed: int) -> list[int]:
    values = list(range(n_points))
    SplitMix64(seed).shuffle(values)
    return values


def random_involution(n_points: int, fixed_count: int, seed: int) -> list[int]:
    if not (0 <= fixed_count <= n_points) or (n_points - fixed_count) % 2:
        raise ValueError("invalid involution cycle type")
    labels = list(range(n_points))
    SplitMix64(seed).shuffle(labels)
    involution = [-1] * n_points
    for state in labels[:fixed_count]:
        involution[state] = state
    remainder = labels[fixed_count:]
    for offset in range(0, len(remainder), 2):
        left, right = remainder[offset], remainder[offset + 1]
        involution[left] = right
        involution[right] = left
    if any(involution[involution[i]] != i for i in range(n_points)):
        raise AssertionError("random involution construction failed")
    return involution


def percentile(values: Sequence[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("empty percentile")
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(ordered[lower])
    weight = position - lower
    return float(ordered[lower] * (1 - weight) + ordered[upper] * weight)


def summarize_control(values: Sequence[float]) -> dict[str, float]:
    return {
        "mean": statistics.fmean(values),
        "sd": statistics.pstdev(values),
        "minimum": min(values),
        "q025": percentile(values, 0.025),
        "median": percentile(values, 0.5),
        "q975": percentile(values, 0.975),
        "maximum": max(values),
    }


def compare_to_control(value: float, summary: dict[str, float]) -> dict:
    sd = summary["sd"]
    if sd > 0:
        z_score: float | None = (value - summary["mean"]) / sd
    else:
        z_score = 0.0 if value == summary["mean"] else None
    return {
        "z_score": z_score,
        "outside_empirical_95": value < summary["q025"] or value > summary["q975"],
        "outside_empirical_range": value < summary["minimum"] or value > summary["maximum"],
    }


def serialize_factor(counter: Counter[int]) -> list[dict[str, int]]:
    return [
        {"length": length, "multiplicity": counter[length]}
        for length in sorted(counter)
        if counter[length]
    ]


def run_prime(
    prime: int,
    random_replicates: int,
    master_seed: int,
    fix_n_max: int,
    direct_fix_n_max: int,
) -> tuple[dict, list[dict]]:
    n_points = prime * prime
    permutation = build_henon_permutation(prime)
    validation = validate_henon_permutation(permutation, prime)
    reversor = [swap_index(i, prime) for i in range(n_points)]
    decomposition = decompose_permutation(permutation, prime, reversor)
    cycle_counts: Counter[int] = decomposition["cycle_counts"]

    fixed_counts = fixed_counts_from_cycles(cycle_counts, fix_n_max)
    direct_counts = direct_fixed_counts(permutation, direct_fix_n_max)
    if fixed_counts[:direct_fix_n_max] != direct_counts:
        raise AssertionError("direct fixed counts disagree with cycle ledger")
    inversion_ok = True
    for n in range(1, fix_n_max + 1):
        primitive_points = sum(
            mobius(d) * fixed_counts[n // d - 1] for d in divisors(n)
        )
        if primitive_points != n * cycle_counts.get(n, 0):
            inversion_ok = False
            break
    if not inversion_ok:
        raise AssertionError("Möbius repetition identity failed")

    cyclotomic = cyclotomic_multiplicities(cycle_counts)
    cyclotomic_degree = sum(totient(d) * count for d, count in cyclotomic.items())
    if cyclotomic_degree != n_points:
        raise AssertionError("cyclotomic factor degree failed")

    prediction = fixed_point_prediction(prime)
    if prediction["predicted_count"] != decomposition["metrics"]["fixed_points"]:
        raise AssertionError("fixed-point discriminant prediction failed")

    control_rows: list[dict] = []
    uniform_metric_values = {metric: [] for metric in PRIMARY_UNIFORM_METRICS}
    reversible_metric_values = {
        metric: [] for metric in PRIMARY_REVERSIBLE_METRICS
    }
    second_fixed_count = decomposition["second_involution_fixed_points"]
    for replicate in range(random_replicates):
        uniform_seed = derived_seed(
            master_seed, prime, "uniform_permutation", replicate
        )
        uniform_perm = random_permutation(n_points, uniform_seed)
        uniform_decomp = decompose_permutation(uniform_perm, prime)
        uniform_metrics = uniform_decomp["metrics"]
        for metric in PRIMARY_UNIFORM_METRICS:
            uniform_metric_values[metric].append(uniform_metrics[metric])
        control_rows.append(
            {
                "p": prime,
                "kind": "uniform_permutation",
                "replicate": replicate,
                "seed": uniform_seed,
                **uniform_metrics,
                "symmetric_cycle_count": None,
                "symmetric_degree": None,
                "symmetric_degree_fraction": None,
                "paired_cycle_pair_count": None,
                "paired_base_degree": None,
            }
        )

        reversible_seed = derived_seed(
            master_seed, prime, "matched_reversible", replicate
        )
        sampled_involution = random_involution(
            n_points, second_fixed_count, reversible_seed
        )
        reversible_perm = [sampled_involution[reversor[i]] for i in range(n_points)]
        reversible_decomp = decompose_permutation(
            reversible_perm, prime, reversor
        )
        reversible_metrics = reversible_decomp["metrics"]
        for metric in PRIMARY_REVERSIBLE_METRICS:
            reversible_metric_values[metric].append(reversible_metrics[metric])
        control_rows.append(
            {
                "p": prime,
                "kind": "matched_reversible",
                "replicate": replicate,
                "seed": reversible_seed,
                **reversible_metrics,
            }
        )

    uniform_summary = {
        metric: summarize_control(values)
        for metric, values in uniform_metric_values.items()
    }
    reversible_summary = {
        metric: summarize_control(values)
        for metric, values in reversible_metric_values.items()
    }
    metrics = decomposition["metrics"]
    uniform_comparison = {
        metric: compare_to_control(metrics[metric], uniform_summary[metric])
        for metric in PRIMARY_UNIFORM_METRICS
    }
    reversible_comparison = {
        metric: compare_to_control(metrics[metric], reversible_summary[metric])
        for metric in PRIMARY_REVERSIBLE_METRICS
    }
    theory = harmonic_cycle_theory(n_points)
    theory["observed_num_cycles_z"] = (
        metrics["num_cycles"] - theory["mean_num_cycles"]
    ) / theory["sd_num_cycles"]

    record = {
        "p": prime,
        "n_points": n_points,
        "a_mod_p": A_VALUE % prime,
        "bad_reduction": prime in BAD_REDUCTION_PRIMES,
        "exceptional_fixed_discriminant": prime == 7,
        "map": "H_6(q,r)=(1-6q^2-r,q) over F_p",
        "inverse": "H_6^{-1}(Q,P)=(P,1-6P^2-Q)",
        "metrics": metrics,
        "cycle_counts": serialize_factor(cycle_counts),
        "fixed_counts_n_le_max": [
            {"iterate": n, "count": count}
            for n, count in enumerate(fixed_counts, start=1)
        ],
        "zeta": {
            "convention": "Z_p(u)=prod_l (1-u^l)^(-c_l,p)",
            "numerator": "1",
            "raw_denominator_factors": serialize_factor(cycle_counts),
            "cyclotomic_denominator_factors": serialize_factor(cyclotomic),
            "denominator_degree": n_points,
            "fixed_count_reconstruction": "Fix(H^n)=sum_{l|n} l*c_l,p",
            "reversibility_identity": "Z_p=Z_p,sym*(Z_p,pair)^2",
            "symmetric_denominator_factors": serialize_factor(
                decomposition["symmetric_cycle_counts"]
            ),
            "paired_base_denominator_factors": serialize_factor(
                decomposition["paired_pair_cycle_counts"]
            ),
        },
        "symmetry": {
            "reversor": "R(q,r)=(r,q)",
            "second_involution": "I=H_6 R",
            "R_fixed_points": prime,
            "I_fixed_points": second_fixed_count,
            "fixed_locus_cycle_patterns": dict(
                sorted(decomposition["symmetric_pattern_counts"].items())
            ),
        },
        "fixed_point_prediction": prediction,
        "uniform_permutation_theory": theory,
        "controls": {
            "replicates_per_ensemble": random_replicates,
            "uniform_permutation": uniform_summary,
            "matched_reversible": reversible_summary,
        },
        "control_comparison": {
            "uniform_permutation": uniform_comparison,
            "matched_reversible": reversible_comparison,
        },
        "self_checks": {
            **validation,
            "point_total": True,
            "direct_fix_through": direct_fix_n_max,
            "direct_fix_identity": True,
            "mobius_repetition_through": fix_n_max,
            "mobius_repetition_identity": True,
            "cyclotomic_degree": cyclotomic_degree,
            "cyclotomic_degree_identity": True,
            "symmetric_pair_factorization": True,
            "fixed_locus_patterns": True,
            "symmetric_cycle_fixed_locus_identity": True,
            "fixed_point_discriminant": True,
        },
    }
    return record, control_rows


def aggregate_effects(prime_records: Sequence[dict], ensemble: str) -> dict:
    metrics = (
        PRIMARY_UNIFORM_METRICS
        if ensemble == "uniform_permutation"
        else PRIMARY_REVERSIBLE_METRICS
    )
    answer: dict[str, dict] = {}
    for metric in metrics:
        z_values: list[float] = []
        outside = 0
        for record in prime_records:
            comparison = record["control_comparison"][ensemble][metric]
            if comparison["z_score"] is not None:
                z_values.append(comparison["z_score"])
            outside += int(comparison["outside_empirical_95"])
        positive = sum(value > 0 for value in z_values)
        negative = sum(value < 0 for value in z_values)
        valid = len(z_values)
        answer[metric] = {
            "valid_standardized_primes": valid,
            "mean_z": statistics.fmean(z_values) if z_values else None,
            "median_z": statistics.median(z_values) if z_values else None,
            "mean_absolute_z": (
                statistics.fmean(abs(value) for value in z_values)
                if z_values
                else None
            ),
            "common_sign_fraction": max(positive, negative) / valid if valid else None,
            "outside_empirical_95_count": outside,
            "outside_empirical_95_fraction": outside / len(prime_records),
        }
    return answer


def classify_bulk_signal(matched_aggregate: dict) -> dict:
    no_bulk = True
    candidate_metrics: list[str] = []
    for metric, values in matched_aggregate.items():
        mean_abs = values["mean_absolute_z"]
        outside = values["outside_empirical_95_fraction"]
        if mean_abs is None or mean_abs >= 1 or outside > 0.20:
            no_bulk = False
        mean_z = values["mean_z"]
        common_sign = values["common_sign_fraction"]
        if (
            mean_z is not None
            and abs(mean_z) >= 2
            and common_sign is not None
            and common_sign >= 0.75
            and outside >= 0.50
        ):
            candidate_metrics.append(metric)
    if no_bulk:
        empirical_label = "NO_BULK_ANOMALY"
    elif candidate_metrics:
        empirical_label = "CANDIDATE_NONRANDOM_SIGNAL"
    else:
        empirical_label = "INCONCLUSIVE_BULK_DIFFERENCE"
    return {
        "empirical_label": empirical_label,
        "candidate_metrics": candidate_metrics,
        "route_a_ceiling": "LOCAL_FACTORS_ONLY",
        "formal_promotion": False,
        "reason": (
            "The census proves exact local factors only. No canonical global "
            "Euler product, convergence theorem, analytic continuation, or "
            "target divisor is established by this computation."
        ),
    }


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_outputs(
    output_directory: Path,
    payload: dict,
    control_rows: Sequence[dict],
) -> None:
    output_directory.mkdir(parents=True, exist_ok=True)
    json_path = output_directory / "c03_census.json"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    summary_fields = [
        "p",
        "bad_reduction",
        "exceptional_fixed_discriminant",
        "n_points",
        "num_cycles",
        "fixed_points",
        "predicted_fixed_points",
        "largest_cycle",
        "largest_cycle_fraction",
        "short_threshold",
        "short_cycle_count",
        "short_point_mass",
        "short_point_mass_fraction",
        "symmetric_cycle_count",
        "symmetric_degree",
        "symmetric_degree_fraction",
        "paired_cycle_pair_count",
        "paired_base_degree",
        "uniform_theory_cycle_z",
    ]
    for ensemble, metrics in (
        ("uniform", PRIMARY_UNIFORM_METRICS),
        ("reversible", PRIMARY_REVERSIBLE_METRICS),
    ):
        for metric in metrics:
            summary_fields.extend(
                [
                    f"{ensemble}_{metric}_mean",
                    f"{ensemble}_{metric}_sd",
                    f"{ensemble}_{metric}_z",
                    f"{ensemble}_{metric}_outside95",
                ]
            )
    with (output_directory / "c03_prime_summary.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fields)
        writer.writeheader()
        for record in payload["primes"]:
            metrics = record["metrics"]
            row = {
                "p": record["p"],
                "bad_reduction": record["bad_reduction"],
                "exceptional_fixed_discriminant": record[
                    "exceptional_fixed_discriminant"
                ],
                "n_points": record["n_points"],
                **metrics,
                "predicted_fixed_points": record["fixed_point_prediction"][
                    "predicted_count"
                ],
                "uniform_theory_cycle_z": record["uniform_permutation_theory"][
                    "observed_num_cycles_z"
                ],
            }
            for short_name, ensemble in (
                ("uniform", "uniform_permutation"),
                ("reversible", "matched_reversible"),
            ):
                for metric, summary in record["controls"][ensemble].items():
                    row[f"{short_name}_{metric}_mean"] = summary["mean"]
                    row[f"{short_name}_{metric}_sd"] = summary["sd"]
                    comparison = record["control_comparison"][ensemble][metric]
                    row[f"{short_name}_{metric}_z"] = comparison["z_score"]
                    row[f"{short_name}_{metric}_outside95"] = comparison[
                        "outside_empirical_95"
                    ]
            writer.writerow({field: row.get(field) for field in summary_fields})

    with (output_directory / "c03_cycle_counts.csv").open(
        "w", newline=""
    ) as handle:
        fields = ["p", "length", "count", "symmetric_count", "paired_pair_count"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in payload["primes"]:
            raw = {
                item["length"]: item["multiplicity"]
                for item in record["zeta"]["raw_denominator_factors"]
            }
            symmetric = {
                item["length"]: item["multiplicity"]
                for item in record["zeta"]["symmetric_denominator_factors"]
            }
            paired = {
                item["length"]: item["multiplicity"]
                for item in record["zeta"]["paired_base_denominator_factors"]
            }
            for length in sorted(raw):
                writer.writerow(
                    {
                        "p": record["p"],
                        "length": length,
                        "count": raw[length],
                        "symmetric_count": symmetric.get(length, 0),
                        "paired_pair_count": paired.get(length, 0),
                    }
                )

    with (output_directory / "c03_fix_counts.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=["p", "iterate", "fix_count"])
        writer.writeheader()
        for record in payload["primes"]:
            for item in record["fixed_counts_n_le_max"]:
                writer.writerow(
                    {
                        "p": record["p"],
                        "iterate": item["iterate"],
                        "fix_count": item["count"],
                    }
                )

    control_fields = [
        "p",
        "kind",
        "replicate",
        "seed",
        "num_cycles",
        "fixed_points",
        "largest_cycle",
        "largest_cycle_fraction",
        "short_threshold",
        "short_cycle_count",
        "short_point_mass",
        "short_point_mass_fraction",
        "cycle_length_gcd",
        "symmetric_cycle_count",
        "symmetric_degree",
        "symmetric_degree_fraction",
        "paired_cycle_pair_count",
        "paired_base_degree",
    ]
    with (output_directory / "c03_random_controls.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=control_fields)
        writer.writeheader()
        for row in control_rows:
            writer.writerow({field: row.get(field) for field in control_fields})


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-prime", type=int, default=DEFAULT_MAX_PRIME)
    parser.add_argument(
        "--random-replicates", type=int, default=DEFAULT_RANDOM_REPLICATES
    )
    parser.add_argument("--master-seed", type=int, default=DEFAULT_MASTER_SEED)
    parser.add_argument("--fix-n-max", type=int, default=DEFAULT_FIX_N_MAX)
    parser.add_argument(
        "--direct-fix-n-max", type=int, default=DEFAULT_DIRECT_FIX_N_MAX
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results" / "c03_finite_field",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_argument_parser().parse_args(argv)
    if args.random_replicates <= 0:
        raise ValueError("random replicates must be positive")
    if args.direct_fix_n_max > args.fix_n_max:
        raise ValueError("direct fixed window exceeds stored fixed window")
    prime_list = primes_up_to(args.max_prime)
    started = time.perf_counter()
    records: list[dict] = []
    all_controls: list[dict] = []
    for index, prime in enumerate(prime_list, start=1):
        prime_started = time.perf_counter()
        record, controls = run_prime(
            prime,
            args.random_replicates,
            args.master_seed,
            args.fix_n_max,
            args.direct_fix_n_max,
        )
        record["elapsed_seconds"] = time.perf_counter() - prime_started
        records.append(record)
        all_controls.extend(controls)
        print(
            f"[{index:02d}/{len(prime_list):02d}] p={prime:3d} "
            f"cycles={record['metrics']['num_cycles']:4d} "
            f"sym={record['metrics']['symmetric_cycle_count']:4d} "
            f"elapsed={record['elapsed_seconds']:.3f}s",
            flush=True,
        )

    good_records = [record for record in records if not record["bad_reduction"]]
    uniform_aggregate = aggregate_effects(good_records, "uniform_permutation")
    reversible_aggregate = aggregate_effects(good_records, "matched_reversible")
    decision = classify_bulk_signal(reversible_aggregate)
    script_path = Path(__file__).resolve()
    protocol_path = script_path.with_name("c03_PROTOCOL.md")
    elapsed = time.perf_counter() - started
    payload = {
        "schema_version": "HCS-C03-v1",
        "candidate_id": "HCS-C03",
        "status": "PILOT_LOCAL_CENSUS",
        "frozen_configuration": {
            "a_value": A_VALUE,
            "max_prime": args.max_prime,
            "fix_n_max": args.fix_n_max,
            "direct_fix_n_max": args.direct_fix_n_max,
            "random_replicates_per_ensemble": args.random_replicates,
            "master_seed": args.master_seed,
            "bad_reduction_primes": sorted(BAD_REDUCTION_PRIMES),
            "short_cycle_threshold": "p=sqrt(number of states)",
            "primary_uniform_metrics": list(PRIMARY_UNIFORM_METRICS),
            "primary_matched_reversible_metrics": list(
                PRIMARY_REVERSIBLE_METRICS
            ),
        },
        "run_metadata": {
            "command": " ".join([sys.executable, str(script_path), *sys.argv[1:]]),
            "python": sys.version,
            "platform": platform.platform(),
            "elapsed_seconds": elapsed,
            "script_sha256": file_sha256(script_path),
            "protocol_sha256": (
                file_sha256(protocol_path) if protocol_path.exists() else None
            ),
        },
        "prime_count": len(records),
        "good_prime_count": len(good_records),
        "total_phase_points": sum(record["n_points"] for record in records),
        "primes": records,
        "good_prime_aggregates": {
            "uniform_permutation": uniform_aggregate,
            "matched_reversible": reversible_aggregate,
        },
        "decision": decision,
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_REJECTED",
        },
        "data_firewall": {
            "riemann_zeros_used": False,
            "target_prime_weights_used": False,
            "post_hoc_normalization_used": False,
        },
    }
    write_outputs(args.output, payload, all_controls)
    print(
        f"wrote {args.output} in {elapsed:.3f}s; "
        f"decision={decision['empirical_label']}; "
        "Route-A ceiling=LOCAL_FACTORS_ONLY",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
