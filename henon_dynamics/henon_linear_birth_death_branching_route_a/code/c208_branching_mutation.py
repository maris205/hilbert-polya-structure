#!/usr/bin/env python3
"""Repaired-hash, stale-hash and unknown-key attacks against the C208 checker."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c208_branching_evidence.json"
CHECKER = Path(__file__).with_name("c208_branching_checker.py")


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data, path):
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                            capture_output=True)
    return result.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        lambda d: d.__setitem__("source_commit", "0" * 40),
        lambda d: d["evaluator"].__setitem__("sha256", "0" * 64),
        lambda d: d.__setitem__("scope_literal", "MUTATED_SCOPE"),
        lambda d: d.__setitem__("headline", "mutated headline"),
        lambda d: d["frozen_object"].__setitem__("determinant_convention", "call PGF a zeta"),
        lambda d: d["theorem"].__setitem__("subcritical_qsd_invariance", "mutated QSD identity"),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS"] * 5),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_euler_factors", True),
        lambda d: d["citations"][0].__setitem__("url", "https://example.invalid/fake"),
        lambda d: d["citations"][0].__setitem__("report_number", "FAKE 3"),
        lambda d: d["regression"]["parameter_cases"][0].__setitem__("p0", "9/10"),
        lambda d: d["regression"]["parameter_cases"][2].__setitem__("beta", "1/7"),
        lambda d: d["regression"]["parameter_cases"][1]["mobius_coefficients_a_b_c_d"].__setitem__(1, "5"),
        lambda d: d["regression"]["parameter_cases"][0]["population_rows"][3]["transition_probabilities_n_0_to_12"].__setitem__(4, "1/2"),
        lambda d: d["regression"]["parameter_cases"][4]["population_rows"][4]["survivor_weights_k_0_to_z"].__setitem__(4, "1/2"),
        lambda d: d["regression"]["parameter_cases"][9]["population_rows"][2].__setitem__("mean", "99"),
        lambda d: d["regression"]["semigroup_cases"][0]["composed_coefficients_a_b_c_d"].__setitem__(0, "7"),
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
        stale["regression"]["parameter_cases"][0]["population_rows"][1]["variance"] = "123"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({
        "status": "C208_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "unknown_key_rejections": 2,
        "total_rejections": repaired + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
