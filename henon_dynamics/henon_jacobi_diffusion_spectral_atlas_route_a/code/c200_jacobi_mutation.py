#!/usr/bin/env python3
"""Repaired/stale-hash and unknown-key attacks against the C200 checker."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c200_jacobi_evidence.json"
CHECKER = Path(__file__).with_name("c200_jacobi_checker.py")


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data, path):
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)], capture_output=True)
    return result.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        lambda d: d.__setitem__("source_commit", "0" * 40),
        lambda d: d["evaluator"].__setitem__("sha256", "0" * 64),
        lambda d: d.__setitem__("headline", "mutated headline"),
        lambda d: d["frozen_object"].__setitem__("realization", "unspecified extension"),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_FAIL"] * 4 + ["A4_ROUTE_B_READY"]),
        lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True),
        lambda d: d["citations"][1].__setitem__("doi", "10.fake/half-clock"),
        lambda d: d["regression"]["parameter_cases"][3].__setitem__("left_boundary", "regular_reflecting"),
        lambda d: d["regression"]["parameter_cases"][0]["polynomial_rows"][2].__setitem__("eigenvalue", "99"),
        lambda d: d["regression"]["parameter_cases"][0]["polynomial_rows"][3]["coefficients_ascending"].__setitem__(0, "7"),
        lambda d: d["regression"]["parameter_cases"][1]["stationary_moments_0_to_8"].__setitem__(2, "5/7"),
        lambda d: d["summary"].__setitem__("exact_scalar_identity_count", 1),
        lambda d: d.__setitem__("unknown_top_level_key", "forbidden"),
        lambda d: d["regression"]["parameter_cases"][0].__setitem__("unknown_nested_key", "forbidden"),
    ]
    repaired = 0
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        for index, mutate in enumerate(mutations):
            data = deepcopy(original)
            mutate(data)
            repair(data)
            if not rejected(data, path):
                raise AssertionError(f"repaired-hash mutation {index} survived")
            repaired += 1
        stale = deepcopy(original)
        stale["regression"]["parameter_cases"][0]["left_boundary"] = "entrance"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({
        "status": "C200_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "unknown_key_rejections": 2,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
