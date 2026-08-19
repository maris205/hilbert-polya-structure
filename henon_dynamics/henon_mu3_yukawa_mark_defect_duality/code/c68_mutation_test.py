#!/usr/bin/env python3
"""Hostile semantic mutations for the C68 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c68_defect_duality_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c68_defect_duality_checker.py"


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
        "source": mutate(original, ["authority", "c65"], "0" * 64),
        "type_order": mutate(original, ["type_order", 0], "S16"),
        "relations": mutate(original, ["relations", "d", 0], 4),
        "basis": mutate(original, ["saturation_basis", "u2", 1], 99),
        "basis_hash": mutate(original, ["saturation_basis_sha256"], "1" * 64),
        "D": mutate(original, ["D_invariants", 0], 4),
        "quotient": mutate(original, ["quotient_smith_invariants", -1], 12),
        "quotient_order": mutate(original, ["quotient_order"], 32),
        "augmented_hash": mutate(original, ["augmented_matrix_sha256"], "2" * 64),
        "row_basis": mutate(original, ["row_lattice_basis", 0, 0], 2),
        "row_index": mutate(original, ["row_lattice_basis_determinant"], 16),
        "dual": mutate(original, ["row_dual_map_smith_invariants", -1], 12),
        "residue": mutate(original, ["residue_table", 1, 1], 0),
        "annihilator": mutate(original, ["annihilator_coordinate_types", 0], 2),
        "claims": mutate(original, ["claims", "canonical_smith_basis_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c68-mutations-") as tmp:
        for name, doc in mutations.items():
            path = Path(tmp) / f"{name}.json"
            path.write_bytes((json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
