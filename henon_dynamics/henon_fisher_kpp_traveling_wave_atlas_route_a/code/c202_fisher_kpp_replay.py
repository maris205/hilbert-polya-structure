#!/usr/bin/env python3
"""Byte-exact isolated replay for HCS-C202."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c202_fisher_kpp_producer.py"
EVIDENCE = ROOT / "results/c202_fisher_kpp_evidence.json"


def main() -> None:
    released = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c202-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        completed = subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(output)],
            check=True, capture_output=True, text=True,
        )
        replayed = output.read_bytes()
    if replayed != released:
        raise AssertionError(completed.stdout)
    print(json.dumps({
        "status": "C202_REPLAY_PASS",
        "bytes": len(released),
        "sha256": sha256(released).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
