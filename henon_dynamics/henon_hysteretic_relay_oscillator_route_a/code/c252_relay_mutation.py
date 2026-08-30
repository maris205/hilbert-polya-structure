#!/usr/bin/env python3
import copy,json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c252_relay_evidence.json"; C=ROOT/"code/c252_relay_checker.py"
def main():
 b=json.loads(E.read_text()); muts=[]
 for k in ("schema","candidate_id","source_commit","fixed_epoch","scope_literal","headline"):
  x=copy.deepcopy(b); x[k]=str(x[k])+"_bad"; muts.append(x)
 for k in b["scope_flags"]:
  x=copy.deepcopy(b); x["scope_flags"][k]=True; muts.append(x)
 for i in range(6):
  x=copy.deepcopy(b); x["regression"]["rows"][i]["full_period"]="0"; muts.append(x)
 rej=0
 with tempfile.TemporaryDirectory() as td:
  for i,x in enumerate(muts):
   p=Path(td)/f"m{i}.json"; p.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; r=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(p),"--quick"],env=env,capture_output=True,text=True); rej += r.returncode!=0
 print(f"C252 hostile mutation: PASS {rej}/{len(muts)}"); assert rej==len(muts)
if __name__=="__main__": main()
