#!/usr/bin/env python3
"""Hostile repaired-hash mutations for the C243 dimer receipt."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c243_dimer_evidence.json"
CHECKER = ROOT / "code/c243_dimer_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c243_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)


def repair(data: dict) -> dict:
    data["payload_sha256"] = checker.payload_hash(data)
    return data


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, edit, repaired: bool = True) -> None:
        x = deepcopy(pristine); edit(x); mutations.append((name, repair(x) if repaired else x))

    add("stale_hash", lambda x: x["regression"]["level_rows"][2].__setitem__("period", "0"), False)
    add("fixed_stability", lambda x: x["regression"]["fixed_points"][2].__setitem__("stability", "hyperbolic"))
    add("fixed_frequency", lambda x: x["regression"]["fixed_points"][0].__setitem__("frequency_or_growth", "0"))
    add("pitchfork_label", lambda x: x["regression"]["fixed_points"][5].__setitem__("stability", "elliptic"))
    add("broken_z", lambda x: x["regression"]["fixed_points"][9].__setitem__("z", "0"))
    add("broken_energy", lambda x: x["regression"]["fixed_points"][10].__setitem__("energy", "1"))
    add("pole_vector", lambda x: x["regression"]["bloch_poles"][0].__setitem__("ydot", "-1"))
    add("pole_chart", lambda x: x["regression"]["bloch_poles"][1].__setitem__("chart", "z_phi"))
    add("level_root", lambda x: x["regression"]["level_rows"][2].__setitem__("y_plus", "0"))
    add("level_modulus", lambda x: x["regression"]["level_rows"][3].__setitem__("elliptic_modulus", "0"))
    add("level_period", lambda x: x["regression"]["level_rows"][4].__setitem__("period", "0"))
    add("level_type", lambda x: x["regression"]["level_rows"][5].__setitem__("level_type", "regular_self_trapped"))
    add("component_count", lambda x: x["regression"]["level_rows"][7].__setitem__("sign_components", 2))
    add("crossing_flag", lambda x: x["regression"]["level_rows"][7].__setitem__("crosses_zero", False))
    add("separatrix_profile", lambda x: x["regression"]["level_rows"][8].__setitem__("separatrix_profile", "wrong"))
    add("pole_warning", lambda x: x["regression"]["level_rows"][8].__setitem__("pole_coordinate_warning", False))
    add("self_criterion", lambda x: x["regression"]["criterion_rows"][1].__setitem__("verdict", "crossing"))
    add("criterion_reverse", lambda x: x["regression"]["criterion_rows"][2].__setitem__("reverse_condition", "none"))
    add("level_count", lambda x: x["regression"].__setitem__("level_row_count", 12))
    add("identity_count", lambda x: x["exact_identities"].pop())
    add("source_lock", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator_lock", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("scope_literal", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("unknown_top", lambda x: x.__setitem__("unknown", 1))
    add("self_trapping_theorem", lambda x: x["theorem"].__setitem__("self_trapping", "all levels self-trap"))

    rejected = 0; accepted: list[str] = []
    for name, mutant in mutations:
        try: checker.validate(mutant)
        except Exception: rejected += 1
        else: accepted.append(name)
    if accepted: raise AssertionError(f"accepted hostile mutations: {accepted}")
    print(f"C243 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__": main()
