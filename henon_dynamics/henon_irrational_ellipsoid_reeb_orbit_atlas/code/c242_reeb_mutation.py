#!/usr/bin/env python3
"""Hostile repaired-hash mutations for the C242 evidence contract."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c242_reeb_evidence.json"
CHECKER = ROOT / "code/c242_reeb_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c242_checker", CHECKER)
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

    # Every edit below repairs the outer digest, so acceptance cannot be
    # defeated by merely changing the hash.
    add("stale_hash", lambda x: x["regression"]["irrational_cases"][0]["rows"][0].__setitem__("cz_index", 999), False)
    add("cz_index", lambda x: x["regression"]["irrational_cases"][0]["rows"][1].__setitem__("cz_index", 3))
    add("floor_m", lambda x: x["regression"]["irrational_cases"][0]["rows"][2]["floor_certificate"].__setitem__("integer", 0))
    add("floor_left", lambda x: x["regression"]["irrational_cases"][0]["rows"][3]["floor_certificate"].__setitem__("left", 0))
    add("floor_right", lambda x: x["regression"]["irrational_cases"][0]["rows"][4]["floor_certificate"].__setitem__("right", 0))
    add("multiplier_real", lambda x: x["regression"]["irrational_cases"][0]["rows"][5].__setitem__("multiplier_real", "0"))
    add("multiplier_imag", lambda x: x["regression"]["irrational_cases"][0]["rows"][6].__setitem__("multiplier_imaginary", "0"))
    add("axis", lambda x: x["regression"]["irrational_cases"][0]["rows"][7].__setitem__("axis", "gamma2"))
    add("iterate", lambda x: x["regression"]["irrational_cases"][0]["rows"][8].__setitem__("iterate", 99))
    add("action", lambda x: x["regression"]["irrational_cases"][0]["rows"][9].__setitem__("action", "wrong"))
    add("period", lambda x: x["regression"]["irrational_cases"][0]["rows"][10].__setitem__("period", "wrong"))
    add("ratio", lambda x: x["regression"]["irrational_cases"][0]["rows"][11].__setitem__("ratio", "1"))
    add("nondegenerate", lambda x: x["regression"]["irrational_cases"][0]["rows"][12].__setitem__("nondegenerate", False))
    add("rational_case_count", lambda x: x["regression"].__setitem__("rational_case_count", 2))
    add("rational_ratio", lambda x: x["regression"]["rational_cases"][0].__setitem__("ratio", "1"))
    add("rational_common_period", lambda x: x["regression"]["rational_cases"][1].__setitem__("common_period", "0"))
    add("rational_dimension", lambda x: x["regression"]["rational_cases"][2].__setitem__("morse_bott_manifold", "two circles"))
    add("rational_resonance", lambda x: x["regression"]["rational_cases"][0]["resonance_certificate"].__setitem__("q*a", 0))
    add("rational_cz", lambda x: x["regression"]["rational_cases"][1]["coordinate_orbits"][0].__setitem__("cz_index", 1))
    add("rational_status", lambda x: x["regression"]["rational_cases"][1]["coordinate_orbits"][1].__setitem__("cz_status", "defined"))
    add("source_lock", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator_lock", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("scope_literal", lambda x: x.__setitem__("scope_literal", "BAD"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_FAIL"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("unknown_top", lambda x: x.__setitem__("unknown", 1))
    add("rational_regime", lambda x: x["regression"]["rational_cases"][2].__setitem__("regime", "irrational"))
    add("identity_count", lambda x: x["exact_identities"].pop())

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
    print(f"C242 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
