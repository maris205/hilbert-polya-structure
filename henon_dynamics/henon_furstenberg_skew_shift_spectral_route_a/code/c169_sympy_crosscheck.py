#!/usr/bin/env python3
"""Independent SymPy identities for the HCS-C169 theorem package."""
from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    x, y, alpha = sp.symbols("x y alpha", real=True)
    m, k = sp.symbols("m k", integer=True)
    checks = 0

    xn, yn = x, y
    for n in range(1, 49):
        xn, yn = sp.expand(xn + alpha), sp.expand(yn + xn)
        assert sp.expand(xn - (x + n * alpha)) == 0
        checks += 1
        assert sp.expand(yn - (y + n * x + sp.binomial(n, 2) * alpha)) == 0
        checks += 1

    # Fourier exponent after composition with T.
    exponent = sp.expand(m * (x + alpha) + k * (y + x))
    expected = sp.expand(m * alpha + (m + k) * x + k * y)
    assert sp.expand(exponent - expected) == 0
    checks += 1

    # R T R and T^{-1} agree as affine maps before reduction modulo one.
    rx, ry = alpha - x, y
    trx, try_ = sp.expand(rx + alpha), sp.expand(ry + rx)
    rtrx, rtry = sp.expand(alpha - trx), try_
    invx, invy = sp.expand(x - alpha), sp.expand(y - x + alpha)
    assert sp.expand(rtrx - invx) == 0
    checks += 1
    assert sp.expand(rtry - invy) == 0
    checks += 1
    assert sp.expand(alpha - (alpha - x) - x) == 0
    checks += 1

    # Each nonzero k decomposes by residues modulo |k|; the tested orbit labels
    # are pairwise distinct and advance by one bilateral coordinate.
    for kval in list(range(-20, 0)) + list(range(1, 21)):
        step = abs(kval)
        for residue in range(step):
            labels = [residue + q * kval for q in range(-10, 11)]
            assert len(labels) == len(set(labels))
            checks += 1
            assert all(labels[i + 1] - labels[i] == kval for i in range(len(labels) - 1))
            checks += 1

    print(json.dumps({"status": "C169_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
