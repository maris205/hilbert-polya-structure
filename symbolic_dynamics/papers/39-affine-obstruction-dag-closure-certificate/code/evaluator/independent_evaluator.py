#!/usr/bin/env python3
"""Second, separately implemented evaluator for the Paper 39 packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from typing import Any


EXPANDED_NODES = ["N00", "N35F", "N35P", "N35S", "N35H", "N35Q", "N35D", "N35B", "N36F", "N36G", "N37O", "N37D", "N37N", "N38T", "N38M", "N38L", "N38O", "N38K", "NX", "NC", "NR", "NS"]
EXPANDED_EDGES = ["E00a", "E00b", "E01", "E02", "E03", "E04a", "E04b", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25"]
INTERNAL_EDGES = EXPANDED_EDGES[:17]
CLOSURE_EDGES = EXPANDED_EDGES[17:22]
EXIT_EDGES = ["E20", "E21", "E23"]
FIREWALL_EDGES = ["E22"]
GUARD_EDGES = EXPANDED_EDGES[26:]
TOKEN_IDS = ["AFFINE_CAYLEY_FROZEN_FAMILY", "FINITE_RANK_LOCAL_SYSTEM_FROZEN_FAMILY", "CHARACTER_FROZEN_FAMILY", "GRADING_FROZEN_FAMILY", "QUOTIENT_FROZEN_FAMILY", "MODULAR_PHASE_FROZEN_FAMILY", "INDUCED_SHIFT_EXIT", "FIRST_RETURN_MAP_EXIT", "VALUATION_TREE_EXIT", "BOUNDARY_MODEL_EXIT", "BASEPOINT_DAMPING_EXIT", "FINITE_TOTAL_WEIGHT_RETROFIT_EXIT", "FROZEN_ASCENDING_HNN_BASS_SERRE_SPLITTING", "ALTERNATIVE_BASS_SERRE_SPLITTING_EXIT", "FROZEN_TREE_LATTICE_GROUPOID_IMPORT", "ALTERNATIVE_GROUPOID_CATEGORY_EXIT"]


def encode(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def registry_rows(markdown: str, preregistration: str) -> list[dict[str, Any]]:
    flattened = " ".join(preregistration.split())
    initial_pre_result = "Status at freeze: candidate definitions frozen; no numerical candidate result inspected" in flattened
    addendum_pre_result = "Two objects discovered during the source audit were added before any experiment on either object was run" in flattened
    output: list[dict[str, Any]] = []
    for line in markdown.split("\n"):
        if not line.startswith("| [`SD-C"):
            continue
        cells = [cell.strip() for cell in line[1:-1].split("|")]
        if len(cells) != 6:
            continue
        id_match = re.search(r"`(SD-C[0-9]{2})`", cells[0])
        path_match = re.search(r"\(([^)]+)\)", cells[0])
        if id_match is None or path_match is None:
            continue
        cid = id_match.group(1)
        obj = cells[1]
        affine = bool(re.search(r"\b(?:affine|cayley|bass-serre)\b|BS\(1", obj, re.I))
        candidate_heading = re.search(rf"^#{{2,3}} {re.escape(cid)}\s+[—-]", preregistration, re.M)
        if candidate_heading:
            tail = preregistration[candidate_heading.end():]
            next_candidate = re.search(r"^#{2,3} SD-C\d{2}(?:\s+[—-]|\s+implementation-freeze)", tail, re.M)
            section = preregistration[candidate_heading.start():candidate_heading.end() + (next_candidate.start() if next_candidate else len(tail))]
        else:
            section = ""
        initial = cid in {"SD-C01", "SD-C02", "SD-C03", "SD-C04"}
        evidence = {
            "candidate_section_present": candidate_heading is not None,
            "fixed_tests_present": ("Fixed tests and stop rule" in section) if initial else ("fixed tests" in " ".join(section.lower().split())),
            "frozen_object_present": ("Frozen object" in section) if initial else bool(re.search(r"\b(?:Define|Set)\b", section)),
            "pre_result_declaration_present": initial_pre_result if initial else addendum_pre_result,
            "stop_rule_present": "stop" in section.lower(),
        }
        output.append({
            "branch_class": "AFFINE" if affine else "NON_AFFINE_PREEXISTING_SOURCE_LOCKED",
            "candidate_id": cid,
            "frozen_route_tuple": cells[2].strip("`"),
            "object": obj,
            "overall_status": cells[3].strip("`"),
            "route_a_path": path_match.group(1),
            "route_b": cells[5],
            "source_locked": all(evidence.values()),
            "source_lock_evidence": evidence,
            "strongest_failure": cells[4],
        })
    return output


def blob(record: dict[str, Any]) -> str:
    selected = {
        key: record.get(key)
        for key in (
            "blocking_conditions",
            "determinant_convention",
            "forbidden_repairs",
            "main_theorem_marker",
            "next_smallest_test",
            "normalization",
            "object",
            "operator_ownership",
            "repair_alphabet",
            "round2_clues",
            "strongest_failures",
            "terminal_codes",
        )
    }
    return json.dumps(selected, ensure_ascii=False, sort_keys=True).lower()


def no_directed_cycle(nodes: list[str], edges: list[dict[str, Any]]) -> bool:
    remaining = set(nodes)
    pairs = [(edge.get("from"), edge.get("to")) for edge in edges]
    if any(source not in remaining or target not in remaining for source, target in pairs):
        return False
    while remaining:
        roots = {node for node in remaining if not any(target == node and source in remaining for source, target in pairs)}
        if not roots:
            return False
        remaining -= roots
    return True


def valid_transfer(entry: dict[str, Any], left: str, right: str, lock: dict[str, Any]) -> bool:
    mode = entry.get("mode")
    required = {"mode", left, right}
    if mode == "CARRY_IDENTICAL":
        return set(entry) == required and entry.get(left) == entry.get(right)
    if mode == "CARRY_WITH_EQUIVALENCE":
        return set(entry) == required | {"equivalence_id"} and entry.get("equivalence_id") in lock.get("equivalence_ids", [])
    if mode == "RESET":
        return set(entry) == required | {"reset_authority_id"} and entry.get("reset_authority_id") in lock.get("reset_authority_ids", [])
    return False


def independently_evaluate(packet: dict[str, Any], contract: dict[str, Any], lock: dict[str, Any], empty_fixture: dict[str, Any], fixture_hash: str, bridge: dict[str, Any], bridge_hash: str) -> dict[str, Any]:
    assertions: list[tuple[str, bool]] = []

    def assert_check(label: str, truth: bool) -> None:
        assertions.append((label, bool(truth)))

    assert_check("schemas", packet.get("schema") == "paper39-source-packet-v1" and contract.get("schema") == "paper39-affine-closure-contract-v1" and lock.get("schema") == "paper39-input-lock-v1")
    assert_check("scope", packet.get("candidate_contract_scope") == "FINITE_FROZEN_P35_P38_REPAIR_ALPHABET_ONLY" and packet.get("universal_affine_no_go_claimed") is False)
    preregistration_expected = {
        "checker_inputs_frozen_before_checker_run": True,
        "closure_universe_and_predicate_status": "RETROSPECTIVE_ENCODING_FROM_KNOWN_P35_P38_OUTCOMES",
        "freeze_boundary": "FROZEN_BEFORE_PAPER39_CHECKER_EXECUTION_NOT_BEFORE_PREDECESSOR_OUTCOMES",
        "independent_of_predecessor_results_claimed": False,
        "predecessor_outcomes_known_when_encoded": True,
    }
    preregistration_semantics = contract.get("preregistration_semantics", {})
    assert_check("retrospective_preregistration", preregistration_semantics == preregistration_expected and packet.get("preregistration_semantics") == preregistration_expected)
    route_lock = lock.get("route_a_evaluator", {})
    route_path = Path(route_lock.get("absolute_path", ""))
    route_text = route_path.read_text(encoding="utf-8") if route_path.is_file() else ""
    good_map = route_lock.get("good_conjunct_criterion_map", [])
    expected_meanings = [
        ("I", "INTRINSIC_SOURCE"),
        ("R", "NONEMPTY_PRIMITIVE_RECURRENCE_WITH_REPETITIONS"),
        ("S", "ARITHMETIC_SELECTIVITY"),
        ("D", "SAME_OBJECT_DETERMINANT_OWNERSHIP"),
        ("M", "MARKER_COMPATIBILITY"),
        ("C", "FROZEN_CONTROL_SURVIVAL"),
    ]
    assert_check("route_a_hash", route_path.is_file() and file_hash(route_path) == route_lock.get("sha256") == "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a")
    assert_check("route_a_version", route_lock.get("skill_version") == "0.2.0" and "**Version:** `0.2.0`" in route_text)
    assert_check("good_map_semantics", [(row.get("good_conjunct"), row.get("meaning")) for row in good_map] == expected_meanings)
    assert_check("good_map_criteria", all(row.get("criterion_ids") and len(row["criterion_ids"]) == len(set(row["criterion_ids"])) for row in good_map))
    assert_check("good_map_anchors", all(row.get("required_anchor_substrings") and all(anchor in route_text for anchor in row["required_anchor_substrings"]) for row in good_map))
    assert_check("route_a_packet", packet.get("route_a_evaluator_provenance") == {**route_lock, "current_hash_verified": True})
    bridge_lock = contract.get("expanded_dag_bridge", {})
    assert_check("bridge_lock", bridge_hash == bridge_lock.get("sha256") == "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240")
    assert_check("bridge_schema", bridge.get("schema") == bridge_lock.get("schema") == "paper39-structural-spine-expanded-proof-dag-bridge-v4")
    assert_check("bridge_granularity", contract.get("graph_granularity") == {"expanded_proof_dag": "22_NODE_28_EDGE_MATHEMATICAL_OBSTRUCTION_LEDGER", "losslessness_meaning": "ARTIFACT_RETENTION_UNDER_TOTAL_MANY_TO_ONE_NONINJECTIVE_PROJECTION", "nodes_and_edges_fields": "6_NODE_5_EDGE_STRUCTURAL_SPINE_ONLY", "structural_spine_is_full_dag": False})
    bridge_counts = bridge.get("counts", {})
    assert_check("bridge_counts", bridge_counts == {"top_level_repair_classes": 14, "frozen_request_tokens": 16, "internal_transition_tags": 17, "structural_spine_nodes": 6, "structural_spine_edges": 5, "expanded_proof_dag_nodes": 22, "expanded_proof_dag_edges": 28, "token_associated_contract_exit_edges": 3, "auxiliary_non_domain_firewall_edges": 1})
    structural = bridge.get("structural_spine", {})
    assert_check("spine_nodes", structural.get("node_ids") == [row.get("node_id") for row in contract.get("nodes", [])])
    assert_check("spine_edges", structural.get("edge_ids") == [row.get("edge_id") for row in contract.get("edges", [])])
    p37_projection_lock = next(spec for spec in lock.get("papers", []) if spec.get("paper_id") == "P37")
    assert_check("e36_37_projection_reset", bridge.get("projection_transfer_constraints") == {
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
    assert_check("expanded_nodes", expanded.get("node_ids") == EXPANDED_NODES)
    assert_check("expanded_edges", expanded.get("edge_ids") == EXPANDED_EDGES)
    assert_check("internal_tags", expanded.get("internal_transition_edge_ids") == INTERNAL_EDGES)
    partition = INTERNAL_EDGES + CLOSURE_EDGES + EXIT_EDGES + FIREWALL_EDGES + GUARD_EDGES
    assert_check("expanded_partitions", expanded.get("closure_edge_ids") == CLOSURE_EDGES and expanded.get("contract_exit_edge_ids") == EXIT_EDGES and expanded.get("non_domain_firewall_edge_ids") == FIREWALL_EDGES and expanded.get("governance_guard_edge_ids") == GUARD_EDGES and set(partition) == set(EXPANDED_EDGES) and len(partition) == len(set(partition)))
    edge_records = bridge.get("expanded_edge_records", [])
    edge_map = {row.get("edge_id"): row for row in edge_records}
    assert_check("edge_records_exact_ids", [row.get("edge_id") for row in edge_records] == EXPANDED_EDGES and all(set(row) == {"edge_id", "from", "to", "edge_kind"} for row in edge_records))
    ranks = bridge.get("expanded_node_rank", {})
    assert_check("rank_domain", list(ranks) == EXPANDED_NODES and all(isinstance(rank, int) for rank in ranks.values()))
    assert_check("edge_endpoints_and_ranks", all(row.get("from") in ranks and row.get("to") in ranks and ranks[row["from"]] < ranks[row["to"]] for row in edge_records))
    expected_kinds = {**{edge: "INTERNAL" for edge in INTERNAL_EDGES}, **{edge: "CLOSURE" for edge in CLOSURE_EDGES}, **{edge: "CONTRACT_EXIT" for edge in EXIT_EDGES}, "E22": "AUXILIARY_NON_DOMAIN_FIREWALL", "E24": "GOVERNANCE_GUARD_REALIZED", "E25": "GOVERNANCE_GUARD_CONDITIONAL"}
    assert_check("edge_kind_partition", all((edge_map.get(edge, {}).get("edge_kind", "").startswith("INTERNAL_TRANSITION") if kind == "INTERNAL" else edge_map.get(edge, {}).get("edge_kind") == kind) for edge, kind in expected_kinds.items()))
    node_projection = bridge.get("node_projection", {})
    edge_projection = bridge.get("edge_projection", {})
    assert_check("node_projection_total", list(node_projection) == EXPANDED_NODES and set(structural.get("node_ids", [])) <= set(node_projection.values()))
    assert_check("edge_projection_total", list(edge_projection) == EXPANDED_EDGES and set(structural.get("edge_ids", [])) <= set(edge_projection.values()))
    paths = bridge.get("expanded_provenance_paths", {})
    all_paths_valid = True
    used_internal: set[str] = set()
    for path in paths.values():
        path_edges = path.get("edge_ids", [])
        used_internal.update(edge for edge in path_edges if edge in INTERNAL_EDGES)
        all_paths_valid = all_paths_valid and path.get("start") == "N00" and bool(path_edges) and all(edge in edge_map for edge in path_edges)
        if path_edges and all(edge in edge_map for edge in path_edges):
            all_paths_valid = all_paths_valid and edge_map[path_edges[0]].get("from") == path.get("start") and edge_map[path_edges[-1]].get("to") == path.get("end")
            all_paths_valid = all_paths_valid and all(edge_map[left].get("to") == edge_map[right].get("from") for left, right in zip(path_edges, path_edges[1:]))
    assert_check("path_continuity", all_paths_valid and used_internal == set(INTERNAL_EDGES))
    endpoint_map = bridge.get("endpoint_classification", {})
    assert_check("endpoint_total", list(endpoint_map) == EXPANDED_NODES and all(set(row) == {"classification", "failed_good_coordinates", "terminal_code"} for row in endpoint_map.values()))
    good_ids = {"I", "R", "S", "D", "M", "C"}
    assert_check("endpoint_obstructions", sum(row.get("classification") == "OBSTRUCTED" for row in endpoint_map.values()) == 17 and all(row.get("failed_good_coordinates") and set(row["failed_good_coordinates"]) <= good_ids for row in endpoint_map.values() if row.get("classification") == "OBSTRUCTED"))
    assert_check("exit_separate", endpoint_map.get("NX", {}).get("classification") == "EXIT" and all(row.get("failed_good_coordinates") == [] for row in endpoint_map.values() if row.get("classification") != "OBSTRUCTED"))
    bridge_tokens = bridge.get("request_tokens", [])
    assert_check("token_ids", [row.get("token_id") for row in bridge_tokens] == TOKEN_IDS and len(TOKEN_IDS) == len(set(TOKEN_IDS)))
    assert_check("token_schema", all(set(row) == {"token_id", "repair_class", "instance_scope", "disposition", "obstruction_endpoint_ids", "obstruction_edge_ids", "boundary_comparison_endpoint_ids", "boundary_comparison_edge_ids", "exit_endpoint_ids", "exit_edge_ids", "classification_provenance_path_ids", "terminal_codes"} for row in bridge_tokens))
    token_by_id = {row.get("token_id"): row for row in bridge_tokens}
    token_semantics = True
    for token in bridge_tokens:
        obstruction_nodes = token.get("obstruction_endpoint_ids", [])
        boundary_nodes = token.get("boundary_comparison_endpoint_ids", [])
        exit_nodes = token.get("exit_endpoint_ids", [])
        role_ok = all(endpoint_map.get(node, {}).get("classification") == "OBSTRUCTED" and endpoint_map.get(node, {}).get("failed_good_coordinates") for node in obstruction_nodes)
        role_ok = role_ok and all(endpoint_map.get(node, {}).get("classification") == "OBSTRUCTED" for node in boundary_nodes)
        role_ok = role_ok and all(endpoint_map.get(node, {}).get("classification") == "EXIT" and endpoint_map.get(node, {}).get("failed_good_coordinates") == [] for node in exit_nodes)
        edge_ok = all(edge_map.get(edge, {}).get("to") in obstruction_nodes for edge in token.get("obstruction_edge_ids", [])) and all(edge_map.get(edge, {}).get("to") in boundary_nodes for edge in token.get("boundary_comparison_edge_ids", [])) and all(edge_map.get(edge, {}).get("to") in exit_nodes for edge in token.get("exit_edge_ids", []))
        disposition_ok = (token.get("disposition") == "OBSTRUCTED" and bool(obstruction_nodes) and not exit_nodes) or (token.get("disposition") == "EXIT" and bool(exit_nodes) and not obstruction_nodes)
        path_rows = [paths.get(path_id, {}) for path_id in token.get("classification_provenance_path_ids", [])]
        classified_nodes = obstruction_nodes + exit_nodes
        path_ok = bool(path_rows) and [row.get("end") for row in path_rows] == classified_nodes and token.get("terminal_codes") == [endpoint_map.get(node, {}).get("terminal_code") for node in classified_nodes]
        token_semantics = token_semantics and bool(token.get("instance_scope")) and "OTHER_INSTANCE" not in json.dumps(token).upper() and role_ok and edge_ok and disposition_ok and path_ok
        assert_check("token:" + str(token.get("token_id")), role_ok and edge_ok and disposition_ok and path_ok)
    assert_check("endpoint_obstruction_totality", token_semantics)
    assert_check("token_census", [sum(row.get("disposition") == value for row in bridge_tokens) for value in ("OBSTRUCTED", "EXIT")] == [8, 8])
    class_rows = bridge.get("repair_class_coverage", [])
    repair_order = [row.get("repair_class") for row in contract.get("repair_mappings", [])]
    assert_check("class_coverage_order", [row.get("repair_class") for row in class_rows] == repair_order)
    contract_dispositions_bridge = {row.get("repair_class"): row.get("disposition") for row in contract.get("repair_mappings", [])}
    covered_internal: set[str] = set()
    class_semantics = True
    for row in class_rows:
        class_id = row.get("repair_class")
        selected = [token_by_id.get(token_id, {}) for token_id in row.get("request_token_ids", [])]
        expected_tokens = [token for token in bridge_tokens if token.get("repair_class") == class_id]
        role_fields = ("obstruction_endpoint_ids", "obstruction_edge_ids", "boundary_comparison_endpoint_ids", "boundary_comparison_edge_ids", "exit_endpoint_ids", "exit_edge_ids")
        fields_ok = True
        for field in role_fields:
            union: list[str] = []
            for token in selected:
                for value in token.get(field, []):
                    if value not in union:
                        union.append(value)
            fields_ok = fields_ok and row.get(field) == union
        wanted = {"OBSTRUCTED": ["OBSTRUCTED"], "OUT_OF_CONTRACT_CATEGORY_CHANGE": ["EXIT"], "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT": ["OBSTRUCTED", "EXIT"]}.get(row.get("disposition"), [])
        current_ok = row.get("request_token_ids") == [token.get("token_id") for token in expected_tokens] and row.get("disposition") == contract_dispositions_bridge.get(class_id) and [token.get("disposition") for token in selected] == wanted and fields_ok
        class_semantics = class_semantics and current_ok
        covered_internal.update(row.get("obstruction_edge_ids", [])); covered_internal.update(row.get("boundary_comparison_edge_ids", []))
        assert_check("class:" + str(class_id), current_ok)
    assert_check("class_coverage_semantics", class_semantics and covered_internal == set(INTERNAL_EDGES))
    exit_credit = {edge for token in bridge_tokens for edge in token.get("exit_edge_ids", [])}
    exit_credit_classes = {edge for row in class_rows for edge in row.get("exit_edge_ids", [])}
    assert_check("token_exit_partition", exit_credit == exit_credit_classes == set(EXIT_EDGES))
    firewalls = bridge.get("non_domain_firewall_edges", [])
    firewall = firewalls[0] if len(firewalls) == 1 else {}
    p37_lock = next(spec for spec in lock.get("papers", []) if spec.get("paper_id") == "P37")
    assert_check("firewall_schema", len(firewalls) == 1 and set(firewall) == {"edge_id", "from", "to", "role", "domain_membership", "source_authority", "exact_scope", "request_token_ids", "repair_class_coverage_ids", "historical_boundary_path", "coverage_use", "terminal_code"})
    assert_check("firewall_typing", firewall.get("edge_id") == "E22" and firewall.get("from") == "N37N" and firewall.get("to") == "NX" and edge_map.get("E22", {}).get("edge_kind") == "AUXILIARY_NON_DOMAIN_FIREWALL")
    assert_check("firewall_empty_fibers", firewall.get("request_token_ids") == [] and firewall.get("repair_class_coverage_ids") == [])
    assert_check("firewall_scope", firewall.get("domain_membership") == "OUTSIDE_EXACT_A14_REPAIR_TAGS_AND_SIGMA16_REQUEST_TOKENS" and firewall.get("coverage_use") == "EXCLUDED_FROM_A14_SIGMA16_AND_ENDPOINT_OBSTRUCTION_EXHAUSTIVENESS")
    assert_check("firewall_authority", firewall.get("source_authority") == {"p37_source_lock_sha256": p37_lock.get("files", {}).get("SOURCE_LOCK.md"), "p37_round2_clues_sha256": p37_lock.get("files", {}).get("ROUND2_CLUES.md")})
    history = firewall.get("historical_boundary_path", {})
    history_edges = history.get("edge_ids", [])
    history_string = f"{history.get('path_id')}|{history.get('start')}|{','.join(history_edges)}|{history.get('end')}"
    history_ok = set(history) == {"path_id", "canonical_string", "sha256", "start", "edge_ids", "end"} and history.get("path_id") == "H_NX_E22" and history.get("start") == "N00" and history.get("end") == "NX" and bool(history_edges) and history_edges[-1:] == ["E22"] and all(edge in edge_map for edge in history_edges)
    history_ok = history_ok and history.get("canonical_string") == history_string and history.get("sha256") == hashlib.sha256(history_string.encode()).hexdigest() == "1231fe11f42c13ec3a7925d68d89f066b1deb2460f57924ecb76dd3d3490850a"
    if history_ok:
        history_ok = edge_map[history_edges[0]].get("from") == "N00" and edge_map[history_edges[-1]].get("to") == "NX" and all(edge_map[left].get("to") == edge_map[right].get("from") for left, right in zip(history_edges, history_edges[1:]))
    assert_check("firewall_history", history_ok)
    credited_edges = {edge for token in bridge_tokens for field in ("obstruction_edge_ids", "boundary_comparison_edge_ids", "exit_edge_ids") for edge in token.get(field, [])}
    credited_edges.update(edge for row in class_rows for field in ("obstruction_edge_ids", "boundary_comparison_edge_ids", "exit_edge_ids") for edge in row.get(field, []))
    assert_check("firewall_zero_credit", "E22" not in credited_edges and endpoint_map.get("NX", {}).get("failed_good_coordinates") == [] and firewall.get("terminal_code") == endpoint_map.get("NX", {}).get("terminal_code"))
    assert_check("guards", bridge.get("realized_guard") == {"expanded_edge_id": "E24", "structural_spine_edge_id": "E_CLOSE_REGISTRY", "terminal": "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY"} and bridge.get("conditional_guard") == {"expanded_edge_id": "E25", "structural_spine_projection": "AUX_EMPTY_REGISTRY_FALLBACK", "terminal": "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR", "realized": False})
    loss = bridge.get("losslessness", {})
    assert_check("artifact_retention", "not claim that the projection is injective or invertible" in str(loss.get("meaning")) and all(value is True for key, value in loss.items() if key != "meaning"))
    p38_lock = next(spec for spec in lock.get("papers", []) if spec.get("paper_id") == "P38")
    predecessor_source_locks = {
        f"{paper['paper_id']}_{paper['candidate_id']}": paper.get("files", {}).get("SOURCE_LOCK.md")
        for paper in lock.get("papers", [])
    }
    assert_check("criterion_provenance", bridge.get("criterion_provenance") == {
        "route_a_evaluator_sha256": route_lock.get("sha256"),
        "p38_source_lock_sha256": p38_lock.get("files", {}).get("SOURCE_LOCK.md"),
        "p38_round2_clues_sha256": p38_lock.get("files", {}).get("ROUND2_CLUES.md"),
        "predecessor_source_lock_sha256": predecessor_source_locks,
        "freeze_timing": "RETROSPECTIVE_P35_P38_OUTCOMES_KNOWN_FROZEN_BEFORE_P39_CHECKER",
    })
    assert_check("good_field_map", bridge.get("good_field_map") == {
        "I": ["A0.arithmetic_origin", "source_lock.allowed_data", "source_lock.forbidden_data", "source_lock.parameter_provenance"],
        "R": ["A1.primitive_ledger", "A1.repetition_semantics", "source_lock.object", "source_lock.dynamics", "source_lock.clock"],
        "S": ["A0.arithmetic_sector", "A1.arithmetic_selectivity", "adversarial_controls.generic_and_composite"],
        "D": ["A2.operator_object", "A2.determinant_convention", "source_lock.regularization_order"],
        "M": ["source_lock.clock", "source_lock.main_theorem_marker", "source_lock.normalization"],
        "C": ["adversarial_controls", "proves_too_much_risk", "blocking_conditions", "stop_rule"],
    })
    terminology_blob = json.dumps(bridge.get("terminology", {}), ensure_ascii=False).lower()
    assert_check("terminology_no_reflexive_termination", "reflexive" not in terminology_blob and "operational termination" not in terminology_blob and "semantic-terminal reachability" not in terminology_blob)
    assert_check("terminology_retrospective_encoding", bridge.get("terminology", {}).get("encoding_timing") == "The 14-class/16-token/Good encoding is a retrospective Paper-39 construction assembled from hashed P35-P38 artifacts after predecessor outcomes were known and frozen before the Paper-39 checker; only literal predecessor fields and the P38 prohibition list are called predecessor-frozen.")
    fixture_rows = empty_fixture.get("rows", [])
    fixture_count = sum(row.get("source_locked") and row.get("branch_class") == contract.get("registry", {}).get("branch_class") for row in fixture_rows)
    fixture_terminal = contract["realized_terminal"] if fixture_count else contract["conditional_empty_registry_terminal"]
    assert_check("empty_fixture_hash", fixture_hash == contract.get("empty_registry_fixture", {}).get("sha256"))
    assert_check("empty_fixture_schema", empty_fixture.get("schema") == "paper39-empty-registry-fixture-v1")
    assert_check("empty_fixture_rows", fixture_rows == [] and empty_fixture.get("source_locked_non_affine_count") == 0)
    assert_check("empty_fixture_execution", fixture_terminal == empty_fixture.get("expected_terminal") == "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR")
    assert_check("empty_fixture_independent", empty_fixture.get("chronology_basis") == "independent_synthetic_empty_fixture_not_live_registry_history")
    records = packet.get("paper_records", [])
    papers = {row.get("paper_id"): row for row in records}
    assert_check("paper_exact_set", list(papers) == ["P35", "P36", "P37", "P38"] and len(records) == 4)

    base = Path(lock["authority_papers_base"])
    for spec in lock.get("papers", []):
        pid = spec["paper_id"]
        row = papers.get(pid, {})
        current_hashes = {relative: file_hash(base / spec["slug"] / relative) for relative in spec["files"]}
        assert_check(f"{pid}:current_hashes", current_hashes == spec["files"])
        assert_check(f"{pid}:packet_hashes", row.get("input_hashes") == spec["files"])
        assert_check(f"{pid}:provenance", row.get("sealed_provenance_triple") == [spec["artifact_commit"]] * 3)
        assert_check(f"{pid}:route", row.get("overall_verdict") == "ROUTE_A_REJECTED" and row.get("route_b_invocation_allowed") is False and len(row.get("route_tuple", [])) == 5)
        assert_check(f"{pid}:typed_raw", all(isinstance(row.get(field), str) and row.get(field) for field in ("object", "main_theorem_marker", "determinant_convention", "next_smallest_test")))
        owner = row.get("operator_ownership", {})
        assert_check(f"{pid}:operator_owner", owner.get("operator_object") == row.get("object") and owner.get("determinant_convention") == row.get("determinant_convention") and bool(owner.get("regularization_order")))
        assert_check(f"{pid}:terminal_codes", row.get("terminal_codes") == row.get("terminal_evidence", {}).get("codes") and bool(row.get("terminal_codes")))
        normalized = row.get("typed_normalization", {})
        assert_check(
            f"{pid}:typed_normalization",
            normalized.get("inherited_obligation") == row.get("next_smallest_test")
            and normalized.get("object") == row.get("object")
            and normalized.get("marker") == row.get("main_theorem_marker")
            and normalized.get("operator_ownership") == row.get("operator_ownership")
            and normalized.get("obstructions") == {"blocking_conditions": row.get("blocking_conditions"), "strongest_failures": row.get("strongest_failures")}
            and normalized.get("forbidden_repairs") == row.get("forbidden_repairs")
            and normalized.get("terminal_codes") == row.get("terminal_codes"),
        )

    catalog = contract.get("witness_catalog", [])
    obstruction_universe = contract.get("required_obstruction_witness_codes", [])
    boundary_universe = contract.get("required_boundary_exit_witness_codes", [])
    expected_codes = obstruction_universe + boundary_universe
    observed_codes = [entry.get("code") for entry in catalog]
    assert_check("witness_code_set", set(observed_codes) == set(expected_codes) and len(observed_codes) == len(set(observed_codes)) == len(expected_codes))
    assert_check("witness_kind_split", len(obstruction_universe) == len(set(obstruction_universe)) and len(boundary_universe) == len(set(boundary_universe)) and not (set(obstruction_universe) & set(boundary_universe)))
    witness_ok: dict[str, bool] = {}
    for entry in catalog:
        evidence = blob(papers.get(entry.get("paper_id"), {}))
        ok = all(str(term).lower() in evidence for term in entry.get("evidence_contains", []))
        witness_ok[entry["code"]] = ok
        assert_check("witness:" + entry["code"], ok)

    p38_repairs = papers.get("P38", {}).get("repair_alphabet", [])
    mappings = contract.get("repair_mappings", [])
    repair_ids = [row.get("repair_class") for row in p38_repairs]
    mapped_ids = [row.get("repair_class") for row in mappings]
    assert_check("repair_exact_set", repair_ids == mapped_ids and len(repair_ids) == len(set(repair_ids)) == 14)
    for mapping in mappings:
        obstruction_codes = mapping.get("obstruction_witness_codes", [])
        boundary_codes = mapping.get("boundary_exit_witness_codes", [])
        assert_check("repair_witness_kinds:" + mapping["repair_class"], set(obstruction_codes) <= set(obstruction_universe) and set(boundary_codes) <= set(boundary_universe))
        assert_check("repair_classified:" + mapping["repair_class"], bool(obstruction_codes or boundary_codes) and all(witness_ok.get(code, False) for code in obstruction_codes + boundary_codes))
        flags = (mapping.get("canonical_tested"), mapping.get("alternative_instances_exit"))
        disposition = {
            (True, False): "OBSTRUCTED",
            (False, True): "OUT_OF_CONTRACT_CATEGORY_CHANGE",
            (True, True): "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT",
        }.get(flags)
        assert_check(
            "repair_disposition:" + mapping["repair_class"],
            disposition is not None
            and mapping.get("disposition") == disposition
            and (disposition != "OBSTRUCTED" or (bool(obstruction_codes) and not boundary_codes))
            and (disposition != "OUT_OF_CONTRACT_CATEGORY_CHANGE" or (not obstruction_codes and bool(boundary_codes)))
            and (disposition != "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT" or (bool(obstruction_codes) and bool(boundary_codes))),
        )
    disposition_names = ["OBSTRUCTED", "OUT_OF_CONTRACT_CATEGORY_CHANGE", "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT"]
    disposition_census = {name: sum(row.get("disposition") == name for row in mappings) for name in disposition_names}
    assert_check("repair_disposition_census", [disposition_census[name] for name in disposition_names] == [6, 6, 2])

    declared = packet.get("declared_edges", [])
    expected_edges = contract.get("edges", [])
    assert_check("edge_ids", [edge.get("edge_id") for edge in declared] == [edge.get("edge_id") for edge in expected_edges] and len(declared) == 5)
    node_order = [node.get("node_id") for node in contract.get("nodes", [])]
    nodes = {node.get("node_id"): node for node in contract.get("nodes", [])}
    assert_check("p38_object_code_narrow", nodes.get("N38_TREE_ORBITAL_TRILEMMA", {}).get("object_code") == "FROZEN_ASCENDING_HNN_PRESENTATION_BASS_SERRE_FULL_EDGE_SHIFT" and "PRESENTATION_CANONICAL_BASS_SERRE_FULL_EDGE_SHIFT" not in json.dumps(contract, ensure_ascii=False))
    assert_check("dag_acyclic", no_directed_cycle(node_order, expected_edges))
    assert_check("dag_chain_total", [(edge.get("from"), edge.get("to")) for edge in expected_edges] == list(zip(node_order, node_order[1:])))
    e36_contract = next((edge for edge in expected_edges if edge.get("edge_id") == "E36_37"), {})
    e36_packet = next((edge for edge in declared if edge.get("edge_id") == "E36_37"), {})
    p36_spec = next(spec for spec in lock.get("papers", []) if spec.get("paper_id") == "P36")
    p37_spec = next(spec for spec in lock.get("papers", []) if spec.get("paper_id") == "P37")
    projection_constraint = bridge.get("projection_transfer_constraints", {}).get("E36_37", {})
    assert_check(
        "e36_37_nonstate_metadata_binding",
        (e36_contract.get("from"), e36_contract.get("to")) == ("N36_CELLULAR_CANCELLATION", "N37_COEFFICIENT_SATURATION")
        and e36_contract.get("inherited_obligation_source") == "P36.next_smallest_test"
        and e36_packet.get("inherited_obligation") == papers.get("P36", {}).get("next_smallest_test")
        and projection_constraint.get("carry_fields") == ["inherited_obligation", "historical_provenance"]
        and projection_constraint.get("expanded_authority_edge_id") == "E07"
        and projection_constraint.get("reset_authority_sha256") == p37_spec.get("files", {}).get("SOURCE_LOCK.md")
        and papers.get("P36", {}).get("input_hashes") == p36_spec.get("files")
        and papers.get("P37", {}).get("input_hashes") == p37_spec.get("files")
        and papers.get("P36", {}).get("sealed_provenance_triple") == [p36_spec.get("artifact_commit")] * 3
        and papers.get("P37", {}).get("sealed_provenance_triple") == [p37_spec.get("artifact_commit")] * 3,
    )
    assert_check("node_full_schema", all(node.get("inherited_obligation_source") and node.get("forbidden_escape_source") and isinstance(node.get("obstruction_codes"), list) and isinstance(node.get("boundary_exit_codes"), list) and (node.get("obstruction_codes") or node.get("boundary_exit_codes")) for node in nodes.values()))
    raw_types = {
        "N35_OBJECT_FIREWALL": {"determinant_owner": papers["P35"]["determinant_convention"], "marker": papers["P35"]["main_theorem_marker"], "object": papers["P35"]["object"], "operator_owner": papers["P35"]["operator_ownership"]},
        "N36_CELLULAR_CANCELLATION": {"determinant_owner": papers["P36"]["determinant_convention"], "marker": papers["P36"]["main_theorem_marker"], "object": papers["P36"]["object"], "operator_owner": papers["P36"]["operator_ownership"]},
        "N37_COEFFICIENT_SATURATION": {"determinant_owner": papers["P37"]["determinant_convention"], "marker": papers["P37"]["main_theorem_marker"], "object": papers["P37"]["object"], "operator_owner": papers["P37"]["operator_ownership"]},
        "N38_TREE_ORBITAL_TRILEMMA": {"determinant_owner": papers["P38"]["determinant_convention"], "marker": papers["P38"]["main_theorem_marker"], "object": papers["P38"]["object"], "operator_owner": papers["P38"]["operator_ownership"]},
        "N39_AFFINE_BRANCH_CLOSED": {"determinant_owner": "NO_NEW_DETERMINANT_AUDIT_ONLY", "marker": "NO_NEW_MARKER_AUDIT_ONLY", "object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM", "operator_owner": {"determinant_convention": "NO_NEW_DETERMINANT_AUDIT_ONLY", "operator_object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM", "regularization_order": "AUDIT_ONLY_NOT_APPLICABLE"}},
        "N_REGISTRY_HANDOFF": {"determinant_owner": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "marker": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY", "operator_owner": {"determinant_convention": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY", "operator_object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY", "regularization_order": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY"}},
    }
    code_fields = {"determinant_owner": "determinant_code", "marker": "marker_code", "object": "object_code", "operator_owner": "operator_owner_code"}
    transfer_lock = contract.get("transfer_semantics_contract", {})
    assert_check("transfer_enum", transfer_lock.get("allowed_modes") == ["CARRY_IDENTICAL", "CARRY_WITH_EQUIVALENCE", "RESET", "EXIT"])
    reset_bindings = {
        "E35_36": {field: "P36_SOURCE_LOCK_SD_C38" for field in ("determinant_owner", "marker", "object", "operator_owner")},
        "E36_37": {field: "P37_SOURCE_LOCK_SD_C39" for field in ("determinant_owner", "marker", "object", "operator_owner")},
        "E37_38": {field: "P38_SOURCE_LOCK_SD_C40" for field in ("determinant_owner", "marker", "object", "operator_owner")},
        "E38_CLOSE": {field: "P39_AUDIT_ONLY_CONTRACT" for field in ("determinant_owner", "marker", "object", "operator_owner")},
        "E_CLOSE_REGISTRY": {field: "SESSION4_REGISTRY_SOURCE_LOCK" for field in ("determinant_owner", "marker", "object", "operator_owner")},
    }
    equivalence_bindings: dict[str, dict[str, str]] = {}
    assert_check("reset_bindings", transfer_lock.get("reset_authority_bindings") == reset_bindings)
    assert_check("equivalence_bindings", transfer_lock.get("equivalence_bindings") == equivalence_bindings and transfer_lock.get("equivalence_ids") == [])
    assert_check("e36_37_non_inheritance", transfer_lock.get("non_inheritance_assertions") == {"E36_37": {"candidate_identity_fields": ["object", "marker", "operator_owner", "determinant_owner"], "statement": "ALL_CANDIDATE_IDENTITY_FIELDS_RESET_TO_INDEPENDENT_P37_SOURCE_LOCK_NO_SOURCE_TO_TARGET_EQUIVALENCE_CREDIT"}})
    assert_check("exit_non_obstruction", transfer_lock.get("exit_semantics") == "CLASSIFICATION_NONMEMBERSHIP_ONLY_NEVER_OBSTRUCTION_EVIDENCE_AND_NOT_A_STRUCTURAL_SPINE_FIELD_TRANSFER")
    targets = {"E35_36": papers.get("P36", {}), "E36_37": papers.get("P37", {}), "E37_38": papers.get("P38", {})}
    for observed, expected in zip(declared, expected_edges):
        eid = expected["edge_id"]
        assert_check(eid + ":endpoints", (observed.get("from"), observed.get("to")) == (expected.get("from"), expected.get("to")))
        assert_check(eid + ":obligation", isinstance(observed.get("inherited_obligation"), str) and len(observed["inherited_obligation"]) > 40)
        for field, code_field in code_fields.items():
            contract_transfer = expected.get("field_transfer", {}).get(field, {})
            observed_transfer = observed.get("field_transfer", {}).get(field, {})
            mode = contract_transfer.get("mode")
            binding_ok = (
                (mode == "RESET" and contract_transfer.get("reset_authority_id") == reset_bindings.get(eid, {}).get(field))
                or (mode == "CARRY_WITH_EQUIVALENCE" and contract_transfer.get("equivalence_id") == equivalence_bindings.get(eid, {}).get(field))
                or mode == "CARRY_IDENTICAL"
            )
            assert_check(
                eid + ":contract_transfer:" + field,
                valid_transfer(contract_transfer, "source_code", "target_code", transfer_lock)
                and contract_transfer.get("source_code") == nodes.get(expected.get("from"), {}).get(code_field)
                and contract_transfer.get("target_code") == nodes.get(expected.get("to"), {}).get(code_field)
                and binding_ok,
            )
            expected_raw = {key: value for key, value in contract_transfer.items() if key not in {"source_code", "target_code"}}
            expected_raw.update({"source": raw_types.get(expected.get("from"), {}).get(field), "target": raw_types.get(expected.get("to"), {}).get(field)})
            assert_check(
                eid + ":packet_transfer:" + field,
                observed_transfer == expected_raw and valid_transfer(observed_transfer, "source", "target", transfer_lock),
            )
        if eid in targets:
            target = targets[eid]
            assert_check(eid + ":object", observed.get("target_object") == target.get("object"))
            assert_check(eid + ":marker", observed.get("target_marker") == target.get("main_theorem_marker"))
            assert_check(eid + ":determinant", observed.get("target_determinant") == target.get("determinant_convention"))
            assert_check(eid + ":operator_owner", observed.get("target_operator_ownership") == target.get("operator_ownership"))
    terminal_edges = {edge.get("edge_id"): edge for edge in declared}
    assert_check("closure_target", terminal_edges.get("E38_CLOSE", {}).get("target_object") == "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM")
    assert_check("registry_target", terminal_edges.get("E_CLOSE_REGISTRY", {}).get("target_object") == "SESSION4_GLOBAL_CANDIDATE_REGISTRY")
    assert_check(
        "terminal_operator_owners",
        terminal_edges.get("E38_CLOSE", {}).get("target_operator_ownership", {}).get("operator_object") == "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM"
        and terminal_edges.get("E_CLOSE_REGISTRY", {}).get("target_operator_ownership", {}).get("operator_object") == "SESSION4_GLOBAL_CANDIDATE_REGISTRY",
    )

    reg_lock = lock["registry"]
    reg_path = base / reg_lock["candidate_registry_relative"]
    prereg_path = base / reg_lock["preregistration_relative"]
    assert_check("registry_current_hashes", file_hash(reg_path) == reg_lock["candidate_registry_sha256"] and file_hash(prereg_path) == reg_lock["preregistration_sha256"])
    registry_text = reg_path.read_text(encoding="utf-8")
    prereg_text = prereg_path.read_text(encoding="utf-8")
    prereg_flat = " ".join(prereg_text.split())
    assert_check("registry_title_status", "# Session 4 Candidate Registry" in registry_text and "Candidate definitions and stop rules are frozen" in registry_text)
    assert_check("prereg_title_status", "# Session 4 Preregistration and Source Lock" in prereg_text and "Status at freeze: candidate definitions frozen; no numerical candidate result inspected" in prereg_flat and "Two objects discovered during the source audit were added before any experiment on either object was run" in prereg_flat)
    parsed_registry = registry_rows(registry_text, prereg_text)
    packet_registry = packet.get("registry", {})
    expected_registry_ids = contract["registry"]["expected_ids"]
    assert_check("registry_rows", parsed_registry == packet_registry.get("rows"))
    assert_check("registry_ids", [row["candidate_id"] for row in parsed_registry] == expected_registry_ids)
    assert_check("registry_class", all(row["source_locked"] and row["branch_class"] == "NON_AFFINE_PREEXISTING_SOURCE_LOCKED" for row in parsed_registry))
    assert_check("registry_lock_evidence", all(len(row.get("source_lock_evidence", {})) == 5 and all(row.get("source_lock_evidence", {}).values()) for row in parsed_registry))
    non_affine = sum(row["source_locked"] and row["branch_class"] == "NON_AFFINE_PREEXISTING_SOURCE_LOCKED" for row in parsed_registry)
    expected_terminal = contract["realized_terminal"] if non_affine else contract["conditional_empty_registry_terminal"]
    assert_check("registry_count", non_affine == packet_registry.get("source_locked_non_affine_count") == 6)
    assert_check("conditional_terminal", expected_terminal == packet_registry.get("realized_terminal") == "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY")
    assert_check("chronology_basis", packet_registry.get("chronology_basis") == "trusted_hashed_source_assertion" and packet_registry.get("chronology_evidence_status") == "TRUSTED_HASHED_SOURCE_ASSERTION_NOT_INDEPENDENTLY_ESTABLISHED" and packet_registry.get("preregistration_source_lock_path") == reg_lock["preregistration_relative"])
    mechanism = packet.get("mechanism_creation", {})
    assert_check("no_new_mechanism", mechanism.get("new_mechanisms") == [])
    assert_check("no_ranking", mechanism.get("ranking") == [])
    assert_check("no_proposal", mechanism.get("successor_proposals") == [])
    assert_check("node_operator_owners", all(isinstance(node.get("operator_owner_code"), str) and bool(node.get("operator_owner_code")) for node in contract.get("nodes", [])))

    projection = {
        "affine_branch": "CLOSE_ENTIRE_AFFINE_BRANCH",
        "contract_relative_exhaustiveness": True,
        "structural_spine_edge_ids": [edge["edge_id"] for edge in expected_edges],
        "empty_registry_fixture_terminal": fixture_terminal,
        "new_mechanism_count": 0,
        "structural_spine_node_ids": [node["node_id"] for node in contract.get("nodes", [])],
        "node_operator_owner_codes": [node["operator_owner_code"] for node in contract.get("nodes", [])],
        "realized_terminal": expected_terminal,
        "registry_ids": expected_registry_ids,
        "repair_classes": mapped_ids,
        "repair_boundary_exit_witnesses": {row["repair_class"]: row["boundary_exit_witness_codes"] for row in mappings},
        "repair_dispositions": {row["repair_class"]: row["disposition"] for row in mappings},
        "repair_disposition_census": disposition_census,
        "repair_obstruction_witnesses": {row["repair_class"]: row["obstruction_witness_codes"] for row in mappings},
        "expanded_bridge_sha256": bridge_hash,
        "expanded_counts": bridge_counts,
        "expanded_edge_ids": EXPANDED_EDGES,
        "expanded_node_ids": EXPANDED_NODES,
        "request_token_dispositions": {row.get("token_id"): row.get("disposition") for row in bridge_tokens},
        "request_token_ids": [row.get("token_id") for row in bridge_tokens],
        "endpoint_obstruction_totality": True,
        "retrospective_encoding_timing": bridge.get("terminology", {}).get("encoding_timing"),
        "retrospective_preregistration_semantics": preregistration_semantics,
        "route_a_evaluator_sha256": route_lock.get("sha256"),
        "route_a_good_conjuncts": [row.get("good_conjunct") for row in good_map],
        "universal_affine_no_go_claimed": False,
    }
    passed = sum(value for _, value in assertions)
    return {
        "all_pass": passed == len(assertions),
        "checks": [{"name": name, "passed": value} for name, value in assertions],
        "counts": {"checks_passed": passed, "checks_total": len(assertions), "expanded_dag_edges": len(EXPANDED_EDGES), "expanded_dag_nodes": len(EXPANDED_NODES), "internal_transition_tags": len(INTERNAL_EDGES), "request_tokens": len(bridge_tokens), "structural_spine_edges": len(expected_edges), "structural_spine_nodes": len(contract.get("nodes", []))},
        "schema": "paper39-independent-evaluation-v1",
        "science_projection": projection,
        "science_projection_sha256": hashlib.sha256(encode(projection)).hexdigest(),
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
        packet = json.loads(Path(args.packet).read_text())
        contract = json.loads(Path(args.contract).read_text())
        lock = json.loads(Path(args.input_lock).read_text())
        fixture_path = Path(args.empty_registry_fixture)
        empty_fixture = json.loads(fixture_path.read_text())
        bridge_path = Path(args.dag_bridge)
        bridge = json.loads(bridge_path.read_text())
        result = independently_evaluate(packet, contract, lock, empty_fixture, file_hash(fixture_path), bridge, file_hash(bridge_path))
        output.write_bytes(encode(result))
        return 0 if result["all_pass"] else 1
    except Exception as exc:
        output.write_bytes(encode({"all_pass": False, "error": f"{type(exc).__name__}:{exc}", "schema": "paper39-independent-error-v1"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
