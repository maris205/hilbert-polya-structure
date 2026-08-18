#!/usr/bin/env python3
"""Independent node-level Route-A v0.2 expectation validator."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml


REQUIRED = ("skill", "skill_version", "candidate_id", "evaluation_state", "evaluation_date", "source_commit",
            "parent_phase2_manifest_sha256", "code_commit", "artifact_path_base", "freeze_note", "source_lock", "a0",
            "a1", "a2", "a3", "a4", "adversarial_controls", "projection_firewall", "authority_integration",
            "expected_route_tuple", "overall_expectation", "claim_boundary", "blocking_conditions", "next_smallest_test",
            "route_b", "route_b_invocation_allowed", "branch_status")
LOCKED_RAW_DIGEST = "d02ce9f054567aa6d0c8e099797920ea9d29bbcebc062c4874b11baaab6b9c01"


class RouteDisposition(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def reject_duplicate_nodes(node):
    if isinstance(node, yaml.MappingNode):
        seen = set()
        for key_node, value_node in node.value:
            if not isinstance(key_node, yaml.ScalarNode):
                raise ValueError("non-scalar key")
            if key_node.value in seen:
                raise ValueError("duplicate")
            seen.add(key_node.value)
            reject_duplicate_nodes(value_node)
    elif isinstance(node, yaml.SequenceNode):
        for child in node.value:
            reject_duplicate_nodes(child)


def independently_validate(path: Path):
    raw = path.read_text(encoding="utf-8")
    root_node = yaml.compose(raw, Loader=yaml.BaseLoader)
    reject_duplicate_nodes(root_node)
    data = yaml.safe_load(raw)
    if type(data) is not dict or tuple(sorted(data)) != tuple(sorted(REQUIRED)):
        raise ValueError("key set")
    scalar_expectations = {
        "skill": "route-a-evaluator", "skill_version": "0.2.0",
        "candidate_id": "P45-ALLH-RETRACTIONS-PREAUTHORITY",
        "evaluation_state": "NOT_RUN_PREAUTHORITY_EXPECTATION",
        "overall_expectation": "ROUTE_A_REJECTED_NOT_EVALUATED",
        "branch_status": "PREAUTHORITY_HOLD_FOR_INDEPENDENT_EVALUATION",
    }
    if any(data.get(k) != v for k, v in scalar_expectations.items()):
        if data.get("evaluation_state") != scalar_expectations["evaluation_state"]:
            raise RouteDisposition("ROUTE_EXPECTATION_RETYPE")
        if data.get("overall_expectation") != scalar_expectations["overall_expectation"] or data.get("branch_status") != scalar_expectations["branch_status"]:
            raise RouteDisposition("UNAUTHORIZED_ROUTE_TERMINAL")
        raise ValueError("scalar")
    expected = ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"]
    if data.get("expected_route_tuple") != expected:
        raise ValueError("tuple")
    if type(data.get("route_b_invocation_allowed")) is not bool or data["route_b_invocation_allowed"]:
        raise ValueError("route B")
    route_b = data.get("route_b")
    if type(route_b) is not dict or set(route_b) != {"invocation_allowed", "reason"} or route_b["invocation_allowed"] is not False:
        raise ValueError("route B object")
    for i in range(5):
        item = data[f"a{i}"]
        if type(item) is not dict or item.get("expected_verdict") != expected[i]:
            raise ValueError("A verdict")
    auth = data.get("authority_integration")
    if type(auth) is not dict or auth.get("authority_writes_by_this_stage") != 0 or auth.get("git_operations_by_this_stage") != 0:
        raise ValueError("authority")
    if type(data.get("blocking_conditions")) is not list or len(data["blocking_conditions"]) < 6:
        raise ValueError("blockers")
    expected_nested = {
        "source_lock": {"candidate_definition", "family", "phase_space", "dense_domain", "dynamics", "parameters",
                        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                        "regularization_order", "main_theorem_marker", "function_space", "roof_function",
                        "potential_function", "cocycle", "cutoff", "precision", "training_data", "allowed_data",
                        "forbidden_data", "artifact_paths"},
        "adversarial_controls": {"controls_required", "proves_too_much_risk", "expected_verdict"},
        "projection_firewall": {"source_type", "block_type", "eigenvalue_type", "singular_type", "projection_type",
                                "target_comparator_type", "required_fields", "declared_repairs_are_exhaustive"},
        "authority_integration": {"status", "authority_writes_by_this_stage", "git_operations_by_this_stage", "root_authorization_required"},
        "route_b": {"invocation_allowed", "reason"},
    }
    for key, exact_keys in expected_nested.items():
        if type(data[key]) is not dict or set(data[key]) != exact_keys:
            raise ValueError("recursive keys:" + key)
    expected_block_keys = [
        {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "controls", "artifacts"},
        {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics_expected", "artifacts"},
        {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics_expected", "artifacts"},
        {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "artifacts"},
        {"expected_verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics_expected", "artifacts"},
    ]
    expected_artifacts = [
        ["SOURCE_LOCK.md", "OBJECT_MARKER_OPERATOR_CONTRACT.md", "EXACT_WITNESS_LEDGER.md"],
        ["OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "LITERATURE_NOVELTY_AUDIT.md"],
        ["OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "THEOREM_FALSIFIERS.md"],
        ["PROOF_PACKAGE.md", "LITERATURE_NOVELTY_AUDIT.md", "RESEARCH_QUESTION_BRIEF.md"],
        ["OBJECT_MARKER_OPERATOR_CONTRACT.md", "PROOF_PACKAGE.md", "ROUTE_EXPECTATION.yaml"],
    ]
    for number in range(5):
        if set(data[f"a{number}"]) != expected_block_keys[number] or data[f"a{number}"]["artifacts"] != expected_artifacts[number]:
            raise ValueError("block recursive schema")
    if hashlib.sha256(raw.encode("utf-8")).hexdigest() != LOCKED_RAW_DIGEST:
        raise ValueError("independent frozen object digest")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    options = parser.parse_args()
    try:
        independently_validate(options.root / "inputs" / "preauthority" / "ROUTE_EXPECTATION.yaml")
        print('{"consumer":"R_INDEPENDENT","verdict":"PASS"}')
        return 0
    except RouteDisposition as exc:
        print(json.dumps({"consumer_key": "R_INDEPENDENT", "outcome": "REJECT", "exit_code": 2,
                          "rejection_code": exc.code,
                          "result_digest": hashlib.sha256(("R_INDEPENDENT\n" + exc.code + "\n").encode()).hexdigest()},
                         sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:
        print('{"error":{"code":"ROUTE_SCHEMA_ERROR","detail":"redacted","stage":"R_INDEPENDENT"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
