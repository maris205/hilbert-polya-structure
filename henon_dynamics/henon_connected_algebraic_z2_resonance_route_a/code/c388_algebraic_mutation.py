#!/usr/bin/env python3
"""Repaired-payload-hash hostile attacks, strict YAML drift, optimized refusal."""
if not __debug__:
    raise RuntimeError("c388 mutation refuses optimized Python")
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import c388_algebraic_checker as check
ROOT=Path(__file__).resolve().parents[1]
def main():
    base=check.load(ROOT/"results/c388_algebraic_evidence.json");check.verify(base);check.evaluation()
    ri=next(i for i,r in enumerate(base["lattice_rows"]) if r["resonant"])
    mutations=[
      ("unknown_root",lambda x:x.update(unknown=1)),
      ("scope_true",lambda x:x["scope_flags"].update(invokes_route_b=True)),
      ("scope_integer",lambda x:x["scope_flags"].update(invokes_route_b=0)),
      ("epoch_boolean",lambda x:x.update(fixed_epoch=True)),
      ("source_drift",lambda x:x.update(source_commit="0"*40)),
      ("tuple_promotion",lambda x:x["route_a"]["tuple"].__setitem__(2,"A2_PASS_ANALYTIC")),
      ("row_omission",lambda x:x["lattice_rows"].pop()),
      ("row_order",lambda x:x["lattice_rows"].reverse()),
      ("hnf_boolean",lambda x:x["lattice_rows"][0]["hnf"].__setitem__(0,True)),
      ("matrix_entry",lambda x:x["lattice_rows"][0]["matrix"][0].__setitem__(0,4)),
      ("matrix_boolean",lambda x:x["lattice_rows"][0]["matrix"][0].__setitem__(0,True)),
      ("unimodular_left",lambda x:x["lattice_rows"][0]["left_unimodular"][0].__setitem__(0,2)),
      ("unimodular_right",lambda x:x["lattice_rows"][0]["right_unimodular"][0].__setitem__(0,2)),
      ("smith_factor",lambda x:x["lattice_rows"][0]["smith_diagonal"].__setitem__(0,2)),
      ("characteristic",lambda x:x["lattice_rows"][0]["characteristic_polynomial"].__setitem__(1,-4)),
      ("resonance_suppressed",lambda x:x["lattice_rows"][ri].update(resonant=False)),
      ("nullity_one",lambda x:x["lattice_rows"][ri].update(torus_dimension=1)),
      ("pseudodet_as_components",lambda x:x["lattice_rows"][ri].update(component_count=x["lattice_rows"][ri]["nonzero_eigenvalue_product_abs"])),
      ("gram_unsaturated",lambda x:x["lattice_rows"][ri]["kernel_gram"][0].__setitem__(0,8)),
      ("gram_determinant",lambda x:x["lattice_rows"][ri].update(kernel_gram_determinant=1)),
      ("torus_census",lambda x:x["torus_rows"][1].update(period_three_cycles=0)),
      ("torus_point",lambda x:x["torus_rows"][1]["cycles"][1][1].__setitem__(0,0)),
      ("dirichlet_sum",lambda x:x["dirichlet_rows"][0].update(partial_sum=[1,1])),
      ("dirichlet_tail",lambda x:x["dirichlet_rows"][0].update(tail_upper=[0,1])),
      ("summary_count",lambda x:x["summary"].update(lattice_count=141)),
    ]
    rejected=[]
    for name,change in mutations:
        x=copy.deepcopy(base);change(x);x["payload_sha256"]=hashlib.sha256(check.canonical({k:v for k,v in x.items() if k!="payload_sha256"})).hexdigest()
        try:check.verify(x)
        except (AssertionError,ValueError,TypeError,IndexError,KeyError):rejected.append(name)
        else:raise AssertionError("mutation accepted: "+name)
    raw=check.EVAL.read_text()
    changes={"yaml_unknown":raw+"unknown_field: false\n","yaml_bool_integer":raw.replace("invokes_route_b: false","invokes_route_b: 0"),"yaml_unquoted_date":raw.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),"yaml_duplicate":raw+"candidate_id: HCS-C388\n"}
    with tempfile.TemporaryDirectory(prefix="c388-yaml-attack-") as d:
        for name,blob in changes.items():
            p=Path(d)/(name+".yaml");p.write_text(blob)
            try:check.evaluation(p)
            except (AssertionError,ValueError,TypeError):rejected.append(name)
            else:raise AssertionError("evaluation mutation accepted: "+name)
    # Exercise the real write entry point as well as the direct YAML gate.
    # A copy preserves the exact package ledger; the authority is copied into
    # the same relative repository layout. No released artifact is modified.
    with tempfile.TemporaryDirectory(prefix="c388-write-attack-") as d:
        sandbox=Path(d)
        package=sandbox/"henon_dynamics"/ROOT.name
        shutil.copytree(ROOT,package)
        authority=Path("flow_systems/skills/route-a-evaluator.md")
        (sandbox/authority).parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT.parents[1]/authority,sandbox/authority)
        for name,blob in changes.items():
            evaluation=package/"evaluations/route_a/HCS-C388/2026-09-05.yaml"
            evaluation.write_text(blob)
            attempt=subprocess.run([sys.executable,"-B",str(package/"code/c388_release_manifest.py"),"--write"],cwd=package,capture_output=True,text=True)
            assert attempt.returncode!=0 and "evaluation raw hash" in attempt.stdout+attempt.stderr,"write-mode gate did not reject YAML: "+name
            rejected.append("release_write_"+name)
    print("C388 repaired-hash/YAML mutation PASS: "+str(len(rejected))+"/"+str(len(mutations)+2*len(changes))+" "+",".join(rejected))
if __name__=="__main__":main()
