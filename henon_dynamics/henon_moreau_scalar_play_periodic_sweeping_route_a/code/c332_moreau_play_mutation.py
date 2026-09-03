#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C332."""
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

if sys.flags.optimize: raise RuntimeError("C332 mutation lane refuses optimized Python")
root=Path(__file__).resolve().parents[1]; evidence_path=root/"results/c332_moreau_play_evidence.json"; evaluation_path=root/"evaluations/route_a/HCS-C332/2026-09-03.yaml"; checker=root/"code/c332_moreau_play_checker.py"; source=json.loads(evidence_path.read_text())
def repair(data):
    body=dict(data); body.pop("payload_sha256",None); data["payload_sha256"]=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
mutators=[
    lambda d:d.__setitem__("candidate_id","HCS-C331"),
    lambda d:d.__setitem__("source_commit","0"*40),
    lambda d:d.__setitem__("evaluation_date","2026-09-02"),
    lambda d:d["evaluator"].__setitem__("authority","wrong.md"),
    lambda d:d["evaluation_lock"].__setitem__("raw_sha256","0"*64),
    lambda d:d["scope_flags"].__setitem__("claims_target_euler_factors",True),
    lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE"),
    lambda d:d["model"].__setitem__("extra","unowned"),
    lambda d:d["theorem_contract"].__setitem__("poincare_map","wrong"),
    lambda d:d["case_rows"][0].__setitem__("range_D","2/2"),
    lambda d:d["case_rows"][1].__setitem__("chamber","D_gt_2r"),
    lambda d:d["case_rows"][2].__setitem__("fixed_set_low","0"),
    lambda d:d["case_rows"][3]["initial_rows"][0].__setitem__("after_two_periods","99"),
    lambda d:d["case_rows"][4]["initial_rows"].pop(),
    lambda d:d["case_rows"][5].__setitem__("extra",1),
    lambda d:d["case_rows"][6].__setitem__("play_variation","0"),
    lambda d:d["case_rows"][7].__setitem__("variation_formula_check",False),
    lambda d:d["case_rows"][8]["path_levels"].pop(),
    lambda d:d["case_rows"][9]["periodic_play_nodes"].__setitem__(2,"999"),
    lambda d:d["case_rows"][10]["stretched_play_nodes"].__setitem__(3,"999"),
    lambda d:d["case_rows"].__setitem__(11,copy.deepcopy(d["case_rows"][10])),
    lambda d:d["boundary_atlas"].pop(),
    lambda d:d["collision_boundary"].__setitem__("C999","fake"),
    lambda d:d["references"][0].__setitem__("doi","10.0000/fake"),
    lambda d:d["enumeration"].__setitem__("extra",1),
]
attempts=0
with tempfile.TemporaryDirectory(prefix="c332-mutations-") as directory:
    directory=Path(directory)
    for index,mutate in enumerate(mutators):
        for repaired in (False,True):
            data=copy.deepcopy(source); mutate(data)
            if repaired: repair(data)
            path=directory/f"evidence-{index}-{int(repaired)}.json"; path.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
            run=subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            if run.returncode==0: raise AssertionError(f"evidence mutation survived: {index}/{repaired}")
            attempts+=1
    raw=evidence_path.read_text()
    for index,changed in enumerate((raw.replace('"candidate_id": "HCS-C332",','"candidate_id": "HCS-C332",\n  "candidate_id": "duplicate",',1),raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1))):
        path=directory/f"parser-{index}.json"; path.write_text(changed)
        run=subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode==0: raise AssertionError(f"JSON parser mutation survived: {index}")
        attempts+=1
    raw=evaluation_path.read_text()
    attacks=(
        raw.replace("HCS-C332","HCS-C331",1),raw.replace("evaluation_date: '2026-09-03'","evaluation_date: 2026-09-03",1),
        raw.replace("A1_PASS_ANALYTIC","A1_WEAK",1),raw.replace("A4_FORMAL_HINT","A4_FAIL",1),
        raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1),raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER","BAD_SCOPE",1),
        raw.replace("  - THEOREM_PACKAGE.md","  - WRONG.md",1),raw.replace("artifact_paths:\n  - results","artifact_paths: results",1),
        raw+"candidate_id: duplicate\n","base: &base\n  verdict: A0_FAIL\ncopy: *base\n"+raw,
        raw.replace("a0:\n","a0:\n  <<: {verdict: A0_FAIL}\n",1),raw.replace("candidate_id: HCS-C332","1: HCS-C332",1),
        raw.replace("theorem_status: PROVABLE_AS_STATED","unknown_field: x\ntheorem_status: PROVABLE_AS_STATED",1),
        raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md","evaluator_authority: wrong.md",1),
        raw.replace("  evidence_status: PROVED\n","",1),raw.replace("  evidence_status: STOP_SCOPED","  evidence_status: PROVED",1),
        raw.replace("  - 10.1007/978-1-4612-4048-8","  - 10.0000/fake",1),
    )
    for index,changed in enumerate(attacks):
        path=directory/f"evaluation-{index}.yaml"; path.write_text(changed)
        run=subprocess.run([sys.executable,"-B",str(checker),"--evaluation",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode==0: raise AssertionError(f"YAML mutation survived: {index}")
        attempts+=1
print(f"C332 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
