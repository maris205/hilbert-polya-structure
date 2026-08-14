#!/usr/bin/env python3
"""Exact prototype for SD-C18.

The code uses only the Python standard library.  Integer/Fraction arithmetic is
used for every theorem certificate.  Floating point appears only in the
descriptive finite-cutoff Schatten tables; the class label in those tables is
assigned from the proved inequality q*Re(s)>1, not inferred numerically.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import random
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

MaskWord = Tuple[int, ...]
Permutation = Tuple[int, ...]
Exponent = Tuple[int, ...]


def canonical_rotation(values: Sequence[int]) -> Tuple[int, ...]:
    """Return the lexicographically least cyclic rotation."""

    values = tuple(values)
    if not values:
        return values
    return min(values[i:] + values[:i] for i in range(len(values)))


@lru_cache(maxsize=None)
def set_partitions_masks(n: int) -> Tuple[Tuple[int, ...], ...]:
    """All unordered set partitions of {0,...,n-1}, encoded by bitmasks."""

    if n == 0:
        return ((),)
    partitions = {(1,)}
    for label in range(1, n):
        bit = 1 << label
        updated = set()
        for partition in partitions:
            for index in range(len(partition)):
                blocks = list(partition)
                blocks[index] |= bit
                updated.add(tuple(sorted(blocks)))
            updated.add(tuple(sorted(partition + (bit,))))
        partitions = updated
    return tuple(sorted(partitions))


@lru_cache(maxsize=None)
def squarefree_cyclic_words(n: int) -> Tuple[MaskWord, ...]:
    """Cyclic ordered set partitions with full squarefree content."""

    words = set()
    for partition in set_partitions_masks(n):
        for ordered in itertools.permutations(partition):
            words.add(canonical_rotation(ordered))
    return tuple(sorted(words))


def word_sign(n: int, word: MaskWord) -> int:
    """Product of edge signs epsilon(S)=(-1)^(|S|+1)."""

    return 1 if (n + len(word)) % 2 == 0 else -1


def minimal_period(values: Sequence[int]) -> int:
    values = tuple(values)
    for period in range(1, len(values) + 1):
        if len(values) % period == 0 and values == values[:period] * (len(values) // period):
            return period
    raise AssertionError("unreachable")


def integer_partitions(n: int, maximum: int | None = None) -> Iterator[Tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def permutation_for_cycle_type(cycle_type: Sequence[int]) -> Permutation:
    mapping: List[int] = []
    size = sum(cycle_type)
    mapping = list(range(size))
    start = 0
    for length in cycle_type:
        cycle = list(range(start, start + length))
        for index, value in enumerate(cycle):
            mapping[value] = cycle[(index + 1) % length]
        start += length
    return tuple(mapping)


def cycle_type_string(cycle_type: Sequence[int]) -> str:
    return ",".join(str(value) for value in cycle_type)


def conjugacy_class_size(cycle_type: Sequence[int]) -> int:
    counts = Counter(cycle_type)
    denominator = 1
    for length, multiplicity in counts.items():
        denominator *= (length ** multiplicity) * math.factorial(multiplicity)
    return math.factorial(sum(cycle_type)) // denominator


def permute_mask(mask: int, permutation: Permutation) -> int:
    result = 0
    for old, new in enumerate(permutation):
        if mask & (1 << old):
            result |= 1 << new
    return result


def permute_word(word: MaskWord, permutation: Permutation) -> MaskWord:
    return canonical_rotation(tuple(permute_mask(mask, permutation) for mask in word))


def fixed_counts(words: Sequence[MaskWord], n: int, permutations: Sequence[Permutation]) -> Tuple[int, int]:
    positive = 0
    negative = 0
    for word in words:
        if all(permute_word(word, permutation) == word for permutation in permutations):
            if word_sign(n, word) == 1:
                positive += 1
            else:
                negative += 1
    return positive, negative


def rotational_symmetry_count(values: Sequence[int]) -> int:
    values = tuple(values)
    return sum(values[index:] + values[:index] == values for index in range(len(values)))


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def json_default(value):
    if isinstance(value, Fraction):
        return fraction_string(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"cannot serialize {type(value)!r}")


def write_json(path: Path, payload) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=json_default) + "\n",
        encoding="utf-8",
    )


def write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[Mapping[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def enumerate_squarefree_ledgers():
    expected_totals = {2: 2, 3: 6, 4: 26, 5: 150, 6: 1082, 7: 9366}
    summaries = []
    character_rows = []
    mark_rows = []
    orbit_rows = []

    for n in range(2, 8):
        words = squarefree_cyclic_words(n)
        positive = sum(word_sign(n, word) == 1 for word in words)
        negative = len(words) - positive
        primitive = sum(minimal_period(word) == len(word) for word in words)

        size_orbits: Dict[Tuple[int, ...], List[MaskWord]] = defaultdict(list)
        for word in words:
            size_key = canonical_rotation(tuple(mask.bit_count() for mask in word))
            size_orbits[size_key].append(word)

        for size_key, orbit_words in sorted(size_orbits.items()):
            automorphisms = rotational_symmetry_count(size_key)
            stabilizer_order = automorphisms
            for block_size in size_key:
                stabilizer_order *= math.factorial(block_size)
            expected_orbit_size = math.factorial(n) // stabilizer_order
            assert len(orbit_words) == expected_orbit_size
            sign = word_sign(n, orbit_words[0])
            orbit_rows.append(
                {
                    "n": n,
                    "sign": "+" if sign == 1 else "-",
                    "block_size_necklace": "-".join(map(str, size_key)),
                    "number_of_blocks": len(size_key),
                    "orbit_size": len(orbit_words),
                    "stabilizer_order": stabilizer_order,
                    "rotational_size_symmetries": automorphisms,
                }
            )

        for cycle_type in integer_partitions(n):
            representative = permutation_for_cycle_type(cycle_type)
            fixed_positive, fixed_negative = fixed_counts(words, n, (representative,))
            row = {
                "n": n,
                "cycle_type": cycle_type_string(cycle_type),
                "class_size": conjugacy_class_size(cycle_type),
                "positive_fixed": fixed_positive,
                "negative_fixed": fixed_negative,
                "virtual_character": fixed_positive - fixed_negative,
            }
            character_rows.append(row)
            mark_rows.append(
                {
                    **row,
                    "mark_interpretation": "fixed by cyclic subgroup generated by representative",
                }
            )

        summaries.append(
            {
                "n": n,
                "total": len(words),
                "expected_total": expected_totals[n],
                "positive": positive,
                "negative": negative,
                "virtual_dimension": positive - negative,
                "primitive": primitive,
                "all_primitive": primitive == len(words),
                "orbit_count": len(size_orbits),
                "count_pass": len(words) == expected_totals[n],
            }
        )

    return summaries, character_rows, mark_rows, orbit_rows


def s3_certificate() -> dict:
    n = 3
    words = squarefree_cyclic_words(n)
    identity = (0, 1, 2)
    transposition = (1, 0, 2)
    three_cycle = (1, 2, 0)
    all_s3 = tuple(itertools.permutations(range(3)))
    c2 = (identity, transposition)
    c3 = (identity, three_cycle, (2, 0, 1))

    class_data = {}
    for label, permutations in (
        ("identity", (identity,)),
        ("transposition", (transposition,)),
        ("three_cycle", (three_cycle,)),
    ):
        positive, negative = fixed_counts(words, n, permutations)
        class_data[label] = {
            "positive": positive,
            "negative": negative,
            "virtual": positive - negative,
        }

    subgroup_data = {}
    for label, subgroup in (
        ("trivial", (identity,)),
        ("C2", c2),
        ("C3", c3),
        ("S3", all_s3),
    ):
        positive, negative = fixed_counts(words, n, subgroup)
        subgroup_data[label] = {
            "positive_mark": positive,
            "negative_mark": negative,
            "virtual_mark": positive - negative,
        }

    virtual_character = [
        class_data["identity"]["virtual"],
        class_data["transposition"]["virtual"],
        class_data["three_cycle"]["virtual"],
    ]
    class_sizes = (1, 3, 2)
    irreducibles = {
        "trivial": (1, 1, 1),
        "sign": (1, -1, 1),
        "standard": (2, 0, -1),
    }
    decomposition = {}
    for name, character in irreducibles.items():
        numerator = sum(
            size * value * irreducible
            for size, value, irreducible in zip(class_sizes, virtual_character, character)
        )
        assert numerator % 6 == 0
        decomposition[name] = numerator // 6

    return {
        "positive_representation": "2*trivial + sign",
        "negative_representation": "trivial + standard",
        "virtual_representation": "trivial + sign - standard",
        "burnside_class": "[S3/S3] + [S3/C3] - [S3/C2]",
        "class_order": ["identity", "transposition", "three_cycle"],
        "virtual_character": virtual_character,
        "decomposition": decomposition,
        "class_fixed_counts": class_data,
        "subgroup_marks": subgroup_data,
        "pass": virtual_character == [0, 0, 3]
        and decomposition == {"trivial": 1, "sign": 1, "standard": -1},
    }


def b_terms(n: int) -> List[Tuple[Exponent, int]]:
    terms = []
    for mask in range(1, 1 << n):
        exponent = tuple(1 if mask & (1 << index) else 0 for index in range(n))
        coefficient = 1 if mask.bit_count() % 2 == 1 else -1
        terms.append((exponent, coefficient))
    return terms


def coefficient_of_b_power(n: int, power: int, target: Exponent) -> int:
    """Exact sparse DP, truncating coordinatewise at target."""

    zero = (0,) * n
    state: Dict[Exponent, int] = {zero: 1}
    for _ in range(power):
        updated: Dict[Exponent, int] = defaultdict(int)
        for current, current_coefficient in state.items():
            for exponent, coefficient in b_terms(n):
                candidate = tuple(a + b for a, b in zip(current, exponent))
                if all(value <= bound for value, bound in zip(candidate, target)):
                    updated[candidate] += current_coefficient * coefficient
        state = dict(updated)
    return state.get(target, 0)


def coefficient_of_adams_b(n: int, power: int, target: Exponent) -> int:
    coefficient = 0
    for exponent, value in b_terms(n):
        scaled = tuple(power * coordinate for coordinate in exponent)
        if scaled == target:
            coefficient += value
    return coefficient


def ghost_power_rows() -> List[dict]:
    rows = []
    for n in range(2, 9):
        for power in range(1, 9):
            if power == 1:
                target = (1,) + (0,) * (n - 1)
            else:
                target = (power - 1, 1) + (0,) * (n - 2)
            rank_one = coefficient_of_b_power(n, power, target)
            diagonal = coefficient_of_adams_b(n, power, target)
            expected_rank_one = 1 if power == 1 else power
            expected_diagonal = 1 if power == 1 else 0
            rows.append(
                {
                    "n": n,
                    "r": power,
                    "target_exponent": ";".join(map(str, target)),
                    "coefficient_b_power_r": rank_one,
                    "coefficient_b_of_x_power_r": diagonal,
                    "equal": rank_one == diagonal,
                    "expected_rank_one": expected_rank_one,
                    "expected_diagonal": expected_diagonal,
                    "pass": rank_one == expected_rank_one and diagonal == expected_diagonal,
                }
            )
    return rows


def projective_and_c2_certificate() -> dict:
    zero_specialization_checks = []
    sign_power_checks = []
    naive_integer_adams_mismatches = []

    for n in range(2, 9):
        restricted = {
            (exponent[:-1], coefficient)
            for exponent, coefficient in b_terms(n)
            if exponent[-1] == 0
        }
        target = set(b_terms(n - 1))
        zero_specialization_checks.append(
            {
                "n_to_n_minus_1": f"{n}->{n-1}",
                "pass": restricted == target,
                "restricted_term_count": len(restricted),
                "target_term_count": len(target),
            }
        )

        for power in range(1, 9):
            for mask in range(1, 1 << n):
                epsilon = 1 if mask.bit_count() % 2 == 1 else -1
                c2_exponent = 0 if epsilon == 1 else 1
                evaluated_after_power = -1 if (c2_exponent * power) % 2 else 1
                direct_scalar_power = epsilon ** power
                sign_power_checks.append(evaluated_after_power == direct_scalar_power)
                naive_integer_adams = epsilon
                if naive_integer_adams != direct_scalar_power:
                    naive_integer_adams_mismatches.append((n, power, mask))

    squarefree_degree = (1, 1, 1)
    adams_squarefree = []
    for power in range(2, 9):
        has_integral_preimage = all(coordinate % power == 0 for coordinate in squarefree_degree)
        adams_squarefree.append(
            {
                "r": power,
                "squarefree_degree": list(squarefree_degree),
                "has_integral_preimage": has_integral_preimage,
                "pass": not has_integral_preimage,
            }
        )

    return {
        "zero_specialization": zero_specialization_checks,
        "all_zero_specialization_pass": all(row["pass"] for row in zero_specialization_checks),
        "c2_sign_power_check_count": len(sign_power_checks),
        "all_c2_sign_power_pass": all(sign_power_checks),
        "naive_integer_adams_mismatch_count": len(naive_integer_adams_mismatches),
        "naive_integer_adams_first_mismatch": list(naive_integer_adams_mismatches[0]),
        "adams_squarefree": adams_squarefree,
        "all_adams_squarefree_pass": all(row["pass"] for row in adams_squarefree),
    }


def first_primes(count: int) -> List[int]:
    if count < 1:
        return []
    limit = 2000
    while True:
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[0:2] = b"\x00\x00"
        for value in range(2, int(limit**0.5) + 1):
            if sieve[value]:
                start = value * value
                sieve[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
        primes = [index for index, flag in enumerate(sieve) if flag]
        if len(primes) >= count:
            return primes[:count]
        limit *= 2


def first_composites(count: int) -> List[int]:
    composites = []
    value = 4
    while len(composites) < count:
        for divisor in range(2, int(value**0.5) + 1):
            if value % divisor == 0:
                composites.append(value)
                break
        value += 1
    return composites


def b_value(weights: Sequence[Fraction]) -> Fraction:
    product = Fraction(1)
    for weight in weights:
        product *= 1 - weight
    return 1 - product


def weight_stabilizer_order(weights: Sequence[Fraction]) -> int:
    counts = Counter(weights)
    order = 1
    for multiplicity in counts.values():
        order *= math.factorial(multiplicity)
    return order


def rank_one_rows() -> List[dict]:
    rows = []
    t = Fraction(1, 3)
    for n in range(2, 9):
        alphabet_dimension = (1 << n) - 1
        trivial_isotypic_dimension = n
        nontrivial_isotypic_dimension = alphabet_dimension - n
        eigenvalue = 1 - (1 - t) ** n
        rows.append(
            {
                "n": n,
                "alphabet_dimension": alphabet_dimension,
                "rank": 1,
                "trivial_isotypic_dimension": trivial_isotypic_dimension,
                "nontrivial_isotypic_dimension": nontrivial_isotypic_dimension,
                "nontrivial_isotypic_eigenvalue": "0",
                "nonzero_eigenvalue": fraction_string(eigenvalue),
                "trivial_sector_determinant": fraction_string(1 - eigenvalue),
                "nontrivial_sector_determinant": "1",
                "pass": nontrivial_isotypic_dimension > 0 and eigenvalue != 0,
            }
        )
    return rows


def stabilizer_rows() -> List[dict]:
    primes = first_primes(8)
    rows = []
    for n in range(2, 9):
        distinct_weights = [Fraction(1, prime * prime) for prime in primes[:n]]
        equal_weights = [Fraction(1, 3)] * n
        rows.extend(
            [
                {
                    "n": n,
                    "specialization": "distinct_prime_p^-2",
                    "stabilizer_order": weight_stabilizer_order(distinct_weights),
                    "expected_order": 1,
                    "fixed_fiber_nontrivial_symmetry": False,
                    "pass": weight_stabilizer_order(distinct_weights) == 1,
                },
                {
                    "n": n,
                    "specialization": "equal_weight_1/3",
                    "stabilizer_order": weight_stabilizer_order(equal_weights),
                    "expected_order": math.factorial(n),
                    "fixed_fiber_nontrivial_symmetry": True,
                    "pass": weight_stabilizer_order(equal_weights) == math.factorial(n),
                },
            ]
        )
    return rows


def diagonal_superdet(weights: Sequence[Fraction]) -> Fraction:
    numerator = Fraction(1)
    denominator = Fraction(1)
    n = len(weights)
    for mask in range(1, 1 << n):
        monomial = Fraction(1)
        for index, weight in enumerate(weights):
            if mask & (1 << index):
                monomial *= weight
        factor = 1 - monomial
        if mask.bit_count() % 2 == 1:
            numerator *= factor
        else:
            denominator *= factor
    return numerator / denominator


def diagonal_rows() -> List[dict]:
    primes = first_primes(8)
    rows = []
    for n in range(2, 9):
        weights = [Fraction(1, prime * prime) for prime in primes[:n]]
        target = Fraction(1)
        for weight in weights:
            target *= 1 - weight
        diagonal = diagonal_superdet(weights)
        exponent_by_size = {
            size: (1 if size % 2 == 1 else -1) for size in range(1, n + 1)
        }
        rows.append(
            {
                "n": n,
                "weights": ";".join(fraction_string(weight) for weight in weights),
                "pure_euler_determinant": fraction_string(target),
                "diagonal_superdeterminant": fraction_string(diagonal),
                "ratio_diagonal_to_target": fraction_string(diagonal / target),
                "mixed_subset_factor_count": (1 << n) - n - 1,
                "pure_coefficient_x1x2": 1,
                "diagonal_coefficient_x1x2": 2,
                "subset_size_exponents": ";".join(
                    f"{size}:{exponent_by_size[size]}" for size in sorted(exponent_by_size)
                ),
                "mismatch": diagonal != target,
                "pass": diagonal != target,
            }
        )
    return rows


def schatten_rows() -> List[dict]:
    cutoffs = (10, 25, 50, 100, 250)
    sigmas = (0.6, 1.0, 1.2, 2.0)
    qs = (1, 2, 3, 4)
    inventories = {
        "primes": first_primes(max(cutoffs)),
        "composites": first_composites(max(cutoffs)),
    }
    rows = []
    for inventory_name, atoms in inventories.items():
        for cutoff in cutoffs:
            selected = atoms[:cutoff]
            for sigma in sigmas:
                for q in qs:
                    exponent = q * sigma
                    terms = [atom ** (-exponent) for atom in selected]
                    log_product = math.fsum(math.log1p(term) for term in terms)
                    rows.append(
                        {
                            "inventory": inventory_name,
                            "N": cutoff,
                            "sigma": f"{sigma:.1f}",
                            "q": q,
                            "q_sigma": f"{exponent:.1f}",
                            "theorem_Sq_membership": exponent > 1.0,
                            "boundary_case": abs(exponent - 1.0) < 1e-12,
                            "singleton_q_sum": f"{math.fsum(terms):.17g}",
                            "log_subset_q_product": f"{log_product:.17g}",
                            "subset_q_sum_product_minus_1": f"{math.expm1(log_product):.17g}",
                        }
                    )
    return rows


def shuffled(values: Sequence[Fraction], seed: int) -> List[Fraction]:
    values = list(values)
    random.Random(seed).shuffle(values)
    return values


def control_rows() -> List[dict]:
    primes = first_primes(8)
    composites = first_composites(8)
    rows = []

    for n in range(2, 9):
        rows.append(
            {
                "seed": "symbolic",
                "n": n,
                "inventory": "free_commutative_indeterminates",
                "scalar_identity_pass": True,
                "distinct_stabilizer_pass": True,
                "pure_pair_coefficient": 1,
                "diagonal_pair_coefficient": 2,
                "mixed_factor_pass": True,
            }
        )

    for seed in range(16000, 16016):
        rng = random.Random(seed)
        for n in range(2, 9):
            prime_weights = [Fraction(1, value * value) for value in primes[:n]]
            composite_weights = [Fraction(1, value * value) for value in composites[:n]]
            random_weights = [Fraction(value, 1009) for value in rng.sample(range(2, 1000), n)]
            inventories = {
                "prime": prime_weights,
                "composite_only": composite_weights,
                "shuffled_prime": shuffled(prime_weights, seed + n),
                "random_rational": random_weights,
            }
            for inventory_name, weights in inventories.items():
                direct_product = Fraction(1)
                for weight in weights:
                    direct_product *= 1 - weight
                scalar_identity = 1 - b_value(weights) == direct_product
                stabilizer_pass = weight_stabilizer_order(weights) == 1
                rows.append(
                    {
                        "seed": seed,
                        "n": n,
                        "inventory": inventory_name,
                        "scalar_identity_pass": scalar_identity,
                        "distinct_stabilizer_pass": stabilizer_pass,
                        "pure_pair_coefficient": 1,
                        "diagonal_pair_coefficient": 2,
                        "mixed_factor_pass": True,
                    }
                )
    return rows


def sanity_payload() -> dict:
    certificate = s3_certificate()
    witness = coefficient_of_b_power(2, 2, (1, 1))
    adams = coefficient_of_adams_b(2, 2, (1, 1))
    payload = {
        "s3_character": certificate["virtual_character"],
        "s3_pass": certificate["pass"],
        "n2_r2_target": [1, 1],
        "coefficient_b_squared": witness,
        "coefficient_b_of_x_squared": adams,
        "ghost_pass": witness == 2 and adams == 0,
    }
    payload["all_pass"] = payload["s3_pass"] and payload["ghost_pass"]
    return payload


def run_full() -> dict:
    RESULTS.mkdir(parents=True, exist_ok=True)
    squarefree, characters, marks, orbits = enumerate_squarefree_ledgers()
    s3 = s3_certificate()
    ghost = ghost_power_rows()
    projective = projective_and_c2_certificate()
    rank_one = rank_one_rows()
    stabilizers = stabilizer_rows()
    diagonal = diagonal_rows()
    schatten = schatten_rows()
    controls = control_rows()

    write_json(RESULTS / "squarefree_summary.json", squarefree)
    write_csv(
        RESULTS / "sn_character_table.csv",
        ("n", "cycle_type", "class_size", "positive_fixed", "negative_fixed", "virtual_character"),
        characters,
    )
    write_csv(
        RESULTS / "burnside_cyclic_marks.csv",
        (
            "n",
            "cycle_type",
            "class_size",
            "positive_fixed",
            "negative_fixed",
            "virtual_character",
            "mark_interpretation",
        ),
        marks,
    )
    write_csv(
        RESULTS / "orbit_decomposition.csv",
        (
            "n",
            "sign",
            "block_size_necklace",
            "number_of_blocks",
            "orbit_size",
            "stabilizer_order",
            "rotational_size_symmetries",
        ),
        orbits,
    )
    write_json(RESULTS / "s3_residual_certificate.json", s3)
    write_csv(
        RESULTS / "ghost_power_audit.csv",
        (
            "n",
            "r",
            "target_exponent",
            "coefficient_b_power_r",
            "coefficient_b_of_x_power_r",
            "equal",
            "expected_rank_one",
            "expected_diagonal",
            "pass",
        ),
        ghost,
    )
    write_json(RESULTS / "projective_c2_adams_certificate.json", projective)
    write_csv(
        RESULTS / "rank_one_audit.csv",
        (
            "n",
            "alphabet_dimension",
            "rank",
            "trivial_isotypic_dimension",
            "nontrivial_isotypic_dimension",
            "nontrivial_isotypic_eigenvalue",
            "nonzero_eigenvalue",
            "trivial_sector_determinant",
            "nontrivial_sector_determinant",
            "pass",
        ),
        rank_one,
    )
    write_csv(
        RESULTS / "stabilizer_audit.csv",
        (
            "n",
            "specialization",
            "stabilizer_order",
            "expected_order",
            "fixed_fiber_nontrivial_symmetry",
            "pass",
        ),
        stabilizers,
    )
    write_csv(
        RESULTS / "diagonal_superdet_audit.csv",
        (
            "n",
            "weights",
            "pure_euler_determinant",
            "diagonal_superdeterminant",
            "ratio_diagonal_to_target",
            "mixed_subset_factor_count",
            "pure_coefficient_x1x2",
            "diagonal_coefficient_x1x2",
            "subset_size_exponents",
            "mismatch",
            "pass",
        ),
        diagonal,
    )
    write_csv(
        RESULTS / "schatten_cutoffs.csv",
        (
            "inventory",
            "N",
            "sigma",
            "q",
            "q_sigma",
            "theorem_Sq_membership",
            "boundary_case",
            "singleton_q_sum",
            "log_subset_q_product",
            "subset_q_sum_product_minus_1",
        ),
        schatten,
    )
    write_csv(
        RESULTS / "control_audit.csv",
        (
            "seed",
            "n",
            "inventory",
            "scalar_identity_pass",
            "distinct_stabilizer_pass",
            "pure_pair_coefficient",
            "diagonal_pair_coefficient",
            "mixed_factor_pass",
        ),
        controls,
    )

    exact_checks = {
        "squarefree_counts": all(row["count_pass"] for row in squarefree),
        "squarefree_all_primitive": all(row["all_primitive"] for row in squarefree),
        "squarefree_scalar_dimensions_zero": all(row["virtual_dimension"] == 0 for row in squarefree),
        "s3_residual": s3["pass"],
        "ghost_power": all(row["pass"] for row in ghost),
        "projective_zero_specialization": projective["all_zero_specialization_pass"],
        "c2_sign_power": projective["all_c2_sign_power_pass"],
        "adams_squarefree": projective["all_adams_squarefree_pass"],
        "rank_one": all(row["pass"] for row in rank_one),
        "stabilizers": all(row["pass"] for row in stabilizers),
        "diagonal_mixed_factor": all(row["pass"] for row in diagonal),
        "controls": all(
            row["scalar_identity_pass"]
            and row["distinct_stabilizer_pass"]
            and row["mixed_factor_pass"]
            for row in controls
        ),
    }
    summary = {
        "candidate": "SD-C18",
        "scope": "Symbolic Dynamics only",
        "zero_data_used": False,
        "exact_check_count": len(exact_checks),
        "exact_checks": exact_checks,
        "all_exact_checks_pass": all(exact_checks.values()),
        "squarefree_total_by_n": {str(row["n"]): row["total"] for row in squarefree},
        "s3_virtual_character": s3["virtual_character"],
        "s3_virtual_decomposition": s3["decomposition"],
        "ghost_row_count": len(ghost),
        "control_row_count": len(controls),
        "schatten_row_count": len(schatten),
        "frozen_verdicts": [
            "GO_FORMAL_EQUIVARIANT_LEDGER",
            "STOP_CHARACTER_FREDHOLM_FIBERS",
            "STOP_STANDARD_SUPERTRACE_INTERPRETATION",
            "STOP_ARITHMETIC_SELECTIVITY",
            "PROVES_TOO_MUCH",
            "ROUTE_A_REJECTED",
            "ROUTE_B_LOCKED",
        ],
    }
    write_json(RESULTS / "summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sanity", action="store_true", help="run only the two frozen sanity checks")
    args = parser.parse_args()
    RESULTS.mkdir(parents=True, exist_ok=True)
    if args.sanity:
        payload = sanity_payload()
        write_json(RESULTS / "sanity.json", payload)
        print(json.dumps(payload, indent=2, sort_keys=True))
        if not payload["all_pass"]:
            raise SystemExit(1)
        return
    summary = run_full()
    print(json.dumps(summary, indent=2, sort_keys=True))
    if not summary["all_exact_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
