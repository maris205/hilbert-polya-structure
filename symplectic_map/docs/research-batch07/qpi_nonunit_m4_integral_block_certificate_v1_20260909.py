"""Fixed q=1,n=4 integral block certificate over Z[tau]_(3,tau).

Exact original matrix, unit cancellations, and displayed basis changes only.
No degree scan, modular rank inference, floating point, or output file writes.
"""

import importlib.util
import json
from pathlib import Path
import sys
import time

import sympy as sp

sys.dont_write_bytecode = True
SOURCE = Path(__file__).with_name('qpi_nonunit_adjacent_extension_check_v1_20260909.py')
SPEC = importlib.util.spec_from_file_location('adjacent_original_helpers', SOURCE)
HELPERS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HELPERS)
t = HELPERS.TAU


def main():
    started = time.monotonic()
    original, monomials, labels = HELPERS.actual_jet(4)
    x, y = sp.symbols('x y')
    s0, s1 = x*y, x*x-x*x*y+x*y*y-t*y
    kernels = []
    for k in range(5):
        poly = sp.Poly(sp.expand(s0**(4-k)*s1**k), x, y)
        kernels.append(sp.Matrix([poly.coeff_monomial(x**i*y**j)
                                  for i, j in monomials]))
    kernel = sp.Matrix.hstack(*kernels)
    assert HELPERS.zero(original*kernel)
    distinguished = [monomials.index((4, 4+k)) for k in range(5)]
    assert sp.expand(kernel.extract(distinguished, range(5)).det()) == 1
    keep = [j for j in range(original.cols) if j not in distinguished]
    reduced, _, target_rows, pivots = HELPERS.unit_reduce(original[:, keep], [])
    assert pivots and set(pivots) == {'1', '-1'}
    assert len(pivots) == 30
    assert [labels[i] for i in target_rows] == [
        (2, 1, 0), (2, 2, 0), (2, 2, 1), (2, 3, 0), (3, 0, 0),
        (3, 1, 0), (3, 1, 1), (3, 2, 0), (3, 2, 1), (3, 3, 0)]
    eye = sp.eye(10)
    A, B, C, D, E, F, G, H, I, J = [eye[:, j] for j in range(10)]
    columns = [t**2*B+2*t*C+t**2*H+2*t*I,
               t**3*D+t**3*J, t**3*B+3*t**2*C,
               t**3*H+3*t**2*I, 2*t**3*F+3*t**2*G+t**4*J,
               -t**3*A-t**3*F]
    hand = sp.Matrix.hstack(*columns)
    assert HELPERS.zero(reduced-hand)
    # New target generators in the old A,...,J free basis.
    target_basis = sp.Matrix.hstack(
        E, J, 2*F+t*J, G, H, I, D+J, A+F, B+H,
        C+I+sp.Rational(1, 2)*t*(B+H))
    # New relations c4,c3,c1,-c5,-2c2-2c3+3t*c0,c0/2.
    source_eye = sp.eye(6)
    c = [source_eye[:, j] for j in range(6)]
    relation_basis = sp.Matrix.hstack(c[4], c[3], c[1], -c[5],
                                      -2*c[2]-2*c[3]+3*t*c[0], c[0]/2)
    target_det = sp.expand(target_basis.det())
    relation_det = sp.expand(relation_basis.det())
    assert target_det in (2, -2)
    assert relation_det in (1, -1)
    expected = sp.zeros(10, 6)
    expected[2, 0], expected[3, 0] = t**3, 3*t**2
    expected[4, 1], expected[5, 1] = t**3, 3*t**2
    expected[6, 2] = expected[7, 3] = expected[8, 4] = t**3
    expected[9, 5] = t
    assert HELPERS.zero(reduced*relation_basis-target_basis*expected)
    result = {
        'evidence': 'FIXED_EXACT_ORIGINAL_INTEGRAL_BLOCK_EQUIVALENCE',
        'case': 'q=1,n=4,A=Z[tau]_(3,tau)',
        'original_shape': list(original.shape),
        'original_kernel_powers_and_unit_minor': 'PASS_EXACT',
        'number_of_unit_cancellations': len(pivots),
        'cancellation_units': sorted(set(pivots)),
        'reduced_shape': list(reduced.shape),
        'six_displayed_relations': 'PASS_EXACT',
        'target_basis_determinant': str(target_det),
        'relation_basis_determinant': str(relation_det),
        'complete_block_equivalence': 'PASS_EXACT',
        'block_entries': HELPERS.entries(expected),
        'permitted_denominators': 'powers of 2 only; no tau or 3 inverted',
        'limits': ['fixed n=4 at (3,tau), not all degrees or all primes',
                   'matrix certificate is separate from the written torsion/defect proof'],
        'elapsed_seconds': round(time.monotonic()-started, 6),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
