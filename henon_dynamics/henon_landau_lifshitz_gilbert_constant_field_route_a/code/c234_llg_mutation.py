#!/usr/bin/env python3
"""Hostile mutation suite for the C234 receipt."""
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
EVIDENCE = ROOT / "results/c234_llg_evidence.json"
CHECKER = ROOT / "code/c234_llg_checker.py"


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, fn) -> None:
        x = deepcopy(pristine)
        fn(x)
        mutations.append((name, x))

    def add_repaired(name: str, fn) -> None:
        """Add a mutation with a recomputed payload hash.

        Repaired-hash cases ensure the independent checker rejects semantic
        drift rather than merely noticing a stale digest.
        """
        x = deepcopy(pristine)
        fn(x)
        body = dict(x)
        body.pop("payload_sha256", None)
        x["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
        mutations.append((name, x))

    add("flow_m3", lambda x: x["regression"]["flow_rows"][0].__setitem__("m3_exact", "0"))
    add("flow_z", lambda x: x["regression"]["flow_rows"][1].__setitem__("z_real", "9"))
    add("flow_radius", lambda x: x["regression"]["flow_rows"][2].__setitem__("transverse_radius", "0"))
    add("flow_energy", lambda x: x["regression"]["flow_rows"][3].__setitem__("energy_derivative", "1"))
    add("flow_norm", lambda x: x["regression"]["flow_rows"][4].__setitem__("norm_residual", "1"))
    add("flow_alpha", lambda x: x["regression"]["flow_rows"][5].__setitem__("damping_rate_alpha_omega", "2"))
    add("stability_north", lambda x: x["regression"]["stability_rows"][0].__setitem__("north_class", "unstable"))
    add("stability_eigen", lambda x: x["regression"]["stability_rows"][1].__setitem__("south_real_eigenvalue", "-4"))
    add("sample_class", lambda x: x["regression"]["sampled_rows"][0].__setitem__("fixed_set_class", "damped_two_poles"))
    add("sample_dimension", lambda x: x["regression"]["sampled_rows"][1].__setitem__("fixed_set_dimension", 2))
    add("boundary_face", lambda x: x["regression"]["boundary_rows"][0].__setitem__("flow", "rotation"))
    # Repaired-hash boundary mutations cover every row and the principal
    # semantic fields (condition/flow/energy/fixed set), plus row ordering.
    add_repaired("boundary_omega_condition", lambda x: x["regression"]["boundary_rows"][0].__setitem__("condition", "omega=1"))
    add_repaired("boundary_omega_flow", lambda x: x["regression"]["boundary_rows"][0].__setitem__("flow", "rotation"))
    add_repaired("boundary_alpha_fixed_set", lambda x: x["regression"]["boundary_rows"][1].__setitem__("fixed_set", "whole_sphere"))
    add_repaired("boundary_damping_energy", lambda x: x["regression"]["boundary_rows"][2].__setitem__("energy_change", "0"))
    add_repaired("boundary_north_condition", lambda x: x["regression"]["boundary_rows"][3].__setitem__("condition", "m=-e3"))
    add_repaired("boundary_south_flow", lambda x: x["regression"]["boundary_rows"][4].__setitem__("flow", "rotation"))
    add_repaired("boundary_row_order", lambda x: x["regression"]["boundary_rows"].reverse())
    add_repaired("boundary_south_face", lambda x: x["regression"]["boundary_rows"][4].__setitem__("face", "north_pole"))
    add("theorem_flow", lambda x: x["theorem"].__setitem__("stereographic_solution", "arbitrary flow"))
    add("theorem_energy", lambda x: x["theorem"].__setitem__("energy_dissipation", "energy grows"))
    add("theorem_stability", lambda x: x["theorem"].__setitem__("stability", "south is stable"))
    add("theorem_sample", lambda x: x["theorem"].__setitem__("sampled_fixed_sets", "never whole sphere"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("periodic_orbit", lambda x: x["frozen_object"].__setitem__("primitive_periodic_orbit", True))
    add("citation_title", lambda x: x["citations"][0].__setitem__("title", "fabricated title"))
    add("citation_doi", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"))
    add_repaired("citation_doi_repaired_hash", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"))
    add("unknown_nested", lambda x: x["theorem"].__setitem__("unknown_nested", True))
    add("unknown_top", lambda x: x.__setitem__("unknown_top", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64))
    add("row_count", lambda x: x["regression"]["row_counts"].__setitem__("flow", 5))
    add("missing_row", lambda x: x["regression"]["sampled_rows"].pop())
    add("schema", lambda x: x.__setitem__("schema", "wrong-schema"))

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c234-llg-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--input", str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations)-set(caught)}"
    print(f"C234 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
