#!/usr/bin/env python3
"""Main strict Route-A v0.2 expectation validator."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml


TOP_KEYS = {"skill", "skill_version", "candidate_id", "evaluation_state", "evaluation_date", "source_commit",
            "parent_phase2_manifest_sha256", "code_commit", "artifact_path_base", "freeze_note", "source_lock",
            "a0", "a1", "a2", "a3", "a4", "adversarial_controls", "projection_firewall", "authority_integration",
            "expected_route_tuple", "overall_expectation", "claim_boundary", "blocking_conditions", "next_smallest_test",
            "route_b", "route_b_invocation_allowed", "branch_status"}
ROUTE_SHA256 = "d02ce9f054567aa6d0c8e099797920ea9d29bbcebc062c4874b11baaab6b9c01"
SOURCE_LOCK_KEYS = {"candidate_definition", "family", "phase_space", "dense_domain", "dynamics", "parameters",
                    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                    "regularization_order", "main_theorem_marker", "function_space", "roof_function",
                    "potential_function", "cocycle", "cutoff", "precision", "training_data", "allowed_data",
                    "forbidden_data", "artifact_paths"}
BLOCK_KEYS = {
    "a0": {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "controls", "artifacts"},
    "a1": {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics_expected", "artifacts"},
    "a2": {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics_expected", "artifacts"},
    "a3": {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "artifacts"},
    "a4": {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics_expected", "artifacts"},
}
ARTIFACTS = {
    "a0": ["SOURCE_LOCK.md", "OBJECT_MARKER_OPERATOR_CONTRACT.md", "EXACT_WITNESS_LEDGER.md"],
    "a1": ["OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "LITERATURE_NOVELTY_AUDIT.md"],
    "a2": ["OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "THEOREM_FALSIFIERS.md"],
    "a3": ["PROOF_PACKAGE.md", "LITERATURE_NOVELTY_AUDIT.md", "RESEARCH_QUESTION_BRIEF.md"],
    "a4": ["OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "ROUTE_EXPECTATION.yaml"],
}


class RouteReject(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError("duplicate YAML member")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_route(path: Path):
    raw = path.read_text(encoding="utf-8")
    data = yaml.load(raw, Loader=UniqueLoader)
    if type(data) is not dict or set(data) != TOP_KEYS:
        raise ValueError("top shape")
    if data["skill"] != "route-a-evaluator" or data["skill_version"] != "0.2.0":
        raise ValueError("version")
    if data["evaluation_state"] != "NOT_RUN_PREAUTHORITY_EXPECTATION":
        raise RouteReject("ROUTE_EXPECTATION_RETYPE")
    if data["candidate_id"] != "P45-ALLH-RETRACTIONS-PREAUTHORITY":
        raise ValueError("identity")
    if data["expected_route_tuple"] != ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"]:
        raise ValueError("tuple")
    if (data["overall_expectation"] != "ROUTE_A_REJECTED_NOT_EVALUATED" or
            data["route_b_invocation_allowed"] is not False or
            data["branch_status"] != "PREAUTHORITY_HOLD_FOR_INDEPENDENT_EVALUATION"):
        raise RouteReject("UNAUTHORIZED_ROUTE_TERMINAL")
    if data["route_b"] != {"invocation_allowed": False, "reason": data["route_b"].get("reason")}:
        raise ValueError("terminal")
    if data["authority_integration"] != {"status": "PREAUTHORITY_RESULT_FREE_NO_WRITE", "authority_writes_by_this_stage": 0,
                                         "git_operations_by_this_stage": 0, "root_authorization_required": True}:
        raise ValueError("authority")
    source_lock = data["source_lock"]
    if type(source_lock) is not dict or set(source_lock) != SOURCE_LOCK_KEYS:
        raise ValueError("source lock recursive keys")
    if set(source_lock["parameters"]) != {"h", "s", "sigma", "k", "q"}:
        raise ValueError("source parameters")
    if type(source_lock["allowed_data"]) is not list or type(source_lock["forbidden_data"]) is not list:
        raise ValueError("source lists")
    if source_lock["artifact_paths"] != ["RESEARCH_QUESTION_BRIEF.md", "SOURCE_LOCK.md", "LITERATURE_NOVELTY_AUDIT.md",
                                         "OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "THEOREM_FALSIFIERS.md",
                                         "EXACT_WITNESS_LEDGER.md", "METHODOLOGY_BLUEPRINT.md", "EXPERIMENT_CONTRACT.json",
                                         "EXPERIMENT_CONTRACT_SCHEMA.json", "EXPERIMENT_PLAN.md", "MUTATION_REGISTRY.json",
                                         "MUTATION_REGISTRY_SCHEMA.json", "SELECTION_AND_PROVENANCE.md"]:
        raise ValueError("source artifact provenance")
    for index, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        block = data[key]
        if type(block) is not dict or set(block) != BLOCK_KEYS[key] or block.get("expected_verdict") != data["expected_route_tuple"][index]:
            raise ValueError("A block")
        if block.get("artifacts") != ARTIFACTS[key]:
            raise ValueError("artifacts")
        nested_key = "analytic_structure" if key == "a3" else "metrics_expected" if key != "a0" else None
        if nested_key and (type(block[nested_key]) is not dict or not block[nested_key]):
            raise ValueError("nested metrics")
    if (set(data["adversarial_controls"]) != {"controls_required", "proves_too_much_risk", "expected_verdict"} or
            set(data["projection_firewall"]) != {"source_type", "block_type", "eigenvalue_type", "singular_type",
                                                    "projection_type", "target_comparator_type", "required_fields",
                                                    "declared_repairs_are_exhaustive"}):
        raise ValueError("control/firewall recursive keys")
    if data["authority_integration"] != {"status": "PREAUTHORITY_RESULT_FREE_NO_WRITE", "authority_writes_by_this_stage": 0,
                                         "git_operations_by_this_stage": 0, "root_authorization_required": True}:
        raise ValueError("authority exact object")
    if hashlib.sha256(raw.encode("utf-8")).hexdigest() != ROUTE_SHA256:
        raise ValueError("full recursive value/provenance digest")
    if any(token in (data["branch_status"], data["overall_expectation"]) for token in ("GO_EVALUATED", "STOP_DUPLICATE")):
        raise ValueError("publication terminal")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ns = ap.parse_args()
    try:
        strict_route(ns.root / "inputs" / "preauthority" / "ROUTE_EXPECTATION.yaml")
        print('{"consumer":"R_MAIN","verdict":"PASS"}')
        return 0
    except RouteReject as exc:
        print(json.dumps({"consumer_key": "R_MAIN", "outcome": "REJECT", "exit_code": 2,
                          "rejection_code": exc.code,
                          "result_digest": hashlib.sha256(("R_MAIN\n" + exc.code + "\n").encode()).hexdigest()},
                         sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:
        print('{"error":{"code":"ROUTE_SCHEMA_ERROR","detail":"redacted","stage":"R_MAIN"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
