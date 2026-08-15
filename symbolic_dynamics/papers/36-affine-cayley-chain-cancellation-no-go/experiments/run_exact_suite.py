#!/usr/bin/env python3
"""Run fresh A/B plus cache-free cold C scientific pipelines for SD-C38."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
FRESH_NAMES = tuple(
    sorted(
        (
            "ANALYSIS_REPORT.md",
            "analysis.json",
            "control_summary.json",
            "dependency_lock.json",
            "environment_lock.json",
            "evaluation.json",
            "finite_chain_audit.csv",
            "graded_control.json",
            "marker_audit.csv",
            "operator_cycle_audit.csv",
            "prototype_bridge_certificate.json",
            "raw_data_table.csv",
            "run_parameters.json",
            "source_raw.json",
            "source_separation_certificate.json",
            "source_summary.json",
            "source_test_report.json",
            "test_report.json",
            "trace_audit.csv",
        )
    )
)
STAGES = (
    ("locks", "write_run_locks.py"),
    ("source", "source_generator.py"),
    ("separation", "audit_source_separation.py"),
    ("evaluation", "evaluate_results.py"),
    ("tests", "run_tests.py"),
    ("analysis", "analyze_results.py"),
)
RESEARCH_DOCUMENTS = (
    ("source_lock_sha256", "SOURCE_LOCK.md"),
    ("root_preregistration_sha256", "PREREGISTRATION.md"),
    ("derivation_package_sha256", "DERIVATION_PACKAGE.md"),
    ("proof_package_sha256", "PROOF_PACKAGE.md"),
    ("literature_audit_sha256", "LITERATURE_AUDIT.md"),
    ("experiment_preregistration_sha256", "experiments/PREREGISTRATION.md"),
    ("experiment_plan_sha256", "experiments/EXPERIMENT_PLAN.md"),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def write_json(path: Path, value: object) -> None:
    path.write_text(canonical_json(value), encoding="utf-8")


def execution_environment() -> dict[str, str]:
    values = dict(os.environ)
    values["PYTHONHASHSEED"] = "0"
    values["PYTHONDONTWRITEBYTECODE"] = "1"
    values["PYTHONPATH"] = str(CODE)
    return values


def remove_caches() -> list[str]:
    removed: list[str] = []
    for path in sorted(ROOT.rglob("*"), reverse=True):
        if path.is_dir() and path.name in {"__pycache__", ".pytest_cache"}:
            removed.append(path.relative_to(ROOT).as_posix())
            shutil.rmtree(path)
        elif path.is_file() and path.suffix == ".pyc":
            removed.append(path.relative_to(ROOT).as_posix())
            path.unlink()
    return sorted(removed)


def build(destination: Path) -> dict[str, str]:
    destination.mkdir(parents=True, exist_ok=False)
    stdout: dict[str, str] = {}
    for stage, script in STAGES:
        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                str(CODE / script),
                "--result-dir",
                str(destination),
            ],
            cwd=ROOT,
            env=execution_environment(),
            check=True,
            text=True,
            capture_output=True,
        )
        stdout[stage] = completed.stdout
    return stdout


def artifact_hashes(directory: Path) -> dict[str, str]:
    actual = tuple(sorted(path.name for path in directory.iterdir() if path.is_file()))
    if actual != FRESH_NAMES:
        raise RuntimeError(f"fresh inventory mismatch: expected {FRESH_NAMES}, found {actual}")
    return {name: digest(directory / name) for name in FRESH_NAMES}


def aggregate(hashes: dict[str, str]) -> str:
    payload = "".join(f"{hashes[name]}  {name}\n" for name in sorted(hashes))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def clear_results() -> None:
    if ROOT.name != "36-affine-cayley-chain-cancellation-no-go":
        raise RuntimeError("refusing to clear results under an unexpected authority root")
    if RESULTS.resolve() != (ROOT / "results").resolve():
        raise RuntimeError("result directory resolution mismatch")
    RESULTS.mkdir(parents=True, exist_ok=True)
    for path in list(RESULTS.iterdir()):
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()


def publish(source: Path) -> None:
    clear_results()
    for name in FRESH_NAMES:
        shutil.copy2(source / name, RESULTS / name)


def research_lock_payload() -> dict[str, object]:
    missing = [relative for _, relative in RESEARCH_DOCUMENTS if not (ROOT / relative).is_file()]
    if missing:
        raise RuntimeError(f"research documents are not ready: {missing}")
    records = [
        {
            "path": relative,
            "pointer_field": field,
            "sha256": digest(ROOT / relative),
        }
        for field, relative in RESEARCH_DOCUMENTS
    ]
    pointers = {record["pointer_field"]: record["sha256"] for record in records}
    research_package = Path("/tmp/paper36_research_package.md")
    research_hash = digest(research_package)
    if research_hash != "d29255f9eda598b780aa79165f0dcce6913880dcfa0b9ce5d370c1c43ffbd299":
        raise RuntimeError("frozen research package hash mismatch")
    return {
        "schema": "SD-C38-research-lock-v1",
        "candidate_id": "SD-C38",
        "research_document_count": len(records),
        "research_documents": records,
        **pointers,
        "research_package_path": "/tmp/paper36_research_package.md",
        "research_package_sha256": research_hash,
        "prototype_scientific_sha256": "499b1a5b0647e9a9999dbfdfc881a8edc0877875102d91607c10e041f69f5221",
        "plan_frozen_before_authority_code": True,
        "plan_frozen_before_authority_results": True,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }


def stdout_rows(first: dict[str, str], second: dict[str, str], cold: dict[str, str]):
    return {
        stage: {
            "run_a_sha256": hashlib.sha256(first[stage].encode("utf-8")).hexdigest(),
            "run_b_sha256": hashlib.sha256(second[stage].encode("utf-8")).hexdigest(),
            "cold_c_sha256": hashlib.sha256(cold[stage].encode("utf-8")).hexdigest(),
            "byte_identical": first[stage] == second[stage] == cold[stage],
        }
        for stage, _ in STAGES
    }


def write_metadata(
    first_hashes: dict[str, str],
    second_hashes: dict[str, str],
    cold_hashes: dict[str, str],
    first_stdout: dict[str, str],
    second_stdout: dict[str, str],
    cold_stdout: dict[str, str],
    removed_before_cold: list[str],
) -> None:
    research = research_lock_payload()
    write_json(RESULTS / "research_lock.json", research)
    research_lock_hash = digest(RESULTS / "research_lock.json")
    stage_stdout = stdout_rows(first_stdout, second_stdout, cold_stdout)
    double_pass = first_hashes == second_hashes and all(
        row["byte_identical"] for row in stage_stdout.values()
    )
    cold_pass = first_hashes == cold_hashes and all(
        row["byte_identical"] for row in stage_stdout.values()
    )
    write_json(
        RESULTS / "double_run_certificate.json",
        {
            "schema": "SD-C38-double-run-certificate-v1",
            "candidate_id": "SD-C38",
            "fresh_result_directories": 2,
            "scientific_payload_count": len(FRESH_NAMES),
            "run_a_hashes": first_hashes,
            "run_b_hashes": second_hashes,
            "run_a_aggregate_sha256": aggregate(first_hashes),
            "run_b_aggregate_sha256": aggregate(second_hashes),
            "payloads_byte_identical": first_hashes == second_hashes,
            "stage_stdout": stage_stdout,
            "stdout_byte_identical": all(row["byte_identical"] for row in stage_stdout.values()),
            "research_lock_sha256": research_lock_hash,
            "status": "PASS" if double_pass else "FAIL",
        },
    )
    write_json(
        RESULTS / "cold_start_certificate.json",
        {
            "schema": "SD-C38-cold-start-certificate-v1",
            "candidate_id": "SD-C38",
            "cold_directory_initially_absent": True,
            "cache_purge_performed": True,
            "cache_paths_removed_before_cold": removed_before_cold,
            "pythonhashseed": "0",
            "pythondontwritebytecode": "1",
            "scientific_payload_count": len(FRESH_NAMES),
            "reference_hashes": first_hashes,
            "cold_hashes": cold_hashes,
            "reference_aggregate_sha256": aggregate(first_hashes),
            "cold_aggregate_sha256": aggregate(cold_hashes),
            "payloads_byte_identical": first_hashes == cold_hashes,
            "research_lock_sha256": research_lock_hash,
            "status": "PASS" if cold_pass else "FAIL",
        },
    )
    write_json(
        RESULTS / "artifact_inventory.json",
        {
            "schema": "SD-C38-artifact-inventory-v1",
            "candidate_id": "SD-C38",
            "fresh_scientific_payload_count": len(FRESH_NAMES),
            "fresh_scientific_payloads": list(FRESH_NAMES),
            "run_metadata_payloads": [
                "artifact_inventory.json",
                "cold_start_certificate.json",
                "double_run_certificate.json",
                "research_lock.json",
            ],
            "integrity_meta_payloads": [
                "SHA256SUMS.txt",
                "aggregate_sha256.txt",
                "idempotence_certificate.json",
                "integrity_audit.json",
            ],
            "expected_final_result_count": len(FRESH_NAMES) + 8,
            "research_lock_sha256": research_lock_hash,
            "scientific_aggregate_sha256": aggregate(first_hashes),
        },
    )
    if not double_pass or not cold_pass:
        raise RuntimeError("fresh A/B or cold C reproducibility failed")


def main() -> int:
    remove_caches()
    first_root = Path(tempfile.mkdtemp(prefix="paper36-run-a-", dir="/tmp"))
    second_root = Path(tempfile.mkdtemp(prefix="paper36-run-b-", dir="/tmp"))
    cold_root = Path(tempfile.mkdtemp(prefix="paper36-cold-c-", dir="/tmp"))
    try:
        first_directory = first_root / "results"
        second_directory = second_root / "results"
        cold_directory = cold_root / "results"
        first_stdout = build(first_directory)
        second_stdout = build(second_directory)
        first_hashes = artifact_hashes(first_directory)
        second_hashes = artifact_hashes(second_directory)
        if first_hashes != second_hashes or first_stdout != second_stdout:
            raise RuntimeError("fresh A/B payload or stdout mismatch")
        removed_before_cold = remove_caches()
        cold_stdout = build(cold_directory)
        cold_hashes = artifact_hashes(cold_directory)
        if first_hashes != cold_hashes or first_stdout != cold_stdout:
            raise RuntimeError("cold C payload or stdout mismatch")
        publish(first_directory)
    finally:
        shutil.rmtree(first_root, ignore_errors=True)
        shutil.rmtree(second_root, ignore_errors=True)
        shutil.rmtree(cold_root, ignore_errors=True)

    write_metadata(
        first_hashes,
        second_hashes,
        cold_hashes,
        first_stdout,
        second_stdout,
        cold_stdout,
        removed_before_cold,
    )
    remove_caches()
    output = {
        "candidate_id": "SD-C38",
        "scientific_payload_count": len(FRESH_NAMES),
        "scientific_aggregate_sha256": aggregate(first_hashes),
        "fresh_a_b": "PASS",
        "cold_c": "PASS",
        "research_lock_sha256": digest(RESULTS / "research_lock.json"),
        "integrity_seal": "PENDING",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
