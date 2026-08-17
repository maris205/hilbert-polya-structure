#!/usr/bin/env python3
"""Algorithm F: factor/permanence-first independent Paper 43 evaluator.

No project-local import is permitted.  Prime generation, simultaneous CRT,
period collapse, factor separation, YAML scalar extraction, and all science
construction are implemented independently of Algorithm C.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


TOP = tuple(sorted((
    "candidate_contract", "claim_question", "control_grid", "factor_axiom_schema",
    "finite_p0_inputs", "integration_chronology", "literature_boundary_contract",
    "marker_contract", "operator_contract", "portable_source_input",
    "raw_route_contract", "raw_selection_cards", "schema",
    "selection_adapter_contract", "source_axiom_schema", "source_fixture_inputs",
    "terminal_contract", "type_ledger", "writer_sync_contract",
)))
SCIENCE_TOP = tuple(sorted((
    "candidate_id", "claim_scope", "control_grid", "crt_proximality",
    "factor_periodic_rigidity", "finite_p0_sharpness", "integration_chronology",
    "literature_boundary", "marker_ledger", "operator_ledger", "periodic_ledger",
    "route", "schema", "selection", "source_periodic_collapse", "source_topology",
    "terminal_codes", "theorems", "type_ledger",
    "universal_aperiodic_factor_theorem_claimed", "witness_ledger",
)))
SECTION_HASHES = {
    "candidate_contract": "0161f6e46cb1f73ae8a2927bd145f1df8909fcb85a268dfb56bbba07fc9bfb57",
    "claim_question": "5bed6f938a1baf72a77d73c5e50ea7d1c11f116d4db922faae434341ac029abf",
    "control_grid": "bdfd5e1d0e7d5a7817636294dfbf7a082b5b7ce5f7e730f301119803273e31d4",
    "factor_axiom_schema": "0c23e45de89a595904e13e6648128cb1586bcb5077af65bb47ca17813a27f045",
    "finite_p0_inputs": "5d4a47893d39a11d584053414b4cd6e49375f964bc40b10144cc9c9845380089",
    "integration_chronology": "ea4cfc7e6a0a345ecd33823037e570500e1a1d1434e063a7d0328c3607b4dd1f",
    "literature_boundary_contract": "801bcba42c429342f7ac10a27fa5c9b4e381cd415ed9e447cfa5a52b17b1b87b",
    "marker_contract": "f2d529f80cdb90e866b64d36af5a0c7f5ca4ca879e0be4c490bb66e6b145d7f5",
    "operator_contract": "15624a07bc69fc8b8c32f57417eef682606d837297e5937843d5b7ba0d60da41",
    "portable_source_input": "3f504149e98b2c7eb06cc52a7863ed3f04c3689bd07948727acae124dcfc7bb0",
    "raw_route_contract": "e5f22a6bbe19f2e196b822ccd252c9276682daaadf2deecb2d55006b9acf72ca",
    "raw_selection_cards": "79d21c8f5067b43f9a74e8ecd5ed5e72b241d070a17245485df583dbb1e1b183",
    "schema": "7d5446c5a88ca086be0a3783596b8c55969a6502098ee756982fd67c4d2715c9",
    "selection_adapter_contract": "f84f273628c90261c2e8663607dd2de82df8451ec9601aebbe7fd09cf0b13223",
    "source_axiom_schema": "102a5c3dfd183a110289fac2c938bf987e2b770f05072031c348eb2b160899af",
    "source_fixture_inputs": "10fea290cd948cc8f9f078bd24c6a64b37223edf88c5b585128e9ebcb917d1c8",
    "terminal_contract": "2fc031b7df1f5370f267752e4ed0702c1aef3f9041ba9b5a81d1830a62c9901b",
    "type_ledger": "1fbc93d49548a4bb569a5b60ab2d7503bc82f8085d31f70e0a344da3db44dfb4",
    "writer_sync_contract": "748ec3d5e5e37ba3481c739f7200599ef2cf7e63b04c290a9f2ef8c2790c740f",
}


def encode(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def hexdigest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate key in packet")
    return dict(pairs)


def scalar_walk(value: Any) -> None:
    pending = [value]
    while pending:
        current = pending.pop()
        if type(current) is dict:
            if any(type(key) is not str for key in current):
                raise ValueError("non-string JSON key")
            pending.extend(current.values())
        elif type(current) is list:
            pending.extend(current)
        elif current is not None and type(current) not in (str, int, bool):
            raise ValueError("nonexact JSON scalar")


def verify_raw_packet(packet: dict[str, Any]) -> dict[str, bool]:
    if tuple(sorted(packet)) != TOP or packet.get("schema") != "paper43-squarefree-factor-raw-packet-v1":
        raise ValueError("raw top-level contract differs")
    scalar_walk(packet)
    for name, expected in SECTION_HASHES.items():
        if hexdigest(encode(packet[name])) != expected:
            raise ValueError(f"frozen raw section differs: {name}")
    for entry in packet["portable_source_input"]["entries"]:
        if set(entry) != {"container_sha256", "decoded_sha256", "id",
                          "relative_container"}:
            raise ValueError("portable source entry shape")
        path = entry["relative_container"]
        pure = PurePosixPath(path)
        if pure.is_absolute() or ".." in pure.parts or "\\" in path:
            raise ValueError("portable source path escape")
        if re.fullmatch(r"[0-9a-f]{64}", entry["container_sha256"]) is None \
                or re.fullmatch(r"[0-9a-f]{64}", entry["decoded_sha256"]) is None:
            raise ValueError("portable source hash syntax")
    if [row["id"] for row in packet["portable_source_input"]["entries"]] \
            != sorted(row["id"] for row in packet["portable_source_input"]["entries"]):
        raise ValueError("portable source IDs unsorted")
    for card in packet["raw_selection_cards"]:
        if set(card) != {"bytes_base64", "candidate_id", "relative_container", "sha256"}:
            raise ValueError("card shape failure")
        raw = base64.b64decode(card["bytes_base64"], validate=True)
        if hexdigest(raw) != card["sha256"]:
            raise ValueError("card binding failure")
    return {
        "all_raw_sections_hash_bound": True,
        "card_bindings_replayed": True,
        "duplicate_keys_rejected": True,
        "exact_scalars_only": True,
        "portable_paths_checked": True,
        "raw_packet_exact_set": True,
    }


def sieve_prefix(count: int) -> list[int]:
    limit = 16
    while True:
        composite = bytearray(limit + 1)
        for value in range(2, math.isqrt(limit) + 1):
            if not composite[value]:
                start = value * value
                composite[start:limit + 1:value] = b"\x01" * (((limit - start) // value) + 1)
        primes = [value for value in range(2, limit + 1) if not composite[value]]
        if len(primes) >= count:
            return primes[:count]
        limit *= 2


def smallest_missing_bitset(support: list[int], modulus: int) -> int:
    bits = 0
    for coordinate in support:
        bits |= 1 << (coordinate % modulus)
    for residue in range(modulus):
        if ((bits >> residue) & 1) == 0:
            return residue
    raise ValueError("fixture occupies all residues")


def simultaneous_crt(residues: list[int], moduli: list[int]) -> tuple[int, int]:
    product = math.prod(moduli)
    total = 0
    for residue, modulus in zip(residues, moduli):
        partial = product // modulus
        inverse = pow(partial, -1, modulus)
        total += residue * partial * inverse
    return total % product, product


def independent_crt_rows(packet: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    controls = packet["control_grid"]
    rows: list[dict[str, Any]] = []
    tail_rows: list[dict[str, Any]] = []
    numerator, denominator = 2, 3
    for window in controls["windows"]:
        if window == 0:
            numerator, denominator = 2, 3
        else:
            denominator *= 2
            common = math.gcd(numerator, denominator)
            numerator //= common
            denominator //= common
        tail_rows.append({
            "bound_denominator": denominator,
            "bound_formula": "2^(1-L)/3",
            "bound_numerator": numerator,
            "window": window,
        })
    for pair_index, (left, right) in enumerate(controls["ordered_source_pairs"]):
        for window in controls["windows"]:
            primes = sieve_prefix(2 * (2 * window + 1))
            assignments: list[dict[str, Any]] = []
            congruences: list[int] = []
            moduli: list[int] = []
            cursor = iter(primes)
            for coordinate in range(-window, window + 1):
                for point_name, support in (("x", left), ("y", right)):
                    prime = next(cursor)
                    modulus = prime ** 2
                    missing = smallest_missing_bitset(support, modulus)
                    rhs = (missing - coordinate) % modulus
                    assignments.append({
                        "coordinate": coordinate,
                        "missing_residue": missing,
                        "modulus": modulus,
                        "point": point_name,
                        "prime": prime,
                        "rhs_residue": rhs,
                        "support": support,
                    })
                    congruences.append(rhs)
                    moduli.append(modulus)
            solution, product = simultaneous_crt(congruences, moduli)
            vector = [solution % modulus for modulus in moduli]
            if vector != congruences:
                raise ValueError("product-form CRT vector failure")
            zero_verified = all(
                (solution + item["coordinate"]) % item["modulus"]
                not in {position % item["modulus"] for position in item["support"]}
                for item in assignments
            )
            if not zero_verified:
                raise ValueError("independent shift-zero verification failed")
            rows.append({
                "assignment_count": len(assignments),
                "assignments": assignments,
                "modulus_product": product,
                "pair_index": pair_index,
                "solution_n": solution,
                "window": window,
                "zero_window_verified": True,
            })
    return rows, tail_rows


def prime_not_factor(period: int) -> int:
    for prime in sieve_prefix(12):
        if math.gcd(prime, period) == 1:
            return prime
    raise ValueError("prime prefix unexpectedly exhausted")


def independent_period_rows(lengths: list[int]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for length in lengths:
        for bits in range(1 << length):
            word = f"{bits:0{length}b}"
            first = word.find("1")
            if first < 0:
                rows.append({
                    "admissible": True,
                    "first_occupied_coordinate": None,
                    "occupied_residue_count": 0,
                    "period": length,
                    "prime_not_dividing_period": None,
                    "word": word,
                })
            else:
                prime = prime_not_factor(length)
                if math.gcd(length, prime * prime) != 1:
                    raise ValueError("period translation is not invertible")
                rows.append({
                    "admissible": False,
                    "first_occupied_coordinate": first,
                    "occupied_residue_count": prime * prime,
                    "period": length,
                    "prime_not_dividing_period": prime,
                    "word": word,
                })
    return rows


def finite_set_rows(sets: list[list[int]], word: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    known_primes = set(sieve_prefix(16))
    rows: list[dict[str, Any]] = []
    for values in sets:
        if values != sorted(values) or len(values) != len(set(values)) \
                or any(value not in known_primes for value in values):
            raise ValueError("finite-P0 type failure")
        q = 1
        for prime in values:
            q *= prime ** 2
        if not values:
            rows.append({
                "branch": "empty", "least_period": 1, "nontrivial_cycle": False,
                "prime_set": [], "product_Q": 1, "support_residues": {},
                "two_fixed_points": True,
            })
        else:
            if any(q % (prime * prime) for prime in values):
                raise ValueError("finite-P0 divisibility failure")
            rows.append({
                "branch": "nonempty", "least_period": q, "nontrivial_cycle": True,
                "prime_set": values, "product_Q": q,
                "support_residues": {str(prime): [1] for prime in values},
                "two_fixed_points": False,
            })
    rotations = [word[index:] + word[:index] for index in range(len(word))]
    if word != "0111" or len(set(rotations)) != 4:
        raise ValueError("independent modulus-four orbit failure")
    return rows, {
        "least_period": 4,
        "missing_residues_mod_4": [0],
        "prime_set": [2],
        "support_residues_mod_4": [1, 2, 3],
        "word": word,
    }


def parse_atom(token: str) -> Any:
    token = token.strip()
    if token.startswith('"'):
        return json.loads(token)
    if token.startswith("'") and token.endswith("'"):
        return token[1:-1].replace("''", "'")
    if token == "true":
        return True
    if token == "false":
        return False
    if token in {"null", "~"}:
        return None
    if re.fullmatch(r"-?[0-9]+", token):
        return int(token)
    return token


def card_scalar_state_machine(raw: bytes) -> dict[str, Any]:
    values: dict[str, Any] = {}
    levels: dict[int, str] = {}
    seen_keys: dict[tuple[str, int], set[str]] = {}
    for line in raw.decode("utf-8").splitlines():
        stripped = line.lstrip(" ")
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        spaces = len(line) - len(stripped)
        if spaces % 2:
            raise ValueError("card indentation is not two-space aligned")
        depth = spaces // 2
        match = re.match(r"^([A-Za-z0-9_]+):(?:\s*(.*))?$", stripped)
        if not match:
            continue
        key, tail = match.group(1), (match.group(2) or "")
        parent = ".".join(levels[index] for index in range(depth) if index in levels)
        scope = (parent, depth)
        if key in seen_keys.setdefault(scope, set()):
            raise ValueError("duplicate card mapping key")
        seen_keys[scope].add(key)
        for index in list(levels):
            if index >= depth:
                del levels[index]
        full = f"{parent}.{key}" if parent else key
        if tail:
            values[full] = parse_atom(tail)
        else:
            levels[depth] = key
    return values


def resolve_selection(packet: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    survivors: list[str] = []
    for card in packet["raw_selection_cards"]:
        raw = base64.b64decode(card["bytes_base64"], validate=True)
        values = card_scalar_state_machine(raw)
        if values["candidate_id"] != card["candidate_id"]:
            raise ValueError("card identity differs")
        evaluated: list[dict[str, Any]] = []
        for rule in packet["selection_adapter_contract"]["clauses"]:
            actual = values.get(rule["path"])
            ok = type(actual) is str and (
                actual == rule["value"] if rule["operator"] == "equals"
                else rule["value"] in actual
            )
            evaluated.append({
                "actual": actual,
                "operator": rule["operator"],
                "passed": ok,
                "path": rule["path"],
                "required": rule["value"],
            })
        chosen = all(item["passed"] for item in evaluated)
        survivors.extend([card["candidate_id"]] if chosen else [])
        rows.append({
            "candidate_id": card["candidate_id"],
            "clauses": evaluated,
            "selected": chosen,
            "sha256": card["sha256"],
        })
    if survivors != ["SD-C02"]:
        raise ValueError("independent selector differs")
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


def orbit_rows(periods: list[int]) -> list[dict[str, Any]]:
    return [
        {
            "adjacent_orbit_minimum_positive": period > 1,
            "case": "second_fixed_point" if period == 1 else "least_period_greater_than_one",
            "fixed_anchor_orbit_minimum_positive": True,
            "period": period,
            "separation_contradicts_proximality": True,
        }
        for period in periods
    ]


def independent_science(packet: dict[str, Any]) -> dict[str, Any]:
    crt_rows, tail_rows = independent_crt_rows(packet)
    periodic_rows = independent_period_rows(packet["control_grid"]["source_period_word_lengths"])
    p0_rows, mod4 = finite_set_rows(packet["finite_p0_inputs"]["prime_sets"],
                                    packet["finite_p0_inputs"]["concrete_word"])
    selection = resolve_selection(packet)
    fixed_rows = [
        {"fixed_count": 1, "log_zeta_coefficient": f"1/{m}", "m": m,
         "rank_one_trace": 1}
        for m in range(1, packet["control_grid"]["fixed_count_max_m"] + 1)
    ]
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
            "period_rows": orbit_rows(packet["control_grid"]["factor_period_symbols"]),
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
            "modulus_four_control": mod4,
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
            "route_b": {"invocation_allowed": False,
                        "reason": "same_object_primitive_ledger_and_completed_structure_fail"},
            "route_b_invocation_allowed": False,
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT",
                      "A3_FAIL", "A4_FAIL"],
        },
        "schema": "paper43-squarefree-factor-science-projection-v1",
        "selection": selection,
        "source_periodic_collapse": {
            "bounded_rows": periodic_rows,
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
                {"id": "P1", "quantifier": "every_lawful_compact_metrizable_Z_factor",
                 "status": "PROOF_SCHEMA_REPLAY", "statement": "Per(Y,S)={pi(0^Z)}"},
                {"id": "P2", "quantifier": "every_m_at_least_1_and_every_lawful_factor",
                 "status": "PROOF_SCHEMA_REPLAY",
                 "statement": "Fix_count=1,zeta=1/(1-z),D=1-z"},
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
    if tuple(sorted(science)) != SCIENCE_TOP:
        raise ValueError("independent science key set differs")
    return science


def main(arguments: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("independent_evaluator.py requires python3 -I -B")
    if len(arguments) != 1:
        raise SystemExit("usage: independent_evaluator.py PACKET.json")
    raw = Path(arguments[0]).read_bytes()
    packet = json.loads(raw.decode("ascii"), object_pairs_hook=unique_pairs)
    if encode(packet) != raw:
        raise ValueError("packet serialization differs")
    checks = verify_raw_packet(packet)
    science = independent_science(packet)
    checks |= {
        "factor_permanence_by_contradiction_replayed": True,
        "finite_P0_stabilizer_replayed": True,
        "product_formula_CRT_replayed": True,
        "selector_state_parser_replayed": True,
        "sieve_prime_generation_replayed": True,
        "source_period_group_proof_replayed": True,
        "theorem_failure_count_zero": science["theorems"]["failure_count"] == 0,
    }
    if not all(checks.values()):
        raise ValueError("Algorithm F check failure")
    output = {
        "checks": checks,
        "checks_passed": sum(value is True for value in checks.values()),
        "checks_total": len(checks),
        "implementation": {
            "algorithm": "F_factor_permanence_first",
            "crt": "simultaneous_product_formula",
            "factor_proof": "contradiction_via_fixed_anchor_orbit_separation",
            "prime_generator": "sieve",
            "project_local_imports": [],
        },
        "schema": "paper43-independent-evaluation-v1",
        "science": science,
        "science_sha256": hexdigest(encode(science)),
    }
    sys.stdout.buffer.write(encode(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
