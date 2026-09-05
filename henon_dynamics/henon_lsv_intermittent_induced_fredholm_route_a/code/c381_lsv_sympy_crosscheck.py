#!/usr/bin/env python3
"""Symbolic identities and independent 100-digit real/complex regression."""
if not __debug__:
    raise RuntimeError("c381 symbolic lane refuses optimized Python")
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

def main():
    x,w,z,a=sp.symbols("x w z a",positive=True)
    g=(sp.sqrt(1+8*x)-1)/4
    identities=[g+2*g*g-x,sp.diff(g,x)-1/(1+4*g),1/w-1/(w+2*w*w)-2/(1+2*w),(1+2*w)**2/(1+4*w)-(1+4*w*w/(1+4*w)),2/(1+2*w)-(2-4*w/(1+2*w)),(1-z)/(1-2*z)-1/(1-z/(1-z)),a/(1-a)-a*(1+a+a*a)-a**4/(1-a),sp.Rational(1,2)/sp.Rational(3,4)-sp.Rational(2,3)]
    for expr in identities:assert sp.simplify(expr)==0
    root=Path(__file__).resolve().parents[1]
    data=json.loads((root/"results/c381_lsv_evidence.json").read_text())
    mp.mp.dps=100
    def inv(v):return (mp.sqrt(1+8*v)-1)/4
    real_checks=0
    for row in data["periodic_rows"]+data["induced_rows"]:
        word=row["word"]
        if set(word)=={"0"}:v=mp.mpf(0)
        elif set(word)=={"1"}:v=mp.mpf(1)
        else:
            v=mp.mpf("0.6")
            for _ in range(400):
                for bit in reversed(word):v=inv(v) if bit=="0" else (1+v)/2
        lo,hi=[mp.mpf(t)/mp.mpf(2)**160 for t in row["point_bounds"]]
        assert lo-mp.mpf("1e-95")<=v<=hi+mp.mpf("1e-95")
        mult=mp.mpf(1);p=v
        for bit in word:
            if bit=="0":mult*=1+4*p;p=p+2*p*p
            else:mult*=2;p=2*p-1
        low,high=[mp.mpf(t)/mp.mpf(2)**80 for t in row["multiplier_bounds"]]
        assert low-mp.mpf("1e-90")<=mult<=high+mp.mpf("1e-90")
        real_checks+=1
    cells=0
    for radius in (mp.mpf(3)/8,mp.mpf(3)/4):
        for j in range(16):
            start=1+radius*mp.exp(2j*mp.pi*j/16);v=start;der=mp.mpf(1);correction=mp.mpf(1)
            for m in range(1,129):
                v=inv(v);der/=1+4*v
                correction*=1+4*v*v/(1+4*v)
                telescope=(v/start)**2*correction
                assert abs(der-telescope)<mp.mpf("1e-90")
                assert mp.re(1/v)>=mp.mpf(4)/7+mp.mpf(2)*m/25-mp.mpf("1e-90")
                assert abs((1+v)/2-1)<mp.mpf(1)/2
                assert abs(v)<=mp.mpf(25)/(2*(m+1))
                assert abs(der)/2*(m+1)**2<1250*mp.exp(625*mp.pi**2/6)
                cells+=1
    for denominator in range(8,129):
        eps=mp.mpf(1)/denominator
        defect=2*(1-inv(eps)/eps)
        assert 0<defect<=4*eps
    print(f"C381 symbolic/high-precision PASS: exact_identities={len(identities)} real_certificates={real_checks} complex_cells={cells} defect_cells=121 precision=100 telescope_residual_below=1e-90")

if __name__=="__main__":main()
