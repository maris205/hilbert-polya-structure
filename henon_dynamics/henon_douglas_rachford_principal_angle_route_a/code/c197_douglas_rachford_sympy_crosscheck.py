#!/usr/bin/env python3
"""Separate SymPy reconstruction of the C197 block theorem and evidence."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c197_douglas_rachford_evidence.json"


def q(value: str):
    return sp.Rational(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if condition is not True and condition != sp.S.true:
            raise AssertionError(message)

    lam, c, s, z = sp.symbols("lambda c s z", real=True)
    identity = sp.eye(2)
    p_u = sp.diag(1, 0)
    p_v = sp.Matrix([[c**2, c*s], [c*s, s**2]])
    r_u = 2*p_u - identity
    r_v = 2*p_v - identity
    t_lam = (1-lam)*identity + lam*(identity + r_v*r_u)/2
    expected = sp.Matrix([[1-lam*s**2, -lam*s*c], [lam*s*c, 1-lam*s**2]])
    for entry in (t_lam - expected):
        check(sp.rem(sp.Poly(sp.expand(entry), c), sp.Poly(c**2+s**2-1, c)) == 0, "symbolic block")
    determinant = sp.expand(expected.det())
    target_det = 1-lam*(2-lam)*s**2
    check(sp.rem(sp.Poly(determinant-target_det, c), sp.Poly(c**2+s**2-1, c)) == 0, "symbolic modulus")
    char = sp.expand((sp.eye(2)-z*expected).det())
    target_char = sp.expand(1-2*z*(1-lam*s**2)+z**2*target_det)
    check(sp.rem(sp.Poly(char-target_char, c), sp.Poly(c**2+s**2-1, c)) == 0, "symbolic determinant factor")

    angles = {row["label"]: (q(row["cosine"]), q(row["sine"]))
              for row in data["regression"]["angles"]}
    for row in data["regression"]["block_rows"]:
        cv, sv = angles[row["angle_label"]]
        lv = q(row["lambda"])
        matrix = expected.subs({c: cv, s: sv, lam: lv})
        reported = sp.Matrix([[q(x) for x in line] for line in row["matrix"]])
        check(matrix == reported, "evidence block")
        check(sp.expand(matrix.det()-q(row["determinant"])) == 0, "evidence determinant")
        check(sp.expand(matrix.trace()-q(row["trace"])) == 0, "evidence trace")
        for n, value in enumerate(row["power_traces_0_to_8"]):
            check(sp.expand((matrix**n).trace()-q(value)) == 0, "evidence power trace")

    for row in data["regression"]["composite_rows"]:
        lv = q(row["lambda"])
        parts = [sp.eye(2), (1-lv)*sp.eye(2)]
        for label in row["angle_labels"]:
            cv, sv = angles[label]
            parts.append(expected.subs({c: cv, s: sv, lam: lv}))
        matrix = sp.diag(*parts)
        polynomial = sp.Poly(sp.expand((sp.eye(8)-z*matrix).det()), z)
        coefficients_ascending = list(reversed(polynomial.all_coeffs()))
        coefficients_ascending += [sp.Integer(0)] * (9-len(coefficients_ascending))
        check(coefficients_ascending == [q(x) for x in row["det_I_minus_zT_coefficients"]], "composite determinant")
        for n, value in enumerate(row["power_traces_0_to_8"]):
            check(sp.expand((matrix**n).trace()-q(value)) == 0, "composite trace")

    print(json.dumps({
        "status": "C197_SYMPY_PASS",
        "checks": checks,
        "symbolic_identities": 6,
        "evidence_rows": len(data["regression"]["block_rows"]) + len(data["regression"]["composite_rows"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
