#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C282."""
import os, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
canonical = ROOT / "results/c282_ruin_evidence.json"
with tempfile.TemporaryDirectory(prefix="c282-replay-") as temp:
    fresh = Path(temp)/"evidence.json"
    env = dict(os.environ); env["C282_EVIDENCE_OUT"] = str(fresh); env["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run([sys.executable, "-B", str(ROOT/"code/c282_ruin_producer.py")], env=env, check=True,
                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert fresh.read_bytes() == canonical.read_bytes()
print(f"C282 byte replay: PASS ({canonical.stat().st_size} bytes)")
