#!/usr/bin/env python3
"""Byte-replay the deterministic C209 producer."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c209_kreweras_producer.py"
EVIDENCE = ROOT / "results/c209_kreweras_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c209-replay-") as directory:
        target = Path(directory) / "evidence.json"
        subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(target)],
            check=True,
            capture_output=True,
            text=True,
        )
        expected = EVIDENCE.read_bytes()
        obtained = target.read_bytes()
        if obtained != expected:
            raise AssertionError("C209 producer byte replay differs")
    payload = json.loads(expected)
    print(json.dumps({
        "status": "C209_REPLAY_PASS",
        "bytes": len(expected),
        "sha256": sha256(expected).hexdigest(),
        "payload_sha256": payload["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
