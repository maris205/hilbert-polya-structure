"""Exact exploratory jet ranks for the eight-section qPI blowup.

This is a finite characteristic-zero diagnostic, not an all-degree proof.
The coefficient columns are x^i y^j, 0 <= i,j <= 2*n.  Each blowup
imposes multiplicity n on the transform after removing previous exceptional
factors. Negative powers below are already killed by earlier jet rows.
No input artifacts are changed and this script writes no output files.
"""

import argparse
import math
import sympy as sp


def jet_matrix(n, tau, q):
    columns = [(i, j) for i in range(2*n+1) for j in range(2*n+1)]
    rows = []
    names = []

    def row(name, formula):
        names.append(name)
        rows.append([formula(i, j) for i, j in columns])

    def binom(a, b):
        return math.comb(a, b) if a >= b >= 0 else 0

    for a in range(n):
        for b in range(n-a):
            # Q=u^(2n)P(1/u,1+v).
            row(('c1', a, b), lambda i, j: binom(j, b) if 2*n-i == a else 0)
            # Q=u^(2n)P(v,1/u).
            row(('c2a', a, b), lambda i, j: int(2*n-j == a and i == b))
            # Q=u^n P(u*w,1/u), then w=tau+v.
            row(('c2b', a, b), lambda i, j: binom(i, b)*tau**(i-b)
                if n+i-j == a and i >= b else 0)
            # P(u,v).
            row(('c3a', a, b), lambda i, j: int(i == a and j == b))
            # u^(-n) P(u,u*v).
            row(('c3b', a, b), lambda i, j: int(i+j-n == a and j == b))
            # u^(-2n)w^(-n)P(u*w,u^2*w), w=tau+v.
            row(('c3c', a, b), lambda i, j: binom(i+j-n, b)*tau**(i+j-n-b)
                if i+2*j-2*n == a and i+j-n >= b else 0)
            # u^(2n)v^(2n)P(1/v,1/u).
            row(('c4a', a, b), lambda i, j: int(2*n-j == a and 2*n-i == b))
            # u^(3n)w^(2n)P(1/(u*w),1/u), w=q+v.
            row(('c4b', a, b), lambda i, j: binom(2*n-i, b)*q**(2*n-i-b)
                if 3*n-i-j == a and 2*n-i >= b else 0)
    return sp.Matrix(rows), columns, names


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=4)
    parser.add_argument('--kernel', action='store_true')
    parser.add_argument('--symbolic-reduction', action='store_true')
    args = parser.parse_args()
    x, y = sp.symbols('x y')
    if args.symbolic_reduction:
        tau, q = sp.symbols('tau q')
        for n in range(1, args.max_n+1):
            matrix, _, _ = jet_matrix(n, tau, q)
            pivots = 0
            while matrix.rows and matrix.cols:
                pivot = None
                for i in range(matrix.rows):
                    for j in range(matrix.cols):
                        entry = sp.factor(matrix[i,j])
                        coefficient, power = entry.as_coeff_exponent(q)
                        if coefficient in (-1, 1) and power.is_Integer:
                            pivot = (i, j)
                            break
                    if pivot is not None:
                        break
                if pivot is None:
                    break
                i, j = pivot
                entry = matrix[i,j]
                r_indices = [r for r in range(matrix.rows) if r != i]
                c_indices = [c for c in range(matrix.cols) if c != j]
                matrix = sp.Matrix([[sp.cancel(matrix[r,c]-matrix[r,j]*matrix[i,c]/entry)
                                     for c in c_indices] for r in r_indices])
                pivots += 1
            print(dict(n=n, legal_unit_pivots=pivots, remaining_shape=matrix.shape), flush=True)
            print(matrix.applyfunc(sp.factor), flush=True)
        return
    for n in range(1, args.max_n+1):
        for tau, q in [(0, 2), (0, 1), (0, -1), (1, 2), (1, 1), (1, -1)]:
            matrix, columns, _ = jet_matrix(n, sp.Integer(tau), sp.Integer(q))
            kernel = matrix.nullspace()
            rank = matrix.cols-len(kernel)
            print(dict(n=n, tau=tau, q=q, rows=matrix.rows,
                       cols=matrix.cols, rank=rank, kernel_dimension=len(kernel)), flush=True)
            if args.kernel and tau == 0 and q == 2:
                for vector in kernel:
                    print(sp.factor(sum(c*x**i*y**j for c, (i,j) in zip(vector, columns))), flush=True)


if __name__ == '__main__':
    main()
