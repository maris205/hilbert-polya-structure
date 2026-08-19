#!/usr/bin/env python3
"""Independent library Smith-form cross-check for the C66 mark matrix."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c66_mark_snf_evidence.json"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    c64 = json.loads(C64.read_text())
    matrix = sp.Matrix(c64["mark_matrix"])
    diagonal = smith_normal_form(matrix, domain=ZZ)
    values = [abs(int(diagonal[i, i])) for i in range(16)]
    assert values == evidence["smith_invariants"]
    assert abs(int(matrix.det())) == evidence["mark_determinant"]
    primary_2 = []
    primary_3 = []
    for value in values:
        x = value
        p2 = 1
        p3 = 1
        while x % 2 == 0 and x > 1:
            x //= 2
            p2 *= 2
        while x % 3 == 0 and x > 1:
            x //= 3
            p3 *= 3
        if p2 > 1:
            primary_2.append(p2)
        if p3 > 1:
            primary_3.append(p3)
        assert x == 1
    assert primary_2 == evidence["primary_invariants"]["2"]
    assert primary_3 == evidence["primary_invariants"]["3"]
    print(json.dumps({"status": "SNF_CROSSCHECK_PASS", "smith_invariants": values,
                      "determinant": int(matrix.det()), "primary_2": primary_2,
                      "primary_3": primary_3}, sort_keys=True))


if __name__ == "__main__":
    main()
