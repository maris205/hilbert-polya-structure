#!/usr/bin/env python3
"""Actual repaired-hash attacks, serialization attacks, and locked YAML attacks."""
if not __debug__: raise RuntimeError("c391 mutation refuses optimized Python")
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def setpath(d,path,value):
    for k in path[:-1]:d=d[k]
    d[path[-1]]=value
def run():
    original=json.loads((ROOT/"results/c391_evidence.json").read_text());attacks=[]
    def add(name,path,value):attacks.append((name,path,value))
    for flag in original["scope_flags"]:
        add("promote_"+flag,("scope_flags",flag),True)
    add("false_to_zero_scope",("scope_flags","invokes_route_b"),0)
    add("false_to_zero_route",("route_a","route_b_invocation_allowed"),0)
    add("false_to_zero_precision",("numerical_precision","interval_certified"),0)
    for name,path,value in (
      ("unknown",("extra",),1),("baseline",("source_commit",),"0"*40),("epoch_bool",("fixed_epoch",),True),
      ("tuple",("route_a","tuple",0),"A0_ANALYTIC_ARITHMETIC_ORIGIN"),("overall",("route_a","overall_verdict"),"ROUTE_A_PRIMARY_CANDIDATE"),
      ("authority",("evaluator","sha256"),"0"*64),("yaml_hash",("route_a_yaml","raw_sha256"),"0"*64),
      ("count_bool",("counts","classical"),True),("count_extra",("counts","extra"),0),
      ("collision_bool",("classical_rows",0,"finite_collision"),1),("periodic_bool",("classical_rows",0,"periodic"),0),
      ("rational_bool",("classical_rows",0,"sigma",0),True),("energy",("classical_rows",0,"energy"),[1,1]),
      ("discriminant",("classical_rows",0,"discriminant"),[0,1]),("component",("classical_rows",0,"clock_component"),"all_real"),
      ("boundary_type",("boundary_rows",0,"self_adjoint"),1),("boundary_flux",("boundary_rows",5,"flux_over_i"),[0,1]),
      ("unitary_type",("scattering_algebra_rows",0,"unitary"),1),("relative_phase",("scattering_algebra_rows",0,"relative_scattering"),[[0,1],[1,1]]),
      ("level_j_bool",("negative_levels",2,"j"),False),("level_energy",("negative_levels",0,"energy"),"1"),
      ("level_log",("negative_levels",0,"log_rho"),"0"),("level_normalizer",("negative_levels",0,"normalizer"),"0"),
      ("level_phase_bool",("negative_levels",0,"phase_pi",0),False),("level_kappa",("negative_levels",0,"kappa"),["0","0"]),
      ("density",("continuum_rows",0,"density"),"0"),("phi",("continuum_rows",0,"phi_at_7_over_10"),["0","0"]),
      ("numeric_nan",("continuum_rows",0,"density"),"nan"),("numeric_number",("continuum_rows",0,"density"),0),
      ("boundary_text",("theorem_boundary",),"target theorem")):
        add(name,path,value)
    cases=[]
    for name,path,value in attacks:
        d=copy.deepcopy(original);setpath(d,path,value);d.pop("payload_sha256");d["payload_sha256"]=hashlib.sha256(canon(d)).hexdigest()
        cases.append((name,json.dumps(d).encode()))
    raw=json.dumps(original).encode()
    serialization=[("duplicate_top",raw[:-1]+b',"candidate_id":"HCS-C391"}'),
      ("nonfinite",raw.replace(b'"fixed_epoch": 1788566400',b'"fixed_epoch": NaN')),
      ("truncated",raw[:-3]),("stale_hash",raw.replace(b'HCS-C391',b'HCS-C390',1))]
    y=(ROOT/"evaluations/route_a/HCS-C391/2026-09-05.yaml").read_text()
    yaml_attacks=[("unknown",y+"extra: 1\n"),("scope_zero",y.replace("  invokes_route_b: false","  invokes_route_b: 0")),
      ("route_zero",y.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0")),
      ("unquoted_date",y.replace("'2026-09-05'","2026-09-05")),("date_int",y.replace("'2026-09-05'","20260905")),
      ("duplicate",y+"candidate_id: HCS-C391\n"),("anchor",y.replace("training_data: none","training_data: &bad none")),
      ("alias",y+"extra: *bad\n"),("merge",y+"extra: {<<: {x: 1}}\n"),
      ("nested_ready_zero",y.replace("    route_b_ready: false","    route_b_ready: 0"))]
    with tempfile.TemporaryDirectory(prefix="c391-hostile-") as directory:
      work=Path(directory)
      for name,blob in cases+serialization:
        p=work/(name+".json");p.write_bytes(blob)
        result=subprocess.run([sys.executable,"-B",str(ROOT/"code/c391_checker.py"),str(p)],capture_output=True,text=True)
        assert result.returncode!=0,"accepted "+name
      for name,text in yaml_attacks:
        p=work/(name+".yaml");p.write_text(text)
        result=subprocess.run([sys.executable,"-B",str(ROOT/"code/c391_checker.py"),"--yaml-only","--yaml-path",str(p)],capture_output=True,text=True)
        assert result.returncode!=0,"accepted YAML "+name
        release=subprocess.run([sys.executable,"-B",str(ROOT/"code/c391_release_manifest.py"),"--write","--evaluation",str(p)],capture_output=True,text=True)
        assert release.returncode!=0,"accepted release-write YAML "+name
    report=dict(repaired_hash=len(cases),serialization=len(serialization),strict_yaml=len(yaml_attacks),release_write_yaml=len(yaml_attacks),distinct_mutations=len(cases)+len(serialization)+len(yaml_attacks),total_refusals=len(cases)+len(serialization)+2*len(yaml_attacks))
    print("C391 hostile PASS",json.dumps(report,sort_keys=True));return report
if __name__=="__main__":run()
