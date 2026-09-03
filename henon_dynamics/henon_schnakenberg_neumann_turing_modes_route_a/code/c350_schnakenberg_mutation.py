#!/usr/bin/env python3
"""Repaired-hash hostile mutations for HCS-C350."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]
CHECKER=ROOT/"code/c350_schnakenberg_checker.py"
EVIDENCE=ROOT/"results/c350_schnakenberg_evidence.json"
EVALUATION=ROOT/"evaluations/route_a/HCS-C350/2026-09-03.yaml"


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()


def repair(value):
    value=copy.deepcopy(value)
    value.pop("payload_sha256",None)
    value["payload_sha256"]=hashlib.sha256(canonical(value)).hexdigest()
    return value


def rejected(evidence_bytes, evaluation_bytes=None):
    with tempfile.TemporaryDirectory(prefix="c350-mutation-") as directory:
        work=Path(directory); ep=work/"evidence.json"; yp=work/"evaluation.yaml"
        ep.write_bytes(evidence_bytes)
        yp.write_bytes(EVALUATION.read_bytes() if evaluation_bytes is None else evaluation_bytes)
        process=subprocess.run([sys.executable,"-B",str(CHECKER),"--evidence",str(ep),"--evaluation",str(yp)],
            stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"))
        return process.returncode!=0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C350 mutation suite refuses optimized Python")
    base=json.loads(EVIDENCE.read_text())
    attacks=[]
    def add(label,fn): attacks.append((label,fn))
    add("candidate",lambda d:d.__setitem__("candidate_id","HCS-C349"))
    add("obstruction",lambda d:d.__setitem__("obstruction_id","HEN-O333"))
    add("source",lambda d:d.__setitem__("source_commit","0"*40))
    add("epoch",lambda d:d.__setitem__("fixed_epoch",1788393601))
    add("scope",lambda d:d.__setitem__("scope_literal","EXPANDED"))
    add("authority",lambda d:d["evaluator"].__setitem__("authority","wrong"))
    add("evaluator-version",lambda d:d["evaluator"].__setitem__("version","0.1.0"))
    add("evaluator-sha",lambda d:d["evaluator"].__setitem__("sha256","0"*64))
    add("yaml-raw",lambda d:d["route_a_yaml"].__setitem__("raw_sha256","0"*64))
    add("yaml-semantic",lambda d:d["route_a_yaml"].__setitem__("semantic_sha256","0"*64))
    add("tuple",lambda d:d["route_a"]["tuple"].__setitem__(0,"A0_WEAK_ARITHMETIC_RELATION"))
    add("overall",lambda d:d["route_a"].__setitem__("overall","ROUTE_A_EXPLORATORY"))
    add("route-b",lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",True))
    add("scope-flag",lambda d:d["scope_flags"].__setitem__("claims_target_zero_match",True))
    add("equilibrium-overclaim",lambda d:d["theorem_contract"].__setitem__("equilibrium","unique equilibrium"))
    add("complexification-contract",lambda d:d["theorem_contract"].__setitem__("modal","real spectrum without complexification"))
    add("finite-condition",lambda d:d["theorem_contract"].__setitem__("finite_domain","continuous window alone implies finite-domain instability"))
    add("boundary",lambda d:d["theorem_contract"].__setitem__("boundaries","zero diffusion included"))
    add("case-a",lambda d:d["case_rows"][4].__setitem__("a","1/5"))
    add("case-B",lambda d:d["case_rows"][5].__setitem__("B","16"))
    add("case-Q",lambda d:d["case_rows"][8].__setitem__("Q","1"))
    add("mode-mu",lambda d:d["mode_rows"][5].__setitem__("mu","2"))
    add("mode-trace",lambda d:d["mode_rows"][10].__setitem__("trace","0"))
    add("mode-det",lambda d:d["mode_rows"][20].__setitem__("determinant","0"))
    add("mode-state",lambda d:d["mode_rows"][25].__setitem__("state","bogus"))
    add("unstable-index",lambda d:d["case_rows"][5].__setitem__("unstable_indices",[1,2,3]))
    add("neutral-index",lambda d:d["case_rows"][6].__setitem__("neutral_indices",[]))
    add("upper-neutral-index",lambda d:d["case_rows"][7].__setitem__("neutral_indices",[]))
    add("count-formula",lambda d:d["case_rows"][5].__setitem__("count_formula_value",1))
    add("continuous-window",lambda d:d["case_rows"][3].__setitem__("continuous_window",False))
    add("finite-turing",lambda d:d["case_rows"][3].__setitem__("finite_domain_turing",True))
    add("delete-case",lambda d:d["case_rows"].pop())
    add("reverse-modes",lambda d:d["mode_rows"].reverse())
    add("delete-wall",lambda d:d["length_wall_rows"].pop())
    add("wall-sign",lambda d:d["length_wall_rows"][0]["ell2_polynomial"].__setitem__(1,"1"))
    add("wall-discriminant",lambda d:d["length_wall_rows"][0].__setitem__("discriminant","0"))
    add("grid-count",lambda d:d["finite_grid"].__setitem__("mode_rows",0))
    add("grid-count-formula-flag",lambda d:d["finite_grid"].__setitem__("records_count_formula",False))
    add("case-digest",lambda d:d["enumeration"].__setitem__("case_sha256","0"*64))
    add("mode-digest",lambda d:d["enumeration"].__setitem__("mode_sha256","0"*64))
    add("finite-proof",lambda d:d["enumeration"].__setitem__("finite_evidence_proves_continuum_theorem",True))
    add("collision",lambda d:d["collision_boundary"].pop("C304"))
    add("nonclaim",lambda d:d["nonclaims"].pop(0))
    add("reference",lambda d:d["references"][0].__setitem__("identifier","DOI:wrong"))
    add("extra-top",lambda d:d.__setitem__("extra",1))
    add("delete-top",lambda d:d.pop("model"))
    passed=0
    for label,fn in attacks:
        value=copy.deepcopy(base); fn(value); encoded=json.dumps(repair(value),sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n"
        if not rejected(encoded): raise AssertionError(f"repaired mutation accepted: {label}")
        passed+=1
    stale=copy.deepcopy(base); stale["candidate_id"]="HCS-C349"
    if not rejected((json.dumps(stale,sort_keys=True,indent=2)+"\n").encode()): raise AssertionError("stale hash accepted")
    passed+=1
    raw=EVIDENCE.read_text()
    malformed=[
        raw.replace('"candidate_id": "HCS-C350",','"candidate_id": "HCS-C350",\n  "candidate_id": "HCS-C350",',1),
        raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),
        raw.replace('"a": "1/100"','"a": "nan"',1),
        "[]\n",
    ]
    for index,text in enumerate(malformed):
        if not rejected(text.encode()): raise AssertionError(f"malformed JSON accepted {index}")
        passed+=1
    yraw=EVALUATION.read_text()
    yaml_attacks=[
        yraw.replace("candidate_id: HCS-C350","candidate_id: HCS-C349",1),
        yraw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md","evaluator_authority: wrong",1),
        yraw.replace("  evidence_status: PROVED","",1),
        yraw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1),
        yraw.replace("  claims_target_zero_match: false","  claims_target_zero_match: true",1),
        yraw.replace("candidate_id: HCS-C350","candidate_id: HCS-C350\ncandidate_id: HCS-C350",1),
        "base: &base {x: 1}\ncopy: *base\n",
        "1: bad\n",
        yraw.replace("evaluation_date: 2026-09-03","evaluation_date: 2026-09-04",1),
    ]
    good_bytes=EVIDENCE.read_bytes()
    for index,text in enumerate(yaml_attacks):
        if not rejected(good_bytes,text.encode()): raise AssertionError(f"YAML mutation accepted {index}")
        passed+=1
    print(f"C350 hostile mutation suite: PASS {passed}/{passed}")


if __name__=="__main__":
    main()
