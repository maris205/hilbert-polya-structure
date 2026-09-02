#!/usr/bin/env python3
"""Replay the C298 producer twice and compare canonical bytes."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c298_grassmann_producer.py"
EVIDENCE = ROOT / "results/c298_grassmann_evidence.json"


def main() -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c298-replay-") as temporary:
        first = Path(temporary) / "first.json"
        second = Path(temporary) / "second.json"
        for path in (first, second):
            output = subprocess.check_output(
                [sys.executable, "-B", str(PRODUCER), "--output", str(path)],
                env=env, text=True,
            )
            assert "C298_PRODUCER_PASS" in output
        archived = EVIDENCE.read_bytes()
        assert first.read_bytes() == second.read_bytes() == archived
        print(
            "C298 byte replay: PASS "
            f"(sha256={hashlib.sha256(archived).hexdigest()}, bytes={len(archived)})"
        )


if __name__ == "__main__":
    main()
