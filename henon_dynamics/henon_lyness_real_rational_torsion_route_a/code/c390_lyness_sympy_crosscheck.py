#!/usr/bin/env python3
"""Symbolic identities plus separate 90-digit noncertifying quadrature."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c390 symbolic refuses optimized Python")
import json
from pathlib import Path
import mpmath as mp
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
def rat(v):return s.Rational(*v)
def main():
    e=json.loads((ROOT/"results/c390_lyness_evidence.json").read_text())
    x,y,a,h,r=s.symbols("x y a h r");H=(x+1)*(y+1)*(x+y+a)/(x*y)
    f=s.Matrix([y,(a+y)/x]);J=f.jacobian([x,y]);S=s.Matrix([[0,1],[1,0]])
    checks=0
    def zero(q):
        nonlocal checks
        assert s.cancel(q)==0;checks+=1
    zero(H.subs({x:y,y:(a+y)/x},simultaneous=True)-H)
    zero(J.det()/(y*(a+y)/x)-1/(x*y))
    inverse=s.Matrix([(a+x)/y,x]);assert (S*f.subs({x:y,y:x},simultaneous=True)-inverse)==s.zeros(2,1);checks+=1
    expanded=x+y+x/y+y/x+(a+1)/x+(a+1)/y+a/(x*y)+a+2;zero(H-expanded)
    zero(s.diff(H.subs({x:r,y:r}),r)-2*(r+1)*(r*r-r-a)/r**3)
    P=(x+1)*(y+1)*(x+y+a)-h*x*y;D=s.discriminant(P,y)
    B=(x+1)*(x+a+1)-h*x;zero(D-(B**2-4*(x+1)**2*(x+a)))
    residual=a*h*h-(2*a*a+10*a-1)*h+(a-2)**3
    zero(s.discriminant(D,x)-256*h**3*(a-h-1)**2*residual)
    zero(residual.subs({a:r*r-r,h:(r+1)**3/r}))
    X,Y,Z=s.symbols("X Y Z");hom=(X+Z)*(Y+Z)*(X+Y+a*Z)-h*X*Y*Z
    zero(hom.subs(Y,(h-a)*Z-X)-h*(h-a+1)*Z**3)
    f0,g0=x,y
    for _ in range(5):f0,g0=g0,s.cancel((1+g0)/f0)
    zero(f0-x);zero(g0-y)
    p=a*x-a*y+a-y*y+y
    q=-a*a*x-a*a+a*x*x*y+a*x*x-a*x*y+a*x-2*a*y+x*y-y*y
    zero(q.subs(x,(a+y)*(y-1)/a)-y*(a+y)**2*(y*y-y-a)/a)
    zero(s.resultant(p,q,x)-a*y*(a+y)**2*(y*y-y-a))
    for row in e["cycle_rows"]:
        M=s.eye(2);av=rat(row["a"])
        for point in row["cycle"]:
            xx,yy=map(rat,point);M=J.subs({a:av,x:xx,y:yy})*M
        claimed=s.Matrix([[rat(z) for z in line] for line in row["return_matrix"]]);assert M==claimed;checks+=1
        assert M.trace()==2 and M.det()==1 and (M-s.eye(2))**2==s.zeros(2);checks+=1
    mp.mp.dps=90
    def m(v):return mp.mpf(v[0])/v[1]
    assert m(e["pi_bounds"][0])<mp.pi<m(e["pi_bounds"][1]);enclosures=1
    for row in e["angle_rows"]:
        for qv,bounds in zip(row["rotation_interval"],row["endpoint_cosine_bounds"]):
            c=mp.cos(2*mp.pi*m(qv));assert m(bounds[0])<c<m(bounds[1]);enclosures+=1
    quadratures=0;worst=mp.mpf(0)
    for row in e["orbit_rows"]:
        av,rv,hv=rat(row["a"]),rat(row["r"]),rat(row["energy"])
        roots=s.nroots(D.subs({a:av,h:hv}),n=90,maxsteps=1000)
        assert all(abs(s.im(z))<s.Float("1e-80") for z in roots)
        roots=sorted(mp.mpf(str(s.re(z))) for z in roots);d0,alpha,beta,d3=roots
        rm=m(row["r"]);assert d0<alpha<rm<beta<d3
        def integrand(t):
            xx=alpha+(beta-alpha)*mp.sin(t)**2
            return 2/mp.sqrt((xx-d0)*(d3-xx))
        theta=mp.asin(mp.sqrt((rm-alpha)/(beta-alpha)))
        whole=mp.quad(integrand,[0,mp.pi/4,mp.pi/2]);part=mp.quad(integrand,[theta,(theta+mp.pi/2)/2,mp.pi/2])
        rho=part/whole;assert whole>0 and 0<rho<1
        aa=m(row["a"]);ell=(1+mp.sqrt(1+4*aa))/2;center=mp.acos(1/(2*ell))/(2*mp.pi)
        if aa==1:worst=max(worst,abs(rho-mp.mpf(1)/5));assert abs(rho-mp.mpf(1)/5)<mp.mpf("1e-70")
        else:assert min(center,mp.mpf(1)/5)<rho<max(center,mp.mpf(1)/5)
        quadratures+=1
    print(f"C390 symbolic/high-precision PASS: exact_identities={checks}; enclosure_controls={enclosures}; quadrature_controls={quadratures}; working_digits=90; a1_error_below=1e-70; quadrature_not_interval_certificate")
if __name__=="__main__":main()
