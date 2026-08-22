#!/usr/bin/env python3
"""Independent SymPy cross-check of the transfer determinant and trace prefix."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c104_multibranch_evidence.json"


def main() -> None:
    value = json.loads(EVIDENCE.read_text())
    matrix = sp.Matrix(value["transfer_atlas"]["matrix"])
    z = sp.symbols("z")
    determinant = sp.Poly((sp.eye(matrix.rows) - z * matrix).det(), z)
    coefficients = list(reversed([int(x) for x in determinant.all_coeffs()]))
    expected = value["transfer_atlas"]["determinant_I_minus_zA_coefficients_low_to_high"]
    assert coefficients == expected
    padded = coefficients + [0] * (6 + 1 - len(coefficients))
    trace_checks = 0
    for n in range(1, 7):
        actual = int(sp.trace(matrix ** n))
        assert actual == int(value["transfer_atlas"]["trace_of_powers"][str(n)])
        trace_checks += 1
    # Newton identities provide an independent check that the determinant
    # coefficients agree with the first six traces.
    for k in range(1, 7):
        lhs = k * padded[k]
        rhs = -sum(padded[k - j] * int(sp.trace(matrix ** j)) for j in range(1, k + 1))
        assert lhs == rhs
    print(json.dumps({"status": "C104_SYMPY_PASS", "trace_checks": trace_checks, "determinant_degree": determinant.degree()}, sort_keys=True))


if __name__ == "__main__":
    main()
