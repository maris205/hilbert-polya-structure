#!/usr/bin/env python3
"""Byte replay for the frozen C153 producer."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c153_walsh_escape_producer.py"
EVIDENCE = ROOT / "results/c153_walsh_escape_evidence.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    with tempfile.TemporaryDirectory(prefix="c153-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(output)], check=True, capture_output=True, text=True)
        if output.read_bytes() != EVIDENCE.read_bytes():
            raise SystemExit("C153 replay bytes differ")
    print(json.dumps({"status": "C153_REPLAY_PASS", "sha256": digest(EVIDENCE)}, sort_keys=True))


if __name__ == "__main__":
    main()
