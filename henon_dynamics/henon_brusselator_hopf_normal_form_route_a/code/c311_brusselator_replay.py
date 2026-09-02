#!/usr/bin/env python3
import hashlib,os,subprocess,sys,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R/"code/c311_brusselator_producer.py";E=R/"results/c311_brusselator_evidence.json"
def main():
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC")
 with tempfile.TemporaryDirectory(prefix="c311-replay-") as t:
  a,b=Path(t)/"a.json",Path(t)/"b.json"
  for p in (a,b):
   if "C311_PRODUCER_PASS" not in subprocess.check_output([sys.executable,"-B",str(P),"--output",str(p)],env=env,text=True):raise AssertionError("sentinel")
  if a.read_bytes()!=b.read_bytes() or a.read_bytes()!=E.read_bytes():raise AssertionError("replay")
  print(f"C311 byte replay: PASS ({hashlib.sha256(a.read_bytes()).hexdigest()})")
if __name__=="__main__":main()
