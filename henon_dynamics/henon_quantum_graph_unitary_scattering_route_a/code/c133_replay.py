#!/usr/bin/env python3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "evidence.json"
    subprocess.run(
        [sys.executable, str(ROOT / "code" / "c133_quantum_graph_producer.py"), "--output", str(out)],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    assert out.read_bytes() == (ROOT / "results" / "c133_quantum_graph_evidence.json").read_bytes()
print("C133 deterministic replay: PASS")
