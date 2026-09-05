#!/usr/bin/env python3
"""Separate Smith/character Fourier and high-precision special-value controls."""
if not __debug__:
    raise RuntimeError("c388 sympy refuses optimized Python")
import json
from pathlib import Path
import mpmath as mp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[1]
def main():
    x=json.loads((ROOT/"results/c388_algebraic_evidence.json").read_text());mp.mp.dps=90
    for row in x["lattice_rows"]:
        A=sp.Matrix(row["matrix"]);D=smith_normal_form(A,domain=ZZ)
        assert [abs(int(D[i,i])) for i in range(A.rows)]==row["smith_diagonal"]
        assert A*A.T==A.T*A and A.rank()==row["rank"]
        a,b,c=row["hnf"];product=mp.mpc(1);zero=0
        for j in range(a):
            for k in range(c):
                z=sp.Rational(j,a);w=sp.Rational(k,c)-sp.Rational(b*j,a*c)
                # Exact congruence decides vanishing; floats never select modes.
                if (z%1,w%1) in ((sp.Rational(1,3),sp.Rational(2,3)),(sp.Rational(2,3),sp.Rational(1,3))):zero+=1;continue
                ev=1+mp.exp(2j*mp.pi*mp.mpf(str(z.evalf(95))))+mp.exp(2j*mp.pi*mp.mpf(str(w.evalf(95))))
                product*=ev
        assert zero==row["torus_dimension"]
        assert abs(abs(product)-row["nonzero_eigenvalue_product_abs"])<mp.mpf("1e-72")
    R=sp.Matrix([[0,1],[-1,-1]]);t=sp.symbols("t")
    assert R**3==sp.eye(2) and R.charpoly(t).as_expr()==t*t+t+1
    assert (sp.eye(2)-R).det()==3
    L=(mp.zeta(2,mp.mpf(1)/3)-mp.zeta(2,mp.mpf(2)/3))/9
    entropy=2/mp.pi*mp.quad(lambda u:mp.log(2*mp.cos(u)),[0,mp.pi/3])
    assert abs(entropy-3*mp.sqrt(3)/(4*mp.pi)*L)<mp.mpf("1e-80")
    for row in x["dirichlet_rows"]:
        lo=mp.mpf(row["partial_sum"][0])/row["partial_sum"][1];tail=mp.mpf(row["tail_upper"][0])/row["tail_upper"][1]
        assert lo<L<lo+tail
    print("C388 SymPy/high-precision PASS: Smith/normality/Fourier=142; torus identities=3; rational-tail controls=8; entropy="+mp.nstr(entropy,40))
if __name__=="__main__":main()
