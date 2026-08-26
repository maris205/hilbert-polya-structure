#!/usr/bin/env python3
"""Repaired-hash semantic mutation suite for the C181 checker."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "code/c181_rotor_router_checker.py"
EVIDENCE = ROOT / "results/c181_rotor_router_evidence.json"
spec = importlib.util.spec_from_file_location("c181_checker", CHECKER_PATH)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def repaired(payload: dict) -> dict:
    payload["payload_sha256"] = checker.canonical_hash(payload)
    return payload


def rejected(payload: dict) -> bool:
    try:
        checker.validate(payload)
    except (AssertionError, KeyError, TypeError, ValueError, IndexError):
        return True
    return False


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name, fn):
        item = copy.deepcopy(base)
        fn(item)
        mutations.append((name, repaired(item)))

    add("scope", lambda x: x.__setitem__("scope_literal", "BROKEN"))
    add("source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("family", lambda x: x["source_lock"].__setitem__("family", "one graph"))
    add("arithmetic_origin", lambda x: x["source_lock"].__setitem__("arithmetic_origin", "prime labels inserted"))
    add("sandpile", lambda x: x["source_lock"].__setitem__("forbidden_recast", "sandpile translation"))
    add("route_a0", lambda x: x["route_a_verdict"].__setitem__("A0", "A0_PASS"))
    add("route_a4", lambda x: x["route_a_verdict"].__setitem__("A4", "A4_FAIL"))
    add("route_b", lambda x: x["route_a_verdict"].__setitem__("route_b_invocation_allowed", True))
    add("graph_id", lambda x: x["graph_rows"][0].__setitem__("graph_id", "broken"))
    add("arc", lambda x: x["graph_rows"][20]["arcs"][0].__setitem__(1, 0))
    add("tree", lambda x: x["graph_rows"][100].__setitem__("arborescence_t", [1, 1, 1, 1]))
    add("M", lambda x: x["graph_rows"][200].__setitem__("M_gcd", 999))
    add("L", lambda x: x["graph_rows"][300].__setitem__("common_orbit_length_L", 999))
    add("state_count", lambda x: x["graph_rows"][400].__setitem__("unicycle_state_count", 0))
    add("eulerian", lambda x: x["graph_rows"][500].__setitem__("eulerian", not x["graph_rows"][500]["eulerian"]))
    add("order_index", lambda x: x["cyclic_order_rows"][0].__setitem__("order_index", 9))
    add("order", lambda x: x["cyclic_order_rows"][10]["cyclic_orders"][0].reverse())
    add("order_digest", lambda x: x["cyclic_order_rows"][20].__setitem__("cyclic_order_digest", "0" * 64))
    add("orbit_count", lambda x: x["cyclic_order_rows"][30].__setitem__("orbit_count", 0))
    add("visit", lambda x: x["cyclic_order_rows"][40]["vertex_visits_per_orbit"].__setitem__(0, 0))
    add("edge_use", lambda x: x["cyclic_order_rows"][50]["arc_traversals_per_orbit"].__setitem__(0, 0))
    add("orbit_digest", lambda x: x["cyclic_order_rows"][60].__setitem__("orbit_digest", "f" * 64))
    add("census", lambda x: x["counts"]["simple_strong_graphs_by_n"].__setitem__("4", 1))
    add("zeta", lambda x: x["theorem"].__setitem__("zeta", "1"))
    add("eulerian_theorem", lambda x: x["theorem"].__setitem__("eulerian", "false"))

    escaped = [name for name, item in mutations if not rejected(item)]
    assert not escaped, f"repaired-hash mutations escaped: {escaped}"
    stale = copy.deepcopy(base)
    stale["counts"]["graph_rows_total"] = 0
    assert rejected(stale), "stale-hash mutation escaped"
    print(json.dumps({"status": "C181_MUTATION_PASS", "repaired_hash_rejections": len(mutations), "stale_hash_rejections": 1}, sort_keys=True))


if __name__ == "__main__":
    main()
