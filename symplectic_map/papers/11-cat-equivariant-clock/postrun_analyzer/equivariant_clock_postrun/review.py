"""Exact execution, result, and post-run analyzer authority validation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .constants import (
    ANALYZER_AUTHORITY_KEYS,
    ANALYZER_AUTHORITY_PREFIX,
    ANALYZER_JUNIT_PATH,
    ANALYZER_REVIEW_PATH,
    CANDIDATE_ID,
    EXECUTION_TREE_SHA256,
    IMMUTABLE_ARTIFACTS,
    SOURCE_LOCK_SHA256,
)
from .protocol import (
    analyzer_tree_sha256,
    parse_analyzer_junit,
    regular_file,
    stable_file_bytes,
    strict_json_loads,
)


DEPLOYMENT_PREFIX = "EQUIVARIANT_CLOCK_CODE_REVIEW_V2 "
RESULT_PREFIX = "EQUIVARIANT_CLOCK_RESULT_REVIEW_V1 "

EXPECTED_DEPLOYMENT_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "review_round": 2,
    "reviewed_code_sha256": EXECUTION_TREE_SHA256,
    "reviewer_independent": True,
    "round1_review_sha256": "ac517ce6f5d206416ec8d19399f6bd3d7216b023d6c9a34a9acb087d016a3ee6",
    "source_lock_sha256": SOURCE_LOCK_SHA256,
    "source_review_sha256": "2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622",
    "test_evidence_sha256": "4cf187fbd29f8a2b89dae2035a0971086b70108e395629ef198fcfc4869307ff",
    "verdict": "DEPLOYMENT_PASS",
}
EXPECTED_RESULT_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "execution_code_sha256": EXECUTION_TREE_SHA256,
    "result_sha256": IMMUTABLE_ARTIFACTS["results/EXPERIMENT_RESULTS.json"][0],
    "reviewer_independent": True,
    "source_lock_sha256": SOURCE_LOCK_SHA256,
    "verdict": "RESULT_PASS",
}


def _parse_exact_authority(text: str, prefix: str, expected: dict[str, Any]) -> dict[str, Any]:
    occurrences = text.count(prefix)
    lines = [line for line in text.splitlines() if line.startswith(prefix)]
    errors: list[str] = []
    authority: dict[str, Any] | None = None
    if occurrences != 1:
        errors.append("AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE")
    if len(lines) != 1:
        errors.append("AUTHORITY_COLUMN_ONE_LINE_COUNT_NOT_ONE")
    if not errors:
        raw = lines[0][len(prefix) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError, TypeError):
            errors.append("AUTHORITY_JSON_INVALID")
        else:
            if type(parsed) is not dict:
                errors.append("AUTHORITY_NOT_OBJECT")
            elif set(parsed) != set(expected):
                errors.append("AUTHORITY_KEYS_NOT_EXACT")
            else:
                authority = parsed
                if raw != json.dumps(parsed, sort_keys=True, separators=(",", ":")):
                    errors.append("AUTHORITY_JSON_NOT_CANONICAL")
                if parsed != expected:
                    errors.append("AUTHORITY_VALUES_NOT_EXACT")
    return {
        "authority_prefix_occurrences": occurrences,
        "canonical_authority_lines": len(lines),
        "authority": authority,
        "errors": errors,
        "pass": not errors,
    }


def validate_execution_authorities(project_root: Path) -> dict[str, Any]:
    root = Path(project_root).absolute()
    records: dict[str, Any] = {}
    errors: list[str] = []
    for role, relative, prefix, expected in (
        (
            "deployment_review",
            "results/CODE_REVIEW.md",
            DEPLOYMENT_PREFIX,
            EXPECTED_DEPLOYMENT_AUTHORITY,
        ),
        (
            "result_review",
            "results/INDEPENDENT_RESULT_INTEGRITY.md",
            RESULT_PREFIX,
            EXPECTED_RESULT_AUTHORITY,
        ),
    ):
        path = root / relative
        if not regular_file(path):
            parsed = {"errors": ["REVIEW_MISSING_OR_UNSAFE"], "pass": False}
            digest = None
        else:
            raw = stable_file_bytes(path)
            parsed = _parse_exact_authority(raw.decode("utf-8"), prefix, expected)
            digest = hashlib.sha256(raw).hexdigest()
            expected_digest = IMMUTABLE_ARTIFACTS[relative][0]
            if digest != expected_digest:
                parsed["errors"].append("REVIEW_FILE_HASH_MISMATCH")
                parsed["pass"] = False
        records[role] = {
            "path": relative,
            "sha256": digest,
            **parsed,
        }
        if records[role].get("pass") is not True:
            errors.append(role.upper() + "_INVALID")
    return {
        "stage": "R118_IMMUTABLE_EXECUTION_AUTHORITIES",
        "records": records,
        "errors": errors,
        "pass": not errors,
    }


def analyzer_authority_payload(
    *, analyzer_sha256: str, analyzer_junit_sha256: str
) -> dict[str, Any]:
    return {
        "analyzer_junit_sha256": analyzer_junit_sha256,
        "analyzer_tree_sha256": analyzer_sha256,
        "candidate_id": CANDIDATE_ID,
        "execution_code_sha256": EXECUTION_TREE_SHA256,
        "registered_result_sha256": IMMUTABLE_ARTIFACTS[
            "results/EXPERIMENT_RESULTS.json"
        ][0],
        "result_review_sha256": IMMUTABLE_ARTIFACTS[
            "results/INDEPENDENT_RESULT_INTEGRITY.md"
        ][0],
        "reviewer_independent": True,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "verdict": "POSTRUN_ANALYZER_PASS",
    }


def parse_analyzer_authority_text(
    text: str,
    *,
    expected_analyzer_sha256: str,
    expected_junit_sha256: str,
) -> dict[str, Any]:
    expected = analyzer_authority_payload(
        analyzer_sha256=expected_analyzer_sha256,
        analyzer_junit_sha256=expected_junit_sha256,
    )
    if set(expected) != ANALYZER_AUTHORITY_KEYS:
        raise RuntimeError("internal analyzer authority schema mismatch")
    return _parse_exact_authority(text, ANALYZER_AUTHORITY_PREFIX, expected)


def validate_analyzer_authority(project_root: Path) -> dict[str, Any]:
    root = Path(project_root).absolute()
    try:
        analyzer_sha = analyzer_tree_sha256(root)
    except (OSError, RuntimeError, ValueError):
        analyzer_sha = None
    junit = parse_analyzer_junit(root / ANALYZER_JUNIT_PATH)
    junit_sha = junit.get("sha256")
    path = root / ANALYZER_REVIEW_PATH
    if analyzer_sha is None or junit.get("pass") is not True or type(junit_sha) is not str:
        return {
            "stage": "R122_INDEPENDENT_ANALYZER_REVIEW",
            "path": ANALYZER_REVIEW_PATH,
            "analyzer_tree_sha256": analyzer_sha,
            "analyzer_junit_sha256": junit_sha,
            "errors": ["ANALYZER_TREE_OR_JUNIT_NOT_FROZEN_PASSING"],
            "pass": False,
        }
    if not regular_file(path):
        return {
            "stage": "R122_INDEPENDENT_ANALYZER_REVIEW",
            "path": ANALYZER_REVIEW_PATH,
            "analyzer_tree_sha256": analyzer_sha,
            "analyzer_junit_sha256": junit_sha,
            "errors": ["ANALYZER_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    review_bytes = stable_file_bytes(path)
    parsed = parse_analyzer_authority_text(
        review_bytes.decode("utf-8"),
        expected_analyzer_sha256=analyzer_sha,
        expected_junit_sha256=junit_sha,
    )
    return {
        "stage": "R122_INDEPENDENT_ANALYZER_REVIEW",
        "path": ANALYZER_REVIEW_PATH,
        "review_file_sha256": hashlib.sha256(review_bytes).hexdigest(),
        "analyzer_tree_sha256": analyzer_sha,
        "analyzer_junit_sha256": junit_sha,
        **parsed,
    }
