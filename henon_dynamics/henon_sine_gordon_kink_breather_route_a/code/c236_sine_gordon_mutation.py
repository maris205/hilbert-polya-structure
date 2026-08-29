#!/usr/bin/env python3
"""Hostile mutation suite for the C236 receipt (including citation locks)."""
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
EVIDENCE = ROOT / "results/c236_sine_gordon_evidence.json"
CHECKER = ROOT / "code/c236_sine_gordon_checker.py"


def repair(item: dict) -> dict:
    body = dict(item)
    body.pop("payload_sha256", None)
    item["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return item


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, fn, repaired: bool = True) -> None:
        item = deepcopy(pristine)
        fn(item)
        if repaired:
            repair(item)
        mutations.append((name, item))

    add("kink_gamma", lambda x: x["regression"]["kink_rows"][0].__setitem__("gamma", "1"))
    add("kink_energy", lambda x: x["regression"]["kink_rows"][1].__setitem__("energy", "0"))
    add("kink_momentum", lambda x: x["regression"]["kink_rows"][2].__setitem__("momentum", "9"))
    add("kink_charge", lambda x: x["regression"]["kink_rows"][3].__setitem__("topological_charge", 0))
    add("kink_mass_shell", lambda x: x["regression"]["kink_rows"][4].__setitem__("mass_shell_residual", "1"))
    add("kink_profile", lambda x: x["regression"]["kink_rows"][5].__setitem__("center_profile", "0"))
    add("breather_eta", lambda x: x["regression"]["breather_rows"][0].__setitem__("eta_sqrt_1_minus_Omega2", "0"))
    add("breather_period", lambda x: x["regression"]["breather_rows"][1].__setitem__("rest_period", "1"))
    add("breather_rest_energy", lambda x: x["regression"]["breather_rows"][2].__setitem__("rest_energy", "1"))
    add("breather_lab_energy", lambda x: x["regression"]["breather_rows"][3].__setitem__("lab_energy", "1"))
    add("breather_lab_momentum", lambda x: x["regression"]["breather_rows"][4].__setitem__("lab_momentum", "-1"))
    add("breather_clock", lambda x: x["regression"]["breather_rows"][5].__setitem__("lab_fixed_x_period_claimed", True))
    add("hessian_potential", lambda x: x["regression"]["hessian_rows"][0].__setitem__("hessian_potential", "1"))
    add("hessian_kernel", lambda x: x["regression"]["hessian_rows"][1].__setitem__("kernel_mode", "1"))
    add("hessian_edge", lambda x: x["regression"]["hessian_rows"][2].__setitem__("essential_edge", "0"))
    add("hessian_factor", lambda x: x["regression"]["hessian_rows"][3].__setitem__("factorization_quadratic_form_nonnegative", False))
    add("theorem_scope", lambda x: x["theorem"].__setitem__("coherent_scope", "all solutions classified"))
    add("theorem_period", lambda x: x["theorem"].__setitem__("breather_boost", "fixed lab period for every V"))
    add("theorem_spectrum", lambda x: x["theorem"].__setitem__("hessian_spectrum", "all real"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(4, "A4_PASS"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("primitive_orbit", lambda x: x["frozen_object"].__setitem__("primitive_periodic_orbit", True))
    add("citation_title", lambda x: x["citations"][0].__setitem__("title", "fabricated title"))
    add("citation_issue", lambda x: x["citations"][0].__setitem__("venue", "Physical Review A 18(3), 1652--1680"))
    add("citation_doi", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"))
    add("unknown_nested", lambda x: x["theorem"].__setitem__("unknown_nested", True))
    add("unknown_top", lambda x: x.__setitem__("unknown_top", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64), repaired=False)
    add("row_count", lambda x: x["regression"]["row_counts"].__setitem__("kink", 5))
    add("missing_row", lambda x: x["regression"]["breather_rows"].pop())
    add("schema", lambda x: x.__setitem__("schema", "wrong-schema"))
    add("boundary_rest_profile", lambda x: x["regression"]["boundary_rows"][0].__setitem__("profile", "moving kink"))
    add("boundary_speed_condition", lambda x: x["regression"]["boundary_rows"][1].__setitem__("condition", "|v|<=1"))
    add("boundary_light_energy", lambda x: x["regression"]["boundary_rows"][2].__setitem__("energy_limit", "finite"))
    add("boundary_small_period", lambda x: x["regression"]["boundary_rows"][3].__setitem__("period_statement", "fixed lab"))
    add("boundary_separatrix_profile", lambda x: x["regression"]["boundary_rows"][4].__setitem__("profile", "periodic"))
    add("boundary_rest_energy", lambda x: x["regression"]["boundary_rows"][5].__setitem__("energy_limit", "0"))
    add("boundary_boost_clock", lambda x: x["regression"]["boundary_rows"][6].__setitem__("period_statement", "fixed lab"))
    add("boundary_vacuum_profile", lambda x: x["regression"]["boundary_rows"][7].__setitem__("profile", "kink"))

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c236-sg-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--input", str(path)], env=env,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(n for n, _ in mutations) - set(caught)}"
    print(f"C236 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
