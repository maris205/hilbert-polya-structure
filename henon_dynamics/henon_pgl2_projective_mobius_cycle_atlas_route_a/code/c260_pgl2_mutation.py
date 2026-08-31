#!/usr/bin/env python3
"""Semantic hostile mutations for HCS-C260."""
import copy,json,os,subprocess,sys,tempfile
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];EVIDENCE=ROOT/"results/c260_pgl2_evidence.json";CHECKER=ROOT/"code/c260_pgl2_checker.py"
def phash(d):
 b=dict(d);b.pop("payload_sha256",None);return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
BASE=json.loads(EVIDENCE.read_text())
M=[
(["schema"],"bad"),(["candidate_id"],"HCS-C259"),(["source_commit"],"0"*40),(["fixed_epoch"],0),(["scope_literal"],"BAD"),
(["evaluator","path"],"bad.md"),(["evaluator","version"],"0.1.0"),(["evaluator","sha256"],"0"*64),
(["frozen_object","phase_space"],"P1(R)"),(["frozen_object","map"],"x+1"),(["frozen_object","clock"],"two updates"),
(["frozen_object","determinant_convention"],"target determinant"),(["frozen_object","arithmetic_origin"],"fitted primes"),
(["theorem","classification"],"three types"),(["theorem","identity"],"1^q"),(["theorem","unipotent"],"order q"),
(["theorem","split"],"order d|q+1"),(["theorem","nonsplit"],"order d|q-1"),(["theorem","fixed"],"always q+1"),
(["theorem","primitive"],"no Mobius inversion"),(["theorem","zeta"],"target zeta"),(["theorem","koopman"],"nonunitary"),
(["theorem","reversor"],"none"),(["theorem","characteristic_two"],"use discriminant square"),(["theorem","type_census"],"unipotent q"),
(["regression","field_count"],17),(["regression","field_values"],[2,3]),(["regression","enumerated_pgl_elements"],0),
(["regression","direct_state_images"],0),(["regression","field_rows",0,"q"],3),
(["regression","field_rows",2,"order_histograms","nonsplit"],{}),(["regression","field_rows",7,"element_record_sha256"],"0"*64),
(["route_a","tuple"],["A0_FAIL"]),(["route_a","overall"],"ROUTE_A_STRONG"),(["route_a","route_b_invocation_allowed"],True),
(["scope_flags","claims_euler_factors"],True),(["scope_flags","claims_hilbert_polya_operator"],True),
(["citations",0,"doi"],"10.fake"),(["nonclaims"],[]),(["exact_identities"],[]),
]
def mutated(path,val):
 d=copy.deepcopy(BASE);n=d
 for k in path[:-1]:n=n[k]
 n[path[-1]]=val;d["payload_sha256"]=phash(d);return d
passed=0;env=dict(os.environ);env["PYTHONDONTWRITEBYTECODE"]="1"
with tempfile.TemporaryDirectory(prefix="c260-mutation-") as td:
 for i,(path,val) in enumerate(M):
  f=Path(td)/f"m{i}.json";f.write_text(json.dumps(mutated(path,val),sort_keys=True,indent=2)+"\n")
  r=subprocess.run([sys.executable,"-B",str(CHECKER),"--quick","--evidence",str(f)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  if r.returncode==0:raise AssertionError(f"mutation survived: {path}")
  passed+=1
print(f"C260 hostile mutation: PASS {passed}/{len(M)}")
