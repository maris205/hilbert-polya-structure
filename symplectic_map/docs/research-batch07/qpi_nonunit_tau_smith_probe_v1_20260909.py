"""Finite exact q=1 Smith diagnostics; not an all-prime theorem.

Usage: python <this-file> --case 3:0 --case 3:2
Here n:0 means QQ[tau] and n:p means GF(p)[tau]. No files are written.
The geometric interpretation is proved separately by the actual-jet paper.
"""

import argparse
import importlib.util
from pathlib import Path
import sys

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

sys.dont_write_bytecode = True
jet_source = Path(__file__).with_name('qpi_nonunit_tau_jets_diagnostic_v1_20260909.py')
jet_spec = importlib.util.spec_from_file_location('qpi_nonunit_tau_jet_source', jet_source)
jet_module = importlib.util.module_from_spec(jet_spec)
jet_spec.loader.exec_module(jet_module)


def run_case(n, p):
    if n < 1 or (p != 0 and not sp.isprime(p)):
        raise ValueError('Require n >= 1 and p equal to zero or a prime.')
    tau = sp.Symbol('tau')
    field = sp.QQ if p == 0 else sp.GF(p)
    matrix, _, _ = jet_module.jet_matrix(n, tau, sp.Integer(1))
    diagonal = smith_normal_form(matrix, domain=field.poly_ring(tau))
    free_rank = 0
    exponents = []
    for i in range(diagonal.rows):
        entry = diagonal[i, i]
        if entry == 0:
            free_rank += 1
            continue
        polynomial = sp.Poly(entry, tau, domain=field)
        if len(polynomial.terms()) != 1:
            raise AssertionError('Observed torsion not supported solely at tau=0.')
        exponent = int(polynomial.degree())
        if exponent:
            exponents.append(exponent)
    return {
        'evidence': 'FINITE_EXACT_LINEAR_ALGEBRA',
        'n': n,
        'q': 1,
        'characteristic': p,
        'matrix_shape': list(matrix.shape),
        'free_cokernel_rank': free_rank,
        'positive_tau_exponents': exponents,
        'torsion_length': sum(exponents),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', action='append', required=True, metavar='N:P')
    args = parser.parse_args()
    for case in args.case:
        n, p = (int(value) for value in case.split(':'))
        print(run_case(n, p), flush=True)


if __name__ == '__main__':
    main()
