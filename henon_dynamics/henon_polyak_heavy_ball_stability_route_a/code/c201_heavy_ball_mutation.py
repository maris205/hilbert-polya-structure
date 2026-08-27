#!/usr/bin/env python3
"""Repaired/stale-hash, unknown-key and mathematical attacks for C201."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c201_heavy_ball_evidence.json"
CHECKER = Path(__file__).with_name("c201_heavy_ball_checker.py")


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
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_FAIL"] * 4 + ["A4_ROUTE_B_READY"]),
        lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True),
        lambda d: d["citations"][0].__setitem__("doi", "10.fake/polyak"),
        lambda d: d["regression"]["parameter_cases"][0].__setitem__("robustly_schur_stable", False),
        lambda d: d["regression"]["parameter_cases"][0]["endpoint_rows"][0].__setitem__("p_at_plus_one", "0"),
        lambda d: d["regression"]["parameter_cases"][4].__setitem__("regime", "robustly_schur_stable"),
        lambda d: d["regression"]["optimal_intervals"][0].__setitem__("q", "1/2"),
        lambda d: d["regression"]["optimal_intervals"][0].__setitem__("alpha_star", "2/5"),
        lambda d: d["regression"]["jordan_counterexample"].__setitem__("jordan_square_zero", False),
        lambda d: d["regression"]["jordan_counterexample"]["terms_k_minus1_to_8"].__setitem__("4", "0"),
        lambda d: d["regression"]["rotated_spd_control"].__setitem__("determinant", "99"),
        lambda d: d["regression"]["finite_order_controls"][0].__setitem__("exact_order", 3),
        lambda d: d.__setitem__("unknown_top_level_key", "forbidden"),
        lambda d: d["regression"]["parameter_cases"][0].__setitem__("unknown_nested_key", "forbidden"),
    ]
    repaired = 0
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        for mutate in mutations:
            data = deepcopy(original)
            mutate(data)
            repair(data)
            if not rejected(data, path):
                raise AssertionError("repaired-hash mutation survived")
            repaired += 1
        stale = deepcopy(original)
        stale["regression"]["parameter_cases"][0]["endpoint_rows"][0]["trace_a"] = "123"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({
        "status": "C201_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "unknown_key_rejections": 2,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
