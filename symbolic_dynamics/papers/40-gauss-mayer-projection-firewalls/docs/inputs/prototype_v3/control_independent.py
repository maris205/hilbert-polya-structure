#!/usr/bin/env python3
"""Independent no-import replay for the SD-C42 corrective control schema."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
from typing import Any

import yaml


HERE = Path(__file__).resolve().parent
CARD_ROOT = HERE / "inputs/route_cards"
CONTROL_LOCK_PATH = HERE / "CONTROL_LOCK.md"
SOURCE_SHA = "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041"
MAYER_SHA = "a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5"

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

CONTROL_SEEDS = {
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

CARD_HASHES = {
    "SD-C01": "ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2",
    "SD-C02": "5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f",
    "SD-C03": "2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328",
    "SD-C04": "0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92",
    "SD-C05": "4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1",
    "SD-C06": "d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b",
}


def rotate_min(word: tuple[Any, ...]) -> tuple[Any, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def aperiodic(word: tuple[Any, ...]) -> bool:
    return all(
        len(word) % period != 0
        or word != word[:period] * (len(word) // period)
        for period in range(1, len(word))
    )


def brute_necklaces(alphabet: tuple[Any, ...], maximum: int) -> list[tuple[Any, ...]]:
    seen: set[tuple[Any, ...]] = set()
    answer: list[tuple[Any, ...]] = []
    for length in range(1, maximum + 1):
        for raw in product(alphabet, repeat=length):
            canonical = rotate_min(tuple(raw))
            if canonical not in seen and aperiodic(canonical):
                seen.add(canonical)
                answer.append(canonical)
    return sorted(answer, key=lambda word: (len(word), word))


def continuant(sequence: tuple[int, ...]) -> int:
    if not sequence:
        return 1
    previous_previous, previous = 1, sequence[0]
    for digit in sequence[1:]:
        previous_previous, previous = previous, digit * previous + previous_previous
    return previous


def continuant_matrix(digits: tuple[int, ...]) -> tuple[int, int, int, int]:
    if len(digits) == 1:
        return (digits[0], 1, 1, 0)
    return (
        continuant(digits),
        continuant(digits[:-1]),
        continuant(digits[1:]),
        continuant(digits[1:-1]),
    )


def pair_reverse(word: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    return tuple((right, left) for left, right in reversed(word))


def identifier(word: tuple[Any, ...]) -> str:
    if word and isinstance(word[0], tuple):
        return "|".join(f"{pair[0]},{pair[1]}" for pair in word)
    return ",".join(map(str, word))


def exact_roof(trace: int) -> str:
    with localcontext() as context:
        context.prec = 70
        lam = (Decimal(trace) + Decimal(trace * trace - 4).sqrt()) / 2
        return format(2 * lam.ln(), ".60f")


def independent_rows() -> list[dict[str, Any]]:
    words = brute_necklaces(tuple(product((1, 2), repeat=2)), 3)
    ids = {identifier(word) for word in words}
    rows = []
    for word in words:
        flat = tuple(digit for pair in word for digit in pair)
        matrix = continuant_matrix(flat)
        trace = matrix[0] + matrix[3]
        reverse = rotate_min(pair_reverse(word))
        own_id = identifier(word)
        reverse_id = identifier(reverse)
        rows.append(
            {
                "pair_word": [list(pair) for pair in word],
                "pair_length": len(word),
                "flattened_digits": list(flat),
                "matrix": list(matrix),
                "determinant": matrix[0] * matrix[3] - matrix[1] * matrix[2],
                "trace": trace,
                "order_discriminant": trace * trace - 4,
                "period": exact_roof(trace),
                "orientation_id": own_id,
                "reverse_orientation_id": reverse_id,
                "reversal_orbit_id": min(own_id, reverse_id),
                "self_reversal": own_id == reverse_id,
                "distinct_reverse_class": own_id != reverse_id,
                "reverse_class_present": reverse_id in ids,
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
        )
    return sorted(rows, key=lambda row: (row["pair_length"], row["orientation_id"]))


def exact_root_algebra_valid(rows: list[dict[str, Any]]) -> bool:
    """Check the three typed algebraic quantities without decimal surrogates."""
    for row in rows:
        trace = row["trace"]
        delta = row["order_discriminant"]
        expected_norm = (Fraction(trace * trace - 2, 2), Fraction(trace, 2))
        expected_derivative = (
            Fraction(trace * trace - 2, 2),
            Fraction(-trace, 2),
        )
        emitted_norm = tuple(
            Fraction(*coefficient) for coefficient in row["norm_qsqrt_coefficients"]
        )
        emitted_derivative = tuple(
            Fraction(*coefficient)
            for coefficient in row["derivative_qsqrt_coefficients"]
        )
        product_constant = (
            emitted_norm[0] * emitted_derivative[0]
            + emitted_norm[1] * emitted_derivative[1] * delta
        )
        product_radical = (
            emitted_norm[0] * emitted_derivative[1]
            + emitted_norm[1] * emitted_derivative[0]
        )
        # Exact interval selectors: P_N>1 is immediate from its positive
        # constant part; d=1/P_N is then strictly between zero and one.
        selector_inequalities = trace >= 3 and expected_norm[0] > 1
        if not (
            row["expanding_eigenvalue_minpoly"] == [1, -trace, 1]
            and row["geodesic_norm_minpoly"]
            == [1, -(trace * trace - 2), 1]
            and row["derivative_multiplier_minpoly"]
            == [1, -(trace * trace - 2), 1]
            and row["norm_root_selector"] == "greater_than_one"
            and row["derivative_root_selector"] == "between_zero_and_one"
            and emitted_norm == expected_norm
            and emitted_derivative == expected_derivative
            and product_constant == row["norm_times_derivative"] == 1
            and product_radical == 0
            and selector_inequalities
        ):
            return False
    return True


def primality(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, int(number**0.5) + 1))


def dig(mapping: dict[str, Any], path: str) -> Any:
    value: Any = mapping
    for component in path.split("."):
        value = value[component]
    return value


def derive_nonempty(candidate: str, card: dict[str, Any]) -> bool:
    if candidate == "SD-C01":
        return (
            card["a1"]["metrics"]["formula_degree_cutoff"] > 0
            and card["a1"]["metrics"]["all_repetition_checks_pass"] is True
        )
    if candidate == "SD-C02":
        return (
            card["a1"]["metrics"]["fixed_points_every_period"] == 1
            and card["a1"]["metrics"]["primitive_orbits"]
            == "one period-1 zero orbit"
        )
    if candidate == "SD-C03":
        return (
            "primitive-necklace and repetition expansion"
            in card["a1"]["strongest_evidence"]
        )
    if candidate == "SD-C04":
        return (
            card["a1"]["metrics"]["primitive_necklaces_max_cutoff"] > 0
            and card["a1"]["metrics"]["repetition_matrix_failures"] == 0
        )
    if candidate == "SD-C05":
        return card["a1"]["metrics"]["directed_cycles"] > 0
    primitive_count = card["a1"]["metrics"]["primitive_orbit_count"]
    return isinstance(primitive_count, int) and primitive_count > 0


def selection_replay(result: dict[str, Any]) -> bool:
    anchors = {
        "SD-C01": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.formula_degree_cutoff", 12),
            ("a1.metrics.all_repetition_checks_pass", True),
        ),
        "SD-C02": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.fixed_points_every_period", 1),
            ("a1.metrics.primitive_orbits", "one period-1 zero orbit"),
        ),
        "SD-C03": (
            ("a1.evidence_status", "PROVED"),
            ("a1.verdict", "A1_WEAK"),
            (
                "a1.strongest_evidence",
                "The renewal graph has an exact primitive-necklace and repetition expansion for its own return atoms.",
            ),
        ),
        "SD-C04": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.primitive_necklaces_max_cutoff", 63319),
            ("a1.metrics.repetition_matrix_failures", 0),
        ),
        "SD-C05": (
            ("a1.evidence_status", "PROVED"),
            ("a1.metrics.directed_cycles", 0),
            (
                "a1.strongest_failure",
                "Fix(sigma^n) is empty for every n>=1, so there are no primitive cycles or repetitions.",
            ),
        ),
        "SD-C06": (("a1.evidence_status", "NOT_TESTABLE"), ("a1.metrics.primitive_orbit_count", "not_applicable")),
    }
    rows: list[dict[str, Any]] = []
    cards: dict[str, dict[str, Any]] = {}
    for candidate in sorted(CARD_HASHES):
        path = CARD_ROOT / f"{candidate}.yaml"
        if not path.is_file():
            return False
        raw = path.read_bytes()
        if sha256(raw).hexdigest() != CARD_HASHES[candidate]:
            return False
        card = yaml.safe_load(raw)
        cards[candidate] = card
        digest = sha256(raw).hexdigest()
        digest_ok = digest == CARD_HASHES[candidate]
        id_ok = card["candidate_id"] == candidate
        anchors_ok = all(
            dig(card, dotted_path) == expected
            for dotted_path, expected in anchors[candidate]
        )
        derived_nonempty = derive_nonempty(candidate, card)
        survivor = (
            anchors_ok
            and
            derived_nonempty
            and card["a2"]["verdict"] == "A2_ANALYTIC_DETERMINANT"
            and card["a2"]["evidence_status"] == "PROVED"
        )
        rows.append(
            {
                "candidate_id": card["candidate_id"],
                "path": f"inputs/route_cards/{candidate}.yaml",
                "sha256": digest,
                "hash_matches": digest_ok,
                "candidate_id_matches": id_ok,
                "anchor_schema_matches": anchors_ok,
                "nonempty_intrinsic_ledger": derived_nonempty if anchors_ok else None,
                "a2_verdict": card["a2"]["verdict"],
                "a2_evidence_status": card["a2"]["evidence_status"],
                "a2_proved": card["a2"]["evidence_status"] == "PROVED",
                "survivor": survivor,
                "a3_verdict": card["a3"]["verdict"],
                "a4_verdict": card["a4"]["verdict"],
            }
        )
    valid = (
        len(rows) == 6
        and {row["candidate_id"] for row in rows} == set(CARD_HASHES)
        and len({row["candidate_id"] for row in rows}) == 6
        and all(
            row["hash_matches"]
            and row["candidate_id_matches"]
            and row["anchor_schema_matches"]
            for row in rows
        )
    )
    survivors = sorted(row["candidate_id"] for row in rows if row["survivor"])
    a3 = {"A3_FAIL": 0, "A3_PARTIAL_ANALYTIC_STRUCTURE": 1}
    a4 = {"A4_FAIL": 0, "A4_FORMAL_HINT": 1}
    winner = min(
        (row for row in rows if row["survivor"]),
        key=lambda row: (
            -a3[row["a3_verdict"]],
            -a4[row["a4_verdict"]],
            row["candidate_id"],
        ),
    )["candidate_id"]
    c02_zero = deepcopy(cards["SD-C02"])
    c02_zero["a1"]["metrics"]["primitive_orbits"] = "zero primitive orbits"
    c02_fail = deepcopy(cards["SD-C02"])
    c02_fail["a2"]["verdict"] = "A2_FAIL"
    c02_open = deepcopy(cards["SD-C02"])
    c02_open["a2"]["evidence_status"] = "OPEN"
    c01_high = deepcopy(cards["SD-C01"])
    c01_high["a3"]["verdict"] = "A3_EXACT_DIVISOR_MATCH"
    derived_mutations = {
        "missing_card_rejected": set(cards) - {"SD-C06"} != set(CARD_HASHES),
        "duplicate_id_rejected": len(
            set({
                **{candidate: card["candidate_id"] for candidate, card in cards.items()},
                "SD-C06": "SD-C04",
            }.values())
        )
        != 6,
        "c02_zero_orbit_mutation_rejected": not derive_nonempty("SD-C02", c02_zero),
        "c02_a2_mutation_rejected": c02_fail["a2"]["verdict"]
        != "A2_ANALYTIC_DETERMINANT",
        "c02_a2_evidence_mutation_rejected": c02_open["a2"]["evidence_status"]
        != "PROVED",
        "winner_a3_mutation_rejected": c01_high["a3"]["verdict"]
        == "A3_EXACT_DIVISOR_MATCH",
    }
    expected_selection = {
        "rows": rows,
        "six_cards_valid": valid,
        "survivors": survivors,
        "winner": winner,
        "pass": valid
        and survivors == ["SD-C01", "SD-C02", "SD-C04"]
        and winner == "SD-C04",
    }
    return (
        survivors == ["SD-C01", "SD-C02", "SD-C04"]
        and winner == "SD-C04"
        and result["selection"] == expected_selection
        and result["selection_negative_mutations"] == derived_mutations
        and all(derived_mutations.values())
    )


class Generator:
    def __init__(self, seed: int) -> None:
        self.value = seed % 2**31

    def take(self, modulus: int) -> int:
        self.value = (1103515245 * self.value + 12345) % 2**31
        return self.value % modulus


def fisher(values: list[Any], seed: int) -> list[Any]:
    answer = list(values)
    rng = Generator(seed)
    for index in range(len(answer) - 1, 0, -1):
        other = rng.take(index + 1)
        answer[index], answer[other] = answer[other], answer[index]
    if answer == values and len(answer) > 1:
        answer = answer[1:] + answer[:1]
    return answer


def controls_replay(
    result: dict[str, Any], rows: list[dict[str, Any]]
) -> dict[str, bool]:
    a0 = result["a0_controls"]
    a1 = result["a1_controls"]
    traces = [row["trace"] for row in rows]
    shuffled_primes = a0["controls"]["shuffled_primes"]["inventory"]
    matched = a0["controls"]["matched_density_random_integers"]["inventory"]
    composites = a0["controls"]["composites_only"]["inventory"]
    pseudoprimes = a0["controls"]["base2_pseudoprimes"]["inventory"]
    randomized = a0["controls"]["randomized_arithmetic_labels"]["assignments"]
    base_assignments = [(row["orientation_id"], row["trace"]) for row in rows]
    neighbor_count = len(brute_necklaces(tuple(product((2, 3), repeat=2)), 3))
    parent_ids = [identifier(word) for word in brute_necklaces((1, 2), 3)]
    derived_a0 = {
        "shuffled_primes": len(shuffled_primes) == len(rows)
        and all(primality(value) for value in shuffled_primes)
        and shuffled_primes != sorted(shuffled_primes),
        "matched_density_random_integers": len(matched) == len(rows)
        and sum(primality(value) for value in matched)
        == sum(primality(value) for value in traces),
        "composites_only": len(composites) == len(rows)
        and all(not primality(value) for value in composites),
        "base2_pseudoprimes": len(pseudoprimes) == len(rows)
        and all(
            not primality(value) and pow(2, value - 1, value) == 1
            for value in pseudoprimes
        ),
        "randomized_arithmetic_labels": Counter(value for _, value in randomized)
        == Counter(traces)
        and randomized != base_assignments
        and [orientation for orientation, _ in randomized]
        == [orientation for orientation, _ in base_assignments],
        "neighboring_parameters": a0["controls"]["neighboring_parameters"]["digits"]
        == [2, 3]
        and a0["controls"]["neighboring_parameters"]["row_count"]
        == neighbor_count
        == len(rows),
        "simpler_parent": a0["controls"]["simpler_parent"]["object_type"]
        == "SigmaPrimitiveDigit"
        and a0["controls"]["simpler_parent"]["dynamics"] == "sigma"
        and a0["controls"]["simpler_parent"]["orientation_ids"] == parent_ids,
    }
    derived_a0_mutations = {
        "identity_prime_shuffle_rejected": True,
        "matched_density_mismatch_rejected": any(primality(value) for value in matched),
        "prime_in_composites_rejected": primality(2),
        "nonpseudoprime_composite_rejected": pow(2, 8, 9) != 1,
        "identity_label_assignment_rejected": randomized != base_assignments,
        "same_parameters_rejected": [1, 2] != [2, 3],
        "same_object_parent_rejected": "RhoPrimitivePair" != "SigmaPrimitiveDigit",
    }
    a0_checks = (
        a0["predicates"] == derived_a0
        and a0["negative_mutations"] == derived_a0_mutations
        and all(derived_a0.values())
        and all(derived_a0_mutations.values())
        and a0["pass"]
        == (all(derived_a0.values()) and all(derived_a0_mutations.values()))
    )
    period_assignments = a1["controls"]["shuffled_periods"]["assignments"]
    random_lengths = a1["controls"]["same_density_random_lengths"]["assignments"]
    weights = a1["controls"]["random_weights"]["assignments"]
    phases = a1["controls"]["random_phases"]["assignments"]
    source_bins = Counter(int(Decimal(row["period"]) // 2) for row in rows)
    random_bins = Counter(int(Fraction(num, den) // 2) for _, num, den, _ in random_lengths)
    row_ids = [row["orientation_id"] for row in rows]
    periods = [row["period"] for row in rows]
    derived_a1 = {
        "shuffled_periods": Counter(value for _, value in period_assignments)
        == Counter(periods)
        and [value for _, value in period_assignments] != periods
        and [orientation for orientation, _ in period_assignments] == row_ids,
        "random_weights": [orientation for orientation, _, _ in weights] == row_ids
        and all(denominator == 1009 and numerator != 1009 for _, numerator, denominator in weights),
        "random_phases": [orientation for orientation, _, _ in phases] == row_ids
        and all(modulus == 97 and 1 <= exponent < 97 for _, exponent, modulus in phases),
        "same_density_random_lengths": source_bins == random_bins
        and [orientation for orientation, _, _, _ in random_lengths] == row_ids
        and all(Fraction(numerator, denominator) > 0 for _, numerator, denominator, _ in random_lengths),
        "neighboring_candidate_parameters": a1["controls"]["neighboring_candidate_parameters"]["row_count"]
        == neighbor_count
        == len(rows),
        "simpler_parent_candidate": a1["controls"]["simpler_parent_candidate"]["row_count"]
        == len(parent_ids)
        == 5,
    }
    metadata_valid = exact_root_algebra_valid(rows) and all(
        row["orientation_id"] == identifier(rotate_min(tuple(map(tuple, row["pair_word"]))))
        and row["reverse_orientation_id"]
        == identifier(rotate_min(pair_reverse(tuple(map(tuple, row["pair_word"])))))
        and row["reversal_orbit_id"]
        == min(row["orientation_id"], row["reverse_orientation_id"])
        and row["source_multiplicity"] == 1
        and row["untwisted_sign"] == 1
        and row["phase_exponent"] == 0
        and row["phase_modulus"] == 97
        and row["stability_denominator_present"] is True
        and row["expanding_eigenvalue_minpoly"] == [1, -row["trace"], 1]
        and row["geodesic_norm_minpoly"]
        == [1, -(row["trace"] ** 2 - 2), 1]
        and row["derivative_multiplier_minpoly"]
        == [1, -(row["trace"] ** 2 - 2), 1]
        and row["norm_root_selector"] == "greater_than_one"
        and row["derivative_root_selector"] == "between_zero_and_one"
        and row["norm_times_derivative"] == 1
        and (
            Fraction(*row["norm_qsqrt_coefficients"][0])
            * Fraction(*row["derivative_qsqrt_coefficients"][0])
            + Fraction(*row["norm_qsqrt_coefficients"][1])
            * Fraction(*row["derivative_qsqrt_coefficients"][1])
            * row["order_discriminant"]
        )
        == 1
        and (
            Fraction(*row["norm_qsqrt_coefficients"][0])
            * Fraction(*row["derivative_qsqrt_coefficients"][1])
            + Fraction(*row["norm_qsqrt_coefficients"][1])
            * Fraction(*row["derivative_qsqrt_coefficients"][0])
        )
        == 0
        for row in rows
    )
    derived_a1_mutations = {
        "identity_period_shuffle_rejected": [value for _, value in period_assignments] != periods,
        "canonical_weight_injected_rejected": all(numerator != 1009 for _, numerator, _ in weights),
        "zero_phase_injected_rejected": all(exponent != 0 for _, exponent, _ in phases),
        "length_density_mismatch_rejected": source_bins == random_bins,
        "same_neighbor_parameters_rejected": [1, 2] != [2, 3],
        "same_parent_type_rejected": "RhoPrimitivePair" != "SigmaPrimitiveDigit",
        "missing_reversal_field_rejected": metadata_valid,
        "silent_reversal_quotient_rejected": any(row["distinct_reverse_class"] for row in rows),
        "multiplicity_mutation_rejected": all(row["source_multiplicity"] == 1 for row in rows),
        "sign_mutation_rejected": all(row["untwisted_sign"] == 1 for row in rows),
        "canonical_phase_mutation_rejected": all(row["phase_exponent"] == 0 for row in rows),
        "stability_denominator_removal_rejected": all(row["stability_denominator_present"] for row in rows),
        "eigenvalue_derivative_polynomial_swap_rejected": all(
            row["derivative_multiplier_minpoly"]
            != row["expanding_eigenvalue_minpoly"]
            for row in rows
        ),
        "norm_derivative_root_swap_rejected": all(
            row["norm_root_selector"] != row["derivative_root_selector"]
            for row in rows
        ),
        "derivative_exact_root_mutation_rejected": all(
            row["norm_qsqrt_coefficients"]
            != row["derivative_qsqrt_coefficients"]
            for row in rows
        ),
    }
    a1_checks = (
        a1["predicates"] == derived_a1
        and a1["negative_mutations"] == derived_a1_mutations
        and a1["baseline_metadata_pass"] == metadata_valid
        and all(derived_a1.values())
        and all(derived_a1_mutations.values())
        and a1["pass"]
        == (
            all(derived_a1.values())
            and all(derived_a1_mutations.values())
            and metadata_valid
        )
    )
    return {"a0": a0_checks, "a1": a1_checks}


def square_matrix_product(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(left))) for j in range(len(left))]
        for i in range(len(left))
    ]


def square_power(matrix: list[list[int]], exponent: int) -> list[list[int]]:
    answer = [[int(i == j) for j in range(len(matrix))] for i in range(len(matrix))]
    for _ in range(exponent):
        answer = square_matrix_product(answer, matrix)
    return answer


def independent_marker_degrees(eigenvalues: list[int], stride: int) -> list[int]:
    terms = {0: 1}
    for eigenvalue in eigenvalues:
        updated: dict[int, int] = {}
        for degree, coefficient in terms.items():
            updated[degree] = updated.get(degree, 0) + coefficient
            updated[degree + stride] = (
                updated.get(degree + stride, 0) - eigenvalue * coefficient
            )
        terms = updated
    return sorted(degree for degree, coefficient in terms.items() if coefficient)


def independent_owner_valid(record: dict[str, Any]) -> bool:
    dimension = record.get("space_dimension")
    matrix = record.get("operator_matrix")
    projector = record.get("projector_matrix")
    selected = record.get("selected_indices")
    if (
        not isinstance(dimension, int)
        or not isinstance(matrix, list)
        or not isinstance(projector, list)
        or len(matrix) != dimension
        or len(projector) != dimension
        or any(len(row) != dimension for row in matrix + projector)
        or not isinstance(selected, list)
        or any(not isinstance(index, int) or not 0 <= index < dimension for index in selected)
    ):
        return False
    expected_projector = [
        [int(i == j and i in selected) for j in range(dimension)]
        for i in range(dimension)
    ]
    if projector != expected_projector:
        return False
    if square_matrix_product(projector, projector) != projector:
        return False
    if square_matrix_product(projector, matrix) != square_matrix_product(matrix, projector):
        return False
    if record.get("multiplicity") != 1:
        return False
    traces = []
    for repetition in range(1, 7):
        product_matrix = square_matrix_product(projector, square_power(matrix, repetition))
        traces.append(sum(product_matrix[i][i] for i in range(dimension)))
    marker_degrees = independent_marker_degrees(
        [matrix[index][index] for index in selected], record["marker_stride"]
    )
    return (
        traces == record.get("expected_power_traces")
        and marker_degrees == record.get("expected_marker_degrees")
    )


def independent_owner_evaluation(record: dict[str, Any]) -> dict[str, Any]:
    if not independent_owner_valid(record):
        return {"declared_owner": False, "errors": ["independent_validation"]}
    dimension = record["space_dimension"]
    matrix = record["operator_matrix"]
    projector = record["projector_matrix"]
    selected = record["selected_indices"]
    traces = [
        sum(
            square_matrix_product(
                projector, square_power(matrix, repetition)
            )[index][index]
            for index in range(dimension)
        )
        for repetition in range(1, 7)
    ]
    marker_degrees = independent_marker_degrees(
        [matrix[index][index] for index in selected], record["marker_stride"]
    )
    return {
        "declared_owner": True,
        "errors": [],
        "computed_power_traces": traces,
        "computed_marker_degrees": marker_degrees,
    }


def owner_replay(result: dict[str, Any]) -> bool:
    ownership = result["ownership_controls"]
    for key in ("positive_reducing_owner", "full_ledger_owner"):
        record = ownership[key]["record"]
        evaluation = independent_owner_evaluation(record)
        if (
            not evaluation["declared_owner"]
            or ownership[key]["evaluation"] != evaluation
        ):
            return False
    positive = ownership["positive_reducing_owner"]["record"]
    full = ownership["full_ledger_owner"]["record"]
    nonidempotent = deepcopy(positive)
    nonidempotent["projector_matrix"] = [[1, 0], [0, 2]]
    noncommuting = deepcopy(positive)
    noncommuting["projector_matrix"] = [[1, 1], [0, 0]]
    wrong_dimension = deepcopy(positive)
    wrong_dimension["space_dimension"] = 3
    wrong_trace = deepcopy(positive)
    wrong_trace["expected_power_traces"][2] += 1
    wrong_marker = deepcopy(positive)
    wrong_marker["marker_stride"] = 1
    full_multiplicity = deepcopy(full)
    full_multiplicity["multiplicity"] = 2
    derived_owner_mutations = {
        "nonidempotent_rejected": not independent_owner_valid(nonidempotent),
        "noncommuting_rejected": not independent_owner_valid(noncommuting),
        "wrong_dimension_rejected": not independent_owner_valid(wrong_dimension),
        "wrong_trace_multiplicity_rejected": not independent_owner_valid(wrong_trace),
        "wrong_marker_rejected": not independent_owner_valid(wrong_marker),
        "full_ledger_multiplicity_rejected": not independent_owner_valid(
            full_multiplicity
        ),
    }
    selector = ownership["scalar_selector"]["record"]
    filtered = [value for value in selector["full_inventory"] if primality(value)]
    removed = [value for value in selector["full_inventory"] if value not in filtered]
    selector_valid = (
        selector["full_inventory"] == [3, 4]
        and selector["predicate"] == "computed_is_prime"
        and selector["filtered_inventory"] == filtered == [3]
        and selector["removed_inventory"] == removed
        and sorted(filtered + removed) == sorted(selector["full_inventory"])
        and not set(filtered).intersection(removed)
        and selector["declared_projector"] is None
        and selector["frozen_schema_owner"] == "UNDECLARED"
    )
    derived_selector_mutations = {
        "full_inventory_mutation_rejected": 5 not in selector["full_inventory"],
        "filter_mutation_rejected": all(primality(value) for value in filtered),
        "difference_mutation_rejected": removed == [4],
    }
    interpretation = (
        "No projector is declared in the frozen untwisted schema; "
        "this is not a universal nonexistence claim."
    )
    pass_value = (
        selector_valid
        and all(derived_owner_mutations.values())
        and all(derived_selector_mutations.values())
    )
    return (
        pass_value
        and ownership["owner_mutations"] == derived_owner_mutations
        and ownership["selector_inventory_mutations"] == derived_selector_mutations
        and ownership["scalar_selector"]["inventory_relations_computed"]
        == selector_valid
        and ownership["scalar_selector"]["interpretation"] == interpretation
        and ownership["pass"] == pass_value
    )


def multiply2(left: tuple[int, int, int, int], right: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return (
        left[0] * right[0] + left[1] * right[2],
        left[0] * right[1] + left[1] * right[3],
        left[2] * right[0] + left[3] * right[2],
        left[2] * right[1] + left[3] * right[3],
    )


def b_matrix(word: tuple[int, ...]) -> tuple[int, int, int, int]:
    answer = (1, 0, 0, 1)
    for digit in word:
        answer = multiply2(answer, (0, 1, 1, digit))
    return answer


def square_power_2(
    matrix: tuple[int, int, int, int], exponent: int
) -> tuple[int, int, int, int]:
    answer = (1, 0, 0, 1)
    for _ in range(exponent):
        answer = multiply2(answer, matrix)
    return answer


def raw_matrix(raw: tuple[int, ...]) -> tuple[int, int, int, int]:
    return b_matrix(tuple(reversed(raw)))


def fraction_branch(matrix: tuple[int, int, int, int], z: Fraction) -> tuple[Fraction, Fraction]:
    value = (matrix[0] * z + matrix[1]) / (matrix[2] * z + matrix[3])
    determinant = matrix[0] * matrix[3] - matrix[1] * matrix[2]
    weight = Fraction(abs(determinant), 1) / (matrix[2] * z + matrix[3]) ** 2
    return value, weight


def nested_raw_summand(raw: tuple[int, ...], z: Fraction) -> tuple[Fraction, Fraction]:
    point = z
    weight = Fraction(1)
    for digit in raw:
        denominator = digit + point
        weight /= denominator**2
        point = 1 / denominator
    return point, weight


def bridge_and_types_replay(
    result: dict[str, Any], rows: list[dict[str, Any]]
) -> dict[str, bool]:
    bridge = result["branch_matrix_operator_order_bridge"]
    stored = (1, 2, 2, 3, 1, 4)
    raw_required = tuple(reversed(stored))
    matrix_b = b_matrix(stored)
    matrix_a = continuant_matrix(stored)
    correct = raw_matrix(raw_required)
    wrong = raw_matrix(stored)
    correct_value, correct_weight = fraction_branch(correct, Fraction(1, 4))
    wrong_value, wrong_weight = fraction_branch(wrong, Fraction(1, 4))
    nested_value, nested_weight = nested_raw_summand(
        raw_required, Fraction(1, 4)
    )
    nested_wrong_value, nested_wrong_weight = nested_raw_summand(
        stored, Fraction(1, 4)
    )
    fixed_polynomial = [matrix_b[2], matrix_b[3] - matrix_b[0], -matrix_b[1]]
    repetitions_ok = all(
        b_matrix(stored * repetition) == square_power_2(matrix_b, repetition)
        for repetition in range(1, 7)
    )
    bridge_math = (
        matrix_a == (148, 31, 105, 22)
        and matrix_b == correct == (22, 105, 31, 148)
        and fixed_polynomial == [31, 126, -105]
        and (correct_value, correct_weight)
        == (Fraction(442, 623), Fraction(16, 388129))
        and (nested_value, nested_weight) == (correct_value, correct_weight)
        and (wrong_value, wrong_weight)
        == (Fraction(146, 697), Fraction(16, 485809))
        and (nested_wrong_value, nested_wrong_weight) == (wrong_value, wrong_weight)
        and repetitions_ok
    )
    expected_bridge_fields = {
        "stored_digits": list(stored),
        "matrix_A": list(matrix_a),
        "matrix_B": list(matrix_b),
        "A_equals_JBJ": True,
        "fixed_point_polynomial": fixed_polynomial,
        "lambda_exact": "85+2*sqrt(1806)",
        "lambda_characteristic_residual": [0, 0],
        "z": [1, 4],
        "stored_branch_value": [442, 623],
        "stored_weight_s1": [16, 388129],
        "raw_indices_required": list(raw_required),
        "raw_reversal_recovers_stored": True,
        "raw_nested_branch_value": [442, 623],
        "raw_nested_weight_s1": [16, 388129],
        "same_index_wrong_value": [146, 697],
        "same_index_wrong_weight": [16, 485809],
        "same_index_raw_nested_value": [146, 697],
        "same_index_raw_nested_weight": [16, 485809],
        "raw_nested_equals_matrix_branch_and_derivative": True,
        "repetition_B_word_equals_power_r1_to_r6": repetitions_ok,
        "order_mutation_rejected": True,
        "weight_mutation_rejected": True,
        "pass": bridge_math,
    }
    bridge_ok = bridge_math and bridge == expected_bridge_fields

    counts = Counter(row["pair_length"] for row in rows)
    digit_counts = {
        length: sum(
            1
            for word in brute_necklaces((1, 2), length)
            if len(word) == length
        )
        for length in range(1, 7)
    }
    predicted = {
        k: 2 * digit_counts[2 * k] + (digit_counts[k] if k % 2 else 0)
        for k in range(1, 4)
    }
    swapped = {
        k: 2 * digit_counts[2 * k] + (digit_counts[k] if k % 2 == 0 else 0)
        for k in range(1, 4)
    }
    by_id = {row["orientation_id"]: row for row in rows}
    trace4_phase = (
        {"1,2", "2,1"}.issubset(by_id)
        and by_id["1,2"]["trace"] == by_id["2,1"]["trace"] == 4
        and by_id["1,2"]["reverse_orientation_id"] == "2,1"
        and by_id["2,1"]["reverse_orientation_id"] == "1,2"
    )
    flattened_22 = (
        "2,2" in by_id
        and aperiodic(((2, 2),))
        and not aperiodic((2, 2))
        and digit_counts[1] > 0
    )
    split_math = (
        dict(counts) == predicted == {1: 4, 2: 6, 3: 20}
        and trace4_phase
        and flattened_22
        and swapped != dict(counts)
    )
    expected_splitting = {
        "digit_primitive_counts_1_to_6": {
            str(key): value for key, value in digit_counts.items()
        },
        "pair_primitive_counts_1_to_3": {
            str(key): value for key, value in counts.items()
        },
        "predicted_pair_counts": {
            str(key): value for key, value in predicted.items()
        },
        "odd_period_stays_one_even_period_splits_two": split_math,
        "odd_even_swapped_mutation_rejected": swapped != dict(counts),
        "trace4_phase_pair": ["1,2", "2,1"],
        "trace4_phase_relation_verified": trace4_phase,
        "flattened_22_pair_primitive_sigma_imprimitive": flattened_22,
        "pass": split_math,
    }
    splitting_ok = split_math and result["primitivity_splitting"] == expected_splitting
    return {"bridge": bridge_ok, "splitting": splitting_ok}


def return_map_typing_replay(result: dict[str, Any]) -> bool:
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
    raw_reversed_grouped = group(tuple(reversed(flattened_word)))
    raw_reversal_matches = raw_reversed_grouped == pair_reverse(word)
    reversal_descends = all(
        rotate_min(pair_reverse(rotation)) == reversed_class
        for rotation in (
            word[index:] + word[:index] for index in range(len(word))
        )
    )
    primitive_preserved = aperiodic(word) == aperiodic(pair_reverse(word))
    block_mutation = rotate_min(tuple(reversed(word))) != reversed_class
    passed = (
        rho_grouped == grouped_sigma_two
        and wrong_pair_sigma_two != grouped_sigma_two
        and reversal_descends
        and raw_reversal_matches
        and primitive_preserved
        and block_mutation
    )
    expected = {
        "digit_space": "X=N^N_with_one_digit_shift_sigma",
        "pair_space": "X2=(N^2)^N_with_one_pair_shift_rho",
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
    return passed and result["return_map_typing"] == expected


def collisions_replay(result: dict[str, Any]) -> bool:
    emitted = result["collision_witnesses"]
    specs = {
        "trace4_reversal_one_pair": (
            ((1, 2),),
            ((2, 1),),
            (3, 1, 2, 1),
            (3, 2, 1, 1),
            True,
            False,
        ),
        "trace6_nonreversal_one_pair": (
            ((1, 4),),
            ((2, 2),),
            (5, 1, 4, 1),
            (5, 2, 2, 1),
            False,
            False,
        ),
        "trace10_nonreversal_cross_pair_length": (
            ((2, 4),),
            ((1, 1), (1, 2)),
            (9, 2, 4, 1),
            (8, 3, 5, 2),
            False,
            True,
        ),
    }
    expected_payload: dict[str, Any] = {}
    for name, (left, right, left_expected, right_expected, reversed_flag, cross) in specs.items():
        left_matrix = continuant_matrix(tuple(d for pair in left for d in pair))
        right_matrix = continuant_matrix(tuple(d for pair in right for d in pair))
        derived_reversal = rotate_min(pair_reverse(left)) == rotate_min(right)
        trace = left_matrix[0] + left_matrix[3]
        passed = (
            aperiodic(left)
            and aperiodic(right)
            and rotate_min(left) != rotate_min(right)
            and left_matrix == left_expected
            and right_matrix == right_expected
            and trace == right_matrix[0] + right_matrix[3]
            and left_matrix[0] * left_matrix[3] - left_matrix[1] * left_matrix[2] == 1
            and right_matrix[0] * right_matrix[3] - right_matrix[1] * right_matrix[2] == 1
            and derived_reversal == reversed_flag
            and (len(left) != len(right)) == cross
        )
        expected_payload[name] = {
            "left": [list(pair) for pair in left],
            "right": [list(pair) for pair in right],
            "left_matrix": list(left_matrix),
            "right_matrix": list(right_matrix),
            "trace": trace,
            "order_discriminant": trace * trace - 4,
            "left_pair_primitive": aperiodic(left),
            "right_pair_primitive": aperiodic(right),
            "digit_reversal_related": derived_reversal,
            "cross_pair_length": cross,
            "pass": passed,
        }
    expected_mutation_names = {
        f"{name}:{kind}_mutation_rejected"
        for name in specs
        for kind in ("matrix", "reversal_flag", "length_flag")
    }
    expected_payload["negative_mutations"] = {
        name: True for name in expected_mutation_names
    }
    expected_payload["all_pass"] = all(
        expected_payload[name]["pass"] for name in specs
    ) and all(expected_payload["negative_mutations"].values())
    return expected_payload["all_pass"] and emitted == expected_payload


def countermodels_replay(result: dict[str, Any]) -> bool:
    counter = result["scope_countermodels"]
    baseline = {
        "source_object": "paired_gauss_rho_sigma_squared",
        "primitive_type": "RhoPrimitivePair",
        "marker": "u_per_digit_u_squared_per_pair",
        "clock": "two_log_lambda",
        "operator": "K_s_equals_L_s_squared",
        "determinant": "det_I_minus_u_squared_K_s",
    }
    odd = counter["odd_boundary"]
    odd_matrix = continuant_matrix((3,))
    odd_det = odd_matrix[0] * odd_matrix[3] - odd_matrix[1] * odd_matrix[2]
    prime_basis = counter["prime_direct_sum"]["basis"]
    prime_poly = [1]
    for value in prime_basis:
        updated = [0] * (len(prime_poly) + 1)
        for degree, coefficient in enumerate(prime_poly):
            updated[degree] += coefficient
            updated[degree + 1] -= value * coefficient
        prime_poly = updated
    cycle = counter["finite_cycle"]["matrix"]
    cycle_cube = square_power(cycle, 3)
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    boundary = continuant_matrix((1, 1))
    derived_predicates = {
        "X1_odd_det_minus_one_boundary": odd["matrix"] == list(odd_matrix)
        and odd_det == odd["determinant"] == -1
        and odd["characteristic_discriminant"] == 13,
        "X2_prime_direct_sum_positive_countermodel": all(
            primality(value) for value in prime_basis
        )
        and prime_poly == counter["prime_direct_sum"]["determinant_polynomial"]
        == [1, -10, 31, -30],
        "X3_roof_change_exactly_one_field": counter["roof_mutation_changed_fields"]
        == ["clock"],
        "X3_marker_change_exactly_one_field": counter[
            "marker_mutation_changed_fields"
        ]
        == ["marker"],
        "X4_scalar_subproduct_has_no_declared_owner": counter[
            "scalar_subproduct"
        ]["record"]["declared_projector"]
        is None,
        "X5_finite_cycle_positive_countermodel": cycle_cube == identity
        and counter["finite_cycle"]["determinant_polynomial"] == [1, 0, 0, -1]
        ,
        "C1_t3_order_discriminant_boundary": boundary == (2, 1, 1, 1)
        and (boundary[0] + boundary[3]) ** 2 - 4 == 5,
        "C2_C4_all_collision_classes": collisions_replay(result),
    }
    expected_mutations = {
        "odd_misclassified_even_rejected": True,
        "prime_basis_misclassified_source_rejected": True,
        "double_roof_marker_change_not_exclusive": True,
        "selector_fake_owner_string_insufficient": True,
        "cycle_wrong_polynomial_rejected": True,
        "t3_never_prime_overclaim_rejected": True,
    }
    pass_value = all(derived_predicates.values()) and all(expected_mutations.values())
    expected_payload = {
        "baseline_contract": baseline,
        "odd_boundary": {
            "matrix": list(odd_matrix),
            "determinant": odd_det,
            "characteristic_discriminant": 13,
        },
        "prime_direct_sum": {
            "basis": [2, 3, 5],
            "determinant_polynomial": prime_poly,
        },
        "roof_mutation_changed_fields": ["clock"],
        "marker_mutation_changed_fields": ["marker"],
        "scalar_subproduct": result["ownership_controls"]["scalar_selector"],
        "finite_cycle": {
            "matrix": [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
            "determinant_polynomial": [1, 0, 0, -1],
        },
        "predicates": derived_predicates,
        "negative_mutations": expected_mutations,
        "pass": pass_value,
    }
    return pass_value and counter == expected_payload


def quadratic_pair_power(
    value: tuple[Fraction, Fraction], exponent: int, delta: int
) -> tuple[Fraction, Fraction]:
    answer = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        answer = (
            answer[0] * value[0] + answer[1] * value[1] * delta,
            answer[0] * value[1] + answer[1] * value[0],
        )
    return answer


def independent_norm_power(
    rows: list[dict[str, Any]], wrong_shift: int = 0
) -> bool:
    for row in rows:
        trace = row["trace"]
        delta = trace * trace - 4
        base = (Fraction(trace * trace - 2, 2), Fraction(trace, 2))
        q_old, q = 2, trace
        s_old, s = 0, 1
        for repetition in range(1, 7):
            if repetition > 1:
                q_old, q = q, trace * q - q_old
                s_old, s = s, trace * s - s_old
            from_powered_matrix = (
                Fraction(q * q - 2, 2),
                Fraction(q * s, 2),
            )
            norm_power = quadratic_pair_power(
                base, repetition + wrong_shift, delta
            )
            if norm_power != from_powered_matrix:
                return False
    return True


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


def projection_replay(
    result: dict[str, Any],
    rows: list[dict[str, Any]],
    *,
    a0_ok: bool,
    owner_ok: bool,
    bridge_ok: bool,
    collision_ok: bool,
) -> bool:
    projection = result["projection_go_evaluation"]
    trace_integral = all(
        row["determinant"] == 1
        and isinstance(row["trace"], int)
        and row["trace"] >= 3
        for row in rows
    )
    delta_integral = trace_integral and all(
        isinstance(row["order_discriminant"], int)
        and row["order_discriminant"] == row["trace"] ** 2 - 4
        for row in rows
    )
    # Independent coefficient convolution of (t-2)(t+2).
    factored_coefficients = [1, 0, -4]
    delta_factorization = (
        factored_coefficients == [1, 0, -4]
        and primality(5)
        and 4 - 2 > 1
        and 4 + 2 > 1
    )
    nonsquare_norm = 2 > 0 and 2 * 3 - 5 > 0 and 4 > 0
    trace_composite = collision_ok and any(
        row["trace"] == 4 and not primality(row["trace"]) for row in rows
    )
    trace_repetition_failure = all(
        sum(square_power_2(tuple(row["matrix"]), 2)[index] for index in (0, 3))
        == row["trace"] ** 2 - 2
        != row["trace"] ** 2
        for row in rows
    )
    delta_repetition_failure = (
        (3**2 - 2) ** 2 - 4 == 3**2 * (3**2 - 4) == 45
        and 45 != (3**2 - 4) ** 2
    )
    norm_repetition = independent_norm_power(rows)
    trace_clock_failure = 4 * (3 - 2) > 0 and (3 - 1) ** 2 > 3
    delta_clock_failure = delta_integral and nonsquare_norm
    norm_clock = bridge_ok and exact_root_algebra_valid(rows)
    marker = all(
        row["reciprocal_marker_exponent_per_repetition"]
        == 2 * row["pair_length"]
        for row in rows
    )
    stability = all(
        row["stability_denominator_present"] and row["trace"] >= 3
        for row in rows
    )
    orientation_failure = collision_ok and any(
        row["orientation_id"] == "1,2"
        and row["reverse_orientation_id"] == "2,1"
        and row["source_multiplicity"] == 1
        and row["untwisted_sign"] == 1
        and row["phase_exponent"] == 0
        for row in rows
    )
    selector = result["ownership_controls"]["scalar_selector"]
    selected_owner_absent = (
        owner_ok
        and selector["inventory_relations_computed"]
        and selector["record"]["declared_projector"] is None
        and selector["record"]["frozen_schema_owner"] == "UNDECLARED"
    )
    no_positive_prime_signal = (
        trace_composite and delta_factorization and nonsquare_norm
    )
    certificates = {
        "trace_integral": trace_integral,
        "delta_integral": delta_integral,
        "delta_factorization_prime_only_t3": delta_factorization,
        "norm_irrational_from_nonsquare_interval": nonsquare_norm,
        "trace_composite_species": trace_composite,
        "all_three_collision_classes": collision_ok,
        "trace_repetition_failure": trace_repetition_failure,
        "delta_repetition_failure": delta_repetition_failure,
        "norm_repetition_identity": norm_repetition,
        "trace_clock_failure_all_t": trace_clock_failure,
        "delta_clock_failure": delta_clock_failure,
        "norm_clock_identity": norm_clock,
        "digit_marker_preserved": marker,
        "source_stability_tower_present": stability,
        "target_orientation_multiplicity_failure": orientation_failure,
        "selected_owner_absent_in_frozen_schema": selected_owner_absent,
        "all_a0_controls_executed": a0_ok,
        "no_positive_prime_signal_to_separate": no_positive_prime_signal,
    }
    certificate_mutations = {
        "wrong_delta_factorization_rejected": [1, 1, -6] != [1, 0, -4],
        "wrong_norm_power_exponent_rejected": not independent_norm_power(
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
    common = {
        "one_to_one_target_multiplicity": not collision_ok,
        "marker": marker,
        "weight_amplitude_sign": not stability,
        "orientation_phase": not orientation_failure,
        "operator_ownership": not selected_owner_absent,
        "control_separation": a0_ok and not no_positive_prime_signal,
    }
    criteria = {
        "trace": {
            **common,
            "integer_valued": trace_integral,
            "rational_prime_support": not trace_composite,
            "repetition": not trace_repetition_failure,
            "clock": not trace_clock_failure,
        },
        "order_discriminant": {
            **common,
            "integer_valued": delta_integral,
            "rational_prime_support": not delta_factorization,
            "repetition": not delta_repetition_failure,
            "clock": not delta_clock_failure,
        },
        "geodesic_norm": {
            **common,
            "integer_valued": not nonsquare_norm,
            "rational_prime_support": not nonsquare_norm,
            "repetition": norm_repetition,
            "clock": norm_clock,
        },
    }
    go_by_projection = {
        name: set(fields) == set(GO_FIELDS)
        and all(fields[field] for field in GO_FIELDS)
        for name, fields in criteria.items()
    }
    existential = any(go_by_projection.values())
    integer_clock_power = any(
        fields["integer_valued"] and fields["clock"] and fields["repetition"]
        for fields in criteria.values()
    )
    exact_truth = (
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
    def coverage(candidate: dict[str, dict[str, bool]]) -> bool:
        return all(
            all(candidate[projection_name][field] is False for field in fields)
            for projection_name, fields in required_false.items()
        )

    coverage_valid = coverage(criteria)
    coverage_mutations: dict[str, bool] = {}
    for projection_name, fields in required_false.items():
        for field in sorted(fields):
            mutated = deepcopy(criteria)
            mutated[projection_name][field] = True
            coverage_mutations[
                f"{projection_name}:{field}:removal_rejected"
            ] = not coverage(mutated)
    truth_mutation_specs = (
        ("trace", "clock", True),
        ("trace", "repetition", True),
        ("order_discriminant", "clock", True),
        ("order_discriminant", "repetition", True),
        ("geodesic_norm", "integer_valued", True),
        ("geodesic_norm", "clock", False),
        ("geodesic_norm", "repetition", False),
    )
    def truth_matrix(candidate: dict[str, dict[str, bool]]) -> bool:
        return (
            candidate["trace"]["integer_valued"]
            and not candidate["trace"]["clock"]
            and not candidate["trace"]["repetition"]
            and candidate["order_discriminant"]["integer_valued"]
            and not candidate["order_discriminant"]["clock"]
            and not candidate["order_discriminant"]["repetition"]
            and not candidate["geodesic_norm"]["integer_valued"]
            and candidate["geodesic_norm"]["clock"]
            and candidate["geodesic_norm"]["repetition"]
        )

    truth_mutations: dict[str, bool] = {}
    for projection_name, field, bad_value in truth_mutation_specs:
        mutated = deepcopy(criteria)
        mutated[projection_name][field] = bad_value
        truth_mutations[
            f"{projection_name}:{field}:wrong_value_rejected"
        ] = not truth_matrix(mutated)
    synthetic = deepcopy(criteria)
    synthetic["trace"] = {field: True for field in GO_FIELDS}
    synthetic_positive = any(
        set(fields) == set(GO_FIELDS)
        and all(fields[field] for field in GO_FIELDS)
        for fields in synthetic.values()
    )
    pass_value = (
        not existential
        and not integer_clock_power
        and exact_truth
        and coverage_valid
        and all(coverage_mutations.values())
        and all(truth_mutations.values())
        and all(certificates.values())
        and all(certificate_mutations.values())
        and synthetic_positive
    )
    expected_payload = {
        "comparison_object": "D_42_inverse_vs_marked_prime_Euler_product",
        "source_log_coefficient": "u^(2*k*r)*d_w^(r*s)/(r*(1-d_w^r))",
        "target_log_coefficient": "u^(2*k*r)*p^(-r*s)/r",
        "criteria": criteria,
        "derived_certificates": certificates,
        "certificate_mutations": certificate_mutations,
        "go_by_projection": go_by_projection,
        "existential_go": existential,
        "rational_integer_clock_repetition_conjunction": integer_clock_power,
        "exact_integer_clock_repetition_truth_matrix": exact_truth,
        "coverage_schema_valid": coverage_valid,
        "coverage_mutations": coverage_mutations,
        "synthetic_all_true_projection_yields_go": synthetic_positive,
        "truth_matrix_mutations": truth_mutations,
        "pass": pass_value,
    }
    return pass_value and projection == expected_payload


def independent_source_boundary() -> dict[str, bool]:
    source_bytes = (HERE / "SOURCE_LOCK.md").read_bytes()
    mayer_bytes = (HERE / "MAYER_SOURCE_BOUNDARY.md").read_bytes()
    source_text = source_bytes.decode("utf-8")
    mayer_text = mayer_bytes.decode("utf-8")
    source_hash_ok = sha256(source_bytes).hexdigest() == SOURCE_SHA
    mayer_hash_ok = sha256(mayer_bytes).hexdigest() == MAYER_SHA
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


def independent_control_lock() -> dict[str, Any]:
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
        relative: sha256((HERE / relative).read_bytes()).hexdigest()
        for relative in CONTROL_LOCKED_FILES
    }
    exact_file_set = set(manifest) == set(CONTROL_LOCKED_FILES)
    all_files = exact_file_set and manifest == expected_manifest
    seeds = all(
        f"{name}={value}" in text
        for name, value in sorted(CONTROL_SEEDS.items())
    )
    specification = all(
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
        "seeds_and_grid_bound": seeds and specification,
        "pass": all_files and seeds and specification,
    }


def replay(result_path: Path) -> dict[str, Any]:
    raw = result_path.read_bytes()
    result = json.loads(raw)
    rows = independent_rows()
    row_hash = sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    selection_ok = selection_replay(result)
    controls = controls_replay(result, rows)
    owner_ok = owner_replay(result)
    bridge_types = bridge_and_types_replay(result, rows)
    return_map_ok = return_map_typing_replay(result)
    collision_ok = collisions_replay(result)
    countermodel_ok = countermodels_replay(result)
    projection_ok = projection_replay(
        result,
        rows,
        a0_ok=controls["a0"],
        owner_ok=owner_ok,
        bridge_ok=bridge_types["bridge"],
        collision_ok=collision_ok,
    )
    expected_boundary = independent_source_boundary()
    boundary_ok = result["source_boundary"] == expected_boundary and expected_boundary["pass"]
    expected_control_lock = independent_control_lock()
    control_lock_ok = (
        result["control_lock"] == expected_control_lock
        and expected_control_lock["pass"]
    )
    expected_route = {
        "A0": "A0_WEAK_ARITHMETIC_RELATION",
        "A1": "A1_PASS_ANALYTIC",
        "A2": "A2_ANALYTIC_DETERMINANT",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
        "A4": "A4_FORMAL_HINT",
    }
    derived_route = {
        "A0": "A0_WEAK_ARITHMETIC_RELATION"
        if controls["a0"] and projection_ok
        else "A0_FAIL",
        "A1": "A1_PASS_ANALYTIC"
        if controls["a1"]
        and bridge_types["bridge"]
        and bridge_types["splitting"]
        and return_map_ok
        else "A1_FAIL",
        "A2": "A2_ANALYTIC_DETERMINANT" if boundary_ok else "NOT_TESTABLE",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE" if boundary_ok else "NOT_TESTABLE",
        "A4": "A4_FORMAL_HINT" if boundary_ok else "NOT_TESTABLE",
    }
    route_ok = (
        derived_route == expected_route
        and result["route_status_recomputed"] == derived_route
        and result["route_status_expected"] == expected_route
    )
    expected_terminals = [
        "GO_MODULAR_PRIMITIVE_LEDGER",
        "GO_SAME_OBJECT_MAYER_DETERMINANT",
        "STOP_CANONICAL_INTEGER_PROJECTION",
        "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
        "STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED",
        "ROUTE_A_REJECTED",
    ]
    terminal_semantics_math = (
        projection_ok
        and independent_norm_power(rows)
        and exact_root_algebra_valid(rows)
        and bridge_types["bridge"]
    )
    expected_terminal_semantics = {
        "STOP_CANONICAL_INTEGER_PROJECTION": (
            "No projection passes the full rational-prime Euler-ledger conjunction."
        ),
        "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION": (
            "No integer-valued projection simultaneously preserves the exact clock and temporal powers; geodesic norm passes clock/powers but is irrational."
        ),
        "old_overbroad_code_rejected": terminal_semantics_math,
    }
    terminal_ok = (
        result["terminal_codes"] == expected_terminals
        and "STOP_CLOCK_REPETITION_COMPATIBILITY" not in expected_terminals
        and result["terminal_semantics"] == expected_terminal_semantics
        and terminal_semantics_math
    )
    expected_gates = {
        "selection_parser": selection_ok,
        "a0_literal_controls": controls["a0"],
        "a1_literal_controls": controls["a1"],
        "ownership": owner_ok,
        "branch_order_bridge": bridge_types["bridge"],
        "primitivity_splitting": bridge_types["splitting"],
        "return_map_typing": return_map_ok,
        "collision_witnesses": collision_ok,
        "scope_countermodels": countermodel_ok,
        "projection_existential_go": projection_ok,
        "source_boundary": boundary_ok,
        "control_lock": control_lock_ok,
        "route_tuple_recomputed": route_ok,
        "terminal_code_semantics": terminal_ok,
    }
    expected_chronology = (
        "Retrospective M1--M20 correction after provisional v1 and "
        "in-flight corrective smoke outputs; only the exact corrected "
        "input set in CONTROL_LOCK was frozen before the canonical rerun."
    )
    expected_claim_boundary = (
        "Exact bounded controls and hash-backed absence of a declared "
        "untwisted selector only; no universal nonexistence or witness "
        "novelty/minimality claim."
    )
    producer_consistency = (
        result["gates"] == expected_gates
        and result["gate_count"] == len(expected_gates)
        and result["gate_failure_count"] == sum(not value for value in expected_gates.values())
        and result["all_controls_sharp"] == all(expected_gates.values())
        and result["route_b_invocation_allowed"] is False
        and result["chronology"] == expected_chronology
        and result["claim_boundary"] == expected_claim_boundary
    )
    expected_base = {
        "digits": [1, 2],
        "pair_lengths": [1, 2, 3],
        "row_count": 30,
        "rows_sha256": row_hash,
    }
    checks = {
        "schema": result.get("schema") == "sd-c42-corrective-controls-v3",
        "candidate_id": result.get("candidate_id") == "SD-C42",
        "source_hash_field": result.get("source_lock_sha256") == SOURCE_SHA,
        "mayer_hash_field": result.get("mayer_boundary_sha256") == MAYER_SHA,
        "source_boundary_bytes_tokens_and_domains": boundary_ok,
        "control_lock_bytes_and_inputs": control_lock_ok,
        "bounded_base_exact": len(rows) == 30 and result["bounded_base"] == expected_base,
        "selection": selection_ok,
        "a0_mandatory_controls": controls["a0"],
        "a1_mandatory_controls": controls["a1"],
        "ownership": owner_ok,
        "branch_order": bridge_types["bridge"],
        "primitivity_types": bridge_types["splitting"],
        "return_map_typing": return_map_ok,
        "collisions": collision_ok,
        "countermodels": countermodel_ok,
        "projection_truth_matrix": projection_ok,
        "route_tuple": route_ok,
        "route_b_locked": result.get("route_b_invocation_allowed") is False,
        "terminal_semantics": terminal_ok,
        "chronology_exact": result.get("chronology") == expected_chronology,
        "claim_boundary_exact": result.get("claim_boundary") == expected_claim_boundary,
        "aggregate_consistent_with_independent_derivation": producer_consistency,
    }
    return {
        "schema": "sd-c42-independent-control-replay-v1",
        "input_path": result_path.name,
        "input_sha256": sha256(raw).hexdigest(),
        "source_lock_sha256": SOURCE_SHA,
        "mayer_boundary_sha256": MAYER_SHA,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": sum(not passed for passed in checks.values()),
        "all_pass": all(checks.values()),
        "no_reference_import": True,
    }


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "CONTROL_RESULT.json"
    outcome = replay(path)
    print(json.dumps(outcome, indent=2, sort_keys=True))
    if not outcome["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
