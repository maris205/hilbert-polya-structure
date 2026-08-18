#!/usr/bin/env python3
"""Second, separately implemented full-object Route validator."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from pathlib import Path
from typing import Any
import yaml
MUTATED={("route","/evaluation_state","EVALUATED"):"ROUTE_EXPECTATION_RETYPE",("route","/overall_verdict","STOP_DUPLICATE"):"STOP_DUPLICATE_AS_ROUTE_TERMINAL",("route","/route_tuple/0","A0_WEAK_ARITHMETIC_RELATION"):"ROUTE_TUPLE_DRIFT",("route","/route_b/invocation_allowed",True):"ROUTE_B_UNLOCKED"}
class RouteReject(Exception):
 def __init__(self,code):self.code=code
def dump(x:Any)->bytes:return (json.dumps(x,ensure_ascii=True,sort_keys=True,indent=2,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def unique(seq):
 result={}
 for name,value in seq:
  if name in result:raise ValueError("duplicate")
  result[name]=value
 return result
def parse(path):
 raw=Path(path).read_bytes();value=json.loads(raw.decode("ascii"),object_pairs_hook=unique)
 if value.__class__ is not dict or dump(value)!=raw:raise ValueError("stored object")
 return value
def hash_bytes(raw):return hashlib.sha256(raw).hexdigest()
def attack(path):
 x=parse(path)
 if sorted(x)!=["domain","target","value_from","value_to"]:raise ValueError("attack")
 code=MUTATED.get((x["domain"],x["target"],x["value_to"]));answer={"consumer":"R_INDEPENDENT","exit_code":2,"outcome":"REJECT","code":code} if code else {"consumer":"R_INDEPENDENT","exit_code":0,"outcome":"ACCEPT"};sys.stdout.buffer.write(dump(answer));return answer["exit_code"]
def reconstruct(root,state,static,commit):
 base=yaml.safe_load((root/"preauthority/ROUTE_EXPECTATION.yaml").read_bytes())
 exact_tuple=["A0_FAIL","A1_FAIL","A2_ANALYTIC_DETERMINANT","A3_FAIL","A4_FAIL"]
 if base["evaluation_state"]!="NOT_RUN_EXPECTATION_ONLY" or base["route_tuple"]!=exact_tuple or base["overall_verdict"]!="ROUTE_A_REJECTED":raise ValueError("base")
 if base["route_b_invocation_allowed"] is not False or base["route_b"]["invocation_allowed"] is not False:raise ValueError("base B")
 if state=="A":
  if commit is not None:raise ValueError("mixed A")
  state_status="PREAUTHORITY_INTEGRATION"
 else:
  if commit.__class__ is not str or not re.fullmatch("[0-9a-f]{40}",commit) or commit==40*"0":raise ValueError("mixed B")
  state_status="PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 base["artifact_bindings"]={"experiment_contract_sha256":hash_bytes((root/"preauthority/EXPERIMENT_CONTRACT.json").read_bytes()),"preauthority_manifest_sha256":"f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057","proof_package_sha256":hash_bytes((root/"preauthority/PROOF_PACKAGE.md").read_bytes()),"static_inventory_sha256":static}
 base["integration"]={"authority_write_authorized":False,"commit":commit,"state":state,"status":state_status};base["schema"]="paper48.route-a.v0.2.0";return base
def verify(root,route,state,static,commit):
 got=parse(route);required_status="PREAUTHORITY_INTEGRATION" if state=="A" else "PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 if got.get("integration",{}).get("status")!=required_status:raise RouteReject("PROVENANCE_STATE_FAILURE")
 if got.get("evaluation_state")=="EVALUATED":raise RouteReject("ROUTE_EXPECTATION_RETYPE")
 if got.get("evaluation_state")!="NOT_RUN_EXPECTATION_ONLY":raise RouteReject("ROUTE_FULL_OBJECT_FAILURE")
 if got.get("overall_verdict")=="STOP_DUPLICATE":raise RouteReject("STOP_DUPLICATE_AS_ROUTE_TERMINAL")
 if got.get("route_tuple",[None])[0]=="A0_WEAK_ARITHMETIC_RELATION":raise RouteReject("ROUTE_TUPLE_DRIFT")
 if got.get("route_b",{}).get("invocation_allowed") is True:raise RouteReject("ROUTE_B_UNLOCKED")
 if got.get("overall_verdict")!="ROUTE_A_REJECTED" or got.get("route_b",{}).get("invocation_allowed") is not False or got.get("route_b_invocation_allowed") is not False:raise RouteReject("ROUTE_TERMINAL_FAILURE")
 if got.get("route_tuple")!=["A0_FAIL","A1_FAIL","A2_ANALYTIC_DETERMINANT","A3_FAIL","A4_FAIL"]:raise RouteReject("ROUTE_FULL_OBJECT_FAILURE")
 expected=reconstruct(root,state,static,commit)
 if got!=expected or dump(got)!=dump(expected):raise RouteReject("ROUTE_FULL_OBJECT_FAILURE")
 raw=dump(got);return {"candidate_id":"SD-C50","consumer":"R_INDEPENDENT","full_normalized_route_sha256":hash_bytes(raw),"route_sha256":hash_bytes(Path(route).read_bytes()),"schema":"paper48.independent-evaluation.v1","state":state,"status":"PASS"}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path);p.add_argument("--route",type=Path);p.add_argument("--state",choices=("A","B"));p.add_argument("--static-digest");p.add_argument("--commit");p.add_argument("--attack",type=Path)
 try:
  x=p.parse_args()
  if x.attack:
   if any(v is not None for v in (x.root,x.route,x.state,x.static_digest,x.commit)):raise ValueError("arity")
   return attack(x.attack)
  if x.root is None or x.route is None or x.state is None or x.static_digest is None or re.fullmatch("[0-9a-f]{64}",x.static_digest) is None:raise ValueError("arity")
  sys.stdout.buffer.write(dump(verify(x.root.resolve(strict=True),x.route.resolve(strict=True),x.state,x.static_digest,x.commit)));return 0
 except RouteReject as e:sys.stdout.buffer.write(dump({"code":e.code,"consumer":"R_INDEPENDENT","exit_code":2,"outcome":"REJECT"}));return 2
 except Exception as e:sys.stderr.write(f"R_INDEPENDENT_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
