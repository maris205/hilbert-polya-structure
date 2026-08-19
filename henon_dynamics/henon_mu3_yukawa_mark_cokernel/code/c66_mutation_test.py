#!/usr/bin/env python3
"""Hostile semantic mutations for the C66 evidence checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c66_mark_snf_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c66_mark_snf_checker.py"


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
        "matrix_hash": mutate(original, ["authority", "c64_matrix_sha256"], "1" * 64),
        "shape": mutate(original, ["mark_shape", 0], 15),
        "rank": mutate(original, ["mark_rank"], 15),
        "determinant": mutate(original, ["mark_determinant"], 1),
        "snf": mutate(original, ["smith_invariants", 1], 4),
        "primary": mutate(original, ["primary_invariants", "2", 0], 4),
        "claim_scope": mutate(original, ["claims", "full_burnside_ring_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c66-mutations-") as tmp:
        for name, doc in mutations.items():
            path = Path(tmp) / f"{name}.json"
            path.write_bytes((json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)], cwd=PROJECT,
                                 capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
