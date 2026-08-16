#!/usr/bin/env python3
"""Independent full-tree integrity audit for the Paper 38 integration."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_CARD = ROOT / "evaluations" / "route_a" / "SD-C40" / "2026-08-15.yaml"
LEDGER = RESULTS / "SHA256SUMS.txt"
PAPER_MANIFEST = ROOT / "PAPER_MANIFEST.sha256"

EXPECTED_SCIENCE_SHA256 = (
    "a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24"
)
PROTOTYPE_SEED_SCIENCE_SHA256 = (
    "3485a1d925924459ce92ff3aeddb31302277589d61bd9d961ecb823b1e5bb089"
)
UNAFFECTED_PROJECTION_SHA256 = (
    "47ad757f78b3b634003082bd8504ce36ad8a3915afbf7ae96aa0616f07693198"
)
EXPECTED_SOURCE_CORE_SHA256 = (
    "e023f2c399ddc5b7981a0b7b78cb33934f6ee03e5e6e2d6f34934864c07c3c1d"
)
EXPECTED_EVALUATOR_CORE_SHA256 = (
    "0934d99fa05329d8146467e903b57f36e23588ce977354f3e948777c8ec5da13"
)
EXPECTED_ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
EXPECTED_RESEARCH_AUTHORITY = {
    "DERIVATION_PACKAGE.md":
        "18c07306c64297338d6b85b4f830ce0ccd15317ec0ee22f0e57823064171307a",
    "LITERATURE_AUDIT.md":
        "dd3b0e2e0258a6423f7a43266ca19d9597e1b3353e8491f7d51a81ab70b302d7",
    "PREREGISTRATION.md":
        "606541a6852e9953882ba07bcaaa12efe06ab7f2a5c25346486a48c19fdbed2f",
    "PROOF_PACKAGE.md":
        "fdb49515d5baafc2baa00e5e3d510d940c6af813f8a32ce56e3116171f7b6d73",
    "SOURCE_LOCK.md":
        "febaeb0b1db1a0713bbb68cf99110d7ecf2df8b39caf3ee9f311598f45fa6a7a",
}
EXPECTED_CORRECTED_PROTOTYPE_LOCK_SHA256 = (
    "7a25ecee27974aa1f593f4793c7f44b8a940ad1b13f824f0a5f3c11669290c5b"
)
EXPECTED_PLAN_POINTERS = {
    "experiments/EXPERIMENT_PLAN.md":
        "fb4a332d3e72f14694c5294761619fd703bb236e0b401ab0d76701fc8b2f2e2b",
    "experiments/PREREGISTRATION.md":
        "18ada0cb02ab2af8473d37643f845aaffdde51d447d54e5cacc6a88b93c65423",
}
EXPECTED_PROTOTYPE_PROVENANCE = {
    "/tmp/paper38_exact_prototype/EXPERIMENT_PLAN.md":
        "2d1cbc15aba2f144a99df61b929da32c0a30378b1f730999d3b753538baadb9c",
    "/tmp/paper38_exact_prototype/PREREGISTRATION.md":
        "e5d010d1acdfee84325601a253eda4e0596b29509cf06b56f3af82fc61003cca",
    "/tmp/paper38_exact_prototype/independent_evaluator.py":
        "ec2bdfed0fa7e26b98b7d0d70b4d286d7b855b2065996432308a8eca59fbf3b7",
    "/tmp/paper38_exact_prototype/run_exact.py":
        "06d23fbf5f2c7fa87aa609cb1f1908f8587c5142794847b17641fce2796aa508",
    "/tmp/paper38_exact_prototype/source_core.py":
        "e023f2c399ddc5b7981a0b7b78cb33934f6ee03e5e6e2d6f34934864c07c3c1d",
}
EXPECTED_RESEARCH_PROVENANCE = {
    "/tmp/paper38_research_package.md":
        "208e839b8379d0e30a2f3647fe7a52f543ead2c9d1dcf57d1c0271dbe525f0c3",
    "/tmp/paper38_route_v0_2.yaml":
        "34529b3fdd42d07311ff1995c81b04cb3ca8559b61fcecc3c841dd3583505983",
    "/tmp/paper38_source_lock.md":
        "34acddf6573a11adbd80adafa97e58cb1ac30be7a75a2c555443cbc7ee8762e0",
}
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
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
A2_METRICS = [
    "zero_error_train", "zero_error_validation", "zero_error_test",
    "extra_zero_count", "missing_zero_count", "root_count_discrepancy",
    "cutoff_drift", "precision_drift", "control_margin",
]
A4_REQUIRED_METRICS = A2_METRICS[:6]


def canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=True) + "\n"
    ).encode("ascii")


def unaffected_science_projection(payload: dict[str, Any]) -> dict[str, Any]:
    projected = json.loads(json.dumps(payload))
    action_fields = {
        "action_discrete_in_Aut_tree",
        "aut_tree_image_discrete",
        "bass_serre_action_faithful",
        "action_kernel",
        "action_proper",
        "finite_stabilizer_tree_lattice_hypotheses_met",
    }
    theorem_fields = {
        "infinite_stabilizer_implies_action_not_discrete",
        "tree_lattice_zeta_hypotheses_fail",
        "r_ge_2_faithful_image_non_discrete",
        "r1_image_discrete_but_infinite_kernel",
        "all_r_bass_serre_action_nonproper",
        "tree_lattice_finite_stabilizer_hypotheses_fail",
    }
    for row in projected["parameter_results"]:
        for key in action_fields:
            row.pop(key, None)
    projected["theorem_boundary"] = {
        key: value for key, value in projected["theorem_boundary"].items()
        if key not in theorem_fields
    }
    projected["checks"] = [
        row for row in projected["checks"]
        if not (
            row["name"].startswith("r")
            and (
                row["name"].endswith(":not_discrete")
                or row["name"].endswith(":action_topology")
            )
        )
    ]
    return projected


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
    evaluation = ROOT / "evaluations" / "route_a" / "SD-C40"
    if evaluation.exists():
        paths.update(relpath(path) for path in evaluation.rglob("*") if path.is_file())
    if (ROOT / "EXPERIMENT_REPORT.md").is_file():
        paths.add("EXPERIMENT_REPORT.md")
    elif include_anticipated:
        paths.add("EXPERIMENT_REPORT.md")
    if include_anticipated:
        paths.update({"results/SHA256SUMS.txt", "results/integrity_audit.json"})
    return paths


def section(text: str, start: str, end: str | None) -> str:
    start_match = re.search(rf"^{re.escape(start)}:\s*$", text, re.MULTILINE)
    if not start_match:
        return ""
    if end is None:
        return text[start_match.start():]
    end_match = re.search(
        rf"^{re.escape(end)}:\s*$", text[start_match.end():], re.MULTILINE
    )
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
    match = re.search(
        rf"^ {{{indent}}}{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE
    )
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

    def payload(
        self, ledger_entries: int, canonical_text_files: int
    ) -> dict[str, Any]:
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
            "schema": "paper38-full-integrity-audit-v1",
            "candidate": "SD-C40",
            "groups": groups,
            "passed": passed_total,
            "total": check_total,
            "all_pass": passed_total == check_total,
            "ledger_entry_count": ledger_entries,
            "canonical_text_file_count": canonical_text_files,
            "paper_manifest_states_supported": ["absent_stage1", "present_stage2"],
            "mutable_metadata_excluded_from_science": True,
            "external_provenance_is_optional": True,
        }


def validate_manifest_if_present(audit: Audit) -> bool:
    if not PAPER_MANIFEST.exists():
        audit.check("manifest_seal", "stage1_absent_or_stage2_valid", True)
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
    audit.check(
        "manifest_seal",
        "stage1_absent_or_stage2_valid",
        valid_format and actual_paths == expected_paths
        and actual_paths == sorted(set(actual_paths)) and hashes_match,
    )
    return True


def run_audit(prepare: bool, hide_external_provenance: bool) -> dict[str, Any]:
    audit = Audit()
    anticipated = managed_files(include_anticipated=True)

    research = json.loads((ROOT / "docs" / "RESEARCH_LOCK.json").read_text("utf-8"))
    audit.check("research_locks", "research_lock_schema_v2",
                research["schema"] == "paper38-research-lock-v2")
    audit.check(
        "research_locks", "frozen_research_exact_five",
        research["locked_research_authority"] == EXPECTED_RESEARCH_AUTHORITY
        and len(research["locked_research_authority"]) == 5,
    )
    audit.check(
        "research_locks", "stable_plan_pointer_exact_set",
        research["stable_plan_pointers"] == EXPECTED_PLAN_POINTERS,
    )
    root_hashes = all(
        (ROOT / path).is_file() and file_sha256(ROOT / path) == digest
        for path, digest in EXPECTED_RESEARCH_AUTHORITY.items()
    )
    plan_hashes = all(
        (ROOT / path).is_file() and file_sha256(ROOT / path) == digest
        for path, digest in EXPECTED_PLAN_POINTERS.items()
    )
    audit.check("research_locks", "frozen_research_hashes", root_hashes)
    audit.check("research_locks", "stable_plan_hashes", plan_hashes)
    audit.check(
        "research_locks", "prototype_provenance_map_frozen",
        research["prototype_provenance"] == EXPECTED_PROTOTYPE_PROVENANCE,
    )
    audit.check(
        "research_locks", "research_provenance_map_frozen",
        research["research_provenance"] == EXPECTED_RESEARCH_PROVENANCE,
    )
    external = {**EXPECTED_PROTOTYPE_PROVENANCE, **EXPECTED_RESEARCH_PROVENANCE}
    external_ok = all(
        hide_external_provenance or not Path(path).is_file()
        or file_sha256(Path(path)) == digest
        for path, digest in external.items()
    )
    audit.check("research_locks", "available_external_hashes_match", external_ok)
    audit.check(
        "research_locks", "bridged_scientific_cores_frozen",
        file_sha256(ROOT / "code" / "source" / "source_core.py")
        == EXPECTED_SOURCE_CORE_SHA256
        and file_sha256(ROOT / "code" / "evaluator" / "independent_evaluator.py")
        == EXPECTED_EVALUATOR_CORE_SHA256,
    )
    audit.check(
        "research_locks", "science_hash_frozen",
        research["expected_scientific_aggregate_sha256"]
        == EXPECTED_SCIENCE_SHA256,
    )
    witness = research["corrected_prototype_witness"]
    audit.check(
        "research_locks", "corrected_prototype_witness_frozen",
        witness == {
            "path": "docs/CORRECTED_PROTOTYPE_LOCK.json",
            "sha256": EXPECTED_CORRECTED_PROTOTYPE_LOCK_SHA256,
        }
        and file_sha256(ROOT / witness["path"])
        == EXPECTED_CORRECTED_PROTOTYPE_LOCK_SHA256,
    )
    normalization = research["normalization_v2"]
    audit.check(
        "research_locks", "normalization_v2_exact",
        normalization["authority_science_sha256"] == EXPECTED_SCIENCE_SHA256
        and normalization["authority_evaluator_sha256"]
        == EXPECTED_EVALUATOR_CORE_SHA256
        and normalization["legacy_science_sha256"]
        == PROTOTYPE_SEED_SCIENCE_SHA256
        and normalization["unaffected_projection_sha256"]
        == UNAFFECTED_PROJECTION_SHA256
        and normalization["route_tuple_changed"] is False,
    )
    dependency = json.loads((ROOT / "docs" / "DEPENDENCY_LOCK.json").read_text("utf-8"))
    all_code_paths = sorted((ROOT / "code").rglob("*.py"))
    actual_imports = set().union(*(imports(path) for path in all_code_paths))
    ignored_import_names = {
        "__future__", "independent_evaluator", "source_core",
    }
    declared_standard_library = set(
        dependency["dependencies"]["python_standard_library"]
    )
    audit.check(
        "research_locks", "standard_library_only_no_network_no_tmp_runtime",
        dependency["dependencies"]["python_external_packages"] == []
        and dependency["dependencies"]["external_datasets"] == []
        and dependency["dependencies"]["network_required"] is False
        and dependency["runtime_contract"]["external_tmp_inputs_required"] is False,
    )
    audit.check(
        "research_locks", "declared_stdlib_equals_AST_imports",
        declared_standard_library == actual_imports - ignored_import_names,
    )

    source_paths = sorted((ROOT / "code" / "source").glob("*.py"))
    evaluator_paths = sorted((ROOT / "code" / "evaluator").glob("*.py"))
    source_imports = set().union(*(imports(path) for path in source_paths))
    evaluator_imports = set().union(*(imports(path) for path in evaluator_paths))
    audit.check("source_firewall", "physical_directories_disjoint",
                set(source_paths).isdisjoint(evaluator_paths))
    audit.check(
        "source_firewall", "source_does_not_import_evaluator",
        not ({"independent_evaluator", "evaluate_packet", "evaluate_route_a"}
             & source_imports),
    )
    audit.check(
        "source_firewall", "evaluator_does_not_import_source",
        not ({"source_core", "emit_packet"} & evaluator_imports),
    )
    prohibited_imports = {"socket", "requests", "urllib", "sympy", "numpy"}
    audit.check(
        "source_firewall", "no_network_or_target_library",
        not ((source_imports | evaluator_imports) & prohibited_imports),
    )
    boundary = json.loads((RESULTS / "source_evaluator_boundary.json").read_text("utf-8"))
    audit.check(
        "source_firewall", "boundary_certificate_all_true",
        boundary["physical_directories_disjoint"] is True
        and boundary["source_imports_evaluator"] is False
        and boundary["evaluator_imports_source"] is False
        and boundary["transport"] == "canonical_json_subprocess_stdin_stdout",
    )
    bridge = json.loads((RESULTS / "prototype_bridge.json").read_text("utf-8"))
    audit.check(
        "source_firewall", "corrected_prototype_bridge_versioned",
        bridge["schema"] == "paper38-corrected-prototype-bridge-v2"
        and bridge["prototype_seed_version"]
        == "v1_known_r1_image_discreteness_defect"
        and bridge["authority_evaluator_version"]
        == "v2_corrected_action_topology"
        and bridge["source_core_byte_preserved"] is True
        and bridge["evaluator_core_byte_preserved"] is False
        and bridge["scientific_payload_byte_preserved"] is False,
    )
    audit.check(
        "source_firewall", "corrected_bridge_unaffected_projection",
        bridge["prototype_seed_scientific_sha256"]
        == PROTOTYPE_SEED_SCIENCE_SHA256
        and bridge["authority_scientific_sha256"] == EXPECTED_SCIENCE_SHA256
        and bridge["unaffected_projection_sha256"]
        == UNAFFECTED_PROJECTION_SHA256
        and bridge["unaffected_projection_expected_sha256"]
        == UNAFFECTED_PROJECTION_SHA256
        and bridge["unaffected_components_match_seed"] is True
        and bridge["normalization_correction"]["route_tuple_changed"] is False
        and bridge["normalization_correction"]["evaluator_check_count_changed"]
        is False,
    )

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
    audit.check(
        "route_schema", "skill_and_version",
        scalar(route_text, "skill") == "route-a-evaluator"
        and scalar(route_text, "skill_version") == "0.2.0",
    )
    audit.check(
        "route_schema", "candidate_and_date",
        scalar(route_text, "candidate_id") == "SD-C40"
        and scalar(route_text, "evaluation_date") == "2026-08-15",
    )

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
        freeze_valid = (
            "Stage 1" in route_text and "Stage 2" in route_text
            and "metadata-only" in route_text
        )
    audit.check("route_schema", "paired_provenance_triple_valid", commit_valid)
    audit.check("route_schema", "freeze_note_stage_valid", freeze_valid)

    expected_sections = {
        "a0": ("A0_STRUCTURAL_ARITHMETIC_RELATION", "PROVED"),
        "a1": ("A1_FAIL", "REFUTED"),
        "a2": ("A2_FAIL", "REFUTED"),
        "a3": ("A3_FAIL", "STOP_SCOPED"),
        "a4": ("A4_FAIL", "REFUTED"),
    }
    section_bounds = {
        "a0": "a1", "a1": "a2", "a2": "a3",
        "a3": "a4", "a4": "adversarial_controls",
    }
    for name, (verdict, evidence) in expected_sections.items():
        block = section(route_text, name, section_bounds[name])
        required = {
            "verdict", "evidence_status", "strongest_evidence",
            "strongest_failure", "artifacts",
        }
        audit.check(
            "route_schema", f"{name}_required_keys",
            required.issubset(set(direct_keys(block, 2))),
        )
        audit.check(
            "route_schema", f"{name}_enums",
            scalar(block, "verdict", 2) == verdict
            and scalar(block, "evidence_status", 2) == evidence,
        )

    a2_block = section(route_text, "a2", "a3")
    a4_block = section(route_text, "a4", "adversarial_controls")
    for key in A2_METRICS:
        value = scalar(a2_block, key, 4)
        audit.check(
            "route_metrics", f"a2_{key}_not_applicable",
            isinstance(value, str) and value.startswith("not_applicable; "),
        )
    audit.check(
        "route_metrics", "a2_target_zero_data_false",
        scalar(a2_block, "target_zero_data_used", 4) == "false",
    )
    for key in A4_REQUIRED_METRICS:
        value = scalar(a4_block, key, 4)
        audit.check(
            "route_metrics", f"a4_{key}_not_applicable",
            isinstance(value, str) and value.startswith("not_applicable; "),
        )
    audit.check(
        "route_metrics", "a4_target_zero_data_false",
        scalar(a4_block, "target_zero_data_used", 4) == "false",
    )
    a3_block = section(route_text, "a3", "a4")
    audit.check(
        "route_metrics", "weil_compression_not_testable",
        "weil_compression:" in a3_block and "status: NOT_TESTABLE" in a3_block
        and re.search(r"^    reason: .+", a3_block, re.MULTILINE) is not None,
    )

    adversarial = section(route_text, "adversarial_controls", "route_tuple")
    audit.check(
        "route_schema", "proves_too_much_realized",
        scalar(adversarial, "proves_too_much_risk", 2) == "REALIZED"
        and scalar(adversarial, "verdict", 2) == "STOP_PROVES_TOO_MUCH",
    )
    route_tuple = indented_list(route_text, "route_tuple", 0)
    audit.check("route_schema", "route_tuple_exact",
                route_tuple == EXPECTED_ROUTE_TUPLE)
    audit.check(
        "route_schema", "overall_and_route_b",
        scalar(route_text, "overall_verdict") == "ROUTE_A_REJECTED"
        and scalar(route_text, "route_b_invocation_allowed") == "false",
    )

    artifact_paths = indented_list(source_block, "artifact_paths", 2)
    audit.check("route_references", "artifact_paths_unique",
                len(artifact_paths) == len(set(artifact_paths)))
    audit.check(
        "route_references", "artifact_paths_concrete",
        all(not path.endswith("/") and "*" not in path for path in artifact_paths),
    )
    audit.check(
        "route_references", "artifact_paths_exact_managed_set",
        set(artifact_paths) == anticipated,
    )
    missing_allowed = {"results/SHA256SUMS.txt", "results/integrity_audit.json"}
    refs_exist = all(
        (ROOT / path).is_file() or (prepare and path in missing_allowed)
        for path in artifact_paths
    )
    audit.check("route_references", "artifact_paths_exist", refs_exist)
    all_route_refs = {
        item for item in re.findall(r"^    - (.+)$", route_text, re.MULTILINE)
        if item.startswith(("code/", "results/", "docs/", "experiments/",
                            "evaluations/", "EXPERIMENT_REPORT.md"))
    }
    audit.check(
        "route_references", "section_artifact_refs_exist",
        all((ROOT / path).is_file() or (prepare and path in missing_allowed)
            for path in all_route_refs),
    )

    science_bytes = (RESULTS / "scientific_results.json").read_bytes()
    science = json.loads(science_bytes)
    audit.check("science", "canonical_scientific_sha256",
                sha256(science_bytes) == EXPECTED_SCIENCE_SHA256)
    audit.check("science", "canonical_scientific_json",
                canonical_bytes(science) == science_bytes)
    checks = science["check_summary"]
    audit.check("science", "evaluator_assertions_277",
                checks["passed"] == checks["total"] == 277)
    audit.check(
        "science", "canonical_scientific_counts",
        len(science["parameter_results"]) == 11
        and len(science["finite_tree_results"]) == 3
        and len(science["noncompact_results"]) == 5
        and len(science["gbs_results"]) == 18
        and len(science["random_one_relator_results"]) == 64
        and len(science["marker_results"]) == 5,
    )
    audit.check(
        "science", "full_tree_and_fredholm_boundaries",
        science["decision"]["full_tree_primitive_ledger"] == "EMPTY"
        and science["decision"]["full_tree_fredholm"]
        == "NOT_OWNED_NON_TRACE_CLASS"
        and science["decision"]["tree_lattice_formula_applicable"] is False,
    )
    r1 = next(row for row in science["parameter_results"] if row["r"] == 1)
    r_ge_2 = [row for row in science["parameter_results"] if row["r"] >= 2]
    theorem = science["theorem_boundary"]
    audit.check(
        "science", "r1_image_discrete_infinite_kernel_nonproper",
        r1["aut_tree_image_discrete"] is True
        and r1["bass_serre_action_faithful"] is False
        and r1["action_kernel"] == "infinite_cyclic"
        and r1["action_proper"] is False
        and r1["finite_stabilizer_tree_lattice_hypotheses_met"] is False
        and theorem["r1_image_discrete_but_infinite_kernel"] is True,
    )
    audit.check(
        "science", "r_ge_2_faithful_image_nondiscrete_nonproper",
        all(
            row["aut_tree_image_discrete"] is False
            and row["bass_serre_action_faithful"] is True
            and row["action_kernel"] == "trivial"
            and row["action_proper"] is False
            and row["finite_stabilizer_tree_lattice_hypotheses_met"] is False
            for row in r_ge_2
        )
        and theorem["r_ge_2_faithful_image_non_discrete"] is True
        and theorem["all_r_bass_serre_action_nonproper"] is True
        and theorem["tree_lattice_finite_stabilizer_hypotheses_fail"] is True,
    )
    audit.check(
        "science", "unaffected_seed_projection_exact",
        sha256(canonical_bytes(unaffected_science_projection(science)))
        == UNAFFECTED_PROJECTION_SHA256,
    )
    audit.check(
        "science", "generic_divergent_marker_controls",
        sum(row.get("source_selective", False)
            for row in science["parameter_results"]) == 0
        and science["parameter_results"][0]["orbital_group_conjugacy_ledger"]
        == "DIVERGENT_AT_EVERY_POSITIVE_HEIGHT"
        and all(not row["markers_compatible"] for row in science["marker_results"]),
    )
    audit.check(
        "science", "theorem_finite_boundary_respected",
        science["theorem_boundary"]["finite_checks_used_as_infinite_proof"] is False,
    )
    run_science = [
        (RESULTS / "runs" / name / "scientific_results.json").read_bytes()
        for name in ("A", "B", "C")
    ]
    run_route = [
        (RESULTS / "runs" / name / "route_evaluation.json").read_bytes()
        for name in ("A", "B", "C")
    ]
    audit.check(
        "science", "fresh_ab_cold_c_science_identity",
        run_science[0] == run_science[1] == run_science[2] == science_bytes,
    )
    audit.check(
        "science", "fresh_ab_cold_c_route_identity",
        run_route[0] == run_route[1] == run_route[2]
        == (RESULTS / "route_evaluation.json").read_bytes(),
    )
    route_result = json.loads((RESULTS / "route_evaluation.json").read_text("utf-8"))
    audit.check(
        "science", "independent_route_tuple_and_hash",
        route_result["route_tuple"] == EXPECTED_ROUTE_TUPLE
        and route_result["scientific_aggregate_sha256"] == EXPECTED_SCIENCE_SHA256
        and route_result["overall"] == "ROUTE_A_REJECTED"
        and route_result["route_b_invocation_allowed"] is False,
    )
    audit.check(
        "science", "independent_evaluation_byte_copy",
        (ROOT / "evaluations" / "route_a" / "SD-C40"
         / "independent_evaluation.json").read_bytes()
        == (RESULTS / "route_evaluation.json").read_bytes(),
    )

    metadata = json.loads((RESULTS / "metadata_stability.json").read_text("utf-8"))
    audit.check(
        "science", "metadata_four_states_exact",
        metadata["state_order"] == ["absent", "null", "empty", "populated"]
        and metadata["scientific_bytes_stable"] is True
        and metadata["route_bytes_stable"] is True
        and len(metadata["states"]) == 4,
    )
    reproducibility = json.loads(
        (RESULTS / "reproducibility_certificate.json").read_text("utf-8")
    )
    audit.check(
        "science", "cold_copy_removed_and_no_environment_leak",
        reproducibility["cold_copy_removed"] is True
        and reproducibility["environment_metadata_excluded_from_scientific_payload"]
        is True,
    )
    idempotence = json.loads(
        (RESULTS / "idempotence_certificate.json").read_text("utf-8")
    )
    audit.check(
        "science", "primary_materialization_idempotent",
        idempotence["second_materialization_byte_identical"] is True
        and idempotence["second_materialization_changed_paths"] == [],
    )
    analysis = json.loads((RESULTS / "analysis_summary.json").read_text("utf-8"))
    audit.check(
        "science", "analysis_exact_no_inferential_overclaim",
        analysis["analysis_regime"]["deterministic_exact_enumeration"] is True
        and analysis["analysis_regime"]["sampling_used"] is False
        and analysis["analysis_regime"]["p_values_applicable"] is False
        and analysis["analysis_regime"]["finite_checks_promoted_to_infinite_proof"]
        is False,
    )

    manifest_certificate = json.loads(
        (RESULTS / "manifest_metadata_stability.json").read_text("utf-8")
    )
    audit.check(
        "manifest_seal", "manifest_absent_present_science_stable",
        manifest_certificate["scientific_bytes_stable"] is True,
    )
    audit.check(
        "manifest_seal", "manifest_absent_present_route_stable",
        manifest_certificate["route_bytes_stable"] is True
        and {row["state"] for row in manifest_certificate["simulated_states"]}
        == {"absent", "present"},
    )
    audit.check(
        "manifest_seal", "manifest_excluded_from_immutable_sets",
        manifest_certificate["excluded_from_immutable_ledger"] is True
        and manifest_certificate["excluded_from_canonical_text_count"] is True,
    )

    exact_set = json.loads((RESULTS / "exact_result_set.json").read_text("utf-8"))
    expected_results = exact_set["paths"]
    actual_results = sorted(
        relpath(path) for path in RESULTS.rglob("*") if path.is_file()
    )
    if prepare:
        actual_for_check = sorted(set(actual_results) | missing_allowed)
    else:
        actual_for_check = actual_results
    audit.check(
        "exact_result_set", "declared_paths_sorted_unique",
        expected_results == sorted(set(expected_results))
        and exact_set["path_count"] == len(expected_results)
        and exact_set["closed_set"] is True,
    )
    audit.check("exact_result_set", "results_exact_membership",
                actual_for_check == expected_results)

    ledger_exclusions = {
        "results/SHA256SUMS.txt",
        "evaluations/route_a/SD-C40/2026-08-15.yaml",
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
        ledger_valid = (
            format_valid and ledger_paths == expected_ledger_paths
            and ledger_paths == sorted(set(ledger_paths)) and hashes_valid
        )
    audit.check("immutable_ledger", "ledger_exact_membership_and_hashes",
                ledger_valid)
    audit.check(
        "immutable_ledger", "ledger_excludes_self_route_manifest",
        not (set(ledger_paths) & ledger_exclusions),
    )
    audit.check(
        "immutable_ledger", "ledger_entry_count_exact",
        len(ledger_paths) == len(expected_ledger_paths),
    )

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
                    or path.suffix in {".pyc", ".pyo"}
                    or path.name.startswith(".paper38-cold-c-")):
                cache_paths.append(relpath(path))
    if (ROOT / "EXPERIMENT_REPORT.md").is_symlink():
        tree_symlinks.append("EXPERIMENT_REPORT.md")
    audit.check("hygiene", "managed_tree_no_symlink", not tree_symlinks)
    audit.check("hygiene", "no_cache_bytecode_or_cold_copy", not cache_paths)
    audit.check(
        "hygiene", "paper_manifest_excluded_from_text_count",
        "PAPER_MANIFEST.sha256" not in artifact_paths_for_text,
    )

    return audit.payload(
        ledger_entries=len(expected_ledger_paths),
        canonical_text_files=len(artifact_paths_for_text),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prepare", action="store_true",
        help="permit the anticipated audit and ledger files",
    )
    parser.add_argument(
        "--hide-external-provenance", action="store_true",
        help="simulate a clean clone without optional /tmp inputs",
    )
    args = parser.parse_args()
    payload = run_audit(args.prepare, args.hide_external_provenance)
    sys.stdout.buffer.write(canonical_bytes(payload))
    return 0 if payload["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
