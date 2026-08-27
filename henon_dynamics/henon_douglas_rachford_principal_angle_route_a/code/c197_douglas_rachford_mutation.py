#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash attacks against the C197 checker."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c197_douglas_rachford_evidence.json"
CHECKER = Path(__file__).with_name("c197_douglas_rachford_checker.py")


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
        lambda d: d.__setitem__("headline", "mutated headline"),
        lambda d: d["evaluator"].__setitem__("sha256", "0" * 64),
        lambda d: d["scope_flags"].__setitem__("uses_prime_table", True),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_FAIL"] * 5),
        lambda d: d["citations"][1].__setitem__("doi", "10.fake/mutation"),
        lambda d: d["regression"]["angles"][0].__setitem__("cosine", "4/5"),
        lambda d: d["regression"]["block_rows"][0]["matrix"][0].__setitem__(0, "99"),
        lambda d: d["regression"]["block_rows"][1].__setitem__("trace", "7"),
        lambda d: d["regression"]["block_rows"][2].__setitem__("determinant", "5"),
        lambda d: d["regression"]["composite_rows"][0]["det_I_minus_zT_coefficients"].__setitem__(1, "13"),
    ]
    repaired_rejections = 0
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        for mutate in mutations:
            data = deepcopy(original)
            mutate(data)
            repair(data)
            if not rejected(data, path):
                raise AssertionError("repaired-hash semantic mutation survived")
            repaired_rejections += 1
        stale = deepcopy(original)
        stale["regression"]["block_rows"][0]["trace"] = "123"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({
        "status": "C197_MUTATION_PASS",
        "repaired_hash_rejections": repaired_rejections,
        "stale_hash_rejections": 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
