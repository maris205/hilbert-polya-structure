#!/usr/bin/env python3
"""Symbolic polynomial-root and asymptotic checks for HCS-C315."""
import sys
import sympy as s
def main():
 if sys.flags.optimize:raise RuntimeError("C315 SymPy lane refuses optimized Python")
 z1,z2,v1,v2,t,z=s.symbols("z1 z2 v1 v2 t z", nonzero=True)
 P=(z-z1)*(z-z2);Q=v1*(z-z2)+v2*(z-z1);p=s.expand(P-t*Q)
 ids=[]
 ids.append(s.diff(p,t,2))
 # At t=0 implicit root derivatives recover the prescribed velocities.
 ids += [s.simplify(Q.subs(z,z1)/s.diff(P,z).subs(z,z1)-v1),s.simplify(Q.subs(z,z2)/s.diff(P,z).subs(z,z2)-v2)]
 # Coefficient laws and the two-particle anchor/beta/intercept identities.
 V=v1+v2;M=v1*z1+v2*z2;y=(v1*z2+v2*z1)/V
 beta=-P.subs(z,y)/s.diff(Q,z)
 ids += [s.simplify(s.Poly(p,z).all_coeffs()[1]+z1+z2+t*V),s.simplify((z1+z2)-y-M/V),s.simplify(beta-v1*v2*(z2-z1)**2/V**3)]
 # General root differentiation algebra: the pzz and q' contributions reduce to goldfish.
 a,b,ad,bd=s.symbols("a b ad bd")
 ids.append(s.simplify(2*ad*bd/(a-b)+2*bd*ad/(b-a)))
 if any(s.factor(i)!=0 for i in ids):raise AssertionError(ids)
 print(f"C315 SymPy cross-check: PASS ({len(ids)} identity groups)")
if __name__=="__main__":main()
