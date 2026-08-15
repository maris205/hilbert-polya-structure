from __future__ import annotations

import json
from pathlib import Path

import pytest

from cat_torsion.cli import build_parser
from cat_torsion.lifecycle import claim_registered_run, validate_registered_claim
from cat_torsion.protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    stable_file_bytes,
    write_json,
)
from cat_torsion.review_gate import (
    AUTHORITY_PREFIX,
    POSTRUN_AUTHORITY_PREFIX,
    parse_postrun_analyzer_authority_text,
    parse_review_authority_text,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def _authority(code_hash: str) -> str:
    payload = {
        "candidate_id": CANDIDATE_ID,
        "reviewed_code_sha256": code_hash,
        "reviewer_independent": True,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "verdict": "DEPLOYMENT_PASS",
    }
    return AUTHORITY_PREFIX + json.dumps(payload, sort_keys=True, separators=(",", ":"))


def test_review_authority_is_exact_canonical_and_stale_closed():
    code_hash = "a" * 64
    marker = _authority(code_hash)
    assert parse_review_authority_text(marker, expected_code_sha256=code_hash)["pass"] is True
    assert parse_review_authority_text(marker, expected_code_sha256="b" * 64)["pass"] is False
    assert parse_review_authority_text(marker + "\n" + marker, expected_code_sha256=code_hash)[
        "pass"
    ] is False
    noncanonical = " " + marker
    assert parse_review_authority_text(noncanonical, expected_code_sha256=code_hash)["pass"] is False


def test_registered_claim_is_one_shot(tmp_path):
    project = tmp_path / "paper"
    results = project / "results"
    results.mkdir(parents=True)
    (results / "CODE_REVIEW.md").write_text("isolated test authority", encoding="utf-8")
    write_json(results / "PRE_EXECUTION_AUDIT.json", {"safe": True})
    code_hash = "c" * 64
    claim_registered_run(project, code_hash)
    assert validate_registered_claim(project, code_hash, require_clean_started=True)["pass"] is True
    with pytest.raises(FileExistsError):
        claim_registered_run(project, code_hash)


def test_fixed_cli_has_no_scientific_overrides():
    parser = build_parser()
    args = parser.parse_args(["registered"])
    assert args.command == "registered"
    assert not hasattr(args, "period")
    assert not hasattr(args, "matrix")
    for option in ("--period", "--cutoff", "--matrix", "--prime", "--trace", "--factor"):
        with pytest.raises(SystemExit):
            parser.parse_args(["registered", option, "13"])


def test_postrun_analyzer_authority_is_stale_closed():
    analyzer_hash = "d" * 64
    payload = {
        "analyzer_code_sha256": analyzer_hash,
        "candidate_id": CANDIDATE_ID,
        "execution_code_sha256": "b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059",
        "review_round": 2,
        "reviewer_independent": True,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "verdict": "POSTRUN_ANALYZER_PASS",
    }
    marker = POSTRUN_AUTHORITY_PREFIX + json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    )
    history = stable_file_bytes(
        PROJECT_ROOT / "results" / "POSTRUN_ANALYZER_REVIEW.md"
    ).decode("utf-8")
    text = history + "\n" + marker
    assert parse_postrun_analyzer_authority_text(
        text, expected_analyzer_sha256=analyzer_hash
    )["pass"] is True
    assert parse_postrun_analyzer_authority_text(
        text, expected_analyzer_sha256="e" * 64
    )["pass"] is False
    assert parse_postrun_analyzer_authority_text(
        text + "\n" + marker, expected_analyzer_sha256=analyzer_hash
    )["pass"] is False
    assert parse_postrun_analyzer_authority_text(
        "X" + history[1:] + "\n" + marker,
        expected_analyzer_sha256=analyzer_hash,
    )["pass"] is False
