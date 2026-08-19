#!/usr/bin/env python3
"""SymPy cross-check for the C69 retraction and complement."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
C65 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/results/c65_defect_evidence.json"
EVIDENCE = PROJECT / "results/c69_defect_splitting_evidence.json"


def diagonal(matrix: sp.Matrix) -> list[int]:
    d = smith_normal_form(matrix, domain=ZZ)
    return [abs(int(d[i, i])) for i in range(min(d.rows, d.cols))]


def main() -> None:
    c64 = json.loads(C64.read_text())
    c65 = json.loads(C65.read_text())
    ev = json.loads(EVIDENCE.read_text())
    M = sp.Matrix(c64["mark_matrix"])
    U = sp.Matrix.hstack(*[sp.Matrix(c65["all_saturation_basis"][f"u{i}"])
                           for i in (1, 2, 3)])
    R = sp.Matrix(ev["retraction_matrix"])
    B = sp.Matrix(ev["complement_basis"])
    moduli = ev["moduli"]
    assert all(int((R * M)[i, j]) % moduli[i] == 0
               for i in range(3) for j in range(16))
    assert [[int((R * U)[i, j]) % moduli[i] for j in range(3)] for i in range(3)] == sp.eye(3).tolist()
    assert abs(int(B.det())) == 32
    N = B.inv() * M
    assert all(x.q == 1 for x in N)
    N = N.applyfunc(int)
    assert B * N == M
    assert diagonal(N) == ev["complement_smith_invariants"]
    print(json.dumps({"status": "SNF_CROSSCHECK_PASS",
                      "retraction": "VERIFIED",
                      "complement_lattice_index": abs(int(B.det())),
                      "complement_smith_invariants": diagonal(N)}, sort_keys=True))


if __name__ == "__main__":
    main()
