#!/usr/bin/env python3
"""Two isolated byte replays for HCS-C334."""
import subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize:raise RuntimeError("C334 replay refuses optimized Python")
root=Path(__file__).resolve().parents[1]; producer=root/"code/c334_morse_producer.py"; expected=(root/"results/c334_morse_evidence.json").read_bytes(); copies=[]
for index in range(2):
    with tempfile.TemporaryDirectory(prefix=f"c334-replay-{index}-") as directory:
        out=Path(directory)/"evidence.json"
        run=subprocess.run([sys.executable,"-B",str(producer),"--output",str(out)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode:raise AssertionError(run.stdout)
        copies.append(out.read_bytes())
if copies[0]!=copies[1] or copies[0]!=expected:raise AssertionError("isolated evidence mismatch")
print("C334 byte replay: PASS (2 isolated reproductions)")
