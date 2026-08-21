#!/usr/bin/env python3
"""Hostile semantic mutation audit for C82."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c82_bitflip_noise_fourier_evidence.json"
CHECKER = PROJECT / "code/c82_bitflip_noise_fourier_checker.py"


def mutate(value, path, replacement):
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return result


def main():
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c73_hash": mutate(original, ["authority", "c73"], "0" * 64),
        "c78_manifest": mutate(original, ["authority", "c78_manifest"], "1" * 64),
        "pivot": mutate(original, ["predicate", "pivot"], "S1"),
        "one_count": mutate(original, ["predicate", "one_count"], 30401),
        "spectrum_count": mutate(original, ["walsh_transform", "nonzero_coefficient_count"], 1023),
        "degree": mutate(original, ["walsh_transform", "maximum_fourier_degree"], 11),
        "energy": mutate(original, ["walsh_transform", "energy_by_degree", "0"], 0),
        "noise": mutate(original, ["bitflip_noise", "autocorrelation_by_distance", "1"], 0),
        "parseval": mutate(original, ["bitflip_noise", "parseval_total"], 1),
        "claim": mutate(original, ["claims", "exact_integer_walsh_spectrum"], False),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c82-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes((json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            if run.returncode != 0:
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C82_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
