#!/usr/bin/env python3
"""Repaired-hash semantic mutation suite for HCS-C256."""
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
EVIDENCE = ROOT / "results/c256_kdv_evidence.json"
CHECKER = ROOT / "code/c256_kdv_checker.py"


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
    add("route_a1", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_root_numbers", True))
    add("equation_sign", lambda x: x["frozen_object"].__setitem__("equation", "u_t-6*u*u_x+u_xxx=0"))
    add("clock", lambda x: x["frozen_object"].__setitem__("clock", "log prime clock"))
    add("determinant", lambda x: x["frozen_object"].__setitem__("determinant_convention", "target determinant"))
    add("first_integral", lambda x: x["theorem"].__setitem__("first_integral", "wrong sign"))
    add("classification", lambda x: x["theorem"].__setitem__("bounded_classification", "all cubics are periodic"))
    add("periodic_formula", lambda x: x["theorem"].__setitem__("periodic_formula", "sn instead of cn"))
    add("period_mean", lambda x: x["theorem"].__setitem__("period_and_mean", "period is 4K"))
    add("soliton_face", lambda x: x["theorem"].__setitem__("soliton_face", "upper double root"))
    add("harmonic_face", lambda x: x["theorem"].__setitem__("harmonic_face", "finite amplitude"))
    add("galilean_theorem", lambda x: x["theorem"].__setitem__("galilean", "speed shifts by a"))
    add("temporal_return", lambda x: x["theorem"].__setitem__("temporal_return", "T=abs(c)/L"))
    add("scope_theorem", lambda x: x["theorem"].__setitem__("scope", "all KdV solutions"))
    add("periodic_count", lambda x: x["receipts"].__setitem__("periodic_row_count", 11))
    add("soliton_count", lambda x: x["receipts"].__setitem__("soliton_row_count", 2))
    add("root", lambda x: x["receipts"]["periodic_rows"][0]["roots"].__setitem__(1, "-3"))
    add("root_order", lambda x: x["receipts"]["periodic_rows"][1].__setitem__("root_order", "unordered"))
    add("speed", lambda x: x["receipts"]["periodic_rows"][2].__setitem__("speed", "9"))
    add("pair_sum", lambda x: x["receipts"]["periodic_rows"][3].__setitem__("pair_sum", "0"))
    add("modulus", lambda x: x["receipts"]["periodic_rows"][4].__setitem__("modulus_m", "1/2"))
    add("amplitude", lambda x: x["receipts"]["periodic_rows"][5].__setitem__("amplitude", "2"))
    add("wave_number", lambda x: x["receipts"]["periodic_rows"][6].__setitem__("wave_number", "2.0"))
    add("K", lambda x: x["receipts"]["periodic_rows"][7].__setitem__("K", "1.0"))
    add("period", lambda x: x["receipts"]["periodic_rows"][8].__setitem__("fundamental_period", "4.0"))
    add("mean", lambda x: x["receipts"]["periodic_rows"][9].__setitem__("period_mean", "0.0"))
    add("mean_square", lambda x: x["receipts"]["periodic_rows"][10].__setitem__("period_mean_square", "0.0"))
    add("residual", lambda x: x["receipts"]["periodic_rows"][11].__setitem__("max_profile_ode_residual_17_nodes", "1e-2"))
    add("soliton_speed", lambda x: x["receipts"]["soliton_rows"][0].__setitem__("speed", "0"))
    add("soliton_mass", lambda x: x["receipts"]["soliton_rows"][1].__setitem__("excess_mass", "1"))
    add("harmonic_constant", lambda x: x["receipts"]["harmonic_rows"][0].__setitem__("constant_level", "0"))
    add("harmonic_period", lambda x: x["receipts"]["harmonic_rows"][1].__setitem__("limiting_period", "1"))
    add("harmonic_qualification", lambda x: x["receipts"]["harmonic_rows"][2].__setitem__("qualification", "constant selects speed"))
    add("galilean_shift", lambda x: x["receipts"]["galilean_rows"][0].__setitem__("shift_a", "0"))
    add("galilean_speed", lambda x: x["receipts"]["galilean_rows"][1].__setitem__("speed_increment", "-1"))
    add("identity", lambda x: x["exact_identities"][7].__setitem__("formula", "L=4*K"))
    add("citation", lambda x: x["citations"][1].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].pop())
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0"*64), repaired=False)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c256-kdv-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path), "--quick"], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode != 0:
                caught.append(name)
    missing = {name for name, _ in mutations} - set(caught)
    assert not missing, f"uncaught mutations: {sorted(missing)}"
    print(f"C256 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
