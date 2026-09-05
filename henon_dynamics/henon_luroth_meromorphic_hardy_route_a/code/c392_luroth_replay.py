#!/usr/bin/env python3
"""Two independent temporary-directory byte replays."""
if not __debug__:
    raise RuntimeError("c392 replay refuses optimized Python")
import subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
blobs=[]
for i in range(2):
    with tempfile.TemporaryDirectory(prefix="c392-replay-") as d:
        target=Path(d)/"evidence.json"
        subprocess.run([sys.executable,"-B",str(ROOT/"code/c392_luroth_producer.py"),"--output",str(target)],check=True,capture_output=True)
        blobs.append(target.read_bytes())
assert blobs[0]==blobs[1]==(ROOT/"results/c392_luroth_evidence.json").read_bytes()
print("C392 two-directory byte replay PASS")
