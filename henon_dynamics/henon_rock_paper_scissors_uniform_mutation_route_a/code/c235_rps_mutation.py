#!/usr/bin/env python3
"""Hostile mutation suite for the C235 evidence contract."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c235_rps_evidence.json"
CHECKER = ROOT / "code/c235_rps_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c235_checker", CHECKER)
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
        mutations.append((name, repair(x) if repaired else x))

    add("stale_period", lambda x: x["regression"]["conservative_rows"][0].__setitem__("period", "0"), repaired=False)
    add("repaired_period", lambda x: x["regression"]["conservative_rows"][0].__setitem__("period", "0"))
    add("repaired_root", lambda x: x["regression"]["conservative_rows"][1].__setitem__("x_minus", "0"))
    add("repaired_h", lambda x: x["regression"]["conservative_rows"][2].__setitem__("h", "1/29"))
    add("repaired_a", lambda x: x["regression"]["conservative_rows"][5].__setitem__("a", "99"))
    add("repaired_limit", lambda x: x["regression"]["center_limit_rows"][0].__setitem__("period_limit", "1"))
    add("repaired_mutation_state", lambda x: x["regression"]["mutation_rows"][0]["final_state"].__setitem__(0, "0"))
    add("repaired_mutation_dlog", lambda x: x["regression"]["mutation_rows"][1].__setitem__("dlog_h_exact", "0"))
    add("repaired_mutation_steps", lambda x: x["regression"]["mutation_rows"][2].__setitem__("steps", 1))
    add("repaired_mutation_positive", lambda x: x["regression"]["mutation_rows"][3].__setitem__("strictly_positive_after", False))
    add("repaired_contraction", lambda x: x["regression"]["contraction_rows"][0].__setitem__("distance_factor", "0"))
    add("repaired_linearization", lambda x: x["regression"]["linearization_rows"][0].__setitem__("imag_abs", "0"))
    add("repaired_conservative_count", lambda x: x["regression"].__setitem__("conservative_row_count", 14))
    add("repaired_mutation_count", lambda x: x["regression"].__setitem__("mutation_row_count", 7))
    add("repaired_source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("repaired_evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("repaired_scope", lambda x: x.__setitem__("scope_literal", "BAD_SCOPE"))
    add("repaired_route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("repaired_route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("repaired_scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("unknown_top_level", lambda x: x.__setitem__("unknown", 1))
    add("unknown_nested", lambda x: x["regression"]["conservative_rows"][0].__setitem__("unknown", 1))
    add("repaired_citation_count", lambda x: x["citations"].pop())
    add("repaired_nonclaim_count", lambda x: x["nonclaims"].pop())
    add("repaired_zero_rate_period_claim", lambda x: x["theorem"].__setitem__("conservative_integral", "When mu=0 every positive product level is periodic, including a=0."))

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
    print(f"C235 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
