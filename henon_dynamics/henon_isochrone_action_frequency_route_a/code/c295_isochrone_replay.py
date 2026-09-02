#!/usr/bin/env python3
"""Fresh-path byte replay for the deterministic HCS-C295 producer."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c295_isochrone_producer.py"
EVIDENCE = ROOT / "results/c295_isochrone_evidence.json"


def main() -> None:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c295-replay-a-") as first_dir, tempfile.TemporaryDirectory(prefix="c295-replay-b-") as second_dir:
        outputs = []
        for directory in (first_dir, second_dir):
            target = Path(directory) / "nested/fresh/evidence.json"
            result = subprocess.run(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            if "C295_PRODUCER_PASS" not in result.stdout:
                raise AssertionError("producer sentinel missing")
            outputs.append(target.read_bytes())
    canonical = EVIDENCE.read_bytes()
    if outputs[0] != outputs[1] or outputs[0] != canonical:
        raise AssertionError("fresh-path producer output is not byte-identical")
    digest = hashlib.sha256(canonical).hexdigest()
    print(f"C295 fresh-path byte replay: PASS (two isolated paths; sha256={digest})")


if __name__ == "__main__":
    main()
