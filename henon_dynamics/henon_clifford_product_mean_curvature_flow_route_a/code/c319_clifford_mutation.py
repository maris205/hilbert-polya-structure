#!/usr/bin/env python3
"""Hostile semantic mutation tests for HCS-C319."""
import copy, hashlib, json, subprocess, sys, tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C319 mutation lane refuses optimized Python")
root = Path(__file__).resolve().parents[1]
source = json.loads((root / "results/c319_clifford_evidence.json").read_text())
checker = root / "code/c319_clifford_checker.py"
evaluation = root / "evaluations/route_a/HCS-C319/2026-09-03.yaml"


def repair(data):
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


mutators = [
    lambda d: d.__setitem__("candidate_id", "HCS-C318"),
    lambda d: d.__setitem__("source_commit", "0" * 40),
    lambda d: d.__setitem__("evaluation_date", "2026-09-02"),
    lambda d: d["scope_flags"].__setitem__("claims_target_zero_match", True),
    lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
    lambda d: d["pq_rows"][0].__setitem__("minimal_y", "2/3"),
    lambda d: d["pq_rows"][0].__setitem__("morse_index", 99),
    lambda d: d["pq_rows"][1].__setitem__("nullity", 1),
    lambda d: d["pq_rows"][2]["branches"][0].__setitem__("collapse_time", "0.0"),
    lambda d: d["pq_rows"][3]["branches"][5].__setitem__("cylinder_radius_squared", 999),
    lambda d: d["pq_rows"][4]["branches"][2].__setitem__("area_to_minimal_ratio", "1.0"),
    lambda d: d["pq_rows"][4]["spectrum_cells"][35].__setitem__("minus_laplacian_eigenvalue", "999"),
    lambda d: d["theorem_contract"].__setitem__("extra_claim", "unowned"),
    lambda d: d["pq_rows"][5]["branches"][0].__setitem__("extra", 1),
    lambda d: d["pq_rows"][6]["branches"].__setitem__(1, copy.deepcopy(d["pq_rows"][6]["branches"][0])),
    lambda d: d["enumeration"].__setitem__("extra", 1),
]
attempts = 0
with tempfile.TemporaryDirectory(prefix="c319-mutation-") as tmp:
    tmp = Path(tmp)
    for i, mutate in enumerate(mutators):
        for repaired in (False, True):
            data = copy.deepcopy(source); mutate(data)
            if repaired: repair(data)
            path = tmp / f"m{i}-{int(repaired)}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
            run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode == 0: raise AssertionError(f"mutation survived: {i}/{repaired}")
            attempts += 1
    raw = evaluation.read_text()
    for i, changed in enumerate((
        raw.replace("HCS-C319", "HCS-C318", 1),
        raw.replace("A0_FAIL", "A0_ANALYTIC_ARITHMETIC_ORIGIN", 1),
        raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true"),
        raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "BAD_SCOPE", 1),
        raw.replace("  - THEOREM_PACKAGE.md", "  - WRONG_THEOREM.md", 1),
        raw.replace("artifact_paths:\n  - results", "artifact_paths: results", 1),
        raw + "candidate_id: duplicate\n",
    )):
        ep = tmp / f"eval-{i}.yaml"; ep.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evaluation", str(ep)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0: raise AssertionError(f"YAML mutation survived: {i}")
        attempts += 1
print(f"C319 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
