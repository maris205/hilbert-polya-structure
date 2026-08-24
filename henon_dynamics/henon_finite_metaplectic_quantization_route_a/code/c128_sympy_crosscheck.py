#!/usr/bin/env python3
"""Separate SymPy cross-check for C128."""
import sympy as sp


def main():
    A = sp.Matrix([[3, -1], [1, 0]])
    R = sp.Matrix([[0, 1], [1, 0]])
    assert A.det() == 1 and R * A * R == A.inv()
    checks = 2
    traces = [2, 3]
    for n in range(2, 17): traces.append(3 * traces[-1] - traces[-2])
    for n in range(1, 17):
        assert abs(int((A**n - sp.eye(2)).det())) == traces[n] - 2
        checks += 1
    N = 7
    w = sp.exp(2 * sp.pi * sp.I / N)
    F = sp.Matrix(N, N, lambda x, y: w ** (x * y) / sp.sqrt(N))
    C = sp.diag(*[w ** ((12 * x * x) % N) for x in range(N)])
    U = C * F.conjugate().T
    Un = sp.N(U, 70)
    eye = sp.eye(N)
    assert max(abs(complex(v)) for v in sp.N(Un * Un.conjugate().T - eye, 60)) < 1e-50
    assert max(abs(complex(v)) for v in sp.N(Un**8 - eye, 60)) < 1e-48
    checks += 2
    z = sp.symbols("z")
    expected = 1-sp.I*z-z**2+sp.I*z**3+z**4-sp.I*z**5-z**6+sp.I*z**7
    assert sp.expand((1 + sp.I*z) * expected) == 1-z**8
    checks += 1
    assert not any((2 * h) % 8 == 1 for h in range(8))
    checks += 1
    print(f"C128 SymPy cross-check: PASS ({checks} checks)")


if __name__ == "__main__": main()
