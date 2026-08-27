#!/usr/bin/env python3
"""Hostile mutation audit for C205."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c205_dyck_shift_evidence.json"
CHECKER = ROOT / "code" / "c205_dyck_shift_checker.py"


def reseal(d):
    d.pop("semantic_payload_sha256", None)
    d["semantic_payload_sha256"] = hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    base = json.loads(EVIDENCE.read_text())
    def setv(path, value):
        d = copy.deepcopy(base); u = d
        for k in path[:-1]: u = u[k]
        u[path[-1]] = value; return d
    repaired = [
        ("fixed_odd", setv(["records", 1, "fixed_points", "3"], 39)),
        ("fixed_even", setv(["records", 2, "fixed_points", "4"], 419)),
        ("primitive_point", setv(["records", 3, "primitive_points", "5"], 1)),
        ("primitive_orbit", setv(["records", 4, "primitive_orbits", "6"], 0)),
        ("direct_word", setv(["records", 1, "direct_periodic_word_audit", "5"], 383)),
        ("entropy", setv(["records", 0, "topological_entropy"], "log(3)")),
        ("source_pages", setv(["source_records", 0, "pages"], "wrong-pages")),
        ("N2_pole_order", setv(["records", 1, "singularity_and_asymptotic", "pole_order"], 1)),
        ("dominant_pole", setv(["records", 2, "singularity_and_asymptotic", "dominant_pole"], "1/5")),
        ("nonrational", setv(["records", 3, "singularity_and_asymptotic", "nonrational"], False)),
        ("origin_marked", setv(["model_convention", "fixed_point_convention"], "unmarked cycles")),
        ("orbit_division", setv(["model_convention", "orbit_convention"], "divide before inversion")),
        ("route_b_flip", setv(["route_a", "route_b_invocation_allowed"], True)),
        ("route", setv(["route_a", "overall"], "PROMOTED")),
        ("scope", setv(["scope_guard"], "TARGET_EULER_FACTORS")),
        ("forbidden_claim", setv(["claim_flags", "target_root_numbers_computed"], True)),
        ("source", setv(["source_commit"], "0" * 40)),
        ("evaluator", setv(["evaluator_sha256"], "0" * 64)),
    ]
    stale = setv(["records", 1, "fixed_points", "3"], 39)
    muts = [(name, d, True) for name, d in repaired] + [("stale_semantic_hash", stale, False)]
    caught = []
    with tempfile.TemporaryDirectory(prefix="c205-mut-") as td:
        for i, (name, d, repair_hash) in enumerate(muts):
            if repair_hash: reseal(d)
            pth = Path(td) / f"m{i}.json"; pth.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
            p = subprocess.run([sys.executable, str(CHECKER), str(pth)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert p.returncode != 0, name
            caught.append(name)
    print(f"C205 hostile mutations: PASS {len(caught)}/{len(muts)}")
    print(f"repaired_hash={len(repaired)} stale_hash=1")
    print("caught=" + ",".join(caught))


if __name__ == "__main__": main()
