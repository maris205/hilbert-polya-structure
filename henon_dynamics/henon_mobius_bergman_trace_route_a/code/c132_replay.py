#!/usr/bin/env python3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
    output = Path(tmp) / "evidence.json"
    subprocess.run([sys.executable, str(ROOT / "code/c132_mobius_bergman_producer.py"), "--output", str(output)], check=True, stdout=subprocess.DEVNULL)
    assert output.read_bytes() == (ROOT / "results/c132_mobius_bergman_evidence.json").read_bytes()
print("C132 deterministic replay: PASS")
