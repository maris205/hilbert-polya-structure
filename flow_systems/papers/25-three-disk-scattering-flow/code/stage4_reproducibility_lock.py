#!/usr/bin/env python3
"""Fail-closed validator for the Paper-25 Stage-4 reproducibility lock.

This validator is deliberately read-only.  It hashes the closed Round-2--8
inventory, checks the pinned runtime and command policy, preserves the Route-A
owner firewall, and can rebuild the Round-8 2,241-row replay twice in isolated
temporary directories.  It never refreshes repository artifacts.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import platform
import subprocess
import sys
import sysconfig
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCK_PATH = PROJECT_ROOT / "experiments/stage4_reproducibility_lock.json"
SCHEMA = "p25-stage4-reproducibility-lock/1.0"

ROUND_ARTIFACTS: dict[str, dict[str, list[str]]] = {
    "2": {
        "sources": ["code/round2_three_disk_ledger.py"],
        "tests": ["code/test_round2_three_disk_ledger.py"],
        "inputs": [],
        "outputs": [
            "results/three_disk_primitive_ledger_round2.csv",
            "results/three_disk_controls_round2.csv",
            "results/round2_metrics.json",
        ],
        "receipts": [
            "experiments/round2_receipt.json",
            "experiments/round2_validation.md",
        ],
        "reproduction_artifacts": [],
    },
    "3": {
        "sources": ["code/round3_return_map_validation.py"],
        "tests": ["code/test_round3_return_map_validation.py"],
        "inputs": ["results/three_disk_primitive_ledger_round2.csv"],
        "outputs": [
            "results/three_disk_return_map_validation_round3.csv",
            "results/round3_stability_metrics.json",
        ],
        "receipts": [
            "experiments/round3_receipt.json",
            "experiments/round3_validation.md",
        ],
        "reproduction_artifacts": [],
    },
    "4": {
        "sources": ["code/round4_conditioning_audit.py"],
        "tests": ["code/test_round4_conditioning_audit.py"],
        "inputs": [
            "results/three_disk_return_map_validation_round3.csv",
            "code/round3_return_map_validation.py",
        ],
        "outputs": [
            "results/round4_conditioning_by_length.csv",
            "results/round4_fallback_audit.csv",
            "results/round4_conditioning_metrics.json",
        ],
        "receipts": ["experiments/round4_reproducibility_receipt.json"],
        "reproduction_artifacts": ["experiments/reproduce_round4.sh"],
    },
    "5": {
        "sources": ["code/round5_universal_half_density.py"],
        "tests": ["code/test_round5_universal_half_density.py"],
        "inputs": [
            "results/three_disk_primitive_ledger_round2.csv",
            "results/three_disk_return_map_validation_round3.csv",
        ],
        "outputs": [
            "results/round5_universal_half_density_ledger.csv",
            "results/round5_universal_half_density_by_repetition.csv",
            "results/round5_universal_half_density_metrics.json",
        ],
        "receipts": ["experiments/round5_reproducibility_receipt.json"],
        "reproduction_artifacts": ["experiments/reproduce_round5.sh"],
    },
    "6": {
        "sources": ["code/round6_symbolic_zeta_calibrator.py"],
        "tests": ["code/test_round6_symbolic_zeta_calibrator.py"],
        "inputs": [
            "experiments/round6_symbolic_zeta_freeze.json",
            "results/three_disk_primitive_ledger_round2.csv",
        ],
        "outputs": [
            "results/round6_symbolic_owner_counts.csv",
            "results/round6_symbolic_zeta_prefix.csv",
            "results/round6_symbolic_zeta_metrics.json",
        ],
        "receipts": [
            "experiments/round6_receipt.json",
            "experiments/round6_validation.md",
        ],
        "reproduction_artifacts": ["experiments/reproduce_round6.sh"],
    },
    "7": {
        "sources": ["code/round7_q_symbolic_family.py"],
        "tests": ["code/test_round7_q_symbolic_family.py"],
        "inputs": ["experiments/round7_q_symbolic_family_freeze.json"],
        "outputs": [
            "results/round7_q_symbolic_counts.csv",
            "results/round7_q_symbolic_prefix.csv",
            "results/round7_q_symbolic_summary.json",
        ],
        "receipts": [
            "experiments/round7_reproducibility_receipt.json",
            "experiments/round7_validation.md",
        ],
        "reproduction_artifacts": ["experiments/reproduce_round7.sh"],
    },
    "8": {
        "sources": ["code/round8_roof_nontransfer.py"],
        "tests": ["code/test_round8_roof_nontransfer.py"],
        "inputs": [
            "experiments/round8_roof_nontransfer_freeze.json",
            "results/three_disk_primitive_ledger_round2.csv",
        ],
        "outputs": [
            "results/round8_exact_roof_witnesses.csv",
            "results/round8_physical_roof_replay.csv",
            "results/round8_roof_nontransfer_summary.json",
        ],
        "receipts": [
            "experiments/round8_reproducibility_receipt.json",
            "experiments/round8_validation.md",
        ],
        "reproduction_artifacts": ["experiments/reproduce_round8.sh"],
    },
}

AUXILIARY_ARTIFACTS = {
    "paper/references.bib",
    "paper/stage2_manuscript_audit.md",
    "notes/stage2_5_integrity_report.json",
    "notes/stage2_5_integrity_report.md",
    "code/README.md",
    "experiments/README.md",
    "results/README.md",
    "notes/stage3_revision_roadmap.json",
    "notes/stage4_author_adjudication.json",
    "notes/stage4_claim_surface_manifest.json",
    "notes/stage4_writer_handoff.json",
    "code/stage4_reproducibility_lock.py",
    "code/test_stage4_reproducibility_lock.py",
    "experiments/reproduce_stage4.sh",
}

EXPECTED_COMMANDS = [
    {
        "id": "round2_legacy_verify",
        "round": 2,
        "command": "python3 code/round2_three_disk_ledger.py --verify-existing",
        "canonical_write_risk": True,
        "stage4_execution": "FORBIDDEN_METADATA_WRITE",
    },
    {
        "id": "round3_legacy_verify",
        "round": 3,
        "command": "python3 code/round3_return_map_validation.py --verify-existing",
        "canonical_write_risk": True,
        "stage4_execution": "FORBIDDEN_METADATA_WRITE",
    },
    {
        "id": "round4_legacy_reproduce",
        "round": 4,
        "command": "bash experiments/reproduce_round4.sh",
        "canonical_write_risk": True,
        "stage4_execution": "FORBIDDEN_CANONICAL_REFRESH",
    },
    {
        "id": "round5_legacy_reproduce",
        "round": 5,
        "command": "bash experiments/reproduce_round5.sh",
        "canonical_write_risk": True,
        "stage4_execution": "FORBIDDEN_RECEIPT_WRITE",
    },
    {
        "id": "round6_verify",
        "round": 6,
        "command": "bash experiments/reproduce_round6.sh",
        "canonical_write_risk": False,
        "stage4_execution": "AUTHORIZED_READ_ONLY",
    },
    {
        "id": "round7_verify",
        "round": 7,
        "command": "bash experiments/reproduce_round7.sh verify",
        "canonical_write_risk": False,
        "stage4_execution": "AUTHORIZED_READ_ONLY",
    },
    {
        "id": "round8_verify",
        "round": 8,
        "command": "bash experiments/reproduce_round8.sh verify",
        "canonical_write_risk": False,
        "stage4_execution": "AUTHORIZED_READ_ONLY_EXECUTED",
    },
    {
        "id": "stage4_closed_replay",
        "round": "stage4_support",
        "command": "bash experiments/reproduce_stage4.sh",
        "canonical_write_risk": False,
        "stage4_execution": "AUTHORIZED_READ_ONLY",
    },
]

EXPECTED_BOUNDARIES = {
    "replay_evidentiary_role": "SOLVER_AND_REPRODUCIBILITY_VALIDATION_ONLY",
    "replay_is_additional_noncohomology_proof": False,
    "symbolic_calibrator_route_a_tuple": [
        "A0_FAIL",
        "A1_PASS_ANALYTIC",
        "A2_ANALYTIC_DETERMINANT",
        "A3_FAIL",
        "A4_FAIL",
    ],
    "tuple_owner": "UNIT_ROOF_SYMBOLIC_CALIBRATOR_ONLY",
    "physical_three_disk_route_tuple": "UNASSIGNED",
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "canonical_results_refresh_authorized": False,
}

EXPECTED_REPLAY = {
    "round": 8,
    "input_path": "results/three_disk_primitive_ledger_round2.csv",
    "input_sha256": "25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736",
    "physical_replay_rows": 2241,
    "owners_per_geometry": 747,
    "geometry_labels": ["29/5", "31/5", "6"],
    "matches_per_geometry": 3,
    "disagreements_per_geometry": 744,
    "witness_rows": 6,
    "core_sha256": "9a29d8894b1ac81f9588fe221375bddc671898b9b08b409b0fa5a1d5a42a9014",
    "output_sha256": {
        "results/round8_exact_roof_witnesses.csv": "53acd2d60db18909e36ad0ad7c1ee505874117d5fbb32eeda1fc374d15530ad5",
        "results/round8_physical_roof_replay.csv": "fa82c62ff34b8e674e78e37e800a5f31fdcbe3b986b37344a36719e30fa53e63",
        "results/round8_roof_nontransfer_summary.json": "39bb90334d57eee2e9fa3678cb5079b2d8f087d60c607a052955bb0303cd4295",
    },
}


class LockValidationError(RuntimeError):
    """Raised when any lock invariant fails."""

    def __init__(self, failures: list[str]):
        self.failures = failures
        super().__init__("; ".join(failures))


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def runtime_record() -> dict[str, Any]:
    import mpmath
    import numpy
    import scipy

    libc_name, libc_version = platform.libc_ver()
    return {
        "python": {
            "implementation": platform.python_implementation(),
            "version": platform.python_version(),
            "cache_tag": sys.implementation.cache_tag,
            "compiler": platform.python_compiler(),
            "soabi": sysconfig.get_config_var("SOABI"),
        },
        "packages": {
            "mpmath": mpmath.__version__,
            "numpy": numpy.__version__,
            "scipy": scipy.__version__,
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "libc": {"name": libc_name, "version": libc_version},
        },
    }


def expected_inventory_paths() -> set[str]:
    paths = set(AUXILIARY_ARTIFACTS)
    for groups in ROUND_ARTIFACTS.values():
        for entries in groups.values():
            paths.update(entries)
    return paths


def _is_safe_relative_path(text: str) -> bool:
    path = PurePosixPath(text)
    return bool(text) and not path.is_absolute() and ".." not in path.parts and path.as_posix() == text


def _environment_failures(expected: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    observed = runtime_record()
    if expected.get("runtime") != observed:
        failures.append(
            "runtime drift: expected "
            + json.dumps(expected.get("runtime"), sort_keys=True)
            + ", observed "
            + json.dumps(observed, sort_keys=True)
        )
    deterministic = expected.get("deterministic_process_environment")
    wanted = {
        "LC_ALL": "C",
        "TZ": "UTC",
        "PYTHONHASHSEED": "0",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if deterministic != wanted:
        failures.append("deterministic process environment declaration changed")
    for name, value in wanted.items():
        if os.environ.get(name) != value:
            failures.append(f"process environment {name} must equal {value!r}")
    return failures


def _validate_round8_replay(project_root: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="p25-stage4-round8-a-") as first_name, tempfile.TemporaryDirectory(
        prefix="p25-stage4-round8-b-"
    ) as second_name:
        roots = [Path(first_name), Path(second_name)]
        stdout_records: list[dict[str, Any]] = []
        for root in roots:
            completed = subprocess.run(
                [
                    sys.executable,
                    str(project_root / "code/round8_roof_nontransfer.py"),
                    "--output-root",
                    str(root),
                ],
                cwd=project_root,
                check=True,
                text=True,
                capture_output=True,
                env={
                    **os.environ,
                    "LC_ALL": "C",
                    "TZ": "UTC",
                    "PYTHONHASHSEED": "0",
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
            )
            stdout_records.append(json.loads(completed.stdout.strip()))

        generated_paths = sorted(EXPECTED_REPLAY["output_sha256"])
        for relative in generated_paths:
            first = (roots[0] / relative).read_bytes()
            second = (roots[1] / relative).read_bytes()
            canonical = (project_root / relative).read_bytes()
            if first != second:
                raise LockValidationError([f"Round-8 isolated replay differs between runs: {relative}"])
            if first != canonical:
                raise LockValidationError([f"Round-8 replay differs from canonical bytes: {relative}"])
            if sha256_bytes(first) != EXPECTED_REPLAY["output_sha256"][relative]:
                raise LockValidationError([f"Round-8 replay hash differs: {relative}"])

        summary = json.loads((roots[0] / "results/round8_roof_nontransfer_summary.json").read_text())
        expected_summary = {
            "physical_replay_rows": 2241,
            "witness_rows": 6,
            "physical_three_disk_route_tuple": "UNASSIGNED",
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "finite_replay_evidence_status": "NUMERICALLY_CERTIFIED",
        }
        observed_summary = {key: summary.get(key) for key in expected_summary}
        if observed_summary != expected_summary:
            raise LockValidationError(["Round-8 scientific summary changed"])
        geometry = summary.get("geometry_summaries", {})
        for label in EXPECTED_REPLAY["geometry_labels"]:
            row = geometry.get(label, {})
            if (
                row.get("frozen_owner_rows") != 747
                or row.get("rows_agreeing_with_period_two_scalar_clock") != 3
                or row.get("rows_disagreeing_with_period_two_scalar_clock") != 744
            ):
                raise LockValidationError([f"Round-8 geometry summary changed: {label}"])
        if any(record.get("core_sha256") != EXPECTED_REPLAY["core_sha256"] for record in stdout_records):
            raise LockValidationError(["Round-8 core digest changed"])
        return {
            "runs": 2,
            "byte_identical": True,
            "canonical_match": True,
            "core_sha256": EXPECTED_REPLAY["core_sha256"],
            "physical_replay_rows": summary["physical_replay_rows"],
            "witness_rows": summary["witness_rows"],
            "owners_per_geometry": 747,
            "matches_per_geometry": 3,
            "disagreements_per_geometry": 744,
            "evidentiary_role": "SOLVER_AND_REPRODUCIBILITY_VALIDATION_ONLY",
        }


def load_lock(path: Path = DEFAULT_LOCK_PATH) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise LockValidationError(["lock root must be an object"])
    return value


def validate_lock_payload(
    lock: dict[str, Any],
    *,
    project_root: Path = PROJECT_ROOT,
    check_environment: bool = True,
    replay_round8: bool = False,
) -> dict[str, Any]:
    failures: list[str] = []
    expected_top_level = {
        "schema",
        "paper",
        "created_utc",
        "classification",
        "authority",
        "environment",
        "bibliography",
        "rounds",
        "commands",
        "scientific_boundaries",
        "round8_replay_contract",
        "artifact_inventory",
        "inventory_contract",
    }
    if set(lock) != expected_top_level:
        failures.append("top-level fields differ from the closed schema")
    if lock.get("schema") != SCHEMA:
        failures.append("schema mismatch")
    if lock.get("paper") != 25:
        failures.append("paper mismatch")
    if lock.get("classification") != "STAGE4_REPRODUCIBILITY_SUPPORT_NOT_SCIENTIFIC_EVIDENCE":
        failures.append("classification mismatch")
    if lock.get("rounds") != ROUND_ARTIFACTS:
        failures.append("Round-2--8 role map changed")
    if lock.get("commands") != EXPECTED_COMMANDS:
        failures.append("reproduction command registry changed")
    if lock.get("scientific_boundaries") != EXPECTED_BOUNDARIES:
        failures.append("scientific or Route boundary changed")
    if lock.get("round8_replay_contract") != EXPECTED_REPLAY:
        failures.append("Round-8 replay contract changed")

    authority = lock.get("authority", {})
    expected_authority = {
        "author_event_sha256": "5e5ad1b6ff2a62060368877016ad4b14f869f22a3e38f9a703672ea52ecd067f",
        "authorization_request_sha256": "174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63",
        "roadmap_sha256": "ec77e5a53f2d5e937909732992be8139cbc2486f86fa5aa0faec1b54a8cd37a2",
        "author_adjudication_sha256": "5986e259fe58d8fcb37ff32aef0a0339b345f0508450f2d33a3aa309f28f4d49",
        "claim_surface_manifest_sha256": "323d27b42fb2e1208cd477297123b45370460913195ac5792d61ded5884b25b9",
        "writer_handoff_sha256": "5cd268c3e9bb5d975838fafbba24fadacdbc8e8fb1fd15f1715ee942d35342b5",
        "author_adjudicated_items": [
            "REV-001",
            "REV-002",
            "REV-003",
            "REV-004",
            "REV-005",
            "REV-006",
        ],
        "support_scope_items": ["REV-003", "REV-004", "REV-005", "REV-006"],
        "canonical_results_refresh_authorized": False,
        "manuscript_patch_authorized_by_this_lock": False,
    }
    if authority != expected_authority:
        failures.append("Stage-4 authority binding changed")

    bibliography = lock.get("bibliography", {})
    expected_bibliography = {
        "path": "paper/references.bib",
        "sha256": "de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b",
        "current_integrity_record": "notes/stage2_5_integrity_report.json",
        "obsolete_stage2_digest": "acec840393408f146f5e6eed9723cd4e12275108a6059fe0fdb0c2bc508e7248",
    }
    if bibliography != expected_bibliography:
        failures.append("bibliography binding changed")

    inventory = lock.get("artifact_inventory")
    expected_paths = expected_inventory_paths()
    seen: set[str] = set()
    if not isinstance(inventory, list):
        failures.append("artifact_inventory must be a list")
        inventory = []
    for index, item in enumerate(inventory):
        if not isinstance(item, dict) or set(item) != {"path", "bytes", "sha256"}:
            failures.append(f"inventory item {index} has invalid fields")
            continue
        relative = item.get("path")
        if not isinstance(relative, str) or not _is_safe_relative_path(relative):
            failures.append(f"inventory item {index} has unsafe path")
            continue
        if relative in seen:
            failures.append(f"duplicate inventory path: {relative}")
            continue
        seen.add(relative)
        path = project_root / relative
        if not path.is_file():
            failures.append(f"missing inventory file: {relative}")
            continue
        raw = path.read_bytes()
        if item.get("bytes") != len(raw):
            failures.append(f"byte length drift: {relative}")
        if item.get("sha256") != sha256_bytes(raw):
            failures.append(f"SHA-256 drift: {relative}")
    if seen != expected_paths:
        failures.append(
            "closed inventory path set changed; missing="
            + repr(sorted(expected_paths - seen))
            + ", extra="
            + repr(sorted(seen - expected_paths))
        )
    inventory_contract = lock.get("inventory_contract", {})
    if inventory_contract != {
        "closed": True,
        "expected_path_count": len(expected_paths),
        "path_order": "POSIX_LEXICOGRAPHIC",
        "hash_algorithm": "SHA-256",
        "duplicate_paths_allowed": False,
        "unlisted_round_artifacts_allowed": False,
    }:
        failures.append("inventory contract changed")
    if [item.get("path") for item in inventory if isinstance(item, dict)] != sorted(seen):
        failures.append("inventory is not in POSIX lexicographic order")

    if check_environment:
        failures.extend(_environment_failures(lock.get("environment", {})))
    if failures:
        raise LockValidationError(failures)

    replay = _validate_round8_replay(project_root) if replay_round8 else {"executed": False}
    return {
        "status": "PASS",
        "schema": SCHEMA,
        "paper": 25,
        "inventory_files_checked": len(seen),
        "environment_checked": check_environment,
        "round8_replay": replay,
        "scientific_value_changed": False,
        "canonical_results_modified": False,
    }


def validate_lock_file(
    lock_path: Path = DEFAULT_LOCK_PATH,
    *,
    project_root: Path = PROJECT_ROOT,
    check_environment: bool = True,
    replay_round8: bool = False,
) -> dict[str, Any]:
    return validate_lock_payload(
        load_lock(lock_path),
        project_root=project_root,
        check_environment=check_environment,
        replay_round8=replay_round8,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK_PATH)
    parser.add_argument("--replay-round8", action="store_true")
    parser.add_argument("--skip-environment", action="store_true")
    args = parser.parse_args()
    try:
        result = validate_lock_file(
            args.lock,
            check_environment=not args.skip_environment,
            replay_round8=args.replay_round8,
        )
    except LockValidationError as exc:
        print(json.dumps({"status": "FAIL", "failures": exc.failures}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
