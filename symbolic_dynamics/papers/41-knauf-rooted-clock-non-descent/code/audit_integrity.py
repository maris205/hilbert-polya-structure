#!/usr/bin/env python3
"""Read-only paired-state and exact-set auditor for Paper 41."""

from __future__ import annotations

import ast
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Any

import yaml


CONTRACT_SHA256 = "2f0bbcf5dd2d2ff725edcb961f94d45c11351ed1c89fe30af803f6ee1aa07bbc"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ZERO = "0" * 40
MANIFEST_REL = "PAPER_MANIFEST.sha256"
ROUTE_REL = "evaluations/route_a/SD-C43/2026-08-17.yaml"
LEDGER_REL = "results/SHA256SUMS.txt"
REGISTRY_REL = "code/contracts/MUTATION_REGISTRY.json"
DUMMY_COMMIT = "0123456789abcdef0123456789abcdef01234567"
RUN_FILES = [
    "independent_evaluation.json", "main_evaluation.json", "route_evaluation.json",
    "scientific_results.json", "source_packet.json",
]
MAIN_ROUTE_CHECKS = sorted([
    "a0_controls", "a0_evidence_exact", "a0_evidence_label", "a0_exact_keys", "a0_verdict_label",
    "a1_controls", "a1_evidence_exact", "a1_evidence_label", "a1_exact_keys", "a1_verdict_label",
    "a2_evidence_exact", "a2_evidence_label", "a2_exact_keys", "a2_metric_exact_set", "a2_verdict_label",
    "a3_evidence_exact", "a3_evidence_label", "a3_exact_keys", "a3_verdict_label",
    "a4_evidence_exact", "a4_evidence_label", "a4_exact_keys", "a4_verdict_label",
    "adversarial_controls", "adversarial_exact_keys", "artifact_base", "artifact_lists_distinct",
    "artifact_lists_nonempty", "artifact_paths_exist", "artifact_paths_safe", "blocking_nonempty",
    "chronology", "identity", "integration_counts", "live_source_keys", "live_top_keys", "manifest_pair",
    "overall", "paired_state", "round2_nonempty", "route_b_lock", "route_tuple", "science_hash_format",
    "science_hash_matches", "scope", "source_artifact_exact_set", "source_data_lists", "source_exact_keys",
    "target_data_forbidden", "terminal_exact_set", "top_exact_keys",
])
INDEPENDENT_ROUTE_CHECKS = sorted([
    "A0_controls", "A0_layer", "A1_controls", "A1_layer", "A2_layer", "A2_metrics", "A3_layer",
    "A4_layer", "adversarial_gate", "artifact_base", "artifact_resolution", "artifact_safety",
    "candidate_identity", "claim_scope", "integration_semantics", "overall", "paired_state", "route_b",
    "route_tuple", "science_hash", "source_key_set", "target_firewall", "terminal_set", "top_key_set",
])
EXPECTED_NORMALIZED_ROUTE_SHA256 = "07063e26ee543c0e095f5d67b18b50bd0b8ce3556d6c3683331399cddec82311"
EXPECTED_STAGE1_ROUTE_RAW_SHA256 = "aa0ec86c9cd33c688b6ce8f826c8b9877a33d38bd2eff3995d616ebe6dbdb057"
EXPECTED_SCIENCE_BYTE_CONTROL = {
    "cases": {
        "bool_vs_int": {
            "canonical_bytes_equal": False,
            "python_object_equal": True,
            "rejected": True,
            "rejection_class": "MAIN_INDEPENDENT_SCIENCE_BYTES_MISMATCH",
        },
        "int_vs_float": {
            "canonical_bytes_equal": False,
            "python_object_equal": True,
            "rejected": True,
            "rejection_class": "MAIN_INDEPENDENT_SCIENCE_BYTES_MISMATCH",
        },
    },
    "comparison": "byte_for_byte",
    "schema": "paper41-cross-evaluator-science-byte-control-v1",
    "status": "PASS",
}
STAGE1_NOTE = (
    "Stage 1 authority artifact has three PENDING_FIRST_ARTIFACT_COMMIT fields and no "
    "PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it replaces source_commit, code_commit, "
    "and source_lock.code_commit with one identical lowercase nonzero 40-hex artifact commit "
    "and adds the sorted self-excluding PAPER_MANIFEST.sha256."
)
CHECK_NAMES = sorted([
    "chronology_exact", "code_exact_set", "critical_result_semantics_exact", "dependency_bytes", "evaluation_exact_set", "experiment_freeze",
    "experiment_exact_set", "immutable_da", "immutable_package", "immutable_research_lock",
    "integration_hygiene", "integration_no_absolute_path_tokens", "integration_no_cache",
    "integration_no_symlink", "ledger_exact_set", "ledger_format",
    "ledger_hashes", "ledger_safe_paths", "ledger_self_excluded", "ledger_sorted_unique",
    "manifest_exact_set", "manifest_format", "manifest_hashes", "manifest_presence_pair",
    "manifest_safe_paths", "manifest_self_excluded", "manifest_sorted_unique", "owned_path_boundary",
    "paired_route_note", "paired_route_triple", "report_mutation_ledger_exact", "report_present", "result_declaration_exact",
    "result_exact_set",
    "science_byte_equality_control",
    "route_artifact_base", "route_artifact_paths", "route_b_locked", "route_canonical_payload",
    "route_duplicate_safe_parse", "route_exact_tuple", "route_file_present", "route_raw_order",
    "route_raw_serialization", "route_science_hash", "route_terminal_set", "snapshot_exact_set", "source_manifest_anchor",
    "text_declaration_exact", "text_exact_set", "writer_excluded",
])


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def strict_json_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return list(left) == list(right) and all(strict_json_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_json_equal(a, b) for a, b in zip(left, right))
    return left == right


def pass_result() -> dict[str, Any]:
    return {
        "check_count": len(CHECK_NAMES),
        "checks": {name: True for name in CHECK_NAMES},
        "schema": "paper41-read-only-integrity-audit-v1",
        "status": "PASS",
    }


def safe_path(value: Any) -> bool:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return False
    parts = PurePosixPath(value).parts
    return all(part not in ("", ".", "..") for part in parts) and PurePosixPath(value).as_posix() == value


def parse_hash_file(path: Path) -> tuple[list[tuple[str, str]], bool]:
    if not path.is_file() or path.is_symlink():
        return [], False
    raw = path.read_bytes()
    format_valid = not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw and raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    rows: list[tuple[str, str]] = []
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return [], False
    for line in text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None or line.rstrip(" \t") != line:
            format_valid = False
        else:
            rows.append((match.group(2), match.group(1)))
    return rows, format_valid


class NoDuplicateLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


NoDuplicateLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def stage2_note(commit: str) -> str:
    return (
        f"Stage 1 artifact commit {commit} contained the three PENDING_FIRST_ARTIFACT_COMMIT "
        "fields and no PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it seals source_commit, "
        "code_commit, and source_lock.code_commit to that same lowercase nonzero 40-hex artifact "
        "commit and adds the sorted self-excluding PAPER_MANIFEST.sha256."
    )


def owned_paths(root: Path, contract: dict[str, Any]) -> tuple[list[str], list[str]]:
    owned = contract["owned_paths"]
    snapshot_root = root / owned["repo_snapshot_root"]
    snapshot_paths = sorted(path.relative_to(root).as_posix() for path in snapshot_root.rglob("*") if path.is_file())
    static = sorted(owned["code"] + owned["docs"] + owned["experiments"] + snapshot_paths)
    managed = sorted(static + owned["results"] + [
        contract["evaluation"]["route_yaml_path"], contract["evaluation"]["route_json_path"], owned["report"],
    ])
    return static, managed


def hygiene(path: Path) -> bool:
    if not path.is_file() or path.is_symlink():
        return False
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw or b"\x00" in raw or not raw.endswith(b"\n"):
        return False
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    for line in text.splitlines():
        if line.rstrip(" \t") != line:
            return False
        if any(ord(char) < 32 and char not in "\t" for char in line):
            return False
    return True


def hash_matches(path: Path, expected: str) -> bool:
    return path.is_file() and not path.is_symlink() and digest(path.read_bytes()) == expected


def json_or_none(path: Path) -> Any:
    try:
        if not path.is_file() or path.is_symlink():
            return None
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None


def no_duplicate_json(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def canonical_json_or_none(path: Path) -> Any:
    try:
        if not path.is_file() or path.is_symlink():
            return None
        raw = path.read_bytes()
        value = json.loads(raw.decode("ascii"), object_pairs_hook=no_duplicate_json)
        return value if raw == canonical(value) else None
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError):
        return None


def import_projection(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.add(node.module or "")
    return sorted(modules)


def registry_expectations(root: Path, contract: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    raw = (root / REGISTRY_REL).read_bytes()
    if digest(raw) != contract["mutation_registry"]["sha256"]:
        raise ValueError("mutation registry anchor differs")
    registry = json.loads(raw.decode("ascii"), object_pairs_hook=no_duplicate_json)
    if raw != canonical(registry):
        raise ValueError("mutation registry bytes are not canonical")
    specifications = {
        "audit": ("audit_mutations", "auditor_rejects"),
        "packet": ("packet_mutations", "dual"),
        "route": ("route_mutations", "dual"),
        "selection": ("selection_mutations", "dual"),
        "static": ("static_mutations", "auditor_rejects"),
    }
    groups: dict[str, Any] = {}
    identifiers: list[str] = []
    for name, (registry_key, decision) in specifications.items():
        rows = registry[registry_key]
        ids = [row["id"] for row in rows]
        if ids != sorted(set(ids)):
            raise ValueError(f"{name} registry IDs differ")
        identifiers.extend(ids)
        executed = []
        for row in rows:
            decisions = (
                {"independent_rejects": True, "main_rejects": True}
                if decision == "dual" else {decision: True}
            )
            executed.append({
                **decisions,
                "expected_rejection": row["expected_rejection"],
                "id": row["id"],
                "json_pointer": row["json_pointer"],
                "operation": row["operation"],
            })
        id_hash = digest("".join(item + "\n" for item in ids).encode("ascii"))
        groups[name] = {
            "count": len(ids),
            "id_sha256": id_hash,
            "rows": executed,
            "survivors": [],
        }
        if contract["mutation_registry"][f"{name}_count"] != len(ids) \
                or contract["mutation_registry"][f"{name}_ids_sha256"] != id_hash:
            raise ValueError(f"{name} mutation contract differs")
    identifiers = sorted(identifiers)
    if identifiers != sorted(set(identifiers)):
        raise ValueError("global mutation IDs collide")
    total_hash = digest("".join(item + "\n" for item in identifiers).encode("ascii"))
    if contract["mutation_registry"]["total_count"] != len(identifiers) \
            or contract["mutation_registry"]["total_ids_sha256"] != total_hash:
        raise ValueError("global sorted mutation ledger differs")
    expected_result = {
        "audit_rejections": len(registry["audit_mutations"]),
        "dual_rejections": 2 * sum(
            len(registry[key]) for key in ("packet_mutations", "selection_mutations", "route_mutations")
        ),
        "groups": groups,
        "mutation_ids": identifiers,
        "mutation_ids_sha256": total_hash,
        "registry_sha256": digest(raw),
        "schema": "paper41-adversarial-mutation-results-v2",
        "static_rejections": len(registry["static_mutations"]),
        "survivors": [],
        "total_mutations": len(identifiers),
    }
    report_projection = {
        "groups": {
            name: {"count": groups[name]["count"], "ids_sha256": groups[name]["id_sha256"]}
            for name in ("audit", "packet", "route", "selection", "static")
        },
        "mutation_ids": identifiers,
        "mutation_ids_sha256": total_hash,
        "registry_sha256": digest(raw),
        "schema": "paper41-report-mutation-ledger-v1",
        "total_mutations": len(identifiers),
    }
    return expected_result, report_projection


def expected_route_result(contract: dict[str, Any], *, independent: bool) -> dict[str, Any]:
    names = INDEPENDENT_ROUTE_CHECKS if independent else MAIN_ROUTE_CHECKS
    return {
        "check_count": len(names),
        "checks": {name: True for name in names},
        "overall_verdict": "ROUTE_A_REJECTED",
        "paired_state": "VALID_STAGE1",
        "route_b_invocation_allowed": False,
        "route_tuple": contract["route_contract"]["tuple"],
        "schema": (
            "paper41-independent-route-evaluation-v1"
            if independent else "paper41-route-evaluation-v1"
        ),
        "terminal_codes": contract["exact_science"]["terminal_codes"],
    }


def critical_result_semantics(root: Path, contract: dict[str, Any]) -> bool:
    try:
        owned = contract["owned_paths"]
        json_paths = [relative for relative in owned["results"] if relative.endswith(".json")]
        json_paths.append(contract["evaluation"]["route_json_path"])
        objects = {relative: canonical_json_or_none(root / relative) for relative in json_paths}
        if any(value is None for value in objects.values()):
            return False

        def raw(relative: str) -> bytes:
            return (root / relative).read_bytes()

        packet = objects["results/source_packet.json"]
        science = objects["results/scientific_results.json"]
        main_evaluation = objects["results/main_evaluation.json"]
        independent_evaluation = objects["results/independent_evaluation.json"]
        relations = True
        for name in RUN_FILES:
            run_bytes = [raw(f"results/runs/{label}/{name}") for label in ("A", "B", "C")]
            relations = relations and run_bytes[0] == run_bytes[1] == run_bytes[2]
            if name != "route_evaluation.json":
                relations = relations and raw(f"results/{name}") == run_bytes[0]
        relations = relations and canonical(main_evaluation.get("science")) == raw("results/scientific_results.json")
        relations = relations and canonical(independent_evaluation.get("science")) == raw("results/scientific_results.json")

        route_projection = {
            "candidate_id": "SD-C43",
            "overall_verdict": science["route"]["overall_verdict"],
            "route_b_invocation_allowed": science["route"]["route_b_invocation_allowed"],
            "route_tuple": science["route"]["route_tuple"],
            "schema": "paper41-run-route-projection-v1",
            "science_sha256": digest(raw("results/scientific_results.json")),
            "terminal_codes": science["terminal_codes"],
        }
        relations = relations and all(
            raw(f"results/runs/{label}/route_evaluation.json") == canonical(route_projection)
            for label in ("A", "B", "C")
        )

        main_route = expected_route_result(contract, independent=False)
        independent_route = expected_route_result(contract, independent=True)
        route_rel = contract["evaluation"]["route_json_path"]
        route_certificate = {
            "independent_check_count": len(INDEPENDENT_ROUTE_CHECKS),
            "independent_route_sha256": digest(canonical(independent_route)),
            "main_check_count": len(MAIN_ROUTE_CHECKS),
            "main_route_sha256": digest(canonical(main_route)),
            "paired_state": "VALID_STAGE1",
            "schema": "paper41-route-schema-certificate-v1",
            "tuple_agreement": True,
        }

        run_hashes = {
            label: {name: digest(raw(f"results/runs/{label}/{name}")) for name in RUN_FILES}
            for label in ("A", "B", "C")
        }
        reproducibility = {
            "all_equal": True,
            "artifact_count_per_run": len(RUN_FILES),
            "run_hashes": run_hashes,
            "schema": "paper41-reproducibility-certificate-v1",
        }
        isolation = {
            "canonical_child_isolated": True,
            "canonical_emitter_explicit_I_B": True,
            "canonical_emitter_stdout_sha256": digest(raw("results/source_packet.json")),
            "canonical_hostile_modules_imported": [],
            "canonical_parent_explicit_I_B": True,
            "canonical_pycache_created": False,
            "hostile_modules_tested": ["hashlib", "json", "pathlib", "sitecustomize", "source_core", "yaml"],
            "hostile_parent_environment_normalized": True,
            "hostile_parent_variables_tested": ["PYTHONDONTWRITEBYTECODE", "PYTHONPYCACHEPREFIX"],
            "naive_hostile_invocation_allowed": False,
            "naive_child_bytecode_suppression_env_cleared": True,
            "naive_prestartup_contamination_observed": True,
            "naive_sitecustomize_marker_observed": True,
            "schema": "paper41-hostile-pythonpath-control-v3",
        }
        dependency_controls = {
            "PyYAML": "6.0.2",
            "dependency_lock_sha256": contract["dependencies"]["dependency_lock_sha256"],
            "entrypoint_policy": contract["entrypoint_policy"],
            "interpreter_isolation": isolation,
            "paper40_da_report_sha256": contract["dependencies"]["paper40_da_report_sha256"],
            "paper40_da_sidecar_sha256": contract["dependencies"]["paper40_da_sidecar_sha256"],
            "python_minimum": "3.11",
            "python_minimum_satisfied": True,
            "route_skill_decoded_sha256": contract["dependencies"]["route_skill_decoded_sha256"],
            "schema": "paper41-dependency-controls-v1",
            "source_snapshot_files": contract["dependencies"]["snapshot_file_count"],
            "status": "PASS",
        }
        external_provenance = {
            "comparison_affects_science_bytes": False,
            "external_historical_tree_available": "NOT_QUERIED_CANONICAL",
            "external_historical_tree_read": False,
            "live_files_compared": 0,
            "matches": "NOT_APPLICABLE_CANONICAL_PORTABLE_RUN",
            "schema": "paper41-optional-live-provenance-comparison-v1",
            "snapshot_container_count": contract["dependencies"]["snapshot_file_count"],
            "status": "PASS",
        }
        static, managed = owned_paths(root, contract)
        static_gate = {
            "PyYAML": "6.0.2",
            "code_path_count": len(owned["code"]),
            "dont_write_bytecode": True,
            "experiment_path_count": len(owned["experiments"]),
            "isolated_interpreter": True,
            "python_minimum": "3.11",
            "python_minimum_satisfied": True,
            "snapshot_path_count": contract["dependencies"]["snapshot_file_count"],
            "transactional_preinstall_control": {
                "forced_failure_class": "FORCED_LATE_PREINSTALL_FAILURE",
                "forced_failure_observed": True,
                "schema": "paper41-transactional-preinstall-control-v1",
                "target_cache_entries": 0,
                "target_output_paths_present": 0,
                "target_physical_writes": 0,
            },
        }
        boundary = {
            "auditor_imports_production": False,
            "dynamic_execution_or_import_calls": [],
            "evaluator_unexpected_file_reads": [],
            "independent_imports_main_or_route": False,
            "main_imports_source": False,
            "minimal_packet_runtime": {
                "files": ["evaluate_packet.py", "independent_evaluator.py", "packet.json"],
                "independent_stdout_sha256": digest(raw("results/independent_evaluation.json")),
                "main_stdout_sha256": digest(raw("results/main_evaluation.json")),
                "no_contracts_docs_or_source_present": True,
                "packet_sha256": digest(raw("results/source_packet.json")),
                "schema": "paper41-minimal-evaluator-packet-control-v1",
                "status": "PASS",
                "stdout_byte_identical_to_full_tree": True,
            },
            "module_imports": {
                "independent_evaluator": import_projection(root / "code/evaluator/independent_evaluator.py"),
                "main_evaluator": import_projection(root / "code/evaluator/evaluate_packet.py"),
                "integrity_auditor": import_projection(root / "code/audit_integrity.py"),
                "route_renderer": import_projection(root / "code/evaluator/evaluate_route_a.py"),
                "source_core": import_projection(root / "code/source/source_core.py"),
                "source_emit": import_projection(root / "code/source/emit_packet.py"),
            },
            "route_imports_production": False,
            "schema": "paper41-source-evaluator-boundary-v3",
            "science_projection_byte_control": EXPECTED_SCIENCE_BYTE_CONTROL,
            "source_imports_evaluator": False,
        }
        expected_mutation, _ = registry_expectations(root, contract)
        stored_audit = pass_result()
        expected_objects = {
            "results/adversarial_tests.json": expected_mutation,
            "results/analysis_summary.json": {
                "candidate_id": "SD-C43",
                "main_independent_science_equal": True,
                "mutation_survivors": 0,
                "overall_verdict": "ROUTE_A_REJECTED",
                "route_b_invocation_allowed": False,
                "schema": "paper41-analysis-summary-v1",
                "science_sha256": digest(raw("results/scientific_results.json")),
                "source_packet_sha256": digest(raw("results/source_packet.json")),
            },
            "results/cold_copy_certificate.json": {
                "external_historical_tree_read": False,
                "non_project_cwd": True,
                "relocated": True,
                "run_c_equals_run_a": True,
                "schema": "paper41-cold-copy-certificate-v1",
            },
            "results/dependency_controls.json": dependency_controls,
            "results/external_provenance_stability.json": external_provenance,
            "results/idempotence_certificate.json": {
                "changed_paths": 0,
                "schema": "paper41-idempotence-certificate-v1",
                "status": "PASS",
            },
            "results/immutable_inputs.json": {
                **contract["immutable_release"],
                "schema": "paper41-immutable-input-reproduction-v1",
                "status": "PASS",
            },
            "results/integrity_audit.json": stored_audit,
            "results/integrity_contract.json": {
                "contract_sha256": CONTRACT_SHA256,
                "managed_path_count": len(managed),
                "result_path_count": len(owned["results"]),
                "schema": "paper41-integrity-contract-result-v1",
                "static_gate": static_gate,
            },
            "results/reproducibility_certificate.json": reproducibility,
            "results/research_reproduction.json": {
                "h_values": science["h_values"],
                "main_independent_equal": True,
                "schema": "paper41-research-reproduction-v1",
                "theorems": science["theorems"],
                "universal_no_go_claimed": False,
            },
            "results/route_evaluation.json": main_route,
            "results/route_schema_certificate.json": route_certificate,
            "results/sealed_state_compatibility.json": {
                "audit_stdout_sha256": digest(canonical(stored_audit)),
                "dummy_commit": DUMMY_COMMIT,
                "schema": "paper41-sealed-state-compatibility-v1",
                "state_a_status": "PASS",
                "state_b_status": "PASS",
                "stdout_byte_identical": True,
            },
            "results/selection_resolver.json": science["selection"],
            "results/source_evaluator_boundary.json": boundary,
            "results/source_resolver.json": science["source_resolver"],
            route_rel: independent_route,
        }
        return relations and all(
            canonical(objects[relative]) == canonical(expected)
            for relative, expected in expected_objects.items()
        )
    except (KeyError, IndexError, OSError, TypeError, ValueError, UnicodeError, json.JSONDecodeError):
        return False


def audit(root: Path) -> dict[str, Any]:
    root = root.resolve()
    contract_path = root / "code/contracts/INTEGRATION_CONTRACT.json"
    if digest(contract_path.read_bytes()) != CONTRACT_SHA256:
        raise ValueError("integration contract hash mismatch")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    checks = {name: False for name in CHECK_NAMES}

    pre = root / "preauthority"
    package_manifest = pre / "SHA256SUMS.txt"
    package_rows, package_format = parse_hash_file(package_manifest)
    package_declared = [path for path, _ in package_rows]
    package_actual = sorted(path.name for path in pre.iterdir() if path.is_file())
    checks["immutable_package"] = (
        package_format and digest(package_manifest.read_bytes()) == contract["immutable_release"]["package_manifest_sha256"]
        and package_declared == sorted(set(package_declared)) and len(package_rows) == 15
        and package_actual == sorted(package_declared + ["SHA256SUMS.txt"])
        and all(digest((pre / relative).read_bytes()) == expected for relative, expected in package_rows)
    )
    research_path = pre / "RESEARCH_LOCK.json"
    research = json_or_none(research_path) or {}
    mappings = research.get("immutable_package_files", {})
    checks["immutable_research_lock"] = (
        hash_matches(research_path, contract["immutable_release"]["research_lock_sha256"])
        and isinstance(mappings, dict) and len(mappings) == 14
        and all((pre / relative).is_file() and digest((pre / relative).read_bytes()) == expected
                for relative, expected in mappings.items())
    )
    da_report = root / "independent_da/paper41_DA_REPORT_v2.md"
    da_sidecar = root / "independent_da/paper41_DA_REPORT_v2.sha256"
    da_actual = sorted(path.name for path in (root / "independent_da").iterdir() if path.is_file())
    checks["immutable_da"] = (
        da_actual == ["paper41_DA_REPORT_v2.md", "paper41_DA_REPORT_v2.sha256"]
        and
        hash_matches(da_report, contract["immutable_release"]["da_report_sha256"])
        and hash_matches(da_sidecar, contract["immutable_release"]["da_sidecar_file_sha256"])
        and contract["immutable_release"]["da_report_sha256"] in da_sidecar.read_text(encoding="utf-8")
    )
    checks["source_manifest_anchor"] = hash_matches(pre / "SOURCE_HASHES.sha256", contract["immutable_release"]["source_manifest_sha256"])
    checks["experiment_freeze"] = all(
        hash_matches(root / relative, expected)
        for relative, expected in contract["experiment_freeze"].items()
    )
    dependency_map = {
        "docs/DEPENDENCY_LOCK.json": contract["dependencies"]["dependency_lock_sha256"],
        "docs/inputs/SESSION4_SELECTION_PACKET.json": contract["dependencies"]["selection_packet_sha256"],
        "code/contracts/ROUTE_A_V0_2_SCHEMA.json": contract["dependencies"]["route_schema_sha256"],
        "docs/inputs/route-a-evaluator-v0.2.0.md.b64": contract["dependencies"]["route_skill_encoded_sha256"],
        "docs/inputs/dependencies/paper40_DA_REPORT.md": contract["dependencies"]["paper40_da_report_sha256"],
        "docs/inputs/dependencies/paper40_DA_REPORT.sha256": contract["dependencies"]["paper40_da_sidecar_sha256"],
    }
    checks["dependency_bytes"] = all(hash_matches(root / relative, expected) for relative, expected in dependency_map.items())

    owned = contract["owned_paths"]
    actual_code = sorted(path.relative_to(root).as_posix() for path in (root / "code").rglob("*") if path.is_file())
    checks["code_exact_set"] = actual_code == owned["code"]
    actual_docs = sorted(path.relative_to(root).as_posix() for path in (root / "docs").rglob("*") if path.is_file())
    snapshot_prefix = owned["repo_snapshot_root"] + "/"
    actual_non_snapshot_docs = [path for path in actual_docs if not path.startswith(snapshot_prefix)]
    snapshot_paths = [path for path in actual_docs if path.startswith(snapshot_prefix)]
    snapshot_relative = [path[len(snapshot_prefix):] for path in snapshot_paths]
    snapshot_path_raw = "".join(path + "\n" for path in snapshot_relative).encode("utf-8")
    snapshot_hash_raw = "".join(
        f"{digest((root / (snapshot_prefix + path)).read_bytes())}  {path}\n" for path in snapshot_relative
    ).encode("utf-8")
    checks["snapshot_exact_set"] = (
        len(snapshot_paths) == contract["dependencies"]["snapshot_file_count"]
        and digest(snapshot_path_raw) == contract["dependencies"]["snapshot_path_list_sha256"]
        and digest(snapshot_hash_raw) == contract["dependencies"]["snapshot_hash_stream_sha256"]
    )
    checks["text_exact_set"] = actual_non_snapshot_docs == owned["docs"]
    actual_experiments = sorted(path.relative_to(root).as_posix() for path in (root / "experiments").rglob("*") if path.is_file())
    checks["experiment_exact_set"] = actual_experiments == owned["experiments"]
    actual_results = sorted(path.relative_to(root).as_posix() for path in (root / "results").rglob("*") if path.is_file())
    checks["result_exact_set"] = actual_results == sorted(owned["results"])
    evaluation_root = root / "evaluations"
    actual_evaluations = sorted(path.relative_to(root).as_posix() for path in evaluation_root.rglob("*") if path.is_file())
    checks["evaluation_exact_set"] = actual_evaluations == sorted([
        contract["evaluation"]["route_yaml_path"], contract["evaluation"]["route_json_path"],
    ])
    checks["report_present"] = (root / owned["report"]).is_file()
    static, managed = owned_paths(root, contract)
    checks["owned_path_boundary"] = all((root / relative).is_file() for relative in managed)
    checks["writer_excluded"] = all(relative not in managed for relative in contract["writer_and_repository_exclusions"] if "*" not in relative)
    checks["integration_no_symlink"] = all(not (root / relative).is_symlink() for relative in managed)
    checks["integration_hygiene"] = all(hygiene(root / relative) for relative in managed)
    integration_roots = [root / item for item in ("code", "docs", "experiments", "results", "evaluations")]
    integration_files = [path for base in integration_roots if base.exists() for path in base.rglob("*")]
    checks["integration_no_cache"] = all(
        "__pycache__" not in path.parts and ".pytest_cache" not in path.parts and path.suffix != ".pyc"
        for path in integration_files
    )
    checks["integration_no_absolute_path_tokens"] = all(
        not re.search(rb"/(?:root|home|tmp)/", (root / relative).read_bytes())
        for relative in managed if (root / relative).is_file() and not (root / relative).is_symlink()
    ) and all((root / relative).is_file() for relative in managed)

    result_declaration = json_or_none(root / "results/exact_result_set.json")
    checks["result_declaration_exact"] = strict_json_equal(result_declaration, {
        "paths": owned["results"],
        "schema": "paper41-exact-result-set-v1",
    })
    text_declaration = json_or_none(root / "results/exact_text_set.json")
    checks["text_declaration_exact"] = strict_json_equal(text_declaration, {
        "ledger_exclusions": [LEDGER_REL, MANIFEST_REL, ROUTE_REL],
        "managed_paths": managed,
        "schema": "paper41-exact-integration-text-set-v1",
        "writer_paths_included": False,
    })
    source_boundary = json_or_none(root / "results/source_evaluator_boundary.json") or {}
    checks["science_byte_equality_control"] = strict_json_equal(
        source_boundary.get("science_projection_byte_control"), EXPECTED_SCIENCE_BYTE_CONTROL
    )
    chronology = contract["integration_chronology"]
    source_packet = json_or_none(root / "results/source_packet.json") or {}
    science_result = json_or_none(root / "results/scientific_results.json") or {}
    report_path = root / owned["report"]
    protocol_path = root / "docs/INTEGRITY_PROTOCOL.md"
    report_text = report_path.read_text(encoding="utf-8") if report_path.is_file() else ""
    protocol_text = protocol_path.read_text(encoding="utf-8") if protocol_path.is_file() else ""
    chronology_tokens = [chronology["status"], *chronology["known_corrections"]]
    chronology_payload = canonical(chronology).decode("ascii").rstrip("\n")
    checks["chronology_exact"] = (
        strict_json_equal(source_packet.get("integration_chronology"), chronology)
        and strict_json_equal(science_result.get("integration_chronology"), chronology)
        and report_text.count(chronology_payload) == 1
        and protocol_text.count(chronology_payload) == 1
        and all(token in protocol_text and token in report_text for token in chronology_tokens)
        and "blind=false" in protocol_text
        and "fully_prospective=false" in protocol_text
        and "results_unseen=false" in protocol_text
        and "No post-result scientific/model repair is used." in protocol_text
        and "post-result scientific/model repair is used" in report_text
        and "corrective post-output\nintegration-engineering and static repairs are disclosed above" in report_text
        and "post-result repair is used" not in report_text
    )
    try:
        _, report_projection = registry_expectations(root, contract)
        report_ledger = canonical(report_projection).decode("ascii").rstrip("\n")
        checks["report_mutation_ledger_exact"] = report_text.count(report_ledger) == 1
    except (KeyError, OSError, TypeError, ValueError, UnicodeError, json.JSONDecodeError):
        checks["report_mutation_ledger_exact"] = False
    checks["critical_result_semantics_exact"] = critical_result_semantics(root, contract)

    ledger_rows, ledger_format = parse_hash_file(root / LEDGER_REL)
    ledger_paths = [path for path, _ in ledger_rows]
    expected_ledger = sorted(set(managed) - {LEDGER_REL, ROUTE_REL, MANIFEST_REL})
    checks["ledger_format"] = ledger_format
    checks["ledger_sorted_unique"] = ledger_paths == sorted(set(ledger_paths))
    checks["ledger_safe_paths"] = all(safe_path(path) for path in ledger_paths)
    checks["ledger_self_excluded"] = LEDGER_REL not in ledger_paths and ROUTE_REL not in ledger_paths and MANIFEST_REL not in ledger_paths
    checks["ledger_exact_set"] = ledger_paths == expected_ledger
    checks["ledger_hashes"] = all((root / relative).is_file() and digest((root / relative).read_bytes()) == expected
                                  for relative, expected in ledger_rows)

    route_path = root / ROUTE_REL
    route_file_valid = route_path.is_file() and not route_path.is_symlink()
    checks["route_file_present"] = route_file_valid
    route_raw = b""
    route_parse_valid = False
    try:
        route_raw = route_path.read_bytes() if route_file_valid else b""
        route = yaml.load(route_raw.decode("ascii"), Loader=NoDuplicateLoader) if route_file_valid else {}
        route_parse_valid = isinstance(route, dict)
    except (OSError, UnicodeError, yaml.YAMLError, ValueError):
        route = {}
    if not isinstance(route, dict):
        route = {}
    checks["route_duplicate_safe_parse"] = route_parse_valid
    source = route.get("source_lock") if isinstance(route.get("source_lock"), dict) else {}
    triple = [route.get("source_commit"), route.get("code_commit"), source.get("code_commit")]
    manifest_path = root / MANIFEST_REL
    manifest_present = manifest_path.exists() or manifest_path.is_symlink()
    if manifest_present:
        commit = triple[0] if triple else None
        triple_valid = len(set(triple)) == 1 and isinstance(commit, str) and re.fullmatch(r"[0-9a-f]{40}", commit) is not None and commit != ZERO
        note_valid = triple_valid and route.get("freeze_note") == stage2_note(commit)
    else:
        triple_valid = triple == [PENDING, PENDING, PENDING]
        note_valid = route.get("freeze_note") == STAGE1_NOTE
    checks["paired_route_triple"] = triple_valid
    checks["paired_route_note"] = note_valid
    checks["manifest_presence_pair"] = triple_valid and note_valid
    checks["route_artifact_base"] = route.get("artifact_path_base") == contract["artifact_path_base"]
    artifact_groups = [source.get("artifact_paths")]
    artifact_groups.extend(
        route.get(layer, {}).get("artifacts") if isinstance(route.get(layer), dict) else None
        for layer in ("a0", "a1", "a2", "a3", "a4")
    )
    artifact_lists_valid = all(isinstance(group, list) and group for group in artifact_groups)
    artifact_paths = [item for group in artifact_groups if isinstance(group, list) for item in group]
    checks["route_artifact_paths"] = (
        artifact_lists_valid
        and all(safe_path(item) for item in artifact_paths)
        and all((root / item).is_file() and not (root / item).is_symlink() for item in artifact_paths)
    )
    normalized = json.loads(json.dumps(route))
    provenance_present = (
        all(key in normalized for key in ("source_commit", "code_commit", "freeze_note"))
        and isinstance(normalized.get("source_lock"), dict)
        and "code_commit" in normalized["source_lock"]
    )
    if provenance_present:
        normalized["source_commit"] = PENDING
        normalized["code_commit"] = PENDING
        normalized["source_lock"]["code_commit"] = PENDING
        normalized["freeze_note"] = STAGE1_NOTE
    checks["route_canonical_payload"] = (
        provenance_present and digest(canonical(normalized)) == EXPECTED_NORMALIZED_ROUTE_SHA256
    )
    try:
        rendered_raw = yaml.safe_dump(
            route, allow_unicode=False, default_flow_style=False, sort_keys=False, width=100
        ).encode("ascii")
        normalized_raw = yaml.safe_dump(
            normalized, allow_unicode=False, default_flow_style=False, sort_keys=False, width=100
        ).encode("ascii")
    except (TypeError, UnicodeError, yaml.YAMLError):
        rendered_raw = b""
        normalized_raw = b""
    checks["route_raw_serialization"] = route_parse_valid and route_raw == rendered_raw
    checks["route_raw_order"] = provenance_present and digest(normalized_raw) == EXPECTED_STAGE1_ROUTE_RAW_SHA256
    checks["route_exact_tuple"] = route.get("route_tuple") == contract["route_contract"]["tuple"]
    checks["route_b_locked"] = route.get("route_b_invocation_allowed") is False and route.get("route_b") == {
        "B": False, "invocation_allowed": False, "invoked": False,
    }
    checks["route_terminal_set"] = route.get("terminal_codes") == contract["exact_science"]["terminal_codes"]
    science_hash = route.get("authority_integration", {}).get("scientific_results_sha256") if isinstance(route.get("authority_integration"), dict) else None
    checks["route_science_hash"] = isinstance(science_hash, str) and (root / "results/scientific_results.json").is_file() and digest((root / "results/scientific_results.json").read_bytes()) == science_hash

    if manifest_present:
        manifest_rows, manifest_format = parse_hash_file(manifest_path) if manifest_path.is_file() and not manifest_path.is_symlink() else ([], False)
        declared = [path for path, _ in manifest_rows]
        actual_all = sorted(path.relative_to(root).as_posix() for path in root.rglob("*")
                            if path.is_file() and path != manifest_path)
        checks["manifest_format"] = manifest_format
        checks["manifest_sorted_unique"] = declared == sorted(set(declared))
        checks["manifest_safe_paths"] = all(safe_path(path) for path in declared)
        checks["manifest_self_excluded"] = MANIFEST_REL not in declared
        checks["manifest_exact_set"] = declared == actual_all
        checks["manifest_hashes"] = all((root / relative).is_file() and digest((root / relative).read_bytes()) == expected
                                        for relative, expected in manifest_rows)
    else:
        checks["manifest_format"] = True
        checks["manifest_sorted_unique"] = True
        checks["manifest_safe_paths"] = True
        checks["manifest_self_excluded"] = True
        checks["manifest_exact_set"] = True
        checks["manifest_hashes"] = True

    failed = sorted(name for name, passed in checks.items() if not passed)
    if failed:
        raise ValueError("integrity checks failed: " + ", ".join(failed))
    return pass_result()


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) == 2 else Path(__file__).resolve().parents[1]
    if len(argv) > 2:
        print("usage: audit_integrity.py [PAPER_ROOT]", file=sys.stderr)
        return 2
    try:
        result = audit(root)
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
