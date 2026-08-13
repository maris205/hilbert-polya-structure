import json

from capacity_audit.protocol import CANDIDATE_ID, EXPECTED_LOCK_SHA256
from capacity_audit.review_gate import AUTHORITY_PREFIX, parse_review_authority_text


CODE_DIGEST = "a" * 64


def authority_line(**changes):
    payload = {
        "candidate_id": CANDIDATE_ID,
        "reviewed_code_sha256": CODE_DIGEST,
        "reviewer_independent": True,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "verdict": "DEPLOYMENT_PASS",
    }
    payload.update(changes)
    return AUTHORITY_PREFIX + json.dumps(payload, sort_keys=True)


def test_exact_column_one_review_authority_passes():
    text = "# Independent code review\n\n" + authority_line() + "\n"
    record = parse_review_authority_text(text, expected_code_sha256=CODE_DIGEST)
    assert record["pass"]


def test_duplicate_authority_occurrence_fails():
    line = authority_line()
    record = parse_review_authority_text(line + "\n" + line, expected_code_sha256=CODE_DIGEST)
    assert not record["pass"]
    assert "AUTHORITY_PREFIX_OCCURRENCE_COUNT_NOT_ONE" in record["errors"]


def test_indented_or_quoted_authority_fails():
    for prefix in ("  ", "> ", "- ", "\t"):
        record = parse_review_authority_text(prefix + authority_line(), expected_code_sha256=CODE_DIGEST)
        assert not record["pass"]
        assert "CANONICAL_COLUMN_ONE_AUTHORITY_LINE_COUNT_NOT_ONE" in record["errors"]


def test_stale_code_digest_fails():
    record = parse_review_authority_text(authority_line(), expected_code_sha256="b" * 64)
    assert not record["pass"]
    assert "REVIEWED_CODE_SHA256_MISMATCH" in record["errors"]


def test_extra_authority_key_fails():
    record = parse_review_authority_text(
        authority_line(comment="not canonical"),
        expected_code_sha256=CODE_DIGEST,
    )
    assert not record["pass"]
    assert "AUTHORITY_KEYS_NOT_EXACT" in record["errors"]


def test_duplicate_authority_json_key_fails():
    line = authority_line()
    duplicate = line.replace(
        '{"candidate_id":',
        '{"candidate_id":"WRONG","candidate_id":',
        1,
    )
    record = parse_review_authority_text(duplicate, expected_code_sha256=CODE_DIGEST)
    assert not record["pass"]
    assert "AUTHORITY_JSON_MALFORMED" in record["errors"]


def test_review_symlink_fails(tmp_path, monkeypatch):
    from capacity_audit.review_gate import validate_review_authority

    project = tmp_path / "project"
    (project / "results").mkdir(parents=True)
    outside = tmp_path / "outside.md"
    outside.write_text(authority_line(), encoding="utf-8")
    (project / "results" / "CODE_REVIEW.md").symlink_to(outside)
    monkeypatch.setattr(
        "capacity_audit.review_gate.reviewed_code_tree_sha256",
        lambda _: CODE_DIGEST,
    )
    record = validate_review_authority(project)
    assert not record["pass"]
    assert record["errors"] == ["CODE_REVIEW_NOT_REGULAR_IN_ROOT_FILE"]
