#!/usr/bin/env python3
"""Run the exact producer from two distinct isolated working directories."""
if not __debug__:
    raise RuntimeError("c381 replay refuses optimized Python")
import subprocess
import sys
import tempfile
from pathlib import Path
def main():
    root=Path(__file__).resolve().parents[1];blobs=[]
    for label in ("one","two"):
        with tempfile.TemporaryDirectory(prefix="c381-replay-"+label+"-") as d:
            work=Path(d);out=work/"evidence.json"
            p=subprocess.run([sys.executable,"-B",str(root/"code/c381_lsv_producer.py"),"--output",str(out)],cwd=work,capture_output=True,text=True)
            assert p.returncode==0,p.stderr
            blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(root/"results/c381_lsv_evidence.json").read_bytes()
    print("C381 isolated replay PASS: two working directories and canonical bytes agree")
if __name__=="__main__":main()
