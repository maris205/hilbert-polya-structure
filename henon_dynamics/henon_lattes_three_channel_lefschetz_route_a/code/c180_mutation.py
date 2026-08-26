#!/usr/bin/env python3
"""Repaired-hash semantic mutation suite for the C180 checker."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c180_lattes_evidence.json"
CHECKER_PATH = ROOT / "code/c180_lattes_checker.py"


spec = importlib.util.spec_from_file_location("c180_checker", CHECKER_PATH)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def repaired(payload: dict) -> dict:
    payload["payload_sha256"] = checker.canonical_hash(payload)
    return payload


def rejected(payload: dict) -> bool:
    try:
        checker.validate(payload)
    except (AssertionError, KeyError, TypeError, ValueError):
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
    add("route_a0", lambda x: x["route_a_verdict"].__setitem__("A0", "A0_PASS"))
    add("route_b", lambda x: x["route_a_verdict"].__setitem__("route_b_invocation_allowed", True))
    add("all_tau", lambda x: x["source_lock"].__setitem__("family", "one elliptic curve only"))
    add("arithmetic_origin", lambda x: x["source_lock"].__setitem__("arithmetic_origin", "prime labels inserted"))
    add("formula_a", lambda x: x["formula_rows"][0].__setitem__("a", 3))
    add("plus_count", lambda x: x["formula_rows"][1].__setitem__("plus_regular_count", 99))
    add("minus_multiplier", lambda x: x["formula_rows"][2].__setitem__("minus_multiplier", 0))
    add("branch_count", lambda x: x["formula_rows"][12].__setitem__("branch_count", 1))
    add("lefschetz", lambda x: x["formula_rows"][3].__setitem__("lefschetz_sum", "0/1"))
    add("period", lambda x: x["formula_rows"][20].__setitem__("exact_period_points", 1))
    add("cycle", lambda x: x["formula_rows"][21].__setitem__("primitive_cycles", 1))
    add("torsion_intersection", lambda x: x["torsion_enumeration_rows"][0].__setitem__("intersection_size", 2))
    add("torsion_digest", lambda x: x["torsion_enumeration_rows"][1].__setitem__("class_digest", "0" * 64))
    add("torsion_union", lambda x: x["torsion_enumeration_rows"][2].__setitem__("union_quotient_classes", 0))
    add("wold_k", lambda x: x["wold_rows"][0].__setitem__("k", [0, 0]))
    add("wold_root", lambda x: x["wold_rows"][100].__setitem__("root", [0, 0]))
    add("wold_depth", lambda x: x["wold_rows"][500].__setitem__("depth", 99))
    add("wold_shift", lambda x: x["wold_rows"][1000].__setitem__("shifted_k", [1, 1]))
    add("count", lambda x: x["counts"].__setitem__("wold_mode_rows", 1))
    add("zeta", lambda x: x["theorem"].__setitem__("artin_mazur_zeta", "1"))
    add("wold_theorem", lambda x: x["theorem"].__setitem__("wold", "unitary"))

    failed = [name for name, item in mutations if not rejected(item)]
    assert not failed, f"repaired-hash mutations escaped: {failed}"

    stale = copy.deepcopy(base)
    stale["formula_rows"][0]["fixed_point_total"] += 1
    assert rejected(stale), "stale-hash mutation escaped"
    print(json.dumps({"status": "C180_MUTATION_PASS", "repaired_hash_rejections": len(mutations), "stale_hash_rejections": 1}, sort_keys=True))


if __name__ == "__main__":
    main()
