#!/usr/bin/env python3
"""Hostile repaired-hash, exact-type, structural, duplicate, and stale attacks."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c290_cr3bp_evidence.json"
CHECKER=ROOT/"code/c290_cr3bp_checker.py"
YAML_PATH=ROOT/"evaluations/route_a/HCS-C290/2026-09-02.yaml"


def phash(data: dict)->str:
    body=dict(data);body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def main()->None:
    original=json.loads(EVIDENCE.read_text()); attacks=[]
    def add(label,edit):
        item=copy.deepcopy(original);edit(item);item["payload_sha256"]=phash(item);attacks.append((label,item))
    add("candidate",lambda d:d.__setitem__("candidate_id","HCS-C000"))
    add("schema",lambda d:d.__setitem__("schema","hcs-c290-v2"))
    add("source",lambda d:d.__setitem__("source_commit","0"*40))
    add("date",lambda d:d.__setitem__("evaluation_date","2026-09-03"))
    add("epoch",lambda d:d.__setitem__("fixed_epoch",0))
    add("scope",lambda d:d.__setitem__("scope_literal","OPEN"))
    add("evaluator",lambda d:d["evaluator"].__setitem__("sha256","0"*64))
    add("model",lambda d:d["model"].__setitem__("equations","wrong Coriolis sign"))
    add("theorem_five",lambda d:d["theorem_contract"].__setitem__("equilibria","four points"))
    add("theorem_poly",lambda d:d["theorem_contract"].__setitem__("triangular_polynomial","wrong constant"))
    add("theorem_critical",lambda d:d["theorem_contract"].__setitem__("critical","stable at equality"))
    add("proof_uniqueness",lambda d:d["proof_contract"].__setitem__("collinear_uniqueness","sampled roots"))
    add("proof_defect",lambda d:d["proof_contract"].__setitem__("critical_defect","eigenvalues only"))
    add("proof_finite",lambda d:d["proof_contract"].__setitem__("finite_role","finite grid proves theorem"))
    add("tuple",lambda d:d["route_a"]["tuple"].__setitem__(1,"A1_WEAK"))
    add("overall",lambda d:d["route_a"].__setitem__("overall","ROUTE_A_VALIDATED"))
    add("route_b",lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",True))
    add("route_b_int",lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",0))
    add("scope_flag",lambda d:d["scope_flags"].__setitem__("root_numbers",True))
    add("triangle_disc",lambda d:d["triangular_cells"][0].__setitem__("routh_discriminant","0"))
    add("triangle_type",lambda d:d["triangular_cells"][0].__setitem__("linear_type","unstable_hamiltonian_quartet"))
    add("triangle_bool",lambda d:d["triangular_cells"][0].__setitem__("linearly_stable",1))
    add("collinear_root",lambda d:d["collinear_cells"][0].__setitem__("x","0"))
    add("collinear_S",lambda d:d["collinear_cells"][0].__setitem__("S","1"))
    add("collinear_type",lambda d:d["collinear_cells"][0].__setitem__("linear_type","center"))
    add("critical_defective",lambda d:d["critical_cell"].__setitem__("defective",False))
    add("critical_defective_int",lambda d:d["critical_cell"].__setitem__("defective",1))
    add("critical_growth_int",lambda d:d["critical_cell"].__setitem__("linear_growth",1))
    add("critical_stable_int",lambda d:d["critical_cell"].__setitem__("linearly_stable",0))
    add("critical_alg_bool",lambda d:d["critical_cell"].__setitem__("algebraic_multiplicity_each",True))
    add("critical_geom_bool",lambda d:d["critical_cell"].__setitem__("geometric_multiplicity_each",True))
    for index,label in enumerate(("L4_minus","L4_plus","L5_minus","L5_plus")):
        add("critical_rank_"+label,lambda d,index=index:d["critical_cell"]["rank_cells"][index].__setitem__("matrix_rank",2))
    add("critical_rank_duplicate",lambda d:d["critical_cell"]["rank_cells"].__setitem__(-1,copy.deepcopy(d["critical_cell"]["rank_cells"][0])))
    add("critical_rank_drop",lambda d:d["critical_cell"]["rank_cells"].pop())
    add("critical_count_bool",lambda d:d["enumeration"].__setitem__("critical_cells",True))
    add("boundary",lambda d:d["boundary_cells"][3].__setitem__("conclusion","stable"))
    add("boundary_resonance",lambda d:d["boundary_cells"][4].__setitem__("conclusion","bounded only away from resonance"))
    add("gascheau_reference",lambda d:d["references"][1].__setitem__("identifier","ghost"))
    add("routh_year",lambda d:d["references"][2].__setitem__("venue","Proceedings of the London Mathematical Society s1-6 (1875), 86-97"))
    add("nonclaim",lambda d:d["nonclaims"].__setitem__(1,"nonlinear stability proved"))
    add("duplicate_triangle",lambda d:d["triangular_cells"].__setitem__(-1,copy.deepcopy(d["triangular_cells"][0])))
    add("drop_collinear",lambda d:d["collinear_cells"].pop())
    add("unknown_top",lambda d:d.__setitem__("extra",1))
    add("missing_top",lambda d:d.pop("critical_cell"))
    add("unknown_row",lambda d:d["collinear_cells"][0].__setitem__("extra",1))
    add("wrong_epoch_type",lambda d:d.__setitem__("fixed_epoch","1788307200"))

    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");passed=0
    with tempfile.TemporaryDirectory(prefix="c290-mutation-") as tmp:
        for label,item in attacks:
            p=Path(tmp)/(label+".json");p.write_text(json.dumps(item,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
            r=subprocess.run([sys.executable,"-B",str(CHECKER),str(p)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            assert r.returncode!=0,label;passed+=1
        raw=EVIDENCE.read_text();marker='  "candidate_id": "HCS-C290",\n';assert raw.count(marker)==1
        p=Path(tmp)/"raw-duplicate.json";p.write_text(raw.replace(marker,marker+marker,1))
        assert subprocess.run([sys.executable,"-B",str(CHECKER),str(p)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode!=0;passed+=1
        stale=copy.deepcopy(original);stale["candidate_id"]="HCS-C000"
        p=Path(tmp)/"stale.json";p.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
        assert subprocess.run([sys.executable,"-B",str(CHECKER),str(p)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode!=0;passed+=1

        yaml_original=yaml.safe_load(YAML_PATH.read_text());yaml_attacks=[]
        def yadd(label,edit):
            item=copy.deepcopy(yaml_original);edit(item);yaml_attacks.append((label,item))
        yadd("yaml_schema",lambda d:d.__setitem__("schema","hcs-route-a-evaluation-v9"))
        yadd("yaml_unknown",lambda d:d.__setitem__("unexpected",True))
        yadd("yaml_missing",lambda d:d.pop("finite_evidence_role"))
        yadd("yaml_tuple",lambda d:d["tuple"].__setitem__(1,"A1_WEAK"))
        yadd("yaml_overall",lambda d:d.__setitem__("overall_verdict","ROUTE_A_VALIDATED"))
        yadd("yaml_route_b",lambda d:d.__setitem__("route_b_invocation_allowed",True))
        yadd("yaml_route_b_int",lambda d:d.__setitem__("route_b_invocation_allowed",0))
        yadd("yaml_epoch_bool",lambda d:d.__setitem__("fixed_epoch",True))
        yadd("yaml_scope_flag",lambda d:d["scope_flags"].__setitem__("root_numbers",True))
        yadd("yaml_owner",lambda d:d["source_owner_tokens"].pop(1))
        for label,item in yaml_attacks:
            path=Path(tmp)/(label+".yaml");path.write_text(yaml.safe_dump(item,sort_keys=False,allow_unicode=True))
            result=subprocess.run([sys.executable,"-B",str(CHECKER),str(EVIDENCE),"--yaml",str(path)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            assert result.returncode!=0,label;passed+=1
        yaml_raw=YAML_PATH.read_text()
        raw_attacks={
            "yaml_duplicate_top":yaml_raw.replace("candidate_id: HCS-C290\n","candidate_id: HCS-C290\ncandidate_id: HCS-C290\n",1),
            "yaml_duplicate_route_b":yaml_raw.replace("route_b_invocation_allowed: false\n","route_b_invocation_allowed: false\nroute_b_invocation_allowed: true\n",1),
            "yaml_duplicate_nested":yaml_raw.replace("  root_numbers: false\n","  root_numbers: false\n  root_numbers: true\n",1),
            "yaml_anchor_alias":"defaults: &defaults {}\n"+yaml_raw,
        }
        for label,raw_attack in raw_attacks.items():
            path=Path(tmp)/(label+".yaml");path.write_text(raw_attack)
            result=subprocess.run([sys.executable,"-B",str(CHECKER),str(EVIDENCE),"--yaml",str(path)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            assert result.returncode!=0,label;passed+=1
    total=len(attacks)+2+len(yaml_attacks)+len(raw_attacks)
    print(f"C290 hostile mutation audit: PASS {passed}/{total} (repaired-hash semantic/structural/exact-type, four critical ranks, strict YAML, raw duplicate-key, stale-hash)")


if __name__=="__main__":main()
