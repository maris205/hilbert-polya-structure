#!/usr/bin/env python3
"""Hostile semantic mutations for HCS-C259; every mutation is rehashed."""
import copy
import json
import os
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c259_kuramoto_evidence.json"
CHECKER = ROOT / "code/c259_kuramoto_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def main():
    base = json.loads(EVIDENCE.read_text())
    operations = []
    for key in ("schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal"):
        operations.append(lambda data, key=key: data.__setitem__(key, str(data[key]) + "_mut"))
    operations.append(lambda data: data["evaluator"].__setitem__("sha256", "0" * 64))
    operations.append(lambda data: data["route_a"].__setitem__("tuple", ["A0_FAIL"]))
    operations.append(lambda data: data["route_a"].__setitem__("overall", "ROUTE_A_EXPLORATORY"))
    operations.append(lambda data: data["route_a"].__setitem__("route_b_invocation_allowed", True))
    for key in base["scope_flags"]:
        operations.append(lambda data, key=key: data["scope_flags"].__setitem__(key, True))
    operations.append(lambda data: data["regression"]["rows"][0].__setitem__("cut_flows", ["0"]))
    operations.append(lambda data: data["regression"]["rows"][1].__setitem__("regime", "violated"))
    operations.append(lambda data: data["regression"]["rows"][2].__setitem__("branch_count_mod_rotation", 1))
    operations.append(lambda data: data["regression"]["rows"][3].__setitem__("stable_branch_count", 2))
    operations.append(lambda data: data["regression"]["rows"][4].__setitem__("reduced_hessian_nullity", 7))
    operations.append(lambda data: data["regression"]["rows"][5].__setitem__("morse_index_histogram", {"0": 9}))
    operations.append(lambda data: data["regression"]["rows"][6].__setitem__("rooted_edges", []))
    operations.append(lambda data: data["regression"]["rows"][7].__setitem__("omega_mean", "999"))
    operations.append(lambda data: data["regression"].__setitem__("tree_count", 1))
    operations.append(lambda data: data["regression"].__setitem__("tree_count_by_n", {}))
    operations.append(lambda data: data["regression"].__setitem__("regime_counts", {"strict": 18248}))
    operations.append(lambda data: data["regression"].__setitem__("boundary_rows", []))
    operations.append(lambda data: data.__setitem__("exact_identities", []))
    operations.append(lambda data: data.__setitem__("citations", []))
    operations.append(lambda data: data.__setitem__("nonclaims", []))

    rejected = 0
    with tempfile.TemporaryDirectory() as directory:
        for index, operation in enumerate(operations):
            mutation = copy.deepcopy(base)
            operation(mutation)
            mutation["payload_sha256"] = payload_hash(mutation)
            path = Path(directory) / f"mutation_{index}.json"
            path.write_text(json.dumps(mutation, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            env = dict(os.environ)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            result = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(path)],
                env=env,
                text=True,
                capture_output=True,
            )
            rejected += result.returncode != 0
    assert rejected == len(operations)
    print(f"C259 hostile mutation: PASS {rejected}/{len(operations)} (semantic mutations rehashed before checking)")


if __name__ == "__main__":
    main()
