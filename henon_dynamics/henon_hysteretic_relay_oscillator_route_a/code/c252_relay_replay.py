#!/usr/bin/env python3
import hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"code/c252_relay_producer.py"; E=ROOT/"results/c252_relay_evidence.json"
def main():
    with tempfile.TemporaryDirectory() as td:
        ps=[]
        for i in range(2):
            q=Path(td)/f"e{i}.json"; env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"
            subprocess.check_output([sys.executable,"-B",str(P),"--output",str(q)],env=env,text=True); ps.append(q)
        assert ps[0].read_bytes()==ps[1].read_bytes()
        assert json.loads(ps[0].read_text())["payload_sha256"]==json.loads(E.read_text())["payload_sha256"]
    print("C252 byte replay: PASS (deterministic producer bytes)")
if __name__=="__main__": main()
