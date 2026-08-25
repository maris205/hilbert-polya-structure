#!/usr/bin/env python3
"""Deterministic evidence replay for HCS-C162."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile
def digest(p):return sha256(p.read_bytes()).hexdigest()
def main():
    root=Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="c162-replay-") as temp:
        one=Path(temp)/"one.json";two=Path(temp)/"two.json"
        for out in (one,two):subprocess.run([sys.executable,str(root/"code/c162_branch_amplitude_producer.py"),"--output",str(out)],check=True,capture_output=True,text=True)
        assert one.read_bytes()==two.read_bytes()==(root/"results/c162_branch_amplitude_evidence.json").read_bytes()
        subprocess.run([sys.executable,str(root/"code/c162_branch_amplitude_checker.py"),"--evidence",str(one)],check=True,capture_output=True,text=True)
        value=digest(one)
    print(json.dumps({"status":"C162_REPLAY_PASS","evidence_sha256":value},sort_keys=True))
if __name__=="__main__":main()
