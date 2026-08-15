#!/usr/bin/env python3
"""Run fresh A/B plus cache-free cold-start C pipelines for SD-C37."""

from __future__ import annotations

from hashlib import sha256
from importlib.metadata import version as package_version
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
EXPECTED_ROOT_NAME = "35-affine-semigroup-object-firewall"
FRESH_NAMES = tuple(
    sorted(
        {
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
        }
    )
)
RESEARCH_DOCUMENTS = (
    ("root_preregistration_sha256", "PREREGISTRATION.md"),
    ("source_lock_sha256", "SOURCE_LOCK.md"),
    ("derivation_package_sha256", "DERIVATION_PACKAGE.md"),
    ("proof_package_sha256", "PROOF_PACKAGE.md"),
    ("literature_audit_sha256", "LITERATURE_AUDIT.md"),
    ("authority_preregistration_sha256", "experiments/PREREGISTRATION.md"),
    ("experiment_plan_sha256", "experiments/EXPERIMENT_PLAN.md"),
)
MATHEMATICAL_PACKAGE = Path("/tmp/paper35_math_package.md")
MATHEMATICAL_SHA256 = "e04f11dbb0ced5ad55a878cc4364c8a8d1ca33cb4cbb919b8e6b2149b83ebd25"
LITERATURE_PACKAGE = Path("/tmp/paper35_literature_audit.md")
LITERATURE_SHA256 = "f2a11df03f72a0277205a805f077996d17ef2d51b235ad993c1619ac3a1d2653"
PROTOTYPE_ROOT = Path("/tmp/paper35_exact_prototype")


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
        if path.is_dir() and path.name in {
            "__pycache__",
            ".pytest_cache",
            ".mypy_cache",
            ".ruff_cache",
        }:
            shutil.rmtree(path)


def verify_external_locks() -> dict[str, object]:
    rows = [
        {
            "name": "mathematical_package",
            "path": str(MATHEMATICAL_PACKAGE),
            "required_sha256": MATHEMATICAL_SHA256,
            "actual_sha256": file_hash(MATHEMATICAL_PACKAGE)
            if MATHEMATICAL_PACKAGE.is_file()
            else None,
        },
        {
            "name": "literature_package",
            "path": str(LITERATURE_PACKAGE),
            "required_sha256": LITERATURE_SHA256,
            "actual_sha256": file_hash(LITERATURE_PACKAGE)
            if LITERATURE_PACKAGE.is_file()
            else None,
        },
    ]
    for row in rows:
        row["match"] = row["actual_sha256"] == row["required_sha256"]
    return {
        "schema_version": "SD-C37-external-lock-verification-v1",
        "locks": rows,
        "status": "PASS" if all(row["match"] for row in rows) else "FAIL",
    }


def build(destination: Path) -> None:
    command("generate_artifacts.py", "--output", str(destination))
    command(
        "independent_evaluator.py",
        "--source",
        str(destination),
        "--output",
        str(destination),
        "--code-dir",
        str(CODE),
    )
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
    if ROOT.name != EXPECTED_ROOT_NAME or RESULTS.resolve() != (ROOT / "results").resolve():
        raise RuntimeError("refusing to clear an unexpected results directory")
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
        {"path": relative, "pointer_field": field, "sha256": file_hash(ROOT / relative)}
        for field, relative in RESEARCH_DOCUMENTS
    ]
    pointers = {record["pointer_field"]: record["sha256"] for record in records}
    external = verify_external_locks()
    return {
        "schema_version": "SD-C37-research-lock-v1",
        "research_document_count": len(records),
        "research_documents": records,
        **pointers,
        "authority_plan_path": "experiments/EXPERIMENT_PLAN.md",
        "authority_preregistration_path": "experiments/PREREGISTRATION.md",
        "authority_plan_frozen_before_results": True,
        "authority_preregistration_frozen_before_results": True,
        "root_preregistration_frozen_before_results": True,
        "external_locks": external["locks"],
        "external_lock_status": external["status"],
        "mathematical_package_sha256": MATHEMATICAL_SHA256,
        "literature_package_sha256": LITERATURE_SHA256,
        "target_zero_data": "not_applicable; target_zero_data_forbidden_and_unused",
        "route_b_invocation_allowed": False,
    }


def prototype_bridge_payload() -> dict[str, object]:
    double_path = PROTOTYPE_ROOT / "results" / "double_run_certificate.json"
    ledger_path = PROTOTYPE_ROOT / "results" / "SHA_LEDGER.json"
    integrity_path = PROTOTYPE_ROOT / "results" / "integrity_audit.json"
    double = json.loads(double_path.read_text(encoding="utf-8"))
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    integrity = json.loads(integrity_path.read_text(encoding="utf-8"))
    bridge_files = (
        "code/source_core.py",
        "code/generate_source.py",
        "code/independent_evaluator.py",
        "code/run_tests.py",
        "code/analyze_results.py",
        "PREREGISTRATION.md",
    )
    rows = [
        {"path": relative, "sha256": file_hash(PROTOTYPE_ROOT / relative)}
        for relative in bridge_files
    ]
    status = (
        "PASS"
        if double.get("status") == "PASS"
        and double.get("byte_identical") is True
        and integrity.get("status") == "PASS"
        and ledger.get("status") == "PASS"
        else "FAIL"
    )
    return {
        "schema_version": "SD-C37-prototype-bridge-v1",
        "prototype_root": str(PROTOTYPE_ROOT),
        "prototype_files": rows,
        "prototype_scientific_aggregate_sha256": double["aggregate_sha256"],
        "prototype_ledger_sha256": ledger["ledger_sha256"],
        "prototype_double_run_status": double["status"],
        "prototype_integrity_status": integrity["status"],
        "authority_recomputes_all_scientific_outputs": True,
        "authority_corrections": [
            "height changed from auxiliary b+k to source-locked b+r^k",
            "primary U/V weights changed from rational diagnostics to unweighted A_plus=S+T",
            "Route A3/A4 changed from prototype boundary shorthand to strict authority FAIL enums",
        ],
        "prototype_outputs_copied_as_authority_results": False,
        "status": status,
    }


def write_metadata(first: dict[str, str], second: dict[str, str], cold: dict[str, str]) -> None:
    byte_identical = first == second and aggregate(first) == aggregate(second)
    cold_identical = first == cold and aggregate(first) == aggregate(cold)
    research = research_lock_payload()
    bridge = prototype_bridge_payload()
    write_json(RESULTS / "research_lock.json", research)
    write_json(RESULTS / "prototype_bridge.json", bridge)
    research_sha256 = file_hash(RESULTS / "research_lock.json")
    bridge_sha256 = file_hash(RESULTS / "prototype_bridge.json")
    write_json(
        RESULTS / "double_run_certificate.json",
        {
            "schema_version": "SD-C37-double-run-v1",
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
                "independent_evaluator.py --source FRESH_RESULTS --output FRESH_RESULTS --code-dir FROZEN_CODE",
                "run_tests.py --results FRESH_RESULTS",
                "analyze_results.py --results FRESH_RESULTS",
            ],
            "pythonhashseed": "0",
            "pythondontwritebytecode": "1",
            "research_lock_sha256": research_sha256,
            "prototype_bridge_sha256": bridge_sha256,
            "status": "PASS" if byte_identical else "FAIL",
        },
    )
    write_json(
        RESULTS / "cold_start_certificate.json",
        {
            "schema_version": "SD-C37-cold-start-v1",
            "cold_start_directory_initially_absent": True,
            "cold_start_cache_free": True,
            "cold_start_artifact_count": len(FRESH_NAMES),
            "reference_aggregate_sha256": aggregate(first),
            "cold_start_aggregate_sha256": aggregate(cold),
            "hashes": cold,
            "research_lock_sha256": research_sha256,
            "prototype_bridge_sha256": bridge_sha256,
            "mismatched_paths": sorted(name for name in FRESH_NAMES if first[name] != cold[name]),
            "byte_identical_to_published_science": cold_identical,
            "status": "PASS" if cold_identical else "FAIL",
        },
    )
    write_json(
        RESULTS / "environment_lock.json",
        {
            "schema_version": "SD-C37-environment-v1",
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "scientific_dependencies": [],
            "seal_audit_dependencies": {"PyYAML": package_version("PyYAML")},
            "cpu_only": True,
            "network_used": False,
            "external_data_used": False,
            "target_zero_data_used": "not_applicable; target_zero_data_forbidden_and_unused",
            "result_timestamps": False,
            "pythonhashseed": "0",
            "pythondontwritebytecode": "1",
        },
    )
    write_json(
        RESULTS / "artifact_inventory.json",
        {
            "schema_version": "SD-C37-artifact-inventory-bootstrap-v1",
            "fresh_artifact_count": len(FRESH_NAMES),
            "fresh_artifacts": list(FRESH_NAMES),
            "run_metadata_before_seal": [
                "artifact_inventory.json",
                "cold_start_certificate.json",
                "double_run_certificate.json",
                "environment_lock.json",
                "prototype_bridge.json",
                "research_lock.json",
            ],
            "expected_final_result_count": 34,
            "research_document_count": len(RESEARCH_DOCUMENTS),
            "research_lock_sha256": research_sha256,
            "prototype_bridge_sha256": bridge_sha256,
            "metadata_seal_pending": True,
        },
    )
    if research["external_lock_status"] != "PASS" or bridge["status"] != "PASS":
        raise RuntimeError("research or prototype bridge lock failed")
    if not byte_identical or not cold_identical:
        raise RuntimeError("fresh or cold-start runs are not byte-identical")


def main() -> int:
    if ROOT.name != EXPECTED_ROOT_NAME:
        raise SystemExit(f"unexpected authority root: {ROOT}")
    external = verify_external_locks()
    if external["status"] != "PASS":
        raise SystemExit(json.dumps(external, sort_keys=True))
    remove_caches()
    first_root = Path(tempfile.mkdtemp(prefix="sdc37-run-a-", dir="/tmp"))
    second_root = Path(tempfile.mkdtemp(prefix="sdc37-run-b-", dir="/tmp"))
    cold_root = Path(tempfile.mkdtemp(prefix="sdc37-cold-c-", dir="/tmp"))
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
                "prototype_bridge_sha256": file_hash(RESULTS / "prototype_bridge.json"),
                "metadata_seal": "PENDING",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
