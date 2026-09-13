"""Recoverable temporary one-shot lifecycle tests; never touches project runtime."""

from __future__ import annotations

import pytest

from bootstrap.constants import TERMINAL_FAILURE
from bootstrap.lifecycle import commit_result, terminalize
from bootstrap.protocol import write_json_exclusive


def _temporary_claim():
    return {
        "schema": "TEMP_CLAIM",
        "candidate_id": "henon_period3_residue_v1",
        "run_id": "R100",
        "state": "STARTED",
    }


def test_result_and_terminal_are_exclusive(tmp_path):
    official = tmp_path / "runtime/candidate_v1/official"
    official.mkdir(parents=True)
    claim = _temporary_claim()
    write_json_exclusive(official / "durable_claim.json", claim)
    manifest = {"code_tree_sha256": "a" * 64}
    result = {"schema": "TEMP_RESULT", "value": 1}
    commit_result(tmp_path, result)
    with pytest.raises(RuntimeError, match="registered result already exists"):
        commit_result(tmp_path, result)
    terminalize(
        tmp_path,
        manifest,
        "b" * 64,
        claim,
        state=TERMINAL_FAILURE,
        failure_code="TEST_FAILURE",
    )
    with pytest.raises(FileExistsError):
        terminalize(
            tmp_path,
            manifest,
            "b" * 64,
            claim,
            state=TERMINAL_FAILURE,
            failure_code="SECOND_TERMINAL",
        )


def test_exclusive_json_write_rejects_second_file_creation(tmp_path):
    path = tmp_path / "artifact.json"
    write_json_exclusive(path, {"a": 1})
    with pytest.raises(FileExistsError):
        write_json_exclusive(path, {"a": 1})
