#!/usr/bin/env python3
"""Semantic hostile mutations for HCS-C277."""
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
ORIGINAL = json.loads((ROOT / "results/c277_caputo_evidence.json").read_text())


def payload_hash(data: dict) -> str:
    d = dict(data); d.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(data: dict, repair: bool = True) -> bool:
    if repair:
        data["payload_sha256"] = payload_hash(data)
    with tempfile.TemporaryDirectory(prefix="c277-mut-") as td:
        path = Path(td) / "bad.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"; env["C277_EVIDENCE_PATH"] = str(path)
        run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c277_caputo_checker.py")],
                             env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return run.returncode != 0


def main() -> None:
    attacks = []
    d=copy.deepcopy(ORIGINAL);d["source_commit"]="0"*40;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["scope_flags"]["euler_factors"]=True;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["route_a"]["tuple"][2]="A2_ANALYTIC_DETERMINANT";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["theorem_contract"]["sharp_smoothing"]="all-order smoothing";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["theorem_contract"]["negative_theta_context"]="theta<0 is unbounded";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["theorem_contract"]["sharp_schatten"]="all p";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["spectral_cells"][0]["spectral_argument"]="9/1";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["spectral_cells"][0]["multiplier"]="0.1";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["nonsemigroup_witnesses"][0]["semigroup_identity"]=True;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["beta_half_long_time"][0]["modes"][0]["resolvent_limit"]="1.0";attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["smoothing_threshold_cells"][-1]["bounded_L2_operator"]=True;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["regression"]["schatten_threshold_cells"][1]["in_S_p"]=True;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["unknown_top_level"]=1;attacks.append((d,True))
    d=copy.deepcopy(ORIGINAL);d["candidate_id"]="HCS-C000";attacks.append((d,False))
    passed=sum(rejected(d, repair) for d,repair in attacks)
    assert passed == len(attacks)
    print(f"C277 hostile mutation: PASS {passed}/{len(attacks)}")


if __name__ == "__main__":
    main()
