#!/usr/bin/env python3
"""Replay the C174 producer in isolation and require byte identity."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    producer = root / "code/c174_parity_renewal_producer.py"
    released = root / "results/c174_parity_renewal_evidence.json"
    with tempfile.TemporaryDirectory(prefix="c174-replay-") as tmp:
        replayed = Path(tmp) / "evidence.json"
        process = subprocess.run(
            [sys.executable, str(producer), "--output", str(replayed)],
            check=False,
            text=True,
            capture_output=True,
        )
        if process.returncode != 0:
            raise RuntimeError(process.stderr or process.stdout)
        released_bytes = released.read_bytes()
        replayed_bytes = replayed.read_bytes()
        if released_bytes != replayed_bytes:
            raise AssertionError("replayed evidence differs from released bytes")
    digest = sha256(released_bytes).hexdigest()
    print(
        json.dumps(
            {
                "status": "C174_REPLAY_PASS",
                "byte_identical": True,
                "evidence_sha256": digest,
                "bytes": len(released_bytes),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
