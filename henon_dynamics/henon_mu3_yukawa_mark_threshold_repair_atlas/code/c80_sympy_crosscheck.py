#!/usr/bin/env python3
"""Compact symbolic checks for the C80 threshold receipt."""

from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c80_threshold_repair_atlas_evidence.json"
EXPECTED = "8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main():
    raw = EVIDENCE.read_bytes()
    assert sha256(raw).hexdigest() == EXPECTED
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    atlas = evidence["target_atlas"]
    assert len(atlas["profile_rows"]) == 1 << 16
    x, y = sp.symbols("x y")
    # Every target table is a complete deleted-cardinality inventory.
    for target, table in enumerate(atlas["deleted_cardinality_tables"]):
        polynomial = sum(value * x ** int(key.split(",")[0]) * y ** int(key.split(",")[1])
                         for key, value in table.items())
        assert sp.expand(polynomial.subs(y, 1)) == sp.expand((1 + x) ** 16)
        # The constant term is one (the full retained support always contains
        # every target), and no threshold exceeds the target's finite bound.
        assert sp.expand(polynomial.subs(x, 0)) == 1
        assert all(int(k.split(",")[1]) <= 3 for k in table)
    q = atlas["deleted_cardinality_tables"][19]
    q_poly = sp.expand(sum(value * x ** int(key.split(",")[0]) * y ** int(key.split(",")[1])
                           for key, value in q.items()))
    expected_q = (
        (1 + x) ** 6 * (1 + x * y) *
        (1 + x) * (1 + x) * (1 + 2*x) * (1 + 5*x)
    )
    # Replace the four fully-deleted-block state markers by y^(max(0,r-2)).
    # A direct symbolic sum over block states avoids relying on the stored q
    # row and gives the exact C78 polynomial.
    transformed = 0
    sizes = (1, 1, 2, 5)
    from itertools import product
    for state in product((0, 1), repeat=4):
        r = sum(state)
        term = x ** sum(size for size, flag in zip(sizes, state) if flag)
        for size, flag in zip(sizes, state):
            if not flag:
                term *= (1 + x) ** size - x ** size
        transformed += term * y ** max(0, r - 2)
    expected_q = sp.expand((1 + x) ** 6 * (1 + x * y) * transformed)
    assert q_poly == expected_q
    assert sp.expand(q_poly.subs(x, 1)) == 30400 + 32704*y + 2368*y**2 + 64*y**3
    assert evidence["target_atlas"]["threshold_distributions"][19] == {
        "0": 30400, "1": 32704, "2": 2368, "3": 64,
    }
    print(json.dumps({"status": "C80_SYMPY_CROSSCHECK_PASS", "target_rows": 20,
                      "q_polynomial": "30400+32704y+2368y^2+64y^3 at x=1",
                      "all_cardinality_marginals": True}, sort_keys=True))


if __name__ == "__main__":
    main()
