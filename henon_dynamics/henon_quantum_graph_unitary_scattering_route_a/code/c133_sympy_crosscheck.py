#!/usr/bin/env python3
"""Fresh symbolic cross-check using the three-by-three block reduction."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results" / "c133_quantum_graph_evidence.json").read_text())
x, y, w, z, t = sp.symbols("x y w z t")
C = sp.Rational(2, 3) * sp.ones(3) - sp.eye(3)
D = sp.diag(x, y, w)

checks = []
checks.extend(sp.simplify(v) == 0 for v in C.T * C - sp.eye(3))
checks.append(sorted(C.eigenvals().keys()) == [-1, 1])
block_det = sp.factor((sp.eye(3) - z**2 * C * D * C * D).det())
full_record = sp.sympify(data["secular_determinant"]["multivariate_expanded"], locals={"x1": x, "x2": y, "x3": w, "z": z})
checks.append(sp.expand(block_det - full_record) == 0)
physical = sp.factor(block_det.subs({z: 1, x: t, y: t**2, w: t**3}))
expected_factor = -(
    (t - 1)**3 * (t + 1) * (t**2 + 1) * (t**2 + t + 1)
    * (3 * t**2 - 2 * t + 3) * (3 * t**2 + 5 * t + 3) / 9
)
checks.append(sp.expand(physical - expected_factor) == 0)
checks.append(sp.degree(physical, t) == 12)
checks.append(sp.expand(physical).subs(t, 0) == 1)

# Newton/log-det check through z^6 at one exact phase specialization.
M = sp.zeros(6)
S = sp.zeros(6)
for i in range(3):
    for j in range(3):
        S[i, j + 3] = C[i, j]
        S[i + 3, j] = C[i, j]
M = S * sp.diag(t, t**2, t**3, t, t**2, t**3)
det_series = sp.series((sp.eye(6) - z * M).det(), z, 0, 7).removeO()
log_series = sum(-sp.trace(M**n) * z**n / n for n in range(1, 7))
checks.append(sp.expand(sp.series(sp.exp(log_series), z, 0, 7).removeO() - det_series) == 0)

assert all(checks)
print(f"C133 SymPy cross-check: PASS ({len(checks)} exact checks)")
