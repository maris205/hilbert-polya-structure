#!/usr/bin/env python3
"""Symbolic cross-check of the C78 bivariate repair polynomial."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from math import comb
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c78_repair_distance_geometry_evidence.json"
EXPECTED = "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae"
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
    x, y, z = sp.symbols("x y z")
    H = 1
    for size in (1, 1, 2, 5):
        H *= sum(comb(size, d) * x ** d for d in range(size)) + z * x ** size
    transformed = 0
    for (degree, full_blocks), coefficient in sp.Poly(sp.expand(H), x, z).terms():
        transformed += coefficient * x ** degree * y ** max(0, full_blocks - 2)
    predicted = sp.expand((1 + x) ** 6 * (1 + x * y) * transformed)
    actual = sp.expand(sum(
        coefficient * x ** int(key.split(",")[0]) * y ** int(key.split(",")[1])
        for key, coefficient in evidence["bivariate_generating_function"]["coefficient_table"].items()
    ))
    assert predicted == actual
    assert sp.expand(predicted.subs(y, 1)) == sp.expand((1 + x) ** 16)
    assert sp.expand(predicted.subs(x, 1)) == 30400 + 32704 * y + 2368 * y ** 2 + 64 * y ** 3
    assert evidence["repair_distance_atlas"]["deletion_count_distribution"] == {
        "0": 30400, "1": 32704, "2": 2368, "3": 64,
    }
    print(json.dumps({
        "status": "SYMPY_CROSSCHECK_PASS",
        "evidence_sha256": EXPECTED,
        "coefficient_identity": True,
        "P_x_at_y1": "(1+x)^16",
        "P_1_at_y": "30400+32704y+2368y^2+64y^3",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
