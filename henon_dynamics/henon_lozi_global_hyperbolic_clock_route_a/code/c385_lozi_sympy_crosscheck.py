#!/usr/bin/env python3
"""Independent symbolic cone, recurrence and high-precision multiplier checks."""
if not __debug__:
    raise RuntimeError("c385 symbolic refuses optimized Python")
import json
from pathlib import Path
import sympy as S
import mpmath as mp

def main():
    a=S.symbols("a",positive=True);r=S.symbols("r",positive=True);z=S.symbols("z")
    checks=0
    for s in (-1,1):
        A=S.Matrix([[-a*s,-1],[1,0]]);J=S.Matrix([[0,1],[1,0]])
        assert A.det()==1 and J*A*J==A.inv();checks+=2
        assert S.simplify(S.diff(1/(-a*s-z),z)-1/(a*s+z)**2)==0;checks+=1
    rr=(a-S.sqrt(a*a-4))/2
    assert S.simplify(rr*(a-rr)-1)==0;checks+=1
    # Cayley-Hamilton repetition with symbolic trace, distinct from orbit solve.
    t=S.symbols("t");M=S.Matrix([[t,-1],[1,0]])
    prev,cur=S.Integer(2),t
    for k in range(1,13):
        assert S.expand(S.trace(M**k)-cur)==0;checks+=1
        prev,cur=cur,S.expand(t*cur-prev)
    mp.mp.dps=80
    data=json.loads((Path(__file__).resolve().parents[1]/"results/c385_lozi_evidence.json").read_text())
    max_error=mp.mpf(0)
    for row in data["rows"]:
        aa=mp.mpf(row["a"][0])/row["a"][1]
        rad=(aa-mp.sqrt(aa*aa-4))/2
        tr=mp.mpf(row["trace"][0])/row["trace"][1]
        lam=(tr+mp.sign(tr)*mp.sqrt(tr*tr-4))/2
        assert mp.sign(lam)==row["unstable_sign"]
        assert abs(lam)>=rad**(-row["n"])*(1-mp.mpf("1e-70"))
        den=abs((1-lam)*(1-1/lam))
        wanted=mp.mpf(row["flat_denominator"][0])/row["flat_denominator"][1]
        err=abs(den-wanted)/(1+wanted);max_error=max(max_error,err)
        assert err<mp.mpf("1e-70")
    print(f"C385 symbolic PASS: {checks} identities; {len(data['rows'])} multiplier cells at 80 digits; max relative defect={mp.nstr(max_error,6)}")
if __name__=="__main__":main()
