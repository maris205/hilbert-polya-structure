#!/usr/bin/env python3
"""Byte-for-byte replay of the canonical C124 evidence receipt."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c124_hardy_producer.py"
EVIDENCE = ROOT / "results/c124_hardy_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c124-replay-") as tmp:
        replay = Path(tmp) / "evidence.json"
        completed = subprocess.run([sys.executable, str(PRODUCER), str(replay)], check=True, capture_output=True, text=True)
        if replay.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs from checked-in evidence")
    digest = sha256(EVIDENCE.read_bytes()).hexdigest()
    print(json.dumps({"status": "C124_BYTE_REPLAY_PASS", "evidence_sha256": digest, "producer_stdout": completed.stdout.strip()}, sort_keys=True))


if __name__ == "__main__":
    main()
