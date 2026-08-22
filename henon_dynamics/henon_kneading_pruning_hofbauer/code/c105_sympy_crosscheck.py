#!/usr/bin/env python3
"""Independent symbolic check of the formal determinant prefix."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
doc = json.loads((ROOT / "results/c105_kneading_evidence.json").read_text())
z = sp.Symbol("z")
traces = {int(k): int(v) for k, v in doc["trace_counts"].items()}
series = sum(sp.Rational(traces[n], n) * z**n for n in traces)
det = sp.series(sp.exp(-series), z, 0, max(traces) + 1).removeO().expand()
coeffs = [f"{sp.Rational(det.coeff(z, n)).p}/{sp.Rational(det.coeff(z, n)).q}" for n in range(max(traces) + 1)]
assert coeffs == doc["determinant_prefix"]
assert all(
    Fraction(int(x.split('/')[0]), int(x.split('/')[1])) == Fraction(int(sp.Rational(det.coeff(z, i)).p), int(sp.Rational(det.coeff(z, i)).q))
    for i, x in enumerate(coeffs)
)
print("C105_SYMPY_PASS")
