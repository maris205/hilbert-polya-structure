#!/usr/bin/env python3
"""Hostile semantic mutations for the C67 coordinate-profile checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c67_coordinate_profile_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c67_coordinate_profile_checker.py"


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
        "coordinate": mutate(original, ["coordinate_orders", 0], 1),
        "dual": mutate(original, ["dual_coordinate_orders", 1], 1),
        "denominator": mutate(original, ["global_inverse_denominator"], 36),
        "dual_denominator": mutate(original, ["dual_global_inverse_denominator"], 36),
        "nonzero": mutate(original, ["inverse_nonzero_count"], 42),
        "claim_scope": mutate(original, ["claims", "canonical_smith_basis_claimed"], True),
        "type_order": mutate(original, ["type_order", 0], "S16"),
        "c66_cokernel": mutate(original, ["c66_compatibility", "cokernel"], "tampered"),
    }
    rejected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c67-mutations-") as tmp:
        for name, doc in mutations.items():
            path = Path(tmp) / f"{name}.json"
            path.write_bytes(
                (json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n").encode()
            )
            run = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
            )
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
