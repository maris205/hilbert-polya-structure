#!/usr/bin/env python3
"""Two-path byte replay for the HCS-C297 evidence receipt."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c297_pt_dimer_producer.py"
ARCHIVE = ROOT / "results/c297_pt_dimer_evidence.json"


def main() -> None:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    payloads = []
    with tempfile.TemporaryDirectory(prefix="c297-replay-a-") as first, tempfile.TemporaryDirectory(prefix="c297-replay-b-") as second:
        for directory in (first, second):
            output = Path(directory) / "evidence.json"
            result = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)], env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            assert "C297_PRODUCER_PASS" in result.stdout
            payloads.append(output.read_bytes())
    archived = ARCHIVE.read_bytes()
    assert payloads[0] == payloads[1] == archived
    print(json.dumps({"status": "C297_REPLAY_PASS", "bytes": len(archived), "sha256": hashlib.sha256(archived).hexdigest(), "paths": 2}, sort_keys=True))


if __name__ == "__main__":
    main()
