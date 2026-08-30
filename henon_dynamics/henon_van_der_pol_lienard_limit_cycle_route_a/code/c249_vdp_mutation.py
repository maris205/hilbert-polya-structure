#!/usr/bin/env python3
"""Hostile repaired-hash and semantic mutation suite for HCS-C249."""
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
EVIDENCE = ROOT / "results/c249_vdp_evidence.json"
CHECKER = ROOT / "code/c249_vdp_checker.py"


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

    # Provenance and route/schema attacks.
    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-08-31"))
    add("source_commit", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("unknown_top", lambda x: x.__setitem__("unexpected", True))
    add("route_a1", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_FAIL"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    # Frozen object and theorem semantic attacks.
    add("frozen_dynamics", lambda x: x["frozen_object"].__setitem__("dynamics", "xdot=x; ydot=y"))
    add("section", lambda x: x["frozen_object"].__setitem__("section", "x=1"))
    add("theorem_lienard", lambda x: x["theorem"].__setitem__("lienard_uniqueness", "not proved"))
    add("theorem_floquet", lambda x: x["theorem"].__setitem__("energy_and_floquet", "no multiplier"))
    add("theorem_scope", lambda x: x["theorem"].__setitem__("scope", "target determinant claimed"))
    add("boundary", lambda x: x["theorem"].__setitem__("boundaries", "all faces omitted"))
    # Parameter and finite receipt attacks.
    add("parameter_mu", lambda x: x["regression"]["parameter_rows"][3].__setitem__("mu", "1/9"))
    add("parameter_cycle", lambda x: x["regression"]["parameter_rows"][4].__setitem__("periodic_orbits", "none"))
    add("parameter_count", lambda x: x["regression"]["parameter_rows"][5].__setitem__("primitive_cycle_count", "zero"))
    add("parameter_stability", lambda x: x["regression"]["parameter_rows"][6].__setitem__("cycle_stability", "repelling"))
    add("parameter_rows_count", lambda x: x["regression"].__setitem__("parameter_row_count", 7))
    add("cycle_rows_count", lambda x: x["regression"].__setitem__("cycle_row_count", 4))
    add("cycle_mu", lambda x: x["regression"]["cycle_rows"][0].__setitem__("mu", "9.000000000000000e-01"))
    add("cycle_section", lambda x: x["regression"]["cycle_rows"][1].__setitem__("section", "wrong"))
    add("cycle_y", lambda x: x["regression"]["cycle_rows"][2].__setitem__("section_y", "0"))
    add("cycle_return", lambda x: x["regression"]["cycle_rows"][3].__setitem__("return_residual", "1"))
    add("cycle_period", lambda x: x["regression"]["cycle_rows"][4].__setitem__("period", "-1"))
    add("cycle_divergence", lambda x: x["regression"]["cycle_rows"][0].__setitem__("divergence_integral", "1"))
    add("cycle_energy", lambda x: x["regression"]["cycle_rows"][1].__setitem__("energy_balance", "1"))
    add("cycle_floquet", lambda x: x["regression"]["cycle_rows"][2].__setitem__("floquet_multiplier", "2"))
    add("cycle_radius", lambda x: x["regression"]["cycle_rows"][3].__setitem__("radius_squared_integral", "-1"))
    add("cycle_status", lambda x: x["regression"]["cycle_rows"][4].__setitem__("status", "target claim"))
    add("identity_formula", lambda x: x["exact_identities"][4].__setitem__("formula", "wrong energy"))
    add("identity_missing", lambda x: x["exact_identities"].pop())
    add("citation_url", lambda x: x["citations"][1].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].pop())
    add("cycle_unknown", lambda x: x["regression"]["cycle_rows"][0].__setitem__("unexpected", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64), repaired=False)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c249-vdp-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path), "--quick"], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations) - set(caught)}"
    print(f"C249 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
