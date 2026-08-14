#!/usr/bin/env python3
"""Canonical isolated double-run, integrity audit, and SHA freeze for SD-C33."""

from __future__ import annotations

import hashlib
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
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_PASS_ANALYTIC",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
LEGACY_HASHES = {
    "bare_ufd_addition_failure.csv": "22bd70d79b3ce52771a6935907dae681e12a0f14d5eee9f2fa10b3dd33c7dd0f",
    "composite_controls.csv": "7fdcba924a49c71e8ec28e71384a01c06609183d790c2751dd5cca4d025f74f8",
    "entropy_budget_dilution.csv": "8b126af8f1c0f2377cb65053beb761d16b2b3a3f729c20e83ab101133a173791",
    "fermat_pseudoprime_controls.csv": "aeeb98694232f4079a8aac1a4051efbe8d306a6e96bc3487621c2ea5f728fc7d",
    "formal_trace_ledger.csv": "5306ca5a179d5e21de04b5480f563c2867fbca1e36b9a8fa387e1db53fb9640a",
    "marker_change_certificate.json": "a69946a9d73d14f1a3b76237c361adc2bc7170d7854db25a5e146e44a99925ba",
    "matched_semiring_clone.csv": "43cc29b0aa544352d35bfda65fccffa7d6fffebbbc0c47864eeb9ee7102712ce",
    "random_operation_controls.json": "933cc06ae774dd784c59e70bb38507b166f4b1a431231e2199e952517e47a2b9",
    "semiring_controls.json": "caa026417b116d90cab4f220e3a787cdf73b93de5e56ba0ba9e2f1459332d35f",
    "source_oracle_certificate.json": "f82bb6027b88c81d0c164475518033c5026392bb2aa20ea5047269c0514a89e4",
    "summary.json": "3d0a338f4b765cf35be6dccd963c22abdac50f1d5d51d20b925f3cd108b24646",
    "test_report.json": "6a99807590a6c2715afb4699552f6e9e9bcf42890df9962e7a98ba06f5693ead",
    "universal_wrapper_controls.json": "fa375fd1e3834d7b5d6317c6061552b265f570362327dc79cd6939710d70993a",
    "wilson_ledger.csv": "cae463291257e3fc244c1d99c8fdf3b1d0199c0be46d45067a6401c3f548fcdd",
}
PROTOTYPE_ORIGINAL_AGGREGATE = "100490afb62c6302329db814a856782d20cf986c608a365b9a72fb848fc5a0cd"
LEGACY_AGGREGATE = "36792d57cc2d58c1b52df47fdf757c86f6e10ed5eae685423259d0d9739a0dee"
FRESH_NAMES = tuple(sorted((*LEGACY_HASHES, "analysis.json", "evaluation.json")))
EXPECTED_RESULT_NAMES = tuple(
    sorted(
        (
            *FRESH_NAMES,
            "artifact_inventory.json",
            "double_run_certificate.json",
            "environment_lock.json",
            "integrity_audit.json",
            "prototype_equivalence.json",
            "research_lock.json",
            "run_parameters.json",
        )
    )
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def remove_caches() -> None:
    for path in sorted(ROOT.rglob("*"), reverse=True):
        if path.is_dir() and path.name in {"__pycache__", ".pytest_cache"}:
            shutil.rmtree(path)


def clear_results() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    for path in RESULTS.iterdir():
        if path.is_file() or path.is_symlink():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)


def command(script: str, *arguments: str) -> None:
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(
        [sys.executable, "-B", str(CODE / script), *arguments],
        cwd=ROOT,
        env=environment,
        check=True,
    )


def build(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    command("generate_results.py", "--output", str(destination), "--cutoff", "4096")
    command("independent_evaluator.py", "--results", str(destination))
    command("run_tests.py", "--results", str(destination))
    command("analyze_results.py", "--results", str(destination))


def artifact_hashes(directory: Path) -> dict[str, str]:
    actual = tuple(sorted(path.name for path in directory.iterdir() if path.is_file()))
    if actual != FRESH_NAMES:
        raise RuntimeError(f"expected {FRESH_NAMES}, found {actual}")
    return {name: sha256(directory / name) for name in FRESH_NAMES}


def aggregate(hashes: dict[str, str]) -> str:
    lines = [f"{digest}  {name}" for name, digest in hashes.items()]
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def legacy_aggregate(hashes: dict[str, str]) -> str:
    legacy = {name: hashes[name] for name in sorted(LEGACY_HASHES)}
    return aggregate(legacy)


def publish(source: Path) -> None:
    clear_results()
    for name in FRESH_NAMES:
        shutil.copy2(source / name, RESULTS / name)


def write_metadata(first: dict[str, str], second: dict[str, str]) -> dict[str, object]:
    fresh_aggregate = aggregate(first)
    double = {
        "candidate_id": "SD-C33",
        "schema_version": "SD-C33-double-run-v1",
        "byte_identical": first == second,
        "artifact_count": len(first),
        "aggregate_sha256": fresh_aggregate,
        "first_hashes": first,
        "second_hashes": second,
        "fresh_result_directories_each_run": True,
        "pythonhashseed": "0",
        "pythondontwritebytecode": "1",
        "runs": 2,
        "commands": [
            "generate_results.py --output FRESH_RESULTS --cutoff 4096",
            "independent_evaluator.py --results FRESH_RESULTS",
            "run_tests.py --results FRESH_RESULTS",
            "analyze_results.py --results FRESH_RESULTS",
        ],
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    write_json(RESULTS / "double_run_certificate.json", double)
    write_json(
        RESULTS / "environment_lock.json",
        {
            "candidate_id": "SD-C33",
            "schema_version": "SD-C33-environment-v1",
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "experiment_core_dependencies": [],
            "authority_audit_dependencies": ["PyYAML"],
            "timestamps_in_results": False,
            "pythonhashseed": "0",
            "pythondontwritebytecode": "1",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "run_parameters.json",
        {
            "candidate_id": "SD-C33",
            "schema_version": "SD-C33-parameters-v1",
            "cutoff": 4096,
            "marker_cutoff": 31,
            "formal_trace_s": 2,
            "operation_table_seed": 31033,
            "random_operation_table_pairs": 32,
            "bare_addition_grid": "1..12 squared",
            "matched_clone_grid": "0..12 squared",
            "dilution_sigma": [1, 2, 3],
            "formal_trace_powers": [1, 16],
            "universal_support_cutoff": 128,
            "route_tuple": ROUTE_TUPLE,
            "overall": "ROUTE_A_REJECTED",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "research_lock.json",
        {
            "candidate_id": "SD-C33",
            "schema_version": "SD-C33-research-lock-v1",
            "research_package_sha256": "d531e13e2c94972b4c38b7df0a9b070da7f04eb80d1f533b433edf16b0937a68",
            "prototype_source_sha256": "01005ee0f7d10a97de9978f6f512596f6146d21abe0302bab61d459892fe86a5",
            "prototype_ledger_sha256": PROTOTYPE_ORIGINAL_AGGREGATE,
            "prototype_aggregate_payload": PROTOTYPE_ORIGINAL_AGGREGATE,
            "authority_LF_canonical_legacy_aggregate": LEGACY_AGGREGATE,
            "claim_boundary": "finite exact artifacts certify implementation; infinite theorems have independent proofs",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    actual_legacy = {name: first[name] for name in sorted(LEGACY_HASHES)}
    write_json(
        RESULTS / "prototype_equivalence.json",
        {
            "candidate_id": "SD-C33",
            "schema_version": "SD-C33-prototype-equivalence-v2",
            "legacy_artifact_count": len(actual_legacy),
            "expected_authority_LF_hashes": LEGACY_HASHES,
            "authority_hashes": actual_legacy,
            "all_authority_LF_hashes_equal": actual_legacy == LEGACY_HASHES,
            "authority_legacy_aggregate_sha256": legacy_aggregate(first),
            "expected_authority_LF_aggregate_sha256": LEGACY_AGGREGATE,
            "authority_LF_aggregate_equal": legacy_aggregate(first) == LEGACY_AGGREGATE,
            "original_prototype_aggregate_sha256": PROTOTYPE_ORIGINAL_AGGREGATE,
            "normalization": "JSON byte-identical; CSV content identical after the sole CRLF-to-LF canonicalization",
            "semantic_equivalence": True,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "artifact_inventory.json",
        {
            "candidate_id": "SD-C33",
            "schema_version": "SD-C33-inventory-v1",
            "fresh_artifact_count": len(FRESH_NAMES),
            "fresh_artifacts": list(FRESH_NAMES),
            "legacy_artifact_count": len(LEGACY_HASHES),
            "legacy_artifacts": sorted(LEGACY_HASHES),
            "expected_result_artifact_count_excluding_sha": len(EXPECTED_RESULT_NAMES),
            "expected_result_artifacts_excluding_sha": list(EXPECTED_RESULT_NAMES),
            "expected_code_result_sha_entries": 31,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    return double


def main() -> int:
    remove_caches()
    with tempfile.TemporaryDirectory(prefix="sdc33-run-a-") as first_root, tempfile.TemporaryDirectory(prefix="sdc33-run-b-") as second_root:
        first_directory = Path(first_root) / "results"
        second_directory = Path(second_root) / "results"
        build(first_directory)
        build(second_directory)
        first = artifact_hashes(first_directory)
        second = artifact_hashes(second_directory)
        if first != second:
            differing = [name for name in FRESH_NAMES if first[name] != second[name]]
            raise RuntimeError(f"fresh runs are not byte-identical: {differing}")
        if {name: first[name] for name in sorted(LEGACY_HASHES)} != LEGACY_HASHES:
            raise RuntimeError("authority legacy artifacts differ from frozen prototype")
        if legacy_aggregate(first) != LEGACY_AGGREGATE:
            raise RuntimeError("authority legacy aggregate differs from frozen prototype")
        publish(first_directory)

    certificate = write_metadata(first, second)
    remove_caches()
    command("audit_artifact_integrity.py")
    command("freeze_artifacts.py")
    command("freeze_artifacts.py")
    command("freeze_artifacts.py", "--check")
    remove_caches()
    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
