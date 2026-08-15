#!/usr/bin/env python3
"""Strict science, separation, Route-A, result-set, hygiene, and SHA audit."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Iterable

import yaml

from freeze_artifacts import (
    EXPERIMENT_CONTROLS,
    META_RESULTS,
    PYTHON_SOURCES,
    RESULT_PAYLOADS,
    ROUTE_RELATIVE,
    typed_entries,
)


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_CARD = ROOT / ROUTE_RELATIVE
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
TARGET_ROOT_FIELDS = {
    "zero_error_train",
    "zero_error_validation",
    "zero_error_test",
    "extra_zero_count",
    "missing_zero_count",
    "root_count_discrepancy",
}
A2_STABILITY_FIELDS = {
    "cutoff_drift",
    "precision_drift",
    "control_margin",
}
RESEARCH_DOCUMENTS = (
    ("preregistration_sha256", "PREREGISTRATION.md"),
    ("source_lock_sha256", "SOURCE_LOCK.md"),
    ("derivation_package_sha256", "DERIVATION_PACKAGE.md"),
    ("proof_package_sha256", "PROOF_PACKAGE.md"),
    ("literature_audit_sha256", "LITERATURE_AUDIT.md"),
    ("experiment_plan_sha256", "experiments/EXPERIMENT_PLAN.md"),
)
REQUIRED_ROUTE_KEYS = {
    "skill",
    "skill_version",
    "candidate_id",
    "source_commit",
    "code_commit",
    "evaluation_date",
    "artifact_path_base",
    "freeze_note",
    "source_lock",
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "adversarial_controls",
    "route_tuple",
    "overall_verdict",
    "claim_boundary",
    "blocking_conditions",
    "next_smallest_test",
    "round2_clues",
    "route_b_invocation_allowed",
}
BANNED_SOURCE_NAMES = {
    "isprime",
    "factorint",
    "primerange",
    "primepi",
    "fibonacci",
    "is_square",
    "zeta",
    "zetazero",
    "riemannr",
    "random",
    "randint",
    "choice",
    "shuffle",
    "socket",
    "requests",
    "urlopen",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(name: str) -> object:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def read_csv(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def recursive_target_fields(value: object, prefix: str = "") -> list[tuple[str, object]]:
    output: list[tuple[str, object]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            if "target_zero" in key.lower() or key in TARGET_ROOT_FIELDS:
                output.append((path, child))
            output.extend(recursive_target_fields(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            output.extend(recursive_target_fields(child, f"{prefix}[{index}]"))
    return output


def canonical_paths() -> list[Path]:
    paths = [ROOT / name for name in PYTHON_SOURCES]
    paths.extend(ROOT / name for name in EXPERIMENT_CONTROLS)
    paths.extend(RESULTS / name for name in RESULT_PAYLOADS)
    paths.extend(RESULTS / name for name in META_RESULTS)
    paths.append(ROUTE_CARD)
    return sorted(paths)


def hygiene(paths: Iterable[Path]) -> dict[str, object]:
    missing: list[str] = []
    crlf: list[str] = []
    eof: list[str] = []
    trailing: list[str] = []
    controls: list[str] = []
    utf8: list[str] = []
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        if not path.is_file():
            missing.append(relative)
            continue
        payload = path.read_bytes()
        if b"\r" in payload:
            crlf.append(relative)
        if not payload.endswith(b"\n") or payload.endswith(b"\n\n"):
            eof.append(relative)
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError:
            utf8.append(relative)
            continue
        if any(line.rstrip(" \t") != line for line in text.splitlines()):
            trailing.append(relative)
        if any(
            (ord(character) < 32 and character not in {"\t", "\n"})
            or 127 <= ord(character) <= 159
            for character in text
        ):
            controls.append(relative)
    return {
        "missing_canonical_files": missing,
        "crlf_files": crlf,
        "noncanonical_eof_files": eof,
        "trailing_whitespace_files": trailing,
        "control_byte_files": controls,
        "utf8_failures": utf8,
    }


def source_separation_checks() -> dict[str, bool]:
    source_paths = [ROOT / "code" / "source_core.py", ROOT / "code" / "generate_artifacts.py"]
    forbidden_hits: list[str] = []
    for path in source_paths:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id.lower() in BANNED_SOURCE_NAMES:
                forbidden_hits.append(f"{path.name}:{node.lineno}:{node.id}")
            if isinstance(node, ast.Attribute) and node.attr.lower() in BANNED_SOURCE_NAMES:
                forbidden_hits.append(f"{path.name}:{node.lineno}:{node.attr}")
    evaluator_tree = ast.parse(
        (ROOT / "code" / "independent_evaluator.py").read_text(encoding="utf-8"),
        filename="independent_evaluator.py",
    )
    imported: set[str] = set()
    for node in ast.walk(evaluator_tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        if isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    firewall = load_json("source_evaluator_firewall.json")
    return {
        "candidate_source_forbidden_identifiers_absent": not forbidden_hits,
        "evaluator_does_not_import_source": "source_core" not in imported
        and "generate_artifacts" not in imported,
        "physical_files_distinct": len({path.resolve() for path in source_paths + [ROOT / "code" / "independent_evaluator.py"]}) == 3,
        "generated_firewall_pass": firewall["status"] == "PASS"
        and firewall["forbidden_identifier_count"] == 0,
    }


def main() -> int:
    graph = read_csv("graph_census.csv")
    exhaustive = [row for row in graph if row["graph_family"] == "exhaustive"]
    controls = [row for row in graph if row["graph_family"] != "exhaustive"]

    def total(rows: list[dict[str, str]], key: str) -> int:
        return sum(int(row[key]) for row in rows)

    evaluation = load_json("evaluation.json")
    tests = load_json("test_report.json")
    graph_summary = load_json("graph_witness_summary.json")
    neutral = load_json("neutral_recognizer.json")
    boundary = load_json("boundary_controls.json")
    double = load_json("double_run_certificate.json")
    cold = load_json("cold_start_certificate.json")
    environment = load_json("environment_lock.json")
    seal = load_json("metadata_seal_stability.json")
    idempotence = load_json("idempotence_certificate.json")
    research = load_json("research_lock.json")
    inventories = read_csv("inventory_controls.csv")
    kraft = read_csv("kraft_clock_summary.csv")
    clocks = read_csv("code_clock_ledger.csv")
    markers = read_csv("marker_ledger.csv")
    counterexample_rows = read_csv("connector_construction_counterexamples.csv")

    scientific_checks = {
        "complete_graph_count": total(exhaustive, "graphs") == 66066,
        "complete_shared_pairs": total(exhaustive, "shared_pairs") == 613996,
        "complete_connector_pairs": total(exhaustive, "connector_pairs") == 161475,
        "complete_mixed_roots": total(exhaustive, "mixed_roots") == 775471,
        "control_graph_count": total(controls, "graphs") == 64,
        "control_shared_pairs": total(controls, "shared_pairs") == 66212,
        "control_connector_pairs": total(controls, "connector_pairs") == 2861,
        "control_mixed_roots": total(controls, "mixed_roots") == 69073,
        "combined_repaired_pairs": total(graph, "mixed_roots") == 844544,
        "true_failure_zero": total(graph, "failures") == 0,
        "strict_proxy_failures_retained": total(graph, "strict_external_connector_failures") == 18272
        and len(counterexample_rows) == 18272,
        "graph_summary": graph_summary["failure_count"] == 0
        and graph_summary["strict_external_connector_failure_count"] == 18272,
        "independent_evaluator": evaluation["status"] == "PASS"
        and evaluation["graph_all_equal"]
        and evaluation["preregistered_C2_status"] == "FAIL_AS_WRITTEN"
        and evaluation["repaired_C2_status"] == "PASS",
        "tests_76": tests["status"] == "PASS"
        and tests["test_count"] == tests["passed"] == 76
        and tests["failed"] == 0,
        "terminal_determinant": neutral["dimension"] == 160
        and neutral["recurrent_dimension"] == 126
        and neutral["terminal_extension_equal"],
        "inventory_controls": len(inventories) == 8
        and all(row["terminal_equals_unclassified"] == "True" for row in inventories)
        and all(row["pruning_differs_when_proper_nonempty"] in {"True", "NA"} for row in inventories),
        "kraft_clock": len(kraft) == 12
        and len(clocks) == 6141
        and evaluation["kraft_failure_count"] == 0,
        "marker_firewall": len(markers) == 17
        and evaluation["marker_item_formal_equal_count"] == 0
        and evaluation["marker_item_z_one_mismatch_count"] == 0,
        "signed_boundary": boundary["signed_scalar"]["nilpotent_order_at_most_3"]
        and boundary["signed_scalar"]["determinant_I_minus_zA"] == ["1/1"],
        "matrix_boundary": boundary["matrix_branches"]["left_times_right_zero"]
        and boundary["matrix_branches"]["right_times_left_zero"],
    }

    reproducibility_checks = {
        "fresh_double_run": double["status"] == "PASS"
        and double["byte_identical"]
        and double["artifact_count"] == 19,
        "cold_start": cold["status"] == "PASS"
        and cold["byte_identical_to_published_science"]
        and cold["cold_start_artifact_count"] == 19,
        "metadata_seal": seal["status"] == "PASS"
        and seal["schema_version"] == "SD-C36-metadata-seal-stability-v3"
        and seal["scientific_payload_byte_identical"]
        and seal["scientific_artifact_count"] == 19,
        "idempotence": idempotence["status"] == "PASS"
        and idempotence["schema_version"] == "SD-C36-idempotence-v2"
        and idempotence["research_lock_pointer_stability"],
    }

    route = yaml.safe_load(ROUTE_CARD.read_text(encoding="utf-8"))
    provenance = [
        route.get("source_commit"),
        route.get("code_commit"),
        route.get("source_lock", {}).get("code_commit"),
    ]
    target_fields = recursive_target_fields(route)
    a2_metrics = route.get("a2", {}).get("metrics", {})
    route_artifacts = set(route.get("source_lock", {}).get("artifact_paths", []))
    ledger_paths_expected = {entry["path"] for entry in typed_entries()}
    route_checks = {
        "required_top_level_keys": REQUIRED_ROUTE_KEYS <= set(route),
        "schema": route.get("skill") == "route-a-evaluator"
        and route.get("skill_version") == "0.2.0",
        "candidate": route.get("candidate_id") == "SD-C36",
        "layer_verdicts": [route[name]["verdict"] for name in ("a0", "a1", "a2", "a3", "a4")]
        == ROUTE_TUPLE,
        "route_tuple": route.get("route_tuple") == ROUTE_TUPLE,
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_pending_provenance": provenance == [PENDING, PENDING, PENDING],
        "two_stage_note": "Two-stage provenance" in route.get("freeze_note", "")
        and PENDING in route.get("freeze_note", ""),
        "all_target_zero_root_fields_scoped": bool(target_fields)
        and all(isinstance(value, str) and value.startswith("not_applicable;") for _, value in target_fields),
        "a2_mandatory_metrics_present": (
            TARGET_ROOT_FIELDS | A2_STABILITY_FIELDS
        ) <= set(a2_metrics),
        "a2_stability_metrics_scoped": all(
            isinstance(a2_metrics.get(name), str)
            and a2_metrics[name].startswith("not_applicable;")
            for name in A2_STABILITY_FIELDS
        ),
        "artifact_paths_cover_ledger": ledger_paths_expected <= route_artifacts,
        "artifact_paths_exist": all((ROOT / path).is_file() for path in route_artifacts),
        "route_card_excluded_from_ledger": ROUTE_RELATIVE not in ledger_paths_expected,
    }

    current_research_records = [
        {
            "path": relative,
            "pointer_field": field,
            "sha256": digest(ROOT / relative),
        }
        for field, relative in RESEARCH_DOCUMENTS
    ]
    research_lock_sha256 = digest(RESULTS / "research_lock.json")
    seal_research_checks = seal.get("research_lock_checks", {})
    research_lock_checks = {
        "schema_v2": research.get("schema_version") == "SD-C36-research-lock-v2",
        "six_documents": research.get("research_document_count")
        == len(RESEARCH_DOCUMENTS)
        == 6,
        "document_ledger_exact": research.get("research_documents")
        == current_research_records,
        "named_pointers_match_current_files": all(
            research.get(record["pointer_field"]) == record["sha256"]
            for record in current_research_records
        ),
        "source_lock_pointer_current": research.get("source_lock_sha256")
        == digest(ROOT / "SOURCE_LOCK.md"),
        "experiment_plan_pointer_current": research.get("experiment_plan_sha256")
        == digest(ROOT / "experiments" / "EXPERIMENT_PLAN.md"),
        "authority_plan_path": research.get("authority_plan_path")
        == "experiments/EXPERIMENT_PLAN.md",
        "freeze_flags": research.get("authority_plan_frozen_before_results") is True
        and research.get("preregistration_frozen_before_results") is True,
        "C2_failure_retained": research.get("C2_failure_retained") is True,
        "target_zero_scoped": isinstance(research.get("target_zero_data"), str)
        and research["target_zero_data"].startswith("not_applicable;"),
        "route_b_false": research.get("route_b_invocation_allowed") is False,
        "double_certificate_links_lock": double.get("research_lock_sha256")
        == research_lock_sha256,
        "cold_certificate_links_lock": cold.get("research_lock_sha256")
        == research_lock_sha256,
        "metadata_seal_links_lock": seal.get("research_lock_sha256")
        == research_lock_sha256,
        "metadata_seal_recomputes_pointers": bool(seal_research_checks)
        and all(seal_research_checks.values()),
    }
    seal_environment_checks = seal.get("environment_lock_checks", {})
    environment_checks = {
        "schema_v2": environment.get("schema_version") == "P34-environment-v2",
        "scientific_dependencies_empty": environment.get(
            "scientific_dependencies"
        )
        == [],
        "seal_audit_dependencies_exact": environment.get(
            "seal_audit_dependencies"
        )
        == {"PyYAML": "6.0.2"},
        "runtime_PyYAML_matches_lock": yaml.__version__ == "6.0.2"
        and environment.get("seal_audit_dependencies", {}).get("PyYAML")
        == yaml.__version__,
        "ambiguous_dependency_field_absent": "experiment_dependencies"
        not in environment,
        "PyYAML_role_scoped": environment.get("dependency_roles", {}).get(
            "PyYAML"
        )
        == "Route-A YAML sealing and integrity audit only",
        "execution_scope": environment.get("cpu_only") is True
        and environment.get("network_used") is False
        and environment.get("external_data_used") is False
        and environment.get("result_timestamps") is False,
        "metadata_seal_links_lock": seal.get("environment_lock_sha256")
        == digest(RESULTS / "environment_lock.json"),
        "metadata_seal_recomputes_environment": bool(seal_environment_checks)
        and all(seal_environment_checks.values()),
    }

    actual_results = {path.name for path in RESULTS.iterdir() if path.is_file()}
    expected_results = set(RESULT_PAYLOADS) | set(META_RESULTS)
    ledger_path = RESULTS / "SHA256SUMS.txt"
    ledger_lines = ledger_path.read_text(encoding="utf-8").splitlines()
    parsed: list[tuple[str, str]] = []
    ledger_errors: list[str] = []
    for line in ledger_lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if not match:
            ledger_errors.append(f"format:{line}")
            continue
        parsed.append((match.group(1), match.group(2)))
    expected_entries = typed_entries()
    expected_pairs = [(entry["sha256"], entry["path"]) for entry in expected_entries]
    for expected_hash, relative in parsed:
        path = ROOT / relative
        if not path.is_file() or digest(path) != expected_hash:
            ledger_errors.append(f"hash:{relative}")
    aggregate = (RESULTS / "aggregate_sha256.txt").read_text(encoding="utf-8").strip()
    inventory = load_json("artifact_inventory.json")
    ledger_checks = {
        "result_set_exact": actual_results == expected_results,
        "ledger_format": not ledger_errors,
        "ledger_sorted": [path for _, path in parsed] == sorted(path for _, path in parsed),
        "ledger_paths_unique": len({path for _, path in parsed}) == len(parsed),
        "ledger_exact_complete_set": parsed == expected_pairs,
        "ledger_hashes_match": not ledger_errors,
        "aggregate_matches": aggregate == hashlib.sha256(ledger_path.read_bytes()).hexdigest(),
        "inventory_schema": inventory["schema_version"] == "SD-C36-artifact-inventory-v2",
        "inventory_entries": inventory["typed_entries"] == expected_entries,
        "inventory_counts": inventory["typed_entry_count"] == len(expected_entries) == 41
        and inventory["exact_final_result_count"] == 29,
        "route_exclusion": inventory["route_card_excluded_for_metadata_only_provenance_binding"],
    }

    hygiene_results = hygiene(canonical_paths())
    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache"}
    )
    hygiene_checks = {
        "all_canonical_files_present": not hygiene_results["missing_canonical_files"],
        "all_canonical_text_lf": not hygiene_results["crlf_files"],
        "all_canonical_text_exact_one_lf_eof": not hygiene_results["noncanonical_eof_files"],
        "all_canonical_text_no_trailing_whitespace": not hygiene_results["trailing_whitespace_files"],
        "all_canonical_text_no_control_bytes": not hygiene_results["control_byte_files"],
        "all_canonical_text_utf8": not hygiene_results["utf8_failures"],
        "no_python_or_test_cache": not cache_paths,
    }
    separation_checks = source_separation_checks()
    all_groups = {
        "scientific": scientific_checks,
        "reproducibility": reproducibility_checks,
        "route": route_checks,
        "research_lock": research_lock_checks,
        "environment": environment_checks,
        "ledger": ledger_checks,
        "hygiene": hygiene_checks,
        "separation": separation_checks,
    }
    passed = all(value for group in all_groups.values() for value in group.values())
    payload = {
        "schema_version": "SD-C36-integrity-v2",
        "candidate_id": "SD-C36",
        "counts": {
            "scientific_checks_passed": sum(scientific_checks.values()),
            "scientific_checks_total": len(scientific_checks),
            "all_group_checks_passed": sum(value for group in all_groups.values() for value in group.values()),
            "all_group_checks_total": sum(len(group) for group in all_groups.values()),
            "canonical_text_files_checked": len(canonical_paths()),
            "ledger_entries": len(parsed),
            "result_files": len(actual_results),
            "python_sources": len(PYTHON_SOURCES),
        },
        "scientific_checks": scientific_checks,
        "reproducibility_checks": reproducibility_checks,
        "route_checks": route_checks,
        "research_lock_checks": research_lock_checks,
        "research_document_records": current_research_records,
        "environment_lock_checks": environment_checks,
        "ledger_checks": ledger_checks,
        "hygiene_checks": hygiene_checks,
        "separation_checks": separation_checks,
        "target_zero_root_fields": {path: value for path, value in target_fields},
        "ledger_errors": ledger_errors,
        "cache_paths": cache_paths,
        **hygiene_results,
        "sha256sums_sha256": hashlib.sha256(ledger_path.read_bytes()).hexdigest(),
        "route_b_invocation_allowed": False,
        "status": "PASS" if passed else "FAIL",
    }
    (RESULTS / "integrity_audit.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if not passed:
        raise SystemExit(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
