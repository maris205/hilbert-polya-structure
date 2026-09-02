#!/usr/bin/env python3
"""Two-fresh-path byte replay for HCS-C284."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c284_point_vortex_evidence.json"

with tempfile.TemporaryDirectory(prefix="c284-replay-a-") as first_temp, \
     tempfile.TemporaryDirectory(prefix="c284-replay-b-") as second_temp:
    fresh_paths = [
        Path(first_temp) / "nested/a/evidence.json",
        Path(second_temp) / "different/b/evidence.json",
    ]
    payloads = []
    for fresh in fresh_paths:
        env = dict(os.environ)
        env["C284_EVIDENCE_OUT"] = str(fresh)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        subprocess.run(
            [sys.executable, "-B", str(ROOT / "code/c284_point_vortex_producer.py")],
            env=env,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        payloads.append(fresh.read_bytes())
    assert payloads[0] == payloads[1] == CANONICAL.read_bytes()

print(
    f"C284 double fresh-path byte replay: PASS "
    f"({CANONICAL.stat().st_size} bytes on both independent paths)"
)
