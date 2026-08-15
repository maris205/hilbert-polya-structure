#!/usr/bin/env python3
from __future__ import annotations
import itertools, json
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]

def primitive(w):
    n=len(w)
    return not any(n%d==0 and all(w[k]==w[k%d] for k in range(n)) for d in range(1,n))

def run():
    rows=[]
    for n in range(1,18,2):
        words=[]
        for h in itertools.product((0,1),repeat=(n+1)//2):
            w=h+h[:0:-1]
            if primitive(w): words.append(w)
        mean=Fraction(sum(w[(j-1)%n]==w[(j+1)%n] for w in words for j in range(n)),len(words)*n)
        rows.append({"period":n,"count":len(words),"orbit_mean":str(mean)})
    cert=json.loads((PROJECT/'results/c65_certificate.json').read_text())
    if [r['primitive_count'] for r in cert['rows'][:len(rows)]] != [r['count'] for r in rows]: raise ArithmeticError
    result={"candidate_id":"HCS-P65-INDEPENDENT","rows":rows,"check":True}
    (PROJECT/'results/c65_independent_check.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({"check":True,"rows":len(rows)},sort_keys=True))

if __name__=='__main__': run()
