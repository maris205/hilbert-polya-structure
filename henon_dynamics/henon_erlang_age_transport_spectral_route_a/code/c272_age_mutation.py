#!/usr/bin/env python3
"""Semantic hostile mutations for HCS-C272."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = json.loads((ROOT / "results/c272_age_evidence.json").read_text())


def phash(d: dict) -> str:
    q = dict(d); q.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(d: dict, repair: bool = True) -> bool:
    if repair: d["payload_sha256"] = phash(d)
    with tempfile.TemporaryDirectory(prefix="c272-mut-") as td:
        p = Path(td) / "bad.json"; p.write_text(json.dumps(d, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"; env["C272_EVIDENCE_PATH"] = str(p)
        r = subprocess.run([sys.executable, "-B", str(ROOT / "code/c272_age_checker.py")], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return r.returncode != 0


def main() -> None:
    attacks = []
    d=copy.deepcopy(ORIGINAL);d["source_commit"]="0"*40;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["scope_flags"]["euler_factors"]=True;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["route_a"]["tuple"][2]="A2_ANALYTIC_DETERMINANT";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["theorem_contract"]["eigenvalue_gate"]="every denominator root is an eigenvalue";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["cases"][0]["beta"]="9/1";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["cases"][0]["essential_edge"]="0/1";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["cases"][0]["characteristic_polynomial_descending"][0]="2/1";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["cases"][0]["roots"][0]["real"]="99.0";attacks.append((d,True))
    edge_i=next(i for i,x in enumerate(ORIGINAL["regression"]["cases"]) if any(r["spectral_location"]=="essential_edge" for r in x["roots"]))
    edge_j=next(j for j,x in enumerate(ORIGINAL["regression"]["cases"][edge_i]["roots"]) if x["spectral_location"]=="essential_edge")
    d=copy.deepcopy(ORIGINAL);d["regression"]["cases"][edge_i]["roots"][edge_j]["spectral_location"]="eigenvalue";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["unknown_top_level"]=1;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["candidate_id"]="HCS-C000";attacks.append((d,False))
    passed=sum(rejected(d,repair) for d,repair in attacks);assert passed==len(attacks)
    print(f"C272 hostile mutation: PASS {passed}/{len(attacks)}")


if __name__ == "__main__":
    main()
