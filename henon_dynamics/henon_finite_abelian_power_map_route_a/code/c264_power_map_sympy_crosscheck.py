#!/usr/bin/env python3
"""Exact SymPy matrix checks for selected HCS-C264 maps."""
import itertools, json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results/c264_power_map_evidence.json").read_text())
lam = sp.symbols("lambda")
checks = 0
selected = [c for c in data["regression"]["cases"] if c["order"] <= 18 and c["d"] in (0, 1, 2, 3, 5, 6, 7, 10, 12, 17)]
for c in selected:
    ns, d = c["group"], c["d"]
    xs = list(itertools.product(*(range(n) for n in ns))) if ns else [()]
    pos = {x: i for i, x in enumerate(xs)}
    U = sp.zeros(len(xs))
    for i, x in enumerate(xs):
        y = tuple(d * v % n for v, n in zip(x, ns))
        U[i, pos[y]] = 1
    expected = lam ** c["koopman_characteristic_ledger"]["zero_multiplicity"]
    for m, number in c["cycle_counts"].items():
        expected *= (lam ** int(m) - 1) ** number
    assert sp.Poly(U.charpoly(lam).as_expr() - sp.expand(expected), lam).is_zero
    checks += 1
    for j, rank in enumerate(c["image_ranks"]):
        assert (U ** j).rank() == rank
        checks += 1
    zero_mult = c["order"] - c["periodic_points"]
    assert sum(int(j) * z for j, z in c["zero_jordan_blocks"].items()) == zero_mult
    checks += 1
assert len(selected) >= 100
print(f"C264_SYMPY_PASS ({checks} symbolic matrix/rank checks across {len(selected)} maps)")
