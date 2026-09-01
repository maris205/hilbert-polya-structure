#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C281."""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
canonical = ROOT / "results/c281_ricci_evidence.json"
with tempfile.TemporaryDirectory(prefix="c281-ricci-replay-") as temp:
    fresh = Path(temp) / "evidence.json"
    env = dict(os.environ)
    env["C281_EVIDENCE_OUT"] = str(fresh)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run([sys.executable, "-B", str(ROOT / "code/c281_ricci_producer.py")], env=env, check=True,
                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert fresh.read_bytes() == canonical.read_bytes()
print(f"C281 byte replay: PASS ({canonical.stat().st_size} bytes)")
