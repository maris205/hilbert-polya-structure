#!/usr/bin/env python3
"""Two isolated byte replays for HCS-C332."""
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C332 replay refuses optimized Python")
root=Path(__file__).resolve().parents[1]
producer=root/"code/c332_moreau_play_producer.py"
expected=(root/"results/c332_moreau_play_evidence.json").read_bytes(); copies=[]
for index in range(2):
    with tempfile.TemporaryDirectory(prefix=f"c332-replay-{index}-") as directory:
        output=Path(directory)/"evidence.json"
        run=subprocess.run([sys.executable,"-B",str(producer),"--output",str(output)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode: raise AssertionError(run.stdout)
        copies.append(output.read_bytes())
if copies[0]!=copies[1] or copies[0]!=expected: raise AssertionError("isolated evidence replay mismatch")
print("C332 byte replay: PASS (2 isolated reproductions)")
