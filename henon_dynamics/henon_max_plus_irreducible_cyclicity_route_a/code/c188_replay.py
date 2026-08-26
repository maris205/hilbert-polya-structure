#!/usr/bin/env python3
"""Byte-for-byte replay of the C188 producer in an isolated directory."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c188_max_plus_producer.py"
EVIDENCE = ROOT / "results/c188_max_plus_evidence.json"


def main() -> None:
    released = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c188-replay-") as temp:
        output = Path(temp) / "evidence.json"
        env = os.environ.copy()
        env["C188_OUTPUT"] = str(output)
        completed = subprocess.run(
            [sys.executable, str(PRODUCER)],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )
        replayed = output.read_bytes()
        if replayed != released:
            raise AssertionError(f"replay differs: {completed.stdout.strip()}")
    print(json.dumps({
        "status": "C188_REPLAY_PASS",
        "bytes": len(released),
        "sha256": sha256(released).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
