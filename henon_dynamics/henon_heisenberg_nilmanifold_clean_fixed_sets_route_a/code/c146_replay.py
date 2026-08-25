#!/usr/bin/env python3
"""Byte-for-byte producer replay for HCS-C146."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c146_heisenberg_producer.py"
EVIDENCE = ROOT / "results/c146_heisenberg_evidence.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    with tempfile.TemporaryDirectory(prefix="c146-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(output)], check=True, capture_output=True, text=True)
        if output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs from frozen evidence")
    print(json.dumps({"status": "C146_REPLAY_PASS", "sha256": digest(EVIDENCE)}, sort_keys=True))


if __name__ == "__main__":
    main()
