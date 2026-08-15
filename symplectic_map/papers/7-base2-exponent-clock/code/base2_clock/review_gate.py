"""Independent pre-execution authority bound to the v2 lock and code tree."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .protocol import (
    CANDIDATE_ID,
    EXPECTED_CODE_FILES,
    EXPECTED_LOCK_SHA256,
    DuplicateJSONKeyError,
    _raw_absolute,
    code_tree_inventory,
    regular_file,
    regular_directory,
    stable_file_bytes,
    strict_json_loads,
)


LEGACY_AUTHORITY_PREFIX = "BASE2_CLOCK_CODE_REVIEW_V1 "
ROUND2_AUTHORITY_PREFIX = "BASE2_CLOCK_CODE_REVIEW_V2 "
ROUND3_AUTHORITY_PREFIX = "BASE2_CLOCK_CODE_REVIEW_V3 "
AUTHORITY_PREFIX = "BASE2_CLOCK_CODE_REVIEW_V4 "
AUTHORITY_KEYS = {
    "candidate_id",
    "review_round",
    "reviewed_code_sha256",
    "reviewer_independent",
    "source_lock_sha256",
    "verdict",
}
LEGACY_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "reviewed_code_sha256": "bb648aa54d98b27df71ab849b7515312003d45898aefe9186f114739c1f3eb07",
    "reviewer_independent": True,
    "source_lock_sha256": EXPECTED_LOCK_SHA256,
    "verdict": "FAIL",
}
ROUND2_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "review_round": 2,
    "reviewed_code_sha256": "8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37",
    "reviewer_independent": True,
    "source_lock_sha256": EXPECTED_LOCK_SHA256,
    "verdict": "DEPLOYMENT_FAIL",
}
ROUND3_AUTHORITY = {
    "candidate_id": CANDIDATE_ID,
    "review_round": 3,
    "reviewed_code_sha256": "dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4",
    "reviewer_independent": True,
    "source_lock_sha256": EXPECTED_LOCK_SHA256,
    "verdict": "DEPLOYMENT_FAIL",
}


def reviewed_code_tree_sha256(project_root: Path) -> str:
    """Hash every scientific source, implementation, script, and test under review."""

    project_root = _raw_absolute(project_root)
    if not regular_directory(project_root):
        raise FileNotFoundError("reviewed project root is missing or unsafe")
    first_inventory = code_tree_inventory(project_root / "code")
    if not first_inventory["pass"]:
        raise FileNotFoundError("reviewed code tree is not the exact closed-world inventory")
    explicit_relative = {
        "pyproject.toml",
        "experiments/source_lock.json",
        "experiments/EXPERIMENT_PLAN.md",
        "notes/PROOF_PACKAGE.md",
        "notes/SOURCE_LOCK_AUDIT.md",
    }
    relative_paths = sorted(explicit_relative | {f"code/{item}" for item in EXPECTED_CODE_FILES})
    paths = [project_root / relative for relative in relative_paths]
    if not paths or any(not regular_file(path) for path in paths):
        raise FileNotFoundError("reviewed code-tree input is missing or unsafe")
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
    stable_keys = ("source_files", "symlinks", "unsupported", "missing", "extra", "pass")
    if any(
        first_inventory[key] != middle_inventory[key]
        or middle_inventory[key] != final_inventory[key]
        for key in stable_keys
    ):
        raise RuntimeError("reviewed code inventory changed during hashing")
    if first_digest != second_digest:
        raise RuntimeError("reviewed file bytes changed during hashing")
    return first_digest


def parse_review_authority_text(
    text: str,
    *,
    expected_code_sha256: str,
    expected_lock_sha256: str = EXPECTED_LOCK_SHA256,
) -> dict[str, Any]:
    """Accept one and only one canonical column-one authority marker."""

    occurrences = text.count(AUTHORITY_PREFIX)
    legacy_occurrences = text.count(LEGACY_AUTHORITY_PREFIX)
    round2_occurrences = text.count(ROUND2_AUTHORITY_PREFIX)
    round3_occurrences = text.count(ROUND3_AUTHORITY_PREFIX)
    lines = [line for line in text.splitlines() if line.startswith(AUTHORITY_PREFIX)]
    legacy_lines = [
        line for line in text.splitlines() if line.startswith(LEGACY_AUTHORITY_PREFIX)
    ]
    round2_lines = [
        line for line in text.splitlines() if line.startswith(ROUND2_AUTHORITY_PREFIX)
    ]
    round3_lines = [
        line for line in text.splitlines() if line.startswith(ROUND3_AUTHORITY_PREFIX)
    ]
    errors: list[str] = []
    authority: dict[str, Any] | None = None
    canonical_legacy = LEGACY_AUTHORITY_PREFIX + json.dumps(
        LEGACY_AUTHORITY, sort_keys=True, separators=(",", ":")
    )
    if legacy_occurrences != 1 or len(legacy_lines) != 1:
        errors.append("HISTORICAL_V1_AUTHORITY_COUNT_NOT_ONE")
    elif legacy_lines[0] != canonical_legacy:
        errors.append("HISTORICAL_V1_FAIL_BINDING_NOT_EXACT")
    canonical_round2 = ROUND2_AUTHORITY_PREFIX + json.dumps(
        ROUND2_AUTHORITY, sort_keys=True, separators=(",", ":")
    )
    if round2_occurrences != 1 or len(round2_lines) != 1:
        errors.append("HISTORICAL_V2_AUTHORITY_COUNT_NOT_ONE")
    elif round2_lines[0] != canonical_round2:
        errors.append("HISTORICAL_V2_FAIL_BINDING_NOT_EXACT")
    canonical_round3 = ROUND3_AUTHORITY_PREFIX + json.dumps(
        ROUND3_AUTHORITY, sort_keys=True, separators=(",", ":")
    )
    if round3_occurrences != 1 or len(round3_lines) != 1:
        errors.append("HISTORICAL_V3_AUTHORITY_COUNT_NOT_ONE")
    elif round3_lines[0] != canonical_round3:
        errors.append("HISTORICAL_V3_FAIL_BINDING_NOT_EXACT")
    if occurrences != 1:
        errors.append("AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE")
    if len(lines) != 1:
        errors.append("CANONICAL_COLUMN_ONE_AUTHORITY_LINE_COUNT_NOT_ONE")
    if not errors:
        raw = lines[0][len(AUTHORITY_PREFIX) :]
        try:
            parsed = strict_json_loads(raw)
        except (json.JSONDecodeError, DuplicateJSONKeyError):
            errors.append("AUTHORITY_JSON_MALFORMED")
        else:
            if type(parsed) is not dict:
                errors.append("AUTHORITY_JSON_NOT_OBJECT")
            elif set(parsed) != AUTHORITY_KEYS:
                errors.append("AUTHORITY_KEYS_NOT_EXACT")
            else:
                authority = parsed
                canonical_current = json.dumps(
                    authority, sort_keys=True, separators=(",", ":")
                )
                if raw != canonical_current:
                    errors.append("AUTHORITY_JSON_NOT_CANONICAL")
                if authority["candidate_id"] != CANDIDATE_ID:
                    errors.append("CANDIDATE_ID_MISMATCH")
                if type(authority["review_round"]) is not int or authority["review_round"] != 4:
                    errors.append("REVIEW_ROUND_NOT_FOUR")
                if authority["source_lock_sha256"] != expected_lock_sha256:
                    errors.append("SOURCE_LOCK_SHA256_MISMATCH")
                if authority["reviewed_code_sha256"] != expected_code_sha256:
                    errors.append("REVIEWED_CODE_SHA256_MISMATCH")
                if authority["reviewer_independent"] is not True:
                    errors.append("REVIEWER_NOT_INDEPENDENT")
                if authority["verdict"] != "DEPLOYMENT_PASS":
                    errors.append("VERDICT_NOT_DEPLOYMENT_PASS")
    return {
        "authority_prefix_occurrences": occurrences,
        "legacy_authority_prefix_occurrences": legacy_occurrences,
        "round2_authority_prefix_occurrences": round2_occurrences,
        "round3_authority_prefix_occurrences": round3_occurrences,
        "canonical_legacy_authority_lines": len(legacy_lines),
        "canonical_round2_authority_lines": len(round2_lines),
        "canonical_round3_authority_lines": len(round3_lines),
        "canonical_authority_lines": len(lines),
        "authority": authority,
        "errors": errors,
        "pass": not errors,
    }


def validate_review_authority(project_root: Path) -> dict[str, Any]:
    """Fail closed until an independent review matches the current digest."""

    project_root = _raw_absolute(project_root)
    review_path = project_root / "results" / "CODE_REVIEW.md"
    code_digest = reviewed_code_tree_sha256(project_root)
    if not regular_file(review_path):
        return {
            "stage": "P3_INDEPENDENT_REVIEW",
            "review_path": "results/CODE_REVIEW.md",
            "reviewed_code_sha256": code_digest,
            "errors": ["CODE_REVIEW_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    parsed = parse_review_authority_text(
        stable_file_bytes(review_path).decode("utf-8"),
        expected_code_sha256=code_digest,
    )
    return {
        "stage": "P3_INDEPENDENT_REVIEW",
        "review_path": "results/CODE_REVIEW.md",
        "reviewed_code_sha256": code_digest,
        **parsed,
    }
