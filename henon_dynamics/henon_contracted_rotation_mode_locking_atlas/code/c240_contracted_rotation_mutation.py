#!/usr/bin/env python3
"""Hostile mutation suite for the C240 evidence contract."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c240_contracted_rotation_evidence.json"
CHECKER = ROOT / "code/c240_contracted_rotation_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c240_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def repair(data: dict) -> dict:
    data["payload_sha256"] = checker.payload_hash(data)
    return data


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, edit, repaired: bool = True) -> None:
        x = deepcopy(pristine)
        edit(x)
        if x == pristine:
            raise AssertionError(f"mutation {name} is a no-op")
        mutations.append((name, repair(x) if repaired else x))

    add("stale_hash_word", lambda x: x["regression"]["word_rows"][0].__setitem__("word", "1"), repaired=False)
    add("word_length", lambda x: x["regression"]["word_rows"][100].__setitem__("length", 99))
    add("word_id", lambda x: x["regression"]["word_rows"][4].__setitem__("word_id", "bad"))
    add("word_carry_sum", lambda x: x["regression"]["word_rows"][20].__setitem__("carry_sum", 7))
    add("word_rotation", lambda x: x["regression"]["word_rows"][20].__setitem__("rotation_number", "1/2"))
    add("word_derivative", lambda x: x["regression"]["word_rows"][30].__setitem__("derivative", "1"))
    add("fixed_slope", lambda x: x["regression"]["word_rows"][1]["fixed_point_affine"].__setitem__("delta_slope", "0"))
    add("state_affine", lambda x: x["regression"]["word_rows"][3]["state_affines"][0].__setitem__("constant", "1"))
    add("interval_lower", lambda x: x["regression"]["word_rows"][1]["delta_interval"].__setitem__("lo", "0"))
    add("interval_upper", lambda x: x["regression"]["word_rows"][2]["delta_interval"].__setitem__("hi", "1"))
    add("interval_closed", lambda x: x["regression"]["word_rows"][1]["delta_interval"].__setitem__("hi_closed", True))
    add("interval_nonempty", lambda x: x["regression"]["word_rows"][2]["delta_interval"].__setitem__("nonempty", False))
    add("boundary_active", lambda x: x["regression"]["word_rows"][1]["boundary_audit"]["lo"]["active_constraints"].append("fake"))
    add("boundary_valid", lambda x: x["regression"]["word_rows"][1]["boundary_audit"]["hi"].__setitem__("half_open_admissible", True))
    add("plateau_component", lambda x: x["regression"]["plateau_rows"][0]["component_count"].__setitem__(0, 0) if isinstance(x["regression"]["plateau_rows"][0]["component_count"], list) else x["regression"]["plateau_rows"][0].__setitem__("component_count", 99))
    add("direct_period", lambda x: x["regression"]["direct_iteration_rows"][0].__setitem__("suffix_period", 12))
    add("direct_word", lambda x: x["regression"]["direct_iteration_rows"][1].__setitem__("suffix_word", "111"))
    add("direct_fixed", lambda x: x["regression"]["direct_iteration_rows"][2].__setitem__("fixed_point", "0"))
    add("direct_residual", lambda x: x["regression"]["direct_iteration_rows"][6].__setitem__("iteration_residual", "1"))
    add("direct_converged", lambda x: x["regression"]["direct_iteration_rows"][4].__setitem__("converged", True))
    add("direct_boundary_ids", lambda x: x["regression"]["direct_iteration_rows"][5].__setitem__("exact_boundary_word_ids", []))
    add("word_count", lambda x: x["regression"].__setitem__("total_word_rows", 0))
    add("source_lock", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator_lock", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("fixed_epoch", lambda x: x.__setitem__("fixed_epoch", 1788048001))
    add("scope_literal", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(2, "A2_CERTIFIED_PREFIX"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("theorem_global_unique", lambda x: x["theorem"].__setitem__("uniqueness_scope", "Every parameter has one global periodic orbit with no qualification."))
    add("theorem_maximal_plateau", lambda x: x["theorem"].__setitem__("mode_locking_scope", "All grouped rows are maximal global plateaux."))
    add("unknown_top", lambda x: x.__setitem__("unknown", 1))

    rejected = 0
    accepted: list[str] = []
    for name, mutant in mutations:
        try:
            checker.validate(mutant)
        except Exception:
            rejected += 1
        else:
            accepted.append(name)
    if accepted:
        raise AssertionError(f"accepted hostile mutations: {accepted}")
    print(f"C240 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
