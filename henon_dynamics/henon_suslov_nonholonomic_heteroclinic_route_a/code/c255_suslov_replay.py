#!/usr/bin/env python3
import json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/"code/c255_suslov_producer.py"; E=ROOT/"results/c255_suslov_evidence.json"
def main():
 with tempfile.TemporaryDirectory() as td:
  ps=[]
  for i in range(2):
   p=Path(td)/f"e{i}.json"; env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; subprocess.check_output([sys.executable,"-B",str(P),"--output",str(p)],env=env,text=True); ps.append(p)
  assert ps[0].read_bytes()==ps[1].read_bytes()==E.read_bytes(); assert json.loads(ps[0].read_text())["payload_sha256"]==json.loads(E.read_text())["payload_sha256"]
 print("C255 byte replay: PASS (two deterministic producer runs equal the released bytes)")
if __name__=="__main__": main()
