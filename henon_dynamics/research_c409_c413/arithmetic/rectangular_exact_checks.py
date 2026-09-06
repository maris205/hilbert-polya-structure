"""Small exact sanity checks; the infinite analytic assertions require proof.

Run with Python 3, using only the standard library. No files are written.
"""

from fractions import Fraction
from math import gcd


def main():
    kernel_checks = 0
    for a in range(2, 9):
        for b in range(2, 9):
            for n in range(1, 5):
                for m in range(1, 5):
                    left, right = a**n - 1, b**m - 1
                    left_kernel = {Fraction(j, left) for j in range(left)}
                    right_kernel = {Fraction(j, right) for j in range(right)}
                    assert len(left_kernel & right_kernel) == gcd(left, right)
                    kernel_checks += 1

    coefficient_checks = 0
    for c in range(2, 6):
        for r in range(1, 6):
            for s in range(1, 6):
                if gcd(r, s) != 1:
                    continue
                for n in range(1, 19):
                    for m in range(1, 19):
                        k = gcd(n, m)
                        i, j = n // k, m // k
                        exponent = gcd(r * i, s * j)
                        assert exponent == gcd(r, j) * gcd(s, i)
                        assert (r * s) % exponent == 0
                        direct = gcd(c ** (r * n) - 1, c ** (s * m) - 1)
                        assert direct == c ** (exponent * k) - 1
                        coefficient_checks += 1

    # For c=2, r=s=1 and x0=y0=2^(-1/5), precisely the primitive
    # positive pairs i+j=5 meet at the point. The residue is -x0
    # times this rational factor, independently of numerical roots.
    primitive_pairs = [(i, 5 - i) for i in range(1, 5) if gcd(i, 5 - i) == 1]
    assert primitive_pairs == [(1, 4), (2, 3), (3, 2), (4, 1)]
    residue_factor = sum((Fraction(1, i) for i, _ in primitive_pairs), Fraction())
    assert residue_factor == Fraction(25, 12)

    print(
        {
            "explicit_circle_kernel_intersections": kernel_checks,
            "dependent_ray_coefficient_checks": coefficient_checks,
            "c2_symmetric_four_pole_residue_factor": str(residue_factor),
            "status": "all exact finite checks passed; no analytic theorem certified by sampling",
        }
    )


if __name__ == "__main__":
    main()
