#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C151."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c151_heisenberg_fibre_evidence.json"
CHECKER = ROOT / "code/c151_heisenberg_fibre_checker.py"

def payload_hash(data):
    work = dict(data); work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def set_path(data, path, value):
    target = data
    for key in path[:-1]: target = target[key]
    target[path[-1]] = value

def main():
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "forged"), ("candidate", ("candidate_id",), "HCS-X"),
        ("date", ("evaluation_date",), "2026-08-24"), ("commit", ("source_commit",), "0"*40),
        ("scope", ("scope_literal",), "BAD"), ("matrix", ("source_lock","matrix_A",0,0), 3),
        ("cutoff", ("source_lock","cutoff","exact_rotation_histogram"), 11),
        ("precision", ("source_lock","precision"), "float"), ("quotient", ("source_lock","quotient_convention"), "right"),
        ("power", ("rotation_ledger",3,"A_power",0,0), 99), ("matrixM", ("rotation_ledger",4,"M=A_power-I",0,0), 99),
        ("det", ("rotation_ledger",5,"det_M"), 1), ("horizontal", ("rotation_ledger",6,"horizontal_fixed_class_count"), 1),
        ("hnf", ("rotation_ledger",7,"column_hnf",0,0), 1), ("Q", ("rotation_ledger",8,"universal_projector_order_Q"), 1),
        ("lcm", ("rotation_ledger",9,"observed_denominator_lcm"), 1), ("support", ("rotation_ledger",10,"rotation_support_size"), 1),
        ("zero", ("rotation_ledger",11,"fixed_circle_component_count"), 1),
        ("histrot", ("rotation_ledger",4,"histogram",0,"rotation"), "1/2"),
        ("histmult", ("rotation_ledger",5,"histogram",0,"multiplicity"), 99),
        ("iff", ("fibre_rotation_theorem","fixed_fibre_iff"), "always"),
        ("invariance", ("fibre_rotation_theorem","representative_invariance"), "false"),
        ("proof", ("fibre_rotation_theorem","representative_invariance_proof_key"), "none"),
        ("kernel", ("fibre_rotation_theorem","clean_kernel"), "isolated"),
        ("denombound", ("central_root_of_unity_projector","denominator_bound"), "Q=D"),
        ("homomorphism", ("central_root_of_unity_projector","rho_is_horizontal_group_homomorphism"), True),
        ("alln", ("central_root_of_unity_projector","all_iterates"), False),
        ("pattern", ("discarded_pattern","status"), "THEOREM"),
        ("witness", ("discarded_pattern","witnesses","n10_fixed_circles"), 123),
        ("extrapolate", ("discarded_pattern","all_n_closed_form_claimed"), True),
        ("unitary", ("formal_lift_hint","unitary"), False),
        ("bridge", ("formal_lift_hint","isolated_orbit_weight_bridge_constructed"), True),
        ("tuple", ("route_a","tuple",0), "A1_WEAK"), ("routeb", ("route_a","route_b_invocation_allowed"), True),
        ("flag", ("claim_boundary","all_n_closed_component_formula"), True), ("extra", ("route_a","forged"), True),
    ]
    rejected=[]
    with tempfile.TemporaryDirectory(prefix="c151-mutations-") as temporary:
        for name,path,value in mutations:
            candidate=deepcopy(source); set_path(candidate,path,value); candidate["payload_sha256"]=payload_hash(candidate)
            output=Path(temporary)/f"{name}.json"; output.write_text(json.dumps(candidate,sort_keys=True,indent=2)+"\n")
            result=subprocess.run([sys.executable,str(CHECKER),str(output)],capture_output=True,text=True)
            if result.returncode==0: raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale=deepcopy(source); stale["payload_sha256"]="0"*64
        output=Path(temporary)/"stale.json"; output.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
        if subprocess.run([sys.executable,str(CHECKER),str(output)],capture_output=True,text=True).returncode==0: raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status":"C151_MUTATION_PASS","repaired_hash_rejected":len(rejected),"stale_hash_rejected":1,"total":len(rejected)+1,"names":rejected},sort_keys=True))

if __name__ == "__main__": main()
