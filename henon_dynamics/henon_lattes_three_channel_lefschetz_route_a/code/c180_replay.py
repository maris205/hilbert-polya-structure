#!/usr/bin/env python3
"""Byte-for-byte deterministic replay for C180 evidence."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c180_lattes_producer.py"
EVIDENCE = ROOT / "results/c180_lattes_evidence.json"


def digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c180-replay-") as tmp:
        out = Path(tmp) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(out)], check=True, capture_output=True, text=True)
        expected, observed = EVIDENCE.read_bytes(), out.read_bytes()
        assert observed == expected, "producer replay is not byte-identical"
    print(json.dumps({"status": "C180_REPLAY_PASS", "bytes": len(expected), "sha256": digest(expected)}, sort_keys=True))


if __name__ == "__main__":
    main()
