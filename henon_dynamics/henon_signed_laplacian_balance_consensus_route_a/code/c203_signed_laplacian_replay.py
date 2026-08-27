#!/usr/bin/env python3
"""Require byte-exact replay of C203 evidence."""
import json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c203_signed_laplacian_evidence.json"; P=Path(__file__).with_name("c203_signed_laplacian_producer.py")
def main():
    with tempfile.TemporaryDirectory() as d:
        q=Path(d)/"e.json"; subprocess.run([sys.executable,str(P),"--output",str(q)],check=True,capture_output=True)
        if q.read_bytes()!=E.read_bytes(): raise AssertionError("canonical replay mismatch")
    print(json.dumps({"status":"C203_REPLAY_PASS","bytes":E.stat().st_size},sort_keys=True))
if __name__=="__main__": main()
