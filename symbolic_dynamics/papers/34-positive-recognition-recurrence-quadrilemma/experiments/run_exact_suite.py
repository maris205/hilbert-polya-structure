#!/usr/bin/env python3
"""Run fresh A/B plus cold-start C scientific pipelines for SD-C36."""

from __future__ import annotations

from hashlib import sha256
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
FRESH_NAMES = tuple(
    sorted(
        {
            "ANALYSIS_REPORT.md",
            "analysis.json",
            "boundary_controls.json",
            "code_clock_ledger.csv",
            "connector_construction_counterexamples.csv",
            "counterexamples.json",
            "evaluation.json",
            "graph_census.csv",
            "graph_witness_samples.csv",
            "graph_witness_summary.json",
            "inventory_controls.csv",
            "kraft_clock_summary.csv",
            "marker_ledger.csv",
            "neutral_recognizer.json",
            "parameters.json",
            "pruning_polynomials.json",
            "raw_data_table.csv",
            "source_evaluator_firewall.json",
            "test_report.json",
        }
    )
)
RESEARCH_DOCUMENTS = (
    ("preregistration_sha256", "PREREGISTRATION.md"),
    ("source_lock_sha256", "SOURCE_LOCK.md"),
    ("derivation_package_sha256", "DERIVATION_PACKAGE.md"),
    ("proof_package_sha256", "PROOF_PACKAGE.md"),
    ("literature_audit_sha256", "LITERATURE_AUDIT.md"),
    ("experiment_plan_sha256", "experiments/EXPERIMENT_PLAN.md"),
)


def file_hash(path: Path) -> str:
    value = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def environment() -> dict[str, str]:
    values = dict(os.environ)
    values["PYTHONHASHSEED"] = "0"
    values["PYTHONDONTWRITEBYTECODE"] = "1"
    values["PYTHONPATH"] = str(CODE)
    return values


def command(script: str, *arguments: str) -> None:
    subprocess.run(
        [sys.executable, "-B", str(CODE / script), *arguments],
        cwd=ROOT,
        env=environment(),
        check=True,
    )


def remove_caches() -> None:
    for path in sorted(ROOT.rglob("*"), reverse=True):
        if path.is_dir() and path.name in {"__pycache__", ".pytest_cache"}:
            shutil.rmtree(path)


def build(destination: Path) -> None:
    command("generate_artifacts.py", "--output", str(destination))
    command("independent_evaluator.py", "--results", str(destination), "--code-root", str(CODE))
    command("run_tests.py", "--results", str(destination))
    command("analyze_results.py", "--results", str(destination))


def artifact_hashes(directory: Path) -> dict[str, str]:
    actual = tuple(sorted(path.name for path in directory.iterdir() if path.is_file()))
    if actual != FRESH_NAMES:
        raise RuntimeError(f"fresh inventory mismatch: expected {FRESH_NAMES}, found {actual}")
    return {name: file_hash(directory / name) for name in FRESH_NAMES}


def aggregate(hashes: dict[str, str]) -> str:
    payload = "".join(f"{hashes[name]}  {name}\n" for name in sorted(hashes))
    return sha256(payload.encode("utf-8")).hexdigest()


def clear_results() -> None:
    if (
        RESULTS.resolve() != (ROOT / "results").resolve()
        or ROOT.name != "34-positive-recognition-recurrence-quadrilemma"
    ):
        raise RuntimeError("refusing to clear an unexpected result directory")
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
    records = [
        {
            "path": relative,
            "pointer_field": field,
            "sha256": file_hash(ROOT / relative),
        }
        for field, relative in RESEARCH_DOCUMENTS
    ]
    pointers = {record["pointer_field"]: record["sha256"] for record in records}
    return {
        "schema_version": "SD-C36-research-lock-v2",
        "research_document_count": len(records),
        "research_documents": records,
        **pointers,
        "authority_plan_path": "experiments/EXPERIMENT_PLAN.md",
        "authority_plan_frozen_before_results": True,
        "preregistration_frozen_before_results": True,
        "C2_failure_retained": True,
        "mathematical_package_sha256": "2b9dc8106d3feaea7ed1c4bd377ec98e05baa25ca83bd370ec2fb9eee14952a7",
        "literature_package_sha256": "e67ab00a518def77c4bdc6ac157736f7f0c4fd7d6e1ee9b92e3f608700a013cc",
        "target_zero_data": "not_applicable; target_zero_data_forbidden_and_unused",
        "route_b_invocation_allowed": False,
    }


def environment_lock_payload() -> dict[str, object]:
    return {
        "schema_version": "P34-environment-v2",
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "scientific_dependencies": [],
        "seal_audit_dependencies": {
            "PyYAML": importlib.metadata.version("PyYAML"),
        },
        "dependency_roles": {
            "PyYAML": "Route-A YAML sealing and integrity audit only",
        },
        "cpu_only": True,
        "network_used": False,
        "external_data_used": False,
        "result_timestamps": False,
        "pythonhashseed": "0",
        "pythondontwritebytecode": "1",
    }


def write_metadata(
    first: dict[str, str],
    second: dict[str, str],
    cold: dict[str, str],
) -> None:
    byte_identical = first == second and aggregate(first) == aggregate(second)
    write_json(RESULTS / "research_lock.json", research_lock_payload())
    research_lock_sha256 = file_hash(RESULTS / "research_lock.json")
    write_json(
        RESULTS / "double_run_certificate.json",
        {
            "schema_version": "P34-double-run-v1",
            "runs": 2,
            "fresh_result_directories_each_run": True,
            "artifact_count": len(FRESH_NAMES),
            "byte_identical": byte_identical,
            "aggregate_sha256": aggregate(first),
            "first_hashes": first,
            "second_hashes": second,
            "mismatched_paths": sorted(name for name in FRESH_NAMES if first[name] != second[name]),
            "commands": [
                "generate_artifacts.py --output FRESH_RESULTS",
                "independent_evaluator.py --results FRESH_RESULTS --code-root FROZEN_CODE",
                "run_tests.py --results FRESH_RESULTS",
                "analyze_results.py --results FRESH_RESULTS",
            ],
            "pythonhashseed": "0",
            "pythondontwritebytecode": "1",
            "research_document_count": len(RESEARCH_DOCUMENTS),
            "research_lock_sha256": research_lock_sha256,
            "status": "PASS" if byte_identical else "FAIL",
        },
    )
    write_json(
        RESULTS / "environment_lock.json",
        environment_lock_payload(),
    )
    cold_identical = first == cold and aggregate(first) == aggregate(cold)
    write_json(
        RESULTS / "cold_start_certificate.json",
        {
            "schema_version": "SD-C36-cold-start-v1",
            "cold_start_directory_initially_absent": True,
            "cold_start_cache_free": True,
            "cold_start_artifact_count": len(FRESH_NAMES),
            "reference_aggregate_sha256": aggregate(first),
            "cold_start_aggregate_sha256": aggregate(cold),
            "hashes": cold,
            "research_lock_sha256": research_lock_sha256,
            "mismatched_paths": sorted(
                name for name in FRESH_NAMES if first[name] != cold[name]
            ),
            "byte_identical_to_published_science": cold_identical,
            "status": "PASS" if cold_identical else "FAIL",
        },
    )
    write_json(
        RESULTS / "artifact_inventory.json",
        {
            "schema_version": "P34-artifact-inventory-v1",
            "fresh_artifact_count": len(FRESH_NAMES),
            "fresh_artifacts": list(FRESH_NAMES),
            "run_metadata_before_seal": [
                "artifact_inventory.json",
                "cold_start_certificate.json",
                "double_run_certificate.json",
                "environment_lock.json",
                "research_lock.json",
            ],
            "expected_final_result_count": 29,
            "research_document_count": len(RESEARCH_DOCUMENTS),
            "research_lock_sha256": research_lock_sha256,
            "metadata_seal_pending": True,
        },
    )
    if not byte_identical or not cold_identical:
        raise RuntimeError("fresh or cold-start runs are not byte-identical")


def main() -> int:
    remove_caches()
    first_root = Path(tempfile.mkdtemp(prefix="paper34-run-a-", dir="/tmp"))
    second_root = Path(tempfile.mkdtemp(prefix="paper34-run-b-", dir="/tmp"))
    cold_root = Path(tempfile.mkdtemp(prefix="paper34-cold-c-", dir="/tmp"))
    try:
        first_directory = first_root / "results"
        second_directory = second_root / "results"
        cold_directory = cold_root / "results"
        build(first_directory)
        build(second_directory)
        first = artifact_hashes(first_directory)
        second = artifact_hashes(second_directory)
        if first != second:
            raise RuntimeError(
                f"fresh runs differ: {[name for name in FRESH_NAMES if first[name] != second[name]]}"
            )
        remove_caches()
        build(cold_directory)
        cold = artifact_hashes(cold_directory)
        if first != cold:
            raise RuntimeError(
                f"cold start differs: {[name for name in FRESH_NAMES if first[name] != cold[name]]}"
            )
        publish(first_directory)
    finally:
        shutil.rmtree(first_root, ignore_errors=True)
        shutil.rmtree(second_root, ignore_errors=True)
        shutil.rmtree(cold_root, ignore_errors=True)

    write_metadata(first, second, cold)
    remove_caches()
    print(
        json.dumps(
            {
                "scientific_stage": "PASS",
                "fresh_double_run": "PASS",
                "cold_start": "PASS",
                "artifact_count": len(FRESH_NAMES),
                "aggregate_sha256": aggregate(first),
                "research_lock_sha256": file_hash(RESULTS / "research_lock.json"),
                "metadata_seal": "PENDING",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
