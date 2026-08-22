#!/usr/bin/env python3
"""Independent SymPy/Newton check for the C110 finite Floquet prefixes."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c110_nonautonomous_evidence.json"
MAX_N = 6
Q = ((1, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 1), (0, 1, 0, 1))
CONTROLS = ("chronological_01", "reversed_10", "same_parameter_00")


def branch(phase: int, symbol: int) -> sp.Matrix:
    slope = 2 * (-1 if symbol == 0 else 1) + (0 if phase == 0 else 1)
    return sp.Matrix([[slope, -1], [1, 0]])


def block(symbol: int, control: str) -> sp.Matrix:
    s0, s1 = divmod(symbol, 2)
    if control == "chronological_01":
        return branch(1, s1) * branch(0, s0)
    if control == "reversed_10":
        return branch(0, s0) * branch(1, s1)
    return branch(0, s1) * branch(0, s0)


def transfer(control: str) -> sp.Matrix:
    out = sp.zeros(8, 8)
    for i in range(4):
        for j in range(4):
            if Q[i][j]:
                b = block(j, control)
                for r in range(2):
                    for c in range(2):
                        out[2 * i + r, 2 * j + c] = b[r, c]
    return out


def main() -> None:
    value = json.loads(EVIDENCE.read_text())
    checks = 0
    for control in CONTROLS:
        A = transfer(control)
        atlas = value["transfer_atlas"][control]
        for n in range(1, MAX_N + 1):
            assert int(sp.trace(A ** n)) == atlas["trace_of_powers"][str(n)]
            checks += 1
        z = sp.symbols("z")
        polynomial = sp.Poly((sp.eye(8) - z * A).det(), z)
        coeffs = [int(polynomial.nth(k)) for k in range(0, polynomial.degree() + 1)]
        assert coeffs == atlas["determinant_I_minus_zA_coefficients_low_to_high"]
        checks += 1
        # Newton recurrence for D(z)=det(I-zA), with c_0=1.
        c = atlas["determinant_I_minus_zA_coefficients_low_to_high"]
        for k in range(1, min(MAX_N, len(c) - 1) + 1):
            lhs = k * c[k]
            rhs = -sum(c[k - j] * atlas["trace_of_powers"][str(j)] for j in range(1, k + 1))
            assert lhs == rhs
            checks += 1
    assert value["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    print(json.dumps({"status": "C110_SYMPY_PASS", "checks": checks, "controls": list(CONTROLS)}, sort_keys=True))


if __name__ == "__main__":
    main()
