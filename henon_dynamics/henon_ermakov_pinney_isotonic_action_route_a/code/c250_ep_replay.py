#!/usr/bin/env python3
"""Byte replay for the C250 evidence producer."""
import hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; PRODUCER=ROOT/"code/c250_ep_producer.py"; SOURCE=ROOT/"results/c250_ep_evidence.json"
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    with tempfile.TemporaryDirectory() as td:
        outs=[]
        for i in range(2):
            p=Path(td)/f"e{i}.json"; env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"
            subprocess.check_output([sys.executable,"-B",str(PRODUCER),"--output",str(p)],env=env,text=True); outs.append(p)
        assert outs[0].read_bytes()==outs[1].read_bytes() and json.loads(outs[0].read_text())["payload_sha256"]==json.loads(SOURCE.read_text())["payload_sha256"]
    print(f"C250 byte replay: PASS ({digest(SOURCE)})")
if __name__=="__main__": main()
