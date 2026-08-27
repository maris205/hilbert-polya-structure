#!/usr/bin/env python3
"""Byte-for-byte isolated replay of the C194 evidence producer."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c194_holte_producer.py"
EVIDENCE = ROOT / "results/c194_holte_evidence.json"


def main() -> None:
    released = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c194-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        environment = os.environ.copy()
        environment["C194_OUTPUT"] = str(output)
        completed = subprocess.run(
            [sys.executable, str(PRODUCER)], check=True, capture_output=True, text=True, env=environment,
        )
        replayed = output.read_bytes()
        if replayed != released:
            raise AssertionError(f"replay differs: {completed.stdout.strip()}")
    print(json.dumps({
        "status": "C194_REPLAY_PASS",
        "bytes": len(released),
        "sha256": sha256(released).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
