#!/usr/bin/env python3
"""Exact symbolic identities; no numerical orbit fit is used."""
import sys
import sympy as S

def main():
    if sys.flags.optimize:raise RuntimeError('C387 sympy refuses optimized Python')
    checks=0
    def zero(v):
        nonlocal checks
        checks+=1
        if S.simplify(S.expand(v))!=0:raise ValueError('symbolic mismatch '+str(v))
    x,y,z,b,c,t,s,u=S.symbols('x y z b c t s u',real=True)
    p,q,d,n,j,m=S.symbols('p q d n j m',integer=True)
    def flow(a,time):
        xx,yy,zz=a;return S.Matrix([xx+time,yy+b*time,zz+c*time+b*xx*time+b*time**2/2])
    def rev(a):
        xx,yy,zz=a;return S.Matrix([-xx,-yy+2*c,zz-2*c*xx])
    a=S.Matrix([x,y,z])
    for v in flow(flow(a,t),s)-flow(a,t+s):zero(v)
    for v in rev(rev(a))-a:zero(v)
    for v in rev(flow(rev(a),t))-flow(a,-t):zero(v)
    theta=c*q+p*x-q*y+p*q/2
    central=(c*t+b*x*t+b*t*t/2-t*y).subs({b:p/q,t:d*q})
    zero(central-d*theta-p*q*d*(d-1)/2)
    zero(S.diff(theta,x)+p/q*S.diff(theta,y))
    mat=S.Matrix([[1,0,0],[0,1,0],[b*t,-t,1]])
    zero(mat.det()-1);zero((mat-S.eye(3)).det())
    zero(((mat-S.eye(3))**2).norm())
    shifted=S.Matrix([y+n*b,z-n*y+n*c-b*n*n/2])
    step=S.Matrix([shifted[0]+b,shifted[1]-shifted[0]+c-b/2])
    for v in step-shifted.subs(n,n+1):zero(v)
    # Exact residue relabeling k=j+m*ell and the lattice phase cancellation.
    ell,r,ss,k=S.symbols('ell r ss k',integer=True)
    zero(m*r*y+(j+m*(ell-r))*(y+ss)-(j+m*ell)*y-(j+m*(ell-r))*ss)
    psi=S.pi*b*m*u*u+2*S.pi*(b*j+c*m)*u
    potential=2*S.pi*(b*m*u+b*j+c*m)
    zero(S.diff(psi,u)-potential)
    g=S.Function('g')(u);chirp=S.exp(-S.I*psi)
    zero(-S.I*S.diff(chirp*g,u)+potential*chirp*g-chirp*(-S.I*S.diff(g,u)))
    # Finite signed-mode specializations independently exercise signs and zero slope.
    for mm in list(range(-6,0))+list(range(1,7)):
        for jj in range(abs(mm)):
            for bb in [S.Rational(-3,2),S.Rational(0),S.Rational(2,3)]:
                zero((S.diff(psi,u)-potential).subs({m:mm,j:jj,b:bb,c:S.Rational(5,7)}))
                zero((psi.subs(u,u+1)-psi-S.pi*b*m*(2*u+1)-2*S.pi*(b*j+c*m)).subs({m:mm,j:jj,b:bb}))
    print('C387_SYMPY_PASS exact_identities='+str(checks)+' signed_modes=true generic_parameters=true')

if __name__=='__main__':main()
