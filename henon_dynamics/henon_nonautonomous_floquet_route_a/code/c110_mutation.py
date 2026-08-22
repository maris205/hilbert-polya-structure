#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C110 evidence ledger."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c110_nonautonomous_evidence.json"
CHECKER = PROJECT / "code/c110_nonautonomous_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    out = copy.deepcopy(value)
    cursor = out
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = replacement  # type: ignore[index]
    return out


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    spec = importlib.util.spec_from_file_location("c110_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.expected()
    row = original["primitive_orbit_ledger"]["rows"][3]
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad-schema"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "word": mutate(original, ["primitive_orbit_ledger", "rows", 3, "word"], "333"),
        "chronology_matrix": mutate(original, ["primitive_orbit_ledger", "rows", 3, "chronological_01_monodromy", 0, 0], row["chronological_01_monodromy"][0][0] + 1),
        "reverse_trace": mutate(original, ["primitive_orbit_ledger", "rows", 3, "reversed_10_trace"], row["reversed_10_trace"] + 1),
        "transfer_trace": mutate(original, ["transfer_atlas", "chronological_01", "trace_of_powers", "4"], original["transfer_atlas"]["chronological_01"]["trace_of_powers"]["4"] + 1),
        "reverse_determinant": mutate(original, ["transfer_atlas", "reversed_10", "determinant_I_minus_zA_coefficients_low_to_high", 3], original["transfer_atlas"]["reversed_10"]["determinant_I_minus_zA_coefficients_low_to_high"][3] + 1),
        "decomposition": mutate(original, ["transfer_atlas", "chronological_01", "primitive_trace_identity_contributions", "6", "3"], original["transfer_atlas"]["chronological_01"]["primitive_trace_identity_contributions"]["6"]["3"] + 1),
        "assessment": mutate(original, ["route_a_assessment", "A2"], "A2_ANALYTIC_DETERMINANT"),
        "claim": mutate(original, ["claims", "fredholm_determinant"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c110-mutations-") as directory:
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
    print(json.dumps({"status": "C110_MUTATION_PASS", "rejected": rejected, "total": len(mutations)}, sort_keys=True))


if __name__ == "__main__":
    main()
