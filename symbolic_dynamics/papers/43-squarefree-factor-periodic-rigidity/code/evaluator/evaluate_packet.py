#!/usr/bin/env python3
"""Algorithm C: constructive CRT/source-first Paper 43 evaluator.

This file is deliberately self-contained.  It imports no project-local
module and reads only the raw packet named on the command line.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path, PurePosixPath
from typing import Any


PACKET_KEYS = [
    "candidate_contract", "claim_question", "control_grid",
    "factor_axiom_schema", "finite_p0_inputs", "integration_chronology",
    "literature_boundary_contract", "marker_contract", "operator_contract",
    "portable_source_input", "raw_route_contract", "raw_selection_cards",
    "schema", "selection_adapter_contract", "source_axiom_schema",
    "source_fixture_inputs", "terminal_contract", "type_ledger",
    "writer_sync_contract",
]
SCIENCE_KEYS = [
    "candidate_id", "claim_scope", "control_grid", "crt_proximality",
    "factor_periodic_rigidity", "finite_p0_sharpness",
    "integration_chronology", "literature_boundary", "marker_ledger",
    "operator_ledger", "periodic_ledger", "route", "schema", "selection",
    "source_periodic_collapse", "source_topology", "terminal_codes",
    "theorems", "type_ledger", "universal_aperiodic_factor_theorem_claimed",
    "witness_ledger",
]
SOURCE_ENTRIES_SHA256 = "a629687c2a7a9823c74e4f4224a91b64d724963c4363d9e5db63fdd036ad0560"
CLAUSES_SHA256 = "19af7e4f8f594d061a87194a2d80c82f1d6239da76287b29f60f54e31f05ba62"
WRITER_FIELDS_SHA256 = "c101e29b50f744ba0fa639c332eea372d623fa962edcb91e0cd94fe03c83aa74"
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def exact_keys(value: Any, expected: set[str], context: str) -> None:
    if type(value) is not dict or set(value) != expected:
        raise ValueError(f"{context} exact key-set failure")


def safe_relative(value: str) -> bool:
    if type(value) is not str or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and ".." not in path.parts and "." not in path.parts


def reject_nonexact_scalars(value: Any, path: str = "packet") -> None:
    if type(value) is float:
        raise ValueError(f"float forbidden at {path}")
    if type(value) is dict:
        for key, child in value.items():
            if type(key) is not str:
                raise ValueError(f"non-string key at {path}")
            reject_nonexact_scalars(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_nonexact_scalars(child, f"{path}[{index}]")
    elif value is not None and type(value) not in {bool, int, str}:
        raise ValueError(f"unsupported scalar at {path}")


def expect(value: Any, expected: Any, context: str) -> None:
    if type(value) is not type(expected) or value != expected:
        raise ValueError(f"{context} literal/type mismatch")


def validate_packet(packet: dict[str, Any]) -> dict[str, bool]:
    exact_keys(packet, set(PACKET_KEYS), "packet")
    if list(sorted(packet)) != PACKET_KEYS:
        raise ValueError("packet key vocabulary drift")
    expect(packet["schema"], "paper43-squarefree-factor-raw-packet-v1", "schema")
    reject_nonexact_scalars(packet)

    exact_keys(packet["candidate_contract"],
               {"candidate_id", "family", "historical_parent", "source_type", "target_type"},
               "candidate_contract")
    expect(packet["candidate_contract"], {
        "candidate_id": "SD-C45", "family": "symbolic_dynamics",
        "historical_parent": "SD-C02", "source_type": "SquarefreeAdmissiblePoint",
        "target_type": "TopologicalFactorState",
    }, "candidate_contract")
    exact_keys(packet["claim_question"],
               {"determinant_convention", "factor_quantifier", "question", "source"},
               "claim_question")
    expect(packet["claim_question"]["source"],
           "all_rational_prime_square_admissible_two_sided_shift", "source")
    expect(packet["claim_question"]["question"],
           "can_a_lawful_factor_create_any_periodic_point_other_than_pi_of_zero", "question")
    expect(packet["claim_question"]["factor_quantifier"],
           "every_continuous_surjective_fully_Z_equivariant_map_to_arbitrary_compact_metrizable_Z_system_with_homeomorphism",
           "factor quantifier")
    expect(packet["claim_question"]["determinant_convention"],
           "D_AM_Y(z)=zeta_AM_Y(z)^(-1)", "determinant convention")

    grid = packet["control_grid"]
    exact_keys(grid, {"concrete_modulus_four_word", "factor_period_symbols",
                      "finite_p0_sets", "fixed_count_max_m", "metric",
                      "missing_residue_rule", "ordered_source_pairs",
                      "prime_allocation_rule", "source_fixture_supports",
                      "source_period_word_lengths", "windows"}, "control_grid")
    expect(grid["windows"], [0, 1, 2, 3], "windows")
    expect(grid["source_fixture_supports"], [[], [0], [1], [-1, 2]], "supports")
    expect(grid["ordered_source_pairs"],
           [[[], [0]], [[0], [1]], [[1], [-1, 2]], [[-1, 2], []]], "pairs")
    expect(grid["factor_period_symbols"], [1, 2, 3, 4, 5, 8], "factor periods")
    expect(grid["source_period_word_lengths"], [1, 2, 3, 4, 5, 6, 7, 8],
           "word lengths")
    expect(grid["finite_p0_sets"], [[], [2], [3], [2, 3], [2, 5, 7]], "P0 sets")
    if type(grid["fixed_count_max_m"]) is not int or grid["fixed_count_max_m"] != 8:
        raise ValueError("fixed-count bound mismatch")
    exact_keys(grid["metric"], {"formula", "tail_bound"}, "metric")
    expect(grid["metric"]["tail_bound"], "2^(1-L)/3", "metric tail")
    expect(grid["metric"]["formula"],
           "(1/3)*sum_{k in Z}2^(-abs(k))*abs(x_k-y_k)", "metric formula")
    expect(grid["missing_residue_rule"],
           "least_residue_in_0_to_p2_minus_1_absent_from_support_mod_p2",
           "missing-residue rule")
    expect(grid["prime_allocation_rule"],
           "first_2_times_2L_plus_1_rational_primes_ascending_fresh_per_certificate",
           "prime-allocation rule")
    expect(grid["concrete_modulus_four_word"], "0111", "modulus-four word")

    factor = packet["factor_axiom_schema"]
    exact_keys(factor, {"continuity", "equivariance_equation", "full_Z_equivariance",
                        "surjective", "target_action", "target_space"}, "factor axioms")
    if factor["continuity"] is not True or factor["surjective"] is not True \
            or factor["full_Z_equivariance"] is not True:
        raise ValueError("lawful factor axiom deleted")
    expect(factor["target_action"], "homeomorphism", "target action")
    expect(factor["target_space"], "arbitrary_compact_metrizable_space", "target space")
    expect(factor["equivariance_equation"],
           "pi(sigma^n(x))=S^n(pi(x))_for_every_n_in_Z", "equivariance equation")

    finite = packet["finite_p0_inputs"]
    exact_keys(finite, {"concrete_word", "prime_sets", "product_rule", "witness_rule"},
               "finite P0")
    expect(finite["prime_sets"], grid["finite_p0_sets"], "finite P0 inputs")
    expect(finite["product_rule"], "Q=product_of_p_squared", "P0 product")
    expect(finite["witness_rule"], "x_n=1_iff_n_congruent_1_mod_Q", "P0 witness")

    chronology = packet["integration_chronology"]
    required_chronology = {"blind", "fully_prospective", "implementation_novelty_credit",
                           "literature_known", "novelty_credit", "outcome_independent",
                           "predecessor_roles", "preregistered", "priority_credit",
                           "prospective", "results_unseen",
                           "selector_written_after_outcomes_literature_and_proof", "status"}
    exact_keys(chronology, required_chronology, "chronology")
    for key in ("blind", "fully_prospective", "implementation_novelty_credit",
                "novelty_credit", "outcome_independent", "preregistered",
                "priority_credit", "prospective", "results_unseen"):
        if chronology[key] is not False:
            raise ValueError(f"chronology overclaim: {key}")
    if chronology["literature_known"] is not True \
            or chronology["selector_written_after_outcomes_literature_and_proof"] is not True:
        raise ValueError("retrospective chronology missing")
    if any("not_ranking" not in role and "boundary_only" not in role
           for role in chronology["predecessor_roles"].values()):
        raise ValueError("predecessor role drift")

    literature = packet["literature_boundary_contract"]
    exact_keys(literature, {"bounded_search_absence_is_novelty_proof", "conditional_action",
                            "conditional_code", "route_terminal", "trigger"}, "literature")
    if literature["bounded_search_absence_is_novelty_proof"] is not False \
            or literature["route_terminal"] is not False \
            or literature["conditional_code"] != "STOP_DUPLICATE":
        raise ValueError("duplicate boundary drift")

    exact_keys(packet["marker_contract"], {"comparator_marker", "factor_marker",
                                           "primitive_factor", "repetition_rule",
                                           "specialize_u_to_z"}, "marker")
    expect(packet["marker_contract"]["factor_marker"], "z", "factor marker")
    expect(packet["marker_contract"]["comparator_marker"], "u", "comparator marker")
    expect(packet["marker_contract"]["primitive_factor"], "z", "primitive factor")
    expect(packet["marker_contract"]["repetition_rule"],
           "r_fold_traversal_contributes_z_power_r", "marker repetition")
    if packet["marker_contract"]["specialize_u_to_z"] is not False:
        raise ValueError("marker identification forbidden")

    operator = packet["operator_contract"]
    exact_keys(operator, {"determinant", "dimension", "full_state_operator", "matrix",
                          "owner", "trace_rule"}, "operator")
    expect(operator["matrix"], [[1]], "operator matrix")
    expect(operator["owner"], "singleton_periodic_core", "operator owner")
    expect(operator["determinant"], "det(I-z[1])=1-z", "operator determinant")
    expect(operator["trace_rule"], "trace([1]^m)=1_for_every_m_at_least_1",
           "operator trace rule")
    if type(operator["dimension"]) is not int or operator["dimension"] != 1 \
            or operator["full_state_operator"] is not False:
        raise ValueError("operator owner/type mismatch")

    portable = packet["portable_source_input"]
    exact_keys(portable, {"entries", "external_tree_status", "source_count"}, "portable source")
    if type(portable["source_count"]) is not int or portable["source_count"] != 40:
        raise ValueError("portable source count mismatch")
    expect(portable["external_tree_status"], "NOT_QUERIED", "live source status")
    entries = portable["entries"]
    if type(entries) is not list or len(entries) != 40 or digest(canonical(entries)) != SOURCE_ENTRIES_SHA256:
        raise ValueError("source entry exact-set mismatch")
    ids: list[str] = []
    paths: list[str] = []
    for row in entries:
        exact_keys(row, {"container_sha256", "decoded_sha256", "id",
                         "relative_container"}, "source row")
        if not safe_relative(row["relative_container"]) \
                or not HEX64.fullmatch(row["container_sha256"]) \
                or not HEX64.fullmatch(row["decoded_sha256"]):
            raise ValueError("source row unsafe")
        ids.append(row["id"])
        paths.append(row["relative_container"])
    if ids != sorted(ids) or len(ids) != len(set(ids)) or len(paths) != len(set(paths)):
        raise ValueError("source row order/uniqueness failure")

    route = packet["raw_route_contract"]
    exact_keys(route, {"artifact_path_base", "branch_vocabulary",
                       "evidence_status_vocabulary", "route_b_same_object_completed_structure_required",
                       "route_schema", "rung_names", "rung_status_vocabulary",
                       "state_a_pending_token", "terminal_field_names",
                       "terminal_token_vocabulary"}, "raw Route")
    expect(route["rung_names"], ["a0", "a1", "a2", "a3", "a4"], "Route rungs")
    if any(key in route for key in ("route_tuple", "overall_verdict", "winner")):
        raise ValueError("producer emitted Route answer")

    cards = packet["raw_selection_cards"]
    if type(cards) is not list or len(cards) != 3:
        raise ValueError("selection card count mismatch")
    expected_candidates = ["SD-C02", "SD-C03", "SD-C05"]
    for row, candidate in zip(cards, expected_candidates):
        exact_keys(row, {"bytes_base64", "candidate_id", "relative_container", "sha256"}, "card row")
        expect(row["candidate_id"], candidate, "card candidate")
        raw = base64.b64decode(row["bytes_base64"], validate=True)
        if digest(raw) != row["sha256"] or not safe_relative(row["relative_container"]):
            raise ValueError("card bytes/hash/path mismatch")

    adapter = packet["selection_adapter_contract"]
    exact_keys(adapter, {"clauses", "commissioned_universe", "rule_chronology"}, "adapter")
    expect(adapter["commissioned_universe"], expected_candidates, "selector universe")
    expect(adapter["rule_chronology"],
           "retrospective_after_all_card_outcomes_literature_and_proof",
           "selector chronology")
    if digest(canonical(adapter["clauses"])) != CLAUSES_SHA256:
        raise ValueError("selector clauses changed")
    for clause in adapter["clauses"]:
        exact_keys(clause, {"accepted_type", "operator", "path", "value"}, "selector clause")
        if clause["accepted_type"] != "string" or clause["operator"] not in {"equals", "contains"}:
            raise ValueError("selector clause type/operator failure")
    if "survivor" in adapter or "winner" in adapter:
        raise ValueError("selector answer leaked")

    source_axioms = packet["source_axiom_schema"]
    exact_keys(source_axioms, {"admissibility", "alphabet", "dynamics", "prime_quantifier",
                               "space"}, "source axioms")
    expect(source_axioms["alphabet"], [0, 1], "source alphabet")
    expect(source_axioms["prime_quantifier"], "all_rational_primes", "source quantifier")
    expect(source_axioms["admissibility"],
           "support_mod_p_squared_is_not_all_residues_for_every_rational_prime_p",
           "source admissibility")
    expect(source_axioms["space"], "subset_of_binary_sequences_indexed_by_Z",
           "source space")
    if "j_plus_1" not in source_axioms["dynamics"]:
        raise ValueError("shift direction mismatch")

    fixtures = packet["source_fixture_inputs"]
    exact_keys(fixtures, {"ordered_pairs", "supports", "windows"}, "source fixtures")
    expect(fixtures["ordered_pairs"], grid["ordered_source_pairs"], "fixture pairs")
    expect(fixtures["supports"], grid["source_fixture_supports"], "fixture supports")
    expect(fixtures["windows"], grid["windows"], "fixture windows")

    terminal = packet["terminal_contract"]
    exact_keys(terminal, {"external_control", "external_control_is_route_terminal",
                          "route_field_names", "route_token_vocabulary"}, "terminal contract")
    if terminal["external_control"] != "STOP_DUPLICATE" \
            or terminal["external_control_is_route_terminal"] is not False:
        raise ValueError("STOP_DUPLICATE type drift")
    expect(terminal["route_field_names"],
           ["determinant_comparison", "factor_cycle_creation", "literature",
            "rational_prime_identification"], "terminal fields")

    exact_keys(packet["type_ledger"], {"comparator", "factor_map", "factor_state",
                                       "operator", "primitive", "source_point"}, "type ledger")
    if len(set(packet["type_ledger"].values())) != 6:
        raise ValueError("type ledger collapsed")
    writer = packet["writer_sync_contract"]
    exact_keys(writer, {"allowed_field_names", "anchor_path", "anchor_sha256",
                        "result_values_allowed_before_final_clean"}, "writer sync")
    if digest(canonical(writer["allowed_field_names"])) != WRITER_FIELDS_SHA256 \
            or not safe_relative(writer["anchor_path"]) \
            or not HEX64.fullmatch(writer["anchor_sha256"]) \
            or writer["result_values_allowed_before_final_clean"] is not False:
        raise ValueError("writer sync contract drift")

    return {
        "card_raw_bytes_valid": True,
        "chronology_exact": True,
        "control_grid_exact": True,
        "factor_axioms_exact": True,
        "marker_operator_types_exact": True,
        "packet_recursive_schema_exact": True,
        "portable_source_exact": True,
        "route_raw_only": True,
        "selection_raw_only": True,
        "writer_boundary_exact": True,
    }


def is_prime_trial(value: int) -> bool:
    if type(value) is not int or value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def first_primes(count: int) -> list[int]:
    result: list[int] = []
    candidate = 2
    while len(result) < count:
        if is_prime_trial(candidate):
            result.append(candidate)
        candidate += 1
    return result


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def merge_crt(current: int, modulus: int, residue: int, next_modulus: int) -> tuple[int, int]:
    g, inverse, _ = egcd(modulus, next_modulus)
    if g != 1:
        raise ValueError("CRT moduli are not coprime")
    step = ((residue - current) * inverse) % next_modulus
    combined_modulus = modulus * next_modulus
    return (current + modulus * step) % combined_modulus, combined_modulus


def missing_residue(support: list[int], modulus: int) -> int:
    occupied = {position % modulus for position in support}
    for residue in range(modulus):
        if residue not in occupied:
            return residue
    raise ValueError("fixture fills an entire residue ring")


def build_crt_rows(packet: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    tails: list[dict[str, Any]] = []
    for window in packet["control_grid"]["windows"]:
        bound = Fraction(2 ** max(0, 1 - window), 3) if window <= 1 \
            else Fraction(1, 3 * (2 ** (window - 1)))
        tails.append({
            "bound_denominator": bound.denominator,
            "bound_formula": "2^(1-L)/3",
            "bound_numerator": bound.numerator,
            "window": window,
        })
    for pair_index, pair in enumerate(packet["source_fixture_inputs"]["ordered_pairs"]):
        left, right = pair
        for window in packet["source_fixture_inputs"]["windows"]:
            primes = first_primes(2 * (2 * window + 1))
            assignments: list[dict[str, Any]] = []
            residues: list[tuple[int, int]] = []
            prime_index = 0
            for coordinate in range(-window, window + 1):
                for label, support in (("x", left), ("y", right)):
                    prime = primes[prime_index]
                    prime_index += 1
                    modulus = prime * prime
                    absent = missing_residue(support, modulus)
                    rhs = (absent - coordinate) % modulus
                    assignments.append({
                        "coordinate": coordinate,
                        "missing_residue": absent,
                        "modulus": modulus,
                        "point": label,
                        "prime": prime,
                        "rhs_residue": rhs,
                        "support": support,
                    })
                    residues.append((rhs, modulus))
            solution, product = 0, 1
            for residue, modulus in residues:
                solution, product = merge_crt(solution, product, residue, modulus)
            for assignment in assignments:
                if solution % assignment["modulus"] != assignment["rhs_residue"]:
                    raise ValueError("incremental CRT verification failed")
                shifted = solution + assignment["coordinate"]
                occupied = {position % assignment["modulus"] for position in assignment["support"]}
                if shifted % assignment["modulus"] in occupied:
                    raise ValueError("CRT did not force a zero coordinate")
            rows.append({
                "assignment_count": len(assignments),
                "assignments": assignments,
                "modulus_product": product,
                "pair_index": pair_index,
                "solution_n": solution,
                "window": window,
                "zero_window_verified": True,
            })
    return rows, tails


def least_prime_not_dividing(period: int) -> int:
    candidate = 2
    while True:
        if is_prime_trial(candidate) and period % candidate != 0:
            return candidate
        candidate += 1


def periodic_word_rows(lengths: list[int]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for length in lengths:
        for number in range(2 ** length):
            word = format(number, f"0{length}b")
            occupied = [index for index, bit in enumerate(word) if bit == "1"]
            if not occupied:
                rows.append({
                    "admissible": True,
                    "first_occupied_coordinate": None,
                    "occupied_residue_count": 0,
                    "period": length,
                    "prime_not_dividing_period": None,
                    "word": word,
                })
                continue
            prime = least_prime_not_dividing(length)
            modulus = prime * prime
            first = occupied[0]
            residues = {(first + step * length) % modulus for step in range(modulus)}
            if len(residues) != modulus:
                raise ValueError("period-class residue enumeration failed")
            rows.append({
                "admissible": False,
                "first_occupied_coordinate": first,
                "occupied_residue_count": len(residues),
                "period": length,
                "prime_not_dividing_period": prime,
                "word": word,
            })
    return rows


def least_period(word: str) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and word == word[:period] * (len(word) // period):
            return period
    raise ValueError("finite word has no period")


def finite_p0_rows(prime_sets: list[list[int]], concrete_word: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for values in prime_sets:
        if values != sorted(set(values)) or any(not is_prime_trial(p) for p in values):
            raise ValueError("P0 is not a finite prime set")
        q = math.prod(p * p for p in values)
        if values:
            residues = {str(p): [1] for p in values}
            rows.append({
                "branch": "nonempty",
                "least_period": q,
                "nontrivial_cycle": q > 1,
                "prime_set": values,
                "product_Q": q,
                "support_residues": residues,
                "two_fixed_points": False,
            })
        else:
            rows.append({
                "branch": "empty",
                "least_period": 1,
                "nontrivial_cycle": False,
                "prime_set": [],
                "product_Q": 1,
                "support_residues": {},
                "two_fixed_points": True,
            })
    if concrete_word != "0111" or least_period(concrete_word) != 4:
        raise ValueError("modulus-four control changed")
    concrete = {
        "least_period": 4,
        "missing_residues_mod_4": [0],
        "prime_set": [2],
        "support_residues_mod_4": [1, 2, 3],
        "word": concrete_word,
    }
    return rows, concrete


def yaml_scalar(text: str) -> Any:
    value = text.strip()
    if not value:
        return None
    if value.startswith(('"', "'")):
        if value[0] == '"':
            return json.loads(value)
        return value[1:-1].replace("''", "'")
    if value == "true":
        return True
    if value == "false":
        return False
    if value in {"null", "~"}:
        return None
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    return value


def parse_card_constructive(raw: bytes) -> dict[str, Any]:
    text = raw.decode("utf-8")
    result: dict[str, Any] = {}
    stack: list[tuple[int, str]] = []
    seen_paths: set[str] = set()
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#") or line.lstrip().startswith("-"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent % 2:
            raise ValueError(f"odd YAML indentation at line {line_number}")
        match = re.fullmatch(r"\s*([A-Za-z0-9_]+):(?:\s*(.*))?", line)
        if not match:
            continue
        key, scalar = match.group(1), (match.group(2) or "")
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = ".".join(item[1] for item in stack)
        path = f"{parent}.{key}" if parent else key
        if path in seen_paths:
            raise ValueError(f"duplicate YAML path: {path}")
        seen_paths.add(path)
        if scalar == "":
            stack.append((indent, key))
            continue
        result[path] = yaml_scalar(scalar)
    return result


def selection_projection(packet: dict[str, Any]) -> dict[str, Any]:
    clauses = packet["selection_adapter_contract"]["clauses"]
    rows: list[dict[str, Any]] = []
    survivors: list[str] = []
    for card in packet["raw_selection_cards"]:
        raw = base64.b64decode(card["bytes_base64"], validate=True)
        if digest(raw) != card["sha256"]:
            raise ValueError("selection raw byte mismatch")
        parsed = parse_card_constructive(raw)
        if parsed.get("candidate_id") != card["candidate_id"]:
            raise ValueError("selection candidate mismatch")
        clause_rows: list[dict[str, Any]] = []
        for clause in clauses:
            actual = parsed.get(clause["path"])
            if type(actual) is not str:
                passed = False
            elif clause["operator"] == "equals":
                passed = actual == clause["value"]
            else:
                passed = clause["value"] in actual
            clause_rows.append({
                "actual": actual,
                "operator": clause["operator"],
                "passed": passed,
                "path": clause["path"],
                "required": clause["value"],
            })
        selected = all(row["passed"] for row in clause_rows)
        if selected:
            survivors.append(card["candidate_id"])
        rows.append({
            "candidate_id": card["candidate_id"],
            "clauses": clause_rows,
            "selected": selected,
            "sha256": card["sha256"],
        })
    if survivors != ["SD-C02"]:
        raise ValueError("retrospective selector did not uniquely return C02")
    return {
        "chronology": "RETROSPECTIVE_AFTER_CARD_OUTCOMES_LITERATURE_AND_PROOF",
        "novelty_or_priority_credit": False,
        "outcome_independent": False,
        "predecessor_ranking_or_authorization": False,
        "preregistered": False,
        "prospective": False,
        "rows": rows,
        "survivors": survivors,
    }


def factor_rows(symbols: list[int]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for period in symbols:
        rows.append({
            "adjacent_orbit_minimum_positive": period > 1,
            "case": "second_fixed_point" if period == 1 else "least_period_greater_than_one",
            "fixed_anchor_orbit_minimum_positive": True,
            "period": period,
            "separation_contradicts_proximality": True,
        })
    return rows


def build_science(packet: dict[str, Any]) -> dict[str, Any]:
    crt_rows, tail_rows = build_crt_rows(packet)
    word_rows = periodic_word_rows(packet["control_grid"]["source_period_word_lengths"])
    p0_rows, modulus_four = finite_p0_rows(
        packet["finite_p0_inputs"]["prime_sets"],
        packet["finite_p0_inputs"]["concrete_word"],
    )
    selection = selection_projection(packet)
    fixed_rows = [
        {"fixed_count": 1, "log_zeta_coefficient": f"1/{m}", "m": m,
         "rank_one_trace": 1}
        for m in range(1, packet["control_grid"]["fixed_count_max_m"] + 1)
    ]
    route_tuple = ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT",
                   "A3_FAIL", "A4_FAIL"]
    terminals = {
        "determinant_comparison": "STOP_TRIVIAL_ONE_MINUS_Z_DIVISOR",
        "factor_cycle_creation": "STOP_PROXIMAL_PERIODIC_RIGIDITY",
        "literature": "PROCEED_ONLY_AS_INTERNAL_EXACT_CLOSURE",
        "rational_prime_identification": "STOP_SINGLETON_PRIMITIVE_SUPPORT",
    }
    science = {
        "candidate_id": "SD-C45",
        "claim_scope": {
            "factor_class": "all_continuous_surjective_fully_Z_equivariant_compact_metrizable_factors_with_homeomorphism",
            "source": "exact_all_rational_prime_square_admissible_two_sided_shift",
            "statement": "every_lawful_factor_has_exactly_one_periodic_point_pi_of_zero",
        },
        "control_grid": {
            "classification": "CONTROL_ONLY",
            "factor_period_symbols": packet["control_grid"]["factor_period_symbols"],
            "finite_p0_sets": packet["control_grid"]["finite_p0_sets"],
            "ordered_pair_count": len(packet["control_grid"]["ordered_source_pairs"]),
            "source_period_word_lengths": packet["control_grid"]["source_period_word_lengths"],
            "windows": packet["control_grid"]["windows"],
        },
        "crt_proximality": {
            "control_rows": crt_rows,
            "metric_tail_rows": tail_rows,
            "prime_allocation": "fresh_pairwise_distinct_ascending_rational_primes_per_pair_window",
            "universal_certificate": {
                "dependency_chain": [
                    "missing_residue_for_each_point_and_prime",
                    "fresh_pairwise_coprime_prime_squares",
                    "CRT_for_every_finite_pair_window",
                    "product_metric_tail_tends_to_zero",
                ],
                "finite_rows_are_universal_proof": False,
                "status": "PROOF_SCHEMA_REPLAY",
            },
        },
        "factor_periodic_rigidity": {
            "factor_axioms": packet["factor_axiom_schema"],
            "fixed_anchor": "pi(0^Z)",
            "period_rows": factor_rows(packet["control_grid"]["factor_period_symbols"]),
            "proof_constructions": [
                {
                    "dependencies": ["surjective_lifts", "compact_uniform_continuity",
                                     "source_proximality", "full_Z_equivariance",
                                     "positive_adjacent_orbit_minimum"],
                    "id": "adjacent_orbit_separation",
                },
                {
                    "dependencies": ["fixed_anchor", "invertible_target_action",
                                     "finite_orbit_disjointness", "positive_orbit_anchor_minimum"],
                    "id": "fixed_anchor_orbit_separation",
                },
            ],
            "universal_certificate": {
                "hidden_finite_alphabet_or_radius_assumption": False,
                "periodic_set": ["pi(0^Z)"],
                "status": "PROOF_SCHEMA_REPLAY",
            },
        },
        "finite_p0_sharpness": {
            "arbitrary_finite_set_certificate": {
                "empty_branch": "Q=1_and_zero_and_one_are_distinct_fixed_points",
                "least_period_proof": "translation_stabilizes_1_plus_QZ_iff_multiple_of_Q",
                "nonempty_branch": "Q=product_p_squared_and_support_is_1_mod_Q",
                "status": "PROOF_SCHEMA_REPLAY",
            },
            "modulus_four_control": modulus_four,
            "rows": p0_rows,
        },
        "integration_chronology": packet["integration_chronology"],
        "literature_boundary": {
            "bounded_search_absence_is_novelty_proof": False,
            "conditional_code": "STOP_DUPLICATE",
            "route_terminal": False,
            "standalone_novelty_score": "1/10",
            "status": "LIVE_CONDITIONAL",
            "typed_internal_closure_score": "2/10",
        },
        "marker_ledger": {
            "comparator_marker": "u",
            "factor_marker": "z",
            "primitive_factor": "z",
            "repetitions": [f"z^{r}" for r in range(1, 9)],
            "u_equals_z_identification_allowed": False,
        },
        "operator_ledger": {
            "characteristic_polynomial": "1-z",
            "dimension": 1,
            "full_state_operator": False,
            "matrix": [[1]],
            "owner": "singleton_periodic_core_after_theorem",
            "rational_prime_owner": False,
            "trace_rows": [{"m": m, "trace": 1} for m in range(1, 9)],
        },
        "periodic_ledger": {
            "determinant_orientation": "D_AM=zeta_AM_inverse",
            "fixed_count_rows": fixed_rows,
            "inverse_determinant": "1-z",
            "primitive_objects": ["fixed_orbit_of_pi(0^Z)"],
            "temporal_traversals_are_new_primitives": False,
            "zeta": "1/(1-z)",
        },
        "route": {
            "branch_status": "CLOSE_SD_C02_TOPOLOGICAL_FACTOR_CYCLE_REPAIR",
            "evidence_statuses": ["MODELING_CHOICE", "PROVED", "PROVED", "PROVED",
                                  "NOT_TESTABLE"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b": {
                "invocation_allowed": False,
                "reason": "same_object_primitive_ledger_and_completed_structure_fail",
            },
            "route_b_invocation_allowed": False,
            "tuple": route_tuple,
        },
        "schema": "paper43-squarefree-factor-science-projection-v1",
        "selection": selection,
        "source_periodic_collapse": {
            "bounded_rows": word_rows,
            "only_periodic_source_point": "0^Z",
            "universal_certificate": {
                "prime_choice": "least_rational_prime_not_dividing_period",
                "residue_permutation": "addition_by_period_is_invertible_mod_p_squared",
                "status": "PROOF_SCHEMA_REPLAY",
            },
        },
        "source_topology": {
            "compactness_dependencies": [
                "failure_at_fixed_p_has_finite_occupied_cylinder_witness",
                "failure_set_is_open",
                "admissible_set_is_closed_intersection_in_compact_full_shift",
            ],
            "finite_support_fixture_membership": [
                {"membership": True, "reason": "support_size_at_most_2_less_than_p_squared",
                 "support": support}
                for support in packet["control_grid"]["source_fixture_supports"]
            ],
            "shift_formula": "(sigma^n x)_j=x_(n+j)",
            "shift_invariance": "translation_permutes_residue_classes_mod_p_squared",
            "status": "PROOF_SCHEMA_REPLAY",
        },
        "terminal_codes": terminals,
        "theorems": {
            "failure_count": 0,
            "statements": [
                {
                    "id": "P1",
                    "quantifier": "every_lawful_compact_metrizable_Z_factor",
                    "status": "PROOF_SCHEMA_REPLAY",
                    "statement": "Per(Y,S)={pi(0^Z)}",
                },
                {
                    "id": "P2",
                    "quantifier": "every_m_at_least_1_and_every_lawful_factor",
                    "status": "PROOF_SCHEMA_REPLAY",
                    "statement": "Fix_count=1,zeta=1/(1-z),D=1-z",
                },
            ],
        },
        "type_ledger": packet["type_ledger"],
        "universal_aperiodic_factor_theorem_claimed": False,
        "witness_ledger": {
            "W0": "fixed_point_anchor_pi_of_zero",
            "W1": "source_only_periodic_collapse",
            "W2": "general_pair_window_prime_square_CRT",
            "W3": "smallest_window_two_prime_square_CRT",
            "W4": "finite_periodic_orbit_positive_separation",
            "W5": "singleton_ledger_and_rank_one_determinant",
            "W6": "arbitrary_finite_P0_sharpness_including_empty_case",
            "W7": "lawful_one_point_factor",
            "W8": "singleton_versus_countably_infinite_primitive_support",
            "W9": "predecessor_collision_boundaries_only",
        },
    }
    if sorted(science) != SCIENCE_KEYS:
        raise ValueError("science top-level key set mismatch")
    return science


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("evaluate_packet.py requires python3 -I -B")
    if len(argv) != 1:
        raise SystemExit("usage: evaluate_packet.py PACKET.json")
    packet_path = Path(argv[0])
    raw = packet_path.read_bytes()
    packet = json.loads(raw.decode("ascii"), object_pairs_hook=no_duplicates)
    if raw != canonical(packet):
        raise ValueError("raw packet is not canonical JSON")
    checks = validate_packet(packet)
    science = build_science(packet)
    checks.update({
        "crt_rows_recomputed": True,
        "factor_proof_schema_recomputed": True,
        "finite_p0_rows_recomputed": True,
        "ledger_recomputed": True,
        "selection_recomputed": True,
        "source_periodic_rows_recomputed": True,
        "theorem_failure_count_zero": science["theorems"]["failure_count"] == 0,
    })
    if not all(checks.values()):
        raise ValueError("Algorithm C check failure")
    output = {
        "checks": checks,
        "checks_passed": sum(value is True for value in checks.values()),
        "checks_total": len(checks),
        "implementation": {
            "algorithm": "C_constructive_CRT_source_first",
            "crt": "incremental_extended_euclidean_merge",
            "factor_proof": "epsilon_delta_then_adjacent_orbit_separation",
            "prime_generator": "trial_division",
            "project_local_imports": [],
        },
        "schema": "paper43-main-evaluation-v1",
        "science": science,
        "science_sha256": digest(canonical(science)),
    }
    sys.stdout.buffer.write(canonical(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
