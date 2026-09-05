#!/usr/bin/env python3
"""Separate symbolic backend and declared finite precision audit."""
if not __debug__:
    raise RuntimeError("c393 symbolic refuses optimized Python")
import json, warnings, os
os.environ["SYMPY_GROUND_TYPES"]="python"
from pathlib import Path
import sympy as S
from sympy.utilities.exceptions import SymPyDeprecationWarning
warnings.filterwarnings("ignore",category=SymPyDeprecationWarning)
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"results/c393_arboreal_evidence.json").read_text())
x,t=S.symbols("x t");f=x;previous=[x];symbolic=0;factorizations=0
for n in range(1,5):
    f=S.expand(f*f+1)
    assert S.expand(S.diff(f,x)-2**n*S.prod(previous))==0;symbolic+=1
    previous.append(f)
    expected=(-1)**(2**n*(2**n-1)//2)*2**(n*2**n)*S.prod((d["critical_values"][i]-t)**(2**(n-i)) for i in range(1,n+1))
    assert S.expand(S.discriminant(f-t,x)-expected)==0;symbolic+=1
    types={tuple(r["lengths"]) for r in d["cycle_indices"][n]["cycle_types"]}
    for p in (3,5,7,11,13,17,19,23,29,31):
        good=len({c%p for c in d["critical_values"][:n+1]})==n+1
        for a in range(p):
            factors=S.factor_list(f-a,x,modulus=p)[1];factorizations+=1
            degrees=tuple(sorted(S.degree(poly,x) for poly,k in factors for _ in range(k)))
            assert sum(degrees)==2**n
            if good and a not in {c%p for c in d["critical_values"][1:n+1]}:
                assert all(k==1 for _,k in factors)
                assert degrees in types
            roots=sum(k for poly,k in factors if S.degree(poly,x)==1)
            direct=sum(1 for v in range(p) if int(f.subs(x,v))%p==a)
            if all(k==1 for _,k in factors):assert roots==direct
for row in d["cycle_indices"]:
    total=S.Integer(row["order"])
    assert S.Rational(*row["fixed_probability"])==sum(r["count"] for r in row["cycle_types"] if 1 in r["lengths"])/total
    symbolic+=1
print(f"C393 symbolic PASS: {symbolic} exact identities; {factorizations} independently factored residue polynomials")
