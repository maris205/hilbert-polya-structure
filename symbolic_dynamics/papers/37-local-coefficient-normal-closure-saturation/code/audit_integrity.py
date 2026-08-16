#!/usr/bin/env python3
"""Independent full-tree audit for the Paper 37 exact integration."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_CARD = ROOT / "evaluations" / "route_a" / "SD-C39" / "2026-08-15.yaml"
LEDGER = RESULTS / "SHA256SUMS.txt"
INTEGRITY_AUDIT = RESULTS / "integrity_audit.json"
PAPER_MANIFEST = ROOT / "PAPER_MANIFEST.sha256"

EXPECTED_SCIENCE_SHA256 = (
    "b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e"
)
EXPECTED_ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]
EXPECTED_SOURCE_CORE_SHA256 = (
    "f127037786d0ca3eea3125d9b94f924e4534cd33e7252e94e2c5ef373378b116"
)
EXPECTED_EVALUATOR_CORE_SHA256 = (
    "eae6fad20e45fce97d82113552ec7a8c13f33a398cda90b3948ad11af39c4b09"
)
EXPECTED_SOURCE_LOCK_SHA256 = (
    "d725f03caffc6c5fab916314df25097b7383af7494287052496516deab0dcb4e"
)
EXPECTED_BRIDGE_HASHES = {
    "/tmp/paper37_exact_prototype/EXPERIMENT_PLAN.md": "9ec8ae5442c6b1c7541dc8b8e4796b041a4720ac0009a1dd46e8f17510531546",
    "/tmp/paper37_exact_prototype/PREREGISTRATION.md": "8906a3700f37496e032778306e9a001ba9759919b17b74323c4446fa5300c212",
    "/tmp/paper37_exact_prototype/independent_evaluator.py": "eae6fad20e45fce97d82113552ec7a8c13f33a398cda90b3948ad11af39c4b09",
    "/tmp/paper37_exact_prototype/run_exact.py": "d01df2a017b026a8704718fa516da762fe552498eb3e9bd9b9010cb51a66f8ef",
    "/tmp/paper37_exact_prototype/source_core.py": "f127037786d0ca3eea3125d9b94f924e4534cd33e7252e94e2c5ef373378b116",
    "/tmp/paper37_research_package.md": "e39a8c89975670926461c46c9c82df58e886647e49fb77244fc530d3a060f3aa",
    "/tmp/paper37_source_lock.md": "d725f03caffc6c5fab916314df25097b7383af7494287052496516deab0dcb4e",
}
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
FROZEN_ROOT_AUTHORITY = {
    "SOURCE_LOCK.md",
    "PREREGISTRATION.md",
    "DERIVATION_PACKAGE.md",
    "PROOF_PACKAGE.md",
    "LITERATURE_AUDIT.md",
}
STABLE_PLAN_POINTERS = {
    "experiments/PREREGISTRATION.md",
    "experiments/EXPERIMENT_PLAN.md",
}
A2_METRICS = [
    "zero_error_train",
    "zero_error_validation",
    "zero_error_test",
    "extra_zero_count",
    "missing_zero_count",
    "root_count_discrepancy",
    "cutoff_drift",
    "precision_drift",
    "control_margin",
]
A4_REQUIRED_METRICS = A2_METRICS[:6]
TOP_LEVEL_KEYS = {
    "skill", "skill_version", "candidate_id", "source_commit", "code_commit",
    "evaluation_date", "artifact_path_base", "freeze_note", "source_lock",
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls", "route_tuple",
    "overall_verdict", "claim_boundary", "blocking_conditions",
    "next_smallest_test", "round2_clues", "route_b_invocation_allowed",
}
SOURCE_LOCK_KEYS = {
    "candidate_definition", "object", "family", "phase_space", "dynamics",
    "parameters", "parameter_provenance", "arithmetic_origin", "clock",
    "normalization", "determinant_convention", "regularization_order",
    "main_theorem_marker", "orbit_cutoff", "cutoff", "precision",
    "training_data", "allowed_data", "forbidden_data", "code_commit",
    "artifact_paths",
}


def canonical_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True) + "\n").encode("ascii")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes())


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def managed_files(include_anticipated: bool) -> set[str]:
    paths: set[str] = set()
    for dirname in ("code", "results", "experiments", "docs"):
        base = ROOT / dirname
        if base.exists():
            paths.update(relpath(path) for path in base.rglob("*") if path.is_file())
    evaluation = ROOT / "evaluations" / "route_a" / "SD-C39"
    if evaluation.exists():
        paths.update(relpath(path) for path in evaluation.rglob("*") if path.is_file())
    if (ROOT / "EXPERIMENT_REPORT.md").is_file():
        paths.add("EXPERIMENT_REPORT.md")
    if include_anticipated:
        paths.update({
            "results/SHA256SUMS.txt",
            "results/integrity_audit.json",
        })
    return paths


def section(text: str, start: str, end: str | None) -> str:
    start_match = re.search(rf"^{re.escape(start)}:\s*$", text, re.MULTILINE)
    if not start_match:
        return ""
    if end is None:
        return text[start_match.start():]
    end_match = re.search(rf"^{re.escape(end)}:\s*$", text[start_match.end():],
                          re.MULTILINE)
    if not end_match:
        return ""
    return text[start_match.start():start_match.end() + end_match.start()]


def direct_keys(block: str, indent: int) -> list[str]:
    pattern = re.compile(rf"^ {{{indent}}}([A-Za-z0-9_]+):(?:\s|$)", re.MULTILINE)
    return pattern.findall(block)


def duplicate_mapping_paths(text: str) -> list[str]:
    seen: dict[tuple[str, ...], set[str]] = {}
    stack: list[tuple[int, str]] = []
    duplicates: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^( *)([A-Za-z0-9_]+):(?:\s|$)", line)
        if not match:
            continue
        indent = len(match.group(1))
        key = match.group(2)
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = tuple(item[1] for item in stack)
        keys = seen.setdefault(parent, set())
        if key in keys:
            duplicates.append(".".join((*parent, key)))
        keys.add(key)
        stack.append((indent, key))
    return duplicates


def scalar(text: str, key: str, indent: int = 0) -> str | None:
    match = re.search(rf"^ {{{indent}}}{re.escape(key)}:\s*(.+?)\s*$", text,
                      re.MULTILINE)
    if not match:
        return None
    value = match.group(1)
    if len(value) >= 2 and value[0] == value[-1] == '"':
        value = value[1:-1]
    return value


def indented_list(block: str, key: str, key_indent: int) -> list[str]:
    lines = block.splitlines()
    marker = " " * key_indent + key + ":"
    for index, line in enumerate(lines):
        if line == marker:
            values = []
            item_prefix = " " * (key_indent + 2) + "- "
            for following in lines[index + 1:]:
                if following.startswith(item_prefix):
                    values.append(following[len(item_prefix):])
                elif following.strip() == "":
                    continue
                else:
                    break
            return values
    return []


def imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text("utf-8"), filename=str(path))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def text_failures(path: Path) -> list[str]:
    failures = []
    data = path.read_bytes()
    name = relpath(path)
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return [f"{name}:utf8"]
    if data.startswith(b"\xef\xbb\xbf"):
        failures.append(f"{name}:bom")
    if b"\r" in data:
        failures.append(f"{name}:line_endings")
    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        failures.append(f"{name}:eof")
    if any(line.endswith((" ", "\t")) for line in text.splitlines()):
        failures.append(f"{name}:trailing_whitespace")
    if any(ord(character) < 32 and character not in "\n\t" for character in text):
        failures.append(f"{name}:control_character")
    return failures


class Audit:
    def __init__(self) -> None:
        self.groups: dict[str, list[dict[str, object]]] = {}

    def check(self, group: str, name: str, condition: bool) -> None:
        self.groups.setdefault(group, []).append({
            "name": name,
            "passed": bool(condition),
        })

    def payload(self, ledger_entries: int, canonical_text_files: int) -> dict[str, Any]:
        groups: dict[str, Any] = {}
        passed_total = 0
        check_total = 0
        for name in sorted(self.groups):
            rows = self.groups[name]
            passed = sum(int(row["passed"]) for row in rows)
            groups[name] = {
                "passed": passed,
                "total": len(rows),
                "all_pass": passed == len(rows),
                "checks": rows,
            }
            passed_total += passed
            check_total += len(rows)
        return {
            "schema": "paper37-full-integrity-audit-v1",
            "candidate": "SD-C39",
            "groups": groups,
            "passed": passed_total,
            "total": check_total,
            "all_pass": passed_total == check_total,
            "ledger_entry_count": ledger_entries,
            "canonical_text_file_count": canonical_text_files,
            "paper_manifest_states_supported": [
                "absent_stage1",
                "present_stage2",
            ],
            "mutable_metadata_excluded_from_science": True,
        }


def validate_manifest_if_present(audit: Audit) -> bool:
    if not PAPER_MANIFEST.exists():
        audit.check("manifest_seal", "stage1_manifest_absent_or_stage2_valid", True)
        return False
    data = PAPER_MANIFEST.read_bytes()
    lines = data.decode("utf-8").splitlines()
    parsed = []
    valid_format = True
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", line)
        if not match:
            valid_format = False
            continue
        parsed.append((match.group(2), match.group(1)))
    expected_paths = sorted(
        relpath(path) for path in ROOT.rglob("*")
        if path.is_file() and path.resolve() != PAPER_MANIFEST.resolve()
    )
    actual_paths = [path for path, _ in parsed]
    hashes_match = valid_format and all(
        (ROOT / path).is_file() and file_sha256(ROOT / path) == digest
        for path, digest in parsed
    )
    audit.check("manifest_seal", "stage1_manifest_absent_or_stage2_valid",
                valid_format and actual_paths == expected_paths
                and actual_paths == sorted(set(actual_paths)) and hashes_match)
    return True


def run_audit(prepare: bool, hide_external_provenance: bool) -> dict[str, Any]:
    audit = Audit()
    anticipated = managed_files(include_anticipated=True)

    research = json.loads((ROOT / "docs" / "RESEARCH_LOCK.json").read_text("utf-8"))
    audit.check("research_locks", "frozen_root_authority_exact_set",
                set(research["root_authority_files"]) == FROZEN_ROOT_AUTHORITY)
    audit.check("research_locks", "stable_plan_pointer_exact_set",
                set(research["stable_plan_pointers"]) == STABLE_PLAN_POINTERS)
    root_hashes = all(
        (ROOT / path).is_file() and file_sha256(ROOT / path) == digest
        for path, digest in research["root_authority_files"].items()
    )
    plan_hashes = all(
        (ROOT / path).is_file() and file_sha256(ROOT / path) == digest
        for path, digest in research["stable_plan_pointers"].items()
    )
    bridge_map_frozen = research["bridge_inputs"] == EXPECTED_BRIDGE_HASHES
    bridge_hashes_if_available = all(
        hide_external_provenance
        or not Path(path).is_file()
        or file_sha256(Path(path)) == digest
        for path, digest in research["bridge_inputs"].items()
    )
    audit.check("research_locks", "root_authority_hashes", root_hashes)
    audit.check("research_locks", "stable_plan_hashes", plan_hashes)
    audit.check("research_locks", "bridge_hash_map_frozen", bridge_map_frozen)
    audit.check("research_locks", "available_bridge_hashes_match",
                bridge_hashes_if_available)
    audit.check("research_locks", "authority_source_lock_frozen",
                file_sha256(ROOT / "SOURCE_LOCK.md") == EXPECTED_SOURCE_LOCK_SHA256)
    audit.check("research_locks", "bridged_scientific_cores_frozen",
                file_sha256(ROOT / "code" / "source" / "source_core.py")
                == EXPECTED_SOURCE_CORE_SHA256
                and file_sha256(ROOT / "code" / "evaluator"
                                / "independent_evaluator.py")
                == EXPECTED_EVALUATOR_CORE_SHA256)
    audit.check("research_locks", "science_hash_frozen",
                research["expected_scientific_aggregate_sha256"]
                == EXPECTED_SCIENCE_SHA256)
    dependency = json.loads((ROOT / "docs" / "DEPENDENCY_LOCK.json").read_text("utf-8"))
    audit.check("research_locks", "standard_library_only",
                dependency["third_party_packages"] == []
                and dependency["network_required"] is False)

    source_paths = sorted((ROOT / "code" / "source").glob("*.py"))
    evaluator_paths = sorted((ROOT / "code" / "evaluator").glob("*.py"))
    source_imports = set().union(*(imports(path) for path in source_paths))
    evaluator_imports = set().union(*(imports(path) for path in evaluator_paths))
    audit.check("source_firewall", "physical_directories_disjoint",
                set(source_paths).isdisjoint(evaluator_paths))
    audit.check("source_firewall", "source_does_not_import_evaluator",
                "independent_evaluator" not in source_imports
                and "evaluate_packet" not in source_imports
                and "evaluate_route_a" not in source_imports)
    audit.check("source_firewall", "evaluator_does_not_import_source",
                "source_core" not in evaluator_imports
                and "emit_packet" not in evaluator_imports)
    prohibited_imports = {"socket", "requests", "urllib", "sympy", "numpy"}
    audit.check("source_firewall", "source_has_no_network_or_target_library",
                not (source_imports & prohibited_imports))
    boundary = json.loads((RESULTS / "source_evaluator_boundary.json").read_text("utf-8"))
    audit.check("source_firewall", "boundary_certificate_all_true",
                boundary["physical_directories_disjoint"] is True
                and boundary["source_imports_evaluator"] is False
                and boundary["evaluator_imports_source"] is False
                and boundary["transport"] == "canonical_json_subprocess_stdin_stdout")

    route_text = ROUTE_CARD.read_text("utf-8")
    top_keys = set(direct_keys(route_text, 0))
    source_block = section(route_text, "source_lock", "a0")
    source_keys = set(direct_keys(source_block, 2))
    audit.check("route_schema", "no_duplicate_mapping_keys",
                not duplicate_mapping_paths(route_text))
    audit.check("route_schema", "top_level_required_keys_exact",
                top_keys == TOP_LEVEL_KEYS)
    audit.check("route_schema", "source_lock_required_keys_exact",
                source_keys == SOURCE_LOCK_KEYS)
    audit.check("route_schema", "skill_and_version",
                scalar(route_text, "skill") == "route-a-evaluator"
                and scalar(route_text, "skill_version") == "0.2.0")
    audit.check("route_schema", "candidate_and_date",
                scalar(route_text, "candidate_id") == "SD-C39"
                and scalar(route_text, "evaluation_date") == "2026-08-15")

    source_commit = scalar(route_text, "source_commit")
    code_commit = scalar(route_text, "code_commit")
    nested_commit = scalar(source_block, "code_commit", 2)
    manifest_present = validate_manifest_if_present(audit)
    if manifest_present:
        commit_valid = bool(re.fullmatch(r"[0-9a-f]{40}", source_commit or ""))
        commit_valid = commit_valid and source_commit == code_commit == nested_commit
        freeze_valid = "sealed" in route_text.lower()
    else:
        commit_valid = source_commit == code_commit == nested_commit == PENDING
        freeze_valid = ("Stage 1" in route_text and "Stage 2" in route_text
                        and "metadata-only" in route_text)
    audit.check("route_schema", "paired_provenance_triple_valid", commit_valid)
    audit.check("route_schema", "freeze_note_stage_valid", freeze_valid)

    expected_section_values = {
        "a0": ("A0_STRUCTURAL_ARITHMETIC_RELATION", "PROVED"),
        "a1": ("A1_FAIL", "REFUTED"),
        "a2": ("A2_ANALYTIC_DETERMINANT", "PROVED"),
        "a3": ("A3_FAIL", "STOP_SCOPED"),
        "a4": ("A4_FAIL", "STOP_SCOPED"),
    }
    section_bounds = {"a0": "a1", "a1": "a2", "a2": "a3",
                      "a3": "a4", "a4": "adversarial_controls"}
    for name, (verdict, evidence) in expected_section_values.items():
        block = section(route_text, name, section_bounds[name])
        required = {"verdict", "evidence_status", "strongest_evidence",
                    "strongest_failure", "artifacts"}
        audit.check("route_schema", f"{name}_required_keys",
                    required.issubset(set(direct_keys(block, 2))))
        audit.check("route_schema", f"{name}_enums",
                    scalar(block, "verdict", 2) == verdict
                    and scalar(block, "evidence_status", 2) == evidence)

    a2_block = section(route_text, "a2", "a3")
    a4_block = section(route_text, "a4", "adversarial_controls")
    for key in A2_METRICS:
        value = scalar(a2_block, key, 4)
        audit.check("route_metrics", f"a2_{key}_not_applicable",
                    isinstance(value, str) and value.startswith("not_applicable; "))
    audit.check("route_metrics", "a2_target_zero_data_false",
                scalar(a2_block, "target_zero_data_used", 4) == "false")
    for key in A4_REQUIRED_METRICS:
        value = scalar(a4_block, key, 4)
        audit.check("route_metrics", f"a4_{key}_not_applicable",
                    isinstance(value, str) and value.startswith("not_applicable; "))
    audit.check("route_metrics", "a4_target_zero_data_false",
                scalar(a4_block, "target_zero_data_used", 4) == "false")
    a3_block = section(route_text, "a3", "a4")
    audit.check("route_metrics", "weil_compression_not_testable",
                "weil_compression:" in a3_block
                and "status: NOT_TESTABLE" in a3_block
                and re.search(r"^    reason: .+", a3_block, re.MULTILINE) is not None)

    adversarial = section(route_text, "adversarial_controls", "route_tuple")
    audit.check("route_schema", "proves_too_much_realized",
                scalar(adversarial, "proves_too_much_risk", 2) == "REALIZED"
                and scalar(adversarial, "verdict", 2) == "STOP_PROVES_TOO_MUCH")
    route_tuple = indented_list(route_text, "route_tuple", 0)
    audit.check("route_schema", "route_tuple_exact", route_tuple == EXPECTED_ROUTE_TUPLE)
    audit.check("route_schema", "overall_and_route_b",
                scalar(route_text, "overall_verdict") == "ROUTE_A_REJECTED"
                and scalar(route_text, "route_b_invocation_allowed") == "false")

    artifact_paths = indented_list(source_block, "artifact_paths", 2)
    audit.check("route_references", "artifact_paths_unique",
                len(artifact_paths) == len(set(artifact_paths)))
    audit.check("route_references", "artifact_paths_concrete",
                all(not path.endswith("/") and "*" not in path for path in artifact_paths))
    audit.check("route_references", "artifact_paths_exact_managed_set",
                set(artifact_paths) == anticipated)
    missing_allowed = {"results/SHA256SUMS.txt", "results/integrity_audit.json"}
    refs_exist = all((ROOT / path).is_file() or (prepare and path in missing_allowed)
                     for path in artifact_paths)
    audit.check("route_references", "artifact_paths_exist", refs_exist)
    all_route_refs = {
        item for item in re.findall(r"^    - (.+)$", route_text, re.MULTILINE)
        if item.startswith(("code/", "results/", "docs/", "experiments/",
                            "evaluations/"))
    }
    audit.check("route_references", "section_artifact_refs_exist",
                all((ROOT / path).is_file() or (prepare and path in missing_allowed)
                    for path in all_route_refs))

    science_bytes = (RESULTS / "scientific_results.json").read_bytes()
    science = json.loads(science_bytes)
    audit.check("science", "canonical_scientific_sha256",
                sha256(science_bytes) == EXPECTED_SCIENCE_SHA256)
    audit.check("science", "canonical_scientific_json",
                canonical_bytes(science) == science_bytes)
    checks = science["check_summary"]
    controls = science["control_summary"]
    audit.check("science", "evaluator_assertions_131",
                checks["passed"] == checks["total"] == 131)
    audit.check("science", "canonical_control_counts",
                controls["affine_parameter_rows"] == 8
                and controls["random_one_relator_rows"] == 48
                and controls["random_direct_cancellations"] == 9
                and controls["random_mixed_failures_after_direct_cancellation"] == 9
                and controls["random_two_relator_presentations"] == 24
                and controls["random_presentations_all_direct"] == 2)
    formula_ok = True
    for row in science["affine_results"]:
        exponent = int(row["exponent"])
        if exponent >= 2:
            observed = int(row["mixed"]["shortest_mixed_leak"]["first_supertrace"])
            formula_ok = formula_ok and observed == -4 * exponent**4 * (exponent - 1)
    audit.check("science", "mixed_witness_formula_all_r_ge_2", formula_ok)
    run_science = [
        (RESULTS / "runs" / name / "scientific_results.json").read_bytes()
        for name in ("A", "B", "C")
    ]
    run_route = [
        (RESULTS / "runs" / name / "route_evaluation.json").read_bytes()
        for name in ("A", "B", "C")
    ]
    audit.check("science", "fresh_ab_cold_c_science_identity",
                run_science[0] == run_science[1] == run_science[2] == science_bytes)
    audit.check("science", "fresh_ab_cold_c_route_identity",
                run_route[0] == run_route[1] == run_route[2]
                == (RESULTS / "route_evaluation.json").read_bytes())
    metadata = json.loads((RESULTS / "metadata_stability.json").read_text("utf-8"))
    audit.check("science", "metadata_four_states_exact",
                metadata["state_order"] == ["absent", "null", "empty", "populated"]
                and metadata["scientific_bytes_stable"] is True
                and metadata["route_bytes_stable"] is True
                and len(metadata["states"]) == 4)
    reproducibility = json.loads(
        (RESULTS / "reproducibility_certificate.json").read_text("utf-8")
    )
    audit.check("science", "cold_copy_removed_and_no_environment_leak",
                reproducibility["cold_copy_removed"] is True
                and reproducibility["environment_metadata_excluded_from_scientific_payload"] is True)
    idempotence = json.loads((RESULTS / "idempotence_certificate.json").read_text("utf-8"))
    audit.check("science", "primary_materialization_idempotent",
                idempotence["second_materialization_byte_identical"] is True
                and idempotence["second_materialization_changed_paths"] == [])

    manifest_certificate = json.loads(
        (RESULTS / "manifest_metadata_stability.json").read_text("utf-8")
    )
    audit.check("manifest_seal", "manifest_absent_present_science_stable",
                manifest_certificate["scientific_bytes_stable"] is True)
    audit.check("manifest_seal", "manifest_absent_present_route_stable",
                manifest_certificate["route_bytes_stable"] is True
                and {row["state"] for row in manifest_certificate["simulated_states"]}
                == {"absent", "present"})
    audit.check("manifest_seal", "manifest_excluded_from_immutable_sets",
                manifest_certificate["excluded_from_immutable_ledger"] is True
                and manifest_certificate["excluded_from_canonical_text_count"] is True)

    exact_set = json.loads((RESULTS / "exact_result_set.json").read_text("utf-8"))
    expected_results = exact_set["paths"]
    actual_results = sorted(
        relpath(path) for path in RESULTS.rglob("*") if path.is_file()
    )
    if prepare:
        actual_for_check = sorted(set(actual_results) | missing_allowed)
    else:
        actual_for_check = actual_results
    audit.check("exact_result_set", "declared_paths_sorted_unique",
                expected_results == sorted(set(expected_results))
                and exact_set["path_count"] == len(expected_results))
    audit.check("exact_result_set", "results_exact_membership",
                actual_for_check == expected_results)

    ledger_exclusions = {
        "results/SHA256SUMS.txt",
        "evaluations/route_a/SD-C39/2026-08-15.yaml",
        "PAPER_MANIFEST.sha256",
    }
    expected_ledger_paths = sorted(anticipated - ledger_exclusions)
    if prepare:
        ledger_valid = True
        ledger_paths = expected_ledger_paths
    else:
        lines = LEDGER.read_text("utf-8").splitlines()
        parsed = []
        format_valid = True
        for line in lines:
            match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", line)
            if not match:
                format_valid = False
                continue
            parsed.append((match.group(2), match.group(1)))
        ledger_paths = [path for path, _ in parsed]
        hashes_valid = format_valid and all(
            (ROOT / path).is_file() and file_sha256(ROOT / path) == digest
            for path, digest in parsed
        )
        ledger_valid = (format_valid and ledger_paths == expected_ledger_paths
                        and ledger_paths == sorted(set(ledger_paths))
                        and hashes_valid)
    audit.check("immutable_ledger", "ledger_exact_membership_and_hashes", ledger_valid)
    audit.check("immutable_ledger", "ledger_excludes_self_route_manifest",
                not (set(ledger_paths) & ledger_exclusions))
    audit.check("immutable_ledger", "ledger_entry_count_exact",
                len(ledger_paths) == len(expected_ledger_paths))

    artifact_paths_for_text = sorted(set(artifact_paths) - {"PAPER_MANIFEST.sha256"})
    text_bad = []
    symlink_bad = []
    for path_text in artifact_paths_for_text:
        path = ROOT / path_text
        if not path.exists() and prepare and path_text in missing_allowed:
            continue
        if path.is_symlink():
            symlink_bad.append(path_text)
        elif path.is_file():
            text_bad.extend(text_failures(path))
    audit.check("hygiene", "utf8_lf_one_eof_no_trailing_or_control",
                not text_bad)
    audit.check("hygiene", "artifact_files_no_symlink", not symlink_bad)
    tree_symlinks = []
    cache_paths = []
    for dirname in ("code", "results", "experiments", "docs", "evaluations"):
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_symlink():
                tree_symlinks.append(relpath(path))
            if (path.name in {"__pycache__", ".pytest_cache"}
                    or path.suffix in {".pyc", ".pyo"}):
                cache_paths.append(relpath(path))
    if (ROOT / "EXPERIMENT_REPORT.md").is_symlink():
        tree_symlinks.append("EXPERIMENT_REPORT.md")
    audit.check("hygiene", "managed_tree_no_symlink", not tree_symlinks)
    audit.check("hygiene", "no_cache_or_bytecode", not cache_paths)
    audit.check("hygiene", "paper_manifest_excluded_from_text_count",
                "PAPER_MANIFEST.sha256" not in artifact_paths_for_text)

    payload = audit.payload(
        ledger_entries=len(expected_ledger_paths),
        canonical_text_files=len(artifact_paths_for_text),
    )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare", action="store_true",
                        help="permit the anticipated audit and ledger files")
    parser.add_argument("--hide-external-provenance", action="store_true",
                        help="simulate a clean clone without optional /tmp inputs")
    args = parser.parse_args()
    payload = run_audit(args.prepare, args.hide_external_provenance)
    sys.stdout.buffer.write(canonical_bytes(payload))
    return 0 if payload["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
