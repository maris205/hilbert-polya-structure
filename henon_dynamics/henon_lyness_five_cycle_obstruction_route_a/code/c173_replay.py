#!/usr/bin/env python3
"""Byte-for-byte producer replay for C173."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c173_lyness_producer.py"
EVIDENCE = ROOT / "results/c173_lyness_evidence.json"


def digest(blob: bytes) -> str:
    return sha256(blob).hexdigest()


def main() -> None:
    reference = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c173-replay-") as directory:
        output = Path(directory) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(output)], check=True, capture_output=True)
        replay = output.read_bytes()
    if replay != reference:
        raise AssertionError(f"byte replay mismatch: {digest(reference)} != {digest(replay)}")
    print(json.dumps({"status": "C173_REPLAY_PASS", "bytes": len(reference), "sha256": digest(reference)}, sort_keys=True))


if __name__ == "__main__":
    main()
