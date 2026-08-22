#!/usr/bin/env python3
"""Hostile mutation audit: semantic edits must be rejected independently."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c106_variational_lattice_evidence.json"
CHECKER = PROJECT / "code/c106_variational_lattice_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = replacement  # type: ignore[index]
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    spec = importlib.util.spec_from_file_location("c106_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "parameter": mutate(original, ["model", "parameters", "kappa", "numerator"], 3),
        "fixed_state": mutate(original, ["certified_orbit_ledger", "fixed_rows", 1, "states", 0, 0, "numerator"], 9),
        "jacobian": mutate(original, ["certified_orbit_ledger", "period_two_rows", 0, "jacobian_at_first", 0, 0, "numerator"], 99),
        "monodromy": mutate(original, ["certified_orbit_ledger", "period_two_rows", 0, "monodromy_trace", "numerator"], -46),
        "polynomial": mutate(original, ["controls", "coupled_det_I_minus_z", 2, "numerator"], 140),
        "symplectic_check": mutate(original, ["checks", "symplectic_form_on_fixed_and_cycle_points"], False),
        "delta": mutate(original, ["controls", "trace_difference_coupled_minus_uncoupled", "numerator"], 8),
        "route_verdict": mutate(original, ["route_a_verdict", "A2"], "A2_CERTIFIED"),
        "forbidden_claim": mutate(original, ["claims", "euler_factors_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c106-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes(canonical(value))
            try:
                checker.validate_evidence_path(path)
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C106_MUTATION_TEST_PASS", "rejected": rejected, "total": len(mutations)}, sort_keys=True))


if __name__ == "__main__":
    main()
