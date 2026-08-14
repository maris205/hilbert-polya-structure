#!/usr/bin/env python3
"""Strict scientific, Route-A, source-separation, and hygiene audit for SD-C34."""

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
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C34" / "2026-08-15.yaml"
CORE = CODE / "residue_core.py"
GENERATOR = CODE / "generate_results.py"
EVALUATOR = CODE / "independent_evaluator.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
CORE_SHA = "e7ad9ff5f515973d4a0d9a991be912961f2b7492dcac7ecf0006bf490c6179cf"
RESEARCH_SHA = "b34dd0489fae5080c683bedcaed6ddcc56025ddad6854da6e786c50c36fa61fb"
PROTOTYPE_LEDGER_SHA = "f7c2e0f1c1be4bdce325515feb83a80bebfaf36e5785c39b31bcb12d9481d5e6"
SELF_GENERATED_RESULT_NAMES = {"integrity_audit.json", "SHA256SUMS.txt"}
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]
EXPECTED_ROWS = {
    "candidate_census.csv": 191,
    "matched_clone.csv": 191,
    "random_relation_controls.csv": 48,
    "modulus_census.csv": 191,
    "stratum_controls.csv": 191,
    "static_selector_firewall.csv": 191,
    "trace_class_diagnostics.csv": 10,
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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    return sorted(str(name) for name in names if str(name) not in SELF_GENERATED_RESULT_NAMES)


def imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    result = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    result |= {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    return result


def identifiers_and_calls(path: Path) -> tuple[set[str], set[str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    identifiers: set[str] = set()
    calls: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            identifiers.add(node.id.lower())
        elif isinstance(node, ast.Attribute):
            identifiers.add(node.attr.lower())
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.add(node.func.id.lower())
            elif isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr.lower())
    return identifiers, calls


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
        parsed = csv_rows(name)
        row_counts[name] = len(parsed)
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        if len(parsed) != expected:
            raise AssertionError(f"{name}: {len(parsed)} != {expected}")

    candidate = csv_rows("candidate_census.csv")
    census = csv_rows("modulus_census.csv")
    clones = csv_rows("matched_clone.csv")
    random_controls = csv_rows("random_relation_controls.csv")
    strata = csv_rows("stratum_controls.csv")
    selector = csv_rows("static_selector_firewall.csv")
    diagnostics = csv_rows("trace_class_diagnostics.csv")
    candidate_diamonds = read_json("candidate_diamonds.json")
    diamonds = read_json("cross_modulus_diamonds.json")
    oracle = read_json("source_oracle_certificate.json")
    bare = read_json("bare_ufd_control.json")
    fredholm = read_json("fredholm_ownership.json")
    evaluation = read_json("evaluation.json")
    tests = read_json("test_report.json")
    summary = read_json("summary.json")
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
        "candidate": route.get("candidate_id") == "SD-C34",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "tuple": route.get("route_tuple") == ROUTE_TUPLE,
        "layer_verdicts": [route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")] == ROUTE_TUPLE,
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
        "ordinary_not_modified": str(route.get("source_lock", {}).get("regularization_order", "")).startswith("not_applicable;"),
    }

    forbidden = {
        "arithmetic_class",
        "factor_shape_evaluator",
        "factorint",
        "is_prime",
        "is_prime_evaluator",
        "prime_table",
        "target_zero",
        "zero_table",
        "riemann_zero",
        "urlopen",
        "requests",
        "socket",
    }
    core_identifiers, core_calls = identifiers_and_calls(CORE)
    generator_identifiers, generator_calls = identifiers_and_calls(GENERATOR)
    evaluator_imports = imports(EVALUATOR)
    source_checks = {
        "core_sha": sha256(CORE) == CORE_SHA,
        "evaluator_separated": evaluation.get("independent_of_candidate_core") is True
        and "residue_core" not in evaluator_imports
        and "generate_results" not in evaluator_imports,
        "core_forbidden_identifiers_empty": core_identifiers.isdisjoint(forbidden),
        "core_forbidden_calls_empty": core_calls.isdisjoint(forbidden),
        "generator_forbidden_identifiers_empty": generator_identifiers.isdisjoint(forbidden),
        "generator_forbidden_calls_empty": generator_calls.isdisjoint(forbidden),
        "oracle_pass": oracle.get("pass") is True,
        "oracle_no_forbidden": oracle.get("forbidden_hits") == [],
        "oracle_core_sha": oracle.get("candidate_core_sha256") == CORE_SHA,
        "no_target_zeros": evaluation.get("target_zero_data_used") is False,
        "route_b_false": evaluation.get("route_b_invocation_allowed") is False,
    }

    prime_rows = [row for row in census if row["evaluator_class"] == "prime"]
    prime_power_rows = [row for row in census if row["evaluator_class"] == "prime_power"]
    mixed_rows = [row for row in census if row["evaluator_class"] == "mixed_composite"]
    composite_rows = prime_power_rows + mixed_rows
    scientific_checks = {
        "candidate": len(candidate) == 191
        and all(row["forward_component_size"] == row["state_count"] for row in candidate)
        and all(row["overlap_state_count"] == row["state_count"] for row in candidate),
        "strata": len(prime_rows) == 43 and len(prime_power_rows) == 14 and len(mixed_rows) == 134,
        "universal_recurrence": all(row["recurrent_support_nonzero"] == "1" for row in census)
        and len(composite_rows) == 148,
        "matched": len(clones) == 191
        and all(row["semiring_transport_exact"] == row["graph_transport_exact"] == row["exact_equal"] == "1" for row in clones),
        "random_controls": len(random_controls) == 48
        and all(row["s2_identity"] == row["r3_identity"] == row["universal_recurrence_nonzero"] == "1" for row in random_controls),
        "diamonds": len(candidate_diamonds) == len(diamonds) == 31
        and all(row["nonbacktracking"] == 1 and row["weight_base_product"] == row["expected_product"] for row in diamonds)
        and all(row["top_is_composite_evaluator"] == 1 for row in diamonds),
        "selector": len(selector) == 191
        and all(row["selector_equivalent_to_prime"] == "1" for row in selector)
        and all(row["selector_used_by_candidate"] == "0" and row["terminal_selector_forbidden"] == "1" for row in selector),
        "diagnostics": len(diagnostics) == 10
        and all(row["monotone_from_previous"] == row["free_marker_preserved"] == "1" for row in diagnostics),
        "fredholm": fredholm.get("ordinary_fredholm_determinant_owned") is True
        and fredholm.get("trace_class_half_plane") == "Re(s)>2"
        and fredholm.get("free_marker_counts_original_edges") is True
        and fredholm.get("prime_selective_primitive_ledger") is False
        and fredholm.get("modified_determinant_used") is False,
        "bare": bare.get("ordinary_addition_matches") is False and bare.get("source_lock_passes") is False,
        "evaluation": evaluation.get("all_pass") is True
        and evaluation.get("failure_count") == 0
        and evaluation.get("check_count") == evaluation.get("pass_count")
        and evaluation.get("stratum_counts") == {"prime": 43, "prime_power": 14, "mixed_composite": 134},
        "tests": tests.get("all_pass") is True and tests.get("passed") == tests.get("total") == 13,
        "summary": summary.get("route_tuple") == ROUTE_TUPLE
        and summary.get("overall") == "ROUTE_A_REJECTED"
        and summary.get("branch_action") == "CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH",
        "analysis": analysis.get("status") == "PASS_EXACT_PROJECTIVE_RECURRENCE_OBSTRUCTION"
        and analysis.get("route_tuple") == ROUTE_TUPLE,
        "double_run": double.get("byte_identical") is True
        and double.get("artifact_count") == 16
        and double.get("first_hashes") == double.get("second_hashes")
        and aggregate(double.get("first_hashes", {})) == double.get("aggregate_sha256"),
        "prototype": prototype.get("byte_identical_payloads") == 6
        and prototype.get("all_six_byte_identical") is True
        and prototype.get("source_oracle_semantic_equivalence") is True,
        "research": research.get("research_package_sha256") == RESEARCH_SHA
        and research.get("prototype_payload_ledger_sha256") == PROTOTYPE_LEDGER_SHA,
        "parameters": parameters.get("cutoff") == 192
        and parameters.get("trace_order") == 8
        and parameters.get("random_trials") == 48
        and parameters.get("route_tuple") == ROUTE_TUPLE,
        "environment": environment.get("experiment_core_dependencies") == []
        and environment.get("timestamps_in_results") is False,
        "inventory": inventory.get("fresh_artifact_count") == 16
        and inventory.get("expected_result_artifact_count_excluding_sha") == 23
        and inventory.get("expected_code_result_sha_entries") == 31,
    }
    metadata_payloads = (evaluation, analysis, double, environment, parameters, research, prototype, inventory, fredholm, bare)
    scientific_checks["target_zero_false"] = all(item.get("target_zero_data_used") is False for item in metadata_payloads)
    scientific_checks["route_b_false"] = all(item.get("route_b_invocation_allowed") is False for item in metadata_payloads)

    listed_paths = route.get("source_lock", {}).get("artifact_paths", [])
    self_generated_paths = {f"results/{name}" for name in SELF_GENERATED_RESULT_NAMES}
    missing_listed = sorted(
        path for path in listed_paths
        if path not in self_generated_paths and not (ROOT / path).is_file()
    )
    current_results = inventory_without_self_generated(
        path.name for path in RESULTS.iterdir() if path.is_file()
    )
    expected_inventory = inventory_without_self_generated(
        inventory["expected_result_artifacts_excluding_sha"]
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
        "result_inventory_excluding_self_generated": current_results == expected_inventory,
        "code_source_count": len(list(CODE.glob("*.py"))) == 8,
        "no_caches": not cache_paths,
        "no_crlf": not crlf_files,
        "no_control_bytes": not control_byte_files,
        "one_terminal_newline": not noncanonical_eof_files,
    }

    all_checks = {**route_checks, **source_checks, **scientific_checks, **artifact_checks}
    payload = {
        "candidate_id": "SD-C34",
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
