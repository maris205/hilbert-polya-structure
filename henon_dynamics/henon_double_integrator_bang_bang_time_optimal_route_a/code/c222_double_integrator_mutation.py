#!/usr/bin/env python3
"""Repaired-hash semantic/schema and stale-hash hostile tests for C222."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c222_double_integrator_evidence.json"
CHECKER = Path(__file__).with_name("c222_double_integrator_checker.py")


def repair(data: dict) -> None:
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
        lambda d: d["frozen_object"].__setitem__("dynamics", "x_dot=0"),
        lambda d: d["frozen_object"].__setitem__("determinant_convention", "dynamical zeta"),
        lambda d: d["theorem"].__setitem__("switching_curve", "x=0"),
        lambda d: d["theorem"].__setitem__("arc_times", "negative times allowed"),
        lambda d: d["theorem"].__setitem__("hjb", "residual nonzero"),
        lambda d: d["theorem"].__setitem__("reachable_set_certificate", "unbounded control"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS"] * 5),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True),
        lambda d: d["citations"][0].__setitem__("persistent_url", "https://example.invalid"),
        lambda d: d["regression"].__setitem__("a_values", ["0"]),
        lambda d: d["regression"]["state_rows"][0].__setitem__("total_time", "0"),
        lambda d: d["regression"]["state_rows"][1].__setitem__("case_id", d["regression"]["state_rows"][0]["case_id"]),
        lambda d: d["regression"]["state_rows"][2].__setitem__("first_control_over_a", 7),
        lambda d: d["summary"].__setitem__("state_row_count", 1),
        lambda d: d["nonclaims"].clear(),
        lambda d: d.__setitem__("unknown_top_level_key", True),
        lambda d: d["regression"]["state_rows"][0].__setitem__("unknown_nested_key", True),
    ]
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        repaired = 0
        for i, mutate in enumerate(mutations):
            data = deepcopy(original)
            mutate(data)
            repair(data)
            if not rejected(data, path):
                raise AssertionError(f"repaired-hash mutation {i} survived")
            repaired += 1
        stale = deepcopy(original)
        stale["regression"]["state_rows"][0]["switching_function"] = "999"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status": "C222_MUTATION_PASS", "repaired_hash_rejections": repaired, "unknown_key_rejections": 2, "stale_hash_rejections": 1, "total_rejections": repaired + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
