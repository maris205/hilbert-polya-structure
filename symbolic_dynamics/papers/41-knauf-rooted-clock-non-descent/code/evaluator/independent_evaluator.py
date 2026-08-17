#!/usr/bin/env python3
"""Standalone recurrence-first evaluator for Paper 41 / SD-C43.

This module deliberately imports no Paper 41 source, primary evaluator, or
Route renderer module.
"""

from __future__ import annotations

from base64 import b64decode
from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Any

import yaml


CONTRACT = "2f0bbcf5dd2d2ff725edcb961f94d45c11351ed1c89fe30af803f6ee1aa07bbc"
SELECTION = "0aa7fd4f18df48950c13f8bc4ea48c5e2e3c7fb4e73a42cbf1199312b2897af8"
SCHEMA_HASH = "ee1c1fa578afd3f266d164465227afe27c95b0b03d83c619260e9bdc19304ea2"
ENCODED_SKILL = "01f41ed58969518edc7a63130efd7ac68bcdf5d78fd3472af88580d124705739"
SKILL = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
SOURCE_MANIFEST = "773671adbfed36050f837d73378baa07237a338c21cf118915dc10cd0d123129"
EXPECTED_NORMALIZED_ROUTE_SHA256 = "07063e26ee543c0e095f5d67b18b50bd0b8ce3556d6c3683331399cddec82311"
EXPECTED_STAGE1_ROUTE_RAW_SHA256 = "aa0ec86c9cd33c688b6ce8f826c8b9877a33d38bd2eff3995d616ebe6dbdb057"
EXPECTED_BOOL_POINTERS_SHA256 = "86a41f6e2a875ae0825a02c7420fbeca2b4b99e97d491f9227a2d5a392de3da7"

TOP = sorted([
    "candidate_id", "claim_boundary", "contract_sha256", "finite_inventory_input",
    "integration_chronology", "marker_ledger", "operator_input", "positive_control_input", "raw_matrices",
    "repair_input", "route_provenance_input", "schema", "selection_input",
    "source_input", "terminal_codes", "type_ledger", "witness_input", "word_convention",
])
TYPES = [
    "BinaryNecklace", "DynamicalTransferOperator", "FareyTraceWord", "KnaufRootedWord",
    "KnaufStableState", "LiouvilleStateObservable", "StateInventoryDiagonal",
]
MARKERS = {
    "k": "finite_spin_chain_depth",
    "r": "temporal_repetition_of_putative_primitive_word",
    "s": "inverse_temperature_or_Dirichlet_variable",
    "u": "free_power_marker_for_diagonal_inventory_operator",
}
TERMINALS = [
    "GO_SOURCE_PARTITION_TRACE_IDENTITY",
    "STOP_DIRECT_LIMIT_RIGHT_ACTION_NON_DESCENT",
    "STOP_INVENTORY_TRACE_PRIMITIVE_DETERMINANT_IDENTIFICATION",
    "STOP_LIOUVILLE_ORBIT_CHARACTER",
    "STOP_ROOTED_CLOCK_CYCLIC_DESCENT",
    "STOP_ROOTED_CLOCK_TEMPORAL_POWERS",
    "ROUTE_A_REJECTED",
]
ROUTE_TUPLE = [
    "A0_ANALYTIC_ARITHMETIC_ORIGIN", "A1_FAIL", "A2_FAIL",
    "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL",
]
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ZERO_COMMIT = "0" * 40
STAGE1_NOTE = (
    "Stage 1 authority artifact has three PENDING_FIRST_ARTIFACT_COMMIT fields and no "
    "PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it replaces source_commit, code_commit, "
    "and source_lock.code_commit with one identical lowercase nonzero 40-hex artifact commit "
    "and adds the sorted self-excluding PAPER_MANIFEST.sha256."
)
A0_CONTROLS = [
    "inherited_unsigned_observable", "inherited_Liouville_observable", "inherited_Moebius_control",
    "inherited_symbolic_parity_control", "exact_composite_and_rotation_witnesses",
]
A1_CONTROLS = [
    "shuffled_periods", "random_weights", "random_phases", "same_density_random_lengths",
    "neighboring_candidate_parameters", "simpler_parent_candidate",
]
ROUTE_ARTIFACTS = [
    "preauthority/SOURCE_LOCK.md", "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
    "preauthority/DERIVATION_PACKAGE.md", "preauthority/PROOF_PACKAGE.md",
    "preauthority/THEOREM_FALSIFIERS.md", "preauthority/LITERATURE_NOVELTY_AUDIT.md",
    "experiments/PREREGISTRATION.md", "experiments/EXPERIMENT_PLAN.md",
    "results/scientific_results.json", "results/main_evaluation.json", "results/independent_evaluation.json",
]
ROUTE_TOP_KEYS = {
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls", "artifact_path_base",
    "authority_integration", "blocking_conditions", "candidate_id", "claim_boundary", "code_commit",
    "evaluation_date", "freeze_note", "next_smallest_test", "overall_verdict", "round2_clues",
    "route_b", "route_b_invocation_allowed", "route_tuple", "skill", "skill_version", "source_commit",
    "source_lock", "target_and_root_metrics", "terminal_codes",
}
ROUTE_SOURCE_KEYS = {
    "allowed_data", "arithmetic_origin", "artifact_paths", "candidate_definition", "clock", "code_commit",
    "cocycle", "cutoff", "determinant_convention", "dynamics", "family", "forbidden_data", "normalization",
    "object", "orbit_cutoff", "parameter_provenance", "parameters", "phase_space", "potential_function",
    "precision", "roof_function", "training_data",
}
ROUTE_LAYER_KEYS = {
    "a0": {"arithmetic_controls", "artifacts", "evidence_status", "strongest_evidence", "strongest_failure", "verdict"},
    "a1": {"artifacts", "evidence_status", "metrics", "strongest_evidence", "strongest_failure", "verdict"},
    "a2": {"artifacts", "evidence_status", "metrics", "strongest_evidence", "strongest_failure", "verdict"},
    "a3": {"analytic_structure", "artifacts", "evidence_status", "strongest_evidence", "strongest_failure", "verdict", "weil_compression"},
    "a4": {"artifacts", "evidence_status", "metrics", "strongest_evidence", "strongest_failure", "verdict"},
}
RULE_CLAUSES = [
    "a0_verdict_equals_A0_ANALYTIC_ARITHMETIC_ORIGIN",
    "a0_evidence_status_equals_PROVED",
    "a1_verdict_equals_A1_FAIL",
    "a2_verdict_equals_A2_FAIL",
    "a3_verdict_equals_A3_PARTIAL_ANALYTIC_STRUCTURE",
    "a3_evidence_status_equals_PROVED",
    "next_smallest_test_requests_primitive_cycle_construction_or_no_go",
    "next_smallest_test_requests_endogenous_sign_test",
]
FORBIDDEN = [
    "candidate_number_order", "hidden_nontriviality", "paper39_order",
    "paper40_correction", "preset_winner", "witness_outcome",
]
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


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def reject_unless(test: bool, reason: str) -> None:
    if not test:
        raise ValueError(reason)


def same_typed_json(left: Any, right: Any) -> bool:
    stack = [(left, right)]
    while stack:
        first, second = stack.pop()
        if type(first) is not type(second):
            return False
        if type(first) is dict:
            if list(first) != list(second):
                return False
            stack.extend((first[key], second[key]) for key in reversed(list(first)))
        elif type(first) is list:
            if len(first) != len(second):
                return False
            stack.extend(zip(reversed(first), reversed(second)))
        elif first != second:
            return False
    return True


def pointer_escape(token: str) -> str:
    return token.replace("~", "~0").replace("/", "~1")


def numeric_preflight(packet: Any) -> None:
    pending = [packet]
    while pending:
        value = pending.pop()
        reject_unless(type(value) is not float, "INDEPENDENT_PACKET_TYPE_SCHEMA_MISMATCH")
        if type(value) is dict:
            pending.extend(value.values())
        elif type(value) is list:
            pending.extend(value)


def bool_projection_digest(packet: Any) -> str:
    pointers: list[str] = []
    pending = [("", packet)]
    while pending:
        pointer, value = pending.pop()
        if type(value) is bool:
            pointers.append(pointer or "/")
        elif type(value) is dict:
            pending.extend(
                (pointer + "/" + pointer_escape(key), value[key]) for key in reversed(sorted(value))
            )
        elif type(value) is list:
            pending.extend((pointer + f"/{index}", value[index]) for index in reversed(range(len(value))))
    return digest("".join(pointer + "\n" for pointer in sorted(pointers)).encode("ascii"))


def keys_are(value: Any, expected: list[str] | set[str], name: str) -> dict[str, Any]:
    reject_unless(isinstance(value, dict), f"{name}: expected mapping")
    reject_unless(sorted(value) == sorted(expected), f"{name}: keys differ")
    return value


def recursive_h(word: str, memo: dict[str, int]) -> int:
    if word in memo:
        return memo[word]
    prefix, final = word[:-1], word[-1]
    if final == "0":
        answer = recursive_h(prefix, memo)
    elif final == "1":
        opposite = "".join("0" if bit == "1" else "1" for bit in prefix)
        answer = recursive_h(prefix, memo) + recursive_h(opposite, memo)
    else:
        raise ValueError("nonbinary word")
    memo[word] = answer
    return answer


def tuple_product(x: tuple[int, int, int, int], y: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a, b, c, d = x
    e, f, g, h = y
    return a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h


def raw_matrix(word: str, packet: dict[str, Any]) -> tuple[int, int, int, int]:
    mats = packet["raw_matrices"]
    left = (1, 0, 0, 1)
    for bit in word:
        raw = mats["L" if bit == "0" else "R"]
        right = (raw[0][0], raw[0][1], raw[1][0], raw[1][1])
        left = tuple_product(left, right)
    return left


def omega_sign(value: int) -> int:
    count = 0
    candidate = 2
    remainder = value
    while remainder > 1:
        if remainder % candidate == 0:
            remainder //= candidate
            count += 1
        else:
            candidate += 1
    return 1 if count % 2 == 0 else -1


def totient_by_count(n: int) -> int:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def ratio(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def portable(payload: str, repository_kind: bool) -> bool:
    if not isinstance(payload, str) or not payload or payload[:1] == "/" or "\\" in payload:
        return False
    parts = PurePosixPath(payload).parts
    if "" in parts or "." in parts or ".." in parts:
        return False
    if not repository_kind and len(parts) != 1:
        return False
    return PurePosixPath(payload).as_posix() == payload


def inspect_sources(block: Any) -> tuple[dict[str, Any], dict[str, str]]:
    block = keys_are(block, ["dependency_ids", "manifest_sha256", "rows", "snapshot_file_count"], "sources")
    dependencies = ["dependency:P40_DA_REPORT", "dependency:P40_DA_REPORT_SIDECAR"]
    reject_unless(block["dependency_ids"] == dependencies, "dependency map differs")
    reject_unless(block["manifest_sha256"] == SOURCE_MANIFEST, "source-manifest field differs")
    reject_unless(block["snapshot_file_count"] == 20, "snapshot count differs")
    reject_unless(isinstance(block["rows"], list) and len(block["rows"]) == 22, "source count differs")
    identifiers: list[str] = []
    lines: list[str] = []
    hashes: dict[str, str] = {}
    repositories = dependencies_seen = 0
    for entry in block["rows"]:
        entry = keys_are(entry, ["expected_sha256", "payload_base64", "source_id"], "source entry")
        match = re.fullmatch(r"(repo|dependency):(.+)", entry["source_id"])
        reject_unless(match is not None, "typed ID grammar differs")
        kind, payload = match.groups()
        reject_unless(portable(payload, kind == "repo"), "typed ID not portable")
        if kind == "repo":
            repositories += 1
        else:
            dependencies_seen += 1
            reject_unless(entry["source_id"] in dependencies, "unmapped dependency")
        expected = entry["expected_sha256"]
        reject_unless(re.fullmatch(r"[0-9a-f]{64}", expected) is not None, "bad expected digest")
        decoded = b64decode(entry["payload_base64"], validate=True)
        reject_unless(digest(decoded) == expected, "embedded source digest differs")
        identifiers.append(entry["source_id"])
        hashes[entry["source_id"]] = expected
        lines.append(f"{expected}  {entry['source_id']}\n")
    reject_unless(identifiers == sorted(identifiers) and len(set(identifiers)) == 22, "typed IDs order/uniqueness differs")
    reject_unless(repositories == 20 and dependencies_seen == 2, "typed ID kind count differs")
    reject_unless(digest("".join(lines).encode()) == SOURCE_MANIFEST, "source manifest cannot be reconstructed")
    public = {
        "dependency_count": 2,
        "ids_sha256": digest("".join(item + "\n" for item in identifiers).encode()),
        "matches": 22,
        "repo_count": 20,
        "source_manifest_sha256": SOURCE_MANIFEST,
    }
    return public, hashes


def inspect_provenance(block: Any) -> None:
    block = keys_are(block, ["encoded_skill_sha256", "encoded_skill_utf8", "route_schema",
                              "route_schema_sha256", "route_schema_utf8", "skill_decoded_sha256"], "Route provenance")
    encoded = block["encoded_skill_utf8"].encode("ascii")
    reject_unless(digest(encoded) == ENCODED_SKILL and block["encoded_skill_sha256"] == ENCODED_SKILL,
                  "encoded Route skill differs")
    skill_bytes = b64decode(b"".join(encoded.split()), validate=True)
    reject_unless(digest(skill_bytes) == SKILL and block["skill_decoded_sha256"] == SKILL,
                  "decoded Route skill differs")
    schema_bytes = block["route_schema_utf8"].encode("ascii")
    reject_unless(digest(schema_bytes) == SCHEMA_HASH and block["route_schema_sha256"] == SCHEMA_HASH,
                  "Route schema byte seal differs")
    parsed = json.loads(schema_bytes)
    reject_unless(same_typed_json(parsed, block["route_schema"]), "Route schema object differs from raw bytes")
    reject_unless(parsed.get("skill_sha256") == SKILL and parsed.get("skill_version") == "0.2.0",
                  "Route schema provenance differs")


def inspect_selection(block: Any, payload_hashes: dict[str, str]) -> dict[str, Any]:
    block = keys_are(block, ["packet", "packet_sha256", "packet_utf8"], "selection")
    raw = block["packet_utf8"].encode("ascii")
    selection = json.loads(raw)
    reject_unless(same_typed_json(selection, block["packet"]), "SELECTION_OUTER_COHERENCE_MISMATCH")
    reject_unless(digest(canonical(selection)) == SELECTION, "INDEPENDENT_SELECTION_SEMANTIC_MISMATCH")
    reject_unless(digest(raw) == SELECTION and block["packet_sha256"] == SELECTION,
                  "INDEPENDENT_SELECTION_BYTE_SEAL_MISMATCH")
    selection = keys_are(selection, ["cards", "chronology", "expected_survivors", "rule", "schema"], "selection packet")
    reject_unless(selection["schema"] == "paper41-session4-selection-packet-v1", "selection schema differs")
    rule = keys_are(selection["rule"], ["clauses", "forbidden_predicates", "schema"], "selection rule")
    reject_unless(rule == {"clauses": RULE_CLAUSES, "forbidden_predicates": FORBIDDEN,
                            "schema": "paper41-retrospective-six-card-selector-v1"}, "selector rule differs")
    chronology = {
        "novelty_credit": False, "outcome_independent": False,
        "paper39_ranking_or_authorization_used": False, "paper40_authorization_used": False,
        "preregistered": False, "priority_credit": False, "prospective": False,
        "status": "RETROSPECTIVE_RESULTS_AND_WITNESSES_KNOWN",
    }
    reject_unless(selection["chronology"] == chronology, "selector chronology differs")
    cards = selection["cards"]
    reject_unless(isinstance(cards, list) and len(cards) == 6, "six-card census differs")
    reject_unless([c.get("candidate_id") for c in cards if isinstance(c, dict)] ==
                  ["SD-C01", "SD-C02", "SD-C03", "SD-C04", "SD-C05", "SD-C06"], "card order differs")
    fields = ["a0_evidence_status", "a0_verdict", "a1_verdict", "a2_verdict",
              "a3_evidence_status", "a3_verdict", "candidate_id", "historical_byte_sha256",
              "next_smallest_test", "source_id"]
    rows: list[dict[str, Any]] = []
    winners: list[str] = []
    for card in cards:
        card = keys_are(card, fields, "card")
        reject_unless(card["source_id"] in payload_hashes, "card source not in source packet")
        reject_unless(card["historical_byte_sha256"] == payload_hashes[card["source_id"]], "card byte digest differs")
        request = card["next_smallest_test"].casefold()
        tests = {
            "a0_analytic": card["a0_verdict"] == "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "a0_proved": card["a0_evidence_status"] == "PROVED",
            "a1_fail": card["a1_verdict"] == "A1_FAIL",
            "a2_fail": card["a2_verdict"] == "A2_FAIL",
            "a3_partial": card["a3_verdict"] == "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "a3_proved": card["a3_evidence_status"] == "PROVED",
            "primitive_request": "construct or rule out a canonical primitive-cycle map" in request,
            "sign_request": "pre-existing symmetry produces the sign" in request,
        }
        qualifies = not any(flag is False for flag in tests.values())
        if qualifies:
            winners.append(card["candidate_id"])
        rows.append({"candidate_id": card["candidate_id"], "clauses": tests, "eligible": qualifies})
    reject_unless(winners == ["SD-C06"] and selection["expected_survivors"] == winners,
                  "retrospective selector result differs")
    return {"card_rows": rows, "chronology": chronology, "rule_clause_count": 8,
            "survivors": winners, "unique": True}


def inspect_fixed_packet(packet: dict[str, Any]) -> None:
    reject_unless(sorted(packet) == TOP, "top-level packet schema differs")
    reject_unless(packet["candidate_id"] == "SD-C43" and packet["schema"] == "paper41-exact-source-packet-v1",
                  "packet identity differs")
    reject_unless(packet["contract_sha256"] == CONTRACT, "contract digest field differs")
    reject_unless(packet["integration_chronology"] == INTEGRATION_CHRONOLOGY,
                  "INTEGRATION_CHRONOLOGY_MISMATCH")
    reject_unless(packet["raw_matrices"] == {"L": [[1, 1], [0, 1]], "R": [[1, 0], [1, 1]]}, "matrix bytes differ")
    reject_unless(packet["word_convention"] == {
        "alphabet": [0, 1], "complement": "bitwise_binary_complement", "h_column_vector": [1, 0],
        "h_row_vector": [1, 1], "product_order": "left_to_right_right_matrix_multiplication",
    }, "word convention differs")
    reject_unless(packet["marker_ledger"] == MARKERS, "marker ledger differs")
    expected_types = [
        {"name": "BinaryNecklace", "owns": "cyclic_word_period_and_powers", "not_owned": "rooted_h"},
        {"name": "DynamicalTransferOperator", "owns": "declared_return_powers_only_if_constructed", "not_owned": "not_source_owned_here"},
        {"name": "FareyTraceWord", "owns": "cyclic_trace_and_matrix_power", "not_owned": "frozen_rooted_h_partition_trace"},
        {"name": "KnaufRootedWord", "owns": "M_w_h_and_depth", "not_owned": "cyclic_primitive_class"},
        {"name": "KnaufStableState", "owns": "stable_h_and_multiplicity", "not_owned": "right_append_action"},
        {"name": "LiouvilleStateObservable", "owns": "lambda_of_h", "not_owned": "source_derived_symbolic_cocycle"},
        {"name": "StateInventoryDiagonal", "owns": "trace_and_marked_determinant", "not_owned": "binary_primitive_returns"},
    ]
    reject_unless(packet["type_ledger"] == expected_types, "type ledger differs")
    reject_unless(packet["terminal_codes"] == TERMINALS, "terminal ledger differs")
    reject_unless(packet["finite_inventory_input"] == {"max_n": 8, "r_max": 3, "s": 3, "u": [1, 2]},
                  "finite inventory fixture differs")
    reject_unless(packet["operator_input"] == {
        "determinant_formula": "product_n_ge_1(1-u*n^(-s))^phi(n)", "determinant_owner": "StateInventoryDiagonal",
        "eigenvalue_one_label": 1, "multiplicity_assumption": "full_stable_multiplicity_equals_Euler_phi",
        "primitive_return_owner": False, "trace_class_domain": "Re(s)>2", "trace_formula": "zeta(s-1)/zeta(s)",
        "trace_log_domain": "|u|<1",
    }, "operator ledger differs")
    reject_unless(packet["repair_input"] == {
        "declared_repairs": ["keep_rooted_words", "quotient_by_rotations", "retain_full_matrix_state",
                             "use_diagonal_Q_s", "use_matrix_trace_or_eigenvalue", "use_word_powers"],
        "scope": "DECLARED_FINITE_REPAIR_FAMILY_ONLY", "universal_exhaustiveness": False,
    }, "repair scope differs")
    reject_unless(packet["claim_boundary"] == {
        "changed_models_excluded": ["adelic_operator", "enlarged_state", "Farey_or_Gauss_transfer_operator",
                                    "history_dependent_cocycle", "matrix_trace_or_eigenvalue_clock", "Selberg_determinant"],
        "scope": "FROZEN_ROOTED_H_AND_DECLARED_FINITE_REPAIR_FAMILY_ONLY", "universal_no_go": False,
    }, "claim boundary differs")


def evaluate_packet(packet: dict[str, Any]) -> dict[str, Any]:
    inspect_fixed_packet(packet)
    inspect_provenance(packet["route_provenance_input"])
    source_public, payload_hashes = inspect_sources(packet["source_input"])
    selection = inspect_selection(packet["selection_input"], payload_hashes)

    fixture = keys_are(packet["witness_input"], ["cyclic_clock_pair", "cyclic_sign_pair", "direct_limit_generator",
                                                  "one_letter_words", "power_clock", "power_sign",
                                                  "recurrence_prefix_max_length", "requested_words"], "witness fixture")
    expected_fixture = {
        "cyclic_clock_pair": ["01", "10"], "cyclic_sign_pair": ["001", "010"],
        "direct_limit_generator": ["", "0"], "one_letter_words": ["0", "1", "11"],
        "power_clock": {"base": "1", "exponent": 2, "power": "11"},
        "power_sign": {"base": "1", "exponent": 2, "power": "11"},
        "recurrence_prefix_max_length": 3,
        "requested_words": ["", "0", "001", "01", "010", "1", "10", "11"],
    }
    reject_unless(fixture == expected_fixture, "witness fixture differs")
    controls = packet["positive_control_input"]
    reject_unless(controls == {"matrix_power_exponent": 2, "matrix_power_word": "01", "trace_rotation_words": ["01", "10"]},
                  "positive-control fixture differs")

    memo = {"": 1}
    values = {word: recursive_h(word, memo) for word in fixture["requested_words"]}
    expected_h = {"": 1, "0": 1, "001": 4, "01": 3, "010": 3, "1": 2, "10": 2, "11": 3}
    reject_unless(values == expected_h, "recursive h witness differs")
    for word, value in values.items():
        a, _, c, _ = raw_matrix(word, packet)
        reject_unless(a + c == value, "raw matrix/recurrence disagreement")

    recurrence_count = 0
    for length in range(4):
        for symbols in itertools.product(("0", "1"), repeat=length):
            word = "".join(symbols)
            other = "".join("1" if symbol == "0" else "0" for symbol in word)
            reject_unless(recursive_h(word + "0", memo) == recursive_h(word, memo), "append-zero recurrence differs")
            reject_unless(recursive_h(word + "1", memo) == recursive_h(word, memo) + recursive_h(other, memo),
                          "append-one recurrence differs")
            recurrence_count += 1

    direct = fixture["direct_limit_generator"]
    reject_unless(direct[1] == direct[0] + "0", "direct-limit generator differs")
    append_images = [direct[0] + "1", direct[1] + "1"]
    append_labels = [recursive_h(word, memo) for word in append_images]
    reject_unless(recursive_h(direct[0], memo) == recursive_h(direct[1], memo) and append_labels == [2, 3],
                  "direct-limit witness differs")
    cyclic_clock_labels = [recursive_h(word, memo) for word in fixture["cyclic_clock_pair"]]
    power_clock = fixture["power_clock"]
    reject_unless(power_clock["power"] == "".join([power_clock["base"]] * power_clock["exponent"]), "power word differs")
    power_clock_labels = [recursive_h(power_clock["base"], memo), recursive_h(power_clock["power"], memo)]
    reject_unless(cyclic_clock_labels == [3, 2] and power_clock_labels == [2, 3], "clock witnesses differ")

    sign_words = sorted({"0", "1", "11", *fixture["cyclic_sign_pair"]})
    signs = {word: omega_sign(recursive_h(word, memo)) for word in sign_words}
    cyclic_signs = [signs[word] for word in fixture["cyclic_sign_pair"]]
    reject_unless(cyclic_signs == [1, -1], "cyclic sign witness differs")
    reject_unless(signs["1"] == -1 and signs["11"] == -1 and signs["11"] != signs["1"] ** 2,
                  "power sign witness differs")
    one_letter = signs["0"] == 1 and signs["1"] == -1 and signs["1"] ** 2 != signs["11"]
    reject_unless(one_letter, "one-letter contradiction differs")

    trace_values = []
    for word in controls["trace_rotation_words"]:
        a, _, _, d = raw_matrix(word, packet)
        trace_values.append(a + d)
    base = raw_matrix(controls["matrix_power_word"], packet)
    repeated = raw_matrix(controls["matrix_power_word"] * 2, packet)
    reject_unless(trace_values == [3, 3] and tuple_product(base, base) == repeated, "matrix positive controls differ")

    inv = packet["finite_inventory_input"]
    multiplicities = {str(n): totient_by_count(n) for n in range(1, inv["max_n"] + 1)}
    traces: dict[str, str] = {}
    for exponent in range(1, inv["r_max"] + 1):
        terms = [Fraction(totient_by_count(n), n ** (inv["s"] * exponent)) for n in range(1, inv["max_n"] + 1)]
        traces[str(exponent)] = ratio(sum(terms, Fraction(0)))
    u = Fraction(inv["u"][0], inv["u"][1])
    factors = [(Fraction(1) - u / (n ** inv["s"])) ** totient_by_count(n) for n in range(1, inv["max_n"] + 1)]
    determinant = Fraction(1)
    for factor in factors:
        determinant *= factor
    reject_unless(totient_by_count(1) == 1 and Fraction(1) - Fraction(1, 1 ** inv["s"]) == 0,
                  "eigenvalue-one factor differs")

    science = {
        "candidate_id": "SD-C43",
        "claim_scope": "FROZEN_ROOTED_H_AND_DECLARED_FINITE_REPAIR_FAMILY_ONLY",
        "finite_inventory_control": {
            "determinant_at_u_one_half": ratio(determinant),
            "eigenvalue_one_forces_zero_at_u_one": True,
            "infinite_multiplicity_status": "INHERITED_SOURCE_THEOREM_NOT_INFERRED_FROM_FINITE_CONTROL",
            "max_n": 8,
            "multiplicities": multiplicities,
            "trace_powers": traces,
        },
        "h_values": values,
        "integration_chronology": packet["integration_chronology"],
        "liouville_values": signs,
        "marker_ledger": packet["marker_ledger"],
        "positive_controls": {"matrix_word_power_identity": True, "trace_rotation_values": trace_values},
        "recurrence": {"checked_prefix_count": recurrence_count, "failures": []},
        "route": {"overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
                  "route_tuple": ROUTE_TUPLE},
        "schema": "paper41-exact-science-projection-v1",
        "selection": selection,
        "source_resolver": source_public,
        "terminal_codes": TERMINALS,
        "theorems": {
            "T0_convention_fidelity": "PROVED",
            "T1_direct_limit_append_one_non_descent": "PROVED",
            "T2_cyclic_clock_and_power_failure": "PROVED",
            "T3_Liouville_character_failure": "PROVED",
            "T4_inventory_trace_determinant_separation": "PROVED_FROM_INHERITED_MULTIPLICITY_AND_EXACT_ALGEBRA",
        },
        "type_names": TYPES,
        "universal_no_go_claimed": False,
        "witness_ledger": {
            "append_images": append_images,
            "append_labels": append_labels,
            "cyclic_clock_labels": cyclic_clock_labels,
            "cyclic_signs": cyclic_signs,
            "one_letter_character_contradiction": one_letter,
            "power_clock_labels": power_clock_labels,
            "power_sign_values": [signs["1"], signs["11"]],
        },
    }
    return {
        "check_count": 25,
        "checks": {name: True for name in [
            "claim_scope", "contract_digest", "direct_limit_generator", "embedded_sources",
            "finite_determinant", "finite_totients", "h_matrix_crosscheck", "h_recurrence",
            "Liouville_cyclic", "Liouville_factorization", "Liouville_power", "marker_exact_set",
            "matrix_power_control", "one_letter_character", "operator_exact_set", "packet_exact_set",
            "repair_boundary", "rotation_clock", "Route_input_bytes", "selection_card_bytes",
            "selection_chronology", "selection_rule", "temporal_clock", "terminal_exact_set", "type_exact_set",
        ]},
        "implementation": "recurrence_independent",
        "schema": "paper41-independent-evaluation-v1",
        "science": science,
    }


class IndependentDuplicateLoader(yaml.SafeLoader):
    pass


def independent_yaml_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    output: dict[Any, Any] = {}
    for raw_key, raw_value in node.value:
        key = loader.construct_object(raw_key, deep=deep)
        if key in output:
            raise ValueError(f"DUPLICATE_YAML_KEY:{key!r}")
        output[key] = loader.construct_object(raw_value, deep=deep)
    return output


IndependentDuplicateLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, independent_yaml_mapping
)


def sealed_note(commit: str) -> str:
    return (
        f"Stage 1 artifact commit {commit} contained the three PENDING_FIRST_ARTIFACT_COMMIT "
        "fields and no PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it seals source_commit, "
        "code_commit, and source_lock.code_commit to that same lowercase nonzero 40-hex artifact "
        "commit and adds the sorted self-excluding PAPER_MANIFEST.sha256."
    )


def path_is_safe(value: Any) -> bool:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return False
    parts = PurePosixPath(value).parts
    return all(part not in ("", ".", "..") for part in parts) and PurePosixPath(value).as_posix() == value


def independent_route_check(route: dict[str, Any], manifest_present: bool, root: Path) -> dict[str, Any]:
    source = route.get("source_lock") if isinstance(route.get("source_lock"), dict) else {}
    artifact_groups = [source.get("artifact_paths")]
    artifact_groups.extend(route.get(layer, {}).get("artifacts") if isinstance(route.get(layer), dict) else None
                           for layer in ("a0", "a1", "a2", "a3", "a4"))
    present_artifacts = [item for group in artifact_groups if isinstance(group, list) for item in group]
    reject_unless(all(path_is_safe(item) for item in present_artifacts), "UNSAFE_ARTIFACT_PATH")
    reject_unless(all((root / item).is_file() and not (root / item).is_symlink() for item in present_artifacts),
                  "MISSING_ARTIFACT")

    normalized = json.loads(json.dumps(route))
    if "source_commit" in normalized:
        normalized["source_commit"] = PENDING
    if "code_commit" in normalized:
        normalized["code_commit"] = PENDING
    if isinstance(normalized.get("source_lock"), dict) and "code_commit" in normalized["source_lock"]:
        normalized["source_lock"]["code_commit"] = PENDING
    if "freeze_note" in normalized:
        normalized["freeze_note"] = STAGE1_NOTE
    reject_unless(
        digest(canonical(normalized)) == EXPECTED_NORMALIZED_ROUTE_SHA256,
        "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH",
    )

    reject_unless(set(route) == ROUTE_TOP_KEYS, "Route top key set differs")
    reject_unless(route["skill"] == "route-a-evaluator" and route["skill_version"] == "0.2.0",
                  "Route skill identity differs")
    reject_unless(route["candidate_id"] == "SD-C43" and route["evaluation_date"] == "2026-08-17",
                  "Route candidate/date differs")
    reject_unless(route["artifact_path_base"] == "papers/41-knauf-rooted-clock-non-descent",
                  "Route artifact base differs")
    source = route["source_lock"]
    reject_unless(isinstance(source, dict) and set(source) == ROUTE_SOURCE_KEYS, "Route source-lock key set differs")
    triple = [route["source_commit"], route["code_commit"], source["code_commit"]]
    if manifest_present:
        commit = triple[0]
        reject_unless(all(isinstance(item, str) and re.fullmatch(r"[0-9a-f]{40}", item) is not None
                          and item != ZERO_COMMIT for item in triple), "INVALID_COMMIT_FORMAT")
        reject_unless(len(set(triple)) == 1, "PAIRED_STATE_MISMATCH")
        reject_unless(route["freeze_note"] == sealed_note(commit), "STALE_FREEZE_NOTE")
        paired = "VALID_STAGE2"
    else:
        reject_unless(triple == [PENDING, PENDING, PENDING], "PAIRED_STATE_MISMATCH")
        reject_unless(route["freeze_note"] == STAGE1_NOTE, "STALE_FREEZE_NOTE")
        paired = "VALID_STAGE1"

    expected_verdicts = dict(zip(("a0", "a1", "a2", "a3", "a4"), ROUTE_TUPLE))
    all_artifacts: list[str] = []
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        value = route[layer]
        reject_unless(isinstance(value, dict) and set(value) == ROUTE_LAYER_KEYS[layer], f"{layer} key set differs")
        reject_unless(value["verdict"] == expected_verdicts[layer], f"{layer} verdict differs")
        expected_status = {"a0": "PROVED", "a1": "PROVED", "a2": "PROVED", "a3": "PROVED", "a4": "OPEN"}[layer]
        reject_unless(value["evidence_status"] == expected_status, f"{layer} evidence status differs")
        reject_unless(isinstance(value["artifacts"], list) and value["artifacts"]
                      and len(value["artifacts"]) == len(set(value["artifacts"])), f"{layer} artifact set differs")
        all_artifacts.extend(value["artifacts"])
    reject_unless(source["artifact_paths"] == ROUTE_ARTIFACTS, "source artifact set differs")
    all_artifacts.extend(source["artifact_paths"])
    reject_unless(all(path_is_safe(item) for item in all_artifacts), "unsafe Route artifact path")
    reject_unless(all((root / item).is_file() and not (root / item).is_symlink() for item in all_artifacts),
                  "Route artifact path does not resolve")
    reject_unless(route["route_tuple"] == ROUTE_TUPLE, "Route tuple differs")
    reject_unless(route["overall_verdict"] == "ROUTE_A_REJECTED", "Route overall differs")
    reject_unless(route["route_b_invocation_allowed"] is False and route["route_b"] ==
                  {"B": False, "invocation_allowed": False, "invoked": False}, "Route B lock differs")
    reject_unless(route["terminal_codes"] == TERMINALS, "Route terminal set differs")
    reject_unless(route["a0"]["arithmetic_controls"] == A0_CONTROLS, "A0 controls differ")
    reject_unless(route["a1"]["metrics"].get("mandatory_controls") == A1_CONTROLS, "A1 controls differ")
    a2_keys = {"control_margin", "cutoff_drift", "extra_zero_count", "missing_zero_count",
               "precision_drift", "root_count_discrepancy", "zero_error_test", "zero_error_train",
               "zero_error_validation"}
    reject_unless(set(route["a2"]["metrics"]) == a2_keys, "A2 metric exact set differs")
    target = route["target_and_root_metrics"]
    reject_unless(target.get("target_data_used") is False and target.get("target_prime_data") == "NA"
                  and target.get("target_root_data") == "NA" and target.get("target_zero_data") == "NA",
                  "target-data firewall differs")
    reject_unless("no universal changed-model no-go" in route["claim_boundary"], "Route claim scope differs")
    integration = route["authority_integration"]
    reject_unless(integration.get("universal_no_go_claimed") is False
                  and integration.get("source_resolver_matches") == 22
                  and integration.get("theorem_failures") == 0
                  and integration.get("chronology") ==
                  "RETROSPECTIVE_CORRECTIVE_RESEAL_AFTER_FAILED_OUTPUTS_AND_AUDIT_FINDINGS",
                  "Route integration semantics differ")
    science_file = root / "results/scientific_results.json"
    reject_unless(science_file.is_file() and digest(science_file.read_bytes()) == integration.get("scientific_results_sha256"),
                  "Route science hash differs")
    reject_unless(set(route["adversarial_controls"]) == {"controls_used", "proves_too_much_risk", "verdict"}
                  and route["adversarial_controls"]["verdict"] == "STOP_SCOPED", "adversarial gate differs")
    return {
        "check_count": 24,
        "checks": {name: True for name in [
            "A0_controls", "A0_layer", "A1_controls", "A1_layer", "A2_layer", "A2_metrics",
            "A3_layer", "A4_layer", "adversarial_gate", "artifact_base", "artifact_resolution",
            "artifact_safety", "candidate_identity", "claim_scope", "integration_semantics",
            "overall", "paired_state", "route_b", "route_tuple", "science_hash", "source_key_set",
            "target_firewall", "terminal_set", "top_key_set",
        ]},
        "overall_verdict": "ROUTE_A_REJECTED",
        "paired_state": paired,
        "route_b_invocation_allowed": False,
        "route_tuple": ROUTE_TUPLE,
        "schema": "paper41-independent-route-evaluation-v1",
        "terminal_codes": TERMINALS,
    }


def no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 5 and argv[1] == "--route" and argv[3] in ("absent", "present"):
            raw = Path(argv[2]).read_bytes()
            route = yaml.load(raw.decode("ascii"), Loader=IndependentDuplicateLoader)
            reject_unless(isinstance(route, dict), "Route YAML is not a mapping")
            result = independent_route_check(route, argv[3] == "present", Path(argv[4]).resolve())
            reject_unless(raw == yaml.safe_dump(
                route, allow_unicode=False, default_flow_style=False, sort_keys=False, width=100
            ).encode("ascii"), "INDEPENDENT_RAW_ROUTE_RENDERER_BYTES_MISMATCH")
            normalized = json.loads(json.dumps(route))
            normalized["source_commit"] = PENDING
            normalized["code_commit"] = PENDING
            normalized["source_lock"]["code_commit"] = PENDING
            normalized["freeze_note"] = STAGE1_NOTE
            normalized_raw = yaml.safe_dump(
                normalized, allow_unicode=False, default_flow_style=False, sort_keys=False, width=100
            ).encode("ascii")
            reject_unless(digest(normalized_raw) == EXPECTED_STAGE1_ROUTE_RAW_SHA256,
                          "INDEPENDENT_RAW_ROUTE_KEY_ORDER_MISMATCH")
            sys.stdout.buffer.write(canonical(result))
            return 0
        if len(argv) != 2:
            print("usage: independent_evaluator.py PACKET.json | --route ROUTE.yaml absent|present ROOT", file=sys.stderr)
            return 2
        with open(argv[1], "rb") as handle:
            raw = handle.read()
        packet = json.loads(raw.decode("ascii"), object_pairs_hook=no_duplicate_keys)
        reject_unless(raw == canonical(packet), "INDEPENDENT_PACKET_CANONICAL_BYTES_MISMATCH")
        numeric_preflight(packet)
        result = evaluate_packet(packet)
        reject_unless(bool_projection_digest(packet) == EXPECTED_BOOL_POINTERS_SHA256,
                      "INDEPENDENT_PACKET_TYPE_SCHEMA_MISMATCH")
    except Exception as error:
        print(f"REJECT: {error}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
