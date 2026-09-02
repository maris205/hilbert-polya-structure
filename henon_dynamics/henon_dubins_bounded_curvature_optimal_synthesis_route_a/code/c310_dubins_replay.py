#!/usr/bin/env python3
import hashlib,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"code/c310_dubins_producer.py";E=ROOT/"results/c310_dubins_evidence.json"
def main():
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC")
 with tempfile.TemporaryDirectory(prefix="c310-replay-") as tmp:
  paths=[Path(tmp)/"a.json",Path(tmp)/"b.json"]
  for path in paths:
   if "C310_PRODUCER_PASS" not in subprocess.check_output([sys.executable,"-B",str(P),"--output",str(path)],env=env,text=True):raise AssertionError("sentinel")
  if paths[0].read_bytes()!=paths[1].read_bytes() or paths[0].read_bytes()!=E.read_bytes():raise AssertionError("replay")
  print(f"C310 byte replay: PASS ({hashlib.sha256(paths[0].read_bytes()).hexdigest()})")
if __name__=="__main__":main()
