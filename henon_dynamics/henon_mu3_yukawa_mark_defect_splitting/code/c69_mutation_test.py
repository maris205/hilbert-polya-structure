#!/usr/bin/env python3
"""Hostile semantic mutations for the C69 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c69_defect_splitting_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c69_defect_splitting_checker.py"


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
        "source": mutate(original, ["authority", "c68"], "0" * 64),
        "type_order": mutate(original, ["type_order", 0], "S16"),
        "modulus": mutate(original, ["moduli", 0], 4),
        "formula": mutate(original, ["retraction_formula", 0], "x9 mod 8"),
        "retraction": mutate(original, ["retraction_matrix", 0, 9], 0),
        "retraction_hash": mutate(original, ["retraction_matrix_sha256"], "1" * 64),
        "RM": mutate(original, ["RM_residues", 0, 0], 1),
        "RU": mutate(original, ["RU_residues", 1, 1], 0),
        "basis": mutate(original, ["complement_basis", 14, 0], 0),
        "basis_hash": mutate(original, ["complement_basis_sha256"], "2" * 64),
        "index": mutate(original, ["complement_lattice_index"], 16),
        "presentation": mutate(original, ["complement_presentation", 0, 0], 2),
        "presentation_hash": mutate(original, ["complement_presentation_sha256"], "3" * 64),
        "snf": mutate(original, ["complement_smith_invariants", -1], 72),
        "order": mutate(original, ["complement_order"], 32),
        "ambient": mutate(original, ["ambient_order"], 7077888),
        "hom_count": mutate(original, ["hom_exponents_by_target", 0], 16),
        "row_count": mutate(original, ["retraction_row_solution_counts", 0], 65536),
        "retraction_count": mutate(original, ["retraction_count"], 2 ** 40),
        "complement_count": mutate(original, ["complement_count"], 2 ** 40),
        "claims": mutate(original, ["claims", "complement_canonical_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c69-mutations-") as tmp:
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
