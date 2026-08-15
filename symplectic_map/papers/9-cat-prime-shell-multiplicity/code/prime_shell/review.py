"""Hash-bound independent deployment and post-run review authorities."""

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
)
from .protocol import (
    code_tree_sha256,
    regular_file,
    sha256_file,
    stable_file_bytes,
    strict_json_loads,
)


ROUND1_PREFIX = "PRIME_SHELL_CODE_REVIEW_V1 "
ROUND1_REVIEW_SHA256 = (
    "77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0"
)
ROUND1_REVIEW_SIZE = 10004
ROUND1_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "reviewed_code_sha256": (
        "ff360e9c42d304fbac36fafcc7a977758b3c6fa0e011aadd2522f8185ae86bbe"
    ),
    "reviewer_independent": True,
    "source_lock_sha256": SOURCE_LOCK_SHA256,
    "test_evidence_sha256": (
        "7b0581287e4525639602c23c95fda7fc97208353ee994b93a6a0120377e4bc92"
    ),
    "verdict": "FAIL",
}
ROUND2_FAIL_PREFIX = "PRIME_SHELL_CODE_REVIEW_ROUND2_FAIL "
ROUND2_REVIEW_SHA256 = (
    "0647a31103b55d55ce901c150cb9b72230ea35541e04af14e539ce9e2ef92db5"
)
ROUND2_REVIEW_SIZE = 20427
ROUND2_FAIL_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "review_round": 2,
    "reviewed_code_sha256": (
        "60f53f04c9ab4c0ee036ceba59b3ee678016902ff40b538e9922719a939bc228"
    ),
    "reviewer_independent": True,
    "round1_review_sha256": ROUND1_REVIEW_SHA256,
    "source_lock_sha256": SOURCE_LOCK_SHA256,
    "test_evidence_sha256": (
        "dd654b54cc68403234686292aa51dcbd063e025badc893f373222997c74da515"
    ),
    "verdict": "FAIL",
}
ROUND3_FAIL_PREFIX = "PRIME_SHELL_CODE_REVIEW_ROUND3_FAIL "
ROUND3_REVIEW_SHA256 = (
    "775d05e002ce4cd1bc343cbca01f2b2db471c239442c9e0752500aafb6c55cff"
)
ROUND3_REVIEW_SIZE = 27854
ROUND3_FAIL_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "review_round": 3,
    "reviewed_code_sha256": (
        "b078ade2e2ecb66c99760f6871d73d812eaf796beac86a7319e9ed47b965d358"
    ),
    "reviewer_independent": True,
    "round1_review_sha256": ROUND1_REVIEW_SHA256,
    "round2_review_sha256": ROUND2_REVIEW_SHA256,
    "source_lock_sha256": SOURCE_LOCK_SHA256,
    "test_evidence_sha256": (
        "ee46ad6ca672b8cf30140ea84734935b6eda5c77d89ca0868640d08f10de6a95"
    ),
    "verdict": "FAIL",
}
DEPLOYMENT_PREFIX = "PRIME_SHELL_CODE_REVIEW_V4 "
DEPLOYMENT_KEYS = {
    "candidate_id",
    "review_round",
    "reviewed_code_sha256",
    "reviewer_independent",
    "round1_review_sha256",
    "round2_review_sha256",
    "round3_review_sha256",
    "source_lock_sha256",
    "test_evidence_sha256",
    "verdict",
}
RESULT_PREFIX = "PRIME_SHELL_RESULT_REVIEW_V1 "
RESULT_KEYS = {
    "candidate_id",
    "execution_code_sha256",
    "result_sha256",
    "reviewer_independent",
    "source_lock_sha256",
    "verdict",
}


def _parse_authority(
    text: str,
    *,
    prefix: str,
    keys: set[str],
    expected: dict[str, Any],
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
        raw = lines[0][len(prefix) :]
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
    historical_prefix = encoded[:ROUND1_REVIEW_SIZE]
    round2_history = encoded[:ROUND2_REVIEW_SIZE]
    round3_history = encoded[:ROUND3_REVIEW_SIZE]
    historical_occurrences = text.count(ROUND1_PREFIX)
    historical_lines = [
        line for line in text.splitlines() if line.startswith(ROUND1_PREFIX)
    ]
    historical_errors: list[str] = []
    historical_authority: dict[str, Any] | None = None
    if (
        len(encoded) < ROUND1_REVIEW_SIZE
        or hashlib.sha256(historical_prefix).hexdigest() != ROUND1_REVIEW_SHA256
    ):
        historical_errors.append("ROUND1_FAIL_HISTORY_NOT_BYTE_EXACT")
    if historical_occurrences != 1 or len(historical_lines) != 1:
        historical_errors.append("ROUND1_FAIL_AUTHORITY_COUNT_NOT_ONE")
    else:
        raw = historical_lines[0][len(ROUND1_PREFIX) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError):
            historical_errors.append("ROUND1_FAIL_AUTHORITY_JSON_MALFORMED")
        else:
            if (
                type(parsed) is not dict
                or parsed != ROUND1_AUTHORITY
                or raw != json.dumps(parsed, sort_keys=True, separators=(",", ":"))
            ):
                historical_errors.append("ROUND1_FAIL_AUTHORITY_NOT_EXACT")
            else:
                historical_authority = parsed
    round2_occurrences = text.count(ROUND2_FAIL_PREFIX)
    round2_lines = [
        line for line in text.splitlines() if line.startswith(ROUND2_FAIL_PREFIX)
    ]
    round2_errors: list[str] = []
    round2_authority: dict[str, Any] | None = None
    if (
        len(encoded) < ROUND2_REVIEW_SIZE
        or hashlib.sha256(round2_history).hexdigest() != ROUND2_REVIEW_SHA256
    ):
        round2_errors.append("ROUND2_FAIL_HISTORY_NOT_BYTE_EXACT")
    if round2_occurrences != 1 or len(round2_lines) != 1:
        round2_errors.append("ROUND2_FAIL_AUTHORITY_COUNT_NOT_ONE")
    else:
        raw = round2_lines[0][len(ROUND2_FAIL_PREFIX) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError):
            round2_errors.append("ROUND2_FAIL_AUTHORITY_JSON_MALFORMED")
        else:
            if (
                type(parsed) is not dict
                or parsed != ROUND2_FAIL_AUTHORITY
                or raw != json.dumps(parsed, sort_keys=True, separators=(",", ":"))
            ):
                round2_errors.append("ROUND2_FAIL_AUTHORITY_NOT_EXACT")
            else:
                round2_authority = parsed
    round3_occurrences = text.count(ROUND3_FAIL_PREFIX)
    round3_lines = [
        line for line in text.splitlines() if line.startswith(ROUND3_FAIL_PREFIX)
    ]
    round3_errors: list[str] = []
    round3_authority: dict[str, Any] | None = None
    if (
        len(encoded) < ROUND3_REVIEW_SIZE
        or hashlib.sha256(round3_history).hexdigest() != ROUND3_REVIEW_SHA256
    ):
        round3_errors.append("ROUND3_FAIL_HISTORY_NOT_BYTE_EXACT")
    if round3_occurrences != 1 or len(round3_lines) != 1:
        round3_errors.append("ROUND3_FAIL_AUTHORITY_COUNT_NOT_ONE")
    else:
        raw = round3_lines[0][len(ROUND3_FAIL_PREFIX) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError):
            round3_errors.append("ROUND3_FAIL_AUTHORITY_JSON_MALFORMED")
        else:
            if (
                type(parsed) is not dict
                or parsed != ROUND3_FAIL_AUTHORITY
                or raw != json.dumps(parsed, sort_keys=True, separators=(",", ":"))
            ):
                round3_errors.append("ROUND3_FAIL_AUTHORITY_NOT_EXACT")
            else:
                round3_authority = parsed
    current = _parse_authority(
        text,
        prefix=DEPLOYMENT_PREFIX,
        keys=DEPLOYMENT_KEYS,
        expected={
            "candidate_id": CANDIDATE_ID,
            "review_round": 4,
            "reviewed_code_sha256": code_sha256,
            "reviewer_independent": True,
            "round1_review_sha256": ROUND1_REVIEW_SHA256,
            "round2_review_sha256": ROUND2_REVIEW_SHA256,
            "round3_review_sha256": ROUND3_REVIEW_SHA256,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "test_evidence_sha256": test_sha256,
            "verdict": "DEPLOYMENT_PASS",
        },
    )
    errors = historical_errors + round2_errors + round3_errors + current["errors"]
    return {
        "round1_review_sha256": hashlib.sha256(historical_prefix).hexdigest(),
        "round1_authority_prefix_occurrences": historical_occurrences,
        "round1_authority": historical_authority,
        "round2_review_sha256": hashlib.sha256(round2_history).hexdigest(),
        "round2_authority_prefix_occurrences": round2_occurrences,
        "round2_authority": round2_authority,
        "round3_review_sha256": hashlib.sha256(round3_history).hexdigest(),
        "round3_authority_prefix_occurrences": round3_occurrences,
        "round3_authority": round3_authority,
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
            "stage": "P3_INDEPENDENT_DEPLOYMENT_REVIEW",
            "reviewed_code_sha256": code_sha,
            "errors": ["PREEXECUTION_TEST_EVIDENCE_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    test_sha = sha256_file(test_path)
    if not regular_file(review_path):
        return {
            "stage": "P3_INDEPENDENT_DEPLOYMENT_REVIEW",
            "reviewed_code_sha256": code_sha,
            "test_evidence_sha256": test_sha,
            "review_path": CODE_REVIEW_PATH,
            "errors": ["CODE_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    review_bytes = stable_file_bytes(review_path)
    parsed = parse_deployment_authority(
        review_bytes.decode("utf-8"), code_sha256=code_sha, test_sha256=test_sha
    )
    return {
        "stage": "P3_INDEPENDENT_DEPLOYMENT_REVIEW",
        "review_path": CODE_REVIEW_PATH,
        "review_file_sha256": hashlib.sha256(review_bytes).hexdigest(),
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
        return {"stage": "R100_INDEPENDENT_RESULT_REVIEW", "errors": ["RESULT_MISSING"], "pass": False}
    result_sha = sha256_file(result_path)
    if not regular_file(review_path):
        return {
            "stage": "R100_INDEPENDENT_RESULT_REVIEW",
            "result_sha256": result_sha,
            "errors": ["RESULT_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    review_bytes = stable_file_bytes(review_path)
    parsed = parse_result_authority(
        review_bytes.decode("utf-8"),
        execution_code_sha256=execution_code_sha256,
        result_sha256=result_sha,
    )
    return {
        "stage": "R100_INDEPENDENT_RESULT_REVIEW",
        "review_file_sha256": hashlib.sha256(review_bytes).hexdigest(),
        "result_sha256": result_sha,
        **parsed,
    }
