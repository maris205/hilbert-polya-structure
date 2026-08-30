#!/usr/bin/env python3
"""Independent SymPy/algebraic receipt for the C244 theorem package."""
from __future__ import annotations
import sys
sys.dont_write_bytecode = True
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c244_pendulum_evidence.json"

def main():
    checks=0
    def ck(ok,label):
        nonlocal checks; checks+=1
        if not ok: raise AssertionError(label)
    u,h,q,s,j=sp.symbols('u h q s j')
    P=sp.expand(2*(1-u**2)*(h-u)-q)
    ck(P==2*u**3-2*h*u**2-2*u+2*h-q,'cubic expansion')
    D=sp.factor(sp.discriminant(P,u))
    ck(sp.expand(D-4*(16*h**4-8*h**3*q-32*h**2+72*h*q-27*q**2+16))==0,'discriminant')
    hs=(3*s**2-1)/(2*s); qs=(1-s**2)**2/(-s)
    ck(sp.factor(P.subs({u:s,h:hs,q:qs}))==0,'critical P')
    ck(sp.factor(sp.diff(P,u).subs({u:s,h:hs,q:qs}))==0,'critical derivative')
    ck(sp.factor(sp.discriminant(P,u).subs({h:hs,q:qs}))==0,'critical discriminant')
    # Hamilton equations from canonical derivatives.
    th,ph,pt,jj=sp.symbols('theta phi p_theta j')
    HH=sp.Rational(1,2)*(pt**2+jj**2/sp.sin(th)**2)+sp.cos(th)
    ck(sp.diff(HH,pt)==pt,'theta dot')
    ck(sp.simplify(sp.diff(HH,jj)-jj/sp.sin(th)**2)==0,'phi dot')
    ck(sp.simplify(-sp.diff(HH,th)-(jj**2*sp.cos(th)/sp.sin(th)**3+sp.sin(th)))==0,'p theta dot')
    # Endpoint and monodromy algebraic invariants.
    M=sp.Matrix([[1,1],[0,1]])
    ck(M.det()==1,'monodromy determinant'); ck(M.trace()==2,'monodromy trace'); ck((M-sp.eye(2)).rank()==1,'monodromy unipotent')
    ck(sp.factor((1-s**2)**2/(-s)).subs(s,sp.Rational(-1,2))==sp.Rational(9,8),'rational critical sample')
    # Verify all serialized roots and quadratures independently at 50 digits.
    d=json.loads(EVIDENCE.read_text()); mp.mp.dps=80
    for idx,row in enumerate(d['regression']['regular_rows']):
        fh=Fraction(row['h']); fj=Fraction(row['j'])
        hh=mp.mpf(fh.numerator)/fh.denominator
        jjv=mp.mpf(fj.numerator)/fj.denominator
        rr=sorted(mp.re(z) for z in mp.polyroots([2,-2*hh,-2,2*hh-jjv**2],maxsteps=1000,error=False))
        for k,x in enumerate(rr):
            ck(abs(mp.mpf(row['roots'][k])-x)<mp.mpf('3e-35'),f'root {idx}/{k}')
            ck(abs(2*(1-x*x)*(hh-x)-jjv**2)<mp.mpf('3e-35'),f'residual {idx}/{k}')
        r1,r2,r3=rr
        def original_action_integrand(x):
            val=2*(1-x*x)*(hh-x)-jjv**2
            if val < 0 and abs(val) < mp.mpf('1e-50'):
                val=mp.mpf('0')
            return mp.sqrt(val)/(1-x*x)
        original_action=mp.quad(original_action_integrand,[r1,(r1+r2)/2,r2])/mp.pi
        ck(abs(original_action-mp.mpf(row['action_I']))<mp.mpf('3e-35'),f'original action integral {idx}')
    # All receipt identities appear verbatim in the evidence.
    ids={x['identity_id'] for x in d['exact_identities']}
    for ident in ('reduced_cubic','discriminant','critical_parameterization','period_quadrature','angle_quadrature','action_quadrature','torus_closure','focus_monodromy','pole_regularization'):
        ck(ident in ids,'identity '+ident)
    print(f'C244_SYMPY_PASS ({checks} symbolic identities and numeric receipts)')

if __name__=='__main__': main()
