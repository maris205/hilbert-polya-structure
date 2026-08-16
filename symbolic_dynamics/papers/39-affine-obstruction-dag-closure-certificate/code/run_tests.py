#!/usr/bin/env python3
"""Adversarial mutation suite for both Paper 39 evaluators."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, Callable


ArtifactBundle = dict[str, dict[str, Any]]
Mutation = Callable[[ArtifactBundle], None]


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def packet_edge(packet: dict[str, Any], edge_id: str) -> dict[str, Any]:
    return next(row for row in packet["declared_edges"] if row["edge_id"] == edge_id)


def contract_edge(contract: dict[str, Any], edge_id: str) -> dict[str, Any]:
    return next(row for row in contract["edges"] if row["edge_id"] == edge_id)


def missing_edge(bundle: ArtifactBundle) -> None:
    packet = bundle["packet"]
    packet["declared_edges"] = [row for row in packet["declared_edges"] if row["edge_id"] != "E36_37"]


def wrong_object_transfer(bundle: ArtifactBundle) -> None:
    changed = packet_edge(bundle["packet"], "E35_36")
    changed["target_object"] = "WRONG_OBJECT_TRANSFER"
    changed["field_transfer"]["object"]["target"] = "WRONG_OBJECT_TRANSFER"


def marker_swap(bundle: ArtifactBundle) -> None:
    packet = bundle["packet"]
    changed = packet_edge(packet, "E36_37")
    changed["target_marker"] = packet["paper_records"][3]["main_theorem_marker"]
    changed["field_transfer"]["marker"]["target"] = packet["paper_records"][3]["main_theorem_marker"]


def determinant_category_swap(bundle: ArtifactBundle) -> None:
    changed = packet_edge(bundle["packet"], "E37_38")
    changed["target_determinant"] = "GROUPOID_TRACE_NOT_ORDINARY_FREDHOLM"
    changed["field_transfer"]["determinant_owner"]["target"] = "GROUPOID_TRACE_NOT_ORDINARY_FREDHOLM"


def post_hoc_representation(bundle: ArtifactBundle) -> None:
    bundle["packet"]["mechanism_creation"]["new_mechanisms"] = ["POST_HOC_REPRESENTATION"]


def stale_provenance(bundle: ArtifactBundle) -> None:
    bundle["packet"]["paper_records"][0]["sealed_provenance_triple"][0] = "0" * 40


def prospective_predecessor_independence_claim(bundle: ArtifactBundle) -> None:
    invalid = {
        "checker_inputs_frozen_before_checker_run": True,
        "closure_universe_and_predicate_status": "PROSPECTIVE_ENCODING_INDEPENDENT_OF_PREDECESSOR_OUTCOMES",
        "freeze_boundary": "FROZEN_BEFORE_PREDECESSOR_OUTCOMES",
        "independent_of_predecessor_results_claimed": True,
        "predecessor_outcomes_known_when_encoded": False,
    }
    bundle["contract"]["preregistration_semantics"] = copy.deepcopy(invalid)
    bundle["packet"]["preregistration_semantics"] = copy.deepcopy(invalid)


def stale_canonical_p38_object_code(bundle: ArtifactBundle) -> None:
    stale = "PRESENTATION_CANONICAL_BASS_SERRE_FULL_EDGE_SHIFT"
    p38_node = next(row for row in bundle["contract"]["nodes"] if row["node_id"] == "N38_TREE_ORBITAL_TRILEMMA")
    p38_node["object_code"] = stale
    contract_edge(bundle["contract"], "E37_38")["field_transfer"]["object"]["target_code"] = stale
    contract_edge(bundle["contract"], "E38_CLOSE")["field_transfer"]["object"]["source_code"] = stale


def unregistered_successor_insertion(bundle: ArtifactBundle) -> None:
    packet = bundle["packet"]
    inserted = copy.deepcopy(packet["registry"]["rows"][-1])
    inserted["candidate_id"] = "SD-C99"
    inserted["object"] = "unregistered successor"
    packet["registry"]["rows"].append(inserted)
    packet["registry"]["source_locked_non_affine_count"] = 7


def existing_entry_misclassification(bundle: ArtifactBundle) -> None:
    bundle["packet"]["registry"]["rows"][0]["branch_class"] = "AFFINE"


def false_empty_registry(bundle: ArtifactBundle) -> None:
    packet = bundle["packet"]
    packet["registry"]["source_locked_non_affine_count"] = 0
    packet["registry"]["realized_terminal"] = "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR"


def ranked_or_proposed_successor(bundle: ArtifactBundle) -> None:
    packet = bundle["packet"]
    packet["mechanism_creation"]["ranking"] = ["SD-C04"]
    packet["mechanism_creation"]["successor_proposals"] = ["SD-C07"]


def bad_transfer_mode(bundle: ArtifactBundle) -> None:
    contract_edge(bundle["contract"], "E35_36")["field_transfer"]["object"]["mode"] = "TELEPORT"
    packet_edge(bundle["packet"], "E35_36")["field_transfer"]["object"]["mode"] = "TELEPORT"


def illegal_carry_and_reset_semantics(bundle: ArtifactBundle) -> None:
    contract_object = contract_edge(bundle["contract"], "E35_36")["field_transfer"]["object"]
    packet_object = packet_edge(bundle["packet"], "E35_36")["field_transfer"]["object"]
    contract_object["reset_authority_id"] = "P37_SOURCE_LOCK_SD_C39"
    packet_object["reset_authority_id"] = "P37_SOURCE_LOCK_SD_C39"


def force_illegal_e36_37_carry(bundle: ArtifactBundle, field: str) -> None:
    contract_transfer = contract_edge(bundle["contract"], "E36_37")["field_transfer"][field]
    packet_transfer = packet_edge(bundle["packet"], "E36_37")["field_transfer"][field]
    contract_transfer["mode"] = "CARRY_WITH_EQUIVALENCE"
    packet_transfer["mode"] = "CARRY_WITH_EQUIVALENCE"
    del contract_transfer["reset_authority_id"]
    del packet_transfer["reset_authority_id"]
    contract_transfer["equivalence_id"] = f"UNLOCKED_E36_37_{field.upper()}_EQUIVALENCE"
    packet_transfer["equivalence_id"] = f"UNLOCKED_E36_37_{field.upper()}_EQUIVALENCE"


def illegal_e36_37_object_carry(bundle: ArtifactBundle) -> None:
    force_illegal_e36_37_carry(bundle, "object")


def illegal_e36_37_marker_carry(bundle: ArtifactBundle) -> None:
    force_illegal_e36_37_carry(bundle, "marker")


def illegal_e36_37_operator_owner_carry(bundle: ArtifactBundle) -> None:
    force_illegal_e36_37_carry(bundle, "operator_owner")


def illegal_e36_37_determinant_owner_carry(bundle: ArtifactBundle) -> None:
    force_illegal_e36_37_carry(bundle, "determinant_owner")


def exit_as_obstruction(bundle: ArtifactBundle) -> None:
    mapping = next(row for row in bundle["contract"]["repair_mappings"] if row["repair_class"] == "basepoint_damping")
    mapping["obstruction_witness_codes"] = list(mapping["boundary_exit_witness_codes"])
    mapping["boundary_exit_witness_codes"] = []
    mapping["canonical_tested"] = True
    mapping["alternative_instances_exit"] = False
    mapping["disposition"] = "OBSTRUCTED"


def missing_expanded_node(bundle: ArtifactBundle) -> None:
    bundle["bridge"]["expanded_proof_dag"]["node_ids"].remove("N38O")


def missing_expanded_edge(bundle: ArtifactBundle) -> None:
    bundle["bridge"]["expanded_edge_records"] = [row for row in bundle["bridge"]["expanded_edge_records"] if row["edge_id"] != "E13"]


def missing_internal_tag(bundle: ArtifactBundle) -> None:
    bundle["bridge"]["expanded_proof_dag"]["internal_transition_edge_ids"].remove("E14")


def missing_projection_fiber(bundle: ArtifactBundle) -> None:
    del bundle["bridge"]["node_projection"]["N37N"]


def missing_request_token(bundle: ArtifactBundle) -> None:
    bundle["bridge"]["request_tokens"] = [row for row in bundle["bridge"]["request_tokens"] if row["token_id"] != "BOUNDARY_MODEL_EXIT"]


def duplicate_request_token(bundle: ArtifactBundle) -> None:
    bundle["bridge"]["request_tokens"].append(copy.deepcopy(bundle["bridge"]["request_tokens"][0]))


def misclassified_request_token(bundle: ArtifactBundle) -> None:
    token = next(row for row in bundle["bridge"]["request_tokens"] if row["token_id"] == "INDUCED_SHIFT_EXIT")
    token["disposition"] = "OBSTRUCTED"


def firewall_loses_auxiliary_typing(bundle: ArtifactBundle) -> None:
    edge_record = next(row for row in bundle["bridge"]["expanded_edge_records"] if row["edge_id"] == "E22")
    edge_record["edge_kind"] = "CONTRACT_EXIT"
    firewall = bundle["bridge"]["non_domain_firewall_edges"][0]
    del firewall["role"]
    del firewall["historical_boundary_path"]["sha256"]


def firewall_nonempty_scope_fibers(bundle: ArtifactBundle) -> None:
    firewall = bundle["bridge"]["non_domain_firewall_edges"][0]
    firewall["request_token_ids"] = ["CHARACTER_FROZEN_FAMILY"]
    firewall["repair_class_coverage_ids"] = ["character"]


def firewall_granted_a14_sigma16_coverage(bundle: ArtifactBundle) -> None:
    token = next(row for row in bundle["bridge"]["request_tokens"] if row["token_id"] == "CHARACTER_FROZEN_FAMILY")
    token["obstruction_endpoint_ids"].append("NX")
    token["obstruction_edge_ids"].append("E22")
    coverage = next(row for row in bundle["bridge"]["repair_class_coverage"] if row["repair_class"] == "character")
    coverage["obstruction_endpoint_ids"].append("NX")
    coverage["obstruction_edge_ids"].append("E22")


MUTATIONS: list[tuple[str, Mutation]] = [
    ("missing_edge", missing_edge),
    ("wrong_object_transfer", wrong_object_transfer),
    ("marker_swap", marker_swap),
    ("determinant_category_swap", determinant_category_swap),
    ("post_hoc_representation", post_hoc_representation),
    ("stale_provenance", stale_provenance),
    ("prospective_predecessor_independence_claim", prospective_predecessor_independence_claim),
    ("stale_canonical_p38_object_code", stale_canonical_p38_object_code),
    ("unregistered_successor_insertion", unregistered_successor_insertion),
    ("existing_entry_misclassification", existing_entry_misclassification),
    ("false_empty_registry", false_empty_registry),
    ("ranked_or_proposed_successor", ranked_or_proposed_successor),
    ("bad_transfer_mode", bad_transfer_mode),
    ("illegal_carry_and_reset_semantics", illegal_carry_and_reset_semantics),
    ("illegal_e36_37_object_carry", illegal_e36_37_object_carry),
    ("illegal_e36_37_marker_carry", illegal_e36_37_marker_carry),
    ("illegal_e36_37_operator_owner_carry", illegal_e36_37_operator_owner_carry),
    ("illegal_e36_37_determinant_owner_carry", illegal_e36_37_determinant_owner_carry),
    ("exit_as_obstruction", exit_as_obstruction),
    ("missing_expanded_node", missing_expanded_node),
    ("missing_expanded_edge", missing_expanded_edge),
    ("missing_internal_tag", missing_internal_tag),
    ("missing_projection_fiber", missing_projection_fiber),
    ("missing_request_token", missing_request_token),
    ("duplicate_request_token", duplicate_request_token),
    ("misclassified_request_token", misclassified_request_token),
    ("firewall_loses_auxiliary_typing", firewall_loses_auxiliary_typing),
    ("firewall_nonempty_scope_fibers", firewall_nonempty_scope_fibers),
    ("firewall_granted_a14_sigma16_coverage", firewall_granted_a14_sigma16_coverage),
]


def invoke(script: Path, packet: Path, contract: Path, input_lock: Path, empty_fixture: Path, dag_bridge: Path, output: Path) -> tuple[int, dict[str, Any]]:
    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            str(script),
            "--packet",
            str(packet),
            "--contract",
            str(contract),
            "--input-lock",
            str(input_lock),
            "--empty-registry-fixture",
            str(empty_fixture),
            "--dag-bridge",
            str(dag_bridge),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.stdout or completed.stderr:
        raise RuntimeError(f"unexpected evaluator output: {script.name}: {completed.stdout!r} {completed.stderr!r}")
    return completed.returncode, json.loads(output.read_text(encoding="utf-8"))


def failed_checks(payload: dict[str, Any]) -> list[str]:
    return [row["name"] for row in payload.get("checks", []) if not row.get("passed")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", required=True)
    parser.add_argument("--contract", required=True)
    parser.add_argument("--input-lock", required=True)
    parser.add_argument("--empty-registry-fixture", required=True)
    parser.add_argument("--dag-bridge", required=True)
    parser.add_argument("--main-evaluator", required=True)
    parser.add_argument("--independent-evaluator", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    packet_path = Path(args.packet).resolve()
    contract_path = Path(args.contract).resolve()
    input_lock_path = Path(args.input_lock).resolve()
    empty_fixture_path = Path(args.empty_registry_fixture).resolve()
    dag_bridge_path = Path(args.dag_bridge).resolve()
    main_script = Path(args.main_evaluator).resolve()
    independent_script = Path(args.independent_evaluator).resolve()
    baseline_packet = json.loads(packet_path.read_text(encoding="utf-8"))
    baseline_contract = json.loads(contract_path.read_text(encoding="utf-8"))
    baseline_bridge = json.loads(dag_bridge_path.read_text(encoding="utf-8"))
    baseline_artifacts = {"bridge": baseline_bridge, "contract": baseline_contract, "packet": baseline_packet}

    rows: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="paper39_mutation_") as temporary:
        temp = Path(temporary)
        main_code, main_base = invoke(main_script, packet_path, contract_path, input_lock_path, empty_fixture_path, dag_bridge_path, temp / "main_base.json")
        independent_code, independent_base = invoke(independent_script, packet_path, contract_path, input_lock_path, empty_fixture_path, dag_bridge_path, temp / "independent_base.json")
        baseline = {
            "independent_accepts": independent_code == 0 and independent_base.get("all_pass") is True,
            "main_accepts": main_code == 0 and main_base.get("all_pass") is True,
            "science_projection_equal": main_base.get("science_projection_sha256") == independent_base.get("science_projection_sha256"),
        }
        for index, (name, mutate) in enumerate(MUTATIONS):
            changed: ArtifactBundle = {
                "bridge": copy.deepcopy(baseline_bridge),
                "contract": copy.deepcopy(baseline_contract),
                "packet": copy.deepcopy(baseline_packet),
            }
            mutate(changed)
            mutated_packet_path = temp / f"packet_{index:02d}.json"
            mutated_contract_path = temp / f"contract_{index:02d}.json"
            mutated_packet_path.write_bytes(canonical_bytes(changed["packet"]))
            mutated_bridge_path = dag_bridge_path
            if changed["bridge"] != baseline_bridge:
                mutated_bridge_path = temp / f"bridge_{index:02d}.json"
                bridge_bytes = canonical_bytes(changed["bridge"])
                mutated_bridge_path.write_bytes(bridge_bytes)
                changed["contract"]["expanded_dag_bridge"]["sha256"] = hashlib.sha256(bridge_bytes).hexdigest()
            mutated_contract_path.write_bytes(canonical_bytes(changed["contract"]))
            main_code, main_result = invoke(main_script, mutated_packet_path, mutated_contract_path, input_lock_path, empty_fixture_path, mutated_bridge_path, temp / f"main_{index:02d}.json")
            independent_code, independent_result = invoke(independent_script, mutated_packet_path, mutated_contract_path, input_lock_path, empty_fixture_path, mutated_bridge_path, temp / f"independent_{index:02d}.json")
            row = {
                "independent_failed_checks": failed_checks(independent_result),
                "independent_rejected": independent_code != 0 and independent_result.get("all_pass") is False,
                "main_failed_checks": failed_checks(main_result),
                "main_rejected": main_code != 0 and main_result.get("all_pass") is False,
                "mutation": name,
                "mutated_artifacts": [artifact for artifact in ("packet", "contract", "bridge") if changed[artifact] != baseline_artifacts[artifact]],
            }
            rows.append(row)

    all_pass = all(baseline.values()) and all(row["main_rejected"] and row["independent_rejected"] for row in rows)
    result = {
        "all_pass": all_pass,
        "baseline": baseline,
        "counts": {
            "independent_rejections": sum(row["independent_rejected"] for row in rows),
            "main_rejections": sum(row["main_rejected"] for row in rows),
            "mutations": len(rows),
        },
        "mutations": rows,
        "schema": "paper39-adversarial-tests-v1",
    }
    Path(args.output).write_bytes(canonical_bytes(result))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
