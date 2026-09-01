#!/usr/bin/env python3
"""Repaired-hash hostile mutations for HCS-C269."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = json.loads((ROOT / "results/c269_chebyshev_evidence.json").read_text())


def repair(data):
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    data["payload_sha256"] = hashlib.sha256(raw.encode()).hexdigest()


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
    lambda d: d["regression"]["counts"].update(cases=120),
    lambda d: d["regression"]["counts"].update(field_models=10),
    lambda d: d["regression"]["counts"].update(degree_values=10),
]
for idx in (0, 1, 10, 11, 21, 33, 44, 70, 90, 110, 120):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i].update(periodic_points=d["regression"]["cases"][i]["periodic_points"] + 1))
for idx in (2, 14, 25, 47, 68, 92, 115):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i].update(branch_value_count=3))
for idx in (3, 17, 38, 75, 108):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i]["image_ranks"].__setitem__(0, 999))
for idx in (4, 29, 57, 86, 119):
    mutators.append(lambda d, i=idx: d["regression"]["cases"][i]["koopman_characteristic_ledger"].update(zero_multiplicity=999))
mutators.append(
    lambda d: next(
        case for case in d["regression"]["cases"] if case["q"] == 4 and case["d"] == 0
    ).update(modulus=[1, 0, 1])
)

passed = 0
for number, mutate in enumerate(mutators):
    trial = copy.deepcopy(base)
    mutate(trial); repair(trial)
    with tempfile.TemporaryDirectory(prefix="c269-mut-") as td:
        path = Path(td) / "mutated.json"
        path.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        proc = subprocess.run(
            [sys.executable, "-B", str(ROOT / "code/c269_chebyshev_checker.py"), str(path), "--quick"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        assert proc.returncode != 0, f"mutation {number} escaped"
    passed += 1
print(f"C269 repaired-hash mutation gate: PASS {passed}/{len(mutators)}")
