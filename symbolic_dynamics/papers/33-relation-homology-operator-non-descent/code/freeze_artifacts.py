#!/usr/bin/env python3
"""Freeze the complete Paper 33 experimental source/result SHA-256 ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

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

ROUTE_CARD = "evaluations/route_a/SD-C35/2026-08-15.yaml"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def result_path(result_dir: Path, relative: str) -> Path:
    if not relative.startswith("results/"):
        raise ValueError(f"not a result path: {relative}")
    return result_dir / relative.removeprefix("results/")


def resolved_path(result_dir: Path, relative: str) -> Path:
    if relative.startswith("results/"):
        return result_path(result_dir, relative)
    return ROOT / relative


def entries(
    result_dir: Path,
) -> list[tuple[str, str, str]]:
    typed_paths: list[tuple[str, str]] = []
    typed_paths.extend(("python_source", path) for path in PYTHON_SOURCES)
    typed_paths.extend(
        ("experiment_control", path) for path in EXPERIMENT_CONTROLS
    )
    typed_paths.extend(
        ("result_payload", f"results/{name}")
        for name in RESULT_PAYLOADS
    )
    answer: list[tuple[str, str, str]] = []
    for kind, relative in sorted(typed_paths, key=lambda row: row[1]):
        path = resolved_path(result_dir, relative)
        if not path.is_file():
            raise FileNotFoundError(path)
        answer.append((kind, relative, digest(path)))
    return answer


def actual_names(paths: Iterable[Path]) -> set[str]:
    return {path.name for path in paths if path.is_file()}


def validate_exact_sets(result_dir: Path) -> None:
    expected_code = {
        Path(path).name for path in PYTHON_SOURCES if path.startswith("code/")
    }
    expected_experiment_python = {
        Path(path).name
        for path in PYTHON_SOURCES
        if path.startswith("experiments/")
    }
    actual_code = actual_names((ROOT / "code").glob("*.py"))
    actual_experiment_python = actual_names(
        (ROOT / "experiments").glob("*.py")
    )
    if actual_code != expected_code:
        raise RuntimeError(
            f"unexpected code source set: {sorted(actual_code ^ expected_code)}"
        )
    if actual_experiment_python != expected_experiment_python:
        raise RuntimeError(
            "unexpected experiment Python set: "
            f"{sorted(actual_experiment_python ^ expected_experiment_python)}"
        )

    expected_payloads = set(RESULT_PAYLOADS)
    known_results = expected_payloads | set(META_RESULT_FILES)
    actual_results = actual_names(result_dir.iterdir())
    missing_payloads = expected_payloads - actual_results
    unknown_results = actual_results - known_results
    if missing_payloads or unknown_results:
        raise RuntimeError(
            "invalid result file set: "
            f"missing_payloads={sorted(missing_payloads)}, "
            f"unknown_results={sorted(unknown_results)}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default=str(RESULTS))
    args = parser.parse_args()

    result_dir = Path(args.result_dir).resolve()
    result_dir.mkdir(parents=True, exist_ok=True)
    validate_exact_sets(result_dir)
    frozen = entries(result_dir)

    ledger_path = result_dir / "SHA256SUMS.txt"
    ledger_text = "".join(
        f"{sha256}  {relative}\n"
        for _, relative, sha256 in frozen
    )
    ledger_path.write_text(ledger_text, encoding="utf-8")
    ledger_sha256 = digest(ledger_path)
    (result_dir / "aggregate_sha256.txt").write_text(
        ledger_sha256 + "\n",
        encoding="utf-8",
    )

    counts = {
        "python_source_count": sum(
            kind == "python_source" for kind, _, _ in frozen
        ),
        "experiment_control_count": sum(
            kind == "experiment_control" for kind, _, _ in frozen
        ),
        "result_payload_count": sum(
            kind == "result_payload" for kind, _, _ in frozen
        ),
    }
    inventory = {
        "candidate_id": "SD-C35",
        "schema_version": "paper_root_ledger_v2",
        "path_base": "paper_root",
        "route_card_audited_separately": ROUTE_CARD,
        "route_card_excluded_for_metadata_only_provenance_binding": True,
        "meta_result_files_excluded": list(META_RESULT_FILES),
        **counts,
        "ledger_entry_count": len(frozen),
        "sha256sums_sha256": ledger_sha256,
        "files": [
            {"kind": kind, "path": relative, "sha256": sha256}
            for kind, relative, sha256 in frozen
        ],
    }
    (result_dir / "artifact_inventory.json").write_text(
        json.dumps(inventory, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "candidate_id": "SD-C35",
        **counts,
        "ledger_entry_count": len(frozen),
        "sha256sums_sha256": ledger_sha256,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
