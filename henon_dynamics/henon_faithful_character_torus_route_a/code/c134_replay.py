#!/usr/bin/env python3
"""Byte-for-byte replay of the canonical C134 evidence."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c134_character_producer.py"
EVIDENCE = ROOT / "results/c134_character_evidence.json"


def main():
    with tempfile.TemporaryDirectory(prefix="c134-replay-") as tmp:
        replay = Path(tmp) / "evidence.json"
        completed = subprocess.run([sys.executable, str(PRODUCER), "--output", str(replay)], check=True, capture_output=True, text=True)
        if replay.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs from canonical evidence")
    print(json.dumps({"status": "C134_BYTE_REPLAY_PASS", "evidence_sha256": sha256(EVIDENCE.read_bytes()).hexdigest(), "producer_stdout": completed.stdout.strip()}, sort_keys=True))


if __name__ == "__main__":
    main()
