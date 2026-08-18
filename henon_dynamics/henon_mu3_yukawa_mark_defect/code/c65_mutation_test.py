#!/usr/bin/env python3
"""Hostile semantic mutations for the C65 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c65_defect_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c65_defect_checker.py"


def mutate(source: dict, path: list[object], value: object) -> dict:
    out = deepcopy(source)
    node = out
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return out


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "source": mutate(original, ["authority", "c64"], "0" * 64),
        "kernel": mutate(original, ["kernel_basis_minor_gcd"], 2),
        "old_snf": mutate(original, ["old_snf", 1], 4),
        "all_snf": mutate(original, ["all_snf", 2], 4),
        "old_index": mutate(original, ["relative_jump", "old_index"], 32),
        "all_index": mutate(original, ["relative_jump", "all_index"], 16),
        "generator": mutate(original, ["relative_jump", "generator"], "m(R4)"),
        "claim_scope": mutate(original, ["claims", "full_burnside_ring_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c65-mutations-") as tmp:
        for name, doc in mutations.items():
            path = Path(tmp) / f"{name}.json"
            path.write_bytes((json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)], cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status":"PASS", "mutations_rejected":len(rejected), "names":sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
