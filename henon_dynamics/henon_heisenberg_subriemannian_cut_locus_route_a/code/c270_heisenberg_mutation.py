#!/usr/bin/env python3
"""Repaired-payload-hash hostile mutation suite for HCS-C270."""
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
SRC = json.loads((ROOT / "results/c270_heisenberg_evidence.json").read_text())


def phash(d: dict) -> str:
    q = dict(d)
    q.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    mutants = []

    def add(name, mutate):
        d = copy.deepcopy(SRC)
        mutate(d)
        d["payload_sha256"] = phash(d)
        mutants.append((name, d))

    add("source_commit", lambda d: d.update(source_commit="0"*40))
    add("epoch", lambda d: d.update(fixed_epoch=0))
    add("scope", lambda d: d.update(scope_literal="BAD"))
    add("evaluator", lambda d: d["evaluator"].update(sha256="0"*64))
    add("route", lambda d: d["route_a"].update(overall="ROUTE_A_PASS"))
    add("route_b", lambda d: d["route_a"].update(route_b_invocation_allowed=True))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(1,"A1_PASS"))
    add("scope_flag", lambda d: d["scope_flags"].update(root_numbers=True))
    add("frame_sign", lambda d: d["convention"].update(frame="wrong"))
    add("cut_factor_two", lambda d: d["trajectory_contract"].update(first_cut_time="pi/abs(lambda)"))
    add("conjugate_factor_two", lambda d: d["trajectory_contract"].update(first_conjugate_time="pi/abs(lambda)"))
    add("jacobian_sign", lambda d: d["exponential_contract"].update(jacobian="wrong"))
    add("first_root", lambda d: d["exponential_contract"].update(first_positive_zero="s=pi"))
    add("angle_factor_four", lambda d: d["distance_contract"].update(implicit_angle="z/rho^2=mu"))
    add("distance_formula", lambda d: d["distance_contract"].update(distance="d=2 rho theta/sin(theta)"))
    add("vertical_distance", lambda d: d["distance_contract"].update(vertical_face="rho=0 gives d=sqrt(pi*abs(z))"))
    add("cut_locus", lambda d: d["distance_contract"].update(cut_locus_from_identity="horizontal plane"))
    add("abnormal", lambda d: d["proof_contract"].update(abnormal="abnormals minimize"))
    add("closed_geodesic", lambda d: d["proof_contract"].update(complete_geodesics="closed orbits exist"))
    add("generalize", lambda d: d["proof_contract"].update(scope="all Carnot groups"))
    add("doi", lambda d: d["source"].update(doi="10.fake/doi"))
    add("trajectory_cell", lambda d: d["regression"]["trajectory_rows"][137].update(z="99"))
    add("jacobian_cell", lambda d: d["regression"]["trajectory_rows"][402].update(jacobian_r_equals_1="99"))
    add("distance_cell", lambda d: d["regression"]["distance_rows"][27].update(distance="99"))
    add("vertical_cell", lambda d: d["regression"]["vertical_rows"][8].update(distance_squared="99"))
    add("counts", lambda d: d["regression"]["counts"].update(numeric_cells=1))
    add("numeric_schema", lambda d: d["regression"]["numeric_field_schema"]["trajectory_rows"].remove("lambda"))
    passed = 0
    for name, mutant in mutants:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "mutant.json"
            p.write_text(json.dumps(mutant, sort_keys=True, indent=2) + "\n")
            env = dict(os.environ)
            env["C270_EVIDENCE_IN"] = str(p)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c270_heisenberg_checker.py")],
                                 env=env, capture_output=True, text=True)
            if run.returncode:
                passed += 1
            else:
                raise AssertionError(f"mutation survived: {name}")
    print(f"C270 hostile repaired-hash mutations: PASS {passed}/{len(mutants)}")


if __name__ == "__main__":
    main()
