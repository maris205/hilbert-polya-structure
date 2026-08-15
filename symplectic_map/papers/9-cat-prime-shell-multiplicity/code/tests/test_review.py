from __future__ import annotations

import json
from pathlib import Path

from prime_shell.constants import CANDIDATE_ID, SOURCE_LOCK_SHA256
from prime_shell.protocol import DuplicateJSONKeyError, strict_json_loads
from prime_shell.review import (
    DEPLOYMENT_PREFIX,
    ROUND1_REVIEW_SHA256,
    ROUND2_REVIEW_SHA256,
    ROUND3_REVIEW_SHA256,
    ROUND3_REVIEW_SIZE,
    parse_deployment_authority,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def review_history() -> str:
    raw = (PROJECT_ROOT / "results" / "CODE_REVIEW.md").read_bytes()
    assert len(raw) >= ROUND3_REVIEW_SIZE
    return raw[:ROUND3_REVIEW_SIZE].decode("utf-8")


def test_duplicate_authority_and_duplicate_json_fail_closed() -> None:
    authority = {
        "candidate_id": CANDIDATE_ID,
        "review_round": 4,
        "reviewed_code_sha256": "a" * 64,
        "reviewer_independent": True,
        "round1_review_sha256": ROUND1_REVIEW_SHA256,
        "round2_review_sha256": ROUND2_REVIEW_SHA256,
        "round3_review_sha256": ROUND3_REVIEW_SHA256,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "test_evidence_sha256": "b" * 64,
        "verdict": "DEPLOYMENT_PASS",
    }
    line = DEPLOYMENT_PREFIX + json.dumps(authority, sort_keys=True, separators=(",", ":"))
    duplicate = parse_deployment_authority(
        review_history() + "\n" + line + "\n" + line,
        code_sha256="a" * 64,
        test_sha256="b" * 64,
    )
    assert duplicate["pass"] is False
    assert "AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE" in duplicate["errors"]
    try:
        strict_json_loads('{"verdict":"DEPLOYMENT_PASS","verdict":"FAIL"}')
    except DuplicateJSONKeyError:
        pass
    else:
        raise AssertionError("duplicate exact authority JSON was accepted")


def test_deployment_authority_requires_exact_hashes_and_canonical_json() -> None:
    text = DEPLOYMENT_PREFIX + json.dumps(
        {
            "candidate_id": CANDIDATE_ID,
            "review_round": 4,
            "reviewed_code_sha256": "a" * 64,
            "reviewer_independent": True,
            "round1_review_sha256": ROUND1_REVIEW_SHA256,
            "round2_review_sha256": ROUND2_REVIEW_SHA256,
            "round3_review_sha256": ROUND3_REVIEW_SHA256,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "test_evidence_sha256": "b" * 64,
            "verdict": "DEPLOYMENT_PASS",
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    full_text = review_history() + "\n" + text
    assert parse_deployment_authority(
        full_text, code_sha256="a" * 64, test_sha256="b" * 64
    )["pass"] is True
    assert parse_deployment_authority(
        full_text, code_sha256="c" * 64, test_sha256="b" * 64
    )["pass"] is False
