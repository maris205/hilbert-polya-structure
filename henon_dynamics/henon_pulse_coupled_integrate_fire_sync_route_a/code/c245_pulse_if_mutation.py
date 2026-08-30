#!/usr/bin/env python3
"""Hostile mutation suite for the C245 receipt."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c245_pulse_if_evidence.json"
CHECKER = ROOT / "code/c245_pulse_if_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c245_checker", CHECKER)
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

    row = 1  # non-synchronous row with a nontrivial history
    hist = 0
    add("stale_hash", lambda x: x["regression"]["event_rows"][row]["event_word"].append(99), repaired=False)
    add("r_value", lambda x: x["regression"]["event_rows"][row].__setitem__("r", "1/3"))
    add("epsilon", lambda x: x["regression"]["event_rows"][row].__setitem__("epsilon", "2/5"))
    add("n_value", lambda x: x["regression"]["event_rows"][row].__setitem__("n", 99))
    add("seed_value", lambda x: x["regression"]["event_rows"][row].__setitem__("seed", 99))
    add("initial_state", lambda x: x["regression"]["event_rows"][row]["initial_state"].__setitem__(0, "1"))
    add("initial_clusters", lambda x: x["regression"]["event_rows"][row]["initial_clusters"].append([99]))
    add("event_word", lambda x: x["regression"]["event_rows"][row]["event_word"].__setitem__(0, 99))
    add("history_pre", lambda x: x["regression"]["event_rows"][row]["history"][hist]["pre_state"].__setitem__(0, "1"))
    add("history_scaled", lambda x: x["regression"]["event_rows"][row]["history"][hist]["scaled_state"].__setitem__(0, "1"))
    add("history_scale", lambda x: x["regression"]["event_rows"][row]["history"][hist].__setitem__("scale", "1"))
    add("firing_indices", lambda x: x["regression"]["event_rows"][row]["history"][hist]["firing_indices"].append(99))
    add("avalanche_generation", lambda x: x["regression"]["event_rows"][row]["history"][hist]["avalanche_generations"].append([99]))
    add("history_post", lambda x: x["regression"]["event_rows"][row]["history"][hist]["post_state"].__setitem__(1, "1"))
    add("clusters_before", lambda x: x["regression"]["event_rows"][row]["history"][hist]["clusters_before"].append([99]))
    add("clusters_after", lambda x: x["regression"]["event_rows"][row]["history"][hist]["clusters_after"].append([99]))
    add("cluster_count_before", lambda x: x["regression"]["event_rows"][row]["history"][hist].__setitem__("cluster_count_before", 99))
    add("cluster_count_after", lambda x: x["regression"]["event_rows"][row]["history"][hist].__setitem__("cluster_count_after", 99))
    add("coarsens_flag", lambda x: x["regression"]["event_rows"][row]["history"][hist].__setitem__("coarsens_or_equal", False))
    add("events_recorded", lambda x: x["regression"]["event_rows"][row].__setitem__("events_recorded", 99))
    add("cycle_period", lambda x: x["regression"]["event_rows"][row].__setitem__("cycle_period", 99))
    add("sync_flag", lambda x: x["regression"]["sync_rows"][0].__setitem__("synchronous_absorbing", False))
    add("primitive_flag", lambda x: x["regression"]["sync_rows"][0].__setitem__("primitive_event_cycle", False))
    add("partition_flag", lambda x: x["regression"]["event_rows"][row].__setitem__("partition_nonincreasing", False))
    add("final_state", lambda x: x["regression"]["event_rows"][row]["final_state"].__setitem__(0, "0"))
    add("event_count", lambda x: x["regression"].__setitem__("event_row_count", 0))
    add("sync_count", lambda x: x["regression"].__setitem__("sync_row_count", 0))
    add("coarse_count", lambda x: x["regression"].__setitem__("coarsening_row_count", 0))
    add("parameter_grid", lambda x: x["regression"]["r_values"].append("1/7"))
    add("source_lock", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator_lock", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("fixed_epoch", lambda x: x.__setitem__("fixed_epoch", 1788048001))
    add("scope_literal", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_FAIL"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    add("theorem_overclaim", lambda x: x["theorem"].__setitem__("literature_scope", "complete global synchrony census"))
    add("identity", lambda x: x["exact_identities"][0].__setitem__("formula", "bad"))
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
    print(f"C245 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
