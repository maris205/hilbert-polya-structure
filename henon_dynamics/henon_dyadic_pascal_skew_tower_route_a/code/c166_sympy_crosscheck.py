#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C166."""
import json
from math import comb

import sympy as sp


def main():
    checks = 0
    t = sp.symbols("t")
    rational_image = -t / (1 + t)
    assert sp.cancel(rational_image.subs(t, rational_image) - t) == 0
    assert sp.cancel(1 + rational_image - 1 / (1 + t)) == 0
    checks += 2
    for dimension in range(2, 13):
        size = dimension + 1
        S = sp.zeros(size)
        S[0, 0] = 1
        for i in range(1, size):
            for j in range(1, i + 1):
                S[i, j] = (-1) ** i * comb(i - 1, j - 1)
        J = sp.eye(size)
        Jinv = sp.eye(size)
        for i in range(1, size):
            J[i, i - 1] = 1
            for j in range(i):
                Jinv[i, j] = (-1) ** (i - j)
        assert S * S == sp.eye(size)
        assert S * J * S == Jinv
        checks += 2

    for r in range(1, 6):
        modulus = 1 << r
        for dimension in range(2, 13):
            a = dimension.bit_length() - 1
            period = 1 << (r + a)
            for n in range(1, 2 * period + 1):
                fixed = all(comb(n, k) % modulus == 0 for k in range(1, dimension + 1))
                assert fixed == (n % period == 0)
                checks += 1
            witness = comb(period // 2, 1 << a)
            assert witness % modulus != 0
            checks += 1

    print(json.dumps({"status": "C166_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
