#!/usr/bin/env python3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
    out=Path(tmp)/"evidence.json"
    subprocess.run([sys.executable,str(ROOT/"code/c138_magnetic_graph_producer.py"),"--output",str(out)],check=True,stdout=subprocess.DEVNULL)
    assert out.read_bytes()==(ROOT/"results/c138_magnetic_graph_evidence.json").read_bytes()
print("C138 deterministic byte replay: PASS")
