#!/usr/bin/env python3
"""Hostile audit: repaired-hash semantic attacks plus one stale-hash attack."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c204_finite_linear_evidence.json"
CHECKER = ROOT / "code" / "c204_finite_linear_checker.py"


def reseal(d):
    d.pop("semantic_payload_sha256", None)
    d["semantic_payload_sha256"] = hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    base = json.loads(EVIDENCE.read_text())
    def setv(path, value):
        d = copy.deepcopy(base); u = d
        for key in path[:-1]: u = u[key]
        u[path[-1]] = value; return d
    repaired = [
        ("fixed_formula", setv(["cases", 0, "fixed_counts_formula", "1"], 2)),
        ("route_overall", setv(["route_a", "overall"], "REJECTED")),
        ("exact_points", setv(["cases", 2, "exact_periodic_points", "3"], 1)),
        ("route_b_flip", setv(["route_a", "route_b_invocation_allowed"], True)),
        ("periodic_dimension", setv(["cases", 4, "periodic_subspace_dimension"], 1)),
        ("max_preperiod", setv(["cases", 0, "max_preperiod"], 2)),
        ("koopman_zero", setv(["cases", 0, "full_function_koopman_characteristic_polynomial", "zero_multiplicity"], 6)),
        ("cycle_factor", setv(["cases", 1, "artin_mazur_zeta_factors", "1"], 7)),
        ("restriction_order", setv(["cases", 5, "periodic_restriction_order"], 3)),
        ("matrix_entry", setv(["cases", 6, "matrix_rows", 0, 3], 1)),
        ("field_order", setv(["cases", 0, "field", "order"], 3)),
        ("gf4_to_z4", setv(["cases", 7, "field", "name"], "Z4")),
        ("gf4_matrix", setv(["cases", 7, "matrix_rows", 0, 1], 0)),
        ("scope_guard", setv(["scope_guard"], "TARGET_LOCAL_FACTORS")),
        ("forbidden_claim", setv(["claim_flags", "target_local_factors_computed"], True)),
        ("source_commit", setv(["source_commit"], "0" * 40)),
        ("evaluator_sha", setv(["evaluator_sha256"], "0" * 64)),
    ]
    stale = setv(["cases", 0, "fixed_counts_formula", "1"], 2)
    muts = [(name, d, True) for name, d in repaired] + [("stale_semantic_hash", stale, False)]
    caught = []
    with tempfile.TemporaryDirectory(prefix="c204-mut-") as td:
        for i, (name, d, repair_hash) in enumerate(muts):
            if repair_hash: reseal(d)
            path = Path(td) / f"m{i}.json"; path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
            p = subprocess.run([sys.executable, str(CHECKER), str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert p.returncode != 0, name
            caught.append(name)
    print(f"C204 hostile mutations: PASS {len(caught)}/{len(muts)}")
    print(f"repaired_hash={len(repaired)} stale_hash=1")
    print("caught=" + ",".join(caught))


if __name__ == "__main__": main()
