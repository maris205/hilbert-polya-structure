import os
from pathlib import Path

from centralizer_q.constants import CODE_REVIEW_PATH, PREEXECUTION_AUDIT_PATH, PREEXECUTION_TEST_PATH
from centralizer_q.lifecycle import claim_registered_run
from centralizer_q.protocol import sha256_file


def test_registered_lifecycle_requires_review_and_is_one_shot(tmp_path: Path, monkeypatch) -> None:
    results = tmp_path / "results"
    results.mkdir()
    for relative in (CODE_REVIEW_PATH, PREEXECUTION_AUDIT_PATH, PREEXECUTION_TEST_PATH):
        path = tmp_path / relative
        path.write_text(relative + "\n", encoding="utf-8")
    fsync_calls: list[int] = []
    real_fsync = os.fsync

    def tracking_fsync(descriptor: int) -> None:
        fsync_calls.append(descriptor)
        real_fsync(descriptor)

    monkeypatch.setattr(os, "fsync", tracking_fsync)
    claim = claim_registered_run(
        tmp_path,
        reviewed_code_sha256="a" * 64,
        review_file_sha256=sha256_file(tmp_path / CODE_REVIEW_PATH),
        preflight_sha256=sha256_file(tmp_path / PREEXECUTION_AUDIT_PATH),
    )
    assert claim.is_file()
    assert len(fsync_calls) >= 2
    try:
        claim_registered_run(
            tmp_path,
            reviewed_code_sha256="a" * 64,
            review_file_sha256="b" * 64,
            preflight_sha256="c" * 64,
        )
    except RuntimeError:
        pass
    else:
        raise AssertionError("second registered claim accepted")
