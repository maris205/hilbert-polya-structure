#!/usr/bin/env python3
"""Independent exact/trigonometric cross-check for C247."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
import json, math
from pathlib import Path
import sympy as sp
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c247_billiard_evidence.json"
def main():
    ncheck=0
    def ck(ok,label):
        nonlocal ncheck;ncheck+=1
        if not ok: raise AssertionError(label)
    a,R,m,n,k=sp.symbols('alpha R m n k', positive=True)
    # Working angle coordinate; p=sin(alpha) is only an auxiliary amplitude.
    ck(sp.diff(2*a,a)==2,'angle shift derivative')
    ck(sp.simplify(sp.sin(a)**2+sp.cos(a)**2-1)==0,'momentum circle')
    ell=2*R*sp.sin(a); ca=R*sp.cos(a)
    ck(sp.simplify(ell.subs(a,sp.pi*m/n)-2*R*sp.sin(sp.pi*m/n))==0,'chord')
    ck(sp.simplify(ca.subs(a,sp.pi*m/n)-R*sp.cos(sp.pi*m/n))==0,'caustic')
    D=sp.Matrix([[1,2],[0,1]]); Dn=sp.Matrix([[1,2*n],[0,1]])
    ck(D**n==Dn,'iterate shear')
    ck(Dn.det()==1 and (Dn-sp.eye(2)).rank()==1,'unipotent')
    ck((Dn-sp.eye(2)).nullspace()==[sp.Matrix([1,0])],'clean kernel')
    ck((sp.eye(2)-Dn).det()==0,'det obstruction')
    # A handful of exact angle/rational identities.
    for mm,nn in [(1,3),(1,4),(2,5),(3,7),(5,11)]:
        ck(math.gcd(mm,nn)==1,f'gcd {mm}/{nn}')
        ck(1<=mm<nn/2,f'fundamental range {mm}/{nn}')
        ck(sp.simplify(2*sp.pi*mm/nn-2*(sp.pi*mm/nn))==0,'rotation '+str(mm))
        cheb_expr=sp.chebyshevt(nn,sp.cos(sp.pi*mm/nn))-(-1)**mm
        ck(abs(complex(sp.N(cheb_expr,80)))<1e-60,'Chebyshev '+str(mm)+'/'+str(nn))
    # Compare every serialized row with independently evaluated trigonometry.
    d=json.loads(EVIDENCE.read_text()); mp.mp.dps=80
    for i,row in enumerate(d['regression']['primitive_rows']):
        mm,nn,sgn=row['m'],row['n'],row['orientation_sign']; aa=sgn*mp.pi*mm/nn; pp=mp.sin(aa)
        for key,val in [('alpha',aa),('p',pp),('caustic_radius',mp.cos(abs(aa))),('chord_length',2*abs(pp)),('primitive_length',2*nn*abs(pp)),('action_length',2*nn*abs(pp)),('rotation_angle',2*aa)]:
            ck(abs(mp.mpf(row[key])-val)<mp.mpf('3e-35'),f'row {i} {key}')
        ck(abs(mp.mpf(row['angle_residual']))<mp.mpf('3e-35'),f'angle residual {i}')
        ck(row['return_map_derivative']==[['1',str(2*nn)],['0','1']],f'return matrix {i}')
        ck(row['return_kernel'].startswith('ker(DB^n-I)=span'),f'kernel receipt {i}')
    # Boundary semantics are intentionally distinct from interior rows.
    b=d['regression']['boundary_rows']; ck(len(b)==2,'boundary count'); ck(all(x['return_matrix_kind']!='unipotent_shear' for x in b),'boundary split'); ck(b[0]['alpha']=='+/-pi/2' and b[0]['orientation']=='both_endpoint_equivalent','diameter endpoint merge'); ck(b[1]['alpha']=='0.0' and 'two one-sided' in b[1]['fixed_manifold'],'grazing one-sided limits')
    ids={x['identity_id'] for x in d['exact_identities']}; ck('action' in ids and 'clean_kernel' in ids and 'boundary_faces' in ids,'identity closure')
    print(f'C247_SYMPY_PASS ({ncheck} symbolic identities and numeric receipts)')
if __name__=='__main__': main()
