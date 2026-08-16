#!/usr/bin/env python3
"""Primary independent-of-source evaluator for the Paper 39 closure packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from typing import Any


def canonical_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def independent_registry_parse(registry_text: str, prereg_text: str) -> list[dict[str, Any]]:
    compact = " ".join(prereg_text.split())
    initial_assertion = "Status at freeze: candidate definitions frozen; no numerical candidate result inspected" in compact
    addendum_assertion = "Two objects discovered during the source audit were added before any experiment on either object was run" in compact
    rows: list[dict[str, Any]] = []
    for raw in registry_text.splitlines():
        match = re.match(
            r"^\| \[`(SD-C\d{2})`\]\(([^)]+)\) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$",
            raw,
        )
        if match is None:
            continue
        candidate_id, route_path, obj, route_tuple, status, failure, route_b = match.groups()
        affine = any(token in obj.lower() for token in ("affine", "cayley", "bass-serre", "bs(1"))
        section_match = re.search(rf"^#{{2,3}} {re.escape(candidate_id)}\s+[—-]", prereg_text, re.MULTILINE)
        if section_match is None:
            section = ""
        else:
            remainder = prereg_text[section_match.end():]
            boundary = re.search(r"^#{2,3} SD-C\d{2}(?:\s+[—-]|\s+implementation-freeze)", remainder, re.MULTILINE)
            section = prereg_text[section_match.start():section_match.end() + (boundary.start() if boundary else len(remainder))]
        initial_candidate = candidate_id in {"SD-C01", "SD-C02", "SD-C03", "SD-C04"}
        lock_evidence = {
            "candidate_section_present": section_match is not None,
            "fixed_tests_present": ("Fixed tests and stop rule" in section) if initial_candidate else ("fixed tests" in " ".join(section.lower().split())),
            "frozen_object_present": ("Frozen object" in section) if initial_candidate else bool(re.search(r"\b(?:Define|Set)\b", section)),
            "pre_result_declaration_present": initial_assertion if initial_candidate else addendum_assertion,
            "stop_rule_present": "stop" in section.lower(),
        }
        rows.append({
            "branch_class": "AFFINE" if affine else "NON_AFFINE_PREEXISTING_SOURCE_LOCKED",
            "candidate_id": candidate_id,
            "frozen_route_tuple": route_tuple.strip("`"),
            "object": obj,
            "overall_status": status.strip("`"),
            "route_a_path": route_path,
            "route_b": route_b,
            "source_locked": all(lock_evidence.values()),
            "source_lock_evidence": lock_evidence,
            "strongest_failure": failure,
        })
    return rows


RAW_REQUIREMENTS = {
    "P35": {
        "determinant_convention": ["ordinary primitive trace-log/Fredholm determinant", "no such Fredholm determinant is claimed"],
        "main_theorem_marker": ["one free z", "original U/V generator edge"],
        "object": ["primary positive object has vertices", "changed objects"],
    },
    "P36": {
        "determinant_convention": ["ordinary Fredholm determinant", "prequotient edge operator"],
        "main_theorem_marker": ["one free z", "original oriented graph edge"],
        "object": ["One uninduced oriented-edge affine Cayley object"],
    },
    "P37": {
        "determinant_convention": ["ordinary trace-class matrix Fredholm determinant", "graded cancellation object"],
        "main_theorem_marker": ["one free z", "Hashimoto transition"],
        "object": ["uninduced oriented-edge affine Hashimoto object", "rank-two even and odd"],
    },
    "P38": {
        "determinant_convention": ["ordinary Fredholm determinant", "same full-tree Hashimoto operator", "not that determinant"],
        "main_theorem_marker": ["new Bass-Serre tree-edge step", "no inherited Cayley marker credit"],
        "object": ["unquotiented Bass-Serre tree", "alternative splittings are separately typed and excluded"],
    },
}


EXPECTED_TUPLES = {
    "P35": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "P36": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "P37": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"],
    "P38": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
}


DERIVED_OBSTRUCTIONS = {
    "AFFINE_REPAIR_ALPHABET_COVERED",
    "CONTRACT_RELATIVE_EXHAUSTIVENESS_ONLY",
    "PREEXISTING_SOURCE_LOCKED_NON_AFFINE_REGISTRY_NONEMPTY",
    "ZERO_NEW_MECHANISMS",
}

EXPECTED_GOOD_MEANINGS = {
    "I": "INTRINSIC_SOURCE",
    "R": "NONEMPTY_PRIMITIVE_RECURRENCE_WITH_REPETITIONS",
    "S": "ARITHMETIC_SELECTIVITY",
    "D": "SAME_OBJECT_DETERMINANT_OWNERSHIP",
    "M": "MARKER_COMPATIBILITY",
    "C": "FROZEN_CONTROL_SURVIVAL",
}

EXPECTED_PREREGISTRATION_SEMANTICS = {
    "checker_inputs_frozen_before_checker_run": True,
    "closure_universe_and_predicate_status": "RETROSPECTIVE_ENCODING_FROM_KNOWN_P35_P38_OUTCOMES",
    "freeze_boundary": "FROZEN_BEFORE_PAPER39_CHECKER_EXECUTION_NOT_BEFORE_PREDECESSOR_OUTCOMES",
    "independent_of_predecessor_results_claimed": False,
    "predecessor_outcomes_known_when_encoded": True,
}

EXPECTED_RESET_BINDINGS = {
    "E35_36": {field: "P36_SOURCE_LOCK_SD_C38" for field in ("determinant_owner", "marker", "object", "operator_owner")},
    "E36_37": {field: "P37_SOURCE_LOCK_SD_C39" for field in ("determinant_owner", "marker", "object", "operator_owner")},
    "E37_38": {field: "P38_SOURCE_LOCK_SD_C40" for field in ("determinant_owner", "marker", "object", "operator_owner")},
    "E38_CLOSE": {field: "P39_AUDIT_ONLY_CONTRACT" for field in ("determinant_owner", "marker", "object", "operator_owner")},
    "E_CLOSE_REGISTRY": {field: "SESSION4_REGISTRY_SOURCE_LOCK" for field in ("determinant_owner", "marker", "object", "operator_owner")},
}

EXPECTED_EQUIVALENCE_BINDINGS: dict[str, dict[str, str]] = {}
EXPECTED_NON_INHERITANCE_ASSERTIONS = {
    "E36_37": {
        "candidate_identity_fields": ["object", "marker", "operator_owner", "determinant_owner"],
        "statement": "ALL_CANDIDATE_IDENTITY_FIELDS_RESET_TO_INDEPENDENT_P37_SOURCE_LOCK_NO_SOURCE_TO_TARGET_EQUIVALENCE_CREDIT",
    }
}
EXPECTED_P38_OBJECT_CODE = "FROZEN_ASCENDING_HNN_PRESENTATION_BASS_SERRE_FULL_EDGE_SHIFT"

EXPECTED_EXPANDED_NODE_IDS = ["N00", "N35F", "N35P", "N35S", "N35H", "N35Q", "N35D", "N35B", "N36F", "N36G", "N37O", "N37D", "N37N", "N38T", "N38M", "N38L", "N38O", "N38K", "NX", "NC", "NR", "NS"]
EXPECTED_EXPANDED_EDGE_IDS = ["E00a", "E00b", "E01", "E02", "E03", "E04a", "E04b", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25"]
EXPECTED_INTERNAL_EDGE_IDS = ["E00a", "E00b", "E01", "E02", "E03", "E04a", "E04b", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14"]
EXPECTED_CLOSURE_EDGE_IDS = ["E15", "E16", "E17", "E18", "E19"]
EXPECTED_EXIT_EDGE_IDS = ["E20", "E21", "E23"]
EXPECTED_FIREWALL_EDGE_IDS = ["E22"]
EXPECTED_GUARD_EDGE_IDS = ["E24", "E25"]
EXPECTED_REQUEST_TOKEN_IDS = ["AFFINE_CAYLEY_FROZEN_FAMILY", "FINITE_RANK_LOCAL_SYSTEM_FROZEN_FAMILY", "CHARACTER_FROZEN_FAMILY", "GRADING_FROZEN_FAMILY", "QUOTIENT_FROZEN_FAMILY", "MODULAR_PHASE_FROZEN_FAMILY", "INDUCED_SHIFT_EXIT", "FIRST_RETURN_MAP_EXIT", "VALUATION_TREE_EXIT", "BOUNDARY_MODEL_EXIT", "BASEPOINT_DAMPING_EXIT", "FINITE_TOTAL_WEIGHT_RETROFIT_EXIT", "FROZEN_ASCENDING_HNN_BASS_SERRE_SPLITTING", "ALTERNATIVE_BASS_SERRE_SPLITTING_EXIT", "FROZEN_TREE_LATTICE_GROUPOID_IMPORT", "ALTERNATIVE_GROUPOID_CATEGORY_EXIT"]
EXPECTED_EXPANDED_EDGE_TUPLES = [
    ("E00a", "N00", "N35F", "INTERNAL_TRANSITION"), ("E00b", "N00", "N35P", "INTERNAL_TRANSITION"),
    ("E01", "N35P", "N35S", "INTERNAL_TRANSITION"), ("E02", "N35S", "N35H", "INTERNAL_TRANSITION"),
    ("E03", "N35H", "N35Q", "INTERNAL_TRANSITION"), ("E04a", "N35H", "N35D", "INTERNAL_TRANSITION"),
    ("E04b", "N35H", "N35B", "INTERNAL_TRANSITION"), ("E05", "N35H", "N36F", "INTERNAL_TRANSITION"),
    ("E06", "N36F", "N36G", "INTERNAL_TRANSITION"), ("E07", "N36F", "N37O", "INTERNAL_TRANSITION_RESET"),
    ("E08", "N37O", "N37D", "INTERNAL_TRANSITION"), ("E09", "N37D", "N37N", "INTERNAL_TRANSITION"),
    ("E10", "N37N", "N38T", "INTERNAL_TRANSITION_RESET"), ("E11", "N38T", "N38M", "INTERNAL_TRANSITION"),
    ("E12", "N38T", "N38L", "INTERNAL_TRANSITION_CATEGORY_IMPORT"), ("E13", "N38T", "N38O", "INTERNAL_TRANSITION_RESET"),
    ("E14", "N38T", "N38K", "INTERNAL_TRANSITION_COMPARISON"), ("E15", "N38T", "NC", "CLOSURE"),
    ("E16", "N38M", "NC", "CLOSURE"), ("E17", "N38L", "NC", "CLOSURE"),
    ("E18", "N38O", "NC", "CLOSURE"), ("E19", "N38K", "NC", "CLOSURE"),
    ("E20", "N35H", "NX", "CONTRACT_EXIT"), ("E21", "N36F", "NX", "CONTRACT_EXIT"),
    ("E22", "N37N", "NX", "AUXILIARY_NON_DOMAIN_FIREWALL"), ("E23", "N38T", "NX", "CONTRACT_EXIT"),
    ("E24", "NC", "NR", "GOVERNANCE_GUARD_REALIZED"), ("E25", "NC", "NS", "GOVERNANCE_GUARD_CONDITIONAL"),
]
TOKEN_KEYS = {"token_id", "repair_class", "instance_scope", "disposition", "obstruction_endpoint_ids", "obstruction_edge_ids", "boundary_comparison_endpoint_ids", "boundary_comparison_edge_ids", "exit_endpoint_ids", "exit_edge_ids", "classification_provenance_path_ids", "terminal_codes"}
COVERAGE_KEYS = {"repair_class", "request_token_ids", "disposition", "obstruction_endpoint_ids", "obstruction_edge_ids", "boundary_comparison_endpoint_ids", "boundary_comparison_edge_ids", "exit_endpoint_ids", "exit_edge_ids"}


def graph_is_acyclic(node_ids: set[str], edges: list[dict[str, Any]]) -> bool:
    adjacency = {node_id: [] for node_id in node_ids}
    indegree = {node_id: 0 for node_id in node_ids}
    for edge in edges:
        source = edge.get("from")
        target = edge.get("to")
        if source not in node_ids or target not in node_ids:
            return False
        adjacency[source].append(target)
        indegree[target] += 1
    queue = sorted(node_id for node_id, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        source = queue.pop(0)
        visited += 1
        for target in sorted(adjacency[source]):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
                queue.sort()
    return visited == len(node_ids)


def transfer_rule_valid(rule: dict[str, Any], source_key: str, target_key: str, semantics: dict[str, Any]) -> bool:
    mode = rule.get("mode")
    if mode not in semantics.get("allowed_modes", []):
        return False
    base_keys = {"mode", source_key, target_key}
    if mode == "CARRY_IDENTICAL":
        return set(rule) == base_keys and rule.get(source_key) == rule.get(target_key)
    if mode == "CARRY_WITH_EQUIVALENCE":
        return set(rule) == base_keys | {"equivalence_id"} and rule.get("equivalence_id") in semantics.get("equivalence_ids", [])
    if mode == "RESET":
        return set(rule) == base_keys | {"reset_authority_id"} and rule.get("reset_authority_id") in semantics.get("reset_authority_ids", [])
    return False


def validate_expanded_bridge(bridge: dict[str, Any], bridge_sha256: str, contract: dict[str, Any], input_lock: dict[str, Any], check: Any) -> dict[str, Any]:
    bridge_lock = contract.get("expanded_dag_bridge", {})
    check("bridge_hash_locked", bridge_sha256 == bridge_lock.get("sha256") == "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240")
    check("bridge_schema", bridge.get("schema") == bridge_lock.get("schema") == "paper39-structural-spine-expanded-proof-dag-bridge-v4")
    check("bridge_byte_import_declared", bridge_lock.get("import_byte_identical") is True and bridge_lock.get("relative_path") == "contract/DAG_BRIDGE.json")
    check("graph_granularity_exact", contract.get("graph_granularity") == {
        "expanded_proof_dag": "22_NODE_28_EDGE_MATHEMATICAL_OBSTRUCTION_LEDGER",
        "losslessness_meaning": "ARTIFACT_RETENTION_UNDER_TOTAL_MANY_TO_ONE_NONINJECTIVE_PROJECTION",
        "nodes_and_edges_fields": "6_NODE_5_EDGE_STRUCTURAL_SPINE_ONLY",
        "structural_spine_is_full_dag": False,
    })
    expected_counts = {
        "top_level_repair_classes": 14, "frozen_request_tokens": 16, "internal_transition_tags": 17,
        "structural_spine_nodes": 6, "structural_spine_edges": 5,
        "expanded_proof_dag_nodes": 22, "expanded_proof_dag_edges": 28,
        "token_associated_contract_exit_edges": 3, "auxiliary_non_domain_firewall_edges": 1,
    }
    counts = bridge.get("counts", {})
    check("bridge_counts_exact", counts == expected_counts)
    structural = bridge.get("structural_spine", {})
    check("bridge_structural_nodes_exact", structural.get("node_ids") == [row.get("node_id") for row in contract.get("nodes", [])])
    check("bridge_structural_edges_exact", structural.get("edge_ids") == [row.get("edge_id") for row in contract.get("edges", [])])
    p37_projection_lock = next(spec for spec in input_lock.get("papers", []) if spec.get("paper_id") == "P37")
    check("bridge_e36_37_reset_constraint_exact", bridge.get("projection_transfer_constraints") == {
        "E36_37": {
            "candidate_identity_field_modes": {"determinant_owner": "RESET", "marker": "RESET", "object": "RESET", "operator_owner": "RESET"},
            "carry_fields": ["inherited_obligation", "historical_provenance"],
            "expanded_authority_edge_id": "E07",
            "forbidden_interpretation": "The edge is not an unfill-plus-coefficient construction and does not identify the P36 filled/control object or marker with the independently locked P37 candidate.",
            "reset_authority_id": "P37_SOURCE_LOCK_SD_C39",
            "reset_authority_sha256": p37_projection_lock.get("files", {}).get("SOURCE_LOCK.md"),
            "rule": "A coarse projection may carry audit obligations and historical provenance, but it may not weaken an expanded RESET to CARRY_WITH_EQUIVALENCE without a separately hashed transport theorem. No such theorem exists for E07.",
            "target_field_semantics": {
                "determinant_owner": "NEW_ORDINARY_PARITY_FREDHOLMS_AND_GRADED_RATIO_PROVE_OWNERSHIP_ANEW",
                "marker": "REDECLARED_ORIGINAL_HASHIMOTO_TRANSITION_MARKER_NOT_TRANSPORTED_FROM_FILL",
                "object": "RESET_TO_SEPARATELY_SOURCE_LOCKED_UNQUOTIENTED_MATRIX_AFFINE_HASHIMOTO",
                "operator_owner": "NEW_MATRIX_PARITY_OPERATORS_PROVE_OWNERSHIP_ANEW",
            },
        }
    })

    expanded = bridge.get("expanded_proof_dag", {})
    check("expanded_node_ids_exact_order", expanded.get("node_ids") == EXPECTED_EXPANDED_NODE_IDS)
    check("expanded_edge_ids_exact_order", expanded.get("edge_ids") == EXPECTED_EXPANDED_EDGE_IDS)
    check("internal_tag_ids_exact_order", expanded.get("internal_transition_edge_ids") == EXPECTED_INTERNAL_EDGE_IDS)
    check("closure_edge_ids_exact_order", expanded.get("closure_edge_ids") == EXPECTED_CLOSURE_EDGE_IDS)
    check("exit_edge_ids_exact_order", expanded.get("contract_exit_edge_ids") == EXPECTED_EXIT_EDGE_IDS)
    check("firewall_edge_ids_exact_order", expanded.get("non_domain_firewall_edge_ids") == EXPECTED_FIREWALL_EDGE_IDS)
    check("guard_edge_ids_exact_order", expanded.get("governance_guard_edge_ids") == EXPECTED_GUARD_EDGE_IDS)
    partition = expanded.get("internal_transition_edge_ids", []) + expanded.get("closure_edge_ids", []) + expanded.get("contract_exit_edge_ids", []) + expanded.get("non_domain_firewall_edge_ids", []) + expanded.get("governance_guard_edge_ids", [])
    check("expanded_edge_partition_exact", set(partition) == set(EXPECTED_EXPANDED_EDGE_IDS) and len(partition) == len(set(partition)) == len(EXPECTED_EXPANDED_EDGE_IDS))

    records = bridge.get("expanded_edge_records", [])
    tuples = [(row.get("edge_id"), row.get("from"), row.get("to"), row.get("edge_kind")) for row in records]
    check("expanded_edge_records_exact", tuples == EXPECTED_EXPANDED_EDGE_TUPLES and all(set(row) == {"edge_id", "from", "to", "edge_kind"} for row in records))
    by_edge = {row.get("edge_id"): row for row in records}
    ranks = bridge.get("expanded_node_rank", {})
    check("expanded_rank_exact_domain", list(ranks) == EXPECTED_EXPANDED_NODE_IDS and all(isinstance(value, int) for value in ranks.values()))
    check("expanded_all_edges_strict_rank", all(row.get("from") in ranks and row.get("to") in ranks and ranks[row["from"]] < ranks[row["to"]] for row in records))

    expected_node_projection = {"N00": "AUX_CONTRACT_ROOT"}
    expected_node_projection.update({node: "N35_OBJECT_FIREWALL" for node in ("N35F", "N35P", "N35S", "N35H", "N35Q", "N35D", "N35B")})
    expected_node_projection.update({node: "N36_CELLULAR_CANCELLATION" for node in ("N36F", "N36G")})
    expected_node_projection.update({node: "N37_COEFFICIENT_SATURATION" for node in ("N37O", "N37D", "N37N")})
    expected_node_projection.update({node: "N38_TREE_ORBITAL_TRILEMMA" for node in ("N38T", "N38M", "N38L", "N38O", "N38K")})
    expected_node_projection.update({"NX": "AUX_NONMEMBERSHIP_SINK", "NC": "N39_AFFINE_BRANCH_CLOSED", "NR": "N_REGISTRY_HANDOFF", "NS": "AUX_EMPTY_REGISTRY_FALLBACK"})
    check("node_projection_exact_fibers", bridge.get("node_projection") == expected_node_projection)
    expected_edge_projection = {"E00a": "AUX_SPINE_ENTRY", "E00b": "AUX_SPINE_ENTRY"}
    expected_edge_projection.update({edge: "COLLAPSE_AT:N35_OBJECT_FIREWALL" for edge in ("E01", "E02", "E03", "E04a", "E04b")})
    expected_edge_projection.update({"E05": "E35_36", "E06": "COLLAPSE_AT:N36_CELLULAR_CANCELLATION", "E07": "E36_37", "E08": "COLLAPSE_AT:N37_COEFFICIENT_SATURATION", "E09": "COLLAPSE_AT:N37_COEFFICIENT_SATURATION", "E10": "E37_38"})
    expected_edge_projection.update({edge: "COLLAPSE_AT:N38_TREE_ORBITAL_TRILEMMA" for edge in ("E11", "E12", "E13", "E14")})
    expected_edge_projection.update({edge: "E38_CLOSE" for edge in ("E15", "E16", "E17", "E18", "E19")})
    expected_edge_projection.update({edge: "AUX_CONTRACT_EXIT" for edge in ("E20", "E21", "E23")})
    expected_edge_projection["E22"] = "AUX_NON_DOMAIN_FIREWALL"
    expected_edge_projection.update({"E24": "E_CLOSE_REGISTRY", "E25": "AUX_EMPTY_REGISTRY_FALLBACK"})
    check("edge_projection_exact_fibers", bridge.get("edge_projection") == expected_edge_projection)
    check("projection_structural_surjective", set(structural.get("node_ids", [])) <= set(expected_node_projection.values()) and set(structural.get("edge_ids", [])) <= set(expected_edge_projection.values()))

    paths = bridge.get("expanded_provenance_paths", {})
    expected_path_ids = ["P_N35F", "P_N35P", "P_N35S", "P_N35H", "P_N35Q", "P_N35D", "P_N35B", "P_N36F", "P_N36G", "P_N37O", "P_N37D", "P_N37N", "P_N38T", "P_N38M", "P_N38L", "P_N38O", "P_N38K", "P_NX_E20", "P_NX_E21", "P_NX_E23"]
    check("provenance_path_ids_exact", list(paths) == expected_path_ids)
    path_ok = True
    used_path_edges: set[str] = set()
    for row in paths.values():
        edge_ids = row.get("edge_ids", [])
        used_path_edges.update(edge_ids)
        path_ok = path_ok and row.get("start") == "N00" and bool(edge_ids) and all(edge_id in by_edge for edge_id in edge_ids)
        if edge_ids and all(edge_id in by_edge for edge_id in edge_ids):
            path_ok = path_ok and by_edge[edge_ids[0]].get("from") == row.get("start") and by_edge[edge_ids[-1]].get("to") == row.get("end")
            path_ok = path_ok and all(by_edge[left].get("to") == by_edge[right].get("from") for left, right in zip(edge_ids, edge_ids[1:]))
    check("provenance_paths_contiguous", path_ok)
    check("internal_tags_covered_by_paths", set(EXPECTED_INTERNAL_EDGE_IDS) <= used_path_edges)

    endpoints = bridge.get("endpoint_classification", {})
    check("endpoint_classifier_total_exact", list(endpoints) == EXPECTED_EXPANDED_NODE_IDS and all(set(row) == {"classification", "failed_good_coordinates", "terminal_code"} for row in endpoints.values()))
    good_coordinates = {"I", "R", "S", "D", "M", "C"}
    obstructed_endpoints = [node for node, row in endpoints.items() if row.get("classification") == "OBSTRUCTED"]
    check("obstruction_endpoint_count_17", len(obstructed_endpoints) == 17)
    check("obstruction_endpoints_nonempty_good_failure", all(row.get("failed_good_coordinates") and set(row["failed_good_coordinates"]) <= good_coordinates and len(row["failed_good_coordinates"]) == len(set(row["failed_good_coordinates"])) for row in endpoints.values() if row.get("classification") == "OBSTRUCTED"))
    check("exit_not_obstruction_evidence", endpoints.get("NX", {}).get("classification") == "EXIT" and endpoints.get("NX", {}).get("failed_good_coordinates") == [] and all(row.get("failed_good_coordinates") == [] for row in endpoints.values() if row.get("classification") != "OBSTRUCTED"))

    repair_classes = [row.get("repair_class") for row in contract.get("repair_mappings", [])]
    tokens = bridge.get("request_tokens", [])
    token_ids = [row.get("token_id") for row in tokens]
    check("request_token_ids_exact_order_unique", token_ids == EXPECTED_REQUEST_TOKEN_IDS and len(token_ids) == len(set(token_ids)))
    check("request_token_schema_exact", all(set(row) == TOKEN_KEYS for row in tokens))
    check("request_token_no_catch_all", all("OTHER_INSTANCE" not in json.dumps(row, ensure_ascii=False).upper() for row in tokens))
    token_by_id = {row.get("token_id"): row for row in tokens}
    token_totality = True
    for token in tokens:
        token_id = token.get("token_id", "UNKNOWN")
        obstruction_nodes = token.get("obstruction_endpoint_ids", [])
        boundary_nodes = token.get("boundary_comparison_endpoint_ids", [])
        exit_nodes = token.get("exit_endpoint_ids", [])
        obstruction_edges = token.get("obstruction_edge_ids", [])
        boundary_edges = token.get("boundary_comparison_edge_ids", [])
        exit_edges = token.get("exit_edge_ids", [])
        all_lists_unique = all(isinstance(token.get(field), list) and len(token[field]) == len(set(token[field])) for field in TOKEN_KEYS if field.endswith("_ids") or field == "terminal_codes")
        check(f"token:{token_id}:unique_lists", all_lists_unique)
        check(f"token:{token_id}:scope_class", isinstance(token.get("instance_scope"), str) and bool(token["instance_scope"]) and token.get("repair_class") in repair_classes)
        roles_ok = all(endpoints.get(node, {}).get("classification") == "OBSTRUCTED" and endpoints.get(node, {}).get("failed_good_coordinates") for node in obstruction_nodes)
        roles_ok = roles_ok and all(endpoints.get(node, {}).get("classification") == "OBSTRUCTED" for node in boundary_nodes)
        roles_ok = roles_ok and all(endpoints.get(node, {}).get("classification") == "EXIT" and endpoints.get(node, {}).get("failed_good_coordinates") == [] for node in exit_nodes)
        check(f"token:{token_id}:endpoint_roles", roles_ok)
        edge_roles_ok = all(edge in by_edge and by_edge[edge].get("to") in obstruction_nodes for edge in obstruction_edges)
        edge_roles_ok = edge_roles_ok and all(edge in by_edge and by_edge[edge].get("to") in boundary_nodes for edge in boundary_edges)
        edge_roles_ok = edge_roles_ok and all(edge in by_edge and by_edge[edge].get("to") in exit_nodes for edge in exit_edges)
        check(f"token:{token_id}:edge_roles", edge_roles_ok)
        disposition_ok = (token.get("disposition") == "OBSTRUCTED" and bool(obstruction_nodes) and not exit_nodes) or (token.get("disposition") == "EXIT" and bool(exit_nodes) and not obstruction_nodes)
        check(f"token:{token_id}:disposition", disposition_ok)
        token_paths = [paths.get(path_id, {}) for path_id in token.get("classification_provenance_path_ids", [])]
        path_endpoints = [row.get("end") for row in token_paths]
        expected_terminal_nodes = obstruction_nodes + exit_nodes
        path_terminal_ok = bool(token_paths) and path_endpoints == expected_terminal_nodes and token.get("terminal_codes") == [endpoints.get(node, {}).get("terminal_code") for node in expected_terminal_nodes]
        check(f"token:{token_id}:path_terminal", path_terminal_ok)
        token_totality = token_totality and roles_ok and edge_roles_ok and disposition_ok and path_terminal_ok
    check("request_token_endpoint_obstruction_totality", token_totality)
    check("request_token_census_8_8", [sum(row.get("disposition") == value for row in tokens) for value in ("OBSTRUCTED", "EXIT")] == [8, 8])

    coverage = bridge.get("repair_class_coverage", [])
    check("bridge_repair_coverage_exact_order", [row.get("repair_class") for row in coverage] == repair_classes and all(set(row) == COVERAGE_KEYS for row in coverage))
    contract_dispositions = {row.get("repair_class"): row.get("disposition") for row in contract.get("repair_mappings", [])}
    internal_covered: set[str] = set()
    for row in coverage:
        repair_class = row.get("repair_class", "UNKNOWN")
        class_tokens = [token_by_id.get(token_id, {}) for token_id in row.get("request_token_ids", [])]
        check(f"coverage:{repair_class}:token_exact", row.get("request_token_ids") == [token.get("token_id") for token in tokens if token.get("repair_class") == repair_class] and all(token.get("repair_class") == repair_class for token in class_tokens))
        check(f"coverage:{repair_class}:disposition_exact", row.get("disposition") == contract_dispositions.get(repair_class))
        expected_token_dispositions = {"OBSTRUCTED": ["OBSTRUCTED"], "OUT_OF_CONTRACT_CATEGORY_CHANGE": ["EXIT"], "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT": ["OBSTRUCTED", "EXIT"]}.get(row.get("disposition"), [])
        check(f"coverage:{repair_class}:token_dispositions", [token.get("disposition") for token in class_tokens] == expected_token_dispositions)
        for field in ("obstruction_endpoint_ids", "obstruction_edge_ids", "boundary_comparison_endpoint_ids", "boundary_comparison_edge_ids", "exit_endpoint_ids", "exit_edge_ids"):
            union: list[str] = []
            for token in class_tokens:
                for value in token.get(field, []):
                    if value not in union:
                        union.append(value)
            check(f"coverage:{repair_class}:{field}", row.get(field) == union)
        internal_covered.update(row.get("obstruction_edge_ids", []))
        internal_covered.update(row.get("boundary_comparison_edge_ids", []))
    check("all_internal_tags_classified", internal_covered == set(EXPECTED_INTERNAL_EDGE_IDS))
    token_exit_coverage = {edge for token in tokens for edge in token.get("exit_edge_ids", [])}
    class_exit_coverage = {edge for row in coverage for edge in row.get("exit_edge_ids", [])}
    check("token_contract_exits_exact", token_exit_coverage == class_exit_coverage == set(EXPECTED_EXIT_EDGE_IDS))

    firewalls = bridge.get("non_domain_firewall_edges", [])
    firewall_keys = {"edge_id", "from", "to", "role", "domain_membership", "source_authority", "exact_scope", "request_token_ids", "repair_class_coverage_ids", "historical_boundary_path", "coverage_use", "terminal_code"}
    check("non_domain_firewall_single_exact_schema", len(firewalls) == 1 and set(firewalls[0]) == firewall_keys)
    firewall = firewalls[0] if len(firewalls) == 1 else {}
    p37 = next(spec for spec in input_lock.get("papers", []) if spec.get("paper_id") == "P37")
    check("firewall_exact_typing", firewall.get("edge_id") == "E22" and firewall.get("from") == "N37N" and firewall.get("to") == "NX" and by_edge.get("E22", {}).get("edge_kind") == "AUXILIARY_NON_DOMAIN_FIREWALL")
    check("firewall_outside_exact_universe", firewall.get("domain_membership") == "OUTSIDE_EXACT_A14_REPAIR_TAGS_AND_SIGMA16_REQUEST_TOKENS" and firewall.get("coverage_use") == "EXCLUDED_FROM_A14_SIGMA16_AND_ENDPOINT_OBSTRUCTION_EXHAUSTIVENESS")
    check("firewall_empty_coverage_fibers", firewall.get("request_token_ids") == [] and firewall.get("repair_class_coverage_ids") == [])
    check("firewall_source_authority", firewall.get("source_authority") == {"p37_source_lock_sha256": p37.get("files", {}).get("SOURCE_LOCK.md"), "p37_round2_clues_sha256": p37.get("files", {}).get("ROUND2_CLUES.md")})
    firewall_path = firewall.get("historical_boundary_path", {})
    firewall_path_edges = firewall_path.get("edge_ids", [])
    firewall_canonical = f"{firewall_path.get('path_id')}|{firewall_path.get('start')}|{','.join(firewall_path_edges)}|{firewall_path.get('end')}"
    firewall_path_ok = set(firewall_path) == {"path_id", "canonical_string", "sha256", "start", "edge_ids", "end"} and firewall_path.get("path_id") == "H_NX_E22" and firewall_path.get("start") == "N00" and firewall_path.get("end") == "NX" and firewall_path_edges and firewall_path_edges[-1] == "E22" and all(edge in by_edge for edge in firewall_path_edges)
    firewall_path_ok = firewall_path_ok and firewall_path.get("canonical_string") == firewall_canonical and firewall_path.get("sha256") == hashlib.sha256(firewall_canonical.encode("utf-8")).hexdigest() == "1231fe11f42c13ec3a7925d68d89f066b1deb2460f57924ecb76dd3d3490850a"
    if firewall_path_ok:
        firewall_path_ok = by_edge[firewall_path_edges[0]].get("from") == "N00" and by_edge[firewall_path_edges[-1]].get("to") == "NX" and all(by_edge[left].get("to") == by_edge[right].get("from") for left, right in zip(firewall_path_edges, firewall_path_edges[1:]))
    check("firewall_historical_path", firewall_path_ok)
    all_coverage_edges = {edge for token in tokens for field in ("obstruction_edge_ids", "boundary_comparison_edge_ids", "exit_edge_ids") for edge in token.get(field, [])}
    all_coverage_edges.update(edge for row in coverage for field in ("obstruction_edge_ids", "boundary_comparison_edge_ids", "exit_edge_ids") for edge in row.get(field, []))
    check("firewall_zero_a14_sigma16_credit", "E22" not in all_coverage_edges and endpoints.get("NX", {}).get("failed_good_coordinates") == [] and firewall.get("terminal_code") == endpoints.get("NX", {}).get("terminal_code"))

    check("realized_guard_exact", bridge.get("realized_guard") == {"expanded_edge_id": "E24", "structural_spine_edge_id": "E_CLOSE_REGISTRY", "terminal": "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY"})
    check("conditional_guard_exact", bridge.get("conditional_guard") == {"expanded_edge_id": "E25", "structural_spine_projection": "AUX_EMPTY_REGISTRY_FALLBACK", "terminal": "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR", "realized": False})
    terminology_blob = json.dumps(bridge.get("terminology", {}), ensure_ascii=False).lower()
    check("terminology_no_reflexive_termination_claim", "reflexive" not in terminology_blob and "operational termination" not in terminology_blob and "semantic-terminal reachability" not in terminology_blob)
    check("terminology_retrospective_encoding_exact", bridge.get("terminology", {}).get("encoding_timing") == "The 14-class/16-token/Good encoding is a retrospective Paper-39 construction assembled from hashed P35-P38 artifacts after predecessor outcomes were known and frozen before the Paper-39 checker; only literal predecessor fields and the P38 prohibition list are called predecessor-frozen.")
    losslessness = bridge.get("losslessness", {})
    check("losslessness_artifact_retention_only", isinstance(losslessness.get("meaning"), str) and "not claim that the projection is injective or invertible" in losslessness["meaning"] and all(value is True for key, value in losslessness.items() if key != "meaning"))

    p38 = next(spec for spec in input_lock.get("papers", []) if spec.get("paper_id") == "P38")
    criterion = bridge.get("criterion_provenance", {})
    predecessor_source_locks = {
        f"{paper['paper_id']}_{paper['candidate_id']}": paper.get("files", {}).get("SOURCE_LOCK.md")
        for paper in input_lock.get("papers", [])
    }
    check("bridge_criterion_provenance", criterion == {
        "route_a_evaluator_sha256": input_lock.get("route_a_evaluator", {}).get("sha256"),
        "p38_source_lock_sha256": p38.get("files", {}).get("SOURCE_LOCK.md"),
        "p38_round2_clues_sha256": p38.get("files", {}).get("ROUND2_CLUES.md"),
        "predecessor_source_lock_sha256": predecessor_source_locks,
        "freeze_timing": "RETROSPECTIVE_P35_P38_OUTCOMES_KNOWN_FROZEN_BEFORE_P39_CHECKER",
    })
    good_field_map = bridge.get("good_field_map", {})
    expected_good_field_map = {
        "I": ["A0.arithmetic_origin", "source_lock.allowed_data", "source_lock.forbidden_data", "source_lock.parameter_provenance"],
        "R": ["A1.primitive_ledger", "A1.repetition_semantics", "source_lock.object", "source_lock.dynamics", "source_lock.clock"],
        "S": ["A0.arithmetic_sector", "A1.arithmetic_selectivity", "adversarial_controls.generic_and_composite"],
        "D": ["A2.operator_object", "A2.determinant_convention", "source_lock.regularization_order"],
        "M": ["source_lock.clock", "source_lock.main_theorem_marker", "source_lock.normalization"],
        "C": ["adversarial_controls", "proves_too_much_risk", "blocking_conditions", "stop_rule"],
    }
    check("bridge_good_field_map", good_field_map == expected_good_field_map)
    return {
        "bridge_sha256": bridge_sha256,
        "counts": counts,
        "edge_projection": bridge.get("edge_projection"),
        "endpoint_classification": endpoints,
        "node_projection": bridge.get("node_projection"),
        "non_domain_firewall_edges": firewalls,
        "repair_class_coverage": coverage,
        "request_tokens": tokens,
        "terminology": bridge.get("terminology"),
    }


def evidence_blob(record: dict[str, Any]) -> str:
    values: list[str] = []
    for key in (
        "blocking_conditions",
        "determinant_convention",
        "forbidden_repairs",
        "main_theorem_marker",
        "next_smallest_test",
        "normalization",
        "object",
        "operator_ownership",
        "round2_clues",
        "strongest_failures",
        "terminal_codes",
    ):
        values.append(json.dumps(record.get(key), ensure_ascii=False, sort_keys=True))
    for item in record.get("repair_alphabet", []):
        values.append(item.get("raw", ""))
    return " ".join(values).lower()


def evaluate(packet: dict[str, Any], contract: dict[str, Any], input_lock: dict[str, Any], empty_fixture: dict[str, Any], empty_fixture_sha256: str, dag_bridge: dict[str, Any], dag_bridge_sha256: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool) -> None:
        checks.append({"name": name, "passed": bool(condition)})

    check("packet_schema", packet.get("schema") == "paper39-source-packet-v1")
    check("contract_schema", contract.get("schema") == "paper39-affine-closure-contract-v1")
    check("input_lock_schema", input_lock.get("schema") == "paper39-input-lock-v1")
    check("finite_contract_scope", packet.get("candidate_contract_scope") == "FINITE_FROZEN_P35_P38_REPAIR_ALPHABET_ONLY")
    check("no_universal_no_go", packet.get("universal_affine_no_go_claimed") is False and contract.get("universal_affine_no_go_claimed") is False)
    check("source_evaluator_separated", packet.get("source_evaluator_separated") is True)
    preregistration_semantics = contract.get("preregistration_semantics", {})
    check("retrospective_preregistration_exact", preregistration_semantics == EXPECTED_PREREGISTRATION_SEMANTICS and packet.get("preregistration_semantics") == preregistration_semantics)
    check("predecessor_outcomes_known", preregistration_semantics.get("predecessor_outcomes_known_when_encoded") is True)
    check("no_predecessor_result_independence_claim", preregistration_semantics.get("independent_of_predecessor_results_claimed") is False)
    check("checker_only_freeze_boundary", preregistration_semantics.get("checker_inputs_frozen_before_checker_run") is True and "NOT_BEFORE_PREDECESSOR_OUTCOMES" in preregistration_semantics.get("freeze_boundary", ""))
    route_lock = input_lock.get("route_a_evaluator", {})
    route_path = Path(route_lock.get("absolute_path", ""))
    route_text = route_path.read_text(encoding="utf-8") if route_path.is_file() else ""
    good_map = route_lock.get("good_conjunct_criterion_map", [])
    packet_route = packet.get("route_a_evaluator_provenance", {})
    check("route_a_evaluator_hash_current", route_path.is_file() and digest(route_path) == route_lock.get("sha256") == "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a")
    check("route_a_evaluator_v02", route_lock.get("skill_version") == "0.2.0" and "**Version:** `0.2.0`" in route_text)
    check("good_conjunct_map_exact", [row.get("good_conjunct") for row in good_map] == ["I", "R", "S", "D", "M", "C"] and {row.get("good_conjunct"): row.get("meaning") for row in good_map} == EXPECTED_GOOD_MEANINGS)
    check("good_conjunct_map_criteria_nonempty", all(row.get("criterion_ids") and len(row.get("criterion_ids")) == len(set(row.get("criterion_ids"))) for row in good_map))
    check("good_conjunct_map_authority_anchors", all(anchor in route_text for row in good_map for anchor in row.get("required_anchor_substrings", [])) and all(row.get("required_anchor_substrings") for row in good_map))
    check("route_a_provenance_packet_exact", packet_route == {**route_lock, "current_hash_verified": True})
    expanded_summary = validate_expanded_bridge(dag_bridge, dag_bridge_sha256, contract, input_lock, check)
    fixture_lock = contract.get("empty_registry_fixture", {})
    fixture_rows = empty_fixture.get("rows", [])
    fixture_non_affine = sum(
        row.get("source_locked") is True and row.get("branch_class") == contract.get("registry", {}).get("branch_class")
        for row in fixture_rows
    )
    fixture_terminal = contract["realized_terminal"] if fixture_non_affine else contract["conditional_empty_registry_terminal"]
    check("empty_fixture_hash_locked", empty_fixture_sha256 == fixture_lock.get("sha256"))
    check("empty_fixture_schema", empty_fixture.get("schema") == "paper39-empty-registry-fixture-v1")
    check("empty_fixture_exact_empty", fixture_rows == [] and empty_fixture.get("source_locked_non_affine_count") == 0)
    check("empty_fixture_branch_executed", fixture_terminal == empty_fixture.get("expected_terminal") == contract["conditional_empty_registry_terminal"])
    check("empty_fixture_independent_from_live_history", empty_fixture.get("chronology_basis") == "independent_synthetic_empty_fixture_not_live_registry_history")

    records = packet.get("paper_records", [])
    record_by_id = {record.get("paper_id"): record for record in records}
    specs = input_lock.get("papers", [])
    check("paper_record_exact_order", [record.get("paper_id") for record in records] == ["P35", "P36", "P37", "P38"])
    check("paper_record_exact_set", set(record_by_id) == {"P35", "P36", "P37", "P38"} and len(records) == 4)

    for spec in specs:
        paper_id = spec["paper_id"]
        record = record_by_id.get(paper_id, {})
        check(f"{paper_id}:candidate_id", record.get("candidate_id") == spec["candidate_id"])
        check(f"{paper_id}:artifact_commit", record.get("artifact_commit") == spec["artifact_commit"])
        check(f"{paper_id}:sealed_provenance", record.get("sealed_provenance_triple") == [spec["artifact_commit"]] * 3)
        check(f"{paper_id}:input_hashes", record.get("input_hashes") == spec["files"])
        check(f"{paper_id}:route_tuple", record.get("route_tuple") == EXPECTED_TUPLES[paper_id])
        check(f"{paper_id}:overall_rejected", record.get("overall_verdict") == "ROUTE_A_REJECTED")
        check(f"{paper_id}:route_b_locked", record.get("route_b_invocation_allowed") is False)
        check(f"{paper_id}:obligation_nonempty", isinstance(record.get("next_smallest_test"), str) and len(record.get("next_smallest_test", "")) > 40)
        check(f"{paper_id}:obstructions_nonempty", len(record.get("blocking_conditions", [])) >= 5)
        check(f"{paper_id}:forbidden_repairs_nonempty", len(record.get("forbidden_repairs", [])) >= 5)
        ownership = record.get("operator_ownership", {})
        check(
            f"{paper_id}:operator_ownership_typed",
            ownership.get("operator_object") == record.get("object")
            and ownership.get("determinant_convention") == record.get("determinant_convention")
            and isinstance(ownership.get("regularization_order"), str)
            and bool(ownership.get("regularization_order")),
        )
        check(f"{paper_id}:terminal_codes_normalized", record.get("terminal_codes") == record.get("terminal_evidence", {}).get("codes") and bool(record.get("terminal_codes")))
        typed = record.get("typed_normalization", {})
        check(
            f"{paper_id}:typed_normalization_exact",
            typed
            == {
                "forbidden_repairs": record.get("forbidden_repairs"),
                "inherited_obligation": record.get("next_smallest_test"),
                "marker": record.get("main_theorem_marker"),
                "object": record.get("object"),
                "obstructions": {"blocking_conditions": record.get("blocking_conditions"), "strongest_failures": record.get("strongest_failures")},
                "operator_ownership": record.get("operator_ownership"),
                "terminal_codes": record.get("terminal_codes"),
            },
        )
        for field, phrases in RAW_REQUIREMENTS[paper_id].items():
            raw = str(record.get(field, "")).lower()
            check(f"{paper_id}:{field}_typed", all(phrase.lower() in raw for phrase in phrases))

    witness_catalog = contract.get("witness_catalog", [])
    witness_codes = [row.get("code") for row in witness_catalog]
    obstruction_code_universe = contract.get("required_obstruction_witness_codes", [])
    boundary_code_universe = contract.get("required_boundary_exit_witness_codes", [])
    required_witnesses = obstruction_code_universe + boundary_code_universe
    check("witness_catalog_exact_set", set(witness_codes) == set(required_witnesses) and len(witness_codes) == len(set(witness_codes)))
    check("witness_kind_universes_disjoint", len(obstruction_code_universe) == len(set(obstruction_code_universe)) and len(boundary_code_universe) == len(set(boundary_code_universe)) and not (set(obstruction_code_universe) & set(boundary_code_universe)))
    verified_witnesses: dict[str, bool] = {}
    for witness in witness_catalog:
        paper_id = witness.get("paper_id")
        blob = evidence_blob(record_by_id.get(paper_id, {}))
        passed = all(str(phrase).lower() in blob for phrase in witness.get("evidence_contains", []))
        verified_witnesses[witness["code"]] = passed
        check(f"witness:{witness['code']}", passed)

    repair_packet = record_by_id.get("P38", {}).get("repair_alphabet", [])
    repair_contract = contract.get("repair_mappings", [])
    packet_classes = [row.get("repair_class") for row in repair_packet]
    contract_classes = [row.get("repair_class") for row in repair_contract]
    check("repair_alphabet_14", len(packet_classes) == 14)
    check("repair_alphabet_exact_set", packet_classes == contract_classes and len(set(packet_classes)) == 14)
    repair_rows: list[dict[str, Any]] = []
    for mapping in repair_contract:
        obstruction_witnesses = mapping.get("obstruction_witness_codes", [])
        boundary_witnesses = mapping.get("boundary_exit_witness_codes", [])
        check(f"repair_witness_kinds:{mapping['repair_class']}", set(obstruction_witnesses) <= set(obstruction_code_universe) and set(boundary_witnesses) <= set(boundary_code_universe))
        obstruction_passed = all(verified_witnesses.get(code, False) for code in obstruction_witnesses)
        boundary_passed = all(verified_witnesses.get(code, False) for code in boundary_witnesses)
        passed = bool(obstruction_witnesses or boundary_witnesses) and obstruction_passed and boundary_passed
        check(f"repair_classified:{mapping['repair_class']}", passed)
        status_tuple = (mapping.get("canonical_tested"), mapping.get("alternative_instances_exit"))
        expected_disposition = {
            (True, False): "OBSTRUCTED",
            (False, True): "OUT_OF_CONTRACT_CATEGORY_CHANGE",
            (True, True): "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT",
        }.get(status_tuple)
        check(
            f"repair_disposition:{mapping['repair_class']}",
            expected_disposition is not None
            and mapping.get("disposition") == expected_disposition
            and (mapping.get("disposition") != "OBSTRUCTED" or (bool(obstruction_witnesses) and not boundary_witnesses))
            and (mapping.get("disposition") != "OUT_OF_CONTRACT_CATEGORY_CHANGE" or (not obstruction_witnesses and bool(boundary_witnesses)))
            and (mapping.get("disposition") != "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT" or (bool(obstruction_witnesses) and bool(boundary_witnesses))),
        )
        repair_rows.append({
            **mapping,
            "boundary_exit_evidence_verified": boundary_passed,
            "evidence_verified": passed,
            "obstruction_evidence_verified": obstruction_passed,
        })
    disposition_order = ["OBSTRUCTED", "OUT_OF_CONTRACT_CATEGORY_CHANGE", "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT"]
    disposition_census = {name: sum(row.get("disposition") == name for row in repair_contract) for name in disposition_order}
    check("repair_disposition_census_6_6_2", [disposition_census[name] for name in disposition_order] == [6, 6, 2])
    check("contract_relative_exhaustiveness_explicit", "No claim is made" in contract.get("exhaustiveness_statement", ""))

    contract_edges = contract.get("edges", [])
    packet_edges = packet.get("declared_edges", [])
    check("edge_exact_ids", [row.get("edge_id") for row in packet_edges] == [row.get("edge_id") for row in contract_edges])
    check("edge_count_5", len(packet_edges) == len(contract_edges) == 5)
    node_ids = {node.get("node_id") for node in contract.get("nodes", [])}
    node_sequence = [node.get("node_id") for node in contract.get("nodes", [])]
    node_by_id = {node.get("node_id"): node for node in contract.get("nodes", [])}
    check("p38_object_code_narrow_exact", node_by_id.get("N38_TREE_ORBITAL_TRILEMMA", {}).get("object_code") == EXPECTED_P38_OBJECT_CODE and "PRESENTATION_CANONICAL_BASS_SERRE_FULL_EDGE_SHIFT" not in json.dumps(contract, ensure_ascii=False))
    check("dag_acyclic", graph_is_acyclic(node_ids, contract_edges))
    check("dag_total_single_chain", [edge.get("from") for edge in contract_edges] == node_sequence[:-1] and [edge.get("to") for edge in contract_edges] == node_sequence[1:])
    e36_contract = next((edge for edge in contract_edges if edge.get("edge_id") == "E36_37"), {})
    e36_packet = next((edge for edge in packet_edges if edge.get("edge_id") == "E36_37"), {})
    p36_spec = next(spec for spec in input_lock.get("papers", []) if spec.get("paper_id") == "P36")
    p37_spec = next(spec for spec in input_lock.get("papers", []) if spec.get("paper_id") == "P37")
    transfer_constraint = dag_bridge.get("projection_transfer_constraints", {}).get("E36_37", {})
    check(
        "e36_37_nonstate_audit_metadata_binding",
        e36_contract.get("from") == "N36_CELLULAR_CANCELLATION"
        and e36_contract.get("to") == "N37_COEFFICIENT_SATURATION"
        and e36_contract.get("inherited_obligation_source") == "P36.next_smallest_test"
        and e36_packet.get("inherited_obligation") == record_by_id.get("P36", {}).get("next_smallest_test")
        and transfer_constraint.get("carry_fields") == ["inherited_obligation", "historical_provenance"]
        and transfer_constraint.get("expanded_authority_edge_id") == "E07"
        and transfer_constraint.get("reset_authority_sha256") == p37_spec.get("files", {}).get("SOURCE_LOCK.md")
        and record_by_id.get("P36", {}).get("input_hashes") == p36_spec.get("files")
        and record_by_id.get("P37", {}).get("input_hashes") == p37_spec.get("files")
        and record_by_id.get("P36", {}).get("sealed_provenance_triple") == [p36_spec.get("artifact_commit")] * 3
        and record_by_id.get("P37", {}).get("sealed_provenance_triple") == [p37_spec.get("artifact_commit")] * 3,
    )
    check("node_full_typed_schema", all(
        bool(node.get("inherited_obligation_source"))
        and bool(node.get("forbidden_escape_source"))
        and isinstance(node.get("obstruction_codes"), list)
        and isinstance(node.get("boundary_exit_codes"), list)
        and bool(node.get("obstruction_codes") or node.get("boundary_exit_codes"))
        for node in contract.get("nodes", [])
    ))
    raw_node_types = {
        "N35_OBJECT_FIREWALL": {"determinant_owner": record_by_id["P35"]["determinant_convention"], "marker": record_by_id["P35"]["main_theorem_marker"], "object": record_by_id["P35"]["object"], "operator_owner": record_by_id["P35"]["operator_ownership"]},
        "N36_CELLULAR_CANCELLATION": {"determinant_owner": record_by_id["P36"]["determinant_convention"], "marker": record_by_id["P36"]["main_theorem_marker"], "object": record_by_id["P36"]["object"], "operator_owner": record_by_id["P36"]["operator_ownership"]},
        "N37_COEFFICIENT_SATURATION": {"determinant_owner": record_by_id["P37"]["determinant_convention"], "marker": record_by_id["P37"]["main_theorem_marker"], "object": record_by_id["P37"]["object"], "operator_owner": record_by_id["P37"]["operator_ownership"]},
        "N38_TREE_ORBITAL_TRILEMMA": {"determinant_owner": record_by_id["P38"]["determinant_convention"], "marker": record_by_id["P38"]["main_theorem_marker"], "object": record_by_id["P38"]["object"], "operator_owner": record_by_id["P38"]["operator_ownership"]},
        "N39_AFFINE_BRANCH_CLOSED": {"determinant_owner": "NO_NEW_DETERMINANT_AUDIT_ONLY", "marker": "NO_NEW_MARKER_AUDIT_ONLY", "object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM", "operator_owner": {"determinant_convention": "NO_NEW_DETERMINANT_AUDIT_ONLY", "operator_object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM", "regularization_order": "AUDIT_ONLY_NOT_APPLICABLE"}},
        "N_REGISTRY_HANDOFF": {"determinant_owner": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "marker": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY", "operator_owner": {"determinant_convention": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "operator_object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY", "regularization_order": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY"}},
    }
    node_code_fields = {"determinant_owner": "determinant_code", "marker": "marker_code", "object": "object_code", "operator_owner": "operator_owner_code"}
    transfer_semantics = contract.get("transfer_semantics_contract", {})
    check("transfer_mode_enum_closed", transfer_semantics.get("allowed_modes") == ["CARRY_IDENTICAL", "CARRY_WITH_EQUIVALENCE", "RESET", "EXIT"])
    check("reset_authority_bindings_exact", transfer_semantics.get("reset_authority_bindings") == EXPECTED_RESET_BINDINGS)
    check("equivalence_bindings_exact", transfer_semantics.get("equivalence_bindings") == EXPECTED_EQUIVALENCE_BINDINGS and transfer_semantics.get("equivalence_ids") == [])
    check("e36_37_identity_non_inheritance_exact", transfer_semantics.get("non_inheritance_assertions") == EXPECTED_NON_INHERITANCE_ASSERTIONS and all(transfer_semantics.get("reset_authority_bindings", {}).get("E36_37", {}).get(field) == "P37_SOURCE_LOCK_SD_C39" for field in ("object", "marker", "operator_owner", "determinant_owner")))
    check("exit_semantics_non_obstruction", transfer_semantics.get("exit_semantics") == "CLASSIFICATION_NONMEMBERSHIP_ONLY_NEVER_OBSTRUCTION_EVIDENCE_AND_NOT_A_STRUCTURAL_SPINE_FIELD_TRANSFER")
    for expected, observed in zip(contract_edges, packet_edges):
        edge_id = expected["edge_id"]
        check(f"{edge_id}:endpoints", observed.get("from") == expected["from"] and observed.get("to") == expected["to"] and expected["from"] in node_ids and expected["to"] in node_ids)
        check(f"{edge_id}:obligation", isinstance(observed.get("inherited_obligation"), str) and len(observed.get("inherited_obligation", "")) > 40)
        check(f"{edge_id}:obstruction_coverage", all(code in verified_witnesses or code in DERIVED_OBSTRUCTIONS for code in expected.get("obstruction_codes", [])))
        for field, node_field in node_code_fields.items():
            contract_transfer = expected.get("field_transfer", {}).get(field, {})
            packet_transfer = observed.get("field_transfer", {}).get(field, {})
            mode = contract_transfer.get("mode")
            semantic_binding = (
                (mode == "RESET" and contract_transfer.get("reset_authority_id") == EXPECTED_RESET_BINDINGS.get(edge_id, {}).get(field))
                or (mode == "CARRY_WITH_EQUIVALENCE" and contract_transfer.get("equivalence_id") == EXPECTED_EQUIVALENCE_BINDINGS.get(edge_id, {}).get(field))
                or mode == "CARRY_IDENTICAL"
            )
            check(
                f"{edge_id}:{field}_contract_transfer",
                transfer_rule_valid(contract_transfer, "source_code", "target_code", transfer_semantics)
                and contract_transfer.get("source_code") == node_by_id.get(expected.get("from"), {}).get(node_field)
                and contract_transfer.get("target_code") == node_by_id.get(expected.get("to"), {}).get(node_field)
                and semantic_binding,
            )
            expected_packet_transfer = {
                key: value
                for key, value in contract_transfer.items()
                if key not in {"source_code", "target_code"}
            }
            expected_packet_transfer.update({
                "source": raw_node_types.get(expected.get("from"), {}).get(field),
                "target": raw_node_types.get(expected.get("to"), {}).get(field),
            })
            check(
                f"{edge_id}:{field}_packet_transfer",
                packet_transfer == expected_packet_transfer
                and transfer_rule_valid(packet_transfer, "source", "target", transfer_semantics),
            )

    expected_targets = {
        "E35_36": record_by_id.get("P36", {}),
        "E36_37": record_by_id.get("P37", {}),
        "E37_38": record_by_id.get("P38", {}),
    }
    for edge in packet_edges:
        if edge.get("edge_id") in expected_targets:
            target = expected_targets[edge["edge_id"]]
            check(f"{edge['edge_id']}:object_transfer", edge.get("target_object") == target.get("object"))
            check(f"{edge['edge_id']}:marker_transfer", edge.get("target_marker") == target.get("main_theorem_marker"))
            check(f"{edge['edge_id']}:determinant_transfer", edge.get("target_determinant") == target.get("determinant_convention"))
            check(f"{edge['edge_id']}:operator_ownership_transfer", edge.get("target_operator_ownership") == target.get("operator_ownership"))
    expected_terminal_targets = {
        "E38_CLOSE": ("TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM", "NO_NEW_MARKER_AUDIT_ONLY", "NO_NEW_DETERMINANT_AUDIT_ONLY"),
        "E_CLOSE_REGISTRY": ("SESSION4_GLOBAL_CANDIDATE_REGISTRY", "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY"),
    }
    for edge in packet_edges:
        if edge.get("edge_id") in expected_terminal_targets:
            obj, marker, determinant = expected_terminal_targets[edge["edge_id"]]
            check(f"{edge['edge_id']}:typed_target", (edge.get("target_object"), edge.get("target_marker"), edge.get("target_determinant")) == (obj, marker, determinant))
            ownership = edge.get("target_operator_ownership", {})
            check(f"{edge['edge_id']}:operator_ownership_target", ownership.get("operator_object") == obj and ownership.get("determinant_convention") == determinant and bool(ownership.get("regularization_order")))

    base = Path(input_lock["authority_papers_base"])
    registry_spec = input_lock["registry"]
    registry_path = base / registry_spec["candidate_registry_relative"]
    prereg_path = base / registry_spec["preregistration_relative"]
    check("registry_hash_current", digest(registry_path) == registry_spec["candidate_registry_sha256"])
    check("registry_prereg_hash_current", digest(prereg_path) == registry_spec["preregistration_sha256"])
    registry_text = registry_path.read_text(encoding="utf-8")
    prereg_text = prereg_path.read_text(encoding="utf-8")
    prereg_compact = " ".join(prereg_text.split())
    check("registry_exact_title_and_status", "# Session 4 Candidate Registry" in registry_text and "Candidate definitions and stop rules are frozen" in registry_text)
    check("prereg_exact_title_and_status", "# Session 4 Preregistration and Source Lock" in prereg_text and "Status at freeze: candidate definitions frozen; no numerical candidate result inspected" in prereg_compact and "Two objects discovered during the source audit were added before any experiment on either object was run" in prereg_compact)
    independent_rows = independent_registry_parse(registry_text, prereg_text)
    packet_registry = packet.get("registry", {})
    check("registry_rows_independent_parse", packet_registry.get("rows") == independent_rows)
    expected_ids = contract.get("registry", {}).get("expected_ids", [])
    check("registry_exact_ids", [row.get("candidate_id") for row in independent_rows] == expected_ids)
    check("registry_all_source_locked", all(row.get("source_locked") is True for row in independent_rows))
    check("registry_lock_evidence_complete", all(all(row.get("source_lock_evidence", {}).values()) and len(row.get("source_lock_evidence", {})) == 5 for row in independent_rows))
    check("registry_all_non_affine", all(row.get("branch_class") == contract["registry"]["branch_class"] for row in independent_rows))
    non_affine_count = sum(row.get("source_locked") is True and row.get("branch_class") == contract["registry"]["branch_class"] for row in independent_rows)
    realized_terminal = contract["realized_terminal"] if non_affine_count else contract["conditional_empty_registry_terminal"]
    check("registry_nonempty", non_affine_count == 6)
    check("registry_count_packet", packet_registry.get("source_locked_non_affine_count") == non_affine_count)
    check("registry_conditional_terminal", packet_registry.get("realized_terminal") == realized_terminal == contract["realized_terminal"])
    check("registry_chronology_basis", packet_registry.get("chronology_basis") == "trusted_hashed_source_assertion" and packet_registry.get("chronology_evidence_status") == "TRUSTED_HASHED_SOURCE_ASSERTION_NOT_INDEPENDENTLY_ESTABLISHED" and packet_registry.get("preregistration_source_lock_path") == registry_spec["preregistration_relative"])
    mechanism = packet.get("mechanism_creation", {})
    check("zero_new_mechanisms", mechanism.get("new_mechanisms") == [] and contract.get("mechanism_creation_allowed") is False)
    check("no_ranking", mechanism.get("ranking") == [] and contract.get("ranking_allowed") is False)
    check("no_successor_proposal", mechanism.get("successor_proposals") == [] and contract["registry"].get("proposal_allowed") is False)

    terminal_codes_by_paper = {paper_id: set(record.get("terminal_evidence", {}).get("codes", [])) for paper_id, record in record_by_id.items()}
    check("P36:terminal_code", "CLOSE_COMPLETE_AFFINE_CHAIN_QUOTIENT_BRANCH" in terminal_codes_by_paper.get("P36", set()))
    check("P37:terminal_code", "CLOSE_LOCAL_COEFFICIENT_SATURATION_BRANCH" in terminal_codes_by_paper.get("P37", set()))
    check("P38:terminal_codes", {"STOP_BASS_SERRE_TREE_BRANCH", "CLOSE_ENTIRE_AFFINE_BRANCH", "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR"} <= terminal_codes_by_paper.get("P38", set()))
    check("node_operator_owners_typed", all(isinstance(node.get("operator_owner_code"), str) and bool(node.get("operator_owner_code")) for node in contract.get("nodes", [])))

    passed = sum(row["passed"] for row in checks)
    all_pass = passed == len(checks)
    normalized_edges = [{**edge, "passed": all_pass or all(row["passed"] for row in checks if row["name"].startswith(edge["edge_id"] + ":"))} for edge in contract_edges]
    science_projection = {
        "affine_branch": "CLOSE_ENTIRE_AFFINE_BRANCH",
        "contract_relative_exhaustiveness": True,
        "structural_spine_edge_ids": [edge["edge_id"] for edge in contract_edges],
        "empty_registry_fixture_terminal": fixture_terminal,
        "new_mechanism_count": 0,
        "structural_spine_node_ids": [node["node_id"] for node in contract.get("nodes", [])],
        "node_operator_owner_codes": [node["operator_owner_code"] for node in contract.get("nodes", [])],
        "realized_terminal": realized_terminal,
        "registry_ids": expected_ids,
        "repair_classes": contract_classes,
        "repair_boundary_exit_witnesses": {row["repair_class"]: row["boundary_exit_witness_codes"] for row in repair_contract},
        "repair_dispositions": {row["repair_class"]: row["disposition"] for row in repair_contract},
        "repair_disposition_census": disposition_census,
        "repair_obstruction_witnesses": {row["repair_class"]: row["obstruction_witness_codes"] for row in repair_contract},
        "expanded_bridge_sha256": dag_bridge_sha256,
        "expanded_counts": expanded_summary.get("counts"),
        "expanded_edge_ids": EXPECTED_EXPANDED_EDGE_IDS,
        "expanded_node_ids": EXPECTED_EXPANDED_NODE_IDS,
        "request_token_dispositions": {row.get("token_id"): row.get("disposition") for row in expanded_summary.get("request_tokens", [])},
        "request_token_ids": [row.get("token_id") for row in expanded_summary.get("request_tokens", [])],
        "endpoint_obstruction_totality": True,
        "retrospective_encoding_timing": expanded_summary.get("terminology", {}).get("encoding_timing"),
        "retrospective_preregistration_semantics": preregistration_semantics,
        "route_a_evaluator_sha256": route_lock.get("sha256"),
        "route_a_good_conjuncts": [row.get("good_conjunct") for row in good_map],
        "universal_affine_no_go_claimed": False,
    }
    return {
        "all_pass": all_pass,
        "checks": checks,
        "counts": {
            "checks_passed": passed,
            "checks_total": len(checks),
            "expanded_dag_edges": len(EXPECTED_EXPANDED_EDGE_IDS),
            "expanded_dag_nodes": len(EXPECTED_EXPANDED_NODE_IDS),
            "internal_transition_tags": len(EXPECTED_INTERNAL_EDGE_IDS),
            "new_mechanisms": len(mechanism.get("new_mechanisms", [])) if isinstance(mechanism.get("new_mechanisms"), list) else -1,
            "registry_source_locked_non_affine": non_affine_count,
            "repair_classes": len(repair_rows),
            "repair_classes_verified": sum(row["evidence_verified"] for row in repair_rows),
            "request_tokens": len(expanded_summary.get("request_tokens", [])),
            "structural_spine_edges": len(contract_edges),
            "structural_spine_nodes": len(contract.get("nodes", [])),
        },
        "decision": {
            "affine_branch": "CLOSE_ENTIRE_AFFINE_BRANCH",
            "conditional_empty_registry_terminal": contract["conditional_empty_registry_terminal"],
            "empty_registry_fixture_executed_terminal": fixture_terminal,
            "exhaustiveness": "RELATIVE_TO_FROZEN_CANDIDATE_CONTRACT",
            "realized_terminal": realized_terminal,
            "route_b_invocation_allowed": False,
            "universal_affine_no_go_claimed": False,
        },
        "expanded_proof_dag": expanded_summary,
        "registry_classification": independent_rows,
        "repair_coverage": repair_rows,
        "schema": "paper39-closure-evaluation-v1",
        "science_projection": science_projection,
        "science_projection_sha256": hashlib.sha256(canonical_bytes(science_projection)).hexdigest(),
        "structural_spine_edges": normalized_edges,
        "structural_spine_nodes": contract.get("nodes", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", required=True)
    parser.add_argument("--contract", required=True)
    parser.add_argument("--input-lock", required=True)
    parser.add_argument("--empty-registry-fixture", required=True)
    parser.add_argument("--dag-bridge", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    try:
        packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))
        contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
        input_lock = json.loads(Path(args.input_lock).read_text(encoding="utf-8"))
        empty_fixture_path = Path(args.empty_registry_fixture)
        empty_fixture = json.loads(empty_fixture_path.read_text(encoding="utf-8"))
        dag_bridge_path = Path(args.dag_bridge)
        dag_bridge = json.loads(dag_bridge_path.read_text(encoding="utf-8"))
        payload = evaluate(packet, contract, input_lock, empty_fixture, digest(empty_fixture_path), dag_bridge, digest(dag_bridge_path))
        output.write_bytes(canonical_bytes(payload))
        return 0 if payload["all_pass"] else 1
    except Exception as exc:
        output.write_bytes(canonical_bytes({"all_pass": False, "error": f"{type(exc).__name__}:{exc}", "schema": "paper39-closure-evaluation-error-v1"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
