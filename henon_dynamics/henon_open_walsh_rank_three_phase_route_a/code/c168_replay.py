#!/usr/bin/env python3
"""Byte-for-byte producer replay for HCS-C168."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c168_rank_three_producer.py"
EVIDENCE = ROOT / "results/c168_rank_three_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c168-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(output)],
            check=True,
            capture_output=True,
            text=True,
        )
        if output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs from frozen evidence")
    print(json.dumps({"status": "C168_REPLAY_PASS", "sha256": sha256(EVIDENCE.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
