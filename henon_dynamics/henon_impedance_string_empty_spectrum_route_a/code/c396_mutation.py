#!/usr/bin/env python3
"""Hash-repaired semantic attacks and actual release-write YAML refusals."""
if not __debug__: raise RuntimeError("c396 mutation refuses optimized Python")
import copy
import hashlib
import importlib.util
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
    original=json.loads((ROOT/"results/c396_evidence.json").read_text());attacks=[]
    def add(name,path,value):attacks.append((name,path,value))
    for flag in original["scope_flags"]:add("promote_"+flag,("scope_flags",flag),True)
    for name,path,value in (
      ("scope_zero",("scope_flags","invokes_route_b"),0),("route_zero",("route_a","route_b_invocation_allowed"),0),("precision_zero",("numerical_precision","interval_certified"),0),
      ("unknown",("extra",),1),("baseline",("source_commit",),"0"*40),("epoch_bool",("fixed_epoch",),True),
      ("tuple",("route_a","tuple",0),"A0_ANALYTIC_ARITHMETIC_ORIGIN"),("overall",("route_a","overall_verdict"),"ROUTE_A_PRIMARY_CANDIDATE"),
      ("authority",("evaluator","sha256"),"0"*64),("yaml_hash",("route_a_yaml","raw_sha256"),"0"*64),
      ("count_bool",("counts","boundary"),True),("count_extra",("counts","extra"),0),
      ("conservative_type",("boundary_rows",0,"conservative"),1),("transparent_type",("boundary_rows",0,"transparent"),0),
      ("q_sign",("boundary_rows",0,"q"),[1,1]),("flux_sign",("boundary_rows",1,"flux"),[1,1]),
      ("eta_bool",("boundary_rows",0,"eta",0),False),("extinct_type",("transport_rows",0,"extinct"),0),
      ("crossings_bool",("transport_rows",0,"crossings"),False),("remainder",("transport_rows",0,"remainder"),[0,1]),
      ("amplitude",("transport_rows",0,"amplitude"),[0,1]),("norm",("transport_rows",0,"operator_norm"),[0,1]),
      ("transport_extra",("transport_rows",0,"extra"),0),("n_bool",("spectrum_rows",3,"n"),False),
      ("eigenvalue",("spectrum_rows",0,"eigenvalue"),["0","0"]),("condition",("spectrum_rows",0,"similarity_condition"),"2"),
      ("branch",("pseudospectrum_rows",0,"branch"),"critical"),("parameter_bool",("pseudospectrum_rows",0,"parameter",0),True),
      ("real_part",("pseudospectrum_rows",0,"real_part"),"0"),("pseudo_norm",("pseudospectrum_rows",0,"resolvent_norm"),"0"),
      ("mu",("pseudospectrum_rows",0,"least_mu"),"0"),("hs",("pseudospectrum_rows",0,"hs_squared"),"0"),
      ("green",("green_rows",0,"w_third"),["0","0"]),("numeric_nan",("green_rows",0,"w_third"),["nan","0"]),
      ("numeric_int",("green_rows",0,"w_third"),[0,"0"]),("boundary_text",("theorem_boundary",),"target theorem")):
        add(name,path,value)
    cases=[]
    for name,path,value in attacks:
        d=copy.deepcopy(original);setpath(d,path,value);d.pop("payload_sha256");d["payload_sha256"]=hashlib.sha256(canon(d)).hexdigest();cases.append((name,json.dumps(d).encode()))
    raw=json.dumps(original).encode()
    serial=[("duplicate",raw[:-1]+b',"candidate_id":"HCS-C396"}'),("nonfinite",raw.replace(b'"fixed_epoch": 1788566400',b'"fixed_epoch": NaN')),("truncated",raw[:-3]),("stale",raw.replace(b'HCS-C396',b'HCS-C395',1))]
    y=(ROOT/"evaluations/route_a/HCS-C396/2026-09-05.yaml").read_text()
    ycases=[("unknown",y+"extra: 1\n"),("scope_zero",y.replace("  invokes_route_b: false","  invokes_route_b: 0")),("route_zero",y.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0")),("unquoted_date",y.replace("'2026-09-05'","2026-09-05")),("date_int",y.replace("'2026-09-05'","20260905")),("duplicate",y+"candidate_id: HCS-C396\n"),("anchor",y.replace("training_data: none","training_data: &bad none")),("alias",y+"extra: *bad\n"),("merge",y+"extra: {<<: {x: 1}}\n"),("nested_ready",y.replace("    route_b_ready: false","    route_b_ready: 0"))]
    with tempfile.TemporaryDirectory(prefix="c396-hostile-") as directory:
      work=Path(directory)
      for name,blob in cases+serial:
        path=work/(name+".json");path.write_bytes(blob)
        p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c396_checker.py"),str(path)],capture_output=True,text=True)
        assert p.returncode!=0,"accepted "+name
      for name,content in ycases:
        path=work/(name+".yaml");path.write_text(content)
        for cmd in ([sys.executable,"-B",str(ROOT/"code/c396_checker.py"),"--yaml-only","--yaml-path",str(path)],[sys.executable,"-B",str(ROOT/"code/c396_release_manifest.py"),"--write","--evaluation",str(path)]):
          p=subprocess.run(cmd,capture_output=True,text=True);assert p.returncode!=0,"accepted YAML "+name
      authority=work/"hostile-evaluator.md"
      authority.write_bytes((ROOT.parents[1]/"flow_systems/skills/route-a-evaluator.md").read_bytes()+b"\nunauthorized change\n")
      for script,args in (("c396_checker.py",["--yaml-only"]),("c396_release_manifest.py",["--write"])):
        p=subprocess.run([sys.executable,"-B",str(ROOT/"code"/script),*args,"--authority-path",str(authority)],capture_output=True,text=True)
        assert p.returncode and "live evaluator bytes changed" in p.stdout+p.stderr,"authority change accepted"
      # Exercise the actual release main(--write) on two temporary physical trees.
      spec=importlib.util.spec_from_file_location("c396_hostile_release",ROOT/"code/c396_release_manifest.py")
      release=importlib.util.module_from_spec(spec);spec.loader.exec_module(release)
      saved_argv=sys.argv[:]
      try:
        for name in ("hidden_extra","symlink"):
          tree=work/name;tree.mkdir();release.ROOT=tree;release.MANIFEST=tree/"C396_RELEASE_MANIFEST.json"
          if name=="hidden_extra":
            fixture=tree/"code/__pycache__/unlisted.txt";fixture.parent.mkdir(parents=True);fixture.write_text("extra")
          else:
            fixture=tree/"proof/ANALYTIC_PROOF.md";fixture.parent.mkdir();fixture.symlink_to(ROOT/"proof/ANALYTIC_PROOF.md")
          def state():
            return {str(p.relative_to(tree)):("link",str(p.readlink())) if p.is_symlink() else ("file",hashlib.sha256(p.read_bytes()).hexdigest()) if p.is_file() else ("directory","") for p in tree.rglob("*")}
          before=state();sys.argv=["c396_release_manifest.py","--write"]
          try:release.main()
          except AssertionError as exc:assert ("unlisted payload" if name=="hidden_extra" else "symlink forbidden") in str(exc)
          else:raise AssertionError("physical attack accepted: "+name)
          assert before==state()
      finally:sys.argv=saved_argv
    report=dict(repaired_hash=len(cases),serialization=len(serial),strict_yaml=len(ycases),release_write_yaml=len(ycases),authority=1,authority_refusals=2,physical_write_refusals=2,distinct_mutations=len(cases)+len(serial)+len(ycases)+3,total_refusals=len(cases)+len(serial)+2*len(ycases)+4)
    print("C396 hostile PASS",json.dumps(report,sort_keys=True));return report
if __name__=="__main__":run()
