#!/usr/bin/env python3
"""Third lane: direct symbolic matrices and 80-digit Fourier/gap checks."""
if not __debug__:
    raise RuntimeError("c379 symbolic lane refuses optimized Python")
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

def main():
    root=Path(__file__).resolve().parents[1]
    x=json.loads((root/"results/c379_multibaker_evidence.json").read_text())
    z,t,k=sp.symbols("z t k",nonzero=True)
    count=0
    for row in x["determinant_rows"]:
        L=row["L"]; P=sp.zeros(L)
        for j in range(L):
            P[j,(j+1)%L]+=t/2
            P[j,(j-1)%L]+=1/(2*t)
        actual=(sp.eye(L)-z*P).det(method="domain-ge")
        expected=sum(sp.Rational(a,b)*z**n*t**(L*w) for n,w,a,b in row["coefficients"])
        assert sp.cancel(actual-expected)==0
        cheb=sp.Rational(1,2**(L-1))*z**L*(sp.chebyshevt(L,1/z)-(t**L+t**(-L))/2)
        assert sp.cancel(actual-cheb)==0
        count+=2
    assert sp.series(sp.log(sp.cos(k)),k,0,6).removeO()==-k**2/2-k**4/12
    assert sp.diff(sp.log(sp.cosh(k)),k,2).subs(k,0)==1
    count+=2
    mp.mp.dps=80
    maximum=mp.mpf(0)
    spectral_cells=0
    for L in range(1,25):
        for phi in (mp.mpf(0),mp.pi/7,mp.pi,2*mp.pi):
            zz=mp.mpf(2)/7
            eig=[mp.cos((2*mp.pi*j+phi)/L) for j in range(L)]
            direct=mp.fprod(1-zz*a for a in eig)
            cheb=mp.power(2,1-L)*zz**L*(mp.chebyt(L,1/zz)-mp.cos(phi))
            maximum=max(maximum,abs(direct-cheb))
            assert abs(direct-cheb)<mp.mpf("1e-70")
            spectral_cells+=L
        eig=[mp.cos(2*mp.pi*j/L) for j in range(L)]
        if L>=3 and L%2:
            assert abs(max(abs(a) for a in eig[1:])-mp.cos(mp.pi/L))<mp.mpf("1e-70")
        if L%2==0:
            assert abs(eig[L//2]+1)<mp.mpf("1e-70")
            if L>=4:
                rho=max(eig[j]**2 for j in range(L) if j not in (0,L//2))
                assert abs(rho-mp.cos(2*mp.pi/L)**2)<mp.mpf("1e-70")
        if L>=2:
            assert abs(1-max((1+a)/2 for a in eig[1:])-mp.sin(mp.pi/L)**2)<mp.mpf("1e-70")
    print(f"C379 SymPy PASS: exact_identities={count} spectral_cells={spectral_cells} precision=80 max_residual_below=1e-70")

if __name__=="__main__":main()
