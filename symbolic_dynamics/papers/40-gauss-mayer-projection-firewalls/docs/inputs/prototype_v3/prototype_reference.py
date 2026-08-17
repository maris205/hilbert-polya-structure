#!/usr/bin/env python3
"""Exact bounded reference audit for the frozen SD-C42 contract.

The program uses only Python integers. It prints one deterministic JSON
record and does not write files. It does not evaluate the Mayer determinant or
load any prime/zero table.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import sys


PACKAGE = Path(__file__).resolve().parent
SOURCE_LOCK_SHA256 = "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041"
CONTROL_LOCK_PATH = PACKAGE / "CONTROL_LOCK.md"
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

Matrix = tuple[int, int, int, int]
Pair = tuple[int, int]
PairWord = tuple[Pair, ...]
IDENTITY: Matrix = (1, 0, 0, 1)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def matpow(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise ValueError("negative powers are outside the exact prototype")
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power >>= 1
    return result


def digit_matrix(a: int) -> Matrix:
    if a < 1:
        raise ValueError("digits must be positive")
    return (a, 1, 1, 0)


def pair_matrix(pair: Pair) -> Matrix:
    return matmul(digit_matrix(pair[0]), digit_matrix(pair[1]))


def monodromy(word: PairWord) -> Matrix:
    result = IDENTITY
    for pair in word:
        result = matmul(result, pair_matrix(pair))
    return result


def determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def trace(matrix: Matrix) -> int:
    return matrix[0] + matrix[3]


def rotations(word: PairWord) -> tuple[PairWord, ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_rotation(word: PairWord) -> PairWord:
    return min(rotations(word))


def reverse_pair_word(word: PairWord) -> PairWord:
    return tuple((right, left) for left, right in reversed(word))


def word_id(word: PairWord) -> str:
    return "|".join(f"{left},{right}" for left, right in word)


def is_primitive(word: PairWord) -> bool:
    length = len(word)
    for period in range(1, length):
        if length % period == 0 and word == word[:period] * (length // period):
            return False
    return True


def primitive_necklaces(alphabet: tuple[Pair, ...], length: int):
    for word in itertools.product(alphabet, repeat=length):
        if is_primitive(word) and word == canonical_rotation(word):
            yield word


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            return False
        factor += 2
    return True


def flatten(word: PairWord) -> tuple[int, ...]:
    return tuple(digit for pair in word for digit in pair)


def word_json(word: PairWord) -> list[list[int]]:
    return [[a, b] for a, b in word]


def audit_alphabet(digits: tuple[int, ...], label: str) -> dict[str, object]:
    alphabet = tuple(itertools.product(digits, repeat=2))
    words_by_length = {
        length: list(primitive_necklaces(alphabet, length)) for length in range(1, 5)
    }
    orientation_ids = {
        word_id(word) for words in words_by_length.values() for word in words
    }
    counts_by_length: dict[str, int] = {}
    failures: dict[str, int] = defaultdict(int)
    trace_prime_count = 0
    trace_composite_count = 0
    order_discriminant_prime_count = 0
    order_discriminant_prime_nonboundary_count = 0
    collision_groups: dict[int, list[PairWord]] = defaultdict(list)
    rows: list[dict[str, object]] = []

    for length in range(1, 5):
        necklaces = words_by_length[length]
        counts_by_length[str(length)] = len(necklaces)
        for word in necklaces:
            matrix = monodromy(word)
            det = determinant(matrix)
            tr = trace(matrix)
            delta = tr * tr - 4

            if det != 1:
                failures["determinant_one"] += 1
            if tr < 3:
                failures["trace_at_least_three"] += 1
            if delta != (tr - 2) * (tr + 2):
                failures["order_discriminant_factorization"] += 1
            if not ((tr - 1) ** 2 < delta < tr * tr):
                failures["nonsquare_interval"] += 1
            if math.isqrt(delta) ** 2 == delta:
                failures["order_discriminant_nonsquare"] += 1
            if not (delta > (tr - 2) ** 2 and (tr - 1) ** 2 > tr):
                failures["clock_strict_inequality_certificate"] += 1

            q_prev, q_now = 2, tr
            for exponent in range(2, 7):
                q_next = tr * q_now - q_prev
                if trace(matpow(matrix, exponent)) != q_next:
                    failures["trace_power_recurrence"] += 1
                q_prev, q_now = q_now, q_next
            if trace(matpow(matrix, 2)) == tr * tr:
                failures["trace_square_mismatch"] += 1

            if is_prime(tr):
                trace_prime_count += 1
            else:
                trace_composite_count += 1
            if is_prime(delta):
                order_discriminant_prime_count += 1
                if not (tr == 3 and delta == 5):
                    order_discriminant_prime_nonboundary_count += 1

            collision_groups[tr].append(word)
            reverse = canonical_rotation(reverse_pair_word(word))
            orientation = word_id(word)
            reverse_orientation = word_id(reverse)
            rows.append(
                {
                    "delta_order": delta,
                    "determinant": det,
                    "matrix": list(matrix),
                    "pair_length": length,
                    "trace": tr,
                    "word": word_json(word),
                    "orientation_id": orientation,
                    "reverse_orientation_id": reverse_orientation,
                    "reversal_orbit_id": min(orientation, reverse_orientation),
                    "self_reversal": orientation == reverse_orientation,
                    "reverse_class_present": reverse_orientation in orientation_ids,
                    "source_multiplicity": 1,
                    "untwisted_sign": 1,
                    "phase_exponent_mod_97": 0,
                    "expanding_eigenvalue_minpoly": [1, -tr, 1],
                    "geodesic_norm_minpoly": [1, -(tr * tr - 2), 1],
                    "derivative_multiplier_minpoly": [1, -(tr * tr - 2), 1],
                    "norm_qsqrt_coefficients": [[tr * tr - 2, 2], [tr, 2]],
                    "derivative_qsqrt_coefficients": [[tr * tr - 2, 2], [-tr, 2]],
                    "marker_exponent_per_repetition": 2 * length,
                }
            )

    rows.sort(
        key=lambda row: (
            row["pair_length"],
            row["word"],
            row["matrix"],
        )
    )
    row_bytes = json.dumps(
        rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    colliding = [group for group in collision_groups.values() if len(group) > 1]

    return {
        "alphabet_label": label,
        "digits": list(digits),
        "pair_alphabet_size": len(alphabet),
        "primitive_pair_necklaces_by_length": counts_by_length,
        "primitive_pair_necklaces_total": len(rows),
        "theorem_failures": dict(sorted(failures.items())),
        "trace_prime_orbit_count": trace_prime_count,
        "trace_composite_orbit_count": trace_composite_count,
        "order_discriminant_prime_orbit_count": order_discriminant_prime_count,
        "order_discriminant_prime_nonboundary_count": (
            order_discriminant_prime_nonboundary_count
        ),
        "trace_collision_group_count": len(colliding),
        "trace_collision_orbit_excess": sum(len(group) - 1 for group in colliding),
        "scientific_rows_sha256": hashlib.sha256(row_bytes).hexdigest(),
    }


def witness_record(word: PairWord) -> dict[str, object]:
    matrix = monodromy(word)
    tr = trace(matrix)
    canonical = canonical_rotation(word)
    reverse = canonical_rotation(reverse_pair_word(word))
    return {
        "word": word_json(word),
        "flattened": list(flatten(word)),
        "primitive_pair_necklace": is_primitive(word),
        "canonical_pair_rotation": word == canonical,
        "orientation_id": word_id(canonical),
        "reverse_orientation_id": word_id(reverse),
        "digit_reversal_related_to_self": canonical == reverse,
        "matrix": list(matrix),
        "trace": tr,
        "determinant": determinant(matrix),
        "delta_order": tr * tr - 4,
    }


def collision_record(left: PairWord, right: PairWord) -> dict[str, object]:
    left_record = witness_record(left)
    right_record = witness_record(right)
    reversal_related = canonical_rotation(reverse_pair_word(left)) == canonical_rotation(
        right
    )
    exact = (
        left_record["primitive_pair_necklace"]
        and right_record["primitive_pair_necklace"]
        and left_record["trace"] == right_record["trace"]
        and left_record["determinant"] == right_record["determinant"] == 1
        and left_record["delta_order"] == right_record["delta_order"]
        and left_record["orientation_id"] != right_record["orientation_id"]
    )
    return {
        "left": left_record,
        "right": right_record,
        "digit_reversal_related": reversal_related,
        "cross_pair_length": len(left) != len(right),
        "exact": exact,
    }


def digit_primitive_count(alphabet: tuple[int, ...], length: int) -> int:
    return sum(
        1
        for word in itertools.product(alphabet, repeat=length)
        if is_primitive(word) and word == min(
            word[index:] + word[:index] for index in range(length)
        )
    )


def splitting_record() -> dict[str, object]:
    digits = (1, 2)
    pair_alphabet = tuple(itertools.product(digits, repeat=2))
    digit_counts = {
        length: digit_primitive_count(digits, length) for length in range(1, 7)
    }
    pair_counts = {
        length: sum(1 for _ in primitive_necklaces(pair_alphabet, length))
        for length in range(1, 4)
    }
    predicted = {
        length: 2 * digit_counts[2 * length]
        + (digit_counts[length] if length % 2 else 0)
        for length in range(1, 4)
    }
    trace4_phases = (
        trace(monodromy(((1, 2),))) == trace(monodromy(((2, 1),))) == 4
        and canonical_rotation(reverse_pair_word(((1, 2),))) == ((2, 1),)
    )
    flattened_22 = is_primitive(((2, 2),)) and not is_primitive((2, 2))
    return {
        "digit_counts_1_to_6": {str(key): value for key, value in digit_counts.items()},
        "pair_counts_1_to_3": {str(key): value for key, value in pair_counts.items()},
        "predicted_pair_counts": {str(key): value for key, value in predicted.items()},
        "trace4_two_rho_phases": trace4_phases,
        "flattened_22_pair_primitive_sigma_imprimitive": flattened_22,
        "pass": pair_counts == predicted == {1: 4, 2: 6, 3: 20}
        and trace4_phases
        and flattened_22,
    }


def return_map_record() -> dict[str, object]:
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
    word = ((1, 2), (2, 3), (1, 4))
    reversed_class = canonical_rotation(reverse_pair_word(word))
    flattened_word = tuple(digit for pair in word for digit in pair)
    raw_reversal_matches = group(tuple(reversed(flattened_word))) == reverse_pair_word(word)
    reversal_descends = all(
        canonical_rotation(reverse_pair_word(rotation)) == reversed_class
        for rotation in rotations(word)
    )
    primitive_preserved = is_primitive(word) == is_primitive(reverse_pair_word(word))
    block_mutation = canonical_rotation(tuple(reversed(word))) != reversed_class
    passed = (
        rho_grouped == grouped_sigma_two
        and wrong_pair_sigma_two != grouped_sigma_two
        and reversal_descends
        and raw_reversal_matches
        and primitive_preserved
        and block_mutation
    )
    return {
        "digit_fixture": list(digits),
        "iota_fixture": [list(pair) for pair in grouped],
        "rho_after_iota": [list(pair) for pair in rho_grouped],
        "iota_after_sigma_squared": [list(pair) for pair in grouped_sigma_two],
        "rho_iota_equals_iota_sigma_squared": rho_grouped
        == grouped_sigma_two,
        "wrong_sigma_squared_on_pair_space_rejected": wrong_pair_sigma_two
        != grouped_sigma_two,
        "global_reversal_descends_to_cyclic_pair_classes": reversal_descends,
        "global_raw_index_reversal_equals_pair_reverse": raw_reversal_matches,
        "global_reversal_preserves_pair_primitivity": primitive_preserved,
        "unreversed_block_order_mutation_rejected": block_mutation,
        "pass": passed,
    }


def branch_b(digit: int) -> Matrix:
    return (0, 1, 1, digit)


def word_branch_matrix(digits: tuple[int, ...]) -> Matrix:
    result = IDENTITY
    for digit in digits:
        result = matmul(result, branch_b(digit))
    return result


def mobius(matrix: Matrix, value: Fraction) -> Fraction:
    return (matrix[0] * value + matrix[1]) / (matrix[2] * value + matrix[3])


def nested_raw(raw: tuple[int, ...], value: Fraction) -> tuple[Fraction, Fraction]:
    point = value
    weight = Fraction(1)
    for digit in raw:
        denominator = digit + point
        weight /= denominator**2
        point = 1 / denominator
    return point, weight


def branch_order_record() -> dict[str, object]:
    stored = (1, 2, 2, 3, 1, 4)
    raw = tuple(reversed(stored))
    stored_matrix = word_branch_matrix(stored)
    raw_matrix = word_branch_matrix(tuple(reversed(raw)))
    wrong_matrix = word_branch_matrix(tuple(reversed(stored)))
    z = Fraction(1, 4)
    nested_value, nested_weight = nested_raw(raw, z)
    wrong_value, wrong_weight = nested_raw(stored, z)
    stored_value = mobius(stored_matrix, z)
    stored_weight = Fraction(1) / (stored_matrix[2] * z + stored_matrix[3]) ** 2
    passed = (
        raw_matrix == stored_matrix == (22, 105, 31, 148)
        and (nested_value, nested_weight)
        == (stored_value, stored_weight)
        == (Fraction(442, 623), Fraction(16, 388129))
        and (wrong_value, wrong_weight)
        == (Fraction(146, 697), Fraction(16, 485809))
        and wrong_matrix != stored_matrix
    )
    return {
        "stored_digits": list(stored),
        "raw_indices": list(raw),
        "stored_matrix_B": list(stored_matrix),
        "branch_value": [nested_value.numerator, nested_value.denominator],
        "weight_s1": [nested_weight.numerator, nested_weight.denominator],
        "same_index_wrong_value": [wrong_value.numerator, wrong_value.denominator],
        "same_index_wrong_weight": [wrong_weight.numerator, wrong_weight.denominator],
        "pass": passed,
    }


def control_lock_record() -> dict[str, object]:
    if not CONTROL_LOCK_PATH.is_file():
        return {
            "sha256": None,
            "exact_file_set": False,
            "all_inputs_bound": False,
            "pass": False,
        }
    raw = CONTROL_LOCK_PATH.read_bytes()
    text = raw.decode("utf-8")
    manifest: dict[str, str] = {}
    for line in text.splitlines():
        parts = line.split("  ", 1)
        if (
            len(parts) == 2
            and len(parts[0]) == 64
            and all(character in "0123456789abcdef" for character in parts[0])
        ):
            manifest[parts[1]] = parts[0]
    expected_manifest = {
        relative: hashlib.sha256((PACKAGE / relative).read_bytes()).hexdigest()
        for relative in CONTROL_LOCKED_FILES
    }
    exact_file_set = set(manifest) == set(CONTROL_LOCKED_FILES)
    all_inputs = exact_file_set and manifest == expected_manifest
    specification = all(
        token in text
        for token in (
            "status=FINAL_BEFORE_CANONICAL_EMPTY_RESULTS_RERUN",
            "prototype_D=2,3,4",
            "prototype_pair_lengths=1,2,3,4",
            "chronology=M1--M20_RETROSPECTIVE_CORRECTION",
        )
    )
    return {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "exact_file_set": exact_file_set,
        "all_inputs_bound": all_inputs and specification,
        "pass": all_inputs and specification,
    }


def main() -> None:
    source_hash_matches = (
        hashlib.sha256((PACKAGE / "SOURCE_LOCK.md").read_bytes()).hexdigest()
        == SOURCE_LOCK_SHA256
    )
    control_lock = control_lock_record()
    canonical = [
        audit_alphabet(tuple(range(1, d + 1)), f"canonical_D{d}")
        for d in (2, 3, 4)
    ]
    neighboring = [
        audit_alphabet(tuple(range(2, d + 2)), f"neighboring_D{d}")
        for d in (2, 3, 4)
    ]

    discriminant_boundary = witness_record(((1, 1),))
    composite_trace = witness_record(((1, 2),))
    collision_trace4 = collision_record(((1, 2),), ((2, 1),))
    collision_trace6 = collision_record(((1, 4),), ((2, 2),))
    collision_trace10 = collision_record(((2, 4),), ((1, 1), (1, 2)))
    collisions_exact = (
        collision_trace4["exact"]
        and collision_trace4["digit_reversal_related"]
        and collision_trace6["exact"]
        and not collision_trace6["digit_reversal_related"]
        and collision_trace10["exact"]
        and not collision_trace10["digit_reversal_related"]
        and collision_trace10["cross_pair_length"]
    )
    splitting = splitting_record()
    return_map = return_map_record()
    branch_order = branch_order_record()

    odd_matrix = digit_matrix(3)
    odd_trace = trace(odd_matrix)
    odd_boundary = {
        "word": [3],
        "matrix": list(odd_matrix),
        "determinant": determinant(odd_matrix),
        "trace": odd_trace,
        "characteristic_discriminant": odd_trace * odd_trace + 4,
        "in_theorem_domain": False,
    }

    all_runs = canonical + neighboring
    global_failures = sum(
        sum(run["theorem_failures"].values()) for run in all_runs
    )
    output = {
        "schema": "sd-c42-exact-prototype-v2",
        "candidate_id": "SD-C42",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_lock_hash_matches": source_hash_matches,
        "control_lock": control_lock,
        "chronology": (
            "Only the exact M1--M20 corrected input set in CONTROL_LOCK was frozen "
            "before this canonical rerun; v1 and in-flight smoke outputs were known."
        ),
        "arithmetic": "exact_integer_only",
        "prime_or_zero_table_loaded": False,
        "canonical_runs": canonical,
        "neighboring_runs": neighboring,
        "witnesses": {
            "order_discriminant_boundary": discriminant_boundary,
            "composite_trace": composite_trace,
            "trace4_reversal_collision": collision_trace4,
            "trace6_nonreversal_collision": collision_trace6,
            "trace10_cross_length_nonreversal_collision": collision_trace10,
            "all_three_collision_classes_exact": collisions_exact,
            "odd_parity_boundary": odd_boundary,
        },
        "primitivity_splitting": splitting,
        "return_map_typing": return_map,
        "branch_operator_order": branch_order,
        "aggregate": {
            "registered_run_count": len(all_runs),
            "scientific_row_count": sum(
                run["primitive_pair_necklaces_total"] for run in all_runs
            ),
            "theorem_failure_count": global_failures,
            "order_discriminant_nonboundary_prime_count": sum(
                run["order_discriminant_prime_nonboundary_count"]
                for run in all_runs
            ),
            "all_three_collision_classes_exact": collisions_exact,
            "primitivity_splitting_exact": splitting["pass"],
            "return_map_typing_exact": return_map["pass"],
            "branch_operator_order_exact": branch_order["pass"],
            "hard_status": (
                "PASS"
                if source_hash_matches
                and control_lock["pass"]
                and global_failures == 0
                and collisions_exact
                and splitting["pass"]
                and return_map["pass"]
                and branch_order["pass"]
                and discriminant_boundary["trace"] == 3
                and discriminant_boundary["delta_order"] == 5
                and composite_trace["trace"] == 4
                else "FAIL"
            ),
        },
        "claim_boundary": (
            "Bounded exact theorem audit only; not a Mayer determinant "
            "evaluation, novelty proof, or universal Gauss-map no-go."
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if output["aggregate"]["hard_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
