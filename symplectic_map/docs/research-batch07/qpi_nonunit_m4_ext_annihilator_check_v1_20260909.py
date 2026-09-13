"""Fixed finite test of the old p=3 direct-sum conjecture for the original M4.

Preselected discriminator: tau^3 acting on Ext^1(M4,A), reduced modulo
(9,tau^4), A=Z[tau]_(3,tau). The old proposed sum forces this action to vanish.
A nonzero finite character is a countercertificate; a zero result is not a
proof of that conjecture. No degree scan, parameter search, or file writes.
"""

import importlib.util
import json
from pathlib import Path
import sys
import time

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

sys.dont_write_bytecode = True
SOURCE = Path(__file__).with_name('qpi_nonunit_adjacent_extension_check_v1_20260909.py')
SPEC = importlib.util.spec_from_file_location('accepted_adjacent_check_helpers', SOURCE)
HELPERS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HELPERS)
TAU = HELPERS.TAU
MODULUS = 9
TAU_CUTOFF = 4


def main():
    started = time.monotonic()
    n = 4
    original, monomials, labels = HELPERS.actual_jet(n)
    x, y = sp.symbols('x y')
    s0, s1 = x*y, x*x-x*x*y+x*y*y-TAU*y
    kernels = []
    for k in range(n+1):
        poly = sp.Poly(sp.expand(s0**(n-k)*s1**k), x, y)
        vector = sp.Matrix([poly.coeff_monomial(x**i*y**j) for i, j in monomials])
        assert HELPERS.zero(original*vector)
        assert all(ij in monomials for ij, coefficient in poly.terms() if coefficient)
        kernels.append(vector)
    distinguished = [monomials.index((n, n+k)) for k in range(n+1)]
    minor = sp.Matrix.hstack(*kernels).extract(distinguished, range(n+1))
    assert sp.expand(minor.det()) == 1
    keep = [j for j in range(len(monomials)) if j not in distinguished]
    injective = original[:, keep]
    assert injective.subs(TAU, 1).rank() == injective.cols
    presentation, _, target_rows, pivots = HELPERS.unit_reduce(injective, [])
    assert set(pivots).issubset({'1', '-1'})
    # The displayed injection is a length-one free resolution of M4.
    ext_relations = presentation.T
    ext_rank = ext_relations.rows
    size = ext_rank*TAU_CUTOFF
    columns = []
    for j in range(ext_relations.cols):
        for shift in range(TAU_CUTOFF):
            col = sp.zeros(size, 1)
            for i in range(ext_rank):
                poly = sp.Poly(sp.expand(ext_relations[i, j]), TAU, domain=sp.ZZ)
                for (power,), coefficient in poly.terms():
                    if power+shift < TAU_CUTOFF:
                        col[i*TAU_CUTOFF+power+shift, 0] += coefficient
            columns.append(col)
    columns += [MODULUS*sp.eye(size)[:, j] for j in range(size)]
    lattice = sp.Matrix.hstack(*columns)
    hnf = hermite_normal_form(lattice)
    assert hnf.shape == (size, size)
    inverse = hnf.inv()
    witnesses = []
    for generator in range(ext_rank):
        target = sp.zeros(size, 1)
        target[generator*TAU_CUTOFF+3, 0] = 1
        coordinates = inverse*target
        bad = next((i for i, value in enumerate(coordinates) if value.q != 1), None)
        if bad is None:
            continue
        character = MODULUS*inverse[bad, :]
        assert all(value.q == 1 for value in character)
        assert all(int(value) % MODULUS == 0 for value in character*lattice)
        nonzero_value = int((character*target)[0]) % MODULUS
        assert nonzero_value != 0
        witnesses.append({
            'ext_generator': generator,
            'test_class': f'tau^3 * e_{generator}',
            'character_value_mod_9': nonzero_value,
            'character_coefficients': [
                {'generator': j//TAU_CUTOFF, 'tau_coefficient': j % TAU_CUTOFF,
                 'weight_mod_9': int(value) % MODULUS}
                for j, value in enumerate(character) if int(value) % MODULUS
            ],
            'annihilates_all_reduction_relations': True,
        })
    result = {
        'evidence': 'FIXED_FINITE_EXT_CHARACTER_CERTIFICATE',
        'original_case': 'q=1,n=4,p=3; no extra degrees',
        'ring': 'A=Z[tau]_(3,tau)',
        'fixed_reduction': '(9,tau^4)',
        'original_J4_shape': list(original.shape),
        'five_original_kernel_powers_and_unit_minor': 'PASS_EXACT',
        'injection_rank_at_tau_1': injective.cols,
        'local_cancellation_pivots': len(pivots),
        'reduced_injective_presentation_shape': list(presentation.shape),
        'reduced_injective_presentation_entries': HELPERS.entries(presentation),
        'remaining_original_target_rows': [labels[i] for i in target_rows],
        'finite_character_witnesses': witnesses,
        'discriminator': 'TAU_CUBED_NONZERO_ON_EXT' if witnesses else 'NO_COUNTERCERTIFICATE',
        'interpretation': ('Contradicts the old fixed p=3 sum if its stated Ext annihilator is tau^3; '
                           'does not identify a replacement full module.' if witnesses else
                           'No obstruction at the fixed quotient; not a proof of the old sum.'),
        'elapsed_seconds': round(time.monotonic()-started, 6),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
