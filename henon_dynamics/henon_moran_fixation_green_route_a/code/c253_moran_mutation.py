#!/usr/bin/env python3
import copy,json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c253_moran_evidence.json"; C=ROOT/"code/c253_moran_checker.py"
def main():
    base=json.loads(E.read_text()); muts=[]
    for k in ("schema","candidate_id","source_commit","fixed_epoch","scope_literal","headline"):
        x=copy.deepcopy(base); x[k]=str(x[k])+"_bad"; muts.append(x)
    for k in base["scope_flags"]:
        x=copy.deepcopy(base); x["scope_flags"][k]=True; muts.append(x)
    for i in range(8):
        x=copy.deepcopy(base); x["regression"]["rows"][i]["fixation_probability"]="0"; muts.append(x)
    rej=0
    with tempfile.TemporaryDirectory() as td:
        for i,x in enumerate(muts):
            p=Path(td)/f"m{i}.json"; p.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"
            r=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(p),"--quick"],env=env,text=True,capture_output=True); rej += r.returncode!=0
    print(f"C253 hostile mutation: PASS {rej}/{len(muts)}"); assert rej==len(muts)
if __name__=="__main__": main()
