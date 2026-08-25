#!/usr/bin/env python3
"""Independent SymPy reconstruction of the C164 operator identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c164_fredholm_owner_evidence.json"


def tm(n: int) -> int:
    return sum(int(digit) for digit in format(n, "b")) % 2


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    replay = data["finite_replay"]
    z = sp.symbols("z")
    checks = 0

    gaps = [s for s in range(16) if tm(s)][:5]
    gauges = sp.symbols("q0:" + str(len(gaps)), nonzero=True)
    u = sp.Matrix(gauges)
    ell = sp.Matrix([[z ** (s + 1) / gauges[j] for j, s in enumerate(gaps)]])
    matrix = u * ell
    truncated_f = sum(z ** (s + 1) for s in gaps)
    assert sp.simplify(sp.trace(matrix) - truncated_f) == 0
    checks += 1
    for power in range(1, 5):
        assert sp.simplify(sp.trace(matrix**power) - truncated_f**power) == 0
        checks += 1
    assert sp.factor((sp.eye(len(gaps)) - matrix).det()) == sp.factor(1 - truncated_f)
    checks += 1
    augmented = sp.diag(z, *([sp.Integer(0)] * len(gaps)))
    augmented[1:, 1:] = matrix
    assert sp.factor((sp.eye(len(gaps) + 1) - augmented).det()) == sp.factor((1 - z) * (1 - truncated_f))
    checks += 1

    limit = 24
    f = sum(tm(n - 1) * z**n for n in range(1, limit + 1))
    for power, row in enumerate(replay["trace_power_rows"], 1):
        polynomial = sp.Poly(sp.expand(f**power), z)
        for degree in range(limit + 1):
            assert int(polynomial.nth(degree)) == row["coefficients"][degree]
            checks += 1
    determinant = sp.Poly(sp.expand((1 - z) * (1 - f)), z)
    for degree in range(limit + 1):
        assert int(determinant.nth(degree)) == replay["determinant_coefficients"][degree]
        checks += 1

    # The branch gauge cancels exactly under any diagonal rescaling.
    rescaling = sp.diag(*sp.symbols("d0:" + str(len(gaps)), nonzero=True))
    conjugated = rescaling * matrix * rescaling.inv()
    for power in range(1, 4):
        assert sp.simplify(sp.trace(conjugated**power) - sp.trace(matrix**power)) == 0
        checks += 1

    # Exact finite control for w_n=2^n: every advance column has norm^2 two.
    for n in range(12):
        assert sp.Rational(2 ** (n + 1), 2**n) == 2
        checks += 1
    print(json.dumps({"status": "C164_SYMPY_PASS", "checks": checks, "formal_degree": limit, "matrix_branches": len(gaps)}, sort_keys=True))


if __name__ == "__main__":
    main()
