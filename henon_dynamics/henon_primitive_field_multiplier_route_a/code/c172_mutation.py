#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks for HCS-C172."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c172_field_multiplier_evidence.json"
CHECKER=ROOT/"code/c172_field_multiplier_checker.py"


def digest(data:dict)->str:
    work=dict(data); work.pop("payload_sha256",None)
    return sha256(json.dumps(work,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def put(data:object,path:tuple[object,...],value:object)->None:
    target=data
    for key in path[:-1]: target=target[key]  # type: ignore[index]
    target[path[-1]]=value  # type: ignore[index]


def main()->None:
    source=json.loads(EVIDENCE.read_text())
    mutations=[
        ("schema",("schema",),"forged"),("candidate",("candidate_id",),"HCS-X"),
        ("date",("evaluation_date",),"2026-01-01"),("scope",("scope_literal",),"expanded"),
        ("commit",("source_commit",),"0"*40),("top_extra",("forged",),True),
        ("object",("source_lock","object"),"fitted"),("parameter",("source_lock","parameters"),"prime Q"),
        ("origin",("source_lock","arithmetic_origin"),"prime dictionary"),("clock",("source_lock","clock"),"log p"),
        ("cutoff",("source_lock","cutoff","n_max"),23),("precision",("source_lock","precision"),"float"),
        ("orbit",("orbit_theorem","decomposition"),"many cycles"),("allQ",("orbit_theorem","all_prime_powers"),False),
        ("zeta",("zeta_theorem","formula"),"1"),("unitary",("koopman_theorem","unitary"),False),
        ("selfadjoint",("koopman_theorem","self_adjoint_iff"),"all Q"),("reversal",("reversal_theorem","identity"),"commutes"),
        ("sameclock",("reversal_theorem","same_clock"),False),("control",("arithmetic_controls",0,"name"),"prime fit"),
        ("delete",("finite_ledgers",),deepcopy(source["finite_ledgers"][:-1])),
        ("Q",("finite_ledgers",2,"Q"),99),("prime",("finite_ledgers",3,"characteristic_prime"),9),
        ("N",("finite_ledgers",4,"N"),1),("inventory",("finite_ledgers",5,"orbit_inventory",0,"primitive_orbits"),99),
        ("fix",("finite_ledgers",6,"fix_counts_n_1_to_24",3),99),("factor",("finite_ledgers",7,"zeta_inverse_factors",1,"factor"),"1"),
        ("det",("finite_ledgers",8,"koopman_determinant"),"1"),("spectrum",("finite_ledgers",9,"koopman_eigenvalue_description"),"real"),
        ("mult",("finite_ledgers",10,"eigenvalue_one_multiplicity"),1),("self",("finite_ledgers",11,"self_adjoint"),True),
        ("h",("finite_ledgers",12,"nonprimitive_control_exponent_h"),1),("cycles",("finite_ledgers",13,"nonprimitive_control_cycle_count"),99),
        ("route",("route_a","tuple",0),"A0_ANALYTIC_ARITHMETIC_ORIGIN"),("route_b",("route_a","route_b_invocation_allowed"),True),
        ("dictionary",("claim_boundary","prime_phase_space_is_prime_orbit_dictionary"),True),
        ("logp",("claim_boundary","log_p_clock_or_von_mangoldt_weight"),True),
        ("target",("claim_boundary","target_divisor_matching"),True),("local",("claim_boundary","arithmetic_local_data"),True),
        ("root",("claim_boundary","root_numbers"),True),("hp",("claim_boundary","hilbert_polya_operator"),True),
        ("finiteproof",("claim_boundary","finite_ledgers_are_proof"),True),("gate",("integrity","hard_gate_status"),"FAIL"),
        ("review",("integrity","external_reviewer_simulated"),True),
    ]
    rejected=[]
    with tempfile.TemporaryDirectory(prefix="c172-mutations-") as temporary:
        for name,path,value in mutations:
            candidate=deepcopy(source); put(candidate,path,value); candidate["payload_sha256"]=digest(candidate)
            output=Path(temporary)/f"{name}.json"; output.write_text(json.dumps(candidate,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
            result=subprocess.run([sys.executable,str(CHECKER),str(output),"--mutation-fast"],capture_output=True,text=True)
            if result.returncode==0: raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale=deepcopy(source); stale["payload_sha256"]="0"*64
        output=Path(temporary)/"stale.json"; output.write_text(json.dumps(stale,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
        result=subprocess.run([sys.executable,str(CHECKER),str(output),"--mutation-fast"],capture_output=True,text=True)
        if result.returncode==0: raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status":"C172_MUTATION_PASS","repaired_hash_rejected":len(rejected),
                      "stale_hash_rejected":1,"total":len(rejected)+1,"names":rejected},sort_keys=True))


if __name__ == "__main__":
    main()
