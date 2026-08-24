#!/usr/bin/env python3
"""Independent SymPy return, block-determinant, and trace checks for C116."""
import json
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c116_lozi_evidence.json").read_text())
MATS = (
    sp.Matrix([[2, sp.Rational(1, 2)], [1, 0]]),
    sp.Matrix([[-2, sp.Rational(1, 2)], [1, 0]]),
)
TRANSLATION = sp.Matrix([1, 0])
RHO = (sp.Rational(1, 2), sp.Rational(2, 3))
lam, z = sp.symbols("lambda z")
checks = 0

for row in DATA["primitive_rows"]:
    matrix = sp.eye(2)
    translation = sp.zeros(2, 1)
    for symbol in row["symbols"]:
        matrix, translation = MATS[symbol] * matrix, MATS[symbol] * translation + TRANSLATION
    point = (sp.eye(2) - matrix).inv() * translation
    expected = sp.Matrix([sp.Rational(value) for value in row["fixed_point"]])
    assert sp.simplify(point - expected) == sp.zeros(2, 1)
    assert str(sp.factor(matrix.charpoly(lam).as_expr())) == row["monodromy_characteristic"]
    assert str(sp.factor(matrix.det())) == row["monodromy_determinant"]
    current = point
    for symbol in row["symbols"]:
        assert current[0] != 0 and bool(current[0] < 0) == (symbol == 0)
        current = MATS[symbol] * current + TRANSLATION
    assert sp.simplify(current - point) == sp.zeros(2, 1)

    n = row["length"]
    block = sp.zeros(n)
    for phase, symbol in enumerate(row["symbols"]):
        block[(phase + 1) % n, phase] = RHO[symbol]
    weight = sp.Rational(row["branch_weight"])
    assert sp.simplify(sp.factor((sp.eye(n) - z * block).det()) - (1 - weight * z**n)) == 0
    checks += 5

operator = DATA["finite_cycle_atlas_operator"]
for power in range(1, 9):
    trace_value = sp.Rational(0)
    for row in DATA["primitive_rows"]:
        n = row["length"]
        if power % n == 0:
            trace_value += n * sp.Rational(row["branch_weight"]) ** (power // n)
    assert sp.factor(trace_value) == sp.Rational(operator["weighted_trace_prefix"][str(power)])
    checks += 1

factor_counter = {}
for row in DATA["primitive_rows"]:
    key = (row["length"], row["branch_weight"])
    factor_counter[key] = factor_counter.get(key, 0) + 1
receipt_counter = {
    (row["length"], row["cycle_weight"]): row["multiplicity"]
    for row in operator["determinant_factor_ledger"]
}
assert factor_counter == receipt_counter
checks += len(factor_counter)
print("C116_SYMPY_PASS", checks)
