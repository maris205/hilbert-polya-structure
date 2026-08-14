#!/usr/bin/env python3
"""Canonical isolated double-run, integrity audit, and SHA freeze for SD-C32."""

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
EXPECTED_AGGREGATE = "b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]
GENERATED_NAMES = (
    "analysis.json",
    "analytic_ownership.json",
    "baseline.json",
    "baseline_subset_ledger.csv",
    "clone_certificate.json",
    "comparison_table.csv",
    "evaluation.json",
    "finite_control_subset_ledger.csv",
    "finite_controls.json",
    "free_monoid_control_ledger.csv",
    "free_monoid_controls.json",
    "marker_ownership_ledger.csv",
    "predicate_mask_ledger.csv",
    "predicate_masks.json",
    "sanity.json",
    "summary.json",
    "test_report.json",
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
    command("generate_results.py", "--output", str(destination))
    command("independent_evaluator.py", "--results", str(destination))
    command("run_tests.py", "--output", str(destination))
    command("analyze_results.py", "--results", str(destination))


def artifact_hashes(directory: Path) -> dict[str, str]:
    actual = tuple(sorted(path.name for path in directory.iterdir() if path.is_file()))
    if actual != GENERATED_NAMES:
        raise RuntimeError(f"expected {GENERATED_NAMES}, found {actual}")
    return {name: sha256(directory / name) for name in GENERATED_NAMES}


def aggregate_hash(hashes: dict[str, str]) -> str:
    lines = [f"{digest}  {name}" for name, digest in hashes.items()]
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def publish_generated(source: Path) -> None:
    clear_results()
    for name in GENERATED_NAMES:
        shutil.copy2(source / name, RESULTS / name)


def write_metadata(first: dict[str, str], second: dict[str, str]) -> dict[str, object]:
    aggregate = aggregate_hash(first)
    certificate = {
        "candidate_id": "SD-C32",
        "schema_version": "SD-C32-double-run-v1",
        "byte_identical": first == second,
        "artifact_count": len(first),
        "aggregate_sha256": aggregate,
        "expected_prototype_aggregate_sha256": EXPECTED_AGGREGATE,
        "prototype_aggregate_matches": aggregate == EXPECTED_AGGREGATE,
        "first_hashes": first,
        "second_hashes": second,
        "fresh_result_directories_each_run": True,
        "pythonhashseed": "0",
        "pythondontwritebytecode": "1",
        "runs": 2,
        "commands": [
            "generate_results.py --output FRESH_RESULTS",
            "independent_evaluator.py --results FRESH_RESULTS",
            "run_tests.py --output FRESH_RESULTS",
            "analyze_results.py --results FRESH_RESULTS",
        ],
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    write_json(RESULTS / "double_run_certificate.json", certificate)
    write_json(
        RESULTS / "environment_lock.json",
        {
            "candidate_id": "SD-C32",
            "schema_version": "SD-C32-environment-v1",
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "arithmetic": "fractions.Fraction and exact incidence matrices",
            "external_dependencies_for_experiment_core": [],
            "authority_audit_dependencies": ["PyYAML"],
            "random_seeds": [29031, 29032, 30012, 30018, 30030, 30331, 31012, 31018, 31030],
            "timestamps_in_results": False,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "run_parameters.json",
        {
            "candidate_id": "SD-C32",
            "schema_version": "SD-C32-parameters-v1",
            "eta": 2,
            "integer_active_cutoffs": [12, 18, 30],
            "generic_dag_seed": 29031,
            "random_inventory_seed": 29032,
            "subset_arities": [2, 3],
            "predicate_masks": list(range(1, 32)),
            "free_commutative_ranks": [2, 3, 4, 5, 6],
            "exponent_caps": [1, 2, 3],
            "main_theorem_u": 1,
            "inherited_regularization_order": 3,
            "route_tuple": ROUTE_TUPLE,
            "overall_status": "REJECTED_AS_RH_COMPLETION",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "source_oracle_certificate.json",
        {
            "candidate_id": "SD-C32",
            "schema_version": "SD-C32-source-oracle-v1",
            "candidate_atoms_from_bottom_covers": True,
            "numeric_marks_select_atoms": False,
            "prime_table_used_in_candidate": False,
            "forbidden_candidate_calls": [],
            "formal_integer_factorization_use": "squarefree radical serialization only; never source-atom selection",
            "candidate_evaluator_separated": True,
            "candidate_core_sha256": sha256(CODE / "coherence_core.py"),
            "independent_evaluator_sha256": sha256(CODE / "independent_evaluator.py"),
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        RESULTS / "research_lock.json",
        {
            "candidate_id": "SD-C32",
            "schema_version": "SD-C32-research-lock-v1",
            "research_package_sha256": "98b58fd77ac6bd3fd7aa5c1f662d2203a34fa2891c631fad36ed8c9a19f45b1d",
            "prototype_ledger_sha256": "a7df78b607500c687981e731764ca0c7adc21489c36d4be29ffa36a802b46472",
            "prototype_preregistration_sha256": "dfb1ec09afe4077ba354830c45bb9b4158720d088c58b500eecee892b0137662",
            "prototype_report_sha256": "9d107b3919bd327f4c56f4f7577a49f8d8d4630baba9b83ad756ae2977b61e8a",
            "prototype_double_run_aggregate_sha256": EXPECTED_AGGREGATE,
            "claim_boundary": "finite certificates illustrate but do not numerically prove the infinite natural-isomorphism theorem",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    return certificate


def main() -> int:
    remove_caches()
    with tempfile.TemporaryDirectory(prefix="sdc32-run-a-") as first_root, tempfile.TemporaryDirectory(prefix="sdc32-run-b-") as second_root:
        first_directory = Path(first_root) / "results"
        second_directory = Path(second_root) / "results"
        build(first_directory)
        build(second_directory)
        first = artifact_hashes(first_directory)
        second = artifact_hashes(second_directory)
        if first != second:
            differing = [name for name in GENERATED_NAMES if first[name] != second[name]]
            raise RuntimeError(f"fresh runs are not byte-identical: {differing}")
        publish_generated(first_directory)

    certificate = write_metadata(first, second)
    if certificate["aggregate_sha256"] != EXPECTED_AGGREGATE:
        raise RuntimeError("authority fresh-run aggregate differs from frozen prototype")
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
