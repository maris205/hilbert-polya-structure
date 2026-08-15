import json
from pathlib import Path

from equivariant_clock.constants import CANDIDATE_ID, SOURCE_LOCK_SHA256, SOURCE_REVIEW_R2_SHA256
from equivariant_clock.protocol import stable_file_bytes
from equivariant_clock.review import (
    DEPLOYMENT_PREFIX,
    ROUND1_REVIEW_SHA256,
    ROUND1_REVIEW_SIZE,
    parse_deployment_authority,
)


def test_deployment_authority_is_hash_bound_and_duplicate_safe() -> None:
    code_sha = "c" * 64
    test_sha = "t" * 64
    authority = {
        "candidate_id": CANDIDATE_ID,
        "review_round": 2,
        "reviewed_code_sha256": code_sha,
        "reviewer_independent": True,
        "round1_review_sha256": ROUND1_REVIEW_SHA256,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_R2_SHA256,
        "test_evidence_sha256": test_sha,
        "verdict": "DEPLOYMENT_PASS",
    }
    line = DEPLOYMENT_PREFIX + json.dumps(authority, sort_keys=True, separators=(",", ":"))
    review_path = Path(__file__).parents[2] / "results" / "CODE_REVIEW.md"
    history = stable_file_bytes(review_path)[:ROUND1_REVIEW_SIZE].decode("utf-8")
    text = history + "\n\n" + line + "\n"
    assert parse_deployment_authority(text, code_sha256=code_sha, test_sha256=test_sha)["pass"]
    assert not parse_deployment_authority(text + line + "\n", code_sha256=code_sha, test_sha256=test_sha)["pass"]
    assert not parse_deployment_authority(text, code_sha256="d" * 64, test_sha256=test_sha)["pass"]
