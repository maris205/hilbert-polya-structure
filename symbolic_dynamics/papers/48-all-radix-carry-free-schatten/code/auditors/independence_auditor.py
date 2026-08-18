#!/usr/bin/env python3
"""Static independence firewall auditor I."""
from __future__ import annotations
import argparse,ast,hashlib,json,re,sys
from pathlib import Path
from typing import Any
ATTACKS={
 ("independence","/independence/source_trees","shared_helper"):"SHARED_PRODUCTION_SOURCE",
 ("independence","/independence/case_expansion","shared_serialized_fixture"):"SHARED_GENERATED_FIXTURE",
 ("comparison","/comparison/tolerance","selected_after_outputs"):"POSTHOC_TOLERANCE",
}
class IndependenceReject(Exception):
 def __init__(self,code):self.code=code
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def load(p):return json.loads(Path(p).read_text(encoding="ascii"))
def attack(p):
 o=load(p)
 if set(o)!={"domain","target","value_from","value_to"}:raise ValueError("attack")
 code=ATTACKS.get((o["domain"],o["target"],o["value_to"]))
 payload={"consumer":"I","exit_code":2,"outcome":"REJECT","code":code} if code else {"consumer":"I","exit_code":0,"outcome":"ACCEPT"}
 sys.stdout.buffer.write(enc(payload));return payload["exit_code"]
def model_code(model):
 if model.get("independence",{}).get("source_trees")!="disjoint":return "SHARED_PRODUCTION_SOURCE"
 if model.get("independence",{}).get("case_expansion")!="independent":return "SHARED_GENERATED_FIXTURE"
 if model.get("comparison",{}).get("tolerance")!="predeclared":return "POSTHOC_TOLERANCE"
 return None
def imports(path):
 tree=ast.parse(path.read_text(encoding="utf-8"));out=[]
 for n in ast.walk(tree):
  if isinstance(n,ast.Import):out += [a.name for a in n.names]
  elif isinstance(n,ast.ImportFrom):out.append(n.module or "")
 return out
def audit(root,allow_outputs=False):
 a=root/"code/evaluator_a/evaluate.py";b=root/"code/evaluator_b/evaluate.py"
 if a.samefile(b) or hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest():raise ValueError("shared source")
 for path in (a,b):
  bad=[x for x in imports(path) if x.startswith("code.") or "evaluator_" in x or x in {"common","helpers"}]
  if bad:raise ValueError("local import")
 ta=a.read_text();tb=b.read_text()
 if "def carry_free" not in ta or "repeated_quotient" not in ta and "quotient" not in ta:raise ValueError("A direct")
 if "def automaton_accepts" not in tb or "def kappa" not in tb or "analytic_digit_spectrum" not in tb:raise ValueError("B digit")
 if "analytic_digit_spectrum" in ta or "def carry_free" in tb:raise ValueError("method bleed")
 if "independent_expansion" not in tb or "def expand" not in ta or "mask_set" not in tb or "def masks" not in ta:raise ValueError("independent expansion")
 model=load(root/"contracts/SCIENCE_MODEL.json")
 code=model_code(model)
 if code:raise IndependenceReject(code)
 if model["independence"]!={"case_expansion":"independent","source_trees":"disjoint"} or model["comparison"]["tolerance"]!="predeclared":raise ValueError("model")
 if (root/"outputs").exists() and not allow_outputs:raise ValueError("candidate output state")
 return {"a_source_sha256":hashlib.sha256(a.read_bytes()).hexdigest(),"b_source_sha256":hashlib.sha256(b.read_bytes()).hexdigest(),"candidate_id":"SD-C50","consumer":"I","independent_case_expansion":True,"schema":"paper48.independence-audit.v1","status":"PASS"}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path);p.add_argument("--attack",type=Path);p.add_argument("--allow-outputs",action="store_true")
 try:
  x=p.parse_args()
  if x.attack:
   if x.root or x.allow_outputs:raise ValueError("arity")
   return attack(x.attack)
  if not x.root:raise ValueError("arity")
  sys.stdout.buffer.write(enc(audit(x.root.resolve(strict=True),x.allow_outputs)));return 0
 except IndependenceReject as e:
  sys.stdout.buffer.write(enc({"code":e.code,"consumer":"I","exit_code":2,"outcome":"REJECT"}));return 2
 except Exception as e:sys.stderr.write(f"I_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
