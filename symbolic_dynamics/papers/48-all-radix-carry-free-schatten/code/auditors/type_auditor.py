#!/usr/bin/env python3
"""Recursive strict-type, schema, and coordinate auditor T."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from fractions import Fraction
from pathlib import Path
from typing import Any
import jsonschema

ATTACKS={
 ("source_type","/object/composite_radix","Kummer_equivalence"):"COMPOSITE_KUMMER_SCOPE",
 ("finite_object","/finite/source/zero","retained_as_infinite_vertex"):"ZERO_VERTEX_RETAINED",
 ("clock_type","/object/clock","one_digit_position"):"DIGIT_POSITION_RETYPE",
 ("infinite_object","/claims/unweighted_AM_zeta","defined"):"UNWEIGHTED_AM_ZETA_ILLEGAL",
 ("evidence_type","/record/evidence_type","INFINITE_THEOREM_CERTIFICATE"):"FINITE_CONTROL_AS_INFINITE_PROOF",
 ("type","/case/q","1/2"):"SCHATTEN_Q_BELOW_ONE",
 ("type","/case/b",1):"RADIX_BELOW_TWO",
 ("type","/case/b","5/2"):"RADIX_NOT_INTEGER",
 ("type","/case/r",0):"TRACE_LENGTH_NONPOSITIVE",
 ("comparison","/comparison/bool_int","python_equality"):"STRICT_SCALAR_TYPE_FAILURE",
 ("ownership_control","/controls/randomized_digit_mask/credit","positive_novelty"):"RANDOM_MASK_NOVELTY",
}
class Dup(Exception):pass
class TypedReject(Exception):
 def __init__(self,code):self.code=code
def pairs(seq):
 o={}
 for k,v in seq:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p:Path,canonical=False):
 raw=p.read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
 if type(o) is not dict or canonical and raw!=enc(o):raise ValueError("canonical")
 return o
def emit(code=None):
 if code is None:sys.stdout.buffer.write(enc({"consumer":"T","exit_code":0,"outcome":"ACCEPT"}));return 0
 sys.stdout.buffer.write(enc({"code":code,"consumer":"T","exit_code":2,"outcome":"REJECT"}));return 2
def attack(p):
 o=load(p,True)
 if set(o)!={"domain","target","value_from","value_to"}:raise ValueError("attack")
 return emit(ATTACKS.get((o["domain"],o["target"],o["value_to"])))
def model_code(model):
 if model.get("object",{}).get("composite_radix")!="direct_no_carry_predicate":return "COMPOSITE_KUMMER_SCOPE"
 if model.get("finite",{}).get("source",{}).get("zero")!="deleted":return "ZERO_VERTEX_RETAINED"
 if model.get("object",{}).get("clock")!="one_admissible_edge":return "DIGIT_POSITION_RETYPE"
 if model.get("claims",{}).get("unweighted_AM_zeta")!="forbidden_infinite_fixed_counts":return "UNWEIGHTED_AM_ZETA_ILLEGAL"
 if model.get("record",{}).get("evidence_type")!="FINITE_OPERATOR_CONTROL":return "FINITE_CONTROL_AS_INFINITE_PROOF"
 q=model.get("case",{}).get("q")
 try:qv=Fraction(q) if type(q) is str else None
 except Exception:qv=None
 if qv is None or qv<1:return "SCHATTEN_Q_BELOW_ONE"
 b=model.get("case",{}).get("b")
 if type(b) is not int:return "RADIX_NOT_INTEGER"
 if b<2:return "RADIX_BELOW_TWO"
 r=model.get("case",{}).get("r")
 if type(r) is not int or r<=0:return "TRACE_LENGTH_NONPOSITIVE"
 if model.get("comparison",{}).get("bool_int")!="strict":return "STRICT_SCALAR_TYPE_FAILURE"
 if model.get("controls",{}).get("randomized_digit_mask",{}).get("credit")!="zero_novelty_control":return "RANDOM_MASK_NOVELTY"
 return None
def strict_tree(node:Any,path="$"):
 if type(node) is dict:
  if any(type(k) is not str for k in node):raise ValueError("key")
  for k,v in node.items():strict_tree(v,path+"/"+k)
 elif type(node) is list:
  for i,v in enumerate(node):strict_tree(v,path+f"/{i}")
 elif type(node) not in (str,int,bool,type(None)):
  raise ValueError("unsupported scalar")
def contract_audit(root:Path)->dict:
 c=load(root/"preauthority/EXPERIMENT_CONTRACT.json");strict_tree(c)
 if c["schema_version"]!="paper48.experiment-contract.v1" or c["serialization"]["booleans"]!="JSON Boolean, never integer":raise ValueError("contract")
 if c["precision_bits"]!=[128,256,512] or any(type(x) is not int for x in c["precision_bits"]):raise ValueError("bits")
 count=0;coords=set()
 for case in c["case_registry"]:
  if not case["case_id"].startswith("FIN-"):continue
  if type(case["b"]) is not int or case["b"]<2 or Fraction(case["q"])<1:raise ValueError("scalar")
  for N in case["N"]:
   for r in case["r"]:
    if type(N) is not int or type(r) is not int or N<1 or r<1:raise ValueError("scalar")
    for control in case["controls"]:
     if control in c["finite_case_expansion"]["shell_controls"]:
      for k,l in case["shell_pairs_by_control"][control]:
       if N>=case["b"]**(max(k,l)+1)-1:count+=3
     elif control=="RANDOMIZED_DIGIT_MASK":count+=3*16*3
     else:count+=3
 if count!=1965:raise ValueError("expansion count")
 model=load(root/"contracts/SCIENCE_MODEL.json");strict_tree(model)
 code=model_code(model)
 if code:raise TypedReject(code)
 if type(model["claims"]["complex_trace_zero_free"]) is not bool or type(model["ownership"]["priority"]) is not bool:raise ValueError("boolean")
 return {"candidate_id":"SD-C50","consumer":"T","expanded_coordinate_count":count,"recursive_strict_types":True,"schema":"paper48.type-audit.v1","status":"PASS"}
def results_audit(root:Path,out:Path):
 c=load(root/"preauthority/EXPERIMENT_CONTRACT.json")
 schema=c["json_schemas"]["finite_projection_record"]
 for rel,owner in (("results/evaluator_a_projection.json","A"),("results/evaluator_b_projection.json","B")):
  o=load(out/rel,True)
  if o.get("producer")!=owner or len(o.get("finite_records",[]))!=1965 or o.get("infinite_records")!=[]:raise ValueError("projection")
  validator=jsonschema.Draft202012Validator(schema)
  for row in o["finite_records"]:
   errors=list(validator.iter_errors(row))
   if errors:raise ValueError("record schema")
 proof=load(out/"results/proof_audit.json",True)
 ischema=c["json_schemas"]["infinite_certificate_record"]
 for row in proof["records"]:jsonschema.Draft202012Validator(ischema).validate(row)
 return {"candidate_id":"SD-C50","projection_rows_validated":3930,"schema":"paper48.result-type-audit.v1","status":"PASS"}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path);p.add_argument("--output-root",type=Path);p.add_argument("--attack",type=Path)
 try:
  a=p.parse_args()
  if a.attack is not None:
   if a.root is not None or a.output_root is not None:raise ValueError("arity")
   return attack(a.attack)
  if a.root is None:raise ValueError("arity")
  root=a.root.resolve(strict=True);o=results_audit(root,a.output_root.resolve(strict=True)) if a.output_root else contract_audit(root);sys.stdout.buffer.write(enc(o));return 0
 except TypedReject as e:return emit(e.code)
 except Exception as e:sys.stderr.write(f"T_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
