#!/usr/bin/env python3
import hashlib,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"code/c315_goldfish_producer.py";E=ROOT/"results/c315_goldfish_evidence.json"
def main():
 if sys.flags.optimize:raise RuntimeError("C315 replay refuses optimized Python")
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC")
 with tempfile.TemporaryDirectory(prefix="c315-replay-") as d:
  fs=[Path(d)/"a.json",Path(d)/"b.json"]
  for f in fs:
   if "C315_PRODUCER_PASS" not in subprocess.check_output([sys.executable,"-B",str(P),"--output",str(f)],env=env,text=True):raise AssertionError("sentinel")
  if fs[0].read_bytes()!=fs[1].read_bytes() or fs[0].read_bytes()!=E.read_bytes():raise AssertionError("replay")
  print(f"C315 byte replay: PASS ({hashlib.sha256(fs[0].read_bytes()).hexdigest()})")
if __name__=="__main__":main()
