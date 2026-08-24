#!/usr/bin/env python3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "evidence.json"
    subprocess.run([sys.executable, str(ROOT / "code" / "c128_metaplectic_producer.py"), "--output", str(out)], check=True, stdout=subprocess.DEVNULL)
    assert out.read_bytes() == (ROOT / "results" / "c128_metaplectic_evidence.json").read_bytes()
print("C128 deterministic replay: PASS")
