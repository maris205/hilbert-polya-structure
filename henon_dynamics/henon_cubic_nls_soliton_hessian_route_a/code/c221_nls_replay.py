#!/usr/bin/env python3
"""Clean-process byte replay of the canonical NLS receipt."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c221_nls_evidence.json"
PRODUCER = ROOT / "code/c221_nls_producer.py"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c221-replay-") as td:
        out = Path(td) / "replayed.json"
        proc = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(out)], capture_output=True, text=True, check=True)
        payload = json.loads(proc.stdout.strip().splitlines()[-1])
        original = EVIDENCE.read_bytes()
        replayed = out.read_bytes()
        if original != replayed:
            raise AssertionError("producer replay differs byte-for-byte")
        if payload.get("status") != "C221_PRODUCER_PASS":
            raise AssertionError("producer replay status")
        print(json.dumps({"status": "C221_REPLAY_PASS", "bytes": len(original), "payload_sha256": json.loads(original)["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
