#!/usr/bin/env python3
"""Strict scientific, Route-A, provenance, ledger, and hygiene audit for SD-C38."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
from pathlib import Path
import re

import yaml

from freeze_artifacts import LEDGER_PATHS


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_CARD = ROOT / "evaluations" / "route_a" / "SD-C38" / "2026-08-15.yaml"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
ROOT_METRICS = (
    "zero_error_train",
    "zero_error_validation",
    "zero_error_test",
    "extra_zero_count",
    "missing_zero_count",
    "root_count_discrepancy",
)
STABILITY_METRICS = ("cutoff_drift", "precision_drift", "control_margin")
ALLOWED_EVIDENCE = {
    "PROVED",
    "CONDITIONAL_THEOREM",
    "NUMERICALLY_CERTIFIED",
    "NUMERICAL_OBSERVATION",
    "HEURISTIC",
    "MODELING_CHOICE",
    "FITTED_PARAMETER",
    "OPEN",
    "REFUTED",
    "NOT_TESTABLE",
    "STOP_SCOPED",
}
EXPECTED_RESULTS = {
    "ANALYSIS_REPORT.md",
    "SHA256SUMS.txt",
    "aggregate_sha256.txt",
    "analysis.json",
    "artifact_inventory.json",
    "cold_start_certificate.json",
    "control_summary.json",
    "dependency_lock.json",
    "double_run_certificate.json",
    "environment_lock.json",
    "evaluation.json",
    "finite_chain_audit.csv",
    "graded_control.json",
    "idempotence_certificate.json",
    "integrity_audit.json",
    "marker_audit.csv",
    "operator_cycle_audit.csv",
    "prototype_bridge_certificate.json",
    "raw_data_table.csv",
    "research_lock.json",
    "run_parameters.json",
    "source_raw.json",
    "source_separation_certificate.json",
    "source_summary.json",
    "source_test_report.json",
    "test_report.json",
    "trace_audit.csv",
}
META_RESULTS = {
    "results/SHA256SUMS.txt",
    "results/aggregate_sha256.txt",
    "results/idempotence_certificate.json",
    "results/integrity_audit.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(name: str):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def aggregate(hashes: dict[str, str]) -> str:
    payload = "".join(f"{hashes[name]}  {name}\n" for name in sorted(hashes))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def text_hygiene(relative_paths: set[str]) -> tuple[dict[str, bool], dict[str, list[str]]]:
    failures = {
        "invalid_utf8": [],
        "crlf_or_cr": [],
        "noncanonical_eof": [],
        "trailing_whitespace": [],
        "control_bytes": [],
    }
    for relative in sorted(relative_paths):
        path = ROOT / relative
        if not path.is_file():
            continue
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            failures["invalid_utf8"].append(relative)
            continue
        if b"\r" in data:
            failures["crlf_or_cr"].append(relative)
        if not data.endswith(b"\n") or data.endswith(b"\n\n"):
            failures["noncanonical_eof"].append(relative)
        if any(line.endswith((" ", "\t")) for line in text.splitlines()):
            failures["trailing_whitespace"].append(relative)
        if any(byte < 32 and byte != 10 for byte in data):
            failures["control_bytes"].append(relative)
    checks = {
        "all_utf8": not failures["invalid_utf8"],
        "all_lf_only": not failures["crlf_or_cr"],
        "all_exact_one_terminal_lf": not failures["noncanonical_eof"],
        "no_trailing_whitespace": not failures["trailing_whitespace"],
        "no_forbidden_control_bytes": not failures["control_bytes"],
    }
    return checks, failures


def main() -> int:
    ledger_path = RESULTS / "SHA256SUMS.txt"
    ledger_lines = ledger_path.read_text(encoding="utf-8").splitlines()
    ledger_rows: list[tuple[str, str]] = []
    ledger_format = True
    for line in ledger_lines:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            ledger_format = False
            continue
        ledger_rows.append((match.group(1), match.group(2)))
    ledger_paths = [relative for _, relative in ledger_rows]
    ledger_hashes_match = all(
        (ROOT / relative).is_file() and digest(ROOT / relative) == expected
        for expected, relative in ledger_rows
    )
    aggregate_value = (RESULTS / "aggregate_sha256.txt").read_text(encoding="utf-8").strip()
    ledger_checks = {
        "format": ledger_format,
        "entry_count": len(ledger_rows) == len(LEDGER_PATHS) == 44,
        "paths_sorted": ledger_paths == sorted(ledger_paths),
        "paths_unique": len(ledger_paths) == len(set(ledger_paths)),
        "path_set_exact": set(ledger_paths) == set(LEDGER_PATHS),
        "hashes_match": ledger_hashes_match,
        "aggregate_matches_ledger": aggregate_value == digest(ledger_path),
    }

    actual_results = {path.name for path in RESULTS.iterdir() if path.is_file()}
    predicted_results = set(actual_results)
    predicted_results.add("integrity_audit.json")
    inventory = read_json("artifact_inventory.json")
    inventory_checks = {
        "result_set_exact_after_audit_write": predicted_results == EXPECTED_RESULTS,
        "expected_final_count": inventory["expected_final_result_count"] == len(EXPECTED_RESULTS) == 27,
        "fresh_payload_count": inventory["fresh_scientific_payload_count"] == 19,
        "fresh_payloads_exist": all((RESULTS / name).is_file() for name in inventory["fresh_scientific_payloads"]),
        "meta_payloads_exact": set(inventory["integrity_meta_payloads"]) == {name.removeprefix("results/") for name in META_RESULTS},
    }

    double = read_json("double_run_certificate.json")
    cold = read_json("cold_start_certificate.json")
    current_science = {name: digest(RESULTS / name) for name in double["run_a_hashes"]}
    reproducibility_checks = {
        "fresh_status": double["status"] == "PASS",
        "cold_status": cold["status"] == "PASS",
        "fresh_payload_count": double["scientific_payload_count"] == 19,
        "cold_payload_count": cold["scientific_payload_count"] == 19,
        "fresh_a_b_equal": double["run_a_hashes"] == double["run_b_hashes"],
        "fresh_stdout_equal": double["stdout_byte_identical"] and all(row["byte_identical"] for row in double["stage_stdout"].values()),
        "cold_equal": cold["reference_hashes"] == cold["cold_hashes"],
        "published_matches_all": current_science == double["run_a_hashes"] == cold["cold_hashes"],
        "scientific_aggregate": aggregate(current_science) == inventory["scientific_aggregate_sha256"] == "58a5d3b404d85163edfe74bea45b077da07ac6ff4f0794aff0bf9f1fbcf6ea9e",
    }

    research = read_json("research_lock.json")
    research_rows = research["research_documents"]
    research_checks = {
        "schema": research["schema"] == "SD-C38-research-lock-v1",
        "seven_documents": research["research_document_count"] == len(research_rows) == 7,
        "document_hashes_current": all(digest(ROOT / row["path"]) == row["sha256"] == research[row["pointer_field"]] for row in research_rows),
        "external_research_package": digest(Path(research["research_package_path"])) == research["research_package_sha256"] == "d29255f9eda598b780aa79165f0dcce6913880dcfa0b9ce5d370c1c43ffbd299",
        "plan_precedes_code": research["plan_frozen_before_authority_code"],
        "plan_precedes_results": research["plan_frozen_before_authority_results"],
        "target_zero_false": research["target_zero_data_used"] is False,
        "route_b_false": research["route_b_invocation_allowed"] is False,
        "certificates_link_lock": digest(RESULTS / "research_lock.json") == double["research_lock_sha256"] == cold["research_lock_sha256"] == inventory["research_lock_sha256"],
    }

    dependencies = read_json("dependency_lock.json")
    dependency_checks = {
        "scientific_dependencies_empty": dependencies["scientific_dependencies"] == [],
        "stdlib_science": dependencies["scientific_runtime"] == "Python standard library only",
        "PyYAML_exact": dependencies["seal_audit_dependencies"] == {"PyYAML": importlib.metadata.version("PyYAML")} == {"PyYAML": yaml.__version__},
        "PyYAML_role_scoped": dependencies["dependency_roles"]["PyYAML"] == "strict Route-A YAML parsing and integrity audit only",
    }

    route = yaml.safe_load(ROUTE_CARD.read_text(encoding="utf-8"))
    provenance = [route.get("source_commit"), route.get("code_commit"), route.get("source_lock", {}).get("code_commit")]
    a2_metrics = route["a2"]["metrics"]
    a4_metrics = route["a4"]["metrics"]
    route_artifacts = set(route["source_lock"]["artifact_paths"])
    expected_route_artifacts = set(LEDGER_PATHS) | META_RESULTS
    route_checks = {
        "schema_v0_2": route["skill"] == "route-a-evaluator" and route["skill_version"] == "0.2.0",
        "candidate": route["candidate_id"] == "SD-C38",
        "artifact_path_base": route["artifact_path_base"] == "papers/36-affine-cayley-chain-cancellation-no-go",
        "paired_pending_provenance": provenance == [PENDING, PENDING, PENDING],
        "two_stage_note": "Two-stage provenance" in route["freeze_note"] and PENDING in route["freeze_note"],
        "layer_verdicts": [route[f"a{index}"]["verdict"] for index in range(5)] == ROUTE_TUPLE,
        "evidence_statuses_allowed": all(route[f"a{index}"]["evidence_status"] in ALLOWED_EVIDENCE for index in range(5)),
        "evidence_statuses_exact": [route[f"a{index}"]["evidence_status"] for index in range(5)] == ["PROVED", "REFUTED", "REFUTED", "STOP_SCOPED", "STOP_SCOPED"],
        "route_tuple": route["route_tuple"] == ROUTE_TUPLE,
        "overall_rejected": route["overall_verdict"] == "ROUTE_A_REJECTED",
        "route_b_false": route["route_b_invocation_allowed"] is False,
        "risk_realized": route["adversarial_controls"]["proves_too_much_risk"] == "REALIZED",
        "adversarial_stop": route["adversarial_controls"]["verdict"] == "STOP_PROVES_TOO_MUCH",
        "arithmetic_controls_at_least_three": len(route["a0"]["arithmetic_controls"]) >= 3,
        "a2_root_metrics_scoped": all(isinstance(a2_metrics[name], str) and a2_metrics[name].startswith("not_applicable;") for name in ROOT_METRICS),
        "a2_stability_metrics_scoped": all(isinstance(a2_metrics[name], str) and a2_metrics[name].startswith("not_applicable;") for name in STABILITY_METRICS),
        "a4_root_metrics_scoped": all(isinstance(a4_metrics[name], str) and a4_metrics[name].startswith("not_applicable;") for name in ROOT_METRICS),
        "target_zero_false": a2_metrics["target_zero_data_used"] is False and a4_metrics["target_zero_data_used"] is False and route["adversarial_controls"]["target_zero_controls_used"] is False,
        "artifact_paths_exact": route_artifacts == expected_route_artifacts,
        "artifact_paths_exist": all((ROOT / relative).is_file() or relative == "results/integrity_audit.json" for relative in route_artifacts),
    }

    source_summary = read_json("source_summary.json")
    source_tests = read_json("source_test_report.json")
    separation = read_json("source_separation_certificate.json")
    evaluation = read_json("evaluation.json")
    bridge = read_json("prototype_bridge_certificate.json")
    tests = read_json("test_report.json")
    idempotence = read_json("idempotence_certificate.json")
    scientific_checks = {
        "source_checks_33": source_summary["source_checks_passed"] == source_summary["source_checks_total"] == 33 and source_tests["all_pass"],
        "source_separation": separation["pass"] and all(separation["checks"].values()),
        "prototype_semantics_33": evaluation["prototype_semantic_passed"] == evaluation["prototype_semantic_total"] == 33 and bridge["pass"],
        "independent_integration_35": evaluation["integration_passed"] == evaluation["integration_total"] == 35 and evaluation["all_checks_pass"],
        "authority_tests_53": tests["passed"] == tests["total"] == 53 and tests["all_pass"],
        "verdict_exact": evaluation["route_tuple"] == ROUTE_TUPLE and evaluation["overall_verdict"] == "ROUTE_A_REJECTED",
        "target_zero_false": evaluation["target_zero_data_used"] is False,
        "route_b_false": evaluation["route_b_invocation_allowed"] is False,
        "idempotence_pass": idempotence["status"] == "PASS" and idempotence["scientific_payloads_unchanged"] and idempotence["ledger_byte_identical"] and idempotence["aggregate_byte_identical"],
        "report_binds_science_and_research": inventory["scientific_aggregate_sha256"] in (ROOT / "EXPERIMENT_REPORT.md").read_text(encoding="utf-8") and digest(RESULTS / "research_lock.json") in (ROOT / "EXPERIMENT_REPORT.md").read_text(encoding="utf-8"),
    }

    canonical_text = set(LEDGER_PATHS) | META_RESULTS
    hygiene_checks, hygiene_failures = text_hygiene(canonical_text)
    cache_paths = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if (path.is_dir() and path.name in {"__pycache__", ".pytest_cache"}) or (path.is_file() and path.suffix == ".pyc"))
    symlink_paths = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_symlink())
    hygiene_checks["no_python_or_test_cache"] = not cache_paths
    hygiene_checks["no_symlink_in_authority_paper"] = not symlink_paths

    check_groups = {
        "ledger_checks": ledger_checks,
        "inventory_checks": inventory_checks,
        "reproducibility_checks": reproducibility_checks,
        "research_checks": research_checks,
        "dependency_checks": dependency_checks,
        "route_checks": route_checks,
        "scientific_checks": scientific_checks,
        "hygiene_checks": hygiene_checks,
    }
    all_values = [value for group in check_groups.values() for value in group.values()]
    passed = sum(bool(value) for value in all_values)
    payload = {
        "schema": "SD-C38-integrity-audit-v1",
        "candidate_id": "SD-C38",
        **check_groups,
        "counts": {
            "all_group_checks_passed": passed,
            "all_group_checks_total": len(all_values),
            "ledger_entries": len(ledger_rows),
            "result_files": len(EXPECTED_RESULTS),
            "scientific_payloads": len(current_science),
            "prototype_semantic_checks": evaluation["prototype_semantic_total"],
            "integration_checks": evaluation["integration_total"],
            "authority_tests": tests["total"],
            "research_documents": research["research_document_count"],
            "canonical_text_files": len(canonical_text),
        },
        "hygiene_failures": hygiene_failures,
        "cache_paths": cache_paths,
        "symlink_paths": symlink_paths,
        "sha256sums_sha256": digest(ledger_path),
        "aggregate_sha256": aggregate_value,
        "scientific_aggregate_sha256": inventory["scientific_aggregate_sha256"],
        "research_lock_sha256": digest(RESULTS / "research_lock.json"),
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
        "pass": passed == len(all_values),
    }
    payload["status"] = "PASS" if payload["pass"] else "FAIL"
    write_json(RESULTS / "integrity_audit.json", payload)
    print(json.dumps({"candidate_id": "SD-C38", "passed": passed, "status": payload["status"], "total": len(all_values)}, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
