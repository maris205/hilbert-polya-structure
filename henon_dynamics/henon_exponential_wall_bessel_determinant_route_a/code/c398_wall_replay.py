#!/usr/bin/env python3
"""Two independent temporary-directory byte replays."""
if not __debug__:
    raise RuntimeError("c398 replay refuses optimized Python")
import subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
blobs=[]
for i in range(2):
    with tempfile.TemporaryDirectory(prefix="c398-replay-") as d:
        target=Path(d)/"evidence.json"
        subprocess.run([sys.executable,"-B",str(ROOT/"code/c398_wall_producer.py"),"--output",str(target)],check=True,capture_output=True)
        blobs.append(target.read_bytes())
assert blobs[0]==blobs[1]==(ROOT/"results/c398_wall_evidence.json").read_bytes()
print("C398 two-directory byte replay PASS")
