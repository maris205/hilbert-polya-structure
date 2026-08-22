#!/usr/bin/env python3
"""Hostile mutation audit for the C111 evidence ledger."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c111_three_site_evidence.json"
CHECKER = PROJECT / "code/c111_three_site_checker.py"


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
    original_raw = EVIDENCE.read_bytes()
    original = json.loads(original_raw)
    spec = importlib.util.spec_from_file_location("c111_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "parameter": mutate(original, ["model", "parameters", "kappa", "numerator"], 2),
        "laplacian": mutate(original, ["model", "laplacian", 0, 0, "numerator"], 9),
        "fixed_state": mutate(original, ["certified_orbit_ledger", "fixed_rows", 1, "states", 0, 0, "numerator"], 9),
        "period_state": mutate(original, ["certified_orbit_ledger", "period_two_rows", 0, "states", 0, 0, "numerator"], 8),
        "monodromy": mutate(original, ["certified_orbit_ledger", "period_two_rows", 0, "monodromy_trace", "numerator"], -386),
        "mode_trace": mutate(original, ["fourier_mode_witness", "period_two_mode_traces", 1, "numerator"], -105),
        "polynomial": mutate(original, ["controls", "coupled_det_I_minus_z", 2, "numerator"], 50212),
        "symplectic_check": mutate(original, ["checks", "symplectic_form_on_fixed_and_cycle_points"], False),
        "route_verdict": mutate(original, ["route_a_verdict", "A2"], "A2_CERTIFIED"),
        "forbidden_claim": mutate(original, ["claims", "euler_factors_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c111-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes(canonical(value))
            try:
                checker.validate_evidence_path(path)
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert EVIDENCE.read_bytes() == original_raw
    assert rejected == len(mutations)
    print(json.dumps({"status": "C111_MUTATION_TEST_PASS", "rejected": rejected, "total": len(mutations)}, sort_keys=True))


if __name__ == "__main__":
    main()
