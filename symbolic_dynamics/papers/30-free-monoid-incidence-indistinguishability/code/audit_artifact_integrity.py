#!/usr/bin/env python3
"""Strict Route-A, scientific, source-separation, and hygiene audit for SD-C32."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C32" / "2026-08-14.yaml"
CORE = CODE / "coherence_core.py"
EVALUATOR = CODE / "independent_evaluator.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
EXPECTED_AGGREGATE = "b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316"
EXPECTED_RESEARCH_SHA = "98b58fd77ac6bd3fd7aa5c1f662d2203a34fa2891c631fad36ed8c9a19f45b1d"
EXPECTED_PROTOTYPE_LEDGER_SHA = "a7df78b607500c687981e731764ca0c7adc21489c36d4be29ffa36a802b46472"

EXPECTED_ROWS = {
    "baseline_subset_ledger.csv": 241,
    "comparison_table.csv": 8,
    "finite_control_subset_ledger.csv": 118,
    "free_monoid_control_ledger.csv": 45,
    "marker_ownership_ledger.csv": 165,
    "predicate_mask_ledger.csv": 186,
}
EXPECTED_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]
EXPECTED_GENERATED = {
    "analysis.json",
    "analytic_ownership.json",
    "baseline.json",
    "baseline_subset_ledger.csv",
    "clone_certificate.json",
    "comparison_table.csv",
    "evaluation.json",
    "finite_control_subset_ledger.csv",
    "finite_controls.json",
    "free_monoid_control_ledger.csv",
    "free_monoid_controls.json",
    "marker_ownership_ledger.csv",
    "predicate_mask_ledger.csv",
    "predicate_masks.json",
    "sanity.json",
    "summary.json",
    "test_report.json",
}
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


def read_json(name: str) -> dict[str, object]:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def csv_rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def paired_provenance(source: object, code: object, lock: object) -> bool:
    values = (source, code, lock)
    if values == (PENDING, PENDING, PENDING):
        return True
    return (
        all(isinstance(value, str) for value in values)
        and source == code == lock
        and re.fullmatch(r"[0-9a-f]{40}", str(source)) is not None
    )


def call_names(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Name):
            names.add(node.func.id.lower())
        elif isinstance(node.func, ast.Attribute):
            names.add(node.func.attr.lower())
    return names


def evaluator_imports() -> set[str]:
    tree = ast.parse(EVALUATOR.read_text(encoding="utf-8"), filename=str(EVALUATOR))
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imports |= {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    return imports


def hygiene_paths() -> list[Path]:
    paths: list[Path] = []
    for base in (CODE, RESULTS, ROOT / "experiments", ROOT / "docs", ROOT / "evaluations"):
        paths.extend(path for path in base.rglob("*") if path.is_file())
    report = ROOT / "EXPERIMENT_REPORT.md"
    if report.is_file():
        paths.append(report)
    return sorted(set(paths))


def main() -> int:
    row_counts: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_ROWS.items():
        raw = (RESULTS / name).read_bytes()
        rows = csv_rows(name)
        row_counts[name] = len(rows)
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        if len(rows) != expected:
            raise AssertionError(f"{name}: {len(rows)} != {expected}")

    sanity = read_json("sanity.json")
    baseline = read_json("baseline.json")
    finite = read_json("finite_controls.json")
    free = read_json("free_monoid_controls.json")
    clone = read_json("clone_certificate.json")
    masks = read_json("predicate_masks.json")
    analytic = read_json("analytic_ownership.json")
    summary = read_json("summary.json")
    evaluation = read_json("evaluation.json")
    tests = read_json("test_report.json")
    analysis = read_json("analysis.json")
    double = read_json("double_run_certificate.json")
    environment = read_json("environment_lock.json")
    parameters = read_json("run_parameters.json")
    oracle = read_json("source_oracle_certificate.json")
    research = read_json("research_lock.json")
    route = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))

    a2_metrics = route.get("a2", {}).get("metrics", {})
    zero_root_fields = (
        "zero_error_train",
        "zero_error_validation",
        "zero_error_test",
        "extra_zero_count",
        "missing_zero_count",
        "root_count_discrepancy",
        "cutoff_drift",
        "precision_drift",
        "control_margin",
    )
    route_checks = {
        "required_keys": not (REQUIRED_ROUTE_KEYS - set(route)),
        "schema": route.get("skill") == "route-a-evaluator" and route.get("skill_version") == "0.2.0",
        "candidate": route.get("candidate_id") == "SD-C32",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "tuple": route.get("route_tuple") == EXPECTED_TUPLE,
        "layer_verdicts": [route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")] == EXPECTED_TUPLE,
        "rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_provenance(
            route.get("source_commit"),
            route.get("code_commit"),
            route.get("source_lock", {}).get("code_commit"),
        ),
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "zero_root_fields_na": all(
            isinstance(a2_metrics.get(field), str)
            and a2_metrics[field].startswith("not_applicable;")
            for field in zero_root_fields
        ),
        "zero_data_false": a2_metrics.get("target_zero_data_used") is False,
        "regularization_order": route.get("source_lock", {}).get("regularization_order") == 3,
        "main_theorem_u": route.get("source_lock", {}).get("main_theorem_u") == 1,
    }

    forbidden_calls = {
        "factorint",
        "isprime",
        "primepi",
        "primerange",
        "sieve",
        "zeta",
        "zetazero",
        "siegelz",
        "mangoldt",
    }
    imports = evaluator_imports()
    source_checks = {
        "evaluator_separated": oracle.get("candidate_evaluator_separated") is True
        and "coherence_core" not in imports
        and "generate_results" not in imports,
        "forbidden_calls_empty": oracle.get("forbidden_candidate_calls") == [],
        "static_no_oracles": call_names(CORE).isdisjoint(forbidden_calls),
        "prime_table_false": oracle.get("prime_table_used_in_candidate") is False,
        "zero_data_false": oracle.get("target_zero_data_used") is False,
        "source_atoms_from_covers": oracle.get("candidate_atoms_from_bottom_covers") is True,
        "numeric_marks_do_not_select": oracle.get("numeric_marks_select_atoms") is False,
        "route_b_false": oracle.get("route_b_invocation_allowed") is False,
    }

    summary_claims = summary.get("claims", {})
    scientific_checks = {
        "sanity": sanity.get("all_pass") is True and sanity.get("all_compilers_pass") is True,
        "baseline": baseline.get("all_pairs_full") is True
        and baseline.get("all_triples_full") is True
        and baseline.get("all_prefix_checks_pass") is True
        and baseline.get("all_relabels_equal") is True
        and baseline.get("all_statistics_nonzero") is True,
        "finite_controls": finite.get("all_compilers_pass") is True
        and finite.get("all_four_pair_zero") is False
        and finite.get("all_four_triple_zero") is True
        and finite.get("full_pair_survivors", {}).get("mutated_cover_promote_6") == [[2, 5], [2, 7], [3, 5]],
        "free_controls": free.get("row_count") == 45
        and free.get("all_pairs_fully_coherent") is True
        and free.get("all_triples_fully_coherent") is True
        and free.get("all_caps_locally_compatible") is True,
        "clone": clone.get("all_clone_ledgers_equal") is True
        and clone.get("baseline_clone_equal_by_cutoff") == [True, True, True]
        and clone.get("baseline_polynomial_UFD_equal_by_cutoff") == [True, True, True]
        and clone.get("theorem_certificate", {}).get("status") == "PROVES_TOO_MUCH",
        "masks": masks.get("row_count") == 186
        and masks.get("pair_separator_exists") is False
        and masks.get("triple_separator_exists") is True
        and masks.get("pair_separating_masks_for_four_finite_controls") == []
        and len(masks.get("triple_separating_masks_for_four_finite_controls", [])) == 28
        and masks.get("every_mask_copied_by_transported_clone") is True,
        "analytic": analytic.get("C2_holomorphic_strip") == "-3 < Re(s) < 4"
        and analytic.get("C2_reflection") == "C2(1-s)=C2(s)"
        and analytic.get("contains_inherited_det3_strip") is True
        and analytic.get("auxiliary_H", {}).get("trace_class") is True
        and analytic.get("auxiliary_H", {}).get("phase_dependence") is False
        and analytic.get("chiral_det3", {}).get("ownership_changed_by_filter") is False
        and analytic.get("marker_row_count") == 165
        and all(row.get("bounds_tend_to_zero") is True for row in analytic.get("tail_certificates", [])),
        "summary": summary.get("route_tuple") == EXPECTED_TUPLE
        and summary.get("overall_status") == "REJECTED_AS_RH_COMPLETION"
        and summary.get("clone_proves_too_much") is True
        and summary.get("finite_pair_separator") is False
        and summary.get("finite_triple_separator") is True
        and summary_claims.get("C2_free_commutative_clone_obstruction") is True,
        "analysis": analysis.get("status") == "PASS_EXACT_CLONE_NO_GO"
        and analysis.get("route_tuple") == EXPECTED_TUPLE
        and analysis.get("statistics", {}).get("baseline_subset_rows") == 241
        and analysis.get("statistics", {}).get("finite_control_subset_rows") == 118
        and analysis.get("statistics", {}).get("free_UFD_control_rows") == 45
        and analysis.get("statistics", {}).get("predicate_mask_rows") == 186
        and analysis.get("statistics", {}).get("marker_rows") == 165,
        "evaluation": evaluation.get("all_pass") is True
        and evaluation.get("independent_of_candidate_core") is True
        and evaluation.get("check_count") == evaluation.get("pass_count") == 1616,
        "tests": tests.get("all_pass") is True and tests.get("tests_run") == 28,
        "double_run": double.get("byte_identical") is True
        and double.get("artifact_count") == 17
        and set(double.get("first_hashes", {})) == EXPECTED_GENERATED
        and double.get("first_hashes") == double.get("second_hashes")
        and double.get("aggregate_sha256") == EXPECTED_AGGREGATE,
        "research_lock": research.get("research_package_sha256") == EXPECTED_RESEARCH_SHA
        and research.get("prototype_ledger_sha256") == EXPECTED_PROTOTYPE_LEDGER_SHA
        and research.get("prototype_double_run_aggregate_sha256") == EXPECTED_AGGREGATE,
        "environment": environment.get("external_dependencies_for_experiment_core") == []
        and environment.get("timestamps_in_results") is False,
        "parameters": parameters.get("route_tuple") == EXPECTED_TUPLE
        and parameters.get("target_zero_data_used") is False
        and parameters.get("route_b_invocation_allowed") is False,
    }

    payloads = (
        sanity,
        baseline,
        finite,
        free,
        clone,
        masks,
        analytic,
        summary,
        evaluation,
        tests,
        analysis,
        double,
        parameters,
        oracle,
        research,
    )
    scientific_checks["no_target_zeros"] = all(
        payload.get("target_zero_data_used") is False for payload in payloads
    )
    scientific_checks["route_b_false"] = all(
        payload.get("route_b_invocation_allowed") is False for payload in payloads
    )

    listed_paths = route.get("source_lock", {}).get("artifact_paths", [])
    self_generated = {"results/integrity_audit.json", "results/SHA256SUMS.txt"}
    missing_listed = sorted(
        path for path in listed_paths if path not in self_generated and not (ROOT / path).is_file()
    )
    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache"}
    )
    control_byte_files: list[str] = []
    crlf_files: list[str] = []
    noncanonical_eof_files: list[str] = []
    for path in hygiene_paths():
        raw = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        if b"\r" in raw:
            crlf_files.append(relative)
        if any(byte < 32 and byte not in (9, 10) for byte in raw) or 127 in raw:
            control_byte_files.append(relative)
        if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
            noncanonical_eof_files.append(relative)

    artifact_checks = {
        "csv_rows": row_counts == EXPECTED_ROWS,
        "csv_lf_only": all(csv_lf_only.values()),
        "listed_paths_exist": not missing_listed,
        "generated_inventory": set(double.get("first_hashes", {})) == EXPECTED_GENERATED,
        "no_caches": not cache_paths,
        "no_crlf": not crlf_files,
        "no_control_bytes": not control_byte_files,
        "one_terminal_newline": not noncanonical_eof_files,
    }
    all_checks = {**route_checks, **source_checks, **scientific_checks, **artifact_checks}
    payload = {
        "candidate_id": "SD-C32",
        "status": "PASS" if all(all_checks.values()) else "FAIL",
        "all_pass": all(all_checks.values()),
        "route_checks": route_checks,
        "source_checks": source_checks,
        "scientific_checks": scientific_checks,
        "artifact_checks": artifact_checks,
        "row_counts": row_counts,
        "csv_lf_only": csv_lf_only,
        "missing_listed_paths": missing_listed,
        "cache_paths": cache_paths,
        "crlf_files": crlf_files,
        "control_byte_files": control_byte_files,
        "noncanonical_eof_files": noncanonical_eof_files,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not payload["all_pass"]:
        raise SystemExit(json.dumps(payload, indent=2, sort_keys=True))
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
