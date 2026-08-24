#!/usr/bin/env python3
"""Direct symbolic identity cross-check for C118."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'results/c118_damped_dimer_evidence.json').read_text())
q1,q2=sp.symbols('q1 q2'); a=sp.Rational(13,2); g=sp.Rational(1,2); k=sp.Rational(1,4)
L=sp.Matrix([[1,-1],[-1,1]])
H=sp.diag(a-2*q1,a-2*q2)-k*L
J=H.row_join(-g*sp.eye(2)).col_join(sp.eye(2).row_join(sp.zeros(2)))
Om=sp.zeros(2).row_join(sp.eye(2)).col_join((-sp.eye(2)).row_join(sp.zeros(2)))
assert sp.simplify(J.T*Om*J-g*Om)==sp.zeros(4)
assert sp.factor(J.det())==sp.Rational(1,4)
checks=2
z=sp.symbols('z')
for mat,poly in zip(D['mode_factorization']['two_step_mode_matrices'],D['mode_factorization']['two_step_mode_det_I_minus_z']):
    M=sp.Matrix([[sp.Rational(x) for x in row] for row in mat])
    got=[str(sp.factor(x)) for x in reversed(sp.Poly((sp.eye(2)-z*M).det(),z).all_coeffs())]
    assert got==poly; checks+=len(got)
full=D['certified_orbit_ledger']['period_two_rows'][0]
M=sp.Matrix([[sp.Rational(x) for x in row] for row in full['monodromy']])
assert [str(sp.factor(x)) for x in reversed(sp.Poly((sp.eye(4)-z*M).det(),z).all_coeffs())]==D['mode_factorization']['reconstructed_full_det_I_minus_z'];checks+=5
print(json.dumps({'status':'C118_SYMPY_CROSSCHECK_PASS','checks':checks},sort_keys=True))
