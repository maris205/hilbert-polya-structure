#!/usr/bin/env python3
"""Independent exact evaluator for the frozen SD-C42 bounded grid.

This implementation deliberately shares no functions with
``prototype_reference.py``. It uses the Fredricksen--Kessler--Maiorana
necklace recursion and continued-fraction continuants instead of raw-word
rotation filtering and repeated digit-matrix multiplication. It reads the
archival result and exits nonzero if any registered scientific-row digest or
summary count differs.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SOURCE_LOCK_SHA256 = "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041"
CONTROL_LOCK_PATH = HERE / "CONTROL_LOCK.md"
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


def aperiodic_necklace_indices(radix: int, size: int):
    digits = [0] * (size + 1)

    def visit(position: int, period: int):
        if position > size:
            if size % period == 0 and period == size:
                yield tuple(digits[1:])
            return
        digits[position] = digits[position - period]
        yield from visit(position + 1, period)
        for symbol in range(digits[position - period] + 1, radix):
            digits[position] = symbol
            yield from visit(position + 1, position)

    yield from visit(1, 1)


def continuant(sequence: tuple[int, ...]) -> int:
    if not sequence:
        return 1
    previous_previous, previous = 1, sequence[0]
    for value in sequence[1:]:
        previous_previous, previous = previous, value * previous + previous_previous
    return previous


def continued_fraction_matrix(flat: tuple[int, ...]) -> tuple[int, int, int, int]:
    if len(flat) == 1:
        return (flat[0], 1, 1, 0)
    return (
        continuant(flat),
        continuant(flat[:-1]),
        continuant(flat[1:]),
        continuant(flat[1:-1]),
    )


def rotate_min(word: tuple[object, ...]) -> tuple[object, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def pair_reverse(
    word: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    return tuple((right, left) for left, right in reversed(word))


def orientation_id(word: tuple[tuple[int, int], ...]) -> str:
    return "|".join(f"{left},{right}" for left, right in word)


def primality_trial_six(value: int) -> bool:
    if value <= 3:
        return value >= 2
    if value % 2 == 0 or value % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= value:
        if value % divisor == 0 or value % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def independent_run(digits: tuple[int, ...], label: str) -> dict[str, object]:
    pairs = tuple(itertools.product(digits, repeat=2))
    words_by_length = {
        length: [
            tuple(pairs[index] for index in indices)
            for indices in aperiodic_necklace_indices(len(pairs), length)
        ]
        for length in range(1, 5)
    }
    orientation_ids = {
        orientation_id(word)
        for words in words_by_length.values()
        for word in words
    }
    by_length: dict[str, int] = {}
    rows: list[dict[str, object]] = []
    trace_groups: dict[int, int] = {}
    trace_prime = 0
    delta_prime = 0
    delta_nonboundary_prime = 0
    failures: dict[str, int] = {}

    def record_failure(name: str, failed: bool) -> None:
        if failed:
            failures[name] = failures.get(name, 0) + 1

    for length in range(1, 5):
        pair_words = words_by_length[length]
        by_length[str(length)] = len(pair_words)
        for pair_word in pair_words:
            flat = tuple(entry for pair in pair_word for entry in pair)
            matrix = continued_fraction_matrix(flat)
            trace = matrix[0] + matrix[3]
            determinant = matrix[0] * matrix[3] - matrix[1] * matrix[2]
            delta = trace * trace - 4
            record_failure("determinant_one", determinant != 1)
            record_failure("trace_at_least_three", trace < 3)
            record_failure(
                "order_discriminant_factorization",
                delta != (trace - 2) * (trace + 2),
            )
            record_failure(
                "nonsquare_interval", not ((trace - 1) ** 2 < delta < trace * trace)
            )
            record_failure(
                "order_discriminant_nonsquare", math.isqrt(delta) ** 2 == delta
            )
            record_failure(
                "clock_strict_inequality_certificate",
                not (delta > (trace - 2) ** 2 and (trace - 1) ** 2 > trace),
            )
            q_previous, q_current = 2, trace
            for exponent in range(2, 7):
                q_next = trace * q_current - q_previous
                powered = power2(matrix, exponent)
                record_failure(
                    "trace_power_recurrence",
                    powered[0] + powered[3] != q_next,
                )
                q_previous, q_current = q_current, q_next
            squared = power2(matrix, 2)
            record_failure(
                "trace_square_mismatch",
                squared[0] + squared[3] == trace * trace,
            )
            trace_groups[trace] = trace_groups.get(trace, 0) + 1
            trace_prime += int(primality_trial_six(trace))
            is_delta_prime = primality_trial_six(delta)
            delta_prime += int(is_delta_prime)
            delta_nonboundary_prime += int(is_delta_prime and (trace, delta) != (3, 5))
            reverse = rotate_min(pair_reverse(pair_word))
            own_id = orientation_id(pair_word)
            reverse_id = orientation_id(reverse)
            rows.append(
                {
                    "delta_order": delta,
                    "determinant": determinant,
                    "matrix": list(matrix),
                    "pair_length": length,
                    "trace": trace,
                    "word": [[a, b] for a, b in pair_word],
                    "orientation_id": own_id,
                    "reverse_orientation_id": reverse_id,
                    "reversal_orbit_id": min(own_id, reverse_id),
                    "self_reversal": own_id == reverse_id,
                    "reverse_class_present": reverse_id in orientation_ids,
                    "source_multiplicity": 1,
                    "untwisted_sign": 1,
                    "phase_exponent_mod_97": 0,
                    "expanding_eigenvalue_minpoly": [1, -trace, 1],
                    "geodesic_norm_minpoly": [1, -(trace * trace - 2), 1],
                    "derivative_multiplier_minpoly": [1, -(trace * trace - 2), 1],
                    "norm_qsqrt_coefficients": [
                        [trace * trace - 2, 2],
                        [trace, 2],
                    ],
                    "derivative_qsqrt_coefficients": [
                        [trace * trace - 2, 2],
                        [-trace, 2],
                    ],
                    "marker_exponent_per_repetition": 2 * length,
                }
            )

    rows.sort(key=lambda row: (row["pair_length"], row["word"], row["matrix"]))
    encoded = json.dumps(
        rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    collision_sizes = [amount for amount in trace_groups.values() if amount > 1]
    return {
        "alphabet_label": label,
        "digits": list(digits),
        "pair_alphabet_size": len(pairs),
        "primitive_pair_necklaces_by_length": by_length,
        "primitive_pair_necklaces_total": len(rows),
        "theorem_failures": dict(sorted(failures.items())),
        "trace_prime_orbit_count": trace_prime,
        "trace_composite_orbit_count": len(rows) - trace_prime,
        "order_discriminant_prime_orbit_count": delta_prime,
        "order_discriminant_prime_nonboundary_count": delta_nonboundary_prime,
        "trace_collision_group_count": len(collision_sizes),
        "trace_collision_orbit_excess": sum(amount - 1 for amount in collision_sizes),
        "scientific_rows_sha256": hashlib.sha256(encoded).hexdigest(),
    }


def primitive_word(word: tuple[object, ...]) -> bool:
    return all(
        len(word) % period != 0
        or word != word[:period] * (len(word) // period)
        for period in range(1, len(word))
    )


def independent_witness(
    word: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    flat = tuple(digit for pair in word for digit in pair)
    matrix = continued_fraction_matrix(flat)
    trace = matrix[0] + matrix[3]
    canonical = rotate_min(word)
    reverse = rotate_min(pair_reverse(word))
    return {
        "word": [[left, right] for left, right in word],
        "flattened": list(flat),
        "primitive_pair_necklace": primitive_word(word),
        "canonical_pair_rotation": word == canonical,
        "orientation_id": orientation_id(canonical),
        "reverse_orientation_id": orientation_id(reverse),
        "digit_reversal_related_to_self": canonical == reverse,
        "matrix": list(matrix),
        "trace": trace,
        "determinant": matrix[0] * matrix[3] - matrix[1] * matrix[2],
        "delta_order": trace * trace - 4,
    }


def independent_collision(
    left: tuple[tuple[int, int], ...], right: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    left_record = independent_witness(left)
    right_record = independent_witness(right)
    reversal = rotate_min(pair_reverse(left)) == rotate_min(right)
    return {
        "left": left_record,
        "right": right_record,
        "digit_reversal_related": reversal,
        "cross_pair_length": len(left) != len(right),
        "exact": (
            left_record["primitive_pair_necklace"]
            and right_record["primitive_pair_necklace"]
            and left_record["trace"] == right_record["trace"]
            and left_record["determinant"] == right_record["determinant"] == 1
            and left_record["delta_order"] == right_record["delta_order"]
            and left_record["orientation_id"] != right_record["orientation_id"]
        ),
    }


def independent_splitting() -> dict[str, object]:
    digit_counts = {
        length: sum(1 for _ in aperiodic_necklace_indices(2, length))
        for length in range(1, 7)
    }
    pair_counts = {
        length: sum(1 for _ in aperiodic_necklace_indices(4, length))
        for length in range(1, 4)
    }
    predicted = {
        length: 2 * digit_counts[2 * length]
        + (digit_counts[length] if length % 2 else 0)
        for length in range(1, 4)
    }
    trace4 = (
        independent_witness(((1, 2),))["trace"]
        == independent_witness(((2, 1),))["trace"]
        == 4
        and rotate_min(pair_reverse(((1, 2),))) == ((2, 1),)
    )
    flattened_22 = primitive_word(((2, 2),)) and not primitive_word((2, 2))
    return {
        "digit_counts_1_to_6": {str(key): value for key, value in digit_counts.items()},
        "pair_counts_1_to_3": {str(key): value for key, value in pair_counts.items()},
        "predicted_pair_counts": {str(key): value for key, value in predicted.items()},
        "trace4_two_rho_phases": trace4,
        "flattened_22_pair_primitive_sigma_imprimitive": flattened_22,
        "pass": pair_counts == predicted == {1: 4, 2: 6, 3: 20}
        and trace4
        and flattened_22,
    }


def independent_return_map() -> dict[str, object]:
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
    reversed_class = rotate_min(pair_reverse(word))
    flattened_word = tuple(digit for pair in word for digit in pair)
    raw_reversal_matches = group(tuple(reversed(flattened_word))) == pair_reverse(word)
    rotations = tuple(word[index:] + word[:index] for index in range(len(word)))
    reversal_descends = all(
        rotate_min(pair_reverse(rotation)) == reversed_class
        for rotation in rotations
    )
    primitive_preserved = primitive_word(word) == primitive_word(pair_reverse(word))
    block_mutation = rotate_min(tuple(reversed(word))) != reversed_class
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


def multiply2(
    left: tuple[int, int, int, int], right: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    return (
        left[0] * right[0] + left[1] * right[2],
        left[0] * right[1] + left[1] * right[3],
        left[2] * right[0] + left[3] * right[2],
        left[2] * right[1] + left[3] * right[3],
    )


def power2(
    matrix: tuple[int, int, int, int], exponent: int
) -> tuple[int, int, int, int]:
    answer = (1, 0, 0, 1)
    for _ in range(exponent):
        answer = multiply2(answer, matrix)
    return answer


def branch_matrix(digits: tuple[int, ...]) -> tuple[int, int, int, int]:
    matrix = (1, 0, 0, 1)
    for digit in digits:
        matrix = multiply2(matrix, (0, 1, 1, digit))
    return matrix


def raw_nested(
    raw: tuple[int, ...], value: Fraction
) -> tuple[Fraction, Fraction]:
    point = value
    weight = Fraction(1)
    for digit in raw:
        weight /= (digit + point) ** 2
        point = 1 / (digit + point)
    return point, weight


def independent_branch_order() -> dict[str, object]:
    stored = (1, 2, 2, 3, 1, 4)
    raw = tuple(reversed(stored))
    matrix = branch_matrix(stored)
    value, weight = raw_nested(raw, Fraction(1, 4))
    wrong_value, wrong_weight = raw_nested(stored, Fraction(1, 4))
    return {
        "stored_digits": list(stored),
        "raw_indices": list(raw),
        "stored_matrix_B": list(matrix),
        "branch_value": [value.numerator, value.denominator],
        "weight_s1": [weight.numerator, weight.denominator],
        "same_index_wrong_value": [wrong_value.numerator, wrong_value.denominator],
        "same_index_wrong_weight": [wrong_weight.numerator, wrong_weight.denominator],
        "pass": matrix == (22, 105, 31, 148)
        and (value, weight) == (Fraction(442, 623), Fraction(16, 388129))
        and (wrong_value, wrong_weight)
        == (Fraction(146, 697), Fraction(16, 485809)),
    }


def independent_control_lock() -> dict[str, object]:
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
        relative: hashlib.sha256((HERE / relative).read_bytes()).hexdigest()
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


def replay(result_path: Path) -> dict[str, object]:
    archived_bytes = result_path.read_bytes()
    archived = json.loads(archived_bytes)
    produced = []
    for prefix, start in (("canonical", 1), ("neighboring", 2)):
        for width in (2, 3, 4):
            produced.append(
                independent_run(
                    tuple(range(start, start + width)), f"{prefix}_D{width}"
                )
            )
    expected_runs = archived["canonical_runs"] + archived["neighboring_runs"]
    comparisons = [
        actual == reference
        for actual, reference in zip(produced, expected_runs, strict=True)
    ]
    order_boundary = independent_witness(((1, 1),))
    composite_trace = independent_witness(((1, 2),))
    trace4 = independent_collision(((1, 2),), ((2, 1),))
    trace6 = independent_collision(((1, 4),), ((2, 2),))
    trace10 = independent_collision(((2, 4),), ((1, 1), (1, 2)))
    all_collisions = (
        trace4["exact"]
        and trace4["digit_reversal_related"]
        and trace6["exact"]
        and not trace6["digit_reversal_related"]
        and trace10["exact"]
        and not trace10["digit_reversal_related"]
        and trace10["cross_pair_length"]
    )
    odd_matrix = continued_fraction_matrix((3,))
    odd_trace = odd_matrix[0] + odd_matrix[3]
    expected_witnesses = {
        "order_discriminant_boundary": order_boundary,
        "composite_trace": composite_trace,
        "trace4_reversal_collision": trace4,
        "trace6_nonreversal_collision": trace6,
        "trace10_cross_length_nonreversal_collision": trace10,
        "all_three_collision_classes_exact": all_collisions,
        "odd_parity_boundary": {
            "word": [3],
            "matrix": list(odd_matrix),
            "determinant": odd_matrix[0] * odd_matrix[3]
            - odd_matrix[1] * odd_matrix[2],
            "trace": odd_trace,
            "characteristic_discriminant": odd_trace * odd_trace + 4,
            "in_theorem_domain": False,
        },
    }
    splitting = independent_splitting()
    return_map = independent_return_map()
    branch = independent_branch_order()
    total_failures = sum(
        sum(run["theorem_failures"].values()) for run in produced
    )
    source_hash_matches = (
        hashlib.sha256((HERE / "SOURCE_LOCK.md").read_bytes()).hexdigest()
        == SOURCE_LOCK_SHA256
    )
    control_lock = independent_control_lock()
    hard_status = (
        "PASS"
        if source_hash_matches
        and control_lock["pass"]
        and all(comparisons)
        and total_failures == 0
        and all_collisions
        and splitting["pass"]
        and return_map["pass"]
        and branch["pass"]
        and order_boundary["trace"] == 3
        and order_boundary["delta_order"] == 5
        and composite_trace["trace"] == 4
        else "FAIL"
    )
    expected_aggregate = {
        "registered_run_count": len(produced),
        "scientific_row_count": sum(
            run["primitive_pair_necklaces_total"] for run in produced
        ),
        "theorem_failure_count": total_failures,
        "order_discriminant_nonboundary_prime_count": sum(
            run["order_discriminant_prime_nonboundary_count"] for run in produced
        ),
        "all_three_collision_classes_exact": all_collisions,
        "primitivity_splitting_exact": splitting["pass"],
        "return_map_typing_exact": return_map["pass"],
        "branch_operator_order_exact": branch["pass"],
        "hard_status": hard_status,
    }
    expected_chronology = (
        "Only the exact M1--M20 corrected input set in CONTROL_LOCK was frozen "
        "before this canonical rerun; v1 and in-flight smoke outputs were known."
    )
    expected_claim = (
        "Bounded exact theorem audit only; not a Mayer determinant "
        "evaluation, novelty proof, or universal Gauss-map no-go."
    )
    checks = {
        "schema": archived.get("schema") == "sd-c42-exact-prototype-v2",
        "candidate": archived.get("candidate_id") == "SD-C42",
        "source_hash_field": archived.get("source_lock_sha256")
        == SOURCE_LOCK_SHA256,
        "source_hash_bytes": source_hash_matches
        and archived.get("source_lock_hash_matches") is True,
        "control_lock": archived.get("control_lock") == control_lock
        and control_lock["pass"],
        "chronology": archived.get("chronology") == expected_chronology,
        "arithmetic_boundary": archived.get("arithmetic") == "exact_integer_only"
        and archived.get("prime_or_zero_table_loaded") is False,
        "all_run_payloads": all(comparisons),
        "witnesses": archived.get("witnesses") == expected_witnesses,
        "primitivity_splitting": archived.get("primitivity_splitting") == splitting,
        "return_map_typing": archived.get("return_map_typing") == return_map,
        "branch_operator_order": archived.get("branch_operator_order") == branch,
        "aggregate": archived.get("aggregate") == expected_aggregate,
        "claim_boundary": archived.get("claim_boundary") == expected_claim,
    }
    report = {
        "schema": "sd-c42-independent-prototype-replay-v2",
        "input_path": result_path.name,
        "input_sha256": hashlib.sha256(archived_bytes).hexdigest(),
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "algorithm": (
            "FKM_aperiodic_necklaces_plus_continuants_plus_direct_raw_transfer"
        ),
        "shared_reference_helpers": False,
        "registered_run_count": len(produced),
        "scientific_row_count": sum(
            run["primitive_pair_necklaces_total"] for run in produced
        ),
        "checks": checks,
        "check_count": len(checks),
        "failure_count": sum(not value for value in checks.values()),
        "all_pass": all(checks.values()),
        "run_matches": {
            run["alphabet_label"]: matches
            for run, matches in zip(produced, comparisons, strict=True)
        },
    }
    return report


def main() -> None:
    result_path = (
        Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "PROTOTYPE_RESULT.json"
    )
    report = replay(result_path)
    print(json.dumps(report, indent=2, sort_keys=True))
    if not report["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
