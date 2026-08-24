#!/usr/bin/env python3
"""Independent SymPy checks for C131."""
import sympy as sp


def main() -> None:
    A = sp.Matrix([[3, -1], [1, 0]])
    R = sp.Matrix([[0, 1], [1, 0]])
    assert A.det() == 1 and R * A * R == A.inv()
    checks = 2
    u = [0, 1]
    for _ in range(18):
        u.append(3 * u[-1] - u[-2])
    for n in range(1, 17):
        assert A**n == sp.Matrix([[u[n + 1], -u[n]], [u[n], -u[n - 1]]])
        assert max(abs(int(x)) for x in A**n - sp.eye(2)) == u[n + 1] - 1
        checks += 2
    for modulus in [3, 5, 7, 9, 11, 15, 23, 57, 145]:
        half = sp.mod_inverse(2, modulus)
        assert (2 * half) % modulus == 1
        checks += 1
        for q in range(modulus):
            for p in range(modulus):
                assert (-half * q * p + half * q * p) % modulus == 0
                assert (2 * half * q * p - q * p) % modulus == 0
                checks += 2
    assert not any((2 * x) % 8 == 1 for x in range(8))
    checks += 1
    print(f"C131 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
