#!/usr/bin/env python3
"""Repaired-hash semantic mutation suite for HCS-C262."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c262_hill_evidence.json"
CHECKER = ROOT / "code/c262_hill_checker.py"


def repair(item: dict) -> dict:
    body = dict(item)
    body.pop("payload_sha256", None)
    item["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return item


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, change, repaired: bool = True) -> None:
        item = deepcopy(pristine)
        change(item)
        mutations.append((name, repair(item) if repaired else item))

    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-08-30"))
    add("source", lambda x: x.__setitem__("source_commit", "0"*40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0"*64))
    add("unknown_top", lambda x: x.__setitem__("unexpected", True))
    add("equation", lambda x: x["frozen_object"].__setitem__("equation", "y''-k(t)y=0"))
    add("period_face", lambda x: x["frozen_object"].__setitem__("parameters", "zero period only"))
    add("clock", lambda x: x["frozen_object"].__setitem__("clock", "log prime clock"))
    add("target_det", lambda x: x["frozen_object"].__setitem__("determinant_convention", "target determinant"))
    add("segments", lambda x: x["theorem"].__setitem__("entire_segments", "C^2-kS^2=1"))
    add("monodromy", lambda x: x["theorem"].__setitem__("monodromy", "det M=-1"))
    add("delta", lambda x: x["theorem"].__setitem__("discriminant", "k1-k2"))
    add("floquet", lambda x: x["theorem"].__setitem__("floquet_classification", "all solutions grow"))
    add("jordan", lambda x: x["theorem"].__setitem__("parabolic_boundary", "all solutions periodic"))
    add("iterate", lambda x: x["theorem"].__setitem__("iterate_law", "M^n=nM"))
    add("rates", lambda x: x["theorem"].__setitem__("floquet_rates", "linear in Delta"))
    add("order", lambda x: x["theorem"].__setitem__("faces", "trace changes under swap"))
    add("route_a1", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_a4", lambda x: x["route_a"]["tuple"].__setitem__(4, "A4_ROUTE_B_READY"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    add("k_grid", lambda x: x["receipts"].__setitem__("k_grid", ["0"]))
    add("tau_grid", lambda x: x["receipts"].__setitem__("tau_grid", ["0"]))
    add("grid_count", lambda x: x["receipts"].__setitem__("grid_row_count", 899))
    add("boundary_count", lambda x: x["receipts"].__setitem__("boundary_row_count", 5))
    add("row_id", lambda x: x["receipts"]["grid_rows"][0].__setitem__("row_id", "bad"))
    add("row_parameter", lambda x: x["receipts"]["grid_rows"][1].__setitem__("k1", "99"))
    add("row_trace", lambda x: x["receipts"]["grid_rows"][2].__setitem__("discriminant", "0"))
    add("row_class", lambda x: x["receipts"]["grid_rows"][3].__setitem__("class", "unstable"))
    add("class_counts", lambda x: x["receipts"].__setitem__("class_counts", {}))
    add("plus_jordan", lambda x: x["receipts"]["boundary_rows"][2].__setitem__("matrix", [["1","0"],["0","1"]]))
    add("minus_jordan", lambda x: x["receipts"]["boundary_rows"][3].__setitem__("matrix", [["-1","0"],["0","-1"]]))
    add("hyperbolic", lambda x: x["receipts"]["boundary_rows"][5].__setitem__("matrix", [["1","0"],["0","1"]]))
    add("identity", lambda x: x["exact_identities"][3].__setitem__("formula", "wrong trace"))
    add("citation", lambda x: x["citations"][0].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].pop())
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0"*64), repaired=False)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c262-hill-mutations-") as directory:
        for name, item in mutations:
            path = Path(directory) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path), "--quick"], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode != 0:
                caught.append(name)
    missing = {name for name, _ in mutations} - set(caught)
    assert not missing, f"uncaught mutations: {sorted(missing)}"
    print(f"C262 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught="+",".join(caught))


if __name__ == "__main__":
    main()
