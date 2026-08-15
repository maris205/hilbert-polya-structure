#!/usr/bin/env python3
"""Freeze the exact experiment-owned SD-C38 SHA-256 ledger."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CODE_FILES = (
    "code/analyze_results.py",
    "code/audit_idempotence.py",
    "code/audit_integrity.py",
    "code/audit_source_separation.py",
    "code/evaluate_results.py",
    "code/freeze_artifacts.py",
    "code/independent_evaluator.py",
    "code/run_tests.py",
    "code/source_core.py",
    "code/source_generator.py",
    "code/write_run_locks.py",
)
EXPERIMENT_FILES = (
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "experiments/IMPLEMENTATION_NOTES.md",
    "experiments/PREREGISTRATION.md",
    "experiments/run_exact_suite.py",
)
DOC_FILES = (
    "docs/EXPERIMENT_ARTIFACT_SCHEMA.md",
    "docs/candidate_registry.md",
    "docs/obstruction_registry.md",
)
REPORT_FILES = (
    "EXPERIMENT_REPORT.md",
)
RESULT_FILES = (
    "results/ANALYSIS_REPORT.md",
    "results/analysis.json",
    "results/artifact_inventory.json",
    "results/cold_start_certificate.json",
    "results/control_summary.json",
    "results/dependency_lock.json",
    "results/double_run_certificate.json",
    "results/environment_lock.json",
    "results/evaluation.json",
    "results/finite_chain_audit.csv",
    "results/graded_control.json",
    "results/marker_audit.csv",
    "results/operator_cycle_audit.csv",
    "results/prototype_bridge_certificate.json",
    "results/raw_data_table.csv",
    "results/research_lock.json",
    "results/run_parameters.json",
    "results/source_raw.json",
    "results/source_separation_certificate.json",
    "results/source_summary.json",
    "results/source_test_report.json",
    "results/test_report.json",
    "results/trace_audit.csv",
)
LEDGER_PATHS = tuple(
    sorted(CODE_FILES + EXPERIMENT_FILES + DOC_FILES + REPORT_FILES + RESULT_FILES)
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ledger_bytes() -> bytes:
    missing = [relative for relative in LEDGER_PATHS if not (ROOT / relative).is_file()]
    if missing:
        raise RuntimeError(f"missing ledger inputs: {missing}")
    return "".join(
        f"{digest(ROOT / relative)}  {relative}\n" for relative in LEDGER_PATHS
    ).encode("utf-8")


def main() -> int:
    payload = ledger_bytes()
    (RESULTS / "SHA256SUMS.txt").write_bytes(payload)
    aggregate = hashlib.sha256(payload).hexdigest()
    (RESULTS / "aggregate_sha256.txt").write_text(aggregate + "\n", encoding="utf-8")
    print(f"entries={len(LEDGER_PATHS)} aggregate_sha256={aggregate}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
