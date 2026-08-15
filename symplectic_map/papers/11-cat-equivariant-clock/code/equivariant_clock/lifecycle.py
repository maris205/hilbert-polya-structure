"""Durable one-shot registration and terminal state transitions."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CLAIM_PATH,
    CODE_REVIEW_PATH,
    LOCKED_MODULI,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
    RESULT_PATH,
    SOURCE_LOCK_SHA256,
    TERMINAL_PATH,
)
from .protocol import lexical_absolute, load_exact_json, regular_file, sha256_file, write_json


PRERUN_RESULT_FILES = frozenset(
    {
        Path(CODE_REVIEW_PATH).name,
        Path(PREEXECUTION_TEST_PATH).name,
        Path(PREEXECUTION_AUDIT_PATH).name,
    }
)
ONE_SHOT_FILES = frozenset(
    {Path(CLAIM_PATH).name, Path(RESULT_PATH).name, Path(TERMINAL_PATH).name}
)


def _exact_same(value: Any, expected: Any) -> bool:
    if type(value) is not type(expected):
        return False
    if type(expected) is dict:
        return set(value) == set(expected) and all(
            _exact_same(value[key], expected[key]) for key in expected
        )
    if type(expected) is list:
        return len(value) == len(expected) and all(
            _exact_same(left, right) for left, right in zip(value, expected, strict=True)
        )
    return value == expected


def result_file_names(project_root: Path) -> set[str]:
    results = lexical_absolute(project_root) / "results"
    entries = list(results.iterdir())
    if any(not regular_file(entry) for entry in entries):
        raise RuntimeError("results contains a non-regular or unsafe entry")
    return {entry.name for entry in entries}


def claim_registered_run(
    project_root: Path,
    *,
    reviewed_code_sha256: str,
    review_file_sha256: str,
    preflight_sha256: str,
) -> Path:
    root = lexical_absolute(project_root)
    observed = result_file_names(root)
    if observed != set(PRERUN_RESULT_FILES):
        raise RuntimeError("registered run requires the exact closed pre-run inventory")
    if observed.intersection(ONE_SHOT_FILES):
        raise RuntimeError("registered lifecycle was already claimed")
    claim = {
        "schema": "EQUIVARIANT_CLOCK_REGISTERED_RUN_CLAIM_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "STARTED",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "review_file_sha256": review_file_sha256,
        "pre_execution_audit_path": PREEXECUTION_AUDIT_PATH,
        "pre_execution_audit_sha256": preflight_sha256,
        "registered_moduli": list(LOCKED_MODULI),
        "structural_control_count": 1,
        "structural_control_in_modulus_namespace": False,
        "result_path": RESULT_PATH,
        "terminal_path": TERMINAL_PATH,
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
    }
    output = root / CLAIM_PATH
    write_json(output, claim, exclusive=True)
    return output


def validate_claim(project_root: Path, reviewed_code_sha256: str) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    path = root / CLAIM_PATH
    if not regular_file(path):
        return {"errors": ["CLAIM_MISSING"], "pass": False}
    claim = load_exact_json(path)
    expected = {
        "schema": "EQUIVARIANT_CLOCK_REGISTERED_RUN_CLAIM_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "STARTED",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "review_file_sha256": sha256_file(root / CODE_REVIEW_PATH),
        "pre_execution_audit_path": PREEXECUTION_AUDIT_PATH,
        "pre_execution_audit_sha256": sha256_file(root / PREEXECUTION_AUDIT_PATH),
        "registered_moduli": list(LOCKED_MODULI),
        "structural_control_count": 1,
        "structural_control_in_modulus_namespace": False,
        "result_path": RESULT_PATH,
        "terminal_path": TERMINAL_PATH,
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
    }
    errors = [] if _exact_same(claim, expected) else ["CLAIM_NOT_EXACT_OR_STALE"]
    return {"claim": claim, "claim_sha256": sha256_file(path), "errors": errors, "pass": not errors}


def write_terminal(
    project_root: Path,
    *,
    reviewed_code_sha256: str,
    state: str,
    moduli_started: list[int],
    moduli_completed: list[int],
    failure_code: str | None,
) -> Path:
    if state not in {"COMPLETED_CERTIFIED", "FAILED_CLOSED"}:
        raise ValueError("terminal state is not source locked")
    root = lexical_absolute(project_root)
    claim = validate_claim(root, reviewed_code_sha256)
    if claim["pass"] is not True:
        raise RuntimeError("cannot terminalize an invalid claim")
    result_exists = regular_file(root / RESULT_PATH)
    if state == "COMPLETED_CERTIFIED" and not result_exists:
        raise RuntimeError("certified terminal requires a committed result")
    terminal = {
        "schema": "EQUIVARIANT_CLOCK_REGISTERED_RUN_TERMINAL_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": state,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "claim_sha256": claim["claim_sha256"],
        "moduli_started": list(moduli_started),
        "moduli_completed": list(moduli_completed),
        "structural_control_completed": state == "COMPLETED_CERTIFIED",
        "result_path": RESULT_PATH if result_exists else None,
        "result_sha256": sha256_file(root / RESULT_PATH) if result_exists else None,
        "failure_code": failure_code,
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
    }
    output = root / TERMINAL_PATH
    write_json(output, terminal, exclusive=True)
    return output
