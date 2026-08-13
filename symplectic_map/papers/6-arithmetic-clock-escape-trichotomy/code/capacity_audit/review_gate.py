"""Fail-closed independent code-review authority and code-tree binding."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    DuplicateJSONKeyError,
    regular_file_within,
    strict_json_loads,
)


AUTHORITY_PREFIX = "CAPACITY_AUDIT_CODE_REVIEW_V1 "
AUTHORITY_KEYS = {
    "candidate_id",
    "reviewed_code_sha256",
    "reviewer_independent",
    "source_lock_sha256",
    "verdict",
}


def reviewed_code_tree_sha256(project_root: Path) -> str:
    """Hash every pre-review implementation, test, and machine-ledger file."""

    project_root = project_root.resolve()
    explicit = [
        project_root / "pyproject.toml",
        project_root / "code" / "README.md",
        project_root / "experiments" / "source_lock.json",
        project_root / "experiments" / "EXPERIMENT_PLAN.md",
        project_root / "experiments" / "proof_ledger.json",
        project_root / "experiments" / "scope_ledger.json",
        project_root / "notes" / "RESEARCH_QUESTION.md",
        project_root / "notes" / "PROOF_PACKAGE.md",
        project_root / "notes" / "PROOF_SKETCH.md",
        project_root / "notes" / "NOVELTY_AUDIT_DRAFT.md",
        project_root / "notes" / "INDEPENDENT_PROOF_NOVELTY_REVIEW.md",
    ]
    discovered = [
        path
        for path in (project_root / "code").rglob("*.py")
        if "__pycache__" not in path.parts
    ]
    paths = sorted({path.resolve() for path in explicit + discovered})
    if not paths or any(not path.is_file() for path in paths):
        raise FileNotFoundError("reviewed code-tree input is missing")

    digest = hashlib.sha256()
    for path in paths:
        relative = path.relative_to(project_root).as_posix().encode("utf-8")
        content = path.read_bytes()
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def parse_review_authority_text(
    text: str,
    *,
    expected_code_sha256: str,
    expected_lock_sha256: str = EXPECTED_LOCK_SHA256,
) -> dict[str, Any]:
    """Parse exactly one column-one authority occurrence.

    Any second occurrence, including a quoted, indented, bulleted, or prose
    mention of the prefix, fails closed.  This prevents hidden or legacy marker
    forms from becoming deployment authority.
    """

    occurrence_count = text.count(AUTHORITY_PREFIX)
    canonical_lines = [line for line in text.splitlines() if line.startswith(AUTHORITY_PREFIX)]
    errors: list[str] = []
    authority: dict[str, Any] | None = None

    if occurrence_count != 1:
        errors.append("AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE")
    if len(canonical_lines) != 1:
        errors.append("CANONICAL_COLUMN_ONE_AUTHORITY_LINE_COUNT_NOT_ONE")

    if not errors:
        raw_json = canonical_lines[0][len(AUTHORITY_PREFIX) :]
        try:
            parsed = strict_json_loads(raw_json)
        except (json.JSONDecodeError, DuplicateJSONKeyError):
            errors.append("AUTHORITY_JSON_MALFORMED")
        else:
            if not isinstance(parsed, dict):
                errors.append("AUTHORITY_JSON_NOT_OBJECT")
            elif set(parsed) != AUTHORITY_KEYS:
                errors.append("AUTHORITY_KEYS_NOT_EXACT")
            else:
                authority = parsed
                if authority["candidate_id"] != CANDIDATE_ID:
                    errors.append("CANDIDATE_ID_MISMATCH")
                if authority["source_lock_sha256"] != expected_lock_sha256:
                    errors.append("SOURCE_LOCK_SHA256_MISMATCH")
                if authority["reviewed_code_sha256"] != expected_code_sha256:
                    errors.append("REVIEWED_CODE_SHA256_MISMATCH")
                if authority["reviewer_independent"] is not True:
                    errors.append("REVIEWER_NOT_INDEPENDENT")
                if authority["verdict"] != "DEPLOYMENT_PASS":
                    errors.append("VERDICT_NOT_DEPLOYMENT_PASS")

    return {
        "authority_prefix_occurrences": occurrence_count,
        "canonical_authority_lines": len(canonical_lines),
        "authority": authority,
        "errors": errors,
        "pass": not errors,
    }


def validate_review_authority(project_root: Path) -> dict[str, Any]:
    """Validate the review file against the current immutable code tree."""

    project_root = project_root.resolve()
    review_path = project_root / "results" / "CODE_REVIEW.md"
    code_digest = reviewed_code_tree_sha256(project_root)
    if not review_path.exists():
        return {
            "gate_id": "G090",
            "review_path": str(review_path),
            "reviewed_code_sha256": code_digest,
            "errors": ["CODE_REVIEW_MISSING"],
            "pass": False,
        }
    if not regular_file_within(project_root, review_path):
        return {
            "gate_id": "G090",
            "review_path": str(review_path),
            "reviewed_code_sha256": code_digest,
            "errors": ["CODE_REVIEW_NOT_REGULAR_IN_ROOT_FILE"],
            "pass": False,
        }

    parsed = parse_review_authority_text(
        review_path.read_text(encoding="utf-8"),
        expected_code_sha256=code_digest,
    )
    return {
        "gate_id": "G090",
        "review_path": str(review_path),
        "reviewed_code_sha256": code_digest,
        **parsed,
    }
