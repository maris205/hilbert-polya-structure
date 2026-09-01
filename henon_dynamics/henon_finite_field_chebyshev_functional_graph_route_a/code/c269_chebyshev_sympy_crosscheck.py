#!/usr/bin/env python3
"""Exact SymPy matrix checks for selected HCS-C269 field maps."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results/c269_chebyshev_evidence.json").read_text())
lam = sp.symbols("lambda")


def unpack(a, p, r):
    out = []
    for _ in range(r): out.append(a % p); a //= p
    return out


def pack(cs, p, r):
    value, place = 0, 1
    for c in cs[:r]: value += c % p * place; place *= p
    return value


def add(a, b, p, r):
    return pack([(x + y) % p for x, y in zip(unpack(a, p, r), unpack(b, p, r))], p, r)


def mul(a, b, p, mod):
    r = len(mod) - 1; aa, bb = unpack(a, p, r), unpack(b, p, r)
    cc = [0] * (2 * r - 1)
    for i, x in enumerate(aa):
        for j, y in enumerate(bb): cc[i + j] = (cc[i + j] + x * y) % p
    for k in range(len(cc) - 1, r - 1, -1):
        lead = cc[k]
        for j in range(r): cc[k - r + j] = (cc[k - r + j] - lead * mod[j]) % p
    return pack(cc, p, r)


def cheb(x, d, p, mod):
    r = len(mod) - 1
    if d == 0: return 2 % p
    if d == 1: return x
    old, cur = 2 % p, x
    for _ in range(2, d + 1):
        old, cur = cur, add(mul(x, cur, p, mod), pack([-z for z in unpack(old, p, r)], p, r), p, r)
    return cur


checks = 0
selected = [c for c in data["regression"]["cases"] if c["q"] <= 16 and c["d"] in (0, 1, 2, 3, 4, 5, 7, 10)]
for c in selected:
    q, p, mod, d = c["q"], c["p"], c["modulus"], c["d"]
    mapping = [cheb(x, d, p, mod) for x in range(q)]
    U = sp.zeros(q)
    for x, y in enumerate(mapping): U[x, y] = 1
    expected = lam ** c["koopman_characteristic_ledger"]["zero_multiplicity"]
    for m, number in c["cycle_counts"].items(): expected *= (lam ** int(m) - 1) ** number
    assert sp.Poly(U.charpoly(lam).as_expr() - sp.expand(expected), lam).is_zero
    checks += 1
    for j, rank in enumerate(c["image_ranks"]):
        assert (U ** j).rank() == rank
        checks += 1
    assert sum(int(j) * z for j, z in c["zero_jordan_blocks"].items()) == q - c["periodic_points"]
    checks += 1
assert len(selected) == 64
print(f"C269_SYMPY_PASS ({checks} symbolic matrix/rank checks across {len(selected)} maps)")
