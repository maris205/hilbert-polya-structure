from __future__ import annotations

from pathlib import Path

import pytest

from prime_shell.cli import run_registered
from prime_shell.constants import (
    CODE_REVIEW_PATH,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
)
from prime_shell.lifecycle import claim_registered_run


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_registered_lifecycle_requires_review_and_is_one_shot(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError):
        run_registered(PROJECT_ROOT)

    fake_root = tmp_path / "paper"
    results = fake_root / "results"
    results.mkdir(parents=True)
    for relative in (CODE_REVIEW_PATH, PREEXECUTION_TEST_PATH, PREEXECUTION_AUDIT_PATH):
        (fake_root / relative).write_text("placeholder\n", encoding="utf-8")
    claim_registered_run(
        fake_root,
        reviewed_code_sha256="a" * 64,
        review_file_sha256="b" * 64,
        preflight_sha256="c" * 64,
    )
    with pytest.raises(RuntimeError):
        claim_registered_run(
            fake_root,
            reviewed_code_sha256="a" * 64,
            review_file_sha256="b" * 64,
            preflight_sha256="c" * 64,
        )
