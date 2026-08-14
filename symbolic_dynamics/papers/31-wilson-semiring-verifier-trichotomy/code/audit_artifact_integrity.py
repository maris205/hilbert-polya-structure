#!/usr/bin/env python3
"""Strict Route-A, scientific, source-separation, and hygiene audit for SD-C33."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C33" / "2026-08-14.yaml"
CORE = CODE / "wilson_core.py"
EVALUATOR = CODE / "independent_evaluator.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
PROTOTYPE_ORIGINAL_AGGREGATE = "100490afb62c6302329db814a856782d20cf986c608a365b9a72fb848fc5a0cd"
LEGACY_AGGREGATE = "36792d57cc2d58c1b52df47fdf757c86f6e10ed5eae685423259d0d9739a0dee"
RESEARCH_SHA = "d531e13e2c94972b4c38b7df0a9b070da7f04eb80d1f533b433edf16b0937a68"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_PASS_ANALYTIC",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
SELF_GENERATED_RESULT_NAMES = {"integrity_audit.json", "SHA256SUMS.txt"}
EXPECTED_ROWS = {
    "bare_ufd_addition_failure.csv": 144,
    "composite_controls.csv": 3531,
    "entropy_budget_dilution.csv": 1692,
    "fermat_pseudoprime_controls.csv": 13,
    "formal_trace_ledger.csv": 16,
    "matched_semiring_clone.csv": 169,
    "wilson_ledger.csv": 4095,
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


def read_json(name: str):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def csv_rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def paired_provenance(source: object, code: object, lock: object) -> bool:
    if (source, code, lock) == (PENDING, PENDING, PENDING):
        return True
    return (
        isinstance(source, str)
        and source == code == lock
        and re.fullmatch(r"[0-9a-f]{40}", source) is not None
    )


def aggregate(hashes: dict[str, str]) -> str:
    lines = [f"{digest}  {name}" for name, digest in hashes.items()]
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def inventory_without_self_generated(names: object) -> list[str]:
    """Canonicalize a pre-audit or complete-tree result inventory."""
    return sorted(str(name) for name in names if str(name) not in SELF_GENERATED_RESULT_NAMES)


def imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    names |= {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    return names


def core_identifiers_and_calls() -> tuple[set[str], set[str], set[int]]:
    tree = ast.parse(CORE.read_text(encoding="utf-8"), filename=str(CORE))
    identifiers: set[str] = set()
    calls: set[str] = set()
    integers: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            identifiers.add(node.id.lower())
        elif isinstance(node, ast.Attribute):
            identifiers.add(node.attr.lower())
        elif isinstance(node, ast.Constant) and isinstance(node.value, int):
            integers.add(node.value)
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.add(node.func.id.lower())
            elif isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr.lower())
    return identifiers, calls, integers


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

    wilson = csv_rows("wilson_ledger.csv")
    composites = csv_rows("composite_controls.csv")
    pseudoprimes = csv_rows("fermat_pseudoprime_controls.csv")
    bare = csv_rows("bare_ufd_addition_failure.csv")
    matched = csv_rows("matched_semiring_clone.csv")
    dilution = csv_rows("entropy_budget_dilution.csv")
    traces = csv_rows("formal_trace_ledger.csv")
    semirings = read_json("semiring_controls.json")
    random_controls = read_json("random_operation_controls.json")
    marker = read_json("marker_change_certificate.json")
    wrappers = read_json("universal_wrapper_controls.json")
    oracle = read_json("source_oracle_certificate.json")
    tests = read_json("test_report.json")
    summary = read_json("summary.json")
    evaluation = read_json("evaluation.json")
    analysis = read_json("analysis.json")
    double = read_json("double_run_certificate.json")
    environment = read_json("environment_lock.json")
    parameters = read_json("run_parameters.json")
    research = read_json("research_lock.json")
    prototype = read_json("prototype_equivalence.json")
    inventory = read_json("artifact_inventory.json")
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
        "candidate": route.get("candidate_id") == "SD-C33",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "tuple": route.get("route_tuple") == ROUTE_TUPLE,
        "layer_verdicts": [route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")] == ROUTE_TUPLE,
        "rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_provenance(route.get("source_commit"), route.get("code_commit"), route.get("source_lock", {}).get("code_commit")),
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "zero_root_fields_na": all(
            isinstance(a2_metrics.get(field), str)
            and a2_metrics[field].startswith("not_applicable;")
            for field in zero_root_fields
        ),
        "zero_data_false": a2_metrics.get("target_zero_data_used") is False,
        "no_modified_determinant": str(route.get("source_lock", {}).get("regularization_order", "")).startswith("not_applicable;"),
    }

    identifiers, calls, integer_literals = core_identifiers_and_calls()
    forbidden = {
        "evaluator_is_prime",
        "factor_vector",
        "factorint",
        "factorization",
        "isprime",
        "monomial_text",
        "prime_iterator",
        "prime_table",
        "riemann_zero",
        "sympy",
        "zero_table",
        "open",
        "read_text",
        "urlopen",
        "request",
    }
    evaluator_imports = imports(EVALUATOR)
    source_checks = {
        "evaluator_separated": evaluation.get("independent_of_candidate_core") is True
        and "wilson_core" not in evaluator_imports
        and "generate_results" not in evaluator_imports,
        "core_forbidden_identifiers_empty": identifiers.isdisjoint(forbidden),
        "core_forbidden_calls_empty": calls.isdisjoint(forbidden),
        "core_integer_literals": integer_literals == {0, 1, 2},
        "oracle_pass": oracle.get("passes") is True,
        "oracle_no_forbidden": oracle.get("forbidden_seen") == [] and oracle.get("external_file_or_network_calls") == [],
        "oracle_literals": oracle.get("integer_literals") == [0, 1, 2],
        "no_target_zeros": evaluation.get("target_zero_data_used") is False,
        "route_b_false": evaluation.get("route_b_invocation_allowed") is False,
    }

    passing_semirings = [row["name"] for row in semirings if row["passes_source_lock"]]
    largest_dilution = next(row for row in dilution if row["p"] == "4093" and row["sigma"] == "2")
    scientific_checks = {
        "wilson": len(wilson) == 4095
        and sum(int(row["accepts"]) for row in wilson) == 564
        and all(row["accepts"] == row["independent_prime_audit"] for row in wilson),
        "composites": len(composites) == 3531 and all(row["wilson_accepts"] == "0" for row in composites),
        "pseudoprimes": len(pseudoprimes) == 13 and all(row["wilson_accepts"] == "0" for row in pseudoprimes),
        "bare": len(bare) == 144 and all(row["ordinary_sum_is_required_monic_monomial"] == "0" for row in bare),
        "matched": len(matched) == 169 and all(row["matches"] == "1" for row in matched),
        "semirings": passing_semirings == ["full_shift_positive_integer_semiring", "matched_transported_semiring_clone"],
        "random_controls": len(random_controls) == 33
        and all(not row["passes_commutative_semiring_axioms"] for row in random_controls[:32])
        and random_controls[-1]["passes_commutative_semiring_axioms"] is True,
        "dilution": len(dilution) == 1692 and float(largest_dilution["max_edge_weight_lower_bound"]) > 0.995,
        "formal_trace": len(traces) == 16 and all(row["ordinary_operator_trace_owned"] == "0" for row in traces),
        "marker": len(marker) == 2 and marker[0]["equal"] is True and marker[1]["equal"] is False,
        "wrappers": len(wrappers) == 5
        and all(row["transient_prunes_to_diagonal"] is True for row in wrappers)
        and all(row["recurrent_exact_clock_noncompact_when_support_has_unbounded_n"] is True for row in wrappers),
        "tests": tests.get("passed") == tests.get("total") == 18 and tests.get("failures") == [],
        "evaluation": evaluation.get("all_pass") is True
        and evaluation.get("check_count") == evaluation.get("pass_count") == 26620
        and evaluation.get("failure_count") == 0,
        "summary": summary.get("cutoff") == 4096
        and summary.get("accepted_count") == 564
        and summary.get("largest_accepted") == 4093
        and summary.get("route_tuple") == ROUTE_TUPLE
        and summary.get("overall") == "ROUTE_A_REJECTED"
        and summary.get("route_b") == "LOCKED",
        "analysis": analysis.get("status") == "PASS_EXACT_VERIFIER_TRICHOTOMY_NO_GO"
        and analysis.get("route_tuple") == ROUTE_TUPLE
        and analysis.get("statistics", {}).get("independent_checks") == 26620
        and analysis.get("statistics", {}).get("exact_tests") == 18,
        "double_run": double.get("byte_identical") is True
        and double.get("artifact_count") == 16
        and double.get("first_hashes") == double.get("second_hashes")
        and aggregate(double.get("first_hashes", {})) == double.get("aggregate_sha256"),
        "prototype": prototype.get("legacy_artifact_count") == 14
        and prototype.get("all_authority_LF_hashes_equal") is True
        and prototype.get("authority_LF_aggregate_equal") is True
        and prototype.get("authority_legacy_aggregate_sha256") == LEGACY_AGGREGATE
        and prototype.get("original_prototype_aggregate_sha256") == PROTOTYPE_ORIGINAL_AGGREGATE
        and prototype.get("semantic_equivalence") is True,
        "research": research.get("research_package_sha256") == RESEARCH_SHA
        and research.get("prototype_ledger_sha256") == PROTOTYPE_ORIGINAL_AGGREGATE
        and research.get("authority_LF_canonical_legacy_aggregate") == LEGACY_AGGREGATE,
        "parameters": parameters.get("cutoff") == 4096
        and parameters.get("operation_table_seed") == 31033
        and parameters.get("route_tuple") == ROUTE_TUPLE,
        "environment": environment.get("experiment_core_dependencies") == []
        and environment.get("timestamps_in_results") is False,
        "inventory": inventory.get("fresh_artifact_count") == 16
        and inventory.get("legacy_artifact_count") == 14
        and inventory.get("expected_result_artifact_count_excluding_sha") == 23
        and inventory.get("expected_code_result_sha_entries") == 31,
    }

    metadata_payloads = (evaluation, analysis, double, environment, parameters, research, prototype, inventory)
    scientific_checks["target_zero_false"] = all(payload.get("target_zero_data_used") is False for payload in metadata_payloads)
    scientific_checks["route_b_false"] = all(payload.get("route_b_invocation_allowed") is False for payload in metadata_payloads)

    listed_paths = route.get("source_lock", {}).get("artifact_paths", [])
    self_generated_paths = {f"results/{name}" for name in SELF_GENERATED_RESULT_NAMES}
    missing_listed = sorted(path for path in listed_paths if path not in self_generated_paths and not (ROOT / path).is_file())
    current_results = inventory_without_self_generated(path.name for path in RESULTS.iterdir() if path.is_file())
    expected_before_audit = inventory_without_self_generated(inventory["expected_result_artifacts_excluding_sha"])
    cache_paths = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.name in {"__pycache__", ".pytest_cache"})
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
        "preaudit_result_inventory": current_results == expected_before_audit,
        "code_source_count": len(list(CODE.glob("*.py"))) == 8,
        "no_caches": not cache_paths,
        "no_crlf": not crlf_files,
        "no_control_bytes": not control_byte_files,
        "one_terminal_newline": not noncanonical_eof_files,
    }

    all_checks = {**route_checks, **source_checks, **scientific_checks, **artifact_checks}
    payload = {
        "candidate_id": "SD-C33",
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
