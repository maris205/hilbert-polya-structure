#!/usr/bin/env python3
"""Wide repaired-hash and stale-hash hostile mutations for HCS-C162."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile

def rehash(d):
    d.pop("payload_sha256",None);d["payload_sha256"]=sha256(json.dumps(d,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def changed(base,path,value=None):
    data=json.loads(json.dumps(base));target=data
    for key in path[:-1]:target=target[key]
    target[path[-1]]=target[path[-1]]+1 if value is None else value
    return data
def main():
    root=Path(__file__).resolve().parents[1];base=json.loads((root/"results/c162_branch_amplitude_evidence.json").read_text())
    variants=[
        changed(base,("shell_summary","occupied_shells")),
        changed(base,("shell_ledger",0,"r2_source_shell_multiplicity")),
        changed(base,("shell_ledger",0,"normalized_positive_time_coefficient"),"wrong phase"),
        changed(base,("local_convergence_sentinels",0,"target","real"),"0"),
        changed(base,("renormalization_theorem","positive_time"),"wrong positive phase"),
        changed(base,("renormalization_theorem","negative_time"),"same rather than conjugate"),
        changed(base,("renormalization_theorem","shell_multiplicity"),"target multiplicity"),
        changed(base,("renormalization_theorem","branch_calculation"),"epsilon power -1"),
        changed(base,("renormalization_theorem","remainder"),"finite table only"),
        changed(base,("renormalization_theorem","coincident_poles"),"pole survives"),
        changed(base,("renormalization_theorem","weyl_and_constant_terms"),"Weyl survives"),
        changed(base,("hard_gate","status"),"FAIL"),
        changed(base,("hard_gate","advance_over_c157"),"more precision only"),
        changed(base,("formal_lift","same_clock"),"rescaled clock"),
        changed(base,("route_a","tuple",3),"A4_FORMAL_HINT"),
        changed(base,("route_a","route_b_invocation_allowed"),True),
        changed(base,("scope_literal",),"ROUTE_B"),
        changed(base,("claim_boundary","isolated_stability_amplitude"),True),
        changed(base,("source_lock","upstream_c157_evidence_sha256"),"0"*64),
        changed(base,("source_lock","precision"),"floating proof"),
        changed(base,("hard_gate","required"),"more digits"),
        changed(base,("evaluation_date",),"2026-08-24"),
        changed(base,("source_commit",),"0"*40),
    ]
    stale=changed(base,("shell_summary","occupied_shells"));rejected=0
    with tempfile.TemporaryDirectory(prefix="c162-mutation-") as temp:
        for i,d in enumerate(variants):
            rehash(d);p=Path(temp)/f"m{i}.json";p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
            run=subprocess.run([sys.executable,str(root/"code/c162_branch_amplitude_checker.py"),"--evidence",str(p)],capture_output=True,text=True)
            rejected+=run.returncode!=0
        p=Path(temp)/"stale.json";p.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
        run=subprocess.run([sys.executable,str(root/"code/c162_branch_amplitude_checker.py"),"--evidence",str(p)],capture_output=True,text=True)
        stale_rejected=run.returncode!=0
    assert rejected==len(variants) and stale_rejected
    print(json.dumps({"status":"C162_MUTATION_PASS","repaired_hash_rejected":rejected,
                      "stale_hash_rejected":1,"total":len(variants)+1},sort_keys=True))
if __name__=="__main__":main()
