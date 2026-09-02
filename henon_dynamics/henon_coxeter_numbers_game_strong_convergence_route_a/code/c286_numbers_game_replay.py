#!/usr/bin/env python3
"""Fresh-path, byte-for-byte replay for HCS-C286 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c286_numbers_game_evidence.json"
PRODUCER = ROOT / "code/c286_numbers_game_producer.py"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(path: Path) -> bytes:
    env = dict(os.environ)
    env["C286_EVIDENCE_OUT"] = str(path)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(
        [sys.executable, "-B", str(PRODUCER)],
        env=env,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return path.read_bytes()


def main() -> None:
    canonical = CANONICAL.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c286-numbers-replay-a-") as first_temp, tempfile.TemporaryDirectory(prefix="c286-numbers-replay-b-") as second_temp:
        first = build(Path(first_temp) / "nested/a/evidence.json")
        second = build(Path(second_temp) / "other/b/evidence.json")
    assert first == second == canonical
    print(f"C286 byte replay: PASS ({len(canonical)} bytes; sha256={digest(canonical)}; two fresh paths)")


if __name__ == "__main__":
    main()
