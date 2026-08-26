#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C172."""
from __future__ import annotations

import json

import sympy as sp


Q_VALUES = [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32]


def main() -> None:
    z = sp.symbols("z")
    checks = 0
    for Q in Q_VALUES:
        N = Q-1
        U = sp.zeros(Q)
        U[0,0] = 1
        for k in range(N):
            U[1+k,1+(k+1)%N] = 1
        determinant = sp.factor((sp.eye(Q)-z*U).det())
        assert sp.expand(determinant-(1-z)*(1-z**N)) == 0
        checks += 1
        assert U.T*U == sp.eye(Q)
        checks += 1
        assert (U-U.T).is_zero_matrix is (N<=2)
        checks += 1
        for n in range(1,25):
            assert sp.trace(U**n) == (Q if n%N==0 else 1)
            checks += 1
    print(json.dumps({"status": "C172_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
