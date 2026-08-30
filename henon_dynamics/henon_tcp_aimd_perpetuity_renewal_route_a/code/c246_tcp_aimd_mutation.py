#!/usr/bin/env python3
"""Hostile mutation suite for the C246 AIMD receipt."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c246_tcp_aimd_evidence.json"
CHECKER = ROOT / "code/c246_tcp_aimd_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c246_checker", CHECKER)
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

    p = 0
    add("stale_hash", lambda x: x["regression"]["parameter_rows"][p]["c"].__setitem__(0, "0") if isinstance(x["regression"]["parameter_rows"][p]["c"], list) else x["regression"]["parameter_rows"][p].__setitem__("c", "0"), repaired=False)
    add("beta", lambda x: x["regression"]["parameter_rows"][p].__setitem__("beta", "1/3"))
    add("a_factor", lambda x: x["regression"]["parameter_rows"][p].__setitem__("a", "1"))
    add("rho", lambda x: x["regression"]["parameter_rows"][p].__setitem__("rho", "3"))
    add("c_factor", lambda x: x["regression"]["parameter_rows"][p].__setitem__("c", "1"))
    add("z_moment", lambda x: x["regression"]["parameter_rows"][p]["embedded_square_moments"][1].__setitem__("value", "0"))
    add("z_order", lambda x: x["regression"]["parameter_rows"][p]["embedded_square_moments"][2].__setitem__("order", 99))
    add("generator_coeff", lambda x: x["regression"]["parameter_rows"][p]["generator_moment_coefficients"][2].__setitem__("constant", "0"))
    add("mu_coeff", lambda x: x["regression"]["parameter_rows"][p]["generator_moment_coefficients"][3].__setitem__("mu_coefficient", "0"))
    add("q_factor_formula", lambda x: x["regression"]["parameter_rows"][p]["q_product"].__setitem__("factor_formula", "Euler factor"))
    add("q_terms", lambda x: x["regression"]["parameter_rows"][p]["q_product"].__setitem__("terms", 1))
    add("q_coeff", lambda x: x["regression"]["parameter_rows"][p]["q_product"]["prefix_coefficients"].__setitem__(1, "0"))
    add("q_spot", lambda x: x["regression"]["parameter_rows"][p]["q_product_spot_values"][0].__setitem__("prefix_laplace", "1"))
    add("occupation_formula", lambda x: x["regression"]["parameter_rows"][p]["stationary_markov_renewal_occupation"].__setitem__("formula", "bad"))
    add("occupation_symbol", lambda x: x["regression"]["parameter_rows"][p]["stationary_markov_renewal_occupation"].__setitem__("mean_symbol", "iid regeneration"))
    add("iid_flag", lambda x: x["regression"]["parameter_rows"][p]["stationary_markov_renewal_occupation"].__setitem__("not_iid_regeneration_for_beta_positive", False))
    add("skeleton_hazard", lambda x: x["regression"]["parameter_rows"][p]["deterministic_hazard_skeleton"][0].__setitem__("jump_hazard_exponential", "0"))
    add("skeleton_reward", lambda x: x["regression"]["parameter_rows"][p]["deterministic_hazard_skeleton"][0]["reward_rows"][2].__setitem__("integral_times_a", "0"))
    add("skeleton_y", lambda x: x["regression"]["parameter_rows"][p]["deterministic_hazard_skeleton"][1].__setitem__("y_next", "0"))
    add("contraction", lambda x: x["regression"]["parameter_rows"][p].__setitem__("contraction_factor", "1"))
    add("row_count", lambda x: x["regression"].__setitem__("parameter_row_count", 0))
    add("beta_grid", lambda x: x["regression"]["beta_values"].append("1/7"))
    add("moment_max", lambda x: x["regression"].__setitem__("moment_max", 2))
    add("boundary", lambda x: x["regression"]["boundary_rows"][0].__setitem__("verdict", "NO_INVARIANT"))
    add("source_lock", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator_lock", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("fixed_epoch", lambda x: x.__setitem__("fixed_epoch", 1788048001))
    add("scope_literal", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    add("theorem_overclaim", lambda x: x["theorem"].__setitem__("occupation", "iid regenerative exact law for every beta"))
    add("identity", lambda x: x["exact_identities"][1].__setitem__("formula", "missing a"))
    add("citation", lambda x: x["citations"][0].__setitem__("doi", "0"))
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
    print(f"C246 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
