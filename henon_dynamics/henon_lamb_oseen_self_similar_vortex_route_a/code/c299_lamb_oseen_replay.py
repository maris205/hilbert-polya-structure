#!/usr/bin/env python3
"""Byte-for-byte replay of the HCS-C299 deterministic evidence producer."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c299_lamb_oseen_producer.py"
EVIDENCE = ROOT / "results/c299_lamb_oseen_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c299-replay-") as temporary:
        first = Path(temporary) / "first.json"
        second = Path(temporary) / "second.json"
        for target in (first, second):
            result = subprocess.run(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                env=env, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            assert "C299_PRODUCER_PASS" in result.stdout
        assert first.read_bytes() == second.read_bytes() == EVIDENCE.read_bytes()
        print(f"C299 byte replay: PASS ({digest(first)})")


if __name__ == "__main__":
    main()
