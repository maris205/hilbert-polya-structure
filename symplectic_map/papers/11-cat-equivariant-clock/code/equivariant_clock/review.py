"""Hash-bound independent deployment and result-review authorities."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CODE_REVIEW_PATH,
    PREEXECUTION_TEST_PATH,
    RESULT_PATH,
    RESULT_REVIEW_PATH,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_R2_SHA256,
)
from .protocol import code_tree_sha256, regular_file, sha256_file, stable_file_bytes, strict_json_loads


ROUND1_PREFIX = "EQUIVARIANT_CLOCK_CODE_REVIEW_V1 "
ROUND1_REVIEW_SHA256 = "ac517ce6f5d206416ec8d19399f6bd3d7216b023d6c9a34a9acb087d016a3ee6"
ROUND1_REVIEW_SIZE = 9765
ROUND1_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "reviewed_code_sha256": "5ee0bdd9f3410a6ed17ab500522d9bc6a205b5444559b5eb02cb3e1c6a52acae",
    "reviewer_independent": True,
    "source_lock_sha256": SOURCE_LOCK_SHA256,
    "source_review_sha256": SOURCE_REVIEW_R2_SHA256,
    "test_evidence_sha256": "e81c286143316a19dc132b5fa6975ffd8f51dde14ec9c81f80b4f0bafc646b59",
    "verdict": "DEPLOYMENT_FAIL",
}
DEPLOYMENT_PREFIX = "EQUIVARIANT_CLOCK_CODE_REVIEW_V2 "
DEPLOYMENT_KEYS = {
    "candidate_id",
    "review_round",
    "reviewed_code_sha256",
    "reviewer_independent",
    "round1_review_sha256",
    "source_lock_sha256",
    "source_review_sha256",
    "test_evidence_sha256",
    "verdict",
}
RESULT_PREFIX = "EQUIVARIANT_CLOCK_RESULT_REVIEW_V1 "
RESULT_KEYS = {
    "candidate_id",
    "execution_code_sha256",
    "result_sha256",
    "reviewer_independent",
    "source_lock_sha256",
    "verdict",
}


def _parse_authority(
    text: str, *, prefix: str, keys: set[str], expected: dict[str, Any]
) -> dict[str, Any]:
    occurrences = text.count(prefix)
    lines = [line for line in text.splitlines() if line.startswith(prefix)]
    errors: list[str] = []
    authority: dict[str, Any] | None = None
    if occurrences != 1:
        errors.append("AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE")
    if len(lines) != 1:
        errors.append("COLUMN_ONE_AUTHORITY_LINE_COUNT_NOT_ONE")
    if not errors:
        raw = lines[0][len(prefix):]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError):
            errors.append("AUTHORITY_JSON_MALFORMED")
        else:
            if type(parsed) is not dict:
                errors.append("AUTHORITY_JSON_NOT_OBJECT")
            elif set(parsed) != keys:
                errors.append("AUTHORITY_KEYS_NOT_EXACT")
            else:
                authority = parsed
                if raw != json.dumps(parsed, sort_keys=True, separators=(",", ":")):
                    errors.append("AUTHORITY_JSON_NOT_CANONICAL")
                for key, value in expected.items():
                    if parsed.get(key) != value or type(parsed.get(key)) is not type(value):
                        errors.append("AUTHORITY_" + key.upper() + "_MISMATCH")
    return {
        "authority_prefix_occurrences": occurrences,
        "canonical_authority_lines": len(lines),
        "authority": authority,
        "errors": errors,
        "pass": not errors,
    }


def parse_deployment_authority(
    text: str, *, code_sha256: str, test_sha256: str
) -> dict[str, Any]:
    encoded = text.encode("utf-8")
    historical = encoded[:ROUND1_REVIEW_SIZE]
    historical_errors: list[str] = []
    if len(encoded) < ROUND1_REVIEW_SIZE or hashlib.sha256(historical).hexdigest() != ROUND1_REVIEW_SHA256:
        historical_errors.append("ROUND1_FAIL_HISTORY_NOT_BYTE_EXACT")
    historical_text = historical.decode("utf-8") if len(historical) == ROUND1_REVIEW_SIZE else ""
    parsed_history = _parse_authority(
        historical_text,
        prefix=ROUND1_PREFIX,
        keys={
            "candidate_id",
            "reviewed_code_sha256",
            "reviewer_independent",
            "source_lock_sha256",
            "source_review_sha256",
            "test_evidence_sha256",
            "verdict",
        },
        expected=ROUND1_AUTHORITY,
    )
    historical_errors.extend(parsed_history["errors"])
    current = _parse_authority(
        text,
        prefix=DEPLOYMENT_PREFIX,
        keys=DEPLOYMENT_KEYS,
        expected={
            "candidate_id": CANDIDATE_ID,
            "review_round": 2,
            "reviewed_code_sha256": code_sha256,
            "reviewer_independent": True,
            "round1_review_sha256": ROUND1_REVIEW_SHA256,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "source_review_sha256": SOURCE_REVIEW_R2_SHA256,
            "test_evidence_sha256": test_sha256,
            "verdict": "DEPLOYMENT_PASS",
        },
    )
    errors = historical_errors + current["errors"]
    return {
        "round1_review_sha256": hashlib.sha256(historical).hexdigest(),
        "round1_authority": parsed_history["authority"],
        **{key: value for key, value in current.items() if key not in {"errors", "pass"}},
        "errors": errors,
        "pass": not errors,
    }


def validate_deployment_authority(project_root: Path) -> dict[str, Any]:
    code_sha = code_tree_sha256(project_root)
    test_path = project_root / PREEXECUTION_TEST_PATH
    review_path = project_root / CODE_REVIEW_PATH
    if not regular_file(test_path):
        return {
            "stage": "P4_INDEPENDENT_DEPLOYMENT_REVIEW",
            "reviewed_code_sha256": code_sha,
            "errors": ["TEST_EVIDENCE_MISSING"],
            "pass": False,
        }
    test_sha = sha256_file(test_path)
    if not regular_file(review_path):
        return {
            "stage": "P4_INDEPENDENT_DEPLOYMENT_REVIEW",
            "reviewed_code_sha256": code_sha,
            "test_evidence_sha256": test_sha,
            "review_path": CODE_REVIEW_PATH,
            "errors": ["CODE_REVIEW_MISSING"],
            "pass": False,
        }
    raw = stable_file_bytes(review_path)
    parsed = parse_deployment_authority(
        raw.decode("utf-8"), code_sha256=code_sha, test_sha256=test_sha
    )
    return {
        "stage": "P4_INDEPENDENT_DEPLOYMENT_REVIEW",
        "review_path": CODE_REVIEW_PATH,
        "review_file_sha256": hashlib.sha256(raw).hexdigest(),
        "reviewed_code_sha256": code_sha,
        "test_evidence_sha256": test_sha,
        **parsed,
    }


def parse_result_authority(
    text: str, *, execution_code_sha256: str, result_sha256: str
) -> dict[str, Any]:
    return _parse_authority(
        text,
        prefix=RESULT_PREFIX,
        keys=RESULT_KEYS,
        expected={
            "candidate_id": CANDIDATE_ID,
            "execution_code_sha256": execution_code_sha256,
            "result_sha256": result_sha256,
            "reviewer_independent": True,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "verdict": "RESULT_PASS",
        },
    )


def validate_result_authority(project_root: Path, execution_code_sha256: str) -> dict[str, Any]:
    result_path = project_root / RESULT_PATH
    review_path = project_root / RESULT_REVIEW_PATH
    if not regular_file(result_path):
        return {"stage": "R119_INDEPENDENT_RESULT_REVIEW", "errors": ["RESULT_MISSING"], "pass": False}
    result_sha = sha256_file(result_path)
    if not regular_file(review_path):
        return {
            "stage": "R119_INDEPENDENT_RESULT_REVIEW",
            "result_sha256": result_sha,
            "errors": ["RESULT_REVIEW_MISSING"],
            "pass": False,
        }
    raw = stable_file_bytes(review_path)
    parsed = parse_result_authority(
        raw.decode("utf-8"),
        execution_code_sha256=execution_code_sha256,
        result_sha256=result_sha,
    )
    return {
        "stage": "R119_INDEPENDENT_RESULT_REVIEW",
        "review_file_sha256": hashlib.sha256(raw).hexdigest(),
        "result_sha256": result_sha,
        **parsed,
    }
