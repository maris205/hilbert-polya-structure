#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C104 evidence ledger."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c104_multibranch_evidence.json"
CHECKER = PROJECT / "code/c104_multibranch_checker.py"


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
    spec = importlib.util.spec_from_file_location("c104_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    row = original["primitive_orbit_ledger"]["rows"][17]
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "word": mutate(original, ["primitive_orbit_ledger", "rows", 17, "word"], "0000"),
        "matrix": mutate(original, ["primitive_orbit_ledger", "rows", 17, "representative_monodromy", 0, 0], row["representative_monodromy"][0][0] + 1),
        "trace": mutate(original, ["transfer_atlas", "trace_of_powers", "4"], original["transfer_atlas"]["trace_of_powers"]["4"] + 1),
        "decomposition": mutate(original, ["transfer_atlas", "primitive_trace_identity_contributions", "6", "3"], original["transfer_atlas"]["primitive_trace_identity_contributions"]["6"]["3"] + 1),
        "determinant": mutate(original, ["transfer_atlas", "determinant_I_minus_zA_coefficients_low_to_high", 2], original["transfer_atlas"]["determinant_I_minus_zA_coefficients_low_to_high"][2] + 1),
        "assessment": mutate(original, ["route_a_assessment", "A2"], "CERTIFIED_FREDHOLM"),
        "claim": mutate(original, ["claims", "fredholm_determinant"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c104-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes(canonical(value))
            try:
                checker.validate_evidence_path(path, expected)
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C104_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
