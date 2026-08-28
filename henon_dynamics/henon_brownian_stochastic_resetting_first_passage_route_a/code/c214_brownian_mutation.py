#!/usr/bin/env python3
"""Hostile repaired-hash, stale-hash, and schema mutations for C214."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c214_brownian_evidence.json"
CHECKER = Path(__file__).with_name("c214_brownian_checker.py")


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
        lambda d: d["evaluator"].__setitem__("sha256", "0" * 64),
        lambda d: d.__setitem__("scope_literal", "BAD_SCOPE"),
        lambda d: d.__setitem__("headline", "synthetic"),
        lambda d: d["frozen_object"].__setitem__("determinant_convention", "dynamical zeta"),
        lambda d: d["frozen_object"].__setitem__("process", "prime-fitted process"),
        lambda d: d["theorem"].__setitem__("stationary_laplace", "also stationary after killing"),
        lambda d: d["theorem"].__setitem__("fpt_laplace", "1"),
        lambda d: d["theorem"].__setitem__("survival_laplace", "wrong survival"),
        lambda d: d["theorem"].__setitem__("optimality", "all rates optimal"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS"] * 5),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_euler_factors", True),
        lambda d: d["citations"][0].__setitem__("persistent_url", "https://example.invalid"),
        lambda d: d["regression"].__setitem__("D_values", ["0"]),
        lambda d: d["regression"]["propagator_rows"][0].__setitem__("reset_density", "0"),
        lambda d: d["regression"]["propagator_rows"][1].__setitem__("reset_integral", "99"),
        lambda d: d["regression"]["fpt_rows"][0].__setitem__("fpt_laplace", "0"),
        lambda d: d["regression"]["fpt_rows"][1].__setitem__("case_id", d["regression"]["fpt_rows"][0]["case_id"]),
        lambda d: d["regression"]["mfpt_rows"][0].__setitem__("mfpt", "0"),
        lambda d: d["regression"]["boundary_rows"][0].__setitem__("statement", "stationary after killing"),
        lambda d: d["summary"].__setitem__("fpt_row_count", 1),
        lambda d: d["nonclaims"].clear(),
        lambda d: d.__setitem__("unknown_top_level_key", True),
        lambda d: d["regression"]["fpt_rows"][0].__setitem__("unknown_nested_key", True),
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
        stale["regression"]["mfpt_rows"][0]["scaled_mfpt"] = "777"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status": "C214_MUTATION_PASS", "repaired_hash_rejections": repaired, "stale_hash_rejections": 1, "unknown_key_rejections": unknown, "total_rejections": repaired + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
