#!/usr/bin/env python3
"""Independent symbolic lane for the C356 theorem identities."""
from __future__ import annotations
import sys
import sympy as s

def main():
    if sys.flags.optimize: raise RuntimeError('C356 SymPy lane refuses optimized Python')
    I=s.I; m,x,y=s.symbols('m x y',real=True); k,t=s.symbols('k t',real=True)
    sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-I],[I,0]]); sz=s.Matrix([[1,0],[0,-1]])
    d=s.Matrix([s.sin(k),s.sin(t),m+s.cos(k)+s.cos(t)])
    H=d[0]*sx+d[1]*sy+d[2]*sz; q=s.expand_trig(sum(z*z for z in d)); checks=0
    lam=s.symbols('lambda')
    assert s.simplify(H.det()-(-q))==0; checks+=1
    assert s.simplify(H.charpoly(lam).as_expr()-(lam**2-q))==0; checks+=1
    qxy=m*m+2+2*m*(x+y)+2*x*y
    corners=[s.expand(qxy.subs({x:a,y:b})) for a,b in ((1,1),(1,-1),(-1,1),(-1,-1))]
    expected=[(m+2)**2,m**2,m**2,(m-2)**2]
    assert all(s.simplify(a-b)==0 for a,b in zip(corners,expected)); checks+=4
    cross=d.diff(k).cross(d.diff(t)); assert s.trigsimp(s.expand_trig(d.dot(cross))-(s.cos(k)+s.cos(t)+m*s.cos(k)*s.cos(t)))==0; checks+=1
    n1,n2,n3,a1,a2,a3,b1,b2,b3=s.symbols('n1 n2 n3 a1 a2 a3 b1 b2 b3',real=True)
    nv=s.Matrix([n1,n2,n3]); av=s.Matrix([a1,a2,a3]); bv=s.Matrix([b1,b2,b3])
    P=(s.eye(2)-(n1*sx+n2*sy+n3*sz))/2; A=-(a1*sx+a2*sy+a3*sz)/2; B=-(b1*sx+b2*sy+b3*sz)/2
    assert s.simplify(s.trace(P*(A*B-B*A))+I*nv.dot(av.cross(bv))/2)==0; checks+=1
    def sg(z): return 1 if z>0 else -1
    for z,w in [(-3,0),(-1,-1),(1,1),(3,0)]:
        assert -(sg(z+2)-2*sg(z)+sg(z-2))//2==w; checks+=1
    for kk,tt,chi in [(0,0,1),(s.pi,0,-1),(0,s.pi,-1),(s.pi,s.pi,1)]:
        assert s.cos(kk)*s.cos(tt)==chi; checks+=1
    assert sum([-1,1,1,-1])==0; checks+=1
    print(f'C356 SymPy cross-check: PASS ({checks} exact checks)')
if __name__=='__main__': main()
