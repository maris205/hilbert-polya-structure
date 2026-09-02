#!/usr/bin/env python3
"""Replay the C294 producer twice and compare canonical bytes."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c294_three_disk_producer.py"
EVIDENCE = ROOT / "results/c294_three_disk_evidence.json"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c294-replay-") as tmp:
        p1 = Path(tmp) / "one.json"
        p2 = Path(tmp) / "two.json"
        for path in (p1, p2):
            output = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(path)], env=env, text=True)
            assert "C294_PRODUCER_PASS" in output
        expected = EVIDENCE.read_bytes()
        assert p1.read_bytes() == p2.read_bytes() == expected
        print(f"C294 byte replay: PASS (sha256={digest(expected)}, bytes={len(expected)})")


if __name__ == "__main__":
    main()
