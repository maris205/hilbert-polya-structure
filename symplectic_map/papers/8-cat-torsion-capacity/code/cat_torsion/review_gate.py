"""Independent deployment authority bound to the frozen lock and exact code tree."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .protocol import (
    CANDIDATE_ID,
    EXPECTED_CODE_FILES,
    EXPECTED_EXECUTION_TREE_SHA256,
    EXPECTED_LOCK_SHA256,
    _raw_absolute,
    code_tree_inventory,
    regular_directory,
    regular_file,
    stable_file_bytes,
    strict_json_loads,
)


AUTHORITY_PREFIX = "CAT_TORSION_CODE_REVIEW_V1 "
AUTHORITY_KEYS = {
    "candidate_id",
    "reviewed_code_sha256",
    "reviewer_independent",
    "source_lock_sha256",
    "verdict",
}
POSTRUN_V1_AUTHORITY_PREFIX = "CAT_TORSION_POSTRUN_ANALYZER_REVIEW_V1 "
POSTRUN_AUTHORITY_PREFIX = "CAT_TORSION_POSTRUN_ANALYZER_REVIEW_V2 "
POSTRUN_V1_REVIEW_SHA256 = (
    "635e7dcd49440a41fd5f966c742b924f38428785ec21f4f7af549bca4f89f71b"
)
POSTRUN_V1_REVIEW_SIZE = 4825
POSTRUN_V1_AUTHORITY = {
    "analyzer_code_sha256": (
        "3434fc93bfcd1018c49f5df3adcb4728fb07173801f27ad06947e39121a2ce2f"
    ),
    "candidate_id": CANDIDATE_ID,
    "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
    "reviewer_independent": True,
    "source_lock_sha256": EXPECTED_LOCK_SHA256,
    "verdict": "POSTRUN_ANALYZER_FAIL",
}
POSTRUN_AUTHORITY_KEYS = {
    "analyzer_code_sha256",
    "candidate_id",
    "execution_code_sha256",
    "review_round",
    "reviewer_independent",
    "source_lock_sha256",
    "verdict",
}


def reviewed_code_tree_sha256(project_root: Path) -> str:
    """Hash the exact reviewed allowlist with stable path/content framing."""

    project_root = _raw_absolute(project_root)
    if not regular_directory(project_root):
        raise FileNotFoundError("project root is missing or has a symlink component")
    first_inventory = code_tree_inventory(project_root / "code")
    if first_inventory["pass"] is not True:
        raise FileNotFoundError("reviewed code tree is not the exact closed-world inventory")
    explicit = {
        "pyproject.toml",
        "experiments/source_lock.json",
        "experiments/EXPERIMENT_PLAN.md",
        "notes/PROOF_PACKAGE.md",
        "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
    }
    relative_paths = sorted(explicit | {f"code/{relative}" for relative in EXPECTED_CODE_FILES})
    paths = [project_root / relative for relative in relative_paths]
    if not paths or any(not regular_file(path) for path in paths):
        raise FileNotFoundError("one or more reviewed files are missing or unsafe")

    def hash_once() -> str:
        digest = hashlib.sha256()
        for relative_text, path in zip(relative_paths, paths, strict=True):
            relative = relative_text.encode("utf-8")
            content = stable_file_bytes(path)
            digest.update(len(relative).to_bytes(8, "big"))
            digest.update(relative)
            digest.update(len(content).to_bytes(8, "big"))
            digest.update(content)
        return digest.hexdigest()

    first_digest = hash_once()
    middle_inventory = code_tree_inventory(project_root / "code")
    second_digest = hash_once()
    final_inventory = code_tree_inventory(project_root / "code")
    stable_keys = ("source_files", "generated_files", "symlinks", "unsupported", "missing", "extra", "pass")
    if any(
        first_inventory[key] != middle_inventory[key]
        or middle_inventory[key] != final_inventory[key]
        for key in stable_keys
    ):
        raise RuntimeError("reviewed inventory changed during hashing")
    if first_digest != second_digest:
        raise RuntimeError("reviewed bytes changed during hashing")
    return first_digest


def parse_review_authority_text(
    text: str,
    *,
    expected_code_sha256: str,
    expected_lock_sha256: str = EXPECTED_LOCK_SHA256,
) -> dict[str, Any]:
    """Accept exactly one canonical column-one V1 authority marker."""

    occurrences = text.count(AUTHORITY_PREFIX)
    lines = [line for line in text.splitlines() if line.startswith(AUTHORITY_PREFIX)]
    errors: list[str] = []
    authority: dict[str, Any] | None = None
    if occurrences != 1:
        errors.append("AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE")
    if len(lines) != 1:
        errors.append("CANONICAL_COLUMN_ONE_AUTHORITY_LINE_COUNT_NOT_ONE")
    if not errors:
        raw = lines[0][len(AUTHORITY_PREFIX) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError):
            errors.append("AUTHORITY_JSON_MALFORMED")
        else:
            if type(parsed) is not dict:
                errors.append("AUTHORITY_JSON_NOT_OBJECT")
            elif set(parsed) != AUTHORITY_KEYS:
                errors.append("AUTHORITY_KEYS_NOT_EXACT")
            else:
                authority = parsed
                if raw != json.dumps(parsed, sort_keys=True, separators=(",", ":")):
                    errors.append("AUTHORITY_JSON_NOT_CANONICAL")
                if parsed["candidate_id"] != CANDIDATE_ID:
                    errors.append("CANDIDATE_ID_MISMATCH")
                if parsed["reviewed_code_sha256"] != expected_code_sha256:
                    errors.append("REVIEWED_CODE_SHA256_MISMATCH")
                if parsed["reviewer_independent"] is not True:
                    errors.append("REVIEWER_NOT_INDEPENDENT")
                if parsed["source_lock_sha256"] != expected_lock_sha256:
                    errors.append("SOURCE_LOCK_SHA256_MISMATCH")
                if parsed["verdict"] != "DEPLOYMENT_PASS":
                    errors.append("VERDICT_NOT_DEPLOYMENT_PASS")
    return {
        "authority_prefix_occurrences": occurrences,
        "canonical_authority_lines": len(lines),
        "authority": authority,
        "errors": errors,
        "pass": not errors,
    }


def validate_review_authority(project_root: Path) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    code_digest = reviewed_code_tree_sha256(project_root)
    review_path = project_root / "results" / "CODE_REVIEW.md"
    if not regular_file(review_path):
        return {
            "stage": "P3_INDEPENDENT_REVIEW",
            "review_path": "results/CODE_REVIEW.md",
            "reviewed_code_sha256": code_digest,
            "errors": ["CODE_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    parsed = parse_review_authority_text(
        stable_file_bytes(review_path).decode("utf-8"), expected_code_sha256=code_digest
    )
    return {
        "stage": "P3_INDEPENDENT_REVIEW",
        "review_path": "results/CODE_REVIEW.md",
        "reviewed_code_sha256": code_digest,
        **parsed,
    }


def validate_execution_review_authority(project_root: Path) -> dict[str, Any]:
    """Validate the immutable execution review against the execution tree, not analyzer code."""

    project_root = _raw_absolute(project_root)
    review_path = project_root / "results" / "CODE_REVIEW.md"
    if not regular_file(review_path):
        return {
            "stage": "P3_IMMUTABLE_EXECUTION_REVIEW",
            "review_path": "results/CODE_REVIEW.md",
            "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
            "errors": ["EXECUTION_CODE_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    review_bytes = stable_file_bytes(review_path)
    parsed = parse_review_authority_text(
        review_bytes.decode("utf-8"),
        expected_code_sha256=EXPECTED_EXECUTION_TREE_SHA256,
    )
    return {
        "stage": "P3_IMMUTABLE_EXECUTION_REVIEW",
        "review_path": "results/CODE_REVIEW.md",
        "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "review_file_sha256": hashlib.sha256(review_bytes).hexdigest(),
        **parsed,
    }


def parse_postrun_analyzer_authority_text(
    text: str,
    *,
    expected_analyzer_sha256: str,
    expected_execution_sha256: str = EXPECTED_EXECUTION_TREE_SHA256,
    expected_lock_sha256: str = EXPECTED_LOCK_SHA256,
) -> dict[str, Any]:
    """Require the byte-exact V1 FAIL history and one canonical round-2 authority."""

    encoded = text.encode("utf-8")
    historical_prefix = encoded[:POSTRUN_V1_REVIEW_SIZE]
    history_occurrences = text.count(POSTRUN_V1_AUTHORITY_PREFIX)
    history_lines = [
        line for line in text.splitlines() if line.startswith(POSTRUN_V1_AUTHORITY_PREFIX)
    ]
    occurrences = text.count(POSTRUN_AUTHORITY_PREFIX)
    lines = [line for line in text.splitlines() if line.startswith(POSTRUN_AUTHORITY_PREFIX)]
    errors: list[str] = []
    historical_authority: dict[str, Any] | None = None
    authority: dict[str, Any] | None = None
    if (
        len(encoded) < POSTRUN_V1_REVIEW_SIZE
        or hashlib.sha256(historical_prefix).hexdigest() != POSTRUN_V1_REVIEW_SHA256
    ):
        errors.append("POSTRUN_V1_REVIEW_HISTORY_NOT_BYTE_EXACT")
    if history_occurrences != 1 or len(history_lines) != 1:
        errors.append("POSTRUN_V1_FAIL_AUTHORITY_COUNT_NOT_ONE")
    else:
        history_raw = history_lines[0][len(POSTRUN_V1_AUTHORITY_PREFIX) :]
        try:
            history_parsed = strict_json_loads(history_raw)
        except (json.JSONDecodeError, ValueError):
            errors.append("POSTRUN_V1_FAIL_AUTHORITY_JSON_MALFORMED")
        else:
            if (
                type(history_parsed) is not dict
                or history_parsed != POSTRUN_V1_AUTHORITY
                or history_raw
                != json.dumps(history_parsed, sort_keys=True, separators=(",", ":"))
            ):
                errors.append("POSTRUN_V1_FAIL_AUTHORITY_NOT_EXACT")
            else:
                historical_authority = history_parsed
    if occurrences != 1:
        errors.append("POSTRUN_AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE")
    if len(lines) != 1:
        errors.append("POSTRUN_CANONICAL_AUTHORITY_LINE_COUNT_NOT_ONE")
    if not errors:
        raw = lines[0][len(POSTRUN_AUTHORITY_PREFIX) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, ValueError):
            errors.append("POSTRUN_AUTHORITY_JSON_MALFORMED")
        else:
            if type(parsed) is not dict:
                errors.append("POSTRUN_AUTHORITY_JSON_NOT_OBJECT")
            elif set(parsed) != POSTRUN_AUTHORITY_KEYS:
                errors.append("POSTRUN_AUTHORITY_KEYS_NOT_EXACT")
            else:
                authority = parsed
                if raw != json.dumps(parsed, sort_keys=True, separators=(",", ":")):
                    errors.append("POSTRUN_AUTHORITY_JSON_NOT_CANONICAL")
                if parsed["candidate_id"] != CANDIDATE_ID:
                    errors.append("POSTRUN_CANDIDATE_ID_MISMATCH")
                if parsed["execution_code_sha256"] != expected_execution_sha256:
                    errors.append("POSTRUN_EXECUTION_TREE_SHA256_MISMATCH")
                if parsed["analyzer_code_sha256"] != expected_analyzer_sha256:
                    errors.append("POSTRUN_ANALYZER_TREE_SHA256_MISMATCH")
                if type(parsed["review_round"]) is not int or parsed["review_round"] != 2:
                    errors.append("POSTRUN_REVIEW_ROUND_NOT_TWO")
                if parsed["reviewer_independent"] is not True:
                    errors.append("POSTRUN_REVIEWER_NOT_INDEPENDENT")
                if parsed["source_lock_sha256"] != expected_lock_sha256:
                    errors.append("POSTRUN_SOURCE_LOCK_SHA256_MISMATCH")
                if parsed["verdict"] != "POSTRUN_ANALYZER_PASS":
                    errors.append("POSTRUN_VERDICT_NOT_PASS")
    return {
        "historical_v1_authority_prefix_occurrences": history_occurrences,
        "historical_v1_canonical_authority_lines": len(history_lines),
        "historical_v1_authority": historical_authority,
        "historical_v1_review_sha256": hashlib.sha256(historical_prefix).hexdigest(),
        "authority_prefix_occurrences": occurrences,
        "canonical_authority_lines": len(lines),
        "authority": authority,
        "errors": errors,
        "pass": not errors,
    }


def validate_postrun_analyzer_authority(project_root: Path) -> dict[str, Any]:
    """Validate an independent review bound to both execution and analyzer trees."""

    project_root = _raw_absolute(project_root)
    analyzer_digest = reviewed_code_tree_sha256(project_root)
    review_path = project_root / "results" / "POSTRUN_ANALYZER_REVIEW.md"
    if not regular_file(review_path):
        return {
            "stage": "R095_POSTRUN_ANALYZER_REVIEW",
            "review_path": "results/POSTRUN_ANALYZER_REVIEW.md",
            "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
            "analyzer_code_sha256": analyzer_digest,
            "errors": ["POSTRUN_ANALYZER_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    review_bytes = stable_file_bytes(review_path)
    parsed = parse_postrun_analyzer_authority_text(
        review_bytes.decode("utf-8"),
        expected_analyzer_sha256=analyzer_digest,
    )
    return {
        "stage": "R095_POSTRUN_ANALYZER_REVIEW",
        "review_path": "results/POSTRUN_ANALYZER_REVIEW.md",
        "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "analyzer_code_sha256": analyzer_digest,
        "review_file_sha256": hashlib.sha256(review_bytes).hexdigest(),
        **parsed,
    }
