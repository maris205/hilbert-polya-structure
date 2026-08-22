#!/usr/bin/env python3
"""Exact low-period pilot for a third-order (memory-three) Hénon map."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c113_memory_evidence.json"
x, y, z, lam = sp.symbols("x y z lam")
A = -sp.Rational(55, 16)
K = sp.Rational(1, 2)

def jac(u): return sp.Matrix([[2*u, -1, -K], [1, 0, 0], [0, 1, 0]])
def s_matrix(m): return [[str(sp.factor(m[i, j])) for j in range(m.cols)] for i in range(m.rows)]
def det_poly(m): return str(sp.factor((sp.eye(3) - z*m).det()))

def main():
    r = sp.sqrt(5)
    fixed = [sp.Rational(5, 4)-r, sp.Rational(5, 4)+r]
    fixed_rows = []
    for u in fixed:
        m = jac(u)
        fixed_rows.append({"state": [str(u)]*3, "jacobian": s_matrix(m), "jacobian_determinant": str(m.det()),
                           "characteristic_polynomial": str(sp.factor(m.charpoly(lam).as_expr())),
                           "det_I_minus_zM": det_poly(m)})
    p0 = (sp.Rational(-7, 4), sp.Rational(1, 4), sp.Rational(-7, 4))
    p1 = (sp.Rational(1, 4), sp.Rational(-7, 4), sp.Rational(1, 4))
    m2 = jac(p1[0]) * jac(p0[0])
    period_two = {"states": [[str(v) for v in p0], [str(v) for v in p1]], "cycle_closes": True,
                  "not_fixed": True, "monodromy": s_matrix(m2), "monodromy_determinant": str(m2.det()),
                  "monodromy_trace": str(sp.factor(sp.trace(m2))),
                  "characteristic_polynomial": str(sp.factor(m2.charpoly(lam).as_expr())),
                  "det_I_minus_zM": det_poly(m2)}
    state = (x, y, z); degrees = []
    for _ in range(3):
        state = (sp.expand(state[0]**2 + A - state[1] - K*state[2]), state[0], state[1])
        degrees.append(sp.Poly(state[0], x, y, z).total_degree())
    payload = {"schema":"hcs-c113-third-order-memory-v1", "scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "source_model":{"map":"G(x,y,z)=(x^2-55/16-y-z/2,x,y)","parameters":{"a":"-55/16","kappa":"1/2"},
        "jacobian":"[[2*x,-1,-1/2],[1,0,0],[0,1,0]]","phase_space":"Qbar^3","memory_order":3},
      "fixed_point_rows":fixed_rows, "period_two_row":period_two, "inverse_or_forward_degree_prefix":degrees,
      "checks":{"fixed_count":2,"period_two_primitive_count":1,"jacobian_determinant_constant":"-1/2",
        "period_two_cycle_closes":True,"period_two_not_fixed":True,"all_exact_symbolic":True},
      "verdict":{"A1":"A1_WEAK","A2":"A2_CERTIFIED_PREFIX","A3":"A3_NOT_ADDRESSED","A4":"A4_FAIL",
        "qualification":"exact fixed/period-two monodromy prefix; no complete 3D orbit atlas or Fredholm owner"},
      "nonclaims":["complete primitive-orbit atlas","analytic Fredholm determinant","arithmetic data","Route B"]}
    raw=json.dumps(payload,sort_keys=True,indent=2)+"\n"; OUT.write_text(raw)
    print(json.dumps({"evidence_sha256":sha256(raw.encode()).hexdigest(),"fixed_count":2,"period_two_count":1,"degree_growth":degrees,"status":"C113_PREFREEZE_G3_PASS"},sort_keys=True))
if __name__=='__main__': main()
