#!/usr/bin/env python3
"""Independent semantic checker for C118; never imports the producer."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
E = ROOT / "results/c118_damped_dimer_evidence.json"
A, G, K = sp.Rational(13,2), sp.Rational(1,2), sp.Rational(1,4)
L = sp.Matrix([[1,-1],[-1,1]])


def canonical(x: object) -> bytes:
    return (json.dumps(x, sort_keys=True, separators=(",", ":")) + "\n").encode()


def ms(m: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(m[i,j])) for j in range(m.cols)] for i in range(m.rows)]


def vs(v: sp.Matrix) -> list[str]:
    return [str(sp.factor(x)) for x in v]


def grad(q: sp.Matrix, k: sp.Rational = K) -> sp.Matrix:
    return sp.Matrix([A*q[i]-q[i]**2 for i in range(2)])-k*L*q


def f(s: sp.Matrix, k: sp.Rational = K) -> sp.Matrix:
    return (grad(s[:2,:], k)-G*s[2:,:]).col_join(s[:2,:])


def inv(s: sp.Matrix, k: sp.Rational = K) -> sp.Matrix:
    return s[2:,:].col_join((grad(s[2:,:], k)-s[:2,:])/G)


def jac(q: sp.Matrix, k: sp.Rational = K) -> sp.Matrix:
    h = sp.diag(*[A-2*q[i] for i in range(2)])-k*L
    return h.row_join(-G*sp.eye(2)).col_join(sp.eye(2).row_join(sp.zeros(2)))


def dp(m: sp.Matrix) -> list[str]:
    z=sp.symbols('z'); p=sp.Poly((sp.eye(m.rows)-z*m).det(),z)
    return [str(sp.factor(x)) for x in reversed(p.all_coeffs())]


def check_row(row: dict[str, object], states: list[sp.Matrix], k: sp.Rational = K) -> sp.Matrix:
    assert row["states"] == [vs(s) for s in states]
    assert row["period"] == len(states)
    assert row["cycle_closes"] is (f(states[-1], k)==states[0])
    assert row["primitive"] is (len(states)==1 or states[0]!=states[1])
    m=sp.eye(4)
    for s in states: m=jac(s[:2,:],k)*m
    assert row["monodromy"]==ms(m)
    assert row["monodromy_trace"]==str(sp.factor(sp.trace(m)))
    assert row["monodromy_determinant"]==str(sp.factor(m.det()))
    assert row["det_I_minus_z_monodromy"]==dp(m)
    return m


def validate(path: Path=E) -> dict[str,object]:
    raw=path.read_bytes(); d=json.loads(raw); assert raw==canonical(d)
    assert d["schema_id"]=="hcs-c118-conformally-symplectic-damped-henon-dimer-prefreeze-v1"
    assert d["status"]=="PREFREEZE_G3_PASS" and d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    assert d["source_model"]["parameters"]=={"a":"13/2","gamma":"1/2","kappa":"1/4","sites":2}
    structural=d["structural_checks"]
    assert structural["expected_jacobian_determinant"]=="1/4"
    assert structural["conformal_symplectic_on_five_exact_samples"] is True
    assert structural["inverse_two_sided_on_two_exact_samples"] is True
    assert structural["exact_one_form_identity_symbolic"] is True
    assert structural["jacobian_determinant_on_five_exact_samples"]==["1/4"]*5
    om=sp.zeros(2).row_join(sp.eye(2)).col_join((-sp.eye(2)).row_join(sp.zeros(2)))
    for q in [sp.Matrix([0,0]),sp.Matrix([5,5]),sp.Matrix([2,2]),sp.Matrix([6,6]),sp.Matrix([sp.Rational(1,3),sp.Rational(-2,5)])]:
        j=jac(q); assert sp.simplify(j.T*om*j-G*om)==sp.zeros(4); assert j.det()==sp.Rational(1,4)
    for s in [sp.Matrix([sp.Rational(1,3),sp.Rational(-2,5),sp.Rational(2,7),sp.Rational(3,8)]),sp.Matrix([2,1,-1,sp.Rational(4,3)])]:
        assert inv(f(s))==s and f(inv(s))==s
    fixed=d["certified_orbit_ledger"]["fixed_rows"]
    check_row(fixed[0],[sp.zeros(4,1)]); check_row(fixed[1],[sp.Matrix([5,5,5,5])])
    cycle=d["certified_orbit_ledger"]["period_two_rows"][0]
    cstates=[sp.Matrix([2,2,6,6]),sp.Matrix([6,6,2,2])]
    direct=check_row(cycle,cstates)
    mode=d["mode_factorization"]
    assert mode["laplacian_eigenvalues"]==["0","2"]
    assert mode["hessian_at_q2"]==["5/2","2"] and mode["hessian_at_q6"]==["-11/2","-6"]
    mats=[]
    for u,v in [(sp.Rational(5,2),sp.Rational(-11,2)),(sp.Rational(2),sp.Rational(-6))]:
        mats.append(sp.Matrix([[v,-G],[1,0]])*sp.Matrix([[u,-G],[1,0]]))
    assert mode["two_step_mode_matrices"]==[ms(x) for x in mats]
    assert mode["two_step_mode_traces"]==["-59/4","-13"]
    assert mode["two_step_mode_determinants"]==["1/4","1/4"]
    z=sp.symbols('z'); rec=sp.expand((sp.eye(2)-z*mats[0]).det()*(sp.eye(2)-z*mats[1]).det())
    coeff=[str(sp.factor(x)) for x in reversed(sp.Poly(rec,z).all_coeffs())]
    assert coeff==mode["reconstructed_full_det_I_minus_z"]==dp(direct)
    unc=check_row({"label":"u","period":2,"states":[vs(s) for s in cstates],"cycle_closes":True,"primitive":True,"monodromy":d["uncoupled_control"]["period_two_monodromy"],"monodromy_trace":d["uncoupled_control"]["trace"],"monodromy_determinant":"1/16","det_I_minus_z_monodromy":d["uncoupled_control"]["det_I_minus_z"]},cstates,sp.Rational(0))
    assert str(sp.factor(sp.trace(direct)-sp.trace(unc)))=="7/4"==d["uncoupled_control"]["coupled_minus_uncoupled_trace"]
    assert d["route_a_verdict"]["A2"]=="A2_FAIL"
    for key in ("complete_orbit_atlas","fredholm_or_nuclear_transfer_owner","arithmetic_local_data","euler_factors","root_numbers","automorphy","hilbert_polya_operator","route_b_authorized"):
        assert d["claims"][key] is False
    return d


if __name__=="__main__":
    validate(); print(json.dumps({"status":"C118_INDEPENDENT_CHECK_PASS","fixed_count":2,"period_two_count":1},sort_keys=True))
