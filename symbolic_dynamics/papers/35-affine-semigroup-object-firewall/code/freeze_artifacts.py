#!/usr/bin/env python3
"""Freeze or verify the exact non-self-referential SD-C37 SHA ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PYTHON_SOURCES = (
    "code/analyze_results.py",
    "code/audit_integrity.py",
    "code/certify_stability.py",
    "code/freeze_artifacts.py",
    "code/generate_artifacts.py",
    "code/independent_evaluator.py",
    "code/run_tests.py",
    "code/seal_metadata.py",
    "code/source_core.py",
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
    "experiments/PREREGISTRATION.md",
)
SCIENTIFIC_PAYLOADS = (
    "ANALYSIS_REPORT.md",
    "admissible_word_census.csv",
    "analysis.json",
    "backtrack_ledger.csv",
    "bc_diagonal_fixtures.json",
    "bc_firewall.json",
    "boundary_controls.json",
    "commutation_witnesses.json",
    "control_evaluation.json",
    "counterexamples.json",
    "evaluation.json",
    "exact_summary.csv",
    "fock_marker_firewall.json",
    "full_monoid_boundary.json",
    "height_dag_ledger.csv",
    "monoid_relation_controls.json",
    "operator_certificates.json",
    "quotient_ledger.csv",
    "relation_witnesses.json",
    "source_evaluator_firewall.json",
    "source_manifest.json",
    "source_parameters.json",
    "test_report.json",
)
RUN_METADATA_PAYLOADS = (
    "cold_start_certificate.json",
    "double_run_certificate.json",
    "environment_lock.json",
    "metadata_seal_stability.json",
    "prototype_bridge.json",
    "research_lock.json",
)
RESULT_PAYLOADS = SCIENTIFIC_PAYLOADS + RUN_METADATA_PAYLOADS
META_RESULTS = (
    "SHA256SUMS.txt",
    "aggregate_sha256.txt",
    "artifact_inventory.json",
    "idempotence_certificate.json",
    "integrity_audit.json",
)
ROUTE_RELATIVE = "evaluations/route_a/SD-C37/2026-08-15.yaml"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def typed_entries() -> list[dict[str, str]]:
    entries: list[tuple[str, str]] = []
    entries.extend(("python_source", name) for name in PYTHON_SOURCES)
    entries.extend(("experiment_control", name) for name in EXPERIMENT_CONTROLS)
    entries.extend(("result_payload", f"results/{name}") for name in RESULT_PAYLOADS)
    return [
        {"kind": kind, "path": name, "sha256": digest(ROOT / name)}
        for kind, name in sorted(entries, key=lambda item: item[1])
    ]


def expected_outputs() -> tuple[str, str, str]:
    entries = typed_entries()
    ledger = "".join(f"{entry['sha256']}  {entry['path']}\n" for entry in entries)
    aggregate = hashlib.sha256(ledger.encode("utf-8")).hexdigest() + "\n"
    inventory = {
        "schema_version": "SD-C37-artifact-inventory-v1",
        "candidate_id": "SD-C37",
        "typed_entry_count": len(entries),
        "python_source_count": len(PYTHON_SOURCES),
        "experiment_control_count": len(EXPERIMENT_CONTROLS),
        "scientific_payload_count": len(SCIENTIFIC_PAYLOADS),
        "run_metadata_payload_count": len(RUN_METADATA_PAYLOADS),
        "result_payload_count": len(RESULT_PAYLOADS),
        "typed_entries": entries,
        "meta_result_files_excluded_from_ledger": list(META_RESULTS),
        "route_card_excluded_for_metadata_only_provenance_binding": True,
        "route_card_path": ROUTE_RELATIVE,
        "exact_final_result_count": len(RESULT_PAYLOADS) + len(META_RESULTS),
        "sha256sums_sha256": hashlib.sha256(ledger.encode("utf-8")).hexdigest(),
        "status": "PASS",
    }
    return ledger, aggregate, json.dumps(inventory, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args()
    ledger, aggregate, inventory = expected_outputs()
    paths = (
        (RESULTS / "SHA256SUMS.txt", ledger),
        (RESULTS / "aggregate_sha256.txt", aggregate),
        (RESULTS / "artifact_inventory.json", inventory),
    )
    if arguments.check:
        failures = [
            str(path)
            for path, text in paths
            if not path.is_file() or path.read_text(encoding="utf-8") != text
        ]
        if failures:
            raise SystemExit(f"freeze mismatch: {failures}")
    else:
        for path, text in paths:
            path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
