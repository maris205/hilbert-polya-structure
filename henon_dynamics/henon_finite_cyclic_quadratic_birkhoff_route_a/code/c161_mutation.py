#!/usr/bin/env python3
"""Wide repaired-hash and stale-hash hostile mutations for HCS-C161."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile

def rehash(data):
    data.pop("payload_sha256",None)
    data["payload_sha256"]=sha256(json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def changed(base,path,value=None):
    data=json.loads(json.dumps(base));target=data
    for key in path[:-1]:target=target[key]
    target[path[-1]]=target[path[-1]]+1 if value is None else value
    return data

def main():
    root=Path(__file__).resolve().parents[1]
    base=json.loads((root/"results/c161_cyclic_gauss_evidence.json").read_text())
    variants=[]
    for path in (("exhaustive_validation","formula_cases"),("exhaustive_validation","vanishing_cases"),
                 ("sentinels",0,"formula","A_n"),("sentinels",0,"formula","B_n"),
                 ("sentinels",0,"formula","C_n"),("sentinels",0,"formula","phase_numerator_mod_q"),
                 ("sentinels",0,"formula","jacobi_sign"),("sentinels",8,"prime_zero_level","count"),
                 ("sentinels",8,"prime_zero_level","discriminant_mod_p")):
        variants.append(changed(base,path))
    variants.extend([
        changed(base,("sentinels",1,"formula","status"),"PRIMITIVE_GAUSS_EVALUATION"),
        changed(base,("all_iterate_theorem","vanishing_gate"),"d may fail to divide B_n"),
        changed(base,("all_iterate_theorem","nonzero_formula"),"mutated"),
        changed(base,("all_iterate_theorem","pure_quadratic_specialization"),"mutated"),
        changed(base,("hard_gate","pivot"),"unrecorded"),
        changed(base,("scope_literal",),"ROUTE_B"),
        changed(base,("claim_boundary","euler_factors"),True),
        changed(base,("hard_gate","status"),"PASS_NO_PIVOT"),
        changed(base,("route_a","tuple",3),"A4_FORMAL_HINT"),
        changed(base,("route_a","route_b_invocation_allowed"),True),
        changed(base,("formal_lift","same_clock_identity"),"G=Tr(U^n)"),
        changed(base,("formal_lift","koopman_shift"),"wrong K"),
        changed(base,("formal_lift","time_reversal_identity"),"Theta U Theta^-1=U"),
        changed(base,("formal_lift","time_reversal_involution"),False),
        changed(base,("source_lock","object"),"wrong source"),
        changed(base,("source_lock","precision"),"unbounded floating evidence"),
        changed(base,("source_lock","clock"),"rescaled time"),
        changed(base,("hard_gate","rejection_reason"),"accepted without proof"),
        changed(base,("evaluation_date",),"2026-08-24"),
        changed(base,("source_commit",),"0"*40),
    ])
    stale=changed(base,("sentinels",0,"formula","A_n"))
    rejected=0
    with tempfile.TemporaryDirectory(prefix="c161-mutation-") as temp:
        for index,data in enumerate(variants):
            rehash(data);path=Path(temp)/f"m{index}.json"
            path.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
            run=subprocess.run([sys.executable,str(root/"code/c161_cyclic_gauss_checker.py"),
                                "--evidence",str(path),"--mutation-fast"],capture_output=True,text=True)
            rejected+=run.returncode!=0
        path=Path(temp)/"stale.json";path.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
        run=subprocess.run([sys.executable,str(root/"code/c161_cyclic_gauss_checker.py"),
                            "--evidence",str(path),"--mutation-fast"],capture_output=True,text=True)
        stale_rejected=run.returncode!=0
    assert rejected==len(variants) and stale_rejected
    print(json.dumps({"status":"C161_MUTATION_PASS","repaired_hash_rejected":rejected,
                      "stale_hash_rejected":1,"total":len(variants)+1},sort_keys=True))

if __name__=="__main__":main()
