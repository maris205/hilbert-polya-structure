#!/usr/bin/env python3
"""Byte-for-byte replay of the C130 evidence receipt."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code" / "c130_suspension_producer.py"
EVIDENCE = ROOT / "results" / "c130_suspension_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c130-replay-") as tmp:
        replay = Path(tmp) / "evidence.json"
        completed = subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(replay)],
            check=True,
            capture_output=True,
            text=True,
        )
        if replay.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs from checked-in evidence")
    print(json.dumps({
        "status": "C130_BYTE_REPLAY_PASS",
        "evidence_sha256": hashlib.sha256(EVIDENCE.read_bytes()).hexdigest(),
        "producer_stdout": completed.stdout.strip(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
