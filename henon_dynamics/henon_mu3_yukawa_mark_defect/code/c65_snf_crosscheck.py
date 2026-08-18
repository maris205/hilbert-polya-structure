#!/usr/bin/env python3
"""Independent library cross-check of the two small Smith forms."""

from __future__ import annotations

import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/results/c65_defect_evidence.json"
C63 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/results/c63_kernel_evidence.json"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"


def main() -> None:
    e = json.loads(EVIDENCE.read_text())
    c63 = json.loads(C63.read_text())
    c64 = json.loads(C64.read_text())
    M = sp.Matrix(c64["mark_matrix"])
    b = c63["nullspace_basis"]
    z = [sp.Matrix(b[k]) for k in ("z1", "z2", "z3")]
    V = sp.Matrix.hstack(*(M * x for x in z))
    old = V[:, [0, 2]]
    def diag(A):
        S = smith_normal_form(A, domain=ZZ)
        return [abs(int(S[i, i])) for i in range(min(S.rows, S.cols)) if S[i, i]]
    assert diag(old) == e["old_snf"] == [2, 8]
    assert diag(V) == e["all_snf"] == [2, 2, 8]
    print(json.dumps({"status":"SNF_CROSSCHECK_PASS", "old_snf":[2,8], "all_snf":[2,2,8]}, sort_keys=True))


if __name__ == "__main__":
    main()
