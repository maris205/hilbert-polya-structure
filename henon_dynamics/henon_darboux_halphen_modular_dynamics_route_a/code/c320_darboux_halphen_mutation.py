#!/usr/bin/env python3
"""Hostile evidence and YAML mutation suite for HCS-C320."""
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize:raise RuntimeError("C320 mutation lane refuses optimized Python")
root=Path(__file__).resolve().parents[1];source=json.loads((root/"results/c320_darboux_halphen_evidence.json").read_text());checker=root/"code/c320_darboux_halphen_checker.py";evaluation=root/"evaluations/route_a/HCS-C320/2026-09-03.yaml"
def repair(d):
    body=dict(d);body.pop("payload_sha256",None);d["payload_sha256"]=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
mutators=[
 lambda d:d.__setitem__("candidate_id","HCS-C319"),lambda d:d.__setitem__("source_commit","0"*40),lambda d:d.__setitem__("evaluation_date","2026-09-02"),
 lambda d:d["scope_flags"].__setitem__("claims_automorphy",True),lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE"),
 lambda d:d["q_series"].__setitem__("order",63),lambda d:d["q_series"]["rows"][0].__setitem__("X1","1/2"),lambda d:d["q_series"]["rows"][2].__setitem__("X2","-8/2"),
 lambda d:d["q_series"]["rows"][16].__setitem__("minus_half_E2","999"),lambda d:d["q_series"]["rows"][17].__setitem__("X3","999"),lambda d:d["q_series"]["rows"][31]["residuals"].__setitem__(1,"1"),
 lambda d:d["theta_numeric_rows"][0]["x"][0].__setitem__("re","0"),lambda d:d["theta_numeric_rows"][1]["x"][1].__setitem__("im","nan"),lambda d:d["theta_numeric_rows"][2]["S_residual"][2].__setitem__("im","1"),
 lambda d:d["collision_rows_x1_eq_x2"][4].__setitem__("b","9"),lambda d:d["axis_equilibrium_rows"][2]["vector_field"].__setitem__(0,1),lambda d:d["q_series"]["rows"][7].__setitem__("extra",1),lambda d:d["q_series"]["rows"].__setitem__(8,copy.deepcopy(d["q_series"]["rows"][7])),lambda d:d["nonclaims"].__setitem__(0,"unowned"),lambda d:d["enumeration"].__setitem__("extra",1),lambda d:d["route_a_yaml"].__setitem__("raw_sha256","0"*64),lambda d:d["evaluator"].__setitem__("authority","wrong"),lambda d:d["enumeration"].__setitem__("audited_leaf_count",1)]
attempts=0
with tempfile.TemporaryDirectory(prefix="c320-mutation-") as td:
    td=Path(td)
    for i,mutate in enumerate(mutators):
        for fixed in (False,True):
            d=copy.deepcopy(source);mutate(d)
            if fixed:repair(d)
            pth=td/f"m{i}-{int(fixed)}.json";pth.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
            p=subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(pth)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            if p.returncode==0:raise AssertionError(f"mutation survived {i}/{fixed}")
            attempts+=1
    raw=evaluation.read_text()
    changes=(raw.replace("HCS-C320","HCS-C319",1),raw.replace("A0_WEAK_ARITHMETIC_RELATION","A0_FAIL",1),raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true"),raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER","BAD_SCOPE",1),raw+"candidate_id: duplicate\n",raw+"1: non-string\n",raw+"unknown_field: forbidden\n",raw.replace("training_data: none\n",""),raw.replace('evaluation_date: "2026-09-03"','evaluation_date: 2026-09-03'),raw+"anchor_source: &x bad\nanchor_alias: *x\n")
    for i,changed in enumerate(changes):
        pth=td/f"e{i}.yaml";pth.write_text(changed)
        p=subprocess.run([sys.executable,"-B",str(checker),"--evaluation",str(pth)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if p.returncode==0:raise AssertionError(f"YAML mutation survived {i}")
        attempts+=1
print(f"C320 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
