import json
from pathlib import Path

from base2_clock.protocol import CANDIDATE_ID, EXPECTED_LOCK_SHA256
from base2_clock.review_gate import (
    AUTHORITY_PREFIX,
    LEGACY_AUTHORITY_PREFIX,
    ROUND2_AUTHORITY_PREFIX,
    ROUND3_AUTHORITY_PREFIX,
    parse_review_authority_text,
    reviewed_code_tree_sha256,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]
CODE_DIGEST = "a" * 64


def _authority(
    *,
    round2_verdict="DEPLOYMENT_FAIL",
    round3_verdict="DEPLOYMENT_FAIL",
    **changes,
):
    payload = {
        "candidate_id": CANDIDATE_ID,
        "review_round": 4,
        "reviewed_code_sha256": CODE_DIGEST,
        "reviewer_independent": True,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "verdict": "DEPLOYMENT_PASS",
    }
    payload.update(changes)
    legacy = LEGACY_AUTHORITY_PREFIX + json.dumps(
        {
            "candidate_id": CANDIDATE_ID,
            "reviewed_code_sha256": (
                "bb648aa54d98b27df71ab849b7515312003d45898aefe9186f114739c1f3eb07"
            ),
            "reviewer_independent": True,
            "source_lock_sha256": EXPECTED_LOCK_SHA256,
            "verdict": "FAIL",
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    round2 = ROUND2_AUTHORITY_PREFIX + json.dumps(
        {
            "candidate_id": CANDIDATE_ID,
            "review_round": 2,
            "reviewed_code_sha256": (
                "8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37"
            ),
            "reviewer_independent": True,
            "source_lock_sha256": EXPECTED_LOCK_SHA256,
            "verdict": round2_verdict,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    round3 = ROUND3_AUTHORITY_PREFIX + json.dumps(
        {
            "candidate_id": CANDIDATE_ID,
            "review_round": 3,
            "reviewed_code_sha256": (
                "dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4"
            ),
            "reviewer_independent": True,
            "source_lock_sha256": EXPECTED_LOCK_SHA256,
            "verdict": round3_verdict,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    current = AUTHORITY_PREFIX + json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    )
    return legacy + "\n" + round2 + "\n" + round3 + "\n" + current


def test_canonical_authority_passes_and_stale_digest_fails():
    assert parse_review_authority_text(
        _authority(), expected_code_sha256=CODE_DIGEST
    )["pass"] is True
    stale = parse_review_authority_text(_authority(), expected_code_sha256="b" * 64)
    assert stale["pass"] is False
    assert "REVIEWED_CODE_SHA256_MISMATCH" in stale["errors"]


def test_duplicate_or_indented_authority_fails_closed():
    line = _authority()
    assert parse_review_authority_text(
        line + "\n" + line, expected_code_sha256=CODE_DIGEST
    )["pass"] is False
    assert parse_review_authority_text(
        "> " + line, expected_code_sha256=CODE_DIGEST
    )["pass"] is False


def test_tampered_round2_failure_history_fails_closed():
    tampered = _authority(round2_verdict="DEPLOYMENT_PASS")
    record = parse_review_authority_text(
        tampered, expected_code_sha256=CODE_DIGEST
    )
    assert record["pass"] is False
    assert "HISTORICAL_V2_FAIL_BINDING_NOT_EXACT" in record["errors"]


def test_tampered_round3_failure_history_fails_closed():
    record = parse_review_authority_text(
        _authority(round3_verdict="DEPLOYMENT_PASS"),
        expected_code_sha256=CODE_DIGEST,
    )
    assert record["pass"] is False
    assert "HISTORICAL_V3_FAIL_BINDING_NOT_EXACT" in record["errors"]


def test_missing_and_legacy_review_authorities_do_not_satisfy_v4_gate():
    missing = parse_review_authority_text("", expected_code_sha256=CODE_DIGEST)
    assert missing["pass"] is False
    legacy = LEGACY_AUTHORITY_PREFIX + json.dumps(
        {
            "candidate_id": CANDIDATE_ID,
            "reviewed_code_sha256": CODE_DIGEST,
            "reviewer_independent": True,
            "source_lock_sha256": EXPECTED_LOCK_SHA256,
            "verdict": "FAIL",
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    parsed = parse_review_authority_text(legacy, expected_code_sha256=CODE_DIGEST)
    assert parsed["pass"] is False
    assert parsed["legacy_authority_prefix_occurrences"] == 1


def test_live_reviewed_tree_has_a_stable_sha256_shape():
    digest = reviewed_code_tree_sha256(PROJECT_ROOT)
    assert len(digest) == 64
    assert all(character in "0123456789abcdef" for character in digest)
