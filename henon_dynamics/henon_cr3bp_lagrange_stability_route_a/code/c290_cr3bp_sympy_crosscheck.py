#!/usr/bin/env python3
"""Independent symbolic differentiation and spectral reconstruction for C290."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/c290_cr3bp_evidence.json"


def main() -> None:
    data = json.loads(DATA.read_text())
    x, y, mu = s.symbols("x y mu", real=True)
    lam = s.Symbol("z")
    r1sq=(x+mu)**2+y**2; r2sq=(x-1+mu)**2+y**2
    Omega=(x**2+y**2)/2+(1-mu)/s.sqrt(r1sq)+mu/s.sqrt(r2sq)
    Ox=s.diff(Omega,x); Oy=s.diff(Omega,y)
    xt=s.Rational(1,2)-mu; yt=s.sqrt(3)/2
    H=s.simplify(s.hessian(Omega,(x,y)).subs({x:xt,y:yt}))
    Hminus=s.simplify(s.hessian(Omega,(x,y)).subs({x:xt,y:-yt}))
    expected=s.Matrix([[s.Rational(3,4),3*s.sqrt(3)*(1-2*mu)/4],[3*s.sqrt(3)*(1-2*mu)/4,s.Rational(9,4)]])
    expected_minus=s.Matrix([[s.Rational(3,4),-3*s.sqrt(3)*(1-2*mu)/4],[-3*s.sqrt(3)*(1-2*mu)/4,s.Rational(9,4)]])
    M=s.Matrix([[0,0,1,0],[0,0,0,1],[H[0,0],H[0,1],0,2],[H[1,0],H[1,1],-2,0]])
    Mminus=s.Matrix([[0,0,1,0],[0,0,0,1],[Hminus[0,0],Hminus[0,1],0,2],[Hminus[1,0],Hminus[1,1],-2,0]])
    target=lam**4+lam**2+s.Rational(27,4)*mu*(1-mu)
    u,w=s.symbols("u w", positive=True)
    abstract_Ox=x-(1-mu)*(x+mu)*u-mu*(x-1+mu)*w
    S=(1-mu)*u+mu*w
    checks=[
        s.simplify(Oy-y*(1-(1-mu)/r1sq**s.Rational(3,2)-mu/r2sq**s.Rational(3,2)))==0,
        s.simplify(abstract_Ox-x*(1-S)-mu*(1-mu)*(w-u))==0,
        H==expected,
        s.simplify(Hminus-expected_minus)==s.zeros(2),
        s.simplify(M.charpoly(lam).as_expr()-target)==0,
        s.simplify(Mminus.charpoly(lam).as_expr()-target)==0,
        s.simplify(H.trace()-3)==0,
        s.simplify(H.det()-s.Rational(27,4)*mu*(1-mu))==0,
        s.simplify(Hminus.det()-s.Rational(27,4)*mu*(1-mu))==0,
    ]
    ss=s.symbols("S", positive=True)
    Mc=s.Matrix([[0,0,1,0],[0,0,0,1],[1+2*ss,0,0,2],[0,1-ss,-2,0]])
    coltarget=lam**4+(2-ss)*lam**2+(1+ss-2*ss**2)
    checks.append(s.simplify(Mc.charpoly(lam).as_expr()-coltarget)==0)
    muR=(1-s.sqrt(s.Rational(23,27)))/2
    MR=s.simplify(M.subs(mu,muR)); MRminus=s.simplify(Mminus.subs(mu,muR)); critical=(lam**2+s.Rational(1,2))**2
    checks.extend([
        s.simplify(27*muR*(1-muR)-1)==0,
        s.simplify(MR.charpoly(lam).as_expr()-critical)==0,
        s.simplify(MRminus.charpoly(lam).as_expr()-critical)==0,
    ])
    expected_rank_cells=[]
    for point,sign,matrix in (("L4",1,MR),("L5",-1,MRminus)):
        for eigenvalue,ev in (("-i/sqrt(2)",-s.I/s.sqrt(2)),("i/sqrt(2)",s.I/s.sqrt(2))):
            rank=(matrix-ev*s.eye(4)).rank()
            checks.extend([rank==3,4-rank==1])
            expected_rank_cells.append({"point":point,"mixed_hessian_sign":sign,"eigenvalue":eigenvalue,"matrix_rank":rank,"geometric_multiplicity":4-rank})
    checks.append(data["critical_cell"]["rank_cells"]==expected_rank_cells)
    for row in data["triangular_cells"]:
        m=s.Rational(row["mu"]); rr=27*m*(1-m)
        checks.extend([s.Rational(row["routh_parameter"])==rr,s.Rational(row["charpoly_constant"])==rr/4,s.Rational(row["routh_discriminant"])==1-rr])
    assert all(checks)
    print(f"C290_SYMPY_PASS ({len(checks)} symbolic checks; differentiated potential and raw 4x4 Jacobian)")


if __name__ == "__main__": main()
