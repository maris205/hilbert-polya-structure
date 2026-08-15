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
    safe_directory_entries,
    sha256_file,
    write_json,
)


CLAIM_RELATIVE = "results/registered_run.claim.json"
TERMINAL_RELATIVE = "results/registered_run.json"
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
    "target_set",
    "success_result_path",
    "hit_result_path",
    "registered_run_count",
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
    "target_set",
    "periods_started",
    "periods_completed",
    "stopped_period",
    "artifact_path",
    "artifact_sha256",
    "failure_code",
    "registered_run_count",
    "candidate_numerical_runs",
}


def claim_registered_run(project_root: Path, reviewed_code_sha256: str) -> dict[str, Any]:
    """Durably claim the sole registered run before candidate construction."""

    project_root = _raw_absolute(project_root)
    if not regular_directory(project_root):
        raise ValueError("project root is missing or has a symlink component")
    results = project_root / "results"
    if not regular_directory(results):
        raise ValueError("results directory is missing or has a symlink component")
    review_path = results / "CODE_REVIEW.md"
    preflight_path = results / "PRE_EXECUTION_AUDIT.json"
    if not regular_file(review_path) or not regular_file(preflight_path):
        raise ValueError("review or official pre-execution audit is missing or unsafe")
    payload = {
        "schema": "BASE2_REGISTERED_RUN_CLAIM_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "STARTED",
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "review_file_sha256": sha256_file(review_path),
        "pre_execution_audit_path": "results/PRE_EXECUTION_AUDIT.json",
        "pre_execution_audit_sha256": sha256_file(preflight_path),
        "registered_periods": list(range(2, 8)),
        "target_set": ["1", "-1"],
        "success_result_path": "results/EXPERIMENT_RESULTS.json",
        "hit_result_path": "results/TARGET_HIT_HALT.json",
        "registered_run_count": 1,
        "candidate_numerical_runs": 0,
    }
    # O_EXCL in write_json is the concurrency boundary.  The claim is never removed.
    write_json(project_root / CLAIM_RELATIVE, payload, exclusive=True)
    return payload


def validate_registered_claim(
    project_root: Path,
    reviewed_code_sha256: str,
    *,
    require_clean_started: bool = False,
) -> dict[str, Any]:
    """Validate the immutable claim and every bound artifact/type."""

    project_root = _raw_absolute(project_root)
    claim_path = project_root / CLAIM_RELATIVE
    errors: list[str] = []
    payload: Any = None
    if not regular_file(claim_path):
        errors.append("CLAIM_MISSING_OR_UNSAFE")
    else:
        payload = load_exact_json(claim_path)
        if type(payload) is not dict or set(payload) != CLAIM_KEYS:
            errors.append("CLAIM_KEYS_NOT_EXACT")
        else:
            expected_scalars = {
                "schema": "BASE2_REGISTERED_RUN_CLAIM_V1",
                "candidate_id": CANDIDATE_ID,
                "run_id": "REGISTERED_RUN_0001",
                "state": "STARTED",
                "source_lock_sha256": EXPECTED_LOCK_SHA256,
                "reviewed_code_sha256": reviewed_code_sha256,
                "pre_execution_audit_path": "results/PRE_EXECUTION_AUDIT.json",
                "success_result_path": "results/EXPERIMENT_RESULTS.json",
                "hit_result_path": "results/TARGET_HIT_HALT.json",
            }
            for key, expected in expected_scalars.items():
                if payload[key] != expected:
                    errors.append(f"CLAIM_{key.upper()}_MISMATCH")
            if payload["registered_periods"] != list(range(2, 8)):
                errors.append("CLAIM_PERIODS_MISMATCH")
            if payload["target_set"] != ["1", "-1"]:
                errors.append("CLAIM_TARGET_SET_MISMATCH")
            if type(payload["registered_run_count"]) is not int or payload[
                "registered_run_count"
            ] != 1:
                errors.append("CLAIM_RUN_COUNT_MISMATCH")
            if type(payload["candidate_numerical_runs"]) is not int or payload[
                "candidate_numerical_runs"
            ] != 0:
                errors.append("CLAIM_NUMERICAL_RUN_COUNT_MISMATCH")
            review_path = project_root / "results" / "CODE_REVIEW.md"
            preflight_path = project_root / "results" / "PRE_EXECUTION_AUDIT.json"
            if not regular_file(review_path) or payload["review_file_sha256"] != sha256_file(
                review_path
            ):
                errors.append("CLAIM_REVIEW_HASH_MISMATCH")
            if not regular_file(preflight_path) or payload[
                "pre_execution_audit_sha256"
            ] != sha256_file(preflight_path):
                errors.append("CLAIM_PREFLIGHT_HASH_MISMATCH")
    if require_clean_started:
        forbidden = [
            TERMINAL_RELATIVE,
            "results/EXPERIMENT_RESULTS.json",
            "results/TARGET_HIT_HALT.json",
            "results/result_manifest.json",
        ]
        try:
            result_names = {
                item["name"] for item in safe_directory_entries(project_root / "results")
            }
        except (OSError, RuntimeError):
            result_names = {"<unsafe-results-directory>"}
        present = [
            relative
            for relative in forbidden
            if Path(relative).name in result_names
        ]
        if "<unsafe-results-directory>" in result_names:
            present.append("results/<unsafe-results-directory>")
        if present:
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
    stopped_period: int | None,
    artifact_path: str | None,
    failure_code: str | None,
) -> Path:
    """Create one immutable success, target-halt, or failure terminal ledger."""

    project_root = _raw_absolute(project_root)
    if state not in {"COMPLETED_NO_HIT", "HALTED_TARGET_HIT", "FAILED_CLOSED"}:
        raise ValueError("invalid registered terminal state")
    claim = validate_registered_claim(project_root, reviewed_code_sha256)
    if claim["pass"] is not True:
        raise RuntimeError("cannot terminate an invalid registered claim")
    claim_payload = claim["payload"]
    frozen = list(range(2, 8))
    if periods_started != frozen[: len(periods_started)]:
        raise ValueError("periods_started is not a frozen prefix")
    if periods_completed != periods_started[: len(periods_completed)]:
        raise ValueError("periods_completed is not a prefix of periods_started")
    artifact_sha256: str | None = None
    if artifact_path is not None:
        artifact = project_root / artifact_path
        if not regular_file(artifact):
            raise ValueError("terminal artifact is missing or unsafe")
        artifact_sha256 = sha256_file(artifact)
    if state == "COMPLETED_NO_HIT":
        valid_state = (
            periods_started == frozen
            and periods_completed == frozen
            and stopped_period is None
            and artifact_path == "results/EXPERIMENT_RESULTS.json"
            and failure_code is None
        )
    elif state == "HALTED_TARGET_HIT":
        valid_state = (
            bool(periods_started)
            and periods_completed == periods_started
            and stopped_period == periods_started[-1]
            and artifact_path == "results/TARGET_HIT_HALT.json"
            and failure_code == "TARGET_HIT"
        )
    else:
        valid_state = (
            periods_completed == periods_started[: len(periods_completed)]
            and failure_code in {
                "GATE_OR_TREE_CHANGED",
                "IMPLEMENTATION_EXCEPTION",
                "INTERRUPTED",
                "OUTPUT_COMMIT_FAILED",
            }
        )
    if not valid_state:
        raise ValueError("terminal state fields are inconsistent")
    payload = {
        "schema": "BASE2_REGISTERED_RUN_TERMINAL_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": state,
        "claim_path": CLAIM_RELATIVE,
        "claim_sha256": claim["claim_sha256"],
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_sha256,
        "review_file_sha256": claim_payload["review_file_sha256"],
        "pre_execution_audit_sha256": claim_payload["pre_execution_audit_sha256"],
        "registered_periods": frozen,
        "target_set": ["1", "-1"],
        "periods_started": periods_started,
        "periods_completed": periods_completed,
        "stopped_period": stopped_period,
        "artifact_path": artifact_path,
        "artifact_sha256": artifact_sha256,
        "failure_code": failure_code,
        "registered_run_count": 1,
        "candidate_numerical_runs": 0,
    }
    path = project_root / TERMINAL_RELATIVE
    write_json(path, payload, exclusive=True)
    return path
