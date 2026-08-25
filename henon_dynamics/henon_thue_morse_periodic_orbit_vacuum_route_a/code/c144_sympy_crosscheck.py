#!/usr/bin/env python3
"""SymPy cross-check of C144 substitution polynomials and vacuum zeta."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c144_thue_morse_evidence.json"


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    data = json.loads(path.read_text())
    z = sp.symbols("z")
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    matrix = sp.Matrix([[1, 1], [1, 1]])
    ck(matrix.charpoly().as_expr() == sp.Symbol("lambda") ** 2 - 2 * sp.Symbol("lambda"), "substitution charpoly")
    for k in range(1, 9):
        polynomial = sp.prod(1 - z ** (1 << j) for j in range(k)).expand()
        expected = sum((-1) ** (n.bit_count() & 1) * z ** n for n in range(1 << k))
        ck(sp.expand(polynomial - expected) == 0, f"Riesz product identity k={k}")
        ck([int(polynomial.coeff(z, n)) for n in range(1 << k)].count(1) == 1 << (k - 1), f"positive coefficients k={k}")
    formal_log = sum(sp.Integer(row["fixed_points"]) * z ** row["period"] / row["period"] for row in data["periodic_orbit_vacuum"]["periodic_point_counts"])
    ck(formal_log == 0, "zero formal logarithm")
    series = sp.exp(formal_log).series(z, 0, 33).removeO()
    for degree, coefficient in enumerate(data["periodic_orbit_vacuum"]["zeta_coefficients_through_degree_32"]):
        ck(series.coeff(z, degree) == coefficient, f"zeta coefficient {degree}")
    for receipt in data["aperiodicity_theorem"]["period_certificates"]:
        p = receipt["putative_period"]
        k = receipt["odd_exponent_k"]
        d = sp.Integer(p) * (2 ** k - 1)
        ck(int(d) == receipt["multiple_d"], f"symbolic multiple p={p}")
    print(json.dumps({"status": "C144_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
