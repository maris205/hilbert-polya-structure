#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for C220."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c220_tasep_evidence.json"
CHECKER = Path(__file__).with_name("c220_tasep_checker.py")


def repair_hash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(data: dict, path: Path) -> bool:
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    return subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path)], capture_output=True).returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        lambda d: d.__setitem__("source_commit", "0" * 40),
        lambda d: d.__setitem__("fixed_epoch", 0),
        lambda d: d["evaluator"].__setitem__("sha256", "0" * 64),
        lambda d: d.__setitem__("scope_literal", "BAD_SCOPE"),
        lambda d: d.__setitem__("headline", "synthetic"),
        lambda d: d["frozen_object"].__setitem__("generator", "prime-fitted generator"),
        lambda d: d["frozen_object"].__setitem__("matrix_ansatz", "DE=ED"),
        lambda d: d["theorem"].__setitem__("normalization", "Z is arbitrary"),
        lambda d: d["theorem"].__setitem__("equal_rate_limit", "no limit"),
        lambda d: d["theorem"].__setitem__("current", "J_L=1"),
        lambda d: d["theorem"].__setitem__("phase_diagram", "all phases identical"),
        lambda d: d["theorem"].__setitem__("zero_faces", "no absorbing faces"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS"] * 5),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_euler_factors", True),
        lambda d: d["citations"][0].__setitem__("doi", "10.0000/bad"),
        lambda d: d["regression"].__setitem__("L_values", [1]),
        lambda d: d["regression"]["interior_rows"][0].__setitem__("weights", ["0"]),
        lambda d: d["regression"]["interior_rows"][1].__setitem__("Z", "0"),
        lambda d: d["regression"]["interior_rows"][2].__setitem__("closed_Z", "777"),
        lambda d: d["regression"]["interior_rows"][3].__setitem__("J_ratio", "0"),
        lambda d: d["regression"]["interior_rows"][25].__setitem__("currents", []),
        lambda d: d["regression"]["interior_rows"][26].__setitem__("nullspace_dimension", 99),
        lambda d: d["regression"]["boundary_rows"][0].__setitem__("absorbing_states", [99]),
        lambda d: d["regression"]["phase_rows"][0].__setitem__("current", "0"),
        lambda d: d.__setitem__("unknown_top_level_key", True),
        lambda d: d["regression"]["interior_rows"][0].__setitem__("unknown_nested_key", True),
    ]
    repaired = 0
    unknown = 0
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        for i, mutate in enumerate(mutations):
            data = deepcopy(original)
            mutate(data)
            if i >= len(mutations) - 2:
                unknown += 1
            repair_hash(data)
            if not rejected(data, path):
                raise AssertionError(f"mutation {i} survived")
            repaired += 1
        stale = deepcopy(original)
        stale["regression"]["interior_rows"][0]["Z"] = "777"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status": "C220_MUTATION_PASS", "repaired_hash_rejections": repaired, "stale_hash_rejections": 1, "unknown_key_rejections": unknown, "total_rejections": repaired + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
