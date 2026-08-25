#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C152."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c152_heat_evidence.json"; CHECKER=ROOT/"code/c152_heat_checker.py"
def ph(data):
    work=dict(data);work.pop("payload_sha256",None)
    return sha256(json.dumps(work,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def put(data,path,value):
    target=data
    for key in path[:-1]:target=target[key]
    target[path[-1]]=value
def main():
    source=json.loads(EVIDENCE.read_text())
    mutations=[
      ("schema",("schema",),"x"),("candidate",("candidate_id",),"x"),("date",("evaluation_date",),"x"),("commit",("source_commit",),"x"),("scope",("scope_literal",),"x"),
      ("convention",("source_lock","direction_convention"),"unordered"),("length",("source_lock","length"),"L=sqrt"),("cutoff",("source_lock","cutoff","coefficient_s_max"),100),("precision",("source_lock","precision"),"float"),
      ("ledger_s",("coefficient_ledger",3,"s=m2+n2"),999),("ledger_mult",("coefficient_ledger",8,"ordered_positive_primitive_multiplicity"),99),
      ("smax",("coefficient_certificate","s_max"),100),("hash1",("coefficient_certificate","dense_primitive_vector_sha256"),"0"*64),("hash2",("coefficient_certificate","dense_mobius_factorized_vector_sha256"),"0"*64),
      ("identity",("coefficient_certificate","coefficient_identity_all_s_through_cutoff"),False),("nonzero",("coefficient_certificate","nonzero_coefficient_count"),1),("collisions",("coefficient_certificate","collision_coefficient_count"),1),("first",("coefficient_certificate","first_multiplicity_four_square"),85),
      ("count",("count_ledger",2,"N_primitive"),1),("mobius",("count_ledger",4,"mobius_inversion_value"),1),("ratio",("count_ledger",6,"leading_ratio_N_over_R2"),"0"),
      ("factor",("heat_transform_theorem","mobius_factorization"),"false"),("bound",("heat_transform_theorem","absolute_interchange_bound"),"none"),("collisionconv",("heat_transform_theorem","collision_convention"),"deduplicate"),("wave",("heat_transform_theorem","not_a_wave_trace"),False),
      ("Q",("counting_theorem","Q_definition"),"axes included"),("Qest",("counting_theorem","quarter_disk_estimate"),"wrong"),("Nasymp",("counting_theorem","primitive_count_asymptotic"),"wrong"),("Hasymp",("counting_theorem","heat_asymptotic"),"wrong"),("proof",("counting_theorem","proof_status"),"ASSUMED"),
      ("selfadj",("natural_quantization_boundary","self_adjoint"),False),("geometry",("natural_quantization_boundary","same_unit_square_classical_geometry"),False),("traceid",("natural_quantization_boundary","heat_transform_equals_operator_trace"),True),("bridge",("natural_quantization_boundary","clean_family_trace_bridge_constructed"),True),
      ("tuple",("route_a","tuple",0),"A1_PASS"),("routeb",("route_a","route_b_invocation_allowed"),True),("flag",("claim_boundary","dirichlet_spectral_trace_identity"),True),("extra",("route_a","forged"),True)]
    rejected=[]
    with tempfile.TemporaryDirectory(prefix="c152-mutations-") as temporary:
      for name,path,value in mutations:
        candidate=deepcopy(source);put(candidate,path,value);candidate["payload_sha256"]=ph(candidate)
        output=Path(temporary)/f"{name}.json";output.write_text(json.dumps(candidate,sort_keys=True,indent=2)+"\n")
        if subprocess.run([sys.executable,str(CHECKER),str(output)],capture_output=True,text=True).returncode==0:raise AssertionError(f"accepted {name}")
        rejected.append(name)
      stale=deepcopy(source);stale["payload_sha256"]="0"*64;output=Path(temporary)/"stale.json";output.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
      if subprocess.run([sys.executable,str(CHECKER),str(output)],capture_output=True,text=True).returncode==0:raise AssertionError("accepted stale")
    print(json.dumps({"status":"C152_MUTATION_PASS","repaired_hash_rejected":len(rejected),"stale_hash_rejected":1,"total":len(rejected)+1,"names":rejected},sort_keys=True))
if __name__ == "__main__":main()
