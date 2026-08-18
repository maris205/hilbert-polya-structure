#!/usr/bin/env python3
"""Physical nested-schema mutations against independent A and both Route validators."""
from __future__ import annotations
import argparse,json,os,subprocess,sys
from pathlib import Path
from typing import Any
SCIENCE=[
 ("N01","D","/payload/cutoffs/0/N","set",True),("N02","D","/payload/cutoffs/0/ordered_edges/0/0","set",True),
 ("N03","D","/payload/cutoffs/0/ordered_harmonic_quotients/0/quotient","set",True),("N04","D","/payload/adjacency_matrices/0/entries/0/0","set",True),
 ("N05","D","/payload/rows/5/m","set",True),("N06","D","/payload/walks/0/vertex_words/0/0","set",1.0),
 ("N07","D","/payload/trace_powers/0/method","set","renamed_method"),("N08","D","/payload/trace_powers/0/value/numerator","set",True),
 ("N09","P","/payload/coordinates/0/ordered_coordinates/0/t","set",True),("N10","P","/payload/coordinates/0/ordered_coordinates/0/quotient","set",99),
 ("N11","P","/payload/endpoint_controls/interval_diagnostics/0/bounded_compact","set",1),("N12","P","/payload/endpoint_controls/interval_diagnostics/0/sigma/numerator","set",0.0),
 ("N13","P","/payload/endpoint_controls/squarefree_degree_controls/0/degree","set",2),("N14","P","/payload/rectangular_mt_controls/0/domain","set","same_endpoint_domain"),
 ("N15","P","/payload/rectangular_mt_controls/0/primitive_scaled/numerator","set",True),("N16","P","/payload/phase_certificate/unexpected","add",False),
 ("N17","P","/payload/complex_phase_certificate/nonreal_operator_hermitian","set",0),("N18","P","/payload/trace_powers/0/method","set","shared_walk_method"),
 ("N19","X","/payload/direct_sha256","set","0"*64),("N20","X","/payload/checks/based_closed_walks","delete",None),
 ("N21","X","/payload/checks/finite_evidence_class","set",True),("N22","X","/payload/parameter_sha256","set",1.0)]
ROUTE=[
 ("N23","/source_lock/clock","set","harmonic_quotient"),("N24","/source_lock/forbidden_data/0","delete",None),
 ("N25","/a4/metrics/fixed_self_adjoint_operator_defined","set",0),("N26","/blocking_conditions/0","delete",None),
 ("N27","/typed_return_map/rational_prime_same_type_identification_exists","set",0),("N28","/authority_integration/authority_writes","set",False),
 ("N29","/a3/analytic_structure/gamma_factor","set",0),("N30","/terminal_codes/spectral_lift","set","STOP_SCOPED"),
 ("N31","/a2/artifacts/0","set","../DERIVATION_PACKAGE.md"),("N32","/adversarial_controls/controls_used/0","delete",None),
 ("N33","/authority_integration/status","set","DONE"),("N34","/authority_integration/status","set",True),
 ("N35","/authority_integration/status","set",1)]
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def mutate(obj:Any,path:str,operation:str,value:Any)->None:
 bits=path.split("/")[1:];cursor=obj
 for bit in bits[:-1]:cursor=cursor[int(bit)] if type(cursor) is list else cursor[bit]
 key=bits[-1]
 if operation=="delete":
  if type(cursor) is list:del cursor[int(key)]
  else:del cursor[key]
 elif operation in ("set","add"):
  if type(cursor) is list:cursor[int(key)]=value
  else:cursor[key]=value
 else:raise ValueError("operation")
def load(path:Path)->dict[str,Any]:
 raw=path.read_bytes();obj=json.loads(raw.decode("ascii"))
 if type(obj) is not dict or raw!=enc(obj):raise ValueError("canonical")
 return obj
def invoke(command:list[str],cwd:Path,hostile:Path)->subprocess.CompletedProcess[bytes]:
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(hostile),"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","LC_ALL":"C"}
 return subprocess.run(command,cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=120)
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False)
 for name in ("root","scratch","direct","parameter","comparison","route"):p.add_argument("--"+name,required=True)
 p.add_argument("--state",required=True,choices=["A","B"]);p.add_argument("--commit");a=p.parse_args()
 try:
  root=Path(a.root).resolve(strict=True);scratch=Path(a.scratch)
  if scratch.exists() or scratch.is_symlink():raise ValueError("scratch")
  scratch.mkdir(parents=True,mode=0o700);cwd=scratch/"cwd";hostile=scratch/"hostile";cwd.mkdir();hostile.mkdir();(hostile/"json.py").write_text("raise RuntimeError('shadow')\n",encoding="ascii")
  originals={"D":load(Path(a.direct)),"P":load(Path(a.parameter)),"X":load(Path(a.comparison))};records=[]
  for identifier,target,pointer,operation,value in SCIENCE:
   case=scratch/identifier;case.mkdir();mutated=json.loads(json.dumps(originals[target]));mutate(mutated,pointer,operation,value);path=case/(target+".json");path.write_bytes(enc(mutated))
   direct=path if target=="D" else Path(a.direct);parameter=path if target=="P" else Path(a.parameter);comparison=path if target=="X" else Path(a.comparison)
   command=[sys.executable,"-I","-B",str(root/"code/auditors/proof_result_auditor.py"),"--root",str(root),"--direct",str(direct),"--parameter",str(parameter),"--comparison",str(comparison)]
   result=invoke(command,cwd,hostile)
   if result.returncode!=3 or result.stdout or result.stderr!=b"A_ERROR:ValueError\n":raise ValueError("science nested survivor")
   records.append({"consumers":{"A":{"exit":3,"rejection":"A_ERROR:ValueError"}},"id":identifier,"operation":operation,"pointer":pointer,"survivor":False,"target":target})
  route0=load(Path(a.route));route_args=["--route","", "--root",str(root),"--state",a.state]+(["--commit",str(a.commit)] if a.state=="B" else [])
  for identifier,pointer,operation,value in ROUTE:
   case=scratch/identifier;case.mkdir();mutated=json.loads(json.dumps(route0));mutate(mutated,pointer,operation,value);path=case/"route.json";path.write_bytes(enc(mutated));observed={}
   for consumer,script in [("R1","validate_route.py"),("R2","audit_route_independent.py")]:
    args=list(route_args);args[1]=str(path);result=invoke([sys.executable,"-I","-B",str(root/"code/route"/script),*args],cwd,hostile)
    obj=json.loads(result.stdout.decode("ascii")) if result.stdout else None
    code="ROUTE_TERMINAL_FAILURE" if identifier=="N30" else "PROVENANCE_STATE_FAILURE" if identifier in ("N33","N34","N35") else "ROUTE_FULL_OBJECT_FAILURE"
    expected={"consumer":consumer,"rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"}
    if result.returncode!=2 or result.stderr or obj!=expected or result.stdout!=enc(obj):raise ValueError("Route nested survivor")
    observed[consumer]={"exit":2,"rejection":code}
   records.append({"consumers":observed,"id":identifier,"operation":operation,"pointer":pointer,"survivor":False,"target":"ROUTE"})
  out={"candidate_id":"SD-C49","payload":{"consumer_invocation_count":48,"instance_count":35,"records":records,"survivors":0},"schema":"paper47-expanded-mutation-results-v1","status":"PASS"};sys.stdout.buffer.write(enc(out))
 except Exception as e:sys.stderr.write(f"EXPANDED_MUTATION_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
