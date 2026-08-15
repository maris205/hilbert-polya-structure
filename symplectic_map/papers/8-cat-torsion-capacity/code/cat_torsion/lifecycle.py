"""Immutable one-shot claim and terminal ledgers for registered execution."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    _raw_absolute,
    load_exact_json,
    regular_directory,
    regular_file,
    sha256_file,
    write_json,
)


CLAIM_RELATIVE = "results/registered_run.claim.json"
TERMINAL_RELATIVE = "results/registered_run.json"
REGISTERED_PERIODS = list(range(1, 13))
CLAIM_KEYS = {
    "schema",
    "candidate_id",
    "run_id",
    "state",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "review_file_sha256",
    "pre_execution_audit_path",
    "pre_execution_audit_sha256",
    "registered_periods",
    "result_path",
    "terminal_path",
    "registered_run_count",
    "registered_exact_audits",
    "candidate_numerical_runs",
}
TERMINAL_KEYS = {
    "schema",
    "candidate_id",
    "run_id",
    "state",
    "claim_path",
    "claim_sha256",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "review_file_sha256",
    "pre_execution_audit_sha256",
    "registered_periods",
    "periods_started",
    "periods_completed",
    "artifact_path",
    "artifact_sha256",
    "classification",
    "failure_code",
    "registered_run_count",
    "registered_exact_audits",
    "candidate_numerical_runs",
}


def claim_registered_run(project_root: Path, reviewed_code_sha256: str) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    if not regular_directory(project_root) or not regular_directory(project_root / "results"):
        raise ValueError("project or results directory is missing or unsafe")
    review_path = project_root / "results" / "CODE_REVIEW.md"
    preflight_path = project_root / "results" / "PRE_EXECUTION_AUDIT.json"
    if not regular_file(review_path) or not regular_file(preflight_path):
        raise ValueError("review or official pre-execution audit is missing or unsafe")
    payload = {
        "schema": "CAT_TORSION_REGISTERED_RUN_CLAIM_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "STARTED",
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "review_file_sha256": sha256_file(review_path),
        "pre_execution_audit_path": "results/PRE_EXECUTION_AUDIT.json",
        "pre_execution_audit_sha256": sha256_file(preflight_path),
        "registered_periods": REGISTERED_PERIODS,
        "result_path": "results/EXPERIMENT_RESULTS.json",
        "terminal_path": TERMINAL_RELATIVE,
        "registered_run_count": 1,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
    }
    write_json(project_root / CLAIM_RELATIVE, payload, exclusive=True)
    return payload


def validate_registered_claim(
    project_root: Path,
    reviewed_code_sha256: str,
    *,
    require_clean_started: bool = False,
) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    claim_path = project_root / CLAIM_RELATIVE
    errors: list[str] = []
    payload: Any = None
    if not regular_file(claim_path):
        errors.append("CLAIM_MISSING_OR_UNSAFE")
    else:
        try:
            payload = load_exact_json(claim_path)
        except (OSError, ValueError):
            errors.append("CLAIM_STRICT_JSON_INVALID")
        if not errors and (type(payload) is not dict or set(payload) != CLAIM_KEYS):
            errors.append("CLAIM_KEYS_NOT_EXACT")
        if not errors:
            expected = {
                "schema": "CAT_TORSION_REGISTERED_RUN_CLAIM_V1",
                "candidate_id": CANDIDATE_ID,
                "run_id": "REGISTERED_RUN_0001",
                "state": "STARTED",
                "source_lock_sha256": EXPECTED_LOCK_SHA256,
                "reviewed_code_sha256": reviewed_code_sha256,
                "pre_execution_audit_path": "results/PRE_EXECUTION_AUDIT.json",
                "registered_periods": REGISTERED_PERIODS,
                "result_path": "results/EXPERIMENT_RESULTS.json",
                "terminal_path": TERMINAL_RELATIVE,
                "registered_run_count": 1,
                "registered_exact_audits": 1,
                "candidate_numerical_runs": 0,
            }
            for key, expected_value in expected.items():
                if payload[key] != expected_value or type(payload[key]) is not type(expected_value):
                    errors.append(f"CLAIM_{key.upper()}_MISMATCH")
            review_path = project_root / "results" / "CODE_REVIEW.md"
            preflight_path = project_root / "results" / "PRE_EXECUTION_AUDIT.json"
            if not regular_file(review_path) or payload["review_file_sha256"] != sha256_file(review_path):
                errors.append("CLAIM_REVIEW_HASH_MISMATCH")
            if not regular_file(preflight_path) or payload[
                "pre_execution_audit_sha256"
            ] != sha256_file(preflight_path):
                errors.append("CLAIM_PREFLIGHT_HASH_MISMATCH")
    if require_clean_started:
        for relative in (
            TERMINAL_RELATIVE,
            "results/EXPERIMENT_RESULTS.json",
            "results/result_manifest.json",
        ):
            if regular_file(project_root / relative):
                errors.append("STARTED_STATE_HAS_ORPHAN_OR_TERMINAL_ARTIFACT")
    return {
        "claim_path": CLAIM_RELATIVE,
        "claim_sha256": sha256_file(claim_path) if regular_file(claim_path) else None,
        "payload": payload,
        "errors": errors,
        "pass": not errors,
    }


def write_terminal_ledger(
    project_root: Path,
    *,
    reviewed_code_sha256: str,
    state: str,
    periods_started: list[int],
    periods_completed: list[int],
    artifact_path: str | None,
    classification: str,
    failure_code: str | None,
) -> Path:
    project_root = _raw_absolute(project_root)
    if state not in {"COMPLETED_CERTIFIED", "FAILED_CLOSED"}:
        raise ValueError("invalid terminal state")
    claim = validate_registered_claim(project_root, reviewed_code_sha256)
    if claim["pass"] is not True:
        raise RuntimeError("cannot terminate an invalid registered claim")
    if periods_started != REGISTERED_PERIODS[: len(periods_started)]:
        raise ValueError("periods_started is not a frozen prefix")
    if periods_completed != periods_started[: len(periods_completed)]:
        raise ValueError("periods_completed is not a prefix of periods_started")
    allowed_classifications = {
        "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH",
        "NARROW_OR_REPAIR",
        "REJECTED_THEOREM_CONTRACT",
    }
    if classification not in allowed_classifications:
        raise ValueError("classification is not source locked")
    artifact_sha256 = None
    if artifact_path is not None:
        artifact = project_root / artifact_path
        if not regular_file(artifact):
            raise ValueError("terminal artifact is missing or unsafe")
        artifact_sha256 = sha256_file(artifact)
    if state == "COMPLETED_CERTIFIED":
        valid = (
            periods_started == REGISTERED_PERIODS
            and periods_completed == REGISTERED_PERIODS
            and artifact_path == "results/EXPERIMENT_RESULTS.json"
            and classification
            == "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH"
            and failure_code is None
        )
    else:
        valid = (
            artifact_path is None
            and classification in {"NARROW_OR_REPAIR", "REJECTED_THEOREM_CONTRACT"}
            and failure_code
            in {
                "GATE_OR_TREE_CHANGED",
                "IMPLEMENTATION_EXCEPTION",
                "INTERRUPTED",
                "THEOREM_CONTRADICTION",
                "OUTPUT_COMMIT_FAILED",
            }
        )
    if not valid:
        raise ValueError("terminal state fields are inconsistent")
    claim_payload = claim["payload"]
    payload = {
        "schema": "CAT_TORSION_REGISTERED_RUN_TERMINAL_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": state,
        "claim_path": CLAIM_RELATIVE,
        "claim_sha256": claim["claim_sha256"],
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "review_file_sha256": claim_payload["review_file_sha256"],
        "pre_execution_audit_sha256": claim_payload["pre_execution_audit_sha256"],
        "registered_periods": REGISTERED_PERIODS,
        "periods_started": periods_started,
        "periods_completed": periods_completed,
        "artifact_path": artifact_path,
        "artifact_sha256": artifact_sha256,
        "classification": classification,
        "failure_code": failure_code,
        "registered_run_count": 1,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
    }
    terminal = project_root / TERMINAL_RELATIVE
    write_json(terminal, payload, exclusive=True)
    return terminal
