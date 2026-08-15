#!/usr/bin/env python3
"""Strict science, Route-A, separation, inventory, hygiene, and SHA audit."""

from __future__ import annotations

import ast
import csv
import hashlib
from importlib.metadata import version as package_version
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
    SCIENTIFIC_PAYLOADS,
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
A2_STABILITY_FIELDS = {"cutoff_drift", "precision_drift", "control_margin"}
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
REQUIRED_SOURCE_LOCK_KEYS = {
    "candidate_definition",
    "object",
    "family",
    "phase_space",
    "dynamics",
    "parameters",
    "parameter_provenance",
    "arithmetic_origin",
    "clock",
    "normalization",
    "determinant_convention",
    "orbit_cutoff",
    "cutoff",
    "precision",
    "training_data",
    "allowed_data",
    "forbidden_data",
    "code_commit",
    "artifact_paths",
}
EVIDENCE_STATUSES = {
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
BANNED_SOURCE_NAMES = {
    "accepted_support",
    "choice",
    "factor_integer",
    "factorint",
    "is_prime",
    "isprime",
    "prime_list",
    "prime_sieve",
    "primerange",
    "random",
    "randint",
    "requests",
    "shuffle",
    "socket",
    "target_support",
    "terminal_projector",
    "urlopen",
    "zetazero",
}
RESEARCH_DOCUMENTS = (
    ("root_preregistration_sha256", "PREREGISTRATION.md"),
    ("source_lock_sha256", "SOURCE_LOCK.md"),
    ("derivation_package_sha256", "DERIVATION_PACKAGE.md"),
    ("proof_package_sha256", "PROOF_PACKAGE.md"),
    ("literature_audit_sha256", "LITERATURE_AUDIT.md"),
    ("authority_preregistration_sha256", "experiments/PREREGISTRATION.md"),
    ("experiment_plan_sha256", "experiments/EXPERIMENT_PLAN.md"),
)


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
    symlinks: list[str] = []
    json_failures: list[str] = []
    csv_failures: list[str] = []
    yaml_failures: list[str] = []
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            symlinks.append(relative)
            continue
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
        if path.suffix == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError:
                json_failures.append(relative)
        if path.suffix == ".csv":
            try:
                rows = list(csv.reader(text.splitlines()))
                if len(rows) < 2 or not rows[0]:
                    csv_failures.append(relative)
            except csv.Error:
                csv_failures.append(relative)
        if path.suffix in {".yaml", ".yml"}:
            try:
                yaml.safe_load(text)
            except yaml.YAMLError:
                yaml_failures.append(relative)
    return {
        "missing_canonical_files": missing,
        "symlink_files": symlinks,
        "crlf_files": crlf,
        "noncanonical_eof_files": eof,
        "trailing_whitespace_files": trailing,
        "control_byte_files": controls,
        "utf8_failures": utf8,
        "json_failures": json_failures,
        "csv_failures": csv_failures,
        "yaml_failures": yaml_failures,
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
    evaluator_path = ROOT / "code" / "independent_evaluator.py"
    evaluator_tree = ast.parse(evaluator_path.read_text(encoding="utf-8"), filename=evaluator_path.name)
    imported: set[str] = set()
    for node in ast.walk(evaluator_tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        if isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    firewall = load_json("source_evaluator_firewall.json")
    manifest = load_json("source_manifest.json")
    source_hashes = {name: digest(RESULTS / name) for name in manifest["artifacts"]}
    return {
        "candidate_source_forbidden_identifiers_absent": not forbidden_hits,
        "evaluator_does_not_import_source": "source_core" not in imported
        and "generate_artifacts" not in imported,
        "physical_files_distinct": len(
            {path.resolve() for path in source_paths + [evaluator_path]}
        )
        == 3,
        "generated_firewall_pass": firewall["pass"] is True
        and firewall["source_identifier_violations"] == [],
        "source_manifest_hashes_match": source_hashes == manifest["sha256"],
        "source_frozen_before_evaluator": manifest["source_frozen_before_evaluator"]
        is True,
    }


def main() -> int:
    heights = read_csv("height_dag_ledger.csv")
    backtracks = read_csv("backtrack_ledger.csv")
    census = read_csv("admissible_word_census.csv")
    quotients = read_csv("quotient_ledger.csv")
    evaluation = load_json("evaluation.json")
    tests = load_json("test_report.json")
    analysis = load_json("analysis.json")
    relations = load_json("relation_witnesses.json")
    commutations = load_json("commutation_witnesses.json")
    monoids = load_json("monoid_relation_controls.json")
    operators = load_json("operator_certificates.json")
    full_boundary = load_json("full_monoid_boundary.json")
    bc = load_json("bc_firewall.json")
    fock = load_json("fock_marker_firewall.json")
    boundary = load_json("boundary_controls.json")
    controls = load_json("control_evaluation.json")
    parameters = load_json("source_parameters.json")
    counterexamples = load_json("counterexamples.json")
    double = load_json("double_run_certificate.json")
    cold = load_json("cold_start_certificate.json")
    environment = load_json("environment_lock.json")
    seal = load_json("metadata_seal_stability.json")
    idempotence = load_json("idempotence_certificate.json")
    research = load_json("research_lock.json")
    bridge = load_json("prototype_bridge.json")

    total_words = sum(int(row["total_words"]) for row in census)
    total_admissible = sum(int(row["admissible_words"]) for row in census)
    total_nb = sum(int(row["cyclic_nb_closed_words"]) for row in census)
    total_primitive_nb = sum(int(row["primitive_cyclic_nb_closed_words"]) for row in census)
    q22 = next(row for row in quotients if row["r"] == "2" and row["q"] == "2")
    scientific_checks = {
        "authority_parameters": parameters["baseline_r"] == 4
        and parameters["r_values"] == [4, 2, 3, 5]
        and parameters["height_definition"] == "h_r(b,k)=b+r^k"
        and parameters["operator_definition"] == "A_plus=S+T on ell2(P_r)"
        and parameters["edge_weight_a"] == parameters["edge_weight_b"] == "1/1",
        "height_rows_520": len(heights) == 520,
        "height_exact_increments": all(
            row["strict_increase"] == "True"
            and int(row["height_increment"])
            == int(row["expected_increment"])
            == (
                int(row["r"]) ** int(row["origin_k"])
                if row["token"] == "U+"
                else (int(row["r"]) - 1)
                * int(row["r"]) ** int(row["origin_k"])
            )
            for row in heights
        ),
        "induced_windows_dag": all(
            not record["directed_cycle_found"] for record in evaluation["dag_records"]
        ),
        "backtracks_520": len(backtracks) == 520
        and all(
            row["closed"] == row["primitive"] == row["immediate_backtrack"] == "True"
            and row["hashimoto_allowed"] == "False"
            for row in backtracks
        ),
        "word_population": len(census) == 64
        and total_words == 699040
        and total_admissible == 126553
        and total_nb == total_primitive_nb == 88,
        "affine_relations": len(relations["witnesses"]) == 8
        and all(
            item["closed"]
            and item["admissible"]
            and item["cyclically_nonbacktracking"]
            and item["primitive"]
            and item["length"] == item["r"] + 3
            and item["weight"] == "1/1"
            for item in relations["witnesses"]
        ),
        "generic_controls": len(commutations["witnesses"]) == 4
        and len(monoids["controls"]) == 4
        and controls["generic_relation_cycles_survive"]
        and not controls["arithmetic_acceptance_labels_used"],
        "operator_certificates": len(operators["certificates"]) == 4
        and all(
            item["a"] == item["b"] == "1/1"
            and item["finite_window_certificate_only"]
            and item["analytic_noncompactness_proof_owned_by_math_lock"]
            and item["a_plus_pairwise_disjoint"]
            and item["symmetric_pairwise_disjoint"]
            and item["hashimoto_pairwise_disjoint"]
            for item in operators["certificates"]
        ),
        "full_monoid_theorem_only": full_boundary["finite_census_performed"] is False
        and full_boundary["outdegree"] == "countably_infinite"
        and full_boundary["status"] == "THEOREM_ONLY_NO_FINITE_AUDIT_PRETENSE",
        "quotients_48": len(quotients) == 48
        and all(
            row["relation_preserved"] == "True" and row["u_q_closed"] == "True"
            for row in quotients
        )
        and q22["required_2_2_degeneracy"] == "True"
        and q22["relation_polygon_vertex_simple"] == "False",
        "bc_firewall": len(bc["fixtures"]) == 2
        and all(
            item["coefficient_identity_Tr_Dm_over_m"]
            and item["linear_log_coefficient_equals_trace"]
            and item["trace_is_not_determinant_germ"]
            and item["determinant_at_z_one"] == "0/1"
            for item in bc["fixtures"]
        ),
        "fock_marker_firewall": len(fock["prime_labels"]) == 8
        and fock["coefficient_methods_equal"]
        and fock["construction_location"] == "independent evaluator after source freeze"
        and fock["z_one_is_not_original_graph_step_marker"]
        and not fock["source_contains_prime_classifier"],
        "signed_matrix_boundary": boundary["signed_scalar"]["odd_powers_cancel"]
        and boundary["signed_scalar"]["even_powers_survive"]
        and boundary["nilpotent_matrix"]["determinant_factor_is_one"]
        and boundary["traceless_invertible_matrix"]["first_trace_zero"]
        and boundary["traceless_invertible_matrix"]["second_trace_nonzero"]
        and not boundary["traceless_invertible_matrix"]["all_orders_cancel"],
        "groupoid_open_boundary": boundary["groupoid_boundary"]["status"]
        == "OPEN_BOUNDARY_NOT_EVALUATED_AS_SAME_OBJECT",
        "independent_evaluator": evaluation["status"] == "PASS"
        and all(evaluation["gates"].values())
        and evaluation["unexpected_mismatches"] == []
        and evaluation["source_hashes_unchanged_after_evaluation"],
        "tests_84": tests["status"] == "PASS"
        and tests["test_count"] == tests["passed"] == 84
        and tests["failed"] == 0
        and tests["mutation_sensitivity_test_count"] == 5,
        "analysis_pass": analysis["status"] == "PASS"
        and analysis["route_tuple"] == ROUTE_TUPLE,
        "counterexamples_retained": counterexamples["all_expected_corrections_retained"]
        and counterexamples["unexpected_mismatches"] == [],
    }
    reproducibility_checks = {
        "fresh_double_run": double["status"] == "PASS"
        and double["byte_identical"]
        and double["artifact_count"] == len(SCIENTIFIC_PAYLOADS) == 23,
        "cold_start": cold["status"] == "PASS"
        and cold["byte_identical_to_published_science"]
        and cold["cold_start_artifact_count"] == 23,
        "metadata_seal": seal["status"] == "PASS"
        and seal["scientific_payload_byte_identical"]
        and seal["scientific_artifact_count"] == 23,
        "idempotence": idempotence["status"] == "PASS",
        "prototype_bridge": bridge["status"] == "PASS"
        and bridge["authority_recomputes_all_scientific_outputs"]
        and not bridge["prototype_outputs_copied_as_authority_results"],
        "dependency_provenance": environment["scientific_dependencies"] == []
        and environment["seal_audit_dependencies"]
        == {"PyYAML": package_version("PyYAML")}
        == {"PyYAML": "6.0.2"},
    }
    current_research_records = [
        {"path": relative, "pointer_field": field, "sha256": digest(ROOT / relative)}
        for field, relative in RESEARCH_DOCUMENTS
    ]
    research_checks = {
        "schema": research["schema_version"] == "SD-C37-research-lock-v1",
        "document_count": research["research_document_count"] == 7,
        "document_hashes": research["research_documents"] == current_research_records,
        "external_lock_status": research["external_lock_status"] == "PASS"
        and all(item["match"] for item in research["external_locks"]),
        "target_data_na": isinstance(research["target_zero_data"], str)
        and research["target_zero_data"].startswith("not_applicable;"),
        "route_b_false": research["route_b_invocation_allowed"] is False,
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
        "candidate": route.get("candidate_id") == "SD-C37",
        "source_lock_keys": REQUIRED_SOURCE_LOCK_KEYS
        <= set(route.get("source_lock", {})),
        "layer_evidence_statuses": all(
            route.get(name, {}).get("evidence_status") in EVIDENCE_STATUSES
            for name in ("a0", "a1", "a2", "a3", "a4")
        ),
        "layer_verdicts": [
            route[name]["verdict"] for name in ("a0", "a1", "a2", "a3", "a4")
        ]
        == ROUTE_TUPLE,
        "route_tuple": route.get("route_tuple") == ROUTE_TUPLE,
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_pending_provenance": provenance == [PENDING, PENDING, PENDING],
        "two_stage_note": "Two-stage provenance" in route.get("freeze_note", "")
        and PENDING in route.get("freeze_note", ""),
        "all_target_zero_root_fields_scoped": bool(target_fields)
        and all(
            isinstance(value, str) and value.startswith("not_applicable;")
            for _, value in target_fields
        ),
        "a2_stability_fields_scoped": all(
            isinstance(a2_metrics.get(field), str)
            and a2_metrics[field].startswith("not_applicable;")
            for field in A2_STABILITY_FIELDS
        ),
        "artifact_paths_cover_ledger": ledger_paths_expected <= route_artifacts,
        "artifact_paths_exist": all((ROOT / path).is_file() for path in route_artifacts),
        "route_card_excluded_from_ledger": ROUTE_RELATIVE not in ledger_paths_expected,
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
        "inventory_schema": inventory["schema_version"]
        == "SD-C37-artifact-inventory-v1",
        "inventory_entries": inventory["typed_entries"] == expected_entries,
        "inventory_counts": inventory["typed_entry_count"] == len(expected_entries) == 47
        and inventory["exact_final_result_count"] == 34
        and inventory["scientific_payload_count"] == 23,
        "route_exclusion": inventory[
            "route_card_excluded_for_metadata_only_provenance_binding"
        ],
    }

    hygiene_results = hygiene(canonical_paths())
    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
    )
    hygiene_checks = {
        "all_canonical_files_present": not hygiene_results["missing_canonical_files"],
        "no_symlinks": not hygiene_results["symlink_files"],
        "all_canonical_text_lf": not hygiene_results["crlf_files"],
        "all_canonical_text_exact_one_lf_eof": not hygiene_results[
            "noncanonical_eof_files"
        ],
        "all_canonical_text_no_trailing_whitespace": not hygiene_results[
            "trailing_whitespace_files"
        ],
        "all_canonical_text_no_control_bytes": not hygiene_results[
            "control_byte_files"
        ],
        "all_canonical_text_utf8": not hygiene_results["utf8_failures"],
        "all_json_parse": not hygiene_results["json_failures"],
        "all_csv_parse": not hygiene_results["csv_failures"],
        "all_yaml_parse": not hygiene_results["yaml_failures"],
        "no_python_or_test_cache": not cache_paths,
    }
    separation_checks = source_separation_checks()
    all_groups = {
        "scientific": scientific_checks,
        "reproducibility": reproducibility_checks,
        "research": research_checks,
        "route": route_checks,
        "ledger": ledger_checks,
        "hygiene": hygiene_checks,
        "separation": separation_checks,
    }
    passed = all(value for group in all_groups.values() for value in group.values())
    payload = {
        "schema_version": "SD-C37-integrity-v1",
        "candidate_id": "SD-C37",
        "counts": {
            "scientific_checks_passed": sum(scientific_checks.values()),
            "scientific_checks_total": len(scientific_checks),
            "all_group_checks_passed": sum(
                value for group in all_groups.values() for value in group.values()
            ),
            "all_group_checks_total": sum(len(group) for group in all_groups.values()),
            "canonical_text_files_checked": len(canonical_paths()),
            "ledger_entries": len(parsed),
            "result_files": len(actual_results),
            "python_sources": len(PYTHON_SOURCES),
        },
        "scientific_checks": scientific_checks,
        "reproducibility_checks": reproducibility_checks,
        "research_checks": research_checks,
        "route_checks": route_checks,
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
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not passed:
        raise SystemExit(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
