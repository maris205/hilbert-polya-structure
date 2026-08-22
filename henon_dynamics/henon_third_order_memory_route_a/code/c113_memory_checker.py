#!/usr/bin/env python3
"""Independent symbolic checker for C113."""
import json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]; d=json.loads((ROOT/"results/c113_memory_evidence.json").read_text())
x,y,z,lam=sp.symbols('x y z lam'); a=-sp.Rational(55,16); k=sp.Rational(1,2)
G=(x*x+a-y-k*z,x,y)
fixed=sp.solve([G[i]-[x,y,z][i] for i in range(3)],[x,y,z],dict=True)
assert len(fixed)==2
expected=[sp.Rational(5,4)-sp.sqrt(5),sp.Rational(5,4)+sp.sqrt(5)]
got=sorted([sp.simplify(q[x]) for q in fixed],key=str); assert all(sp.simplify(g-e)==0 for g,e in zip(got,sorted(expected,key=str)))
J=lambda u:sp.Matrix([[2*u,-1,-k],[1,0,0],[0,1,0]])
for row,u in zip(d["fixed_point_rows"],expected):
    m=J(u); assert sp.simplify(m.det()+sp.Rational(1,2))==0
    assert sp.simplify(sp.sympify(row["det_I_minus_zM"])-(sp.eye(3)-z*m).det())==0
p0=(sp.Rational(-7,4),sp.Rational(1,4),sp.Rational(-7,4)); p1=(sp.Rational(1,4),sp.Rational(-7,4),sp.Rational(1,4))
image=tuple(sp.simplify(G[i].subs({x:p0[0],y:p0[1],z:p0[2]})) for i in range(3)); assert image==p1
back=tuple(sp.simplify(G[i].subs({x:p1[0],y:p1[1],z:p1[2]})) for i in range(3)); assert back==p0
m2=J(p1[0])*J(p0[0]); row=d["period_two_row"]
assert sp.simplify(m2.det()-sp.Rational(1,4))==0 and sp.simplify(m2.trace()+sp.Rational(15,4))==0
assert sp.simplify(sp.sympify(row["det_I_minus_zM"])-(sp.eye(3)-z*m2).det())==0
assert d["verdict"]["A1"]=="A1_WEAK" and d["verdict"]["A2"]=="A2_CERTIFIED_PREFIX"
print("C113_CHECK_PASS")
