#!/usr/bin/env python3
"""Repaired-hash hostile mutations for the HCS-C264 semantic gate."""
import copy, hashlib, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = json.loads((ROOT / "results/c264_power_map_evidence.json").read_text())


def repair(data):
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


mutators = [
    lambda d: d.update(candidate_id="HCS-C000"),
    lambda d: d.update(source_commit="0" * 40),
    lambda d: d.update(fixed_epoch=0),
    lambda d: d.update(scope_literal="OPEN_SCOPE"),
    lambda d: d["evaluator"].update(sha256="0" * 64),
    lambda d: d["route_a"].update(tuple=["A0_FAIL"] * 5),
    lambda d: d["route_a"].update(overall="ROUTE_A_ACCEPTED"),
    lambda d: d["route_a"].update(route_b_invocation_allowed=True),
    lambda d: d["scope_flags"].update(root_number_claimed=True),
    lambda d: d["regression"]["counts"].update(cases=645),
    lambda d: d["regression"]["counts"].update(group_types=33),
    lambda d: d["regression"]["counts"].update(d_values=18),
]
for idx in (0, 1, 18, 19, 37, 38, 100, 211, 350, 500, 645):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i].update(periodic_points=d["regression"]["cases"][i]["periodic_points"] + 1))
for idx in (0, 18, 40, 120, 300, 600):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i].update(order=d["regression"]["cases"][i]["order"] + 1))
for idx in (1, 50, 250, 500):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i]["koopman_characteristic_ledger"].update(zero_multiplicity=999))

passed = 0
for number, mutate in enumerate(mutators):
    trial = copy.deepcopy(base)
    mutate(trial); repair(trial)
    with tempfile.TemporaryDirectory(prefix="c264-mut-") as td:
        path = Path(td) / "mutated.json"
        path.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        proc = subprocess.run([sys.executable, "-B", str(ROOT / "code/c264_power_map_checker.py"), str(path), "--quick"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        assert proc.returncode != 0, f"mutation {number} escaped"
    passed += 1
print(f"C264 repaired-hash mutation gate: PASS {passed}/{len(mutators)}")
