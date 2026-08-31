#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C257."""
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
EVIDENCE = ROOT / "results/c257_newton_cayley_evidence.json"
CHECKER = ROOT / "code/c257_newton_checker.py"


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
    add("source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("unknown_top", lambda x: x.__setitem__("unexpected", True))
    add("phase", lambda x: x["frozen_object"].__setitem__("phase_space", "R"))
    add("dynamics", lambda x: x["frozen_object"].__setitem__("dynamics", "z^2"))
    add("cayley", lambda x: x["frozen_object"].__setitem__("cayley_coordinate", "w=z"))
    add("route_a1", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    add("failure", lambda x: x["route_a"].__setitem__("strongest_failure", "none"))
    add("theorem_conjugacy", lambda x: x["theorem"].__setitem__("global_conjugacy", "not proved"))
    add("theorem_basins", lambda x: x["theorem"].__setitem__("basin_julia_atlas", "wrong"))
    add("theorem_tail", lambda x: x["theorem"].__setitem__("periodic_preperiodic", "omitted"))
    add("theorem_owner", lambda x: x["theorem"].__setitem__("ownership", "same as C177"))
    add("period_count", lambda x: x["exact_receipt"].__setitem__("period_row_count", 15))
    add("period_n", lambda x: x["exact_receipt"]["period_rows"][2].__setitem__("n", 9))
    add("fixed", lambda x: x["exact_receipt"]["period_rows"][3].__setitem__("fixed_points_on_sphere", 0))
    add("exact", lambda x: x["exact_receipt"]["period_rows"][4].__setitem__("exact_period_points", 1))
    add("orbits", lambda x: x["exact_receipt"]["period_rows"][5].__setitem__("primitive_orbits", 1))
    add("multiplier", lambda x: x["exact_receipt"]["period_rows"][6].__setitem__("julia_cycle_multiplier", "3"))
    add("order_count", lambda x: x["exact_receipt"].__setitem__("root_order_row_count", 127))
    add("order_m", lambda x: x["exact_receipt"]["root_order_rows"][17].__setitem__("root_of_unity_order", 19))
    add("tail", lambda x: x["exact_receipt"]["root_order_rows"][31].__setitem__("two_adic_tail", 0))
    add("odd", lambda x: x["exact_receipt"]["root_order_rows"][47].__setitem__("odd_part", 5))
    add("eventual_period", lambda x: x["exact_receipt"]["root_order_rows"][62].__setitem__("eventual_exact_period", 99))
    add("classification", lambda x: x["exact_receipt"]["root_order_rows"][63].__setitem__("classification", "periodic"))
    add("real_w", lambda x: x["exact_receipt"]["real_sample_rows"][0].__setitem__("w_after_2", "0"))
    add("real_basin", lambda x: x["exact_receipt"]["real_sample_rows"][5].__setitem__("basin", "root -a"))
    add("cauchy_map", lambda x: x["exact_receipt"]["cauchy_rows"][1].__setitem__("T(s)=(s^2-1)/(2s)", "0"))
    add("cauchy_density", lambda x: x["exact_receipt"]["cauchy_rows"][2].__setitem__("density", "uniform"))
    add("identity", lambda x: x["exact_identities"][2].__setitem__("formula", "wrong"))
    add("identity_drop", lambda x: x["exact_identities"].pop())
    add("citation", lambda x: x["citations"][0].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].pop())
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64), repaired=False)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c257-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / (name + ".json")
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path), "--quick"], env=env, capture_output=True, text=True)
            if proc.returncode != 0:
                caught.append(name)
    missing = set(name for name, _ in mutations) - set(caught)
    if missing:
        raise AssertionError("uncaught mutations: " + ",".join(sorted(missing)))
    print(f"C257 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
