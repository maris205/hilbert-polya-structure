#!/usr/bin/env python3
"""Independent SymPy cross-check for the C68 quotient Smith forms."""

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
EVIDENCE = PROJECT / "results/c68_defect_duality_evidence.json"


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
    assert M * sp.Matrix.hstack(*[sp.Matrix(c65["kernel_basis"][f"z{i}"])
                                  for i in (1, 2, 3)]) == U * sp.diag(8, 2, 2)
    assert diagonal(M.row_join(U)) == ev["quotient_smith_invariants"]
    P = sp.Matrix(ev["row_lattice_basis"])
    assert abs(int(P.det())) == 32
    dual = P.inv() * M.T
    assert all(x.q == 1 for x in dual)
    assert diagonal(dual.applyfunc(int)) == ev["row_dual_map_smith_invariants"]
    print(json.dumps({"status": "SNF_CROSSCHECK_PASS",
                      "quotient_smith_invariants": diagonal(M.row_join(U)),
                      "dual_smith_invariants": diagonal(dual.applyfunc(int)),
                      "row_lattice_index": abs(int(P.det()))}, sort_keys=True))


if __name__ == "__main__":
    main()
