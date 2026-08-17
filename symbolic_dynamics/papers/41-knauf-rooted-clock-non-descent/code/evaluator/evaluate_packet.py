#!/usr/bin/env python3
"""Primary exact evaluator for the Paper 41 primitive packet."""

from __future__ import annotations

from base64 import b64decode
from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import PurePosixPath
import re
import sys
from typing import Any


CONTRACT_SHA256 = "2f0bbcf5dd2d2ff725edcb961f94d45c11351ed1c89fe30af803f6ee1aa07bbc"
SELECTION_SHA256 = "0aa7fd4f18df48950c13f8bc4ea48c5e2e3c7fb4e73a42cbf1199312b2897af8"
ROUTE_SCHEMA_SHA256 = "ee1c1fa578afd3f266d164465227afe27c95b0b03d83c619260e9bdc19304ea2"
ROUTE_SKILL_ENCODED_SHA256 = "01f41ed58969518edc7a63130efd7ac68bcdf5d78fd3472af88580d124705739"
ROUTE_SKILL_DECODED_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
SOURCE_MANIFEST_SHA256 = "773671adbfed36050f837d73378baa07237a338c21cf118915dc10cd0d123129"
EXPECTED_BOOL_POINTERS_SHA256 = "86a41f6e2a875ae0825a02c7420fbeca2b4b99e97d491f9227a2d5a392de3da7"

TOP_KEYS = {
    "candidate_id", "claim_boundary", "contract_sha256", "finite_inventory_input",
    "integration_chronology", "marker_ledger", "operator_input", "positive_control_input", "raw_matrices",
    "repair_input", "route_provenance_input", "schema", "selection_input",
    "source_input", "terminal_codes", "type_ledger", "witness_input", "word_convention",
}
EXPECTED_H = {"": 1, "0": 1, "1": 2, "01": 3, "10": 2, "11": 3, "001": 4, "010": 3}
EXPECTED_TYPES = [
    "BinaryNecklace", "DynamicalTransferOperator", "FareyTraceWord", "KnaufRootedWord",
    "KnaufStableState", "LiouvilleStateObservable", "StateInventoryDiagonal",
]
EXPECTED_MARKERS = {
    "k": "finite_spin_chain_depth",
    "r": "temporal_repetition_of_putative_primitive_word",
    "s": "inverse_temperature_or_Dirichlet_variable",
    "u": "free_power_marker_for_diagonal_inventory_operator",
}
EXPECTED_TERMINALS = [
    "GO_SOURCE_PARTITION_TRACE_IDENTITY",
    "STOP_DIRECT_LIMIT_RIGHT_ACTION_NON_DESCENT",
    "STOP_INVENTORY_TRACE_PRIMITIVE_DETERMINANT_IDENTIFICATION",
    "STOP_LIOUVILLE_ORBIT_CHARACTER",
    "STOP_ROOTED_CLOCK_CYCLIC_DESCENT",
    "STOP_ROOTED_CLOCK_TEMPORAL_POWERS",
    "ROUTE_A_REJECTED",
]
EXPECTED_ROUTE = [
    "A0_ANALYTIC_ARITHMETIC_ORIGIN", "A1_FAIL", "A2_FAIL",
    "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL",
]
EXPECTED_RULE_CLAUSES = [
    "a0_verdict_equals_A0_ANALYTIC_ARITHMETIC_ORIGIN",
    "a0_evidence_status_equals_PROVED",
    "a1_verdict_equals_A1_FAIL",
    "a2_verdict_equals_A2_FAIL",
    "a3_verdict_equals_A3_PARTIAL_ANALYTIC_STRUCTURE",
    "a3_evidence_status_equals_PROVED",
    "next_smallest_test_requests_primitive_cycle_construction_or_no_go",
    "next_smallest_test_requests_endogenous_sign_test",
]
EXPECTED_FORBIDDEN_PREDICATES = [
    "candidate_number_order", "hidden_nontriviality", "paper39_order",
    "paper40_correction", "preset_winner", "witness_outcome",
]
CARD_KEYS = {
    "a0_evidence_status", "a0_verdict", "a1_verdict", "a2_verdict",
    "a3_evidence_status", "a3_verdict", "candidate_id", "historical_byte_sha256",
    "next_smallest_test", "source_id",
}
INTEGRATION_CHRONOLOGY = {
    "blind": False,
    "cards_science_witnesses_da_known_before_original_docs": True,
    "fully_prospective": False,
    "known_corrections": [
        "unsorted_result_contract_and_raw_snapshot_hygiene_corrections_known",
        "direct_write_changed_accounting_and_idempotence_defect_known",
        "post_seal_evaluator_byte_drift_known",
        "route_semantic_survivors_and_mutation_coverage_gaps_known",
        "superseded_1c38_static_seal_and_clone_evidence_known",
        "parent_prebootstrap_module_shadow_and_cache_gap_known",
        "direct_emitter_bytecode_cache_gap_known",
        "mandatory_external_tree_portability_gap_known",
        "cross_evaluator_python_equality_type_gap_known",
        "cli_role_and_python_minimum_contract_gaps_known",
        "python_startup_sitecustomize_preexec_gap_known",
        "packet_selection_numeric_equivalent_type_gap_known",
        "coordinated_auditor_json_type_gap_known",
        "globally_sorted_mutation_id_ledger_and_report_audit_gap_known",
        "evaluator_direct_read_and_dynamic_import_boundary_gap_known",
        "hostile_parent_environment_negative_control_gap_known",
        "critical_result_semantic_auditor_closure_gap_known",
        "immutable_ledger_mutation_coverage_gap_known",
        "ast_role_allowlist_and_dynamic_read_gap_known",
        "source_resolver_structural_mutation_coverage_gap_known",
        "selection_and_route_safe_existing_ordered_mutation_gap_known",
        "nontransactional_failed_clone_contamination_gap_known",
    ],
    "novelty_credit": False,
    "original_experiment_docs_pre_initial_code_and_outputs": True,
    "priority_credit": False,
    "replacement_static_frozen_before_replacement_canonical_rerun": True,
    "results_unseen": False,
    "route_survivors_seen_before_replacement_seal": True,
    "status": "RETROSPECTIVE_CORRECTIVE_RESEAL_AFTER_FAILED_OUTPUTS_AND_AUDIT_FINDINGS",
    "superseded_output_materialization_seen_before_replacement_seal": True,
    "write_and_idempotence_defects_seen_before_replacement_seal": True,
}


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest_bytes(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def strict_json_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return list(left) == list(right) and all(strict_json_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_json_equal(a, b) for a, b in zip(left, right))
    return left == right


def json_pointer_token(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def bool_pointers(value: Any, pointer: str = "") -> list[str]:
    if type(value) is bool:
        return [pointer or "/"]
    if type(value) is dict:
        return [
            item
            for key in sorted(value)
            for item in bool_pointers(value[key], pointer + "/" + json_pointer_token(key))
        ]
    if type(value) is list:
        return [item for index, child in enumerate(value) for item in bool_pointers(child, pointer + f"/{index}")]
    return []


def require_packet_numeric_types(packet: Any) -> None:
    def contains_float(value: Any) -> bool:
        if type(value) is float:
            return True
        if type(value) is dict:
            return any(contains_float(child) for child in value.values())
        if type(value) is list:
            return any(contains_float(child) for child in value)
        return False

    require(not contains_float(packet), "PACKET_TYPE_SCHEMA_MISMATCH")


def require_packet_bool_projection(packet: Any) -> None:
    raw = "".join(pointer + "\n" for pointer in sorted(bool_pointers(packet))).encode("ascii")
    require(digest_bytes(raw) == EXPECTED_BOOL_POINTERS_SHA256, "PACKET_TYPE_SCHEMA_MISMATCH")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def exact_keys(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    require(isinstance(value, dict), f"{label} must be an object")
    require(set(value) == keys, f"{label} key set mismatch")
    return value


def safe_payload(payload: str, slash: bool) -> bool:
    if not payload or payload.startswith("/") or "\\" in payload:
        return False
    parts = PurePosixPath(payload).parts
    if any(part in ("", ".", "..") for part in parts):
        return False
    return (slash or len(parts) == 1) and PurePosixPath(payload).as_posix() == payload


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def matrix_for(word: str, matrices: dict[str, list[list[int]]]) -> list[list[int]]:
    result = [[1, 0], [0, 1]]
    for symbol in word:
        result = matmul(result, matrices["L" if symbol == "0" else "R"])
    return result


def h_value(word: str, matrices: dict[str, list[list[int]]]) -> int:
    matrix = matrix_for(word, matrices)
    return matrix[0][0] + matrix[1][0]


def liouville(n: int) -> int:
    require(n >= 1, "Liouville input must be positive")
    parity = 0
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            n //= divisor
            parity ^= 1
        divisor += 1
    if n > 1:
        parity ^= 1
    return -1 if parity else 1


def phi(n: int) -> int:
    result = n
    factor = 2
    remaining = n
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def validate_route_provenance(value: Any) -> dict[str, Any]:
    route = exact_keys(value, {
        "encoded_skill_sha256", "encoded_skill_utf8", "route_schema",
        "route_schema_sha256", "route_schema_utf8", "skill_decoded_sha256",
    }, "route_provenance_input")
    encoded = route["encoded_skill_utf8"].encode("ascii")
    require(digest_bytes(encoded) == ROUTE_SKILL_ENCODED_SHA256, "encoded Route skill bytes changed")
    require(route["encoded_skill_sha256"] == ROUTE_SKILL_ENCODED_SHA256, "encoded Route skill hash field changed")
    decoded = b64decode(b"".join(encoded.split()), validate=True)
    require(digest_bytes(decoded) == ROUTE_SKILL_DECODED_SHA256, "decoded Route skill bytes changed")
    require(route["skill_decoded_sha256"] == ROUTE_SKILL_DECODED_SHA256, "decoded Route skill hash field changed")
    schema_raw = route["route_schema_utf8"].encode("ascii")
    require(digest_bytes(schema_raw) == ROUTE_SCHEMA_SHA256, "Route schema bytes changed")
    require(route["route_schema_sha256"] == ROUTE_SCHEMA_SHA256, "Route schema hash field changed")
    require(strict_json_equal(json.loads(schema_raw), route["route_schema"]), "Route schema object/raw mismatch")
    schema = route["route_schema"]
    require(schema.get("skill_sha256") == ROUTE_SKILL_DECODED_SHA256, "Route schema skill provenance changed")
    require(schema.get("skill_version") == "0.2.0", "Route schema version changed")
    return schema


def validate_sources(value: Any) -> dict[str, Any]:
    source = exact_keys(value, {
        "dependency_ids", "manifest_sha256", "rows", "snapshot_file_count",
    }, "source_input")
    require(source["manifest_sha256"] == SOURCE_MANIFEST_SHA256, "source manifest hash field changed")
    require(source["dependency_ids"] == [
        "dependency:P40_DA_REPORT", "dependency:P40_DA_REPORT_SIDECAR",
    ], "dependency map changed")
    require(source["snapshot_file_count"] == 20, "snapshot count changed")
    rows = source["rows"]
    require(isinstance(rows, list) and len(rows) == 22, "source row count changed")
    ids: list[str] = []
    manifest_lines: list[str] = []
    repo_count = dependency_count = 0
    payload_hashes: dict[str, str] = {}
    for row in rows:
        row = exact_keys(row, {"expected_sha256", "payload_base64", "source_id"}, "source row")
        source_id = row["source_id"]
        match = re.fullmatch(r"(repo|dependency):(.+)", source_id)
        require(match is not None, "malformed typed source ID")
        kind, payload = match.groups()
        require(safe_payload(payload, slash=(kind == "repo")), "unsafe typed source ID")
        if kind == "repo":
            repo_count += 1
        else:
            dependency_count += 1
            require(source_id in source["dependency_ids"], "unknown dependency ID")
        expected = row["expected_sha256"]
        require(re.fullmatch(r"[0-9a-f]{64}", expected) is not None, "malformed source hash")
        raw = b64decode(row["payload_base64"], validate=True)
        require(digest_bytes(raw) == expected, "source payload hash mismatch")
        ids.append(source_id)
        payload_hashes[source_id] = expected
        manifest_lines.append(f"{expected}  {source_id}\n")
    require(ids == sorted(set(ids)), "source IDs are not sorted and unique")
    require(repo_count == 20 and dependency_count == 2, "source kind counts changed")
    require(digest_bytes("".join(manifest_lines).encode("utf-8")) == SOURCE_MANIFEST_SHA256,
            "source manifest reconstruction mismatch")
    return {
        "dependency_count": dependency_count,
        "ids_sha256": digest_bytes("".join(f"{item}\n" for item in ids).encode("utf-8")),
        "matches": len(rows),
        "repo_count": repo_count,
        "source_manifest_sha256": SOURCE_MANIFEST_SHA256,
        "payload_hashes": payload_hashes,
    }


def validate_selection(value: Any, source: dict[str, Any]) -> dict[str, Any]:
    selection = exact_keys(value, {"packet", "packet_sha256", "packet_utf8"}, "selection_input")
    raw = selection["packet_utf8"].encode("ascii")
    packet = json.loads(raw)
    require(strict_json_equal(packet, selection["packet"]), "SELECTION_OUTER_COHERENCE_MISMATCH")
    require(digest_bytes(canonical_bytes(packet)) == SELECTION_SHA256, "SELECTION_SEMANTIC_MISMATCH")
    require(digest_bytes(raw) == SELECTION_SHA256, "SELECTION_BYTE_SEAL_MISMATCH")
    require(selection["packet_sha256"] == SELECTION_SHA256, "SELECTION_BYTE_SEAL_MISMATCH")
    exact_keys(packet, {"cards", "chronology", "expected_survivors", "rule", "schema"}, "selection packet")
    require(packet["schema"] == "paper41-session4-selection-packet-v1", "selection schema changed")
    rule = exact_keys(packet["rule"], {"clauses", "forbidden_predicates", "schema"}, "selection rule")
    require(rule["schema"] == "paper41-retrospective-six-card-selector-v1", "selection rule schema changed")
    require(rule["clauses"] == EXPECTED_RULE_CLAUSES, "selection clauses changed")
    require(rule["forbidden_predicates"] == EXPECTED_FORBIDDEN_PREDICATES, "selection forbidden predicates changed")
    chronology = packet["chronology"]
    expected_chronology = {
        "novelty_credit": False, "outcome_independent": False,
        "paper39_ranking_or_authorization_used": False, "paper40_authorization_used": False,
        "preregistered": False, "priority_credit": False, "prospective": False,
        "status": "RETROSPECTIVE_RESULTS_AND_WITNESSES_KNOWN",
    }
    require(chronology == expected_chronology, "selection chronology changed")
    cards = packet["cards"]
    require(isinstance(cards, list) and len(cards) == 6, "selection card count changed")
    ids = [card.get("candidate_id") if isinstance(card, dict) else None for card in cards]
    require(ids == [f"SD-C0{i}" for i in range(1, 7)], "selection card IDs/order changed")
    card_rows: list[dict[str, Any]] = []
    survivors: list[str] = []
    payload_hashes = source["payload_hashes"]
    for card in cards:
        card = exact_keys(card, CARD_KEYS, "selection card")
        require(card["source_id"] in payload_hashes, "selection source ID absent from source resolver")
        require(card["historical_byte_sha256"] == payload_hashes[card["source_id"]], "selection historical hash mismatch")
        text = card["next_smallest_test"].lower()
        clauses = {
            "a0_analytic": card["a0_verdict"] == "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "a0_proved": card["a0_evidence_status"] == "PROVED",
            "a1_fail": card["a1_verdict"] == "A1_FAIL",
            "a2_fail": card["a2_verdict"] == "A2_FAIL",
            "a3_partial": card["a3_verdict"] == "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "a3_proved": card["a3_evidence_status"] == "PROVED",
            "primitive_request": "construct or rule out a canonical primitive-cycle map" in text,
            "sign_request": "pre-existing symmetry produces the sign" in text,
        }
        eligible = all(clauses.values())
        if eligible:
            survivors.append(card["candidate_id"])
        card_rows.append({"candidate_id": card["candidate_id"], "clauses": clauses, "eligible": eligible})
    require(survivors == ["SD-C06"], "derived selection survivor changed")
    require(packet["expected_survivors"] == survivors, "declared selection survivor changed")
    return {
        "card_rows": card_rows,
        "chronology": chronology,
        "rule_clause_count": len(EXPECTED_RULE_CLAUSES),
        "survivors": survivors,
        "unique": len(survivors) == 1,
    }


def validate_static_contract(packet: dict[str, Any]) -> None:
    require(set(packet) == TOP_KEYS, "packet top-level key set mismatch")
    require(packet["schema"] == "paper41-exact-source-packet-v1", "packet schema changed")
    require(packet["candidate_id"] == "SD-C43", "candidate ID changed")
    require(packet["contract_sha256"] == CONTRACT_SHA256, "contract hash field changed")
    require(packet["integration_chronology"] == INTEGRATION_CHRONOLOGY,
            "INTEGRATION_CHRONOLOGY_MISMATCH")
    require(packet["raw_matrices"] == {"L": [[1, 1], [0, 1]], "R": [[1, 0], [1, 1]]}, "matrix contract changed")
    require(packet["word_convention"] == {
        "alphabet": [0, 1], "complement": "bitwise_binary_complement",
        "h_column_vector": [1, 0], "h_row_vector": [1, 1],
        "product_order": "left_to_right_right_matrix_multiplication",
    }, "word convention changed")
    require(packet["marker_ledger"] == EXPECTED_MARKERS, "marker ledger changed")
    require([item.get("name") for item in packet["type_ledger"] if isinstance(item, dict)] == EXPECTED_TYPES,
            "type ledger")
    expected_type_rows = [
        {"name": "BinaryNecklace", "owns": "cyclic_word_period_and_powers", "not_owned": "rooted_h"},
        {"name": "DynamicalTransferOperator", "owns": "declared_return_powers_only_if_constructed", "not_owned": "not_source_owned_here"},
        {"name": "FareyTraceWord", "owns": "cyclic_trace_and_matrix_power", "not_owned": "frozen_rooted_h_partition_trace"},
        {"name": "KnaufRootedWord", "owns": "M_w_h_and_depth", "not_owned": "cyclic_primitive_class"},
        {"name": "KnaufStableState", "owns": "stable_h_and_multiplicity", "not_owned": "right_append_action"},
        {"name": "LiouvilleStateObservable", "owns": "lambda_of_h", "not_owned": "source_derived_symbolic_cocycle"},
        {"name": "StateInventoryDiagonal", "owns": "trace_and_marked_determinant", "not_owned": "binary_primitive_returns"},
    ]
    require(packet["type_ledger"] == expected_type_rows, "type ledger")
    require(packet["terminal_codes"] == EXPECTED_TERMINALS, "terminal code ledger changed")
    require(packet["finite_inventory_input"] == {"max_n": 8, "r_max": 3, "s": 3, "u": [1, 2]}, "finite inventory input changed")
    require(packet["operator_input"] == {
        "determinant_formula": "product_n_ge_1(1-u*n^(-s))^phi(n)",
        "determinant_owner": "StateInventoryDiagonal", "eigenvalue_one_label": 1,
        "multiplicity_assumption": "full_stable_multiplicity_equals_Euler_phi",
        "primitive_return_owner": False, "trace_class_domain": "Re(s)>2",
        "trace_formula": "zeta(s-1)/zeta(s)", "trace_log_domain": "|u|<1",
    }, "operator contract changed")
    require(packet["repair_input"] == {
        "declared_repairs": ["keep_rooted_words", "quotient_by_rotations", "retain_full_matrix_state",
                             "use_diagonal_Q_s", "use_matrix_trace_or_eigenvalue", "use_word_powers"],
        "scope": "DECLARED_FINITE_REPAIR_FAMILY_ONLY", "universal_exhaustiveness": False,
    }, "repair contract changed")
    require(packet["claim_boundary"] == {
        "changed_models_excluded": ["adelic_operator", "enlarged_state", "Farey_or_Gauss_transfer_operator",
                                    "history_dependent_cocycle", "matrix_trace_or_eigenvalue_clock", "Selberg_determinant"],
        "scope": "FROZEN_ROOTED_H_AND_DECLARED_FINITE_REPAIR_FAMILY_ONLY", "universal_no_go": False,
    }, "claim boundary changed")


def evaluate_packet(packet: dict[str, Any]) -> dict[str, Any]:
    validate_static_contract(packet)
    validate_route_provenance(packet["route_provenance_input"])
    source = validate_sources(packet["source_input"])
    selection = validate_selection(packet["selection_input"], source)

    witness = exact_keys(packet["witness_input"], {
        "cyclic_clock_pair", "cyclic_sign_pair", "direct_limit_generator", "one_letter_words",
        "power_clock", "power_sign", "recurrence_prefix_max_length", "requested_words",
    }, "witness_input")
    require(witness == {
        "cyclic_clock_pair": ["01", "10"], "cyclic_sign_pair": ["001", "010"],
        "direct_limit_generator": ["", "0"], "one_letter_words": ["0", "1", "11"],
        "power_clock": {"base": "1", "exponent": 2, "power": "11"},
        "power_sign": {"base": "1", "exponent": 2, "power": "11"},
        "recurrence_prefix_max_length": 3,
        "requested_words": ["", "0", "001", "01", "010", "1", "10", "11"],
    }, "witness ledger changed")
    controls = packet["positive_control_input"]
    require(controls == {"matrix_power_exponent": 2, "matrix_power_word": "01", "trace_rotation_words": ["01", "10"]},
            "positive-control input changed")

    matrices = packet["raw_matrices"]
    values = {word: h_value(word, matrices) for word in witness["requested_words"]}
    require(values == EXPECTED_H, "small-word h ledger changed")

    recurrence_rows: list[dict[str, Any]] = []
    for length in range(witness["recurrence_prefix_max_length"] + 1):
        for bits in itertools.product("01", repeat=length):
            word = "".join(bits)
            complement = "".join("1" if bit == "0" else "0" for bit in word)
            h_word = h_value(word, matrices)
            append_zero = h_value(word + "0", matrices)
            append_one = h_value(word + "1", matrices)
            expected_one = h_word + h_value(complement, matrices)
            require(append_zero == h_word and append_one == expected_one, "recurrence convention failed")
            recurrence_rows.append({"append_one": append_one, "append_zero": append_zero,
                                    "expected_one": expected_one, "h": h_word, "word": word})

    direct = witness["direct_limit_generator"]
    require(direct[1] == direct[0] + "0", "direct-limit generator changed")
    direct_invariant = h_value(direct[0], matrices) == h_value(direct[1], matrices)
    append_images = [item + "1" for item in direct]
    append_labels = [h_value(item, matrices) for item in append_images]
    require(direct_invariant and append_labels == [2, 3], "append-one non-descent witness failed")

    cyclic_labels = [h_value(item, matrices) for item in witness["cyclic_clock_pair"]]
    power = witness["power_clock"]
    require(power["power"] == power["base"] * power["exponent"], "word power encoding changed")
    power_labels = [h_value(power["base"], matrices), h_value(power["power"], matrices)]
    require(cyclic_labels == [3, 2] and power_labels == [2, 3] and 3 != 2**2,
            "clock non-descent witness failed")

    sign_words = sorted(set(witness["cyclic_sign_pair"] + ["1", "11", "0"]))
    signs = {word: liouville(h_value(word, matrices)) for word in sign_words}
    cyclic_signs = [signs[item] for item in witness["cyclic_sign_pair"]]
    require(cyclic_signs == [1, -1], "Liouville cyclic witness failed")
    require(signs["1"] == -1 and signs["11"] == -1 and signs["11"] != signs["1"]**2,
            "Liouville power witness failed")
    alpha, beta = signs["0"], signs["1"]
    one_letter_contradiction = beta**2 != signs["11"] and alpha == 1 and beta == -1
    require(one_letter_contradiction, "one-letter character contradiction failed")

    trace_words = controls["trace_rotation_words"]
    trace_values = [sum(matrix_for(word, matrices)[i][i] for i in range(2)) for word in trace_words]
    base_matrix = matrix_for(controls["matrix_power_word"], matrices)
    repeated_matrix = matrix_for(controls["matrix_power_word"] * controls["matrix_power_exponent"], matrices)
    power_matrix = matmul(base_matrix, base_matrix)
    require(trace_values == [3, 3] and repeated_matrix == power_matrix, "changed-clock positive control failed")

    inventory = packet["finite_inventory_input"]
    max_n, s_value, r_max = inventory["max_n"], inventory["s"], inventory["r_max"]
    u_value = Fraction(*inventory["u"])
    multiplicities = {str(n): phi(n) for n in range(1, max_n + 1)}
    traces = {
        str(r): fraction_text(sum((Fraction(phi(n), n ** (s_value * r)) for n in range(1, max_n + 1)), Fraction(0)))
        for r in range(1, r_max + 1)
    }
    determinant = Fraction(1)
    for n in range(1, max_n + 1):
        determinant *= (Fraction(1) - u_value * Fraction(1, n**s_value)) ** phi(n)
    require(phi(1) == 1 and (Fraction(1) - Fraction(1, 1**s_value)) == 0,
            "eigenvalue-one determinant factor failed")

    source_public = {key: value for key, value in source.items() if key != "payload_hashes"}
    science = {
        "candidate_id": "SD-C43",
        "claim_scope": "FROZEN_ROOTED_H_AND_DECLARED_FINITE_REPAIR_FAMILY_ONLY",
        "finite_inventory_control": {
            "determinant_at_u_one_half": fraction_text(determinant),
            "eigenvalue_one_forces_zero_at_u_one": True,
            "infinite_multiplicity_status": "INHERITED_SOURCE_THEOREM_NOT_INFERRED_FROM_FINITE_CONTROL",
            "max_n": max_n,
            "multiplicities": multiplicities,
            "trace_powers": traces,
        },
        "h_values": values,
        "integration_chronology": packet["integration_chronology"],
        "liouville_values": signs,
        "marker_ledger": packet["marker_ledger"],
        "positive_controls": {
            "matrix_word_power_identity": True,
            "trace_rotation_values": trace_values,
        },
        "recurrence": {"checked_prefix_count": len(recurrence_rows), "failures": []},
        "route": {
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "route_tuple": EXPECTED_ROUTE,
        },
        "schema": "paper41-exact-science-projection-v1",
        "selection": selection,
        "source_resolver": source_public,
        "terminal_codes": EXPECTED_TERMINALS,
        "theorems": {
            "T0_convention_fidelity": "PROVED",
            "T1_direct_limit_append_one_non_descent": "PROVED",
            "T2_cyclic_clock_and_power_failure": "PROVED",
            "T3_Liouville_character_failure": "PROVED",
            "T4_inventory_trace_determinant_separation": "PROVED_FROM_INHERITED_MULTIPLICITY_AND_EXACT_ALGEBRA",
        },
        "type_names": EXPECTED_TYPES,
        "universal_no_go_claimed": False,
        "witness_ledger": {
            "append_images": append_images,
            "append_labels": append_labels,
            "cyclic_clock_labels": cyclic_labels,
            "cyclic_signs": cyclic_signs,
            "one_letter_character_contradiction": one_letter_contradiction,
            "power_clock_labels": power_labels,
            "power_sign_values": [signs["1"], signs["11"]],
        },
    }
    return {
        "check_count": 24,
        "checks": {name: True for name in [
            "claim_boundary", "contract", "convention", "cyclic_clock", "cyclic_sign",
            "direct_limit", "finite_inventory", "immutable_sources", "Liouville_factorization",
            "marker_ledger", "matrix_power_control", "one_letter_character", "operator_domain",
            "packet_schema", "power_clock", "power_sign", "recurrence", "repair_scope",
            "route_provenance", "selection_chronology", "selection_resolver", "source_resolver",
            "terminal_ledger", "type_ledger",
        ]},
        "implementation": "matrix_primary",
        "schema": "paper41-main-evaluation-v1",
        "science": science,
    }


def duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: evaluate_packet.py PACKET.json", file=sys.stderr)
        return 2
    try:
        raw = open(argv[1], "rb").read()
        packet = json.loads(raw.decode("ascii"), object_pairs_hook=duplicate_rejecting_object)
        require(raw == canonical_bytes(packet), "PACKET_CANONICAL_BYTES_MISMATCH")
        require_packet_numeric_types(packet)
        result = evaluate_packet(packet)
        require_packet_bool_projection(packet)
    except Exception as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(canonical_bytes(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
