#!/usr/bin/env python3
"""Strict source, science, Route-A, ledger, and hygiene audit for SD-C35."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Iterable, Mapping

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_CARD = ROOT / "evaluations" / "route_a" / "SD-C35" / "2026-08-15.yaml"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
CORE_SHA256 = "3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168"
RUNNER_SHA256 = "03e840f8941e69220a467fa106a55939529bd1adbe1b2fe2d2e67d2fb1887335"
PROTOTYPE_AGGREGATE = "c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4"
RESEARCH_HASHES = {
    "research_package_sha256": "15c414149e4e06953be394f7175e98d504a688769bbad168365b86c853b8533f",
    "source_lock_sha256": "d3653a9c8a663b5e9a89964f5e8ea2528e28f12384162963bc312c00e7173649",
    "derivation_package_sha256": "38c426c80fae8764e0ece18eb36864acb31868388f36e3ac65f82673b3add2ce",
    "proof_package_sha256": "610ca712bc011bad6cfac10f3ff05e0fbe256044c0a8f27adf8873b3dbf0ca8b",
    "literature_audit_sha256": "382e1b44f51ef18868746855422541676aeb3a0512c2973754c1d18076218c27",
    "route_a_research_yaml_sha256": "5f8c62144e3df01f0a0eabf1b46e229e31ea31e2a040563227e9dc6a5d1c90fd",
}

PYTHON_SOURCES = (
    "code/audit_artifact_integrity.py",
    "code/audit_idempotence.py",
    "code/audit_source_separation.py",
    "code/cycle_quotient_core.py",
    "code/freeze_artifacts.py",
    "code/generate_results.py",
    "code/independent_evaluator.py",
    "code/post_census_classifier.py",
    "code/run_tests.py",
    "code/source_generator.py",
    "code/write_run_locks.py",
    "experiments/run_exact_suite.py",
)
EXPERIMENT_CONTROLS = (
    "EXPERIMENT_REPORT.md",
    "docs/EXPERIMENT_ARTIFACT_SCHEMA.md",
    "docs/candidate_registry.md",
    "docs/obstruction_registry.md",
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "experiments/IMPLEMENTATION_NOTES.md",
)
RESULT_PAYLOADS = (
    "classification_certificate.json",
    "cross_square_complex.json",
    "double_run_certificate.json",
    "environment_lock.json",
    "evaluation.json",
    "evaluation_comparison.csv",
    "matched_clone.csv",
    "modulus_homology_census.csv",
    "modulus_source_census.csv",
    "prototype_bridge_certificate.json",
    "random_action_controls.csv",
    "research_lock.json",
    "run_parameters.json",
    "source_oracle_certificate.json",
    "source_separation_certificate.json",
    "source_summary.json",
    "source_test_report.json",
    "summary.json",
    "test_report.json",
    "twist_census.csv",
    "unit_test_report.json",
)
META_RESULT_FILES = (
    "SHA256SUMS.txt",
    "aggregate_sha256.txt",
    "artifact_inventory.json",
    "idempotence_certificate.json",
    "integrity_audit.json",
)
ROUTE_RELATIVE = "evaluations/route_a/SD-C35/2026-08-15.yaml"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
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
TARGET_ZERO_FIELDS = (
    "zero_error_train",
    "zero_error_validation",
    "zero_error_test",
    "extra_zero_count",
    "missing_zero_count",
    "root_count_discrepancy",
)
RAW_HEADER = (
    "modulus",
    "state_count",
    "s_orbits",
    "r_orbits",
    "relation_rank",
    "relative_betti",
    "cusp_count",
    "cuspidal_betti",
    "cusp_rs_middle_distinct",
    "cusp_rs_returns",
    "adjacency_augmented_rank",
    "adjacency_descends",
)
LABEL_HEADER = RAW_HEADER + (
    "evaluator_class",
    "evaluator_prime",
    "residual_relative_nonzero",
    "residual_cuspidal_nonzero",
)
EXPECTED_RESULT_ROWS = {
    "modulus_source_census.csv": 191,
    "modulus_homology_census.csv": 191,
    "matched_clone.csv": 191,
    "random_action_controls.csv": 64,
    "twist_census.csv": 21,
    "evaluation_comparison.csv": 3,
}
BANNED_SOURCE_IDENTIFIERS = {
    "accepted_support",
    "classify",
    "evaluator_class",
    "evaluator_prime",
    "factor_integer",
    "is_prime",
    "mixed_composite",
    "prime_power",
    "prime_table",
    "riemann_zero",
    "target_zero",
    "zeta_zero",
}
FORBIDDEN_EVALUATOR_IMPORTS = {
    "cycle_quotient_core",
    "generate_results",
    "post_census_classifier",
    "source_generator",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(result_dir: Path, name: str) -> object:
    return json.loads((result_dir / name).read_text(encoding="utf-8"))


def read_csv(result_dir: Path, name: str) -> list[dict[str, str]]:
    with (result_dir / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def csv_header(result_dir: Path, name: str) -> tuple[str, ...]:
    with (result_dir / name).open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        return tuple(next(reader))


def resolved_path(result_dir: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"unsafe ledger path: {relative}")
    if relative.startswith("results/"):
        return result_dir / relative.removeprefix("results/")
    return ROOT / relative


def expected_typed_entries(result_dir: Path) -> list[dict[str, str]]:
    typed: list[tuple[str, str]] = []
    typed.extend(("python_source", path) for path in PYTHON_SOURCES)
    typed.extend(("experiment_control", path) for path in EXPERIMENT_CONTROLS)
    typed.extend(
        ("result_payload", f"results/{name}") for name in RESULT_PAYLOADS
    )
    return [
        {
            "kind": kind,
            "path": relative,
            "sha256": digest(resolved_path(result_dir, relative)),
        }
        for kind, relative in sorted(typed, key=lambda row: row[1])
    ]


def parse_ledger(
    result_dir: Path,
    path: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    pattern = re.compile(r"^([0-9a-f]{64})  ([^\r\n]+)$")
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = pattern.fullmatch(line)
        if match is None:
            errors.append(f"line {index}: malformed")
            continue
        sha256, relative = match.groups()
        try:
            actual = digest(resolved_path(result_dir, relative))
        except (FileNotFoundError, ValueError) as error:
            errors.append(f"line {index}: {error}")
            actual = ""
        rows.append({"path": relative, "sha256": sha256, "actual": actual})
    return rows, errors


def ast_identifiers(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found: set[str] = set()
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Name):
            names.append(node.id)
        elif isinstance(node, ast.Attribute):
            names.append(node.attr)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.append(node.name)
        elif isinstance(node, ast.arg):
            names.append(node.arg)
        found.update(name.lower() for name in names)
    return found


def ast_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    return imports


def json_all_true(payload: object, field: str) -> bool:
    return (
        isinstance(payload, Mapping)
        and payload.get("failures") == []
        and payload.get("passes") == payload.get("test_count")
        and payload.get("test_count") == field
    )


def exact_not_applicable(metrics: object) -> bool:
    return isinstance(metrics, Mapping) and all(
        metrics.get(field) == "not_applicable" for field in TARGET_ZERO_FIELDS
    )


def canonical_text_paths() -> list[Path]:
    """Audit canonical text while excluding transient TeX compiler products."""

    transient_suffixes = {".aux", ".blg", ".log", ".out", ".pdf"}
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() not in transient_suffixes:
            try:
                path.read_bytes().decode("utf-8")
            except UnicodeDecodeError:
                continue
            paths.append(path)
    return sorted(paths)


def text_hygiene(paths: Iterable[Path]) -> dict[str, list[str]]:
    failures = {
        "crlf_files": [],
        "control_byte_files": [],
        "trailing_whitespace_files": [],
        "noncanonical_eof_files": [],
    }
    for path in paths:
        raw = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        if b"\r" in raw:
            failures["crlf_files"].append(relative)
        if any(byte < 32 and byte != 10 for byte in raw) or 127 in raw:
            failures["control_byte_files"].append(relative)
        if any(line.endswith((b" ", b"\t")) for line in raw.splitlines()):
            failures["trailing_whitespace_files"].append(relative)
        if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
            failures["noncanonical_eof_files"].append(relative)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default=str(RESULTS))
    parser.add_argument("--allow-bootstrap-idempotence", action="store_true")
    args = parser.parse_args()
    result_dir = Path(args.result_dir).resolve()
    output = result_dir / "integrity_audit.json"

    ledger_rows, ledger_errors = parse_ledger(
        result_dir,
        result_dir / "SHA256SUMS.txt",
    )
    expected_entries = expected_typed_entries(result_dir)
    expected_ledger = [
        {"path": row["path"], "sha256": row["sha256"]}
        for row in expected_entries
    ]
    observed_ledger = [
        {"path": row["path"], "sha256": row["sha256"]}
        for row in ledger_rows
    ]
    inventory = load_json(result_dir, "artifact_inventory.json")
    aggregate_sha256 = digest(result_dir / "SHA256SUMS.txt")

    expected_code = {
        Path(path).name for path in PYTHON_SOURCES if path.startswith("code/")
    }
    expected_experiment_python = {
        Path(path).name
        for path in PYTHON_SOURCES
        if path.startswith("experiments/")
    }
    actual_code = {path.name for path in (ROOT / "code").glob("*.py")}
    actual_experiment_python = {
        path.name for path in (ROOT / "experiments").glob("*.py")
    }
    actual_results = {
        path.name for path in result_dir.iterdir() if path.is_file()
    }
    expected_results = set(RESULT_PAYLOADS) | set(META_RESULT_FILES)
    result_set_after_write = actual_results | {output.name}

    ledger_checks = {
        "ledger_format": not ledger_errors,
        "ledger_paths_unique": len({row["path"] for row in ledger_rows}) == len(ledger_rows),
        "ledger_sorted": observed_ledger == sorted(observed_ledger, key=lambda row: row["path"]),
        "ledger_exact_complete_set": observed_ledger == expected_ledger,
        "ledger_hashes_match": all(row["sha256"] == row["actual"] for row in ledger_rows),
        "aggregate_matches_ledger": (result_dir / "aggregate_sha256.txt").read_text(encoding="utf-8") == aggregate_sha256 + "\n",
        "inventory_schema": isinstance(inventory, Mapping)
        and inventory.get("schema_version") == "paper_root_ledger_v2"
        and inventory.get("path_base") == "paper_root",
        "inventory_exact_entries": isinstance(inventory, Mapping)
        and inventory.get("files") == expected_entries,
        "inventory_counts": isinstance(inventory, Mapping)
        and inventory.get("python_source_count") == 12
        and inventory.get("experiment_control_count") == 7
        and inventory.get("result_payload_count") == 21
        and inventory.get("ledger_entry_count") == 40,
        "inventory_meta_exclusions": isinstance(inventory, Mapping)
        and inventory.get("meta_result_files_excluded") == list(META_RESULT_FILES)
        and inventory.get("route_card_audited_separately") == ROUTE_RELATIVE
        and inventory.get("route_card_excluded_for_metadata_only_provenance_binding") is True,
        "inventory_ledger_hash": isinstance(inventory, Mapping)
        and inventory.get("sha256sums_sha256") == aggregate_sha256,
        "python_source_set_exact": actual_code == expected_code
        and actual_experiment_python == expected_experiment_python,
        "result_set_exact_after_audit_write": result_set_after_write == expected_results,
    }

    route = yaml.safe_load(ROUTE_CARD.read_text(encoding="utf-8"))
    freeze_note = str(route.get("freeze_note", ""))
    source_lock = route.get("source_lock", {})
    listed_paths = source_lock.get("artifact_paths", [])
    required_artifact_paths = {
        *PYTHON_SOURCES,
        *EXPERIMENT_CONTROLS,
        *(f"results/{name}" for name in RESULT_PAYLOADS),
        *(f"results/{name}" for name in META_RESULT_FILES),
        ROUTE_RELATIVE,
    }
    missing_listed_files = sorted(
        path for path in listed_paths
        if not isinstance(path, str)
        or Path(path).is_absolute()
        or ".." in Path(path).parts
        or not (ROOT / path).is_file()
    )
    route_checks = {
        "required_top_level_keys": isinstance(route, Mapping)
        and not (REQUIRED_ROUTE_KEYS - set(route)),
        "schema": route.get("skill") == "route-a-evaluator"
        and route.get("skill_version") == "0.2.0",
        "candidate_and_family": route.get("candidate_id") == "SD-C35"
        and source_lock.get("family") == "symbolic_dynamics",
        "route_tuple": route.get("route_tuple") == ROUTE_TUPLE,
        "layer_verdicts": [route.get(f"a{i}", {}).get("verdict") for i in range(5)] == ROUTE_TUPLE,
        "evidence_statuses": [route.get(f"a{i}", {}).get("evidence_status") for i in range(5)]
        == ["PROVED", "REFUTED", "REFUTED", "STOP_SCOPED", "STOP_SCOPED"],
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "risk_realized": route.get("adversarial_controls", {}).get("proves_too_much_risk") == "REALIZED",
        "adversarial_stop": route.get("adversarial_controls", {}).get("verdict") == "STOP_PROVES_TOO_MUCH",
        "paired_pending_provenance": (
            route.get("source_commit"),
            route.get("code_commit"),
            source_lock.get("code_commit"),
        ) == (PENDING, PENDING, PENDING),
        "two_stage_metadata_note": all(
            phrase in freeze_note.lower()
            for phrase in ("stage 1", "stage 2", "metadata-only", "all three fields")
        ),
        "target_zero_metrics_a2_na": exact_not_applicable(route.get("a2", {}).get("metrics")),
        "target_zero_metrics_a4_na": exact_not_applicable(route.get("a4", {}).get("metrics")),
        "target_zero_false": route.get("a2", {}).get("metrics", {}).get("target_zero_data_used") is False
        and route.get("a4", {}).get("metrics", {}).get("target_zero_data_used") is False
        and route.get("adversarial_controls", {}).get("target_zero_controls_used") is False,
        "artifact_paths_cover_canonical_set": required_artifact_paths.issubset(set(listed_paths)),
        "artifact_paths_exist": not missing_listed_files,
        "route_card_not_in_sha_ledger": ROUTE_RELATIVE not in {row["path"] for row in ledger_rows},
    }

    core_path = ROOT / "code" / "cycle_quotient_core.py"
    runner_path = ROOT / "code" / "generate_results.py"
    source_path = ROOT / "code" / "source_generator.py"
    classifier_path = ROOT / "code" / "post_census_classifier.py"
    evaluator_path = ROOT / "code" / "independent_evaluator.py"
    core_hits = ast_identifiers(core_path) & BANNED_SOURCE_IDENTIFIERS
    source_hits = ast_identifiers(source_path) & BANNED_SOURCE_IDENTIFIERS
    evaluator_import_hits = ast_imports(evaluator_path) & FORBIDDEN_EVALUATOR_IMPORTS
    source_import_hits = ast_imports(source_path) & {
        "generate_results",
        "independent_evaluator",
        "post_census_classifier",
    }
    oracle = load_json(result_dir, "source_oracle_certificate.json")
    separation = load_json(result_dir, "source_separation_certificate.json")
    classification = load_json(result_dir, "classification_certificate.json")
    bridge = load_json(result_dir, "prototype_bridge_certificate.json")
    separation_checks = {
        "prototype_core_sha": digest(core_path) == CORE_SHA256,
        "prototype_runner_sha": digest(runner_path) == RUNNER_SHA256,
        "candidate_sources_have_no_classifier_identifiers": not core_hits and not source_hits,
        "source_generator_has_no_postprocess_import": not source_import_hits,
        "independent_evaluator_has_no_project_import": not evaluator_import_hits,
        "process_files_physically_distinct": len({digest(source_path), digest(classifier_path), digest(evaluator_path)}) == 3,
        "raw_census_has_no_labels": csv_header(result_dir, "modulus_source_census.csv") == RAW_HEADER,
        "labelled_census_header_exact": csv_header(result_dir, "modulus_homology_census.csv") == LABEL_HEADER,
        "source_oracle": isinstance(oracle, Mapping)
        and oracle.get("pass") is True
        and oracle.get("hits") == [],
        "source_separation_certificate": isinstance(separation, Mapping)
        and separation.get("pass") is True
        and separation.get("banned_identifier_hits") == []
        and separation.get("core_bridge_exact") is True
        and separation.get("core_bridge_sha256_actual") == CORE_SHA256
        and separation.get("classifier_process") == classifier_path.name
        and separation.get("independent_evaluator_process") == evaluator_path.name,
        "classification_certificate": isinstance(classification, Mapping)
        and classification.get("pass") is True
        and classification.get("source_columns_preserved") is True
        and classification.get("rows") == 191
        and classification.get("class_counts") == {"prime": 43, "prime_power": 14, "mixed_composite": 134}
        and classification.get("classifier_sha256") == digest(classifier_path)
        and classification.get("raw_census_sha256") == digest(result_dir / "modulus_source_census.csv")
        and classification.get("labelled_census_sha256") == digest(result_dir / "modulus_homology_census.csv"),
        "prototype_bridge": isinstance(bridge, Mapping)
        and bridge.get("pass") is True
        and bridge.get("prototype_core_sha256_actual") == CORE_SHA256
        and bridge.get("prototype_runner_sha256_actual") == RUNNER_SHA256
        and bridge.get("prototype_payload_aggregate_actual") == PROTOTYPE_AGGREGATE
        and bridge.get("prototype_test_count") == bridge.get("prototype_test_passes") == 25,
    }

    raw_rows = read_csv(result_dir, "modulus_source_census.csv")
    census = read_csv(result_dir, "modulus_homology_census.csv")
    matched = read_csv(result_dir, "matched_clone.csv")
    random_rows = read_csv(result_dir, "random_action_controls.csv")
    twists = read_csv(result_dir, "twist_census.csv")
    comparison = read_csv(result_dir, "evaluation_comparison.csv")
    row_counts = {name: len(read_csv(result_dir, name)) for name in EXPECTED_RESULT_ROWS}
    raw_preserved = len(raw_rows) == len(census) and all(
        all(labelled[key] == raw[key] for key in RAW_HEADER)
        for raw, labelled in zip(raw_rows, census)
    )
    by_class = {
        label: [row for row in census if row["evaluator_class"] == label]
        for label in ("prime", "prime_power", "mixed_composite")
    }
    honest = [row for row in twists if row["kind"] == "honest_character"]
    virtual = [row for row in twists if row["kind"] == "zero_superdimension_difference"]
    cross = load_json(result_dir, "cross_square_complex.json")
    source_summary = load_json(result_dir, "source_summary.json")
    source_tests = load_json(result_dir, "source_test_report.json")
    summary = load_json(result_dir, "summary.json")
    prototype_tests = load_json(result_dir, "test_report.json")
    evaluation = load_json(result_dir, "evaluation.json")
    unit_tests = load_json(result_dir, "unit_test_report.json")
    double_run = load_json(result_dir, "double_run_certificate.json")
    environment = load_json(result_dir, "environment_lock.json")
    parameters = load_json(result_dir, "run_parameters.json")
    research = load_json(result_dir, "research_lock.json")
    idempotence = load_json(result_dir, "idempotence_certificate.json")

    expected_class_counts = {"prime": 43, "prime_power": 14, "mixed_composite": 134}
    expected_firewall = {
        "honest_identity_cycle_word_killers": 0,
        "honest_both_chain_norm_killers": 2,
        "honest_cusp_nonzero": 6,
        "virtual_identity_word_killers": 15,
        "virtual_both_chain_norm_killers": 2,
        "virtual_cusp_nonzero": 15,
    }
    observed_firewall = {
        "honest_identity_cycle_word_killers": sum(int(row["kills_identity_cycle_words"]) for row in honest),
        "honest_both_chain_norm_killers": sum(int(row["kills_both_chain_norms"]) for row in honest),
        "honest_cusp_nonzero": sum(int(row["cusp_sr_nonzero"]) for row in honest),
        "virtual_identity_word_killers": sum(int(row["kills_identity_cycle_words"]) for row in virtual),
        "virtual_both_chain_norm_killers": sum(int(row["kills_both_chain_norms"]) for row in virtual),
        "virtual_cusp_nonzero": sum(int(row["cusp_sr_nonzero"]) for row in virtual),
    }
    class_counts = {label: len(rows) for label, rows in by_class.items()}
    composite_rows = by_class["prime_power"] + by_class["mixed_composite"]
    double_payloads = double_run.get("payloads", []) if isinstance(double_run, Mapping) else []
    double_stdout = double_run.get("stdout", {}) if isinstance(double_run, Mapping) else {}
    idempotence_boolean_fields = (
        "freeze_byte_idempotent",
        "freeze_stdout_idempotent",
        "integrity_byte_idempotent",
        "integrity_stdout_idempotent",
    )
    idempotence_stage_ok = (
        idempotence.get("certificate_stage") == "final"
        or (
            args.allow_bootstrap_idempotence
            and idempotence.get("certificate_stage") == "bootstrap"
        )
    ) if isinstance(idempotence, Mapping) else False
    scientific_checks = {
        "csv_row_counts": row_counts == EXPECTED_RESULT_ROWS,
        "raw_columns_preserved": raw_preserved,
        "modulus_range": [int(row["modulus"]) for row in census] == list(range(2, 193)),
        "relation_rank_formula": all(int(row["relation_rank"]) == int(row["s_orbits"]) + int(row["r_orbits"]) - 1 for row in census),
        "quotient_dimension_formula": all(int(row["relative_betti"]) == int(row["state_count"]) - int(row["relation_rank"]) for row in census),
        "universal_cusp_return": all(row["cusp_rs_middle_distinct"] == row["cusp_rs_returns"] == "1" for row in census),
        "all_relative_survive": all(int(row["relative_betti"]) > 0 and row["residual_relative_nonzero"] == "1" for row in census),
        "class_counts": class_counts == expected_class_counts,
        "all_composites_survive": len(composite_rows) == 148 and all(int(row["relative_betti"]) > 0 for row in composite_rows),
        "composite_cuspidal_survivors": sum(int(row["cuspidal_betti"]) > 0 for row in composite_rows) == 139,
        "prime_cuspidal_zeros": sum(int(row["cuspidal_betti"]) == 0 for row in by_class["prime"]) == 5,
        "operator_non_descent_all": sum(int(row["adjacency_descends"]) for row in census) == 0,
        "operator_non_descent_n2": census[0]["modulus"] == "2"
        and census[0]["relation_rank"] == "2"
        and census[0]["adjacency_augmented_rank"] == "3",
        "matched_controls": len(matched) == 191
        and all(row["transport_exact"] == row["state_count_equal"] == row["component_count_equal"] == "1" for row in matched)
        and all(row["relative_betti_original"] == row["relative_betti_clone"] for row in matched)
        and all(row["relation_rank_original"] == row["relation_rank_clone"] for row in matched),
        "random_controls": len(random_rows) == 64
        and all(row["components"] == row["s2_killed_by_relation_quotient"] == row["r3_killed_by_relation_quotient"] == row["residual_nonzero"] == "1" for row in random_rows)
        and all(int(row["residual_betti"]) > 0 for row in random_rows),
        "character_firewall": len(honest) == 6 and len(virtual) == 15 and observed_firewall == expected_firewall,
        "cross_diamonds": cross == {
            "cutoff": 192,
            "nodes": 191,
            "edges": 158,
            "components": 64,
            "diamonds": 31,
            "graph_betti_before_filling": 31,
            "diamond_boundary_rank": 31,
            "homology_after_filling": 0,
            "component_invariant": "remove_all_factors_2_and_3",
        },
        "source_summary": isinstance(source_summary, Mapping)
        and source_summary.get("moduli") == 191
        and source_summary.get("matched_clone_exact_rows") == 191
        and source_summary.get("random_controls_relators_killed") == 64
        and source_summary.get("random_controls_residual_nonzero") == 64
        and source_summary.get("all_tested_adjacencies_fail_to_descend") is True,
        "source_tests_21": isinstance(source_tests, Mapping)
        and source_tests.get("passes") == source_tests.get("test_count") == 21
        and source_tests.get("failures") == []
        and all(source_tests.get("checks", {}).values()),
        "prototype_tests_25": isinstance(prototype_tests, Mapping)
        and prototype_tests.get("passes") == prototype_tests.get("test_count") == 25
        and prototype_tests.get("failures") == []
        and all(prototype_tests.get("checks", {}).values()),
        "summary_semantics": isinstance(summary, Mapping)
        and summary.get("route_tuple") == ROUTE_TUPLE
        and summary.get("overall") == "ROUTE_A_REJECTED"
        and summary.get("route_b") == "LOCKED"
        and summary.get("branch_action") == "CLOSE_SEMIRING_RESIDUE_FAMILY"
        and summary.get("class_summary", {}).get("prime", {}).get("relative_nonzero") == 43
        and summary.get("class_summary", {}).get("prime_power", {}).get("relative_nonzero") == 14
        and summary.get("class_summary", {}).get("mixed_composite", {}).get("relative_nonzero") == 134,
        "independent_evaluation_8349": isinstance(evaluation, Mapping)
        and evaluation.get("pass") is True
        and evaluation.get("failures") == []
        and evaluation.get("low_level_checks_passed") == evaluation.get("low_level_checks_total") == 8349
        and evaluation.get("imports_candidate_or_generator_modules") is False
        and evaluation.get("route_tuple") == ROUTE_TUPLE
        and evaluation.get("overall_verdict") == "ROUTE_A_REJECTED"
        and evaluation.get("branch_action") == "CLOSE_SEMIRING_RESIDUE_FAMILY"
        and evaluation.get("character_firewall") == expected_firewall,
        "unit_tests_1932": isinstance(unit_tests, Mapping)
        and unit_tests.get("passes") == unit_tests.get("test_count") == 1932
        and unit_tests.get("failures") == [],
        "comparison_table": len(comparison) == 3
        and {row["stratum"]: int(row["blocks"]) for row in comparison} == expected_class_counts
        and all(int(row["relative_nonzero"]) == expected_class_counts[row["stratum"]] for row in comparison),
        "double_run_20": isinstance(double_run, Mapping)
        and double_run.get("payload_count") == 20
        and double_run.get("payloads_identical_to_frozen") is True
        and double_run.get("stdout_identical") is True
        and len(double_payloads) == 20
        and all(row.get("byte_identical") is True and row.get("run_a") == row.get("run_b") == row.get("frozen") for row in double_payloads)
        and len(double_stdout) == 6
        and all(row.get("identical") is True and row.get("run_a_sha256") == row.get("run_b_sha256") for row in double_stdout.values()),
        "run_locks": isinstance(environment, Mapping)
        and environment.get("target_zero_data_used") is False
        and environment.get("python_cache_policy") == "PYTHONDONTWRITEBYTECODE=1"
        and isinstance(parameters, Mapping)
        and parameters.get("cutoff") == 192
        and parameters.get("random_trials") == 64
        and parameters.get("route_b_invocation_allowed") is False
        and parameters.get("pipeline") == [
            "source_generator.py",
            "audit_source_separation.py",
            "post_census_classifier.py",
            "independent_evaluator.py",
            "run_tests.py",
        ],
        "research_lock": isinstance(research, Mapping)
        and all(research.get(key) == value for key, value in RESEARCH_HASHES.items())
        and research.get("prototype_core_sha256") == CORE_SHA256
        and research.get("prototype_runner_sha256") == RUNNER_SHA256
        and research.get("canonical_experiment_plan_precedes_outputs") is True
        and research.get("canonical_experiment_plan_sha256") == digest(ROOT / "experiments" / "EXPERIMENT_PLAN.md"),
        "idempotence_semantics": isinstance(idempotence, Mapping)
        and idempotence.get("pass") is True
        and idempotence_stage_ok
        and all(idempotence.get(field) is True for field in idempotence_boolean_fields),
        "target_zero_not_used": isinstance(evaluation, Mapping)
        and evaluation.get("target_zero_data_used") is False
        and evaluation.get("route_b_invocation_allowed") is False
        and exact_not_applicable(evaluation.get("target_zero_metrics")),
    }

    route_science_checks = {
        "route_a1_counts": route.get("a1", {}).get("metrics", {}).get("prime_relative_nonzero") == 43
        and route.get("a1", {}).get("metrics", {}).get("prime_power_relative_nonzero") == 14
        and route.get("a1", {}).get("metrics", {}).get("mixed_composite_relative_nonzero") == 134
        and route.get("a1", {}).get("metrics", {}).get("all_composite_relative_nonzero") == 148
        and route.get("a1", {}).get("metrics", {}).get("random_controls_relators_killed") == 64
        and route.get("a1", {}).get("metrics", {}).get("random_controls_residual_nonzero") == 64,
        "route_character_firewall": route.get("a1", {}).get("metrics", {}).get("honest_characters_killing_identity_cycle_words") == 0
        and route.get("a1", {}).get("metrics", {}).get("honest_characters_killing_both_chain_norms") == 2
        and route.get("a1", {}).get("metrics", {}).get("zero_superdimension_twists_killing_identity_cycle_words") == 15
        and route.get("a1", {}).get("metrics", {}).get("zero_superdimension_twists_killing_both_chain_norms") == 2
        and route.get("a1", {}).get("metrics", {}).get("zero_superdimension_twists_with_cusp_survivor") == 15,
        "route_operator_non_descent": route.get("a2", {}).get("metrics", {}).get("tested_blocks_with_operator_descent") == 0
        and route.get("a2", {}).get("metrics", {}).get("tested_blocks_with_operator_non_descent") == 191
        and route.get("a2", {}).get("metrics", {}).get("primary_quotient_operator_owned") is False,
        "route_generator_word_firewall": "generator sequence R then S" in route.get("a1", {}).get("strongest_failure", "")
        and "operator word SR" in route.get("a1", {}).get("strongest_failure", ""),
        "family_closed": "semiring-residue family" in str(route.get("next_smallest_test", "")).lower()
        or "semiring-residue family" in str(route.get("claim_boundary", "")).lower(),
    }

    text_paths = canonical_text_paths()
    hygiene_failures = text_hygiene(text_paths)
    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache"}
        or path.suffix.lower() in {".pyc", ".pyo"}
    )
    plan_text = (ROOT / "experiments" / "EXPERIMENT_PLAN.md").read_text(encoding="utf-8")
    hygiene_checks = {
        "no_python_or_test_cache": not cache_paths,
        "all_canonical_text_lf": not hygiene_failures["crlf_files"],
        "all_canonical_text_no_control_bytes": not hygiene_failures["control_byte_files"],
        "all_canonical_text_no_trailing_whitespace": not hygiene_failures["trailing_whitespace_files"],
        "all_canonical_text_exact_one_lf_eof": not hygiene_failures["noncanonical_eof_files"],
        "prereg_no_premature_commit_hash": "8d09007" not in plan_text
        and re.search(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", plan_text.lower()) is None,
    }

    all_checks = {
        **ledger_checks,
        **route_checks,
        **separation_checks,
        **scientific_checks,
        **route_science_checks,
        **hygiene_checks,
    }
    passed = all(all_checks.values())
    payload = {
        "candidate_id": "SD-C35",
        "status": "PASS" if passed else "FAIL",
        "pass": passed,
        "ledger_checks": ledger_checks,
        "route_checks": route_checks,
        "separation_checks": separation_checks,
        "scientific_checks": scientific_checks,
        "route_science_checks": route_science_checks,
        "hygiene_checks": hygiene_checks,
        "counts": {
            "python_sources": 12,
            "experiment_controls": 7,
            "result_payloads": 21,
            "ledger_entries": len(ledger_rows),
            "canonical_text_files_checked": len(text_paths),
            "scientific_checks_passed": sum(scientific_checks.values()),
            "scientific_checks_total": len(scientific_checks),
            "all_group_checks_passed": sum(all_checks.values()),
            "all_group_checks_total": len(all_checks),
        },
        "sha256sums_sha256": aggregate_sha256,
        "ledger_errors": ledger_errors,
        "missing_route_artifact_files": missing_listed_files,
        "cache_paths": cache_paths,
        **hygiene_failures,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
        "bootstrap_idempotence_allowed": args.allow_bootstrap_idempotence,
    }
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "candidate_id": "SD-C35",
        "pass": passed,
        "checks": f"{sum(all_checks.values())}/{len(all_checks)}",
        "ledger_entries": len(ledger_rows),
        "python_sources": 12,
        "result_payloads": 21,
    }, sort_keys=True))
    if not passed:
        failures = [name for name, value in all_checks.items() if not value]
        print(json.dumps({"failures": failures}, sort_keys=True), file=sys.stderr)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
