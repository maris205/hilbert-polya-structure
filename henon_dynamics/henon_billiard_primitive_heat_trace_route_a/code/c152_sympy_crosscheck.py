#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C152."""
from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def main():
    data=json.loads((ROOT/"results/c152_heat_evidence.json").read_text())
    checks=0
    def check(condition,message):
        nonlocal checks; checks+=1
        if not condition: raise AssertionError(message)
    cutoff=500
    direct=[0]*(cutoff+1); allrep=[0]*(cutoff+1)
    for m in range(1,isqrt(cutoff)+1):
        for n in range(1,isqrt(cutoff-m*m)+1):
            s=m*m+n*n; allrep[s]+=1
            if gcd(m,n)==1: direct[s]+=1
    for s in range(2,cutoff+1):
        transformed=sum(int(sp.mobius(d))*allrep[s//(d*d)] for d in range(1,isqrt(s)+1) if s%(d*d)==0)
        check(transformed==direct[s],f"series coefficient {s}")
    t,r=sp.symbols("t r", positive=True)
    c=sp.Rational(3,2)/sp.pi
    main_term=sp.simplify(8*t*c*sp.integrate(r**3*sp.exp(-4*t*r**2),(r,0,sp.oo)))
    check(main_term==sp.Rational(3,8)/(sp.pi*t),"Stieltjes leading term")
    check(sp.simplify(sp.Rational(6,1)/sp.pi**2 * sp.pi/4-sp.Rational(3,2)/sp.pi)==0,"primitive density")
    check(data["heat_transform_theorem"]["not_a_dirichlet_spectral_trace"] is True,"not spectral trace")
    check(data["route_a"]["route_b_invocation_allowed"] is False,"Route B")
    print(json.dumps({"status":"C152_SYMPY_PASS","checks":checks},sort_keys=True))

if __name__ == "__main__": main()
