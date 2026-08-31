#!/usr/bin/env python3
"""Repaired-hash semantic mutation suite for HCS-C261."""
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
EVIDENCE = ROOT / "results/c261_airy_evidence.json"
CHECKER = ROOT / "code/c261_airy_checker.py"


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
    add("equation_sign", lambda x: x["frozen_object"].__setitem__("equation", "u_t-u_xxx=0"))
    add("mode_sign", lambda x: x["frozen_object"].__setitem__("fourier_action", "exp(-i*n^3*t)"))
    add("log_clock", lambda x: x["frozen_object"].__setitem__("clock", "log prime clock"))
    add("target_det", lambda x: x["frozen_object"].__setitem__("determinant_convention", "target determinant"))
    add("unitary", lambda x: x["theorem"].__setitem__("unitary_group", "contractive semigroup"))
    add("full_period", lambda x: x["theorem"].__setitem__("minimal_full_period", "period pi"))
    add("revival", lambda x: x["theorem"].__setitem__("rational_revival", "quadratic phase"))
    add("strobe", lambda x: x["theorem"].__setitem__("strobe_order", "order divides q"))
    add("fixed", lambda x: x["theorem"].__setitem__("fixed_modes", "q divides n"))
    add("state_period", lambda x: x["theorem"].__setitem__("state_period", "2*pi/max(S)"))
    add("irrational", lambda x: x["theorem"].__setitem__("irrational_sampling", "all modes fixed"))
    add("compact", lambda x: x["theorem"].__setitem__("operator_boundary", "trace class"))
    add("route_a1", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_a4", lambda x: x["route_a"]["tuple"].__setitem__(4, "A4_ROUTE_B_READY"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_root_numbers", True))
    add("qmax", lambda x: x["receipts"].__setitem__("q_max", 95))
    add("row_count", lambda x: x["receipts"].__setitem__("modular_row_count", 1))
    add("row_id", lambda x: x["receipts"]["modular_rows"][0].__setitem__("row_id", "bad"))
    add("phase_hash", lambda x: x["receipts"]["modular_rows"][1].__setitem__("phase_exponent_sha256", "0"*64))
    add("order", lambda x: x["receipts"]["modular_rows"][2].__setitem__("strobe_order", 99))
    add("stride", lambda x: x["receipts"]["modular_rows"][3].__setitem__("fixed_mode_stride", 99))
    add("density", lambda x: x["receipts"]["modular_rows"][4].__setitem__("fixed_mode_density", "1/99"))
    add("fixed_count", lambda x: x["receipts"]["modular_rows"][5].__setitem__("fixed_modes_in_minus512_to_512", 0))
    add("dft_count", lambda x: x["receipts"].__setitem__("dft_row_count", 0))
    add("dft_pair", lambda x: x["receipts"]["dft_rows"][0].__setitem__("q", 9))
    add("support", lambda x: x["receipts"]["support_rows"][0].__setitem__("fourier_support", [1, 2]))
    add("support_gcd", lambda x: x["receipts"]["support_rows"][1].__setitem__("gcd_nonzero_cubic_frequencies", 8))
    add("identity", lambda x: x["exact_identities"][1].__setitem__("formula", "square"))
    add("citation", lambda x: x["citations"][1].__setitem__("source", "G. Farmakis et al., Proceedings of the Royal Society A 477 (2021)"))
    add("nonclaim", lambda x: x["nonclaims"].pop())
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0"*64), repaired=False)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c261-airy-mutations-") as directory:
        for name, item in mutations:
            path = Path(directory) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path), "--quick"], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode != 0:
                caught.append(name)
    missing = {name for name, _ in mutations} - set(caught)
    assert not missing, f"uncaught mutations: {sorted(missing)}"
    print(f"C261 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
