#!/usr/bin/env python3
"""Byte-replay the deterministic HCS-C176 evidence producer."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c176_sandpile_producer.py"
EVIDENCE = ROOT / "results/c176_sandpile_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c176-replay-") as tmp:
        target = Path(tmp) / "evidence.json"
        subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(target)],
            check=True,
            capture_output=True,
            text=True,
        )
        expected = EVIDENCE.read_bytes()
        got = target.read_bytes()
        if got != expected:
            raise AssertionError("byte replay differs")
    print(json.dumps({
        "status": "C176_REPLAY_PASS",
        "bytes": len(expected),
        "sha256": sha256(expected).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
