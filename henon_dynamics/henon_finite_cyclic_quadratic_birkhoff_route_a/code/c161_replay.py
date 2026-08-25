#!/usr/bin/env python3
"""Deterministic replay for HCS-C161."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess, sys, tempfile

def digest(path): return sha256(path.read_bytes()).hexdigest()
def main():
    root=Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="c161-replay-") as temp:
        p=Path(temp); one=p/"one.json"; two=p/"two.json"
        for output in (one,two):
            subprocess.run([sys.executable,str(root/"code/c161_cyclic_gauss_producer.py"),"--output",str(output)],check=True,capture_output=True,text=True)
        assert one.read_bytes()==two.read_bytes()==(root/"results/c161_cyclic_gauss_evidence.json").read_bytes()
        subprocess.run([sys.executable,str(root/"code/c161_cyclic_gauss_checker.py"),"--evidence",str(one)],check=True,capture_output=True,text=True)
        value=digest(one)
    print(json.dumps({"status":"C161_REPLAY_PASS","evidence_sha256":value},sort_keys=True))
if __name__ == "__main__": main()
