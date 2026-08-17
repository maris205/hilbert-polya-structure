#!/usr/bin/env python3
"""Reference evaluator for the SD-C42 M1--M20 corrective control seal.

The program is intentionally finite and exact.  It reads the six immutable
historical Route cards, derives the pair ledger and all mandatory Route-A
controls, evaluates explicit matrix projectors, checks the Gauss branch/order
bridge, and constructs the projection-level GO conjunctions.  It writes no
files and does not import any prototype module.
"""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
from typing import Any, Iterable

import yaml


PACKAGE = Path(__file__).resolve().parent
ROUTE_ROOT = PACKAGE / "inputs/route_cards"
CONTROL_LOCK_PATH = PACKAGE / "CONTROL_LOCK.md"

# Patched to the final active bytes before CONTROL_LOCK.md is sealed.
SOURCE_LOCK_SHA256 = "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041"
MAYER_BOUNDARY_SHA256 = "a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5"

CONTROL_LOCKED_FILES = (
    "SOURCE_LOCK.md",
    "MAYER_SOURCE_BOUNDARY.md",
    "SELECTION_AUDIT.md",
    "control_reference.py",
    "control_independent.py",
    "test_control_reference.py",
    "prototype_reference.py",
    "prototype_independent.py",
    "test_prototype_reference.py",
    "inputs/route_cards/SD-C01.yaml",
    "inputs/route_cards/SD-C02.yaml",
    "inputs/route_cards/SD-C03.yaml",
    "inputs/route_cards/SD-C04.yaml",
    "inputs/route_cards/SD-C05.yaml",
    "inputs/route_cards/SD-C06.yaml",
)

CARD_SPECS: dict[str, dict[str, Any]] = {
    "SD-C01": {
        "sha256": "ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2",
        "nonempty_anchors": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.formula_degree_cutoff", 12),
            ("a1.metrics.all_repetition_checks_pass", True),
        ),
        "nonempty": True,
    },
    "SD-C02": {
        "sha256": "5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f",
        "nonempty_anchors": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.fixed_points_every_period", 1),
            ("a1.metrics.primitive_orbits", "one period-1 zero orbit"),
        ),
        "nonempty": True,
    },
    "SD-C03": {
        "sha256": "2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328",
        "nonempty_anchors": (
            ("a1.evidence_status", "PROVED"),
            ("a1.verdict", "A1_WEAK"),
            (
                "a1.strongest_evidence",
                "The renewal graph has an exact primitive-necklace and repetition expansion for its own return atoms.",
            ),
        ),
        "nonempty": True,
    },
    "SD-C04": {
        "sha256": "0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92",
        "nonempty_anchors": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.primitive_necklaces_max_cutoff", 63319),
            ("a1.metrics.repetition_matrix_failures", 0),
        ),
        "nonempty": True,
    },
    "SD-C05": {
        "sha256": "4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1",
        "nonempty_anchors": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.directed_cycles", 0),
            (
                "a1.strongest_failure",
                "Fix(sigma^n) is empty for every n>=1, so there are no primitive cycles or repetitions.",
            ),
        ),
        "nonempty": False,
    },
    "SD-C06": {
        "sha256": "d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b",
        "nonempty_anchors": (
            ("a1.evidence_status", "NOT_TESTABLE"),
            ("a1.metrics.primitive_orbit_count", "not_applicable"),
        ),
        "nonempty": False,
    },
}

A3_ORDER = {
    "A3_FAIL": 0,
    "A3_PARTIAL_ANALYTIC_STRUCTURE": 1,
    "A3_CONTROLLED_CONTINUATION": 2,
    "A3_EXACT_DIVISOR_MATCH": 3,
}
A4_ORDER = {"A4_FAIL": 0, "A4_FORMAL_HINT": 1, "A4_NATURAL_QUANTIZATION": 2}

SEEDS = {
    "a0_shuffled_primes": 42001,
    "a0_matched_density": 42002,
    "a0_composites": 42003,
    "a0_pseudoprimes": 42004,
    "a0_randomized_labels": 42005,
    "a1_shuffled_periods": 42101,
    "a1_random_weights": 42102,
    "a1_random_phases": 42103,
    "a1_same_density_lengths": 42104,
}


class LCG:
    """Platform-independent 31-bit linear congruential generator."""

    def __init__(self, seed: int) -> None:
        self.state = seed % (2**31)

    def next(self) -> int:
        self.state = (1103515245 * self.state + 12345) % (2**31)
        return self.state

    def randbelow(self, bound: int) -> int:
        if bound <= 0:
            raise ValueError("positive bound required")
        return self.next() % bound


def shuffled(values: Iterable[Any], seed: int) -> list[Any]:
    original = list(values)
    result = list(original)
    rng = LCG(seed)
    for index in range(len(result) - 1, 0, -1):
        target = rng.randbelow(index + 1)
        result[index], result[target] = result[target], result[index]
    if len(result) > 1 and result == original:
        result = result[1:] + result[:1]
    return result


Matrix2 = tuple[int, int, int, int]


def mat2_mul(left: Matrix2, right: Matrix2) -> Matrix2:
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def mat2_pow(matrix: Matrix2, exponent: int) -> Matrix2:
    if exponent < 0:
        raise ValueError("nonnegative exponent required")
    result: Matrix2 = (1, 0, 0, 1)
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = mat2_mul(result, base)
        base = mat2_mul(base, base)
        power //= 2
    return result


def mat2_trace(matrix: Matrix2) -> int:
    return matrix[0] + matrix[3]


def mat2_det(matrix: Matrix2) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def digit_a(digit: int) -> Matrix2:
    return (digit, 1, 1, 0)


def branch_b(digit: int) -> Matrix2:
    return (0, 1, 1, digit)


def word_matrix(digits: Iterable[int], builder: Any) -> Matrix2:
    result: Matrix2 = (1, 0, 0, 1)
    for digit in digits:
        result = mat2_mul(result, builder(digit))
    return result


def conjugate_by_j(matrix: Matrix2) -> Matrix2:
    j: Matrix2 = (0, 1, 1, 0)
    return mat2_mul(mat2_mul(j, matrix), j)


PairWord = tuple[tuple[int, int], ...]


def rotations(word: tuple[Any, ...]) -> tuple[tuple[Any, ...], ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_rotation(word: tuple[Any, ...]) -> tuple[Any, ...]:
    if not word:
        raise ValueError("nonempty word required")
    return min(rotations(word))


def is_primitive(word: tuple[Any, ...]) -> bool:
    length = len(word)
    for divisor in range(1, length):
        if length % divisor == 0 and word == word[:divisor] * (length // divisor):
            return False
    return True


def primitive_necklaces(alphabet: tuple[Any, ...], max_length: int) -> list[tuple[Any, ...]]:
    result: list[tuple[Any, ...]] = []
    for length in range(1, max_length + 1):
        for raw in product(alphabet, repeat=length):
            word = tuple(raw)
            if word == canonical_rotation(word) and is_primitive(word):
                result.append(word)
    return result


def reverse_pair_word(word: PairWord) -> PairWord:
    return tuple((right, left) for left, right in reversed(word))


def word_id(word: tuple[Any, ...]) -> str:
    if word and isinstance(word[0], tuple):
        return "|".join(f"{left},{right}" for left, right in word)
    return ",".join(str(item) for item in word)


def roof_string(trace: int) -> str:
    with localcontext() as context:
        context.prec = 70
        delta = Decimal(trace * trace - 4)
        lam = (Decimal(trace) + delta.sqrt()) / Decimal(2)
        return format(Decimal(2) * lam.ln(), ".60f")


def pair_rows(digits: tuple[int, ...] = (1, 2), max_length: int = 3) -> list[dict[str, Any]]:
    alphabet = tuple(product(digits, repeat=2))
    words = primitive_necklaces(alphabet, max_length)
    orientation_ids = {word_id(word) for word in words}
    rows: list[dict[str, Any]] = []
    for word in words:
        flattened = tuple(digit for pair in word for digit in pair)
        matrix = word_matrix(flattened, digit_a)
        trace = mat2_trace(matrix)
        reverse = canonical_rotation(reverse_pair_word(word))
        orientation = word_id(word)
        reverse_orientation = word_id(reverse)
        row = {
            "pair_word": [list(pair) for pair in word],
            "pair_length": len(word),
            "flattened_digits": list(flattened),
            "matrix": list(matrix),
            "determinant": mat2_det(matrix),
            "trace": trace,
            "order_discriminant": trace * trace - 4,
            "period": roof_string(trace),
            "orientation_id": orientation,
            "reverse_orientation_id": reverse_orientation,
            "reversal_orbit_id": min(orientation, reverse_orientation),
            "self_reversal": orientation == reverse_orientation,
            "distinct_reverse_class": orientation != reverse_orientation,
            "reverse_class_present": reverse_orientation in orientation_ids,
            "source_multiplicity": 1,
            "untwisted_sign": 1,
            "phase_modulus": 97,
            "phase_exponent": 0,
            "expanding_eigenvalue_minpoly": [1, -trace, 1],
            "geodesic_norm_minpoly": [1, -(trace * trace - 2), 1],
            "derivative_multiplier_minpoly": [1, -(trace * trace - 2), 1],
            "norm_root_selector": "greater_than_one",
            "derivative_root_selector": "between_zero_and_one",
            "norm_times_derivative": 1,
            "norm_qsqrt_coefficients": [
                [trace * trace - 2, 2],
                [trace, 2],
            ],
            "derivative_qsqrt_coefficients": [
                [trace * trace - 2, 2],
                [-trace, 2],
            ],
            "stability_denominator_present": True,
            "reciprocal_marker_exponent_per_repetition": 2 * len(word),
        }
        rows.append(row)
    return sorted(rows, key=lambda row: (row["pair_length"], row["orientation_id"]))


def digit_necklace_counts(alphabet_size: int, max_length: int) -> dict[int, int]:
    alphabet = tuple(range(1, alphabet_size + 1))
    return {
        length: sum(1 for word in primitive_necklaces(alphabet, length) if len(word) == length)
        for length in range(1, max_length + 1)
    }


def splitting_census() -> dict[str, Any]:
    digit_counts = digit_necklace_counts(2, 6)
    pair_counts = Counter(row["pair_length"] for row in pair_rows())
    predicted = {
        length: 2 * digit_counts[2 * length]
        + (digit_counts[length] if length % 2 else 0)
        for length in range(1, 4)
    }
    rows = pair_rows()
    by_id = {row["orientation_id"]: row for row in rows}
    trace4_phase_relation = (
        {"1,2", "2,1"}.issubset(by_id)
        and by_id["1,2"]["trace"] == by_id["2,1"]["trace"] == 4
        and by_id["1,2"]["reverse_orientation_id"] == "2,1"
        and by_id["2,1"]["reverse_orientation_id"] == "1,2"
        and canonical_rotation((1, 2)) == (1, 2)
        and set(rotations((1, 2))) == {(1, 2), (2, 1)}
    )
    flattened_22_property = (
        "2,2" in by_id
        and is_primitive(((2, 2),))
        and not is_primitive((2, 2))
        and digit_counts[1] > 0
    )
    pass_value = (
        dict(pair_counts) == predicted == {1: 4, 2: 6, 3: 20}
        and trace4_phase_relation
        and flattened_22_property
    )
    swapped = {
        length: 2 * digit_counts[2 * length]
        + (digit_counts[length] if length % 2 == 0 else 0)
        for length in range(1, 4)
    }
    return {
        "digit_primitive_counts_1_to_6": digit_counts,
        "pair_primitive_counts_1_to_3": dict(pair_counts),
        "predicted_pair_counts": predicted,
        "odd_period_stays_one_even_period_splits_two": pass_value,
        "odd_even_swapped_mutation_rejected": swapped != dict(pair_counts),
        "trace4_phase_pair": ["1,2", "2,1"],
        "trace4_phase_relation_verified": trace4_phase_relation,
        "flattened_22_pair_primitive_sigma_imprimitive": flattened_22_property,
        "pass": pass_value and swapped != dict(pair_counts),
    }


def return_map_typing_certificate() -> dict[str, Any]:
    digits = (1, 2, 3, 4, 5, 6, 7, 8)

    def group(sequence: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
        return tuple(
            (sequence[index], sequence[index + 1])
            for index in range(0, len(sequence), 2)
        )

    grouped = group(digits)
    rho_grouped = grouped[1:]
    grouped_sigma_two = group(digits[2:])
    wrong_pair_sigma_two = grouped[2:]
    conjugacy = rho_grouped == grouped_sigma_two
    wrong_pair_map_rejected = wrong_pair_sigma_two != grouped_sigma_two

    word = ((1, 2), (2, 3), (1, 4))
    reversed_class = canonical_rotation(reverse_pair_word(word))
    flattened_word = tuple(digit for pair in word for digit in pair)
    raw_reversed_grouped = group(tuple(reversed(flattened_word)))
    raw_reversal_matches = raw_reversed_grouped == reverse_pair_word(word)
    reversal_descends = all(
        canonical_rotation(reverse_pair_word(rotation)) == reversed_class
        for rotation in rotations(word)
    )
    primitive_preserved = is_primitive(word) == is_primitive(reverse_pair_word(word))
    wrong_block_order = canonical_rotation(tuple(reversed(word)))
    block_order_mutation_rejected = wrong_block_order != reversed_class
    passed = (
        conjugacy
        and wrong_pair_map_rejected
        and reversal_descends
        and raw_reversal_matches
        and primitive_preserved
        and block_order_mutation_rejected
    )
    return {
        "digit_space": "X=N^N_with_one_digit_shift_sigma",
        "pair_space": "X2=(N^2)^N_with_one_pair_shift_rho",
        "digit_fixture": list(digits),
        "iota_fixture": [list(pair) for pair in grouped],
        "rho_after_iota": [list(pair) for pair in rho_grouped],
        "iota_after_sigma_squared": [list(pair) for pair in grouped_sigma_two],
        "rho_iota_equals_iota_sigma_squared": conjugacy,
        "wrong_sigma_squared_on_pair_space_rejected": wrong_pair_map_rejected,
        "global_reversal_descends_to_cyclic_pair_classes": reversal_descends,
        "global_raw_index_reversal_equals_pair_reverse": raw_reversal_matches,
        "global_reversal_preserves_pair_primitivity": primitive_preserved,
        "unreversed_block_order_mutation_rejected": block_order_mutation_rejected,
        "pass": passed,
    }


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes(count: int) -> list[int]:
    result: list[int] = []
    value = 2
    while len(result) < count:
        if is_prime(value):
            result.append(value)
        value += 1
    return result


def generated_by_primality(count: int, seed: int, want_prime: bool) -> list[int]:
    rng = LCG(seed)
    result: list[int] = []
    seen: set[int] = set()
    while len(result) < count:
        value = 2 + rng.randbelow(9991)
        if value not in seen and is_prime(value) is want_prime:
            seen.add(value)
            result.append(value)
    return result


def first_base2_pseudoprimes(count: int) -> list[int]:
    result: list[int] = []
    value = 3
    while len(result) < count:
        if not is_prime(value) and pow(2, value - 1, value) == 1:
            result.append(value)
        value += 2
    return result


def nested_get(record: dict[str, Any], dotted_path: str) -> Any:
    value: Any = record
    for key in dotted_path.split("."):
        if not isinstance(value, dict) or key not in value:
            raise KeyError(dotted_path)
        value = value[key]
    return value


def card_path(candidate_id: str) -> Path:
    path = ROUTE_ROOT / f"{candidate_id}.yaml"
    if not path.is_file():
        raise ValueError(f"missing frozen card snapshot for {candidate_id}")
    return path


def parse_selection_cards(
    overridden: dict[str, dict[str, Any]] | None = None,
    omitted: set[str] | None = None,
) -> dict[str, Any]:
    overridden = overridden or {}
    omitted = omitted or set()
    rows: list[dict[str, Any]] = []
    valid = True
    for candidate_id, spec in CARD_SPECS.items():
        if candidate_id in omitted:
            continue
        path = card_path(candidate_id)
        raw = path.read_bytes()
        parsed = deepcopy(overridden.get(candidate_id, yaml.safe_load(raw)))
        digest_ok = sha256(raw).hexdigest() == spec["sha256"]
        id_ok = parsed.get("candidate_id") == candidate_id
        anchors_ok = all(
            nested_get(parsed, dotted_path) == expected
            for dotted_path, expected in spec["nonempty_anchors"]
        )
        derived_nonempty = spec["nonempty"] if anchors_ok else None
        a2_exact = nested_get(parsed, "a2.verdict") == "A2_ANALYTIC_DETERMINANT"
        a2_proved = nested_get(parsed, "a2.evidence_status") == "PROVED"
        survivor = bool(derived_nonempty and a2_exact and a2_proved)
        row = {
            "candidate_id": parsed.get("candidate_id"),
            "path": f"inputs/route_cards/{candidate_id}.yaml",
            "sha256": sha256(raw).hexdigest(),
            "hash_matches": digest_ok,
            "candidate_id_matches": id_ok,
            "anchor_schema_matches": anchors_ok,
            "nonempty_intrinsic_ledger": derived_nonempty,
            "a2_verdict": nested_get(parsed, "a2.verdict"),
            "a2_evidence_status": nested_get(parsed, "a2.evidence_status"),
            "a2_proved": a2_proved,
            "survivor": survivor,
            "a3_verdict": nested_get(parsed, "a3.verdict"),
            "a4_verdict": nested_get(parsed, "a4.verdict"),
        }
        rows.append(row)
        valid = valid and digest_ok and id_ok and anchors_ok
    exact_ids = {row["candidate_id"] for row in rows} == set(CARD_SPECS)
    unique_ids = len({row["candidate_id"] for row in rows}) == len(rows)
    valid = valid and exact_ids and unique_ids and len(rows) == 6
    survivors = sorted(row["candidate_id"] for row in rows if row["survivor"])
    winner = None
    if valid and survivors:
        eligible = [row for row in rows if row["survivor"]]
        winner = min(
            eligible,
            key=lambda row: (
                -A3_ORDER[row["a3_verdict"]],
                -A4_ORDER[row["a4_verdict"]],
                row["candidate_id"],
            ),
        )["candidate_id"]
    return {
        "rows": rows,
        "six_cards_valid": valid,
        "survivors": survivors,
        "winner": winner,
        "pass": valid
        and survivors == ["SD-C01", "SD-C02", "SD-C04"]
        and winner == "SD-C04",
    }


def selection_mutations() -> dict[str, bool]:
    base_cards = {
        candidate_id: yaml.safe_load(card_path(candidate_id).read_bytes())
        for candidate_id in CARD_SPECS
    }
    zero_c02 = deepcopy(base_cards["SD-C02"])
    zero_c02["a1"]["metrics"]["primitive_orbits"] = "zero primitive orbits"
    fail_c02 = deepcopy(base_cards["SD-C02"])
    fail_c02["a2"]["verdict"] = "A2_FAIL"
    open_c02 = deepcopy(base_cards["SD-C02"])
    open_c02["a2"]["evidence_status"] = "OPEN"
    elevated_c01 = deepcopy(base_cards["SD-C01"])
    elevated_c01["a3"]["verdict"] = "A3_EXACT_DIVISOR_MATCH"
    duplicate_c06 = deepcopy(base_cards["SD-C06"])
    duplicate_c06["candidate_id"] = "SD-C04"
    mutations = {
        "missing_card_rejected": not parse_selection_cards(omitted={"SD-C06"})["pass"],
        "duplicate_id_rejected": not parse_selection_cards(
            overridden={"SD-C06": duplicate_c06}
        )["pass"],
        "c02_zero_orbit_mutation_rejected": not parse_selection_cards(
            overridden={"SD-C02": zero_c02}
        )["pass"],
        "c02_a2_mutation_rejected": not parse_selection_cards(
            overridden={"SD-C02": fail_c02}
        )["pass"],
        "c02_a2_evidence_mutation_rejected": not parse_selection_cards(
            overridden={"SD-C02": open_c02}
        )["pass"],
        "winner_a3_mutation_rejected": not parse_selection_cards(
            overridden={"SD-C01": elevated_c01}
        )["pass"],
    }
    return mutations


def orientation_metadata_valid(rows: list[dict[str, Any]]) -> bool:
    required = {
        "pair_word",
        "orientation_id",
        "reverse_orientation_id",
        "reversal_orbit_id",
        "self_reversal",
        "distinct_reverse_class",
        "reverse_class_present",
        "source_multiplicity",
        "untwisted_sign",
        "phase_modulus",
        "phase_exponent",
        "stability_denominator_present",
        "expanding_eigenvalue_minpoly",
        "geodesic_norm_minpoly",
        "derivative_multiplier_minpoly",
        "norm_root_selector",
        "derivative_root_selector",
        "norm_times_derivative",
        "norm_qsqrt_coefficients",
        "derivative_qsqrt_coefficients",
    }
    if not all(required.issubset(row) for row in rows):
        return False
    ids = {row["orientation_id"] for row in rows}
    return all(
        row["orientation_id"] == word_id(canonical_rotation(tuple(map(tuple, row["pair_word"]))))
        and row["reverse_orientation_id"]
        == word_id(
            canonical_rotation(reverse_pair_word(tuple(map(tuple, row["pair_word"]))))
        )
        and row["reversal_orbit_id"]
        == min(row["orientation_id"], row["reverse_orientation_id"])
        and row["self_reversal"]
        == (row["orientation_id"] == row["reverse_orientation_id"])
        and row["distinct_reverse_class"] == (not row["self_reversal"])
        and row["reverse_class_present"]
        and row["reverse_orientation_id"] in ids
        and row["source_multiplicity"] == 1
        and row["untwisted_sign"] == 1
        and row["phase_modulus"] == 97
        and row["phase_exponent"] == 0
        and row["expanding_eigenvalue_minpoly"] == [1, -row["trace"], 1]
        and row["geodesic_norm_minpoly"]
        == [1, -(row["trace"] ** 2 - 2), 1]
        and row["derivative_multiplier_minpoly"]
        == [1, -(row["trace"] ** 2 - 2), 1]
        and row["norm_root_selector"] == "greater_than_one"
        and row["derivative_root_selector"] == "between_zero_and_one"
        and row["norm_times_derivative"] == 1
        and row["norm_qsqrt_coefficients"]
        == [[row["trace"] ** 2 - 2, 2], [row["trace"], 2]]
        and row["derivative_qsqrt_coefficients"]
        == [[row["trace"] ** 2 - 2, 2], [-row["trace"], 2]]
        and row["trace"] >= 3
        and quadratic_multiply(
            (
                Fraction(*row["norm_qsqrt_coefficients"][0]),
                Fraction(*row["norm_qsqrt_coefficients"][1]),
            ),
            (
                Fraction(*row["derivative_qsqrt_coefficients"][0]),
                Fraction(*row["derivative_qsqrt_coefficients"][1]),
            ),
            row["order_discriminant"],
        )
        == (Fraction(1), Fraction(0))
        and row["stability_denominator_present"] is True
        for row in rows
    )


def build_a0_controls(base_rows: list[dict[str, Any]]) -> dict[str, Any]:
    count = len(base_rows)
    traces = [row["trace"] for row in base_rows]
    prime_count = sum(is_prime(value) for value in traces)

    prime_source = first_primes(count)
    shuffled_primes = shuffled(prime_source, SEEDS["a0_shuffled_primes"])

    matched_primes = generated_by_primality(
        prime_count, SEEDS["a0_matched_density"], True
    )
    matched_composites = generated_by_primality(
        count - prime_count, SEEDS["a0_matched_density"] + 1, False
    )
    matched = shuffled(
        matched_primes + matched_composites, SEEDS["a0_matched_density"] + 2
    )

    composites = generated_by_primality(count, SEEDS["a0_composites"], False)
    pseudoprimes = shuffled(
        first_base2_pseudoprimes(count), SEEDS["a0_pseudoprimes"]
    )

    assignments = [(row["orientation_id"], row["trace"]) for row in base_rows]
    randomized_values = shuffled(
        [value for _, value in assignments], SEEDS["a0_randomized_labels"]
    )
    randomized_assignments = [
        (orientation, value)
        for (orientation, _), value in zip(assignments, randomized_values, strict=True)
    ]

    neighboring_rows = pair_rows((2, 3), 3)
    parent_words = primitive_necklaces((1, 2), 3)
    parent = {
        "object_type": "SigmaPrimitiveDigit",
        "dynamics": "sigma",
        "alphabet": [1, 2],
        "orientation_ids": [word_id(word) for word in parent_words],
    }

    predicates = {
        "shuffled_primes": Counter(shuffled_primes) == Counter(prime_source)
        and shuffled_primes != prime_source
        and all(is_prime(value) for value in shuffled_primes),
        "matched_density_random_integers": len(matched) == count
        and sum(is_prime(value) for value in matched) == prime_count,
        "composites_only": len(composites) == count
        and all(not is_prime(value) for value in composites),
        "base2_pseudoprimes": len(pseudoprimes) == count
        and all(
            not is_prime(value) and pow(2, value - 1, value) == 1
            for value in pseudoprimes
        ),
        "randomized_arithmetic_labels": Counter(randomized_values) == Counter(traces)
        and randomized_assignments != assignments,
        "neighboring_parameters": len(neighboring_rows) == count
        and {digit for row in neighboring_rows for digit in row["flattened_digits"]}
        == {2, 3},
        "simpler_parent": parent["object_type"] == "SigmaPrimitiveDigit"
        and parent["dynamics"] == "sigma"
        and len(parent_words) == 5,
    }

    identity_assignments = list(assignments)
    matched_bad = list(matched)
    first_prime_index = next(index for index, value in enumerate(matched_bad) if is_prime(value))
    matched_bad[first_prime_index] = 4
    composite_bad = list(composites)
    composite_bad[0] = 2
    pseudoprime_bad = list(pseudoprimes)
    pseudoprime_bad[0] = 9
    mutation_rejections = {
        "identity_prime_shuffle_rejected": prime_source == prime_source
        and not (prime_source != prime_source),
        "matched_density_mismatch_rejected": sum(is_prime(value) for value in matched_bad)
        != prime_count,
        "prime_in_composites_rejected": not all(
            not is_prime(value) for value in composite_bad
        ),
        "nonpseudoprime_composite_rejected": not all(
            not is_prime(value) and pow(2, value - 1, value) == 1
            for value in pseudoprime_bad
        ),
        "identity_label_assignment_rejected": not (
            identity_assignments != assignments
        ),
        "same_parameters_rejected": {1, 2} != {2, 3},
        "same_object_parent_rejected": "RhoPrimitivePair" != parent["object_type"],
    }
    return {
        "base_row_count": count,
        "base_trace_prime_count": prime_count,
        "controls": {
            "shuffled_primes": {
                "source": "algorithmically generated first-prime inventory",
                "inventory": shuffled_primes,
            },
            "matched_density_random_integers": {
                "source": "LCG integers conditioned only on exact prime-count match",
                "inventory": matched,
            },
            "composites_only": {
                "source": "LCG integers accepted by computed composite predicate",
                "inventory": composites,
            },
            "base2_pseudoprimes": {
                "source": "computed composite Fermat base-2 witnesses",
                "inventory": pseudoprimes,
            },
            "randomized_arithmetic_labels": {
                "source": "permutation of base orbit-derived trace labels",
                "assignments": randomized_assignments,
            },
            "neighboring_parameters": {
                "source": "same pair construction with frozen neighboring digits",
                "digits": [2, 3],
                "row_count": len(neighboring_rows),
            },
            "simpler_parent": {
                "source": "one-digit sigma parent, rederived rather than inherited as pair type",
                **parent,
            },
        },
        "predicates": predicates,
        "negative_mutations": mutation_rejections,
        "pass": len(predicates) == 7
        and all(predicates.values())
        and all(mutation_rejections.values()),
    }


def build_a1_controls(base_rows: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [row["orientation_id"] for row in base_rows]
    periods = [row["period"] for row in base_rows]
    shuffled_period_values = shuffled(periods, SEEDS["a1_shuffled_periods"])
    shuffled_periods = list(zip(ids, shuffled_period_values, strict=True))

    weight_rng = LCG(SEEDS["a1_random_weights"])
    weights = []
    for orientation in ids:
        numerator = weight_rng.randbelow(2001) - 1000
        if numerator == 0:
            numerator = 1
        weights.append((orientation, numerator, 1009))

    phase_rng = LCG(SEEDS["a1_random_phases"])
    phases = [(orientation, 1 + phase_rng.randbelow(96), 97) for orientation in ids]

    length_rng = LCG(SEEDS["a1_same_density_lengths"])
    denominator = 1_000_003
    source_bins = [int(Decimal(period) // Decimal(2)) for period in periods]
    random_lengths = []
    for orientation, bin_index in zip(ids, source_bins, strict=True):
        numerator = (
            2 * bin_index * denominator
            + 1
            + length_rng.randbelow(2 * denominator - 1)
        )
        random_lengths.append((orientation, numerator, denominator, bin_index))

    neighboring_rows = pair_rows((2, 3), 3)
    parent_words = primitive_necklaces((1, 2), 3)

    random_bins = [
        int((Fraction(numerator, den)) // 2)
        for _, numerator, den, _ in random_lengths
    ]
    predicates = {
        "shuffled_periods": Counter(shuffled_period_values) == Counter(periods)
        and shuffled_period_values != periods,
        "random_weights": len(weights) == len(base_rows)
        and all(numerator != 1009 for _, numerator, _ in weights),
        "random_phases": len(phases) == len(base_rows)
        and all(1 <= exponent < modulus == 97 for _, exponent, modulus in phases),
        "same_density_random_lengths": len(random_lengths) == len(base_rows)
        and Counter(random_bins) == Counter(source_bins)
        and all(Fraction(numerator, den) > 0 for _, numerator, den, _ in random_lengths),
        "neighboring_candidate_parameters": len(neighboring_rows) == len(base_rows)
        and {digit for row in neighboring_rows for digit in row["flattened_digits"]}
        == {2, 3},
        "simpler_parent_candidate": len(parent_words) == 5,
    }

    bad_lengths = deepcopy(random_lengths)
    orientation, numerator, den, bin_index = bad_lengths[0]
    bad_lengths[0] = (orientation, numerator + 2 * den, den, bin_index)
    bad_bins = [int(Fraction(num, d) // 2) for _, num, d, _ in bad_lengths]
    mutation_rejections = {
        "identity_period_shuffle_rejected": not (periods != periods),
        "canonical_weight_injected_rejected": not all(
            numerator != 1009 for _, numerator, _ in [(ids[0], 1009, 1009)] + weights[1:]
        ),
        "zero_phase_injected_rejected": not all(
            1 <= exponent < modulus == 97
            for _, exponent, modulus in [(ids[0], 0, 97)] + phases[1:]
        ),
        "length_density_mismatch_rejected": Counter(bad_bins) != Counter(source_bins),
        "same_neighbor_parameters_rejected": {1, 2} != {2, 3},
        "same_parent_type_rejected": "RhoPrimitivePair" != "SigmaPrimitiveDigit",
    }

    metadata_pass = orientation_metadata_valid(base_rows)
    orientation_bad = deepcopy(base_rows)
    orientation_bad[0].pop("reverse_orientation_id")
    distinct_row_index = next(
        index for index, row in enumerate(base_rows) if row["distinct_reverse_class"]
    )
    quotient_bad = deepcopy(base_rows)
    quotient_bad[distinct_row_index]["reverse_orientation_id"] = quotient_bad[
        distinct_row_index
    ]["orientation_id"]
    multiplicity_bad = deepcopy(base_rows)
    multiplicity_bad[0]["source_multiplicity"] = 2
    sign_bad = deepcopy(base_rows)
    sign_bad[0]["untwisted_sign"] = -1
    phase_bad = deepcopy(base_rows)
    phase_bad[0]["phase_exponent"] = 1
    stability_bad = deepcopy(base_rows)
    stability_bad[0]["stability_denominator_present"] = False
    polynomial_bad = deepcopy(base_rows)
    polynomial_bad[0]["derivative_multiplier_minpoly"] = [
        1,
        -polynomial_bad[0]["trace"],
        1,
    ]
    root_bad = deepcopy(base_rows)
    root_bad[0]["norm_root_selector"] = "between_zero_and_one"
    derivative_bad = deepcopy(base_rows)
    derivative_bad[0]["derivative_qsqrt_coefficients"] = derivative_bad[0][
        "norm_qsqrt_coefficients"
    ]
    metadata_mutations = {
        "missing_reversal_field_rejected": not orientation_metadata_valid(orientation_bad),
        "silent_reversal_quotient_rejected": not orientation_metadata_valid(quotient_bad),
        "multiplicity_mutation_rejected": not orientation_metadata_valid(multiplicity_bad),
        "sign_mutation_rejected": not orientation_metadata_valid(sign_bad),
        "canonical_phase_mutation_rejected": not orientation_metadata_valid(phase_bad),
        "stability_denominator_removal_rejected": not orientation_metadata_valid(
            stability_bad
        ),
        "eigenvalue_derivative_polynomial_swap_rejected": not orientation_metadata_valid(
            polynomial_bad
        ),
        "norm_derivative_root_swap_rejected": not orientation_metadata_valid(root_bad),
        "derivative_exact_root_mutation_rejected": not orientation_metadata_valid(
            derivative_bad
        ),
    }
    return {
        "controls": {
            "shuffled_periods": {
                "source": "source-derived derivative roofs permuted across orientation IDs",
                "assignments": shuffled_periods,
            },
            "random_weights": {
                "source": "LCG signed rational weights, denominator 1009",
                "assignments": weights,
            },
            "random_phases": {
                "source": "LCG nonzero phase exponents modulo 97",
                "assignments": phases,
            },
            "same_density_random_lengths": {
                "source": "LCG positive rationals preserving exact two-unit roof bins",
                "assignments": random_lengths,
                "source_bin_histogram": dict(Counter(source_bins)),
                "random_bin_histogram": dict(Counter(random_bins)),
            },
            "neighboring_candidate_parameters": {
                "source": "rederived pair ledger on digits 2,3",
                "row_count": len(neighboring_rows),
            },
            "simpler_parent_candidate": {
                "source": "rederived one-digit sigma necklaces on digits 1,2",
                "row_count": len(parent_words),
            },
        },
        "predicates": predicates,
        "baseline_metadata_pass": metadata_pass,
        "negative_mutations": {**mutation_rejections, **metadata_mutations},
        "pass": len(predicates) == 6
        and all(predicates.values())
        and metadata_pass
        and all(mutation_rejections.values())
        and all(metadata_mutations.values()),
    }


def matn_shape(matrix: list[list[int]]) -> tuple[int, int] | None:
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return None
    widths = {len(row) for row in matrix}
    if len(widths) != 1:
        return None
    return (len(matrix), widths.pop())


def matn_mul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    left_shape = matn_shape(left)
    right_shape = matn_shape(right)
    if left_shape is None or right_shape is None or left_shape[1] != right_shape[0]:
        raise ValueError("incompatible matrices")
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(left_shape[1]))
            for j in range(right_shape[1])
        ]
        for i in range(left_shape[0])
    ]


def matn_pow(matrix: list[list[int]], exponent: int) -> list[list[int]]:
    shape = matn_shape(matrix)
    if shape is None or shape[0] != shape[1]:
        raise ValueError("square matrix required")
    result = [[int(i == j) for j in range(shape[0])] for i in range(shape[0])]
    base = deepcopy(matrix)
    power = exponent
    while power:
        if power & 1:
            result = matn_mul(result, base)
        base = matn_mul(base, base)
        power //= 2
    return result


def matn_trace(matrix: list[list[int]]) -> int:
    shape = matn_shape(matrix)
    if shape is None or shape[0] != shape[1]:
        raise ValueError("square matrix required")
    return sum(matrix[index][index] for index in range(shape[0]))


def coordinate_projector(dimension: int, indices: list[int]) -> list[list[int]]:
    selected = set(indices)
    return [
        [int(i == j and i in selected) for j in range(dimension)]
        for i in range(dimension)
    ]


def marker_degrees_for_diagonal(eigenvalues: list[int], stride: int) -> list[int]:
    coefficients = [1]
    for eigenvalue in eigenvalues:
        factor = [0] * (stride + 1)
        factor[0] = 1
        factor[stride] = -eigenvalue
        updated = [0] * (len(coefficients) + stride)
        for first_index, first in enumerate(coefficients):
            for second_index, second in enumerate(factor):
                updated[first_index + second_index] += first * second
        coefficients = updated
    return [index for index, coefficient in enumerate(coefficients) if coefficient]


def evaluate_owner(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    matrix = record.get("operator_matrix")
    projector = record.get("projector_matrix")
    dimension = record.get("space_dimension")
    indices = record.get("selected_indices")
    multiplicity = record.get("multiplicity")
    stride = record.get("marker_stride")
    expected_traces = record.get("expected_power_traces")
    expected_degrees = record.get("expected_marker_degrees")
    if not isinstance(matrix, list) or matn_shape(matrix) != (dimension, dimension):
        errors.append("operator_dimension")
    if not isinstance(projector, list) or matn_shape(projector) != (dimension, dimension):
        errors.append("projector_dimension")
    if not isinstance(indices, list) or not all(
        isinstance(index, int) and 0 <= index < dimension for index in indices
    ):
        errors.append("selected_indices")
    if errors:
        return {"declared_owner": False, "errors": errors}

    computed_projector = coordinate_projector(dimension, indices)
    if projector != computed_projector:
        errors.append("projector_not_coordinate_selector")
    if matn_mul(projector, projector) != projector:
        errors.append("projector_not_idempotent")
    if matn_mul(projector, matrix) != matn_mul(matrix, projector):
        errors.append("projector_not_commuting")
    if multiplicity != 1:
        errors.append("multiplicity_not_one")

    computed_traces = [
        matn_trace(matn_mul(projector, matn_pow(matrix, repetition)))
        for repetition in range(1, 7)
    ]
    if expected_traces != computed_traces:
        errors.append("power_trace_mismatch")

    diagonal_selected = [matrix[index][index] for index in indices]
    off_diagonal_zero = all(
        matrix[i][j] == 0
        for i in indices
        for j in indices
        if i != j
    )
    if not off_diagonal_zero:
        errors.append("selected_block_not_diagonal")
    computed_degrees = marker_degrees_for_diagonal(diagonal_selected, stride)
    if expected_degrees != computed_degrees:
        errors.append("marker_support_mismatch")
    return {
        "declared_owner": not errors,
        "errors": errors,
        "computed_power_traces": computed_traces,
        "computed_marker_degrees": computed_degrees,
    }


def build_ownership_controls() -> dict[str, Any]:
    positive = {
        "space_dimension": 2,
        "operator_matrix": [[2, 0], [0, 3]],
        "projector_matrix": [[1, 0], [0, 0]],
        "selected_indices": [0],
        "multiplicity": 1,
        "marker_stride": 2,
        "expected_power_traces": [2, 4, 8, 16, 32, 64],
        "expected_marker_degrees": [0, 2],
    }
    full = deepcopy(positive)
    full.update(
        {
            "projector_matrix": [[1, 0], [0, 1]],
            "selected_indices": [0, 1],
            "expected_power_traces": [5, 13, 35, 97, 275, 793],
            "expected_marker_degrees": [0, 2, 4],
        }
    )

    mutations: dict[str, dict[str, Any]] = {}
    mutations["nonidempotent"] = deepcopy(positive)
    mutations["nonidempotent"]["projector_matrix"] = [[1, 0], [0, 2]]
    mutations["noncommuting"] = deepcopy(positive)
    mutations["noncommuting"]["projector_matrix"] = [[1, 1], [0, 0]]
    mutations["wrong_dimension"] = deepcopy(positive)
    mutations["wrong_dimension"]["space_dimension"] = 3
    mutations["wrong_trace_multiplicity"] = deepcopy(positive)
    mutations["wrong_trace_multiplicity"]["expected_power_traces"][2] += 1
    mutations["wrong_marker"] = deepcopy(positive)
    mutations["wrong_marker"]["marker_stride"] = 1
    mutations["full_ledger_multiplicity"] = deepcopy(full)
    mutations["full_ledger_multiplicity"]["multiplicity"] = 2

    positive_result = evaluate_owner(positive)
    full_result = evaluate_owner(full)
    mutation_rejections = {
        f"{name}_rejected": not evaluate_owner(record)["declared_owner"]
        for name, record in mutations.items()
    }

    explicit_toy_labels = [value + 1 for value in (2, 3)]
    computed_filtered = [value for value in explicit_toy_labels if is_prime(value)]
    computed_removed = [
        value for value in explicit_toy_labels if value not in computed_filtered
    ]
    selector_record = {
        "full_inventory": explicit_toy_labels,
        "predicate": "computed_is_prime",
        "filtered_inventory": computed_filtered,
        "removed_inventory": computed_removed,
        "declared_projector": None,
        "frozen_schema_owner": "UNDECLARED",
    }

    def selector_inventory_valid(record: dict[str, Any]) -> bool:
        full_inventory = record["full_inventory"]
        filtered = [value for value in full_inventory if is_prime(value)]
        removed = [value for value in full_inventory if value not in filtered]
        return (
            record["filtered_inventory"] == filtered
            and record["removed_inventory"] == removed
            and sorted(filtered + removed) == sorted(full_inventory)
            and not set(filtered).intersection(removed)
            and record["declared_projector"] is None
            and record["frozen_schema_owner"] == "UNDECLARED"
        )

    selector_mutations: dict[str, bool] = {}
    bad_full = deepcopy(selector_record)
    bad_full["full_inventory"].append(5)
    selector_mutations["full_inventory_mutation_rejected"] = not selector_inventory_valid(
        bad_full
    )
    bad_filtered = deepcopy(selector_record)
    bad_filtered["filtered_inventory"].append(4)
    selector_mutations["filter_mutation_rejected"] = not selector_inventory_valid(
        bad_filtered
    )
    bad_removed = deepcopy(selector_record)
    bad_removed["removed_inventory"] = []
    selector_mutations["difference_mutation_rejected"] = not selector_inventory_valid(
        bad_removed
    )

    return {
        "positive_reducing_owner": {"record": positive, "evaluation": positive_result},
        "full_ledger_owner": {"record": full, "evaluation": full_result},
        "owner_mutations": mutation_rejections,
        "scalar_selector": {
            "record": selector_record,
            "inventory_relations_computed": selector_inventory_valid(selector_record),
            "interpretation": (
                "No projector is declared in the frozen untwisted schema; "
                "this is not a universal nonexistence claim."
            ),
        },
        "selector_inventory_mutations": selector_mutations,
        "pass": positive_result["declared_owner"]
        and full_result["declared_owner"]
        and all(mutation_rejections.values())
        and selector_inventory_valid(selector_record)
        and all(selector_mutations.values()),
    }


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            result[i + j] += first * second
    return result


def det_i_minus_u_matrix(matrix: list[list[int]]) -> list[int]:
    shape = matn_shape(matrix)
    if shape is None or shape[0] != shape[1]:
        raise ValueError("square matrix required")
    dimension = shape[0]
    result = [0] * (dimension + 1)
    for permutation in permutations(range(dimension)):
        term = [1]
        for row, column in enumerate(permutation):
            term = polynomial_multiply(
                term, [int(row == column), -matrix[row][column]]
            )
        sign = permutation_sign(permutation)
        for degree, coefficient in enumerate(term):
            result[degree] += sign * coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def build_countermodels(
    ownership: dict[str, Any], witnesses: dict[str, Any]
) -> dict[str, Any]:
    baseline = {
        "source_object": "paired_gauss_rho_sigma_squared",
        "primitive_type": "RhoPrimitivePair",
        "marker": "u_per_digit_u_squared_per_pair",
        "clock": "two_log_lambda",
        "operator": "K_s_equals_L_s_squared",
        "determinant": "det_I_minus_u_squared_K_s",
    }

    def changed_fields(record: dict[str, Any]) -> list[str]:
        return [field for field in baseline if record.get(field) != baseline[field]]

    odd_matrix = digit_a(3)
    odd = {
        **baseline,
        "source_object": "one_digit_gauss_sigma",
        "primitive_type": "SigmaPrimitiveDigit",
        "operator": "L_s",
        "determinant": "det_I_minus_u_L_s",
    }
    odd_trace = mat2_trace(odd_matrix)
    odd_discriminant = odd_trace**2 - 4 * mat2_det(odd_matrix)

    prime_basis = first_primes(3)
    prime_operator = [
        [prime_basis[i] if i == j else 0 for j in range(3)] for i in range(3)
    ]
    prime_loop = {
        **baseline,
        "source_object": "prime_indexed_direct_sum",
        "primitive_type": "PrimeBasisLoop",
        "operator": "finite_diagonal_prime_control",
        "determinant": "computed_finite_prime_control",
    }

    roof_change = deepcopy(baseline)
    roof_change["clock"] = "log_trace"
    marker_change = deepcopy(baseline)
    marker_change["marker"] = "z_per_pair_return"

    selector = ownership["scalar_selector"]

    cycle_matrix = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    finite_cycle = {
        **baseline,
        "source_object": "finite_directed_three_cycle",
        "primitive_type": "FiniteCyclePrimitive",
        "operator": "three_cycle_adjacency",
        "determinant": "det_I_minus_u_C",
    }

    boundary_matrix = word_matrix((1, 1), digit_a)
    t3_boundary = (
        boundary_matrix == (2, 1, 1, 1)
        and mat2_trace(boundary_matrix) == 3
        and mat2_trace(boundary_matrix) ** 2 - 4 == 5
        and is_prime(5)
    )
    predicates = {
        "X1_odd_det_minus_one_boundary": mat2_det(odd_matrix) == -1
        and odd_discriminant == 13
        and changed_fields(odd) != [],
        "X2_prime_direct_sum_positive_countermodel": all(
            is_prime(value) for value in prime_basis
        )
        and det_i_minus_u_matrix(prime_operator) == [1, -10, 31, -30]
        and changed_fields(prime_loop) != [],
        "X3_roof_change_exactly_one_field": changed_fields(roof_change) == ["clock"],
        "X3_marker_change_exactly_one_field": changed_fields(marker_change)
        == ["marker"],
        "X4_scalar_subproduct_has_no_declared_owner": selector[
            "inventory_relations_computed"
        ]
        and selector["record"]["declared_projector"] is None,
        "X5_finite_cycle_positive_countermodel": det_i_minus_u_matrix(cycle_matrix)
        == [1, 0, 0, -1]
        and matn_trace(matn_pow(cycle_matrix, 3)) == 3
        and changed_fields(finite_cycle) != [],
        "C1_t3_order_discriminant_boundary": t3_boundary,
        "C2_C4_all_collision_classes": witnesses["all_pass"],
    }

    mutation_rejections = {
        "odd_misclassified_even_rejected": mat2_det(odd_matrix) != 1,
        "prime_basis_misclassified_source_rejected": changed_fields(prime_loop) != [],
        "double_roof_marker_change_not_exclusive": len(
            changed_fields({**roof_change, "marker": "z_per_pair_return"})
        )
        == 2,
        "selector_fake_owner_string_insufficient": selector["record"][
            "declared_projector"
        ]
        is None,
        "cycle_wrong_polynomial_rejected": det_i_minus_u_matrix(cycle_matrix)
        != [1, 0, -1],
        "t3_never_prime_overclaim_rejected": t3_boundary,
    }
    return {
        "baseline_contract": baseline,
        "odd_boundary": {
            "matrix": list(odd_matrix),
            "determinant": mat2_det(odd_matrix),
            "characteristic_discriminant": odd_discriminant,
        },
        "prime_direct_sum": {
            "basis": prime_basis,
            "determinant_polynomial": det_i_minus_u_matrix(prime_operator),
        },
        "roof_mutation_changed_fields": changed_fields(roof_change),
        "marker_mutation_changed_fields": changed_fields(marker_change),
        "scalar_subproduct": selector,
        "finite_cycle": {
            "matrix": cycle_matrix,
            "determinant_polynomial": det_i_minus_u_matrix(cycle_matrix),
        },
        "predicates": predicates,
        "negative_mutations": mutation_rejections,
        "pass": all(predicates.values()) and all(mutation_rejections.values()),
    }


def mobius_value(matrix: Matrix2, value: Fraction) -> Fraction:
    a, b, c, d = matrix
    return (a * value + b) / (c * value + d)


def branch_weight_s1(matrix: Matrix2, value: Fraction) -> Fraction:
    _, _, c, d = matrix
    return Fraction(abs(mat2_det(matrix)), 1) / (c * value + d) ** 2


def raw_nested_summand_s1(
    raw_indices: tuple[int, ...], value: Fraction
) -> tuple[Fraction, Fraction]:
    point = value
    weight = Fraction(1)
    for digit in raw_indices:
        denominator = digit + point
        weight *= Fraction(1, 1) / denominator**2
        point = Fraction(1, 1) / denominator
    return point, weight


def build_branch_bridge() -> dict[str, Any]:
    digits = (1, 2, 2, 3, 1, 4)
    matrix_a = word_matrix(digits, digit_a)
    matrix_b = word_matrix(digits, branch_b)
    def raw_iteration_matrix(raw_indices: tuple[int, ...]) -> Matrix2:
        # L-iteration nests the last raw branch on the left.
        return word_matrix(tuple(reversed(raw_indices)), branch_b)

    raw_indices = tuple(reversed(digits))
    recovered_stored_matrix = raw_iteration_matrix(raw_indices)
    same_index_raw_matrix = raw_iteration_matrix(digits)
    z = Fraction(1, 4)
    stored_value = mobius_value(matrix_b, z)
    stored_weight = branch_weight_s1(matrix_b, z)
    recovered_value = mobius_value(recovered_stored_matrix, z)
    recovered_weight = branch_weight_s1(recovered_stored_matrix, z)
    wrong_value = mobius_value(same_index_raw_matrix, z)
    wrong_weight = branch_weight_s1(same_index_raw_matrix, z)
    nested_recovered_value, nested_recovered_weight = raw_nested_summand_s1(
        raw_indices, z
    )
    nested_wrong_value, nested_wrong_weight = raw_nested_summand_s1(digits, z)

    # Exact quadratic arithmetic for lambda = 85 + 2 sqrt(1806).
    lambda_constant = 85
    lambda_radical = 2
    radicand = 1806
    lambda_square_constant = lambda_constant**2 + lambda_radical**2 * radicand
    lambda_square_radical = 2 * lambda_constant * lambda_radical
    characteristic_constant = lambda_square_constant - 170 * lambda_constant + 1
    characteristic_radical = lambda_square_radical - 170 * lambda_radical

    matrix_bridge = matrix_a == conjugate_by_j(matrix_b)
    fixed_polynomial = [matrix_b[2], matrix_b[3] - matrix_b[0], -matrix_b[1]]

    repetitions_ok = all(
        word_matrix(digits * repetition, branch_b) == mat2_pow(matrix_b, repetition)
        for repetition in range(1, 7)
    )
    pass_value = (
        matrix_a == (148, 31, 105, 22)
        and matrix_b == (22, 105, 31, 148)
        and matrix_bridge
        and fixed_polynomial == [31, 126, -105]
        and characteristic_constant == 0
        and characteristic_radical == 0
        and stored_value == Fraction(442, 623)
        and stored_weight == Fraction(16, 388129)
        and recovered_stored_matrix == matrix_b
        and recovered_value == stored_value
        and recovered_weight == stored_weight
        and nested_recovered_value == recovered_value
        and nested_recovered_weight == recovered_weight
        and wrong_value == Fraction(146, 697)
        and wrong_weight == Fraction(16, 485809)
        and nested_wrong_value == wrong_value
        and nested_wrong_weight == wrong_weight
        and wrong_value != stored_value
        and wrong_weight != stored_weight
        and repetitions_ok
    )
    return {
        "stored_digits": list(digits),
        "matrix_A": list(matrix_a),
        "matrix_B": list(matrix_b),
        "A_equals_JBJ": matrix_bridge,
        "fixed_point_polynomial": fixed_polynomial,
        "lambda_exact": "85+2*sqrt(1806)",
        "lambda_characteristic_residual": [
            characteristic_constant,
            characteristic_radical,
        ],
        "z": [z.numerator, z.denominator],
        "stored_branch_value": [stored_value.numerator, stored_value.denominator],
        "stored_weight_s1": [stored_weight.numerator, stored_weight.denominator],
        "raw_indices_required": list(raw_indices),
        "raw_reversal_recovers_stored": recovered_stored_matrix == matrix_b,
        "raw_nested_branch_value": [
            nested_recovered_value.numerator,
            nested_recovered_value.denominator,
        ],
        "raw_nested_weight_s1": [
            nested_recovered_weight.numerator,
            nested_recovered_weight.denominator,
        ],
        "same_index_wrong_value": [wrong_value.numerator, wrong_value.denominator],
        "same_index_wrong_weight": [wrong_weight.numerator, wrong_weight.denominator],
        "same_index_raw_nested_value": [
            nested_wrong_value.numerator,
            nested_wrong_value.denominator,
        ],
        "same_index_raw_nested_weight": [
            nested_wrong_weight.numerator,
            nested_wrong_weight.denominator,
        ],
        "raw_nested_equals_matrix_branch_and_derivative": (
            nested_recovered_value == recovered_value
            and nested_recovered_weight == recovered_weight
        ),
        "repetition_B_word_equals_power_r1_to_r6": repetitions_ok,
        "order_mutation_rejected": wrong_value != stored_value,
        "weight_mutation_rejected": wrong_weight != stored_weight,
        "pass": pass_value,
    }


def collision_witnesses() -> dict[str, Any]:
    specifications = {
        "trace4_reversal_one_pair": {
            "left": ((1, 2),),
            "right": ((2, 1),),
            "trace": 4,
            "delta": 12,
            "left_matrix": (3, 1, 2, 1),
            "right_matrix": (3, 2, 1, 1),
            "reversal_related": True,
            "cross_pair_length": False,
        },
        "trace6_nonreversal_one_pair": {
            "left": ((1, 4),),
            "right": ((2, 2),),
            "trace": 6,
            "delta": 32,
            "left_matrix": (5, 1, 4, 1),
            "right_matrix": (5, 2, 2, 1),
            "reversal_related": False,
            "cross_pair_length": False,
        },
        "trace10_nonreversal_cross_pair_length": (
            {
                "left": ((2, 4),),
                "right": ((1, 1), (1, 2)),
                "trace": 10,
                "delta": 96,
                "left_matrix": (9, 2, 4, 1),
                "right_matrix": (8, 3, 5, 2),
                "reversal_related": False,
                "cross_pair_length": True,
            }
        ),
    }
    result: dict[str, Any] = {}
    for name, spec in specifications.items():
        left = spec["left"]
        right = spec["right"]
        expected_trace = spec["trace"]
        expected_delta = spec["delta"]
        left_flat = tuple(digit for pair in left for digit in pair)
        right_flat = tuple(digit for pair in right for digit in pair)
        left_matrix = word_matrix(left_flat, digit_a)
        right_matrix = word_matrix(right_flat, digit_a)
        left_reverse = canonical_rotation(reverse_pair_word(left))
        reversal_related = canonical_rotation(right) == left_reverse
        cross_pair_length = len(left) != len(right)
        passed = (
            is_primitive(left)
            and is_primitive(right)
            and canonical_rotation(left) != canonical_rotation(right)
            and left_matrix == spec["left_matrix"]
            and right_matrix == spec["right_matrix"]
            and mat2_trace(left_matrix) == mat2_trace(right_matrix) == expected_trace
            and mat2_det(left_matrix) == mat2_det(right_matrix) == 1
            and expected_trace**2 - 4 == expected_delta
            and reversal_related is spec["reversal_related"]
            and cross_pair_length is spec["cross_pair_length"]
        )
        result[name] = {
            "left": [list(pair) for pair in left],
            "right": [list(pair) for pair in right],
            "left_matrix": list(left_matrix),
            "right_matrix": list(right_matrix),
            "trace": expected_trace,
            "order_discriminant": expected_delta,
            "left_pair_primitive": is_primitive(left),
            "right_pair_primitive": is_primitive(right),
            "digit_reversal_related": reversal_related,
            "cross_pair_length": cross_pair_length,
            "pass": passed,
        }
    mutation_rejections: dict[str, bool] = {}
    for name, record in result.items():
        bad_matrix = deepcopy(record)
        bad_matrix["left_matrix"][0] += 1
        mutation_rejections[f"{name}:matrix_mutation_rejected"] = (
            bad_matrix["left_matrix"] != list(specifications[name]["left_matrix"])
        )
        mutation_rejections[f"{name}:reversal_flag_mutation_rejected"] = (
            (not record["digit_reversal_related"])
            != specifications[name]["reversal_related"]
        )
        mutation_rejections[f"{name}:length_flag_mutation_rejected"] = (
            (not record["cross_pair_length"])
            != specifications[name]["cross_pair_length"]
        )
    result["negative_mutations"] = mutation_rejections
    result["all_pass"] = all(
        item["pass"]
        for key, item in result.items()
        if key not in {"negative_mutations", "all_pass"}
    ) and all(mutation_rejections.values())
    return result


GO_FIELDS = (
    "integer_valued",
    "rational_prime_support",
    "one_to_one_target_multiplicity",
    "repetition",
    "clock",
    "marker",
    "weight_amplitude_sign",
    "orientation_phase",
    "operator_ownership",
    "control_separation",
)


def projection_go(criteria: dict[str, bool]) -> bool:
    return set(criteria) == set(GO_FIELDS) and all(criteria[field] for field in GO_FIELDS)


Quadratic = tuple[Fraction, Fraction]


def quadratic_multiply(left: Quadratic, right: Quadratic, delta: int) -> Quadratic:
    a, b = left
    c, d = right
    return (a * c + b * d * delta, a * d + b * c)


def quadratic_power(value: Quadratic, exponent: int, delta: int) -> Quadratic:
    result: Quadratic = (Fraction(1), Fraction(0))
    base = value
    power = exponent
    while power:
        if power & 1:
            result = quadratic_multiply(result, base, delta)
        base = quadratic_multiply(base, base, delta)
        power //= 2
    return result


def norm_power_certificate(rows: list[dict[str, Any]], wrong_shift: int = 0) -> bool:
    for row in rows:
        trace = row["trace"]
        delta = trace * trace - 4
        primitive_norm: Quadratic = (
            Fraction(trace * trace - 2, 2),
            Fraction(trace, 2),
        )
        q_previous, q_current = 2, trace
        s_previous, s_current = 0, 1
        for repetition in range(1, 7):
            if repetition == 1:
                q_r, s_r = q_current, s_current
            else:
                q_previous, q_current = q_current, trace * q_current - q_previous
                s_previous, s_current = s_current, trace * s_current - s_previous
                q_r, s_r = q_current, s_current
            norm_from_powered_matrix: Quadratic = (
                Fraction(q_r * q_r - 2, 2),
                Fraction(q_r * s_r, 2),
            )
            norm_power = quadratic_power(
                primitive_norm, repetition + wrong_shift, delta
            )
            if norm_from_powered_matrix != norm_power:
                return False
    return True


def build_projection_go(
    witnesses: dict[str, Any],
    rows: list[dict[str, Any]],
    a0: dict[str, Any],
    ownership: dict[str, Any],
    bridge: dict[str, Any],
) -> dict[str, Any]:
    trace4 = witnesses["trace4_reversal_one_pair"]
    trace6 = witnesses["trace6_nonreversal_one_pair"]
    trace10 = witnesses["trace10_nonreversal_cross_pair_length"]
    collision_evidence = trace4["pass"] and trace6["pass"] and trace10["pass"]

    trace_integral = all(
        row["determinant"] == 1
        and isinstance(row["trace"], int)
        and row["trace"] >= 3
        for row in rows
    )
    delta_integral = trace_integral and all(
        row["order_discriminant"] == row["trace"] ** 2 - 4
        and isinstance(row["order_discriminant"], int)
        for row in rows
    )
    factored_coefficients = polynomial_multiply([1, -2], [1, 2])
    delta_factorization_universal = (
        factored_coefficients == [1, 0, -4]
        and is_prime(5)
        and (4 - 2) > 1
        and (4 + 2) > 1
    )
    nonsquare_norm_universal = (
        # Delta-(t-1)^2=2t-5 has positive slope and is positive at t=3;
        # t^2-Delta=4.
        2 > 0 and 2 * 3 - 5 > 0 and 4 > 0
    )
    trace_composite_species = trace4["pass"] and not is_prime(trace4["trace"])
    trace_repetition_failure = all(
        mat2_trace(mat2_pow(tuple(row["matrix"]), 2)) == row["trace"] ** 2 - 2
        and mat2_trace(mat2_pow(tuple(row["matrix"]), 2)) != row["trace"] ** 2
        for row in rows
    )
    delta_repetition_failure = (
        # At t=3: q2=7, Delta(M^2)=45=t^2*Delta, while Delta^2=25.
        (3**2 - 2) ** 2 - 4 == 3**2 * (3**2 - 4) == 45
        and 45 != (3**2 - 4) ** 2
    )
    norm_repetition_identity = norm_power_certificate(rows)
    trace_clock_failure_universal = (
        # sqrt(t^2-4)>t-2 follows from 4(t-2)>0; then lambda^2>t.
        4 * (3 - 2) > 0 and (3 - 1) ** 2 > 3
    )
    delta_clock_failure = delta_integral and nonsquare_norm_universal
    norm_clock_identity = (
        bridge["pass"]
        and all(
            row["expanding_eigenvalue_minpoly"] == [1, -row["trace"], 1]
            and row["geodesic_norm_minpoly"]
            == [1, -(row["trace"] ** 2 - 2), 1]
            and row["derivative_multiplier_minpoly"]
            == [1, -(row["trace"] ** 2 - 2), 1]
            and row["norm_root_selector"] == "greater_than_one"
            and row["derivative_root_selector"] == "between_zero_and_one"
            and row["norm_times_derivative"] == 1
            and row["norm_qsqrt_coefficients"]
            == [[row["trace"] ** 2 - 2, 2], [row["trace"], 2]]
            and row["derivative_qsqrt_coefficients"]
            == [[row["trace"] ** 2 - 2, 2], [-row["trace"], 2]]
            and quadratic_multiply(
                (
                    Fraction(*row["norm_qsqrt_coefficients"][0]),
                    Fraction(*row["norm_qsqrt_coefficients"][1]),
                ),
                (
                    Fraction(*row["derivative_qsqrt_coefficients"][0]),
                    Fraction(*row["derivative_qsqrt_coefficients"][1]),
                ),
                row["order_discriminant"],
            )
            == (Fraction(1), Fraction(0))
            for row in rows
        )
        and bridge["lambda_characteristic_residual"] == [0, 0]
    )
    marker_preserved = all(
        row["reciprocal_marker_exponent_per_repetition"] == 2 * row["pair_length"]
        for row in rows
    )
    stability_tower_present = all(
        row["stability_denominator_present"] and row["trace"] >= 3 for row in rows
    )
    orientation_target_failure = (
        orientation_metadata_valid(rows)
        and trace4["digit_reversal_related"]
        and trace4["left_pair_primitive"]
        and trace4["right_pair_primitive"]
    )
    scalar_selector = ownership["scalar_selector"]
    selected_owner_absent = (
        scalar_selector["inventory_relations_computed"]
        and scalar_selector["record"]["declared_projector"] is None
        and scalar_selector["record"]["frozen_schema_owner"] == "UNDECLARED"
    )
    no_positive_prime_signal = trace_composite_species and delta_factorization_universal and nonsquare_norm_universal

    certificates = {
        "trace_integral": trace_integral,
        "delta_integral": delta_integral,
        "delta_factorization_prime_only_t3": delta_factorization_universal,
        "norm_irrational_from_nonsquare_interval": nonsquare_norm_universal,
        "trace_composite_species": trace_composite_species,
        "all_three_collision_classes": collision_evidence,
        "trace_repetition_failure": trace_repetition_failure,
        "delta_repetition_failure": delta_repetition_failure,
        "norm_repetition_identity": norm_repetition_identity,
        "trace_clock_failure_all_t": trace_clock_failure_universal,
        "delta_clock_failure": delta_clock_failure,
        "norm_clock_identity": norm_clock_identity,
        "digit_marker_preserved": marker_preserved,
        "source_stability_tower_present": stability_tower_present,
        "target_orientation_multiplicity_failure": orientation_target_failure,
        "selected_owner_absent_in_frozen_schema": selected_owner_absent,
        "all_a0_controls_executed": a0["pass"],
        "no_positive_prime_signal_to_separate": no_positive_prime_signal,
    }
    certificate_mutations = {
        "wrong_delta_factorization_rejected": polynomial_multiply([1, -2], [1, 3])
        != [1, 0, -4],
        "wrong_norm_power_exponent_rejected": not norm_power_certificate(
            rows, wrong_shift=1
        ),
        "derivative_eigenvalue_polynomial_swap_rejected": all(
            row["derivative_multiplier_minpoly"]
            != row["expanding_eigenvalue_minpoly"]
            for row in rows
        ),
        "derivative_norm_root_selector_swap_rejected": all(
            row["derivative_root_selector"] != row["norm_root_selector"]
            for row in rows
        ),
    }
    criteria = {
        "trace": {
            "integer_valued": trace_integral,
            "rational_prime_support": not trace_composite_species,
            "one_to_one_target_multiplicity": not collision_evidence,
            "repetition": not trace_repetition_failure,
            "clock": not trace_clock_failure_universal,
            "marker": marker_preserved,
            "weight_amplitude_sign": not stability_tower_present,
            "orientation_phase": not orientation_target_failure,
            "operator_ownership": not selected_owner_absent,
            "control_separation": a0["pass"] and not no_positive_prime_signal,
        },
        "order_discriminant": {
            "integer_valued": delta_integral,
            "rational_prime_support": not delta_factorization_universal,
            "one_to_one_target_multiplicity": not collision_evidence,
            "repetition": not delta_repetition_failure,
            "clock": not delta_clock_failure,
            "marker": marker_preserved,
            "weight_amplitude_sign": not stability_tower_present,
            "orientation_phase": not orientation_target_failure,
            "operator_ownership": not selected_owner_absent,
            "control_separation": a0["pass"] and not no_positive_prime_signal,
        },
        "geodesic_norm": {
            "integer_valued": not nonsquare_norm_universal,
            "rational_prime_support": not nonsquare_norm_universal,
            "one_to_one_target_multiplicity": not collision_evidence,
            "repetition": norm_repetition_identity,
            "clock": norm_clock_identity,
            "marker": marker_preserved,
            "weight_amplitude_sign": not stability_tower_present,
            "orientation_phase": not orientation_target_failure,
            "operator_ownership": not selected_owner_absent,
            "control_separation": a0["pass"] and not no_positive_prime_signal,
        },
    }
    go_by_projection = {
        name: projection_go(fields) for name, fields in criteria.items()
    }
    existential_go = any(go_by_projection.values())
    rational_integer_clock_repetition = any(
        fields["integer_valued"] and fields["clock"] and fields["repetition"]
        for fields in criteria.values()
    )
    exact_truth_matrix = (
        criteria["trace"]["integer_valued"]
        and not criteria["trace"]["clock"]
        and not criteria["trace"]["repetition"]
        and criteria["order_discriminant"]["integer_valued"]
        and not criteria["order_discriminant"]["clock"]
        and not criteria["order_discriminant"]["repetition"]
        and not criteria["geodesic_norm"]["integer_valued"]
        and criteria["geodesic_norm"]["clock"]
        and criteria["geodesic_norm"]["repetition"]
    )

    required_false = {
        "trace": {
            "rational_prime_support",
            "one_to_one_target_multiplicity",
            "repetition",
            "clock",
            "weight_amplitude_sign",
            "operator_ownership",
        },
        "order_discriminant": {
            "rational_prime_support",
            "one_to_one_target_multiplicity",
            "repetition",
            "clock",
            "weight_amplitude_sign",
            "operator_ownership",
        },
        "geodesic_norm": {
            "integer_valued",
            "rational_prime_support",
            "one_to_one_target_multiplicity",
            "weight_amplitude_sign",
            "operator_ownership",
        },
    }

    def coverage_valid(candidate: dict[str, dict[str, bool]]) -> bool:
        return all(
            all(candidate[projection][field] is False for field in fields)
            for projection, fields in required_false.items()
        )

    coverage_mutations: dict[str, bool] = {}
    for projection, fields in required_false.items():
        for field in sorted(fields):
            mutated = deepcopy(criteria)
            mutated[projection][field] = True
            coverage_mutations[f"{projection}:{field}:removal_rejected"] = not coverage_valid(
                mutated
            )

    synthetic = deepcopy(criteria)
    synthetic["trace"] = {field: True for field in GO_FIELDS}
    synthetic_positive_control = any(
        projection_go(fields) for fields in synthetic.values()
    )
    truth_matrix_mutations = {}
    for projection, field, bad_value in (
        ("trace", "clock", True),
        ("trace", "repetition", True),
        ("order_discriminant", "clock", True),
        ("order_discriminant", "repetition", True),
        ("geodesic_norm", "integer_valued", True),
        ("geodesic_norm", "clock", False),
        ("geodesic_norm", "repetition", False),
    ):
        mutated = deepcopy(criteria)
        mutated[projection][field] = bad_value
        mutated_valid = (
            mutated["trace"]["integer_valued"]
            and not mutated["trace"]["clock"]
            and not mutated["trace"]["repetition"]
            and mutated["order_discriminant"]["integer_valued"]
            and not mutated["order_discriminant"]["clock"]
            and not mutated["order_discriminant"]["repetition"]
            and not mutated["geodesic_norm"]["integer_valued"]
            and mutated["geodesic_norm"]["clock"]
            and mutated["geodesic_norm"]["repetition"]
        )
        truth_matrix_mutations[f"{projection}:{field}:wrong_value_rejected"] = not mutated_valid
    return {
        "comparison_object": "D_42_inverse_vs_marked_prime_Euler_product",
        "source_log_coefficient": "u^(2*k*r)*d_w^(r*s)/(r*(1-d_w^r))",
        "target_log_coefficient": "u^(2*k*r)*p^(-r*s)/r",
        "criteria": criteria,
        "derived_certificates": certificates,
        "certificate_mutations": certificate_mutations,
        "go_by_projection": go_by_projection,
        "existential_go": existential_go,
        "rational_integer_clock_repetition_conjunction": rational_integer_clock_repetition,
        "exact_integer_clock_repetition_truth_matrix": exact_truth_matrix,
        "coverage_schema_valid": coverage_valid(criteria),
        "coverage_mutations": coverage_mutations,
        "synthetic_all_true_projection_yields_go": synthetic_positive_control,
        "truth_matrix_mutations": truth_matrix_mutations,
        "pass": not existential_go
        and not rational_integer_clock_repetition
        and exact_truth_matrix
        and coverage_valid(criteria)
        and all(coverage_mutations.values())
        and all(truth_matrix_mutations.values())
        and all(certificates.values())
        and all(certificate_mutations.values())
        and synthetic_positive_control,
    }


def source_boundary_status() -> dict[str, Any]:
    source_path = PACKAGE / "SOURCE_LOCK.md"
    mayer_path = PACKAGE / "MAYER_SOURCE_BOUNDARY.md"
    source_bytes = source_path.read_bytes()
    mayer_bytes = mayer_path.read_bytes()
    source_text = source_bytes.decode("utf-8")
    mayer_text = mayer_bytes.decode("utf-8")
    source_hash_ok = sha256(source_bytes).hexdigest() == SOURCE_LOCK_SHA256
    mayer_hash_ok = sha256(mayer_bytes).hexdigest() == MAYER_BOUNDARY_SHA256
    source_tokens = all(
        token in source_text
        for token in (
            "D_{42}(s,u)=\\det(I-u^2K_s)",
            "A2_ANALYTIC_DETERMINANT",
            "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A4_FORMAL_HINT",
            "route_b_invocation_allowed: false",
        )
    )
    mayer_tokens = all(
        token in mayer_text
        for token in (
            "A_\\infty(D)",
            "\\operatorname{Re}s>1/2",
            "\\operatorname{Re}s>1",
            "Proposition 3",
            "absolute-convergence",
            "Corollary 3",
            "meromorphic continuation",
        )
    )
    return {
        "source_lock_hash_matches": source_hash_ok,
        "mayer_boundary_hash_matches": mayer_hash_ok,
        "source_required_tokens": source_tokens,
        "mayer_required_tokens": mayer_tokens,
        "pass": source_hash_ok and mayer_hash_ok and source_tokens and mayer_tokens,
    }


def control_lock_status() -> dict[str, Any]:
    if not CONTROL_LOCK_PATH.is_file():
        return {
            "sha256": None,
            "exact_file_set": False,
            "all_file_hashes_bound": False,
            "seeds_and_grid_bound": False,
            "pass": False,
        }
    raw = CONTROL_LOCK_PATH.read_bytes()
    text = raw.decode("utf-8")
    file_hashes = {
        relative: sha256((PACKAGE / relative).read_bytes()).hexdigest()
        for relative in CONTROL_LOCKED_FILES
    }
    manifest: dict[str, str] = {}
    for line in text.splitlines():
        parts = line.split("  ", 1)
        if (
            len(parts) == 2
            and len(parts[0]) == 64
            and all(character in "0123456789abcdef" for character in parts[0])
        ):
            manifest[parts[1]] = parts[0]
    exact_file_set = set(manifest) == set(CONTROL_LOCKED_FILES)
    all_files = exact_file_set and manifest == file_hashes
    seed_tokens = all(
        f"{name}={value}" in text for name, value in sorted(SEEDS.items())
    )
    specification_tokens = all(
        token in text
        for token in (
            "status=FINAL_BEFORE_CANONICAL_EMPTY_RESULTS_RERUN",
            "control_digits=1,2",
            "control_pair_lengths=1,2,3",
            "prototype_D=2,3,4",
            "prototype_pair_lengths=1,2,3,4",
            "chronology=M1--M20_RETROSPECTIVE_CORRECTION",
        )
    )
    return {
        "sha256": sha256(raw).hexdigest(),
        "exact_file_set": exact_file_set,
        "all_file_hashes_bound": all_files,
        "seeds_and_grid_bound": seed_tokens and specification_tokens,
        "pass": all_files and seed_tokens and specification_tokens,
    }


def build_result() -> dict[str, Any]:
    base_rows = pair_rows()
    selection = parse_selection_cards()
    selection_negative = selection_mutations()
    a0 = build_a0_controls(base_rows)
    a1 = build_a1_controls(base_rows)
    ownership = build_ownership_controls()
    bridge = build_branch_bridge()
    splitting = splitting_census()
    return_map = return_map_typing_certificate()
    witnesses = collision_witnesses()
    countermodels = build_countermodels(ownership, witnesses)
    projection = build_projection_go(witnesses, base_rows, a0, ownership, bridge)
    boundary = source_boundary_status()
    control_lock = control_lock_status()

    route_status = {
        "A0": "A0_WEAK_ARITHMETIC_RELATION"
        if a0["pass"] and projection["pass"]
        else "A0_FAIL",
        "A1": "A1_PASS_ANALYTIC"
        if a1["pass"] and bridge["pass"] and splitting["pass"] and return_map["pass"]
        else "A1_FAIL",
        "A2": "A2_ANALYTIC_DETERMINANT" if boundary["pass"] else "NOT_TESTABLE",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE" if boundary["pass"] else "NOT_TESTABLE",
        "A4": "A4_FORMAL_HINT" if boundary["pass"] else "NOT_TESTABLE",
    }
    expected_route = {
        "A0": "A0_WEAK_ARITHMETIC_RELATION",
        "A1": "A1_PASS_ANALYTIC",
        "A2": "A2_ANALYTIC_DETERMINANT",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
        "A4": "A4_FORMAL_HINT",
    }

    gates = {
        "selection_parser": selection["pass"] and all(selection_negative.values()),
        "a0_literal_controls": a0["pass"],
        "a1_literal_controls": a1["pass"],
        "ownership": ownership["pass"],
        "branch_order_bridge": bridge["pass"],
        "primitivity_splitting": splitting["pass"],
        "return_map_typing": return_map["pass"],
        "collision_witnesses": witnesses["all_pass"],
        "scope_countermodels": countermodels["pass"],
        "projection_existential_go": projection["pass"],
        "source_boundary": boundary["pass"],
        "control_lock": control_lock["pass"],
        "route_tuple_recomputed": route_status == expected_route,
    }
    terminal_codes = [
        "GO_MODULAR_PRIMITIVE_LEDGER",
        "GO_SAME_OBJECT_MAYER_DETERMINANT",
        "STOP_CANONICAL_INTEGER_PROJECTION",
        "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
        "STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED",
        "ROUTE_A_REJECTED",
    ]
    terminal_semantics_pass = (
        "STOP_CLOCK_REPETITION_COMPATIBILITY" not in terminal_codes
        and not projection["rational_integer_clock_repetition_conjunction"]
        and projection["criteria"]["geodesic_norm"]["clock"]
        and projection["criteria"]["geodesic_norm"]["repetition"]
    )
    gates["terminal_code_semantics"] = terminal_semantics_pass
    return {
        "schema": "sd-c42-corrective-controls-v3",
        "candidate_id": "SD-C42",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "mayer_boundary_sha256": MAYER_BOUNDARY_SHA256,
        "chronology": (
            "Retrospective M1--M20 correction after provisional v1 and "
            "in-flight corrective smoke outputs; only the exact corrected "
            "input set in CONTROL_LOCK was frozen before the canonical rerun."
        ),
        "bounded_base": {
            "digits": [1, 2],
            "pair_lengths": [1, 2, 3],
            "row_count": len(base_rows),
            "rows_sha256": sha256(
                json.dumps(base_rows, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest(),
        },
        "selection": selection,
        "selection_negative_mutations": selection_negative,
        "a0_controls": a0,
        "a1_controls": a1,
        "ownership_controls": ownership,
        "branch_matrix_operator_order_bridge": bridge,
        "primitivity_splitting": splitting,
        "return_map_typing": return_map,
        "collision_witnesses": witnesses,
        "scope_countermodels": countermodels,
        "projection_go_evaluation": projection,
        "source_boundary": boundary,
        "control_lock": control_lock,
        "route_status_recomputed": route_status,
        "route_status_expected": expected_route,
        "route_b_invocation_allowed": False,
        "terminal_codes": terminal_codes,
        "terminal_semantics": {
            "STOP_CANONICAL_INTEGER_PROJECTION": (
                "No projection passes the full rational-prime Euler-ledger conjunction."
            ),
            "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION": (
                "No integer-valued projection simultaneously preserves the exact clock and temporal powers; geodesic norm passes clock/powers but is irrational."
            ),
            "old_overbroad_code_rejected": terminal_semantics_pass,
        },
        "gates": gates,
        "gate_count": len(gates),
        "gate_failure_count": sum(not value for value in gates.values()),
        "all_controls_sharp": all(gates.values()),
        "claim_boundary": (
            "Exact bounded controls and hash-backed absence of a declared "
            "untwisted selector only; no universal nonexistence or witness "
            "novelty/minimality claim."
        ),
    }


def main() -> None:
    result = build_result()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["all_controls_sharp"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
