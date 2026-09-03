#!/usr/bin/env python3
"""Two isolated byte replays for HCS-C335."""
import subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize:raise RuntimeError("C335 replay refuses optimized Python")
root=Path(__file__).resolve().parents[1];producer=root/"code/c335_shot_noise_ou_producer.py";expected=(root/"results/c335_shot_noise_ou_evidence.json").read_bytes();copies=[]
for index in range(2):
    with tempfile.TemporaryDirectory(prefix=f"c335-replay-{index}-") as directory:
        out=Path(directory)/"evidence.json"
        run=subprocess.run([sys.executable,"-B",str(producer),"--output",str(out)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode:raise AssertionError(run.stdout)
        copies.append(out.read_bytes())
if copies[0]!=copies[1] or copies[0]!=expected:raise AssertionError("isolated evidence mismatch")
print("C335 byte replay: PASS (2 isolated reproductions)")
