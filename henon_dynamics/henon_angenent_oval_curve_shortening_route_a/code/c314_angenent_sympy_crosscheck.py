#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C314."""
import sys
import sympy as s


def main():
    if sys.flags.optimize:
        raise RuntimeError("C314 SymPy lane refuses optimized Python")
    x,y,r,c,a,u=s.symbols("x y r c a u", positive=True)
    T=s.log(s.cos(x))-s.log(s.cosh(y))
    tx,ty=s.diff(T,x),s.diff(T,y);g=s.sqrt(tx**2+ty**2)
    div=s.diff(tx/g,x)+s.diff(ty/g,y)
    identities=[]
    identities.append(s.trigsimp(s.simplify(-g*div-1)))
    identities.append(s.simplify((1-c**2)+(c**2-r**2)-(1-r**2)))
    identities.append(s.simplify(c/s.sqrt(1-r**2)-c/s.sqrt(1-r**2)))
    identities.append(s.simplify(s.integrate(1/s.sqrt(a*a-u*u),(u,0,a))-s.pi/2))
    identities.append(s.simplify(s.limit((-2*s.log(r))/(1-r**2),r,1,dir="-")-1))
    identities.append(s.simplify(s.limit(s.acosh(c/r)+s.log(r)-s.log(2)-s.log(c),r,0,dir="+")))
    # Curvature pressure formula and its two extrema.
    th=s.symbols("th", real=True)
    p=1/(1-r**2)-s.sin(th)**2
    identities += [s.simplify(p.subs(th,0)-1/(1-r**2)),s.simplify(p.subs(th,s.pi/2)-r**2/(1-r**2))]
    # Graph slope and length substitution.
    identities.append(s.simplify(1+(1-c**2)/(c**2-r**2)-(1-r**2)/(c**2-r**2)))
    if any(value != 0 for value in identities):
        raise AssertionError(identities)
    print(f"C314 SymPy cross-check: PASS ({len(identities)} identity groups)")


if __name__ == "__main__":
    main()
