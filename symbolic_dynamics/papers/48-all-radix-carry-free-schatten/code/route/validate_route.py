#!/usr/bin/env python3
"""Primary strict full-object Route validator R_MAIN."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from pathlib import Path
from typing import Any
import yaml
ATTACKS={
 ("route","/evaluation_state","EVALUATED"):"ROUTE_EXPECTATION_RETYPE",
 ("route","/overall_verdict","STOP_DUPLICATE"):"STOP_DUPLICATE_AS_ROUTE_TERMINAL",
 ("route","/route_tuple/0","A0_WEAK_ARITHMETIC_RELATION"):"ROUTE_TUPLE_DRIFT",
 ("route","/route_b/invocation_allowed",True):"ROUTE_B_UNLOCKED",
}
class RouteReject(Exception):
 def __init__(self,code):self.code=code
class Dup(Exception):pass
def pairs(seq):
 o={}
 for k,v in seq:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p):
 raw=Path(p).read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise ValueError("canonical")
 return o
def h(raw):return hashlib.sha256(raw).hexdigest()
def emit(code=None):
 x={"consumer":"R_MAIN","exit_code":2,"outcome":"REJECT","code":code} if code else {"consumer":"R_MAIN","exit_code":0,"outcome":"ACCEPT"};sys.stdout.buffer.write(enc(x));return x["exit_code"]
def attacked(p):
 o=load(p)
 if set(o)!={"domain","target","value_from","value_to"}:raise ValueError("attack")
 return emit(ATTACKS.get((o["domain"],o["target"],o["value_to"])))
def expected(root,state,static,commit):
 x=yaml.safe_load((root/"preauthority/ROUTE_EXPECTATION.yaml").read_text())
 if x.get("evaluation_state")!="NOT_RUN_EXPECTATION_ONLY":raise ValueError("expectation status exact")
 status="PREAUTHORITY_INTEGRATION" if state=="A" else "PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 if state=="A" and commit is not None:raise ValueError("A provenance")
 if state=="B" and (type(commit) is not str or re.fullmatch(r"[0-9a-f]{40}",commit) is None or commit=="0"*40):raise ValueError("B provenance")
 return {**x,"artifact_bindings":{"experiment_contract_sha256":h((root/"preauthority/EXPERIMENT_CONTRACT.json").read_bytes()),"preauthority_manifest_sha256":"f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057","proof_package_sha256":h((root/"preauthority/PROOF_PACKAGE.md").read_bytes()),"static_inventory_sha256":static},"integration":{"authority_write_authorized":False,"commit":commit,"state":state,"status":status},"schema":"paper48.route-a.v0.2.0"}
def validate(root,route,state,static,commit):
 actual=load(route)
 # Exact state status is checked before any normalized comparison.
 wanted_status="PREAUTHORITY_INTEGRATION" if state=="A" else "PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 if type(actual.get("integration")) is not dict or actual["integration"].get("status")!=wanted_status:raise RouteReject("PROVENANCE_STATE_FAILURE")
 if actual.get("evaluation_state")=="EVALUATED":raise RouteReject("ROUTE_EXPECTATION_RETYPE")
 if actual.get("evaluation_state")!="NOT_RUN_EXPECTATION_ONLY":raise RouteReject("ROUTE_FULL_OBJECT_FAILURE")
 if actual.get("overall_verdict")=="STOP_DUPLICATE":raise RouteReject("STOP_DUPLICATE_AS_ROUTE_TERMINAL")
 if actual.get("route_tuple",[None])[0]=="A0_WEAK_ARITHMETIC_RELATION":raise RouteReject("ROUTE_TUPLE_DRIFT")
 if actual.get("route_b",{}).get("invocation_allowed") is True:raise RouteReject("ROUTE_B_UNLOCKED")
 if actual.get("overall_verdict")!="ROUTE_A_REJECTED" or actual.get("route_b",{}).get("invocation_allowed") is not False or actual.get("route_b_invocation_allowed") is not False:raise RouteReject("ROUTE_TERMINAL_FAILURE")
 if actual.get("route_tuple")!=["A0_FAIL","A1_FAIL","A2_ANALYTIC_DETERMINANT","A3_FAIL","A4_FAIL"]:raise RouteReject("ROUTE_FULL_OBJECT_FAILURE")
 target=expected(root,state,static,commit)
 if enc(actual)!=enc(target):raise RouteReject("ROUTE_FULL_OBJECT_FAILURE")
 if actual["route_tuple"]!=["A0_FAIL","A1_FAIL","A2_ANALYTIC_DETERMINANT","A3_FAIL","A4_FAIL"] or actual["overall_verdict"]!="ROUTE_A_REJECTED" or actual["route_b"]["invocation_allowed"] is not False or actual["route_b_invocation_allowed"] is not False:raise ValueError("ROUTE_TERMINAL_FAILURE")
 raw=enc(actual)
 return {"candidate_id":"SD-C50","consumer":"R_MAIN","full_normalized_route_sha256":h(raw),"route_sha256":h(Path(route).read_bytes()),"schema":"paper48.main-evaluation.v1","state":state,"status":"PASS"}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path);p.add_argument("--route",type=Path);p.add_argument("--state",choices=["A","B"]);p.add_argument("--static-digest");p.add_argument("--commit");p.add_argument("--attack",type=Path)
 try:
  a=p.parse_args()
  if a.attack:
   if any(x is not None for x in (a.root,a.route,a.state,a.static_digest,a.commit)):raise ValueError("arity")
   return attacked(a.attack)
  if None in (a.root,a.route,a.state,a.static_digest) or re.fullmatch(r"[0-9a-f]{64}",a.static_digest) is None:raise ValueError("arity")
  sys.stdout.buffer.write(enc(validate(a.root.resolve(strict=True),a.route.resolve(strict=True),a.state,a.static_digest,a.commit)));return 0
 except RouteReject as e:sys.stdout.buffer.write(enc({"code":e.code,"consumer":"R_MAIN","exit_code":2,"outcome":"REJECT"}));return 2
 except Exception as e:sys.stderr.write(f"R_MAIN_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
