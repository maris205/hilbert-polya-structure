#!/usr/bin/env python3
"""Independent checker for HCS-C24.

This checker does not import the producer.  It starts from the explicit
seven-vertex hyperelliptic automaton, uses an adjacency/Mobius count oracle,
and reconstructs every released monodromy from directed edge tokens.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT_ROOT / "results" / "c24_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c24_independent_check.json"
LETTERS = (1, 2, 3, 4)
TYPES = ("t", "b")
WIELANDT = 10

WORD_STATES = {
    "": ((1, 2, 3, 4), (4, 3, 2, 1)),
    "t": ((1, 2, 3, 4), (4, 1, 3, 2)),
    "b": ((1, 4, 2, 3), (4, 3, 2, 1)),
    "tt": ((1, 2, 3, 4), (4, 2, 1, 3)),
    "tb": ((1, 2, 4, 3), (4, 1, 3, 2)),
    "bt": ((1, 4, 2, 3), (4, 3, 1, 2)),
    "bb": ((1, 3, 4, 2), (4, 3, 2, 1)),
}

TRANSITIONS = {
    ("", "t"): "t",
    ("", "b"): "b",
    ("t", "t"): "tt",
    ("t", "b"): "tb",
    ("b", "t"): "bt",
    ("b", "b"): "bb",
    ("tt", "t"): "",
    ("tt", "b"): "tt",
    ("tb", "t"): "tb",
    ("tb", "b"): "t",
    ("bt", "t"): "b",
    ("bt", "b"): "bt",
    ("bb", "t"): "bb",
    ("bb", "b"): "",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def omega(permutation: tuple[tuple[int, ...], tuple[int, ...]]) -> sp.Matrix:
    top, bottom = permutation
    top_at = {letter: index for index, letter in enumerate(top)}
    bottom_at = {letter: index for index, letter in enumerate(bottom)}
    result = sp.zeros(4)
    for alpha in LETTERS:
        for beta in LETTERS:
            inversion = (top_at[alpha] - top_at[beta]) * (bottom_at[alpha] - bottom_at[beta])
            if inversion < 0:
                result[alpha - 1, beta - 1] = 1 if top_at[alpha] < top_at[beta] else -1
    return result


def edge_data(source_word: str, move_type: str) -> tuple[str, int, int, sp.Matrix]:
    target_word = TRANSITIONS[(source_word, move_type)]
    top, bottom = WORD_STATES[source_word]
    if move_type == "t":
        winner, loser = top[-1], bottom[-1]
    else:
        winner, loser = bottom[-1], top[-1]
    matrix = sp.eye(4)
    matrix[loser - 1, winner - 1] += 1
    return target_word, winner, loser, matrix


def matrix_list(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]


def parse_fraction(value: str) -> sp.Rational:
    return sp.Rational(value)


def cycle_rotations(tokens: tuple[tuple[int, str, int], ...]) -> list[tuple[tuple[int, str, int], ...]]:
    return [tokens[index:] + tokens[:index] for index in range(len(tokens))]


def canonical(tokens: tuple[tuple[int, str, int], ...]) -> tuple[tuple[int, str, int], ...]:
    return min(cycle_rotations(tokens))


def is_primitive(tokens: tuple[tuple[int, str, int], ...]) -> bool:
    n = len(tokens)
    return not any(n % d == 0 and tokens == tokens[:d] * (n // d) for d in range(1, n))


def return_branches(tokens: tuple[tuple[int, str, int], ...], central: int) -> list[str]:
    phases = [tokens[index:] + tokens[:index] for index in range(len(tokens)) if tokens[index][0] == central]
    if not phases:
        return []
    based = min(phases)
    visits = [index for index, token in enumerate(based) if token[0] == central]
    pieces = []
    for number, start in enumerate(visits):
        stop = visits[number + 1] if number + 1 < len(visits) else len(based)
        pieces.append("".join(token[1] for token in based[start:stop]))
    return min(pieces[index:] + pieces[:index] for index in range(len(pieces)))


def positivity_exponent(matrix: sp.Matrix) -> int | None:
    value = sp.eye(4)
    for exponent in range(1, WIELANDT + 1):
        value = matrix * value
        if all(entry > 0 for entry in value):
            return exponent
    return None


def tokens_from_row(row: dict[str, object]) -> tuple[tuple[int, str, int], ...]:
    tokens = []
    for encoded in row["canonical_edges"]:
        source, move_type, target = str(encoded).split(":")
        tokens.append((int(source[1:]), move_type, int(target[1:])))
    return tuple(tokens)


def reconstruct_cycle(
    tokens: tuple[tuple[int, str, int], ...],
    id_to_word: dict[int, str],
) -> sp.Matrix:
    result = sp.eye(4)
    current = tokens[0][0]
    for source, move_type, target in tokens:
        if source != current:
            raise ValueError("discontinuous token sequence")
        source_word = id_to_word[source]
        target_word, _, _, edge = edge_data(source_word, move_type)
        if target != next(key for key, value in id_to_word.items() if value == target_word):
            raise ValueError("wrong target in token sequence")
        result = edge * result
        current = target
    if current != tokens[0][0]:
        raise ValueError("open token sequence")
    return result


def mobius_cycle_counts(max_length: int) -> tuple[list[int], list[int]]:
    words = list(WORD_STATES)
    word_id = {word: index for index, word in enumerate(words)}
    adjacency = sp.zeros(len(words))
    for source in words:
        for move_type in TYPES:
            adjacency[word_id[source], word_id[TRANSITIONS[(source, move_type)]]] += 1
    traces, primitive = [], []
    for length in range(1, max_length + 1):
        trace = int((adjacency**length).trace())
        count = sum(
            int(sp.mobius(divisor)) * int((adjacency ** (length // divisor)).trace())
            for divisor in sp.divisors(length)
        ) // length
        traces.append(trace)
        primitive.append(count)
    return traces, primitive


def enumerate_eventual_cycles(
    max_length: int,
    id_to_word: dict[int, str],
) -> dict[tuple[tuple[int, str, int], ...], tuple[list[int], sp.Matrix]]:
    word_to_id = {word: state_id for state_id, word in id_to_word.items()}
    found: dict[tuple[tuple[int, str, int], ...], tuple[list[int], sp.Matrix]] = {}
    for length in range(1, max_length + 1):
        for start_word in WORD_STATES:
            for move_types in itertools.product(TYPES, repeat=length):
                current_word = start_word
                tokens = []
                for move_type in move_types:
                    target_word = TRANSITIONS[(current_word, move_type)]
                    tokens.append((word_to_id[current_word], move_type, word_to_id[target_word]))
                    current_word = target_word
                if current_word != start_word:
                    continue
                key = canonical(tuple(tokens))
                if not is_primitive(key) or key in found:
                    continue
                phase_matrices = [reconstruct_cycle(phase, id_to_word) for phase in cycle_rotations(key)]
                exponents = [positivity_exponent(matrix) for matrix in phase_matrices]
                if all(exponent is not None for exponent in exponents):
                    found[key] = ([int(exponent) for exponent in exponents], phase_matrices[0])
    return found


def check_certificate(certificate: dict[str, object]) -> dict[str, bool]:
    source = certificate["source_lock"]
    graph = certificate["graph"]
    enumeration = certificate["enumeration"]
    released = certificate["eventually_positive_cycles"]

    certificate_states = {
        int(row["id"]): (tuple(row["top"]), tuple(row["bottom"])) for row in graph["states"]
    }
    permutation_to_word = {value: key for key, value in WORD_STATES.items()}
    id_to_word = {state_id: permutation_to_word[permutation] for state_id, permutation in certificate_states.items()}
    word_to_id = {word: state_id for state_id, word in id_to_word.items()}

    source_checks = (
        source["initial_permutation"] == {"top": [1, 2, 3, 4], "bottom": [4, 3, 2, 1]}
        and source["literal_candidate_retained"] is True
        and source["rauzy_class_state_count"] == 7
        and source["rauzy_class_edge_count"] == 14
        and source["det_omega0"] == 1
        and source["rank_omega0"] == 4
        and source["genus"] == 2
        and source["zero_orders"] == [2]
        and source["stratum"] == "H(2)"
        and source["relative_equals_absolute"] is True
        and all(row["equal"] is False for row in source["irreducibility"])
    )

    edge_rows = {(int(row["source"]), row["type"]): row for row in graph["edges"]}
    edge_checks = len(edge_rows) == 14
    for source_word in WORD_STATES:
        for move_type in TYPES:
            source_id = word_to_id[source_word]
            target_word, winner, loser, matrix = edge_data(source_word, move_type)
            row = edge_rows[(source_id, move_type)]
            target_id = word_to_id[target_word]
            edge_checks &= row["target"] == target_id
            edge_checks &= row["winner"] == winner and row["loser"] == loser
            edge_checks &= row["chronological_matrix"] == matrix_list(matrix)
            edge_checks &= matrix * omega(WORD_STATES[source_word]) * matrix.T == omega(WORD_STATES[target_word])

    max_length = int(enumeration["max_elementary_length"])
    traces, primitive_counts = mobius_cycle_counts(max_length)
    released_enumeration = enumeration["rows"]
    count_checks = [int(row["closed_based_paths"]) for row in released_enumeration] == traces
    count_checks &= [int(row["primitive_free_cycles"]) for row in released_enumeration] == primitive_counts
    count_checks &= sum(primitive_counts) == int(enumeration["primitive_free_cycle_total"])

    independently_found = enumerate_eventual_cycles(max_length, id_to_word)
    released_by_tokens = {tokens_from_row(row): row for row in released}
    ledger_checks = set(independently_found) == set(released_by_tokens)
    singular_by_length: dict[str, int] = {}
    eventual_by_length: dict[str, int] = {}
    positive_by_length: dict[str, int] = {}
    return_period_by_length: dict[str, dict[str, int]] = {}
    central = word_to_id[""]
    for tokens, (exponents, matrix) in independently_found.items():
        row = released_by_tokens[tokens]
        characteristic = [int(value) for value in matrix.charpoly().all_coeffs()]
        determinants = {}
        power = sp.eye(4)
        for repetition in range(1, int(enumeration["max_repetition"]) + 1):
            power = matrix * power
            determinants[str(repetition)] = int((sp.eye(4) - power).det())
        lower = parse_fraction(row["perron_root_interval"]["lower"])
        upper = parse_fraction(row["perron_root_interval"]["upper"])
        polynomial = matrix.charpoly().as_poly()
        root_interval_ok = (
            lower > 1
            and upper > lower
            and polynomial.count_roots(lower, upper) == 1
            and polynomial.count_roots(upper, sp.oo) == 0
        )
        expected_winners, expected_losers = [], []
        for source, move_type, _ in tokens:
            _, winner, loser, _ = edge_data(id_to_word[source], move_type)
            expected_winners.append(winner)
            expected_losers.append(loser)
        ledger_checks &= canonical(tokens) == tokens and is_primitive(tokens)
        ledger_checks &= row["type_word"] == "".join(token[1] for token in tokens)
        ledger_checks &= row["winner_word"] == expected_winners
        ledger_checks &= row["loser_word"] == expected_losers
        ledger_checks &= row["complete_winner_set"] is True and sorted(set(expected_winners)) == list(LETTERS)
        ledger_checks &= row["eventual_positive_exponents_by_phase"] == exponents
        ledger_checks &= row["positive_phase_indices"] == [index for index, exponent in enumerate(exponents) if exponent == 1]
        ledger_checks &= row["chronological_matrix"] == matrix_list(matrix)
        ledger_checks &= row["determinant"] == int(matrix.det()) == 1
        start_form = omega(WORD_STATES[id_to_word[tokens[0][0]]]).inv()
        ledger_checks &= matrix.T * start_form * matrix == start_form
        ledger_checks &= row["fixed_form_check"] is True
        ledger_checks &= row["characteristic_coefficients_descending"] == characteristic
        ledger_checks &= characteristic == characteristic[::-1]
        ledger_checks &= row["det_I_minus_power"] == determinants
        ledger_checks &= root_interval_ok
        ledger_checks &= row["labeled_periodic_admissibility"] == "PROVED_FROM_PRIMITIVE_M_TRANSPOSE_PF_VECTOR_AND_EDGE_LENGTH_FACTORIZATION"
        ledger_checks &= row["unmarked_teichmueller_primitive_class"] == "NOT_CLASSIFIED_OR_QUOTIENTED"
        expected_branches = return_branches(tokens, central)
        ledger_checks &= row["central_state"] == central
        ledger_checks &= row["central_first_return_branches"] == expected_branches
        ledger_checks &= row["central_return_period"] == len(expected_branches)
        length_key = str(len(tokens))
        eventual_by_length[length_key] = eventual_by_length.get(length_key, 0) + 1
        if any(exponent == 1 for exponent in exponents):
            positive_by_length[length_key] = positive_by_length.get(length_key, 0) + 1
        return_key = str(len(expected_branches))
        return_bucket = return_period_by_length.setdefault(length_key, {})
        return_bucket[return_key] = return_bucket.get(return_key, 0) + 1
        if determinants["1"] == 0:
            singular_by_length[length_key] = singular_by_length.get(length_key, 0) + 1
            ledger_checks &= all(value == 0 for value in determinants.values())
            ledger_checks &= row["metaplectic_character_locus"] == "singular_fixed_vector_locus"

    summary_checks = (
        eventual_by_length == enumeration["eventually_positive_by_length"]
        and positive_by_length == enumeration["positive_in_at_least_one_phase_by_length"]
        and singular_by_length == enumeration["character_singular_by_length"]
        and return_period_by_length == enumeration["central_return_period_by_elementary_length"]
        and enumeration["all_eventually_positive_cycles_hit_central_state"] is True
        and len(independently_found) == enumeration["eventually_positive_cycle_count"] == 146
        and len({tuple(row["characteristic_coefficients_descending"]) for row in released})
        == enumeration["distinct_reciprocal_characteristic_polynomials"] == 41
        and sum(singular_by_length.values()) == enumeration["character_singular_cycle_count"] == 21
    )
    decision_checks = (
        certificate["operator_gate"]["central_sign"].startswith("unresolved required lift data")
        and certificate["operator_gate"]["ordinary_trace"].startswith("forbidden")
        and certificate["decisions"]["naive_pointwise_weil_character_euler_product"]
        == "REFUTED_ON_LABELED_CODING_BY_SINGULAR_PRIMITIVE_CYCLES"
        and certificate["decisions"]["unsmoothed_branch_compressible_ordinary_fredholm"]
        == "PROVED_SCOPED_OBSTRUCTION_WHEN_STATED_COMPRESSION_EXISTS"
        and certificate["decisions"]["canonical_analytic_zorich_application"]
        == "OPEN_APPLICATION_GATE"
        and certificate["decisions"]["unmarked_teichmueller_orbit_identification"]
        == "OPEN_NOT_NEEDED_FOR_LABELED_RETURN_OBSTRUCTION"
        and certificate["decisions"]["route_b_authorized"] is False
    )
    return {
        "literal_source_lock": bool(source_checks),
        "seven_state_fourteen_edge_graph": bool(edge_checks),
        "mobius_trace_completeness_oracle": bool(count_checks),
        "independent_eventual_positive_ledger": bool(ledger_checks),
        "singular_character_locus_counts": bool(summary_checks),
        "claim_boundary_and_center_sign": bool(decision_checks),
    }


def main() -> None:
    args = parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    checks = check_certificate(certificate)
    passed = all(checks.values())
    output = {
        "schema": "HCS-C24-INDEPENDENT-CHECK-v1",
        "material_passport": {
            "origin_skill": "ars-codex academic-research-suite / experiment-agent",
            "origin_mode": "validate",
            "origin_date": "2026-08-09T00:00:00Z",
            "verification_status": "VERIFIED" if passed else "UNVERIFIED",
            "version_label": "validation_v1",
        },
        "certificate": portable_path(args.certificate),
        "certificate_sha256": sha256(args.certificate),
        "checker_sha256": sha256(Path(__file__)),
        "checks": checks,
        "summary": {
            "primitive_free_cycles_through_12": certificate["enumeration"]["primitive_free_cycle_total"],
            "eventually_positive_cycles": certificate["enumeration"]["eventually_positive_cycle_count"],
            "character_singular_cycles": certificate["enumeration"]["character_singular_cycle_count"],
        },
        "passed": passed,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
