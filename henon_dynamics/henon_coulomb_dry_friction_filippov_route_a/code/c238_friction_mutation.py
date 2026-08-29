#!/usr/bin/env python3
"""Hostile mutation suite for the C238 evidence contract."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c238_friction_evidence.json"
CHECKER = ROOT / "code/c238_friction_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c238_checker", CHECKER)
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

    add("stale_hash", lambda x: x["regression"]["rest_rows"][0].__setitem__("half_cycles", 99), repaired=False)
    add("rest_count", lambda x: x["regression"].__setitem__("rest_row_count", 7))
    add("rest_turn", lambda x: x["regression"]["rest_rows"][2]["turning_points"].__setitem__(0, "999"))
    add("rest_threshold", lambda x: x["regression"]["rest_rows"][3].__setitem__("stopping_turn", "999"))
    add("rest_energy", lambda x: x["regression"]["rest_rows"][4].__setitem__("final_energy", "0"))
    add("general_center_sign", lambda x: x["regression"]["general_rows"][7].__setitem__("center", "-1"))
    add("general_phase", lambda x: x["regression"]["general_rows"][7].__setitem__("initial_phase", "3.141592653589793"))
    add("general_arc_count", lambda x: x["regression"]["general_rows"][0].__setitem__("moving_arc_count", 1))
    add("general_first_turn", lambda x: x["regression"]["general_rows"][1].__setitem__("first_turn", "1"))
    add("general_stop_time", lambda x: x["regression"]["general_rows"][2].__setitem__("stopping_time", "0"))
    add("general_radius", lambda x: x["regression"]["general_rows"][3].__setitem__("radius", "0"))
    add("stick_regime", lambda x: x["regression"]["stick_rows"][0].__setitem__("regime", "release_left"))
    add("stick_acceleration", lambda x: x["regression"]["stick_rows"][2].__setitem__("selected_acceleration", "0"))
    add("harmonic_x", lambda x: x["regression"]["harmonic_rows"][0].__setitem__("x", "0"))
    add("harmonic_energy", lambda x: x["regression"]["harmonic_rows"][1].__setitem__("energy", "0"))
    add("dissipation_residual", lambda x: x["regression"]["dissipation_rows"][0].__setitem__("dissipation_residual", "1"))
    add("dissipation_turn", lambda x: x["regression"]["dissipation_rows"][1].__setitem__("first_turn", "0"))
    add("general_count", lambda x: x["regression"].__setitem__("general_row_count", 9))
    add("harmonic_count", lambda x: x["regression"].__setitem__("harmonic_row_count", 3))
    add("source_lock", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator_lock", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("scope_literal", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("unknown_top", lambda x: x.__setitem__("unknown", 1))
    add("backward_uniqueness_overclaim", lambda x: x["theorem"].__setitem__("wellposedness", "The selected trajectory is unique for all forward and backward times."))
    add("zero_friction_capture_overclaim", lambda x: x["theorem"].__setitem__("capture_count", "The rest capture formula holds for all c>=0."))

    rejected = 0; accepted: list[str] = []
    for name, mutant in mutations:
        try: checker.validate(mutant)
        except Exception: rejected += 1
        else: accepted.append(name)
    if accepted: raise AssertionError(f"accepted hostile mutations: {accepted}")
    print(f"C238 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__": main()
