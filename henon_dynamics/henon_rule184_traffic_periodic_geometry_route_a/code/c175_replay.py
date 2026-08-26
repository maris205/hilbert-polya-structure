#!/usr/bin/env python3
"""Byte-replay the deterministic HCS-C175 evidence producer."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c175_rule184_producer.py"
EVIDENCE = ROOT / "results/c175_rule184_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c175-replay-") as tmp:
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
        "status": "C175_REPLAY_PASS",
        "bytes": len(expected),
        "sha256": sha256(expected).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
