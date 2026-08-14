#!/usr/bin/env python3
"""Canonical sanity, double-run, integrity audit, and SHA freeze for SD-C34."""

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
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]
PROTOTYPE_EXACT_HASHES = {
    "cross_modulus_diamonds.json": "b1c1b0d777d169724d99257cfe87063bdf537367a747ca156321088f8f194ab3",
    "matched_clone.csv": "b2dc8ee8caef54073ba6204c628798fef0904d4993dee8b0416994128e662371",
    "modulus_census.csv": "864eae41a44deda389b3f5b08ff2b139d1e8a94b18468b7312ddb9c5424ce7b3",
    "random_relation_controls.csv": "1db0563c78b665193ea2dcfd001fc08c2562389cb11c8f3d39e45d060d0cc40b",
    "summary.json": "a8d2f151e523eb064ac50ac743089209270d55669fa19cb3220b1f2f14809073",
    "test_report.json": "cd73003539313186b8c2c6f080d2bd4997dc3f5241a468ec6eee7c7a5d9d6074",
}
FRESH_NAMES = tuple(
    sorted(
        (
            "analysis.json",
            "bare_ufd_control.json",
            "candidate_census.csv",
            "candidate_diamonds.json",
            "cross_modulus_diamonds.json",
            "evaluation.json",
            "fredholm_ownership.json",
            "matched_clone.csv",
            "modulus_census.csv",
            "random_relation_controls.csv",
            "source_oracle_certificate.json",
            "static_selector_firewall.csv",
            "stratum_controls.csv",
            "summary.json",
            "test_report.json",
            "trace_class_diagnostics.csv",
        )
    )
)
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


def sanity() -> None:
    with tempfile.TemporaryDirectory(prefix="sdc34-sanity-") as temporary:
        destination = Path(temporary) / "results"
        destination.mkdir()
        command(
            "generate_results.py",
            "--output",
            str(destination),
            "--cutoff",
            "12",
            "--trace-order",
            "4",
            "--random-trials",
            "4",
        )
        command(
            "independent_evaluator.py",
            "--results",
            str(destination),
            "--cutoff",
            "12",
            "--trace-order",
            "4",
            "--random-trials",
            "4",
        )
        evaluation = json.loads((destination / "evaluation.json").read_text(encoding="utf-8"))
        if evaluation.get("all_pass") is not True or evaluation.get("failure_count") != 0:
            raise RuntimeError("sanity evaluator failed")


def build(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    command(
        "generate_results.py",
        "--output",
        str(destination),
        "--cutoff",
        "192",
        "--trace-order",
        "8",
        "--random-trials",
        "48",
    )
    command(
        "independent_evaluator.py",
        "--results",
        str(destination),
        "--cutoff",
        "192",
        "--trace-order",
        "8",
        "--random-trials",
        "48",
    )
    command("analyze_results.py", "--results", str(destination))
    command("run_tests.py", "--results", str(destination))


def artifact_hashes(directory: Path) -> dict[str, str]:
    actual = tuple(sorted(path.name for path in directory.iterdir() if path.is_file()))
    if actual != FRESH_NAMES:
        raise RuntimeError(f"expected {FRESH_NAMES}, found {actual}")
    return {name: sha256(directory / name) for name in FRESH_NAMES}


def aggregate(hashes: dict[str, str]) -> str:
    lines = [f"{digest}  {name}" for name, digest in hashes.items()]
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def publish(source: Path) -> None:
    clear_results()
    for name in FRESH_NAMES:
        shutil.copy2(source / name, RESULTS / name)


def source_oracle_semantic_equivalence() -> bool:
    authority = json.loads((RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8"))
    prototype = json.loads(
        Path("/tmp/paper32_residue_groupoid_prototype/results_a/source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    compared = (
        "candidate_core",
        "candidate_core_sha256",
        "forbidden_patterns",
        "forbidden_hits",
        "imports",
        "pass",
    )
    return all(authority.get(key) == prototype.get(key) for key in compared)


def write_metadata(first: dict[str, str], second: dict[str, str]) -> dict[str, object]:
    fresh_aggregate = aggregate(first)
    double = {
        "candidate_id": "SD-C34",
        "schema_version": "SD-C34-double-run-v1",
        "byte_identical": first == second,
        "artifact_count": len(first),
        "aggregate_sha256": fresh_aggregate,
        "first_hashes": first,
        "second_hashes": second,
        "fresh_result_directories_each_run": True,
        "sanity_first_passed": True,
        "pythonhashseed": "0",
        "pythondontwritebytecode": "1",
        "runs": 2,
        "commands": [
            "generate_results.py --output FRESH_RESULTS --cutoff 192 --trace-order 8 --random-trials 48",
            "independent_evaluator.py --results FRESH_RESULTS --cutoff 192 --trace-order 8 --random-trials 48",
            "analyze_results.py --results FRESH_RESULTS",
            "run_tests.py --results FRESH_RESULTS",
        ],
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    write_json(RESULTS / "double_run_certificate.json", double)
    write_json(
        RESULTS / "environment_lock.json",
        {
            "candidate_id": "SD-C34",
            "schema_version": "SD-C34-environment-v1",
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
            "candidate_id": "SD-C34",
            "schema_version": "SD-C34-parameters-v1",
            "cutoff": 192,
            "trace_order": 8,
            "random_trials": 48,
            "random_seed_family": "320000+trial",
            "matched_clone_seed_family": "1000003+n",
            "cross_multipliers": [2, 3],
            "analytic_sigmas": [3, 4],
            "analytic_cutoffs": [16, 32, 64, 128, 192],
            "route_tuple": ROUTE_TUPLE,
            "overall": "ROUTE_A_REJECTED",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "research_lock.json",
        {
            "candidate_id": "SD-C34",
            "schema_version": "SD-C34-research-lock-v1",
            "research_package_sha256": "b34dd0489fae5080c683bedcaed6ddcc56025ddad6854da6e786c50c36fa61fb",
            "derivation_package_sha256": "a4423a4f742d695be704f715e77c192d53b5b30a26d5e9db3629ad68467cfe32",
            "proof_package_sha256": "d50434c323af93df3fae848d730f27081a02d983d4f6ca36f680f6bd96a9633c",
            "prototype_core_sha256": "e7ad9ff5f515973d4a0d9a991be912961f2b7492dcac7ecf0006bf490c6179cf",
            "prototype_runner_sha256": "cb6b128b9b3ace9cd39cf11ffe4ff02ac077d2bc923470bb61dd41580877616a",
            "prototype_payload_ledger_sha256": "f7c2e0f1c1be4bdce325515feb83a80bebfaf36e5785c39b31bcb12d9481d5e6",
            "claim_boundary": "finite artifacts certify implementation and controls; infinite theorems have independent proofs",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    actual_exact = {name: first[name] for name in sorted(PROTOTYPE_EXACT_HASHES)}
    write_json(
        RESULTS / "prototype_equivalence.json",
        {
            "candidate_id": "SD-C34",
            "schema_version": "SD-C34-prototype-equivalence-v1",
            "prototype_payload_ledger_sha256": "f7c2e0f1c1be4bdce325515feb83a80bebfaf36e5785c39b31bcb12d9481d5e6",
            "byte_identical_payloads": len(PROTOTYPE_EXACT_HASHES),
            "expected_hashes": PROTOTYPE_EXACT_HASHES,
            "authority_hashes": actual_exact,
            "all_six_byte_identical": actual_exact == PROTOTYPE_EXACT_HASHES,
            "source_oracle_semantic_equivalence": source_oracle_semantic_equivalence(),
            "source_oracle_note_changed_for_physical_evaluator_name": True,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "artifact_inventory.json",
        {
            "candidate_id": "SD-C34",
            "schema_version": "SD-C34-inventory-v1",
            "fresh_artifact_count": len(FRESH_NAMES),
            "fresh_artifacts": list(FRESH_NAMES),
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
    sanity()
    with tempfile.TemporaryDirectory(prefix="sdc34-run-a-") as first_root, tempfile.TemporaryDirectory(prefix="sdc34-run-b-") as second_root:
        first_directory = Path(first_root) / "results"
        second_directory = Path(second_root) / "results"
        build(first_directory)
        build(second_directory)
        first = artifact_hashes(first_directory)
        second = artifact_hashes(second_directory)
        if first != second:
            differing = [name for name in FRESH_NAMES if first[name] != second[name]]
            raise RuntimeError(f"fresh runs are not byte-identical: {differing}")
        actual_exact = {name: first[name] for name in sorted(PROTOTYPE_EXACT_HASHES)}
        if actual_exact != PROTOTYPE_EXACT_HASHES:
            differing = [name for name in sorted(PROTOTYPE_EXACT_HASHES) if actual_exact[name] != PROTOTYPE_EXACT_HASHES[name]]
            raise RuntimeError(f"authority payloads differ from frozen prototype: {differing}")
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
