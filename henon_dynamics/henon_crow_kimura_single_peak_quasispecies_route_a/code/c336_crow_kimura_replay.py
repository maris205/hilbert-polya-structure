#!/usr/bin/env python3
"""Two isolated byte-exact producer replays for HCS-C336."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c336_crow_kimura_producer.py"
EVIDENCE = ROOT / "results/c336_crow_kimura_evidence.json"


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C336 replay refuses optimized Python")
    checked = EVIDENCE.read_bytes()
    outputs = []
    with tempfile.TemporaryDirectory(prefix="c336-replay-") as directory:
        work = Path(directory)
        for index in range(2):
            target = work / f"evidence-{index}.json"
            process = subprocess.run(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                cwd=work,
                env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
                check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if "C336_PRODUCER_PASS" not in process.stdout:
                raise AssertionError("producer sentinel absent")
            outputs.append(target.read_bytes())
    if outputs[0] != outputs[1] or outputs[0] != checked:
        raise AssertionError("isolated replay differs from checked evidence")
    value = json.loads(checked)
    body = dict(value)
    claimed = body.pop("payload_sha256")
    computed = sha(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    if claimed != computed:
        raise AssertionError("payload hash stale after replay")
    print(f"C336 byte replay: PASS sha256={sha(checked)} bytes={len(checked)}")


if __name__ == "__main__":
    main()
