#!/usr/bin/env python3
"""SymPy series, pole, branch-conjugation, and N=1 boundary checks for C205."""
import json
from pathlib import Path

import sympy as sp

PATH = Path(__file__).resolve().parents[1] / "results" / "c205_dyck_shift_evidence.json"


def main():
    data = json.loads(PATH.read_text()); z, s = sp.symbols("z s"); cells = entropy_cells = 0
    for rec in data["records"]:
        N = rec["N"]
        assert sp.simplify(-sp.log(sp.Rational(1, N + 1)) - sp.log(N + 1)) == 0
        assert rec["topological_entropy"] == f"log({N+1})"
        entropy_cells += 1
        root = sp.sqrt(1 - 4 * N * z**2)
        Z = 2 * (1 + root) / (1 + root - 2 * N * z)**2
        series = sp.series(z * sp.diff(sp.log(Z), z), z, 0, 13).removeO().expand()
        for n in range(1, 13):
            assert int(series.coeff(z, n)) == rec["fixed_points"][str(n)]
            cells += 1
        if N == 1:
            assert sp.simplify(Z - 1 / (1 - 2 * z)) == 0
        else:
            r = sp.Rational(1, N + 1); root_r = sp.Rational(N - 1, N + 1)
            h = 1 + s - 2 * N * z
            assert sp.simplify(h.subs({z: r, s: root_r})) == 0
            ds = -4 * N * z / s
            assert sp.simplify((ds - 2 * N).subs({z: r, s: root_r})) != 0
            assert 2 * (1 + root_r) != 0
            algebraic = 2 * (1 + s) / (1 + s - 2 * N * z)**2
            conjugate = algebraic.subs(s, -s)
            # Unequal under the quadratic conjugation, hence not rational in z.
            assert sp.rem(sp.together(algebraic - conjugate).as_numer_denom()[0], s**2 - (1 - 4*N*z**2), s) != 0
            assert (N + 1) ** 2 > 4 * N
    assert cells == 72 and entropy_cells == 6
    print("C205 SymPy cross-check: PASS (72 zeta-series coefficients)")
    print("N=1 cancellation; N>1 double poles, branch conjugation, dominance gaps: PASS")
    print("6 entropy/dominant-radius identities: PASS")


if __name__ == "__main__": main()
