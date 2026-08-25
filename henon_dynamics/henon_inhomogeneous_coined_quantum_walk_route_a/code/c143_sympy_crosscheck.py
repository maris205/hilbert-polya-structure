#!/usr/bin/env python3
"""Separate SymPy reconstruction of the C143 walk identities."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


ROOT=Path(__file__).resolve().parents[1]


def build(word):
    coins={'0':sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5)],[sp.Rational(4,5),-sp.Rational(3,5)]]),'1':sp.Matrix([[sp.Rational(5,13),sp.Rational(12,13)],[sp.Rational(12,13),-sp.Rational(5,13)]])}
    c=sp.zeros(10);s=sp.zeros(10)
    for x,ch in enumerate(word):
        c[2*x:2*x+2,2*x:2*x+2]=coins[ch]
        s[2*((x+1)%5)+1,2*x]=1;s[2*((x-1)%5),2*x+1]=1
    return s,c,s*c


def main():
    data=json.loads((ROOT/'results/c143_quantum_walk_evidence.json').read_text());z=sp.symbols('z');checks=0;polys={}
    for word in ('00011','00101'):
        s,c,u=build(word)
        assert s**2==sp.eye(10);checks+=1
        assert c**2==sp.eye(10);checks+=1
        assert u.T*u==sp.eye(10);checks+=1
        assert c*u*c==u.inv();checks+=1
        poly=sp.Poly((sp.eye(10)-z*u).det(),z);polys[word]=poly.as_expr();checks+=1
        listed=[sp.Rational(x) for x in data['arrangement_control']['determinant_polynomials_ascending'][word]]
        assert sp.expand(poly.as_expr()-sum(listed[k]*z**k for k in range(11)))==0;checks+=1
        for n in range(1,13):
            assert sp.trace(u**n)==sp.Rational(data['trace_ledgers'][word][n-1]['trace_Un']);checks+=1
    assert sp.factor(polys['00011']-polys['00101'])==sp.Rational(196,4225)*z**2*(z-1)**2*(z+1)**2*(z**2+1);checks+=1
    c0=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5)],[sp.Rational(4,5),-sp.Rational(3,5)]])
    c1=sp.Matrix([[sp.Rational(5,13),sp.Rational(12,13)],[sp.Rational(12,13),-sp.Rational(5,13)]])
    cb=(3*c0+2*c1)/5
    assert cb.T*cb-sp.eye(2)==-sp.Rational(24,1625)*sp.eye(2);checks+=1
    assert cb.det()==-sp.Rational(1601,1625);checks+=1
    print(json.dumps({'status':'PASS','sympy_checks':checks},sort_keys=True))


if __name__=='__main__':main()
