#!/usr/bin/env python3
"""Fresh symbolic derivation for the HCS-C255 Suslov atlas."""
import sympy as s
I1,I2,I3,a,b,w1,w2,H,R=s.symbols("I1 I2 I3 a b w1 w2 H R", positive=True)
ell=a*w1+b*w2; f1=-ell*w2/I1; f2=ell*w1/I2
checks=[]
checks.append((s.expand(I1*w1*f1+I2*w2*f2),"energy"))
checks.append((s.expand(a*b+b*(-a)),"equilibrium direction"))
sch=I3-a**2/I1-b**2/I2
M=s.Matrix([[I1,0,a],[0,I2,b],[a,b,I3]])
checks.append((s.factor(M.det()-I1*I2*sch),"Schur determinant"))
P=-ell/(I1*I2); grad=s.Matrix([I1*w1,I2*w2]); J=s.Matrix([[0,P],[-P,0]])
checks.append((s.simplify((J*grad)[0]-f1),"Poisson omega1"))
checks.append((s.simplify((J*grad)[1]-f2),"Poisson omega2"))
checks.append((s.simplify(s.diff(f1/ell,w1)+s.diff(f2/ell,w2)),"invariant signed density"))
div=s.diff(f1,w1)+s.diff(f2,w2)
checks.append((s.simplify(div-(-a*w2/I1+b*w1/I2)),"divergence"))
checks.append((s.simplify(div.subs({w1:b,w2:-a})-(a**2/I1+b**2/I2)),"endpoint divergence"))
checks.append((s.simplify(f1.subs({w1:-w1,w2:-w2})-f1),"even vector field 1"))
checks.append((s.simplify(f2.subs({w1:-w1,w2:-w2})-f2),"even vector field 2"))
# Scaled explicit branch.  cd,sd are cosine/sine of delta and sig^2=1.
z,kappa,q,C,cd,sd,sig=s.symbols("z kappa q C cd sd sig", real=True, nonzero=True)
U=R*(cd*sig/s.cosh(z)-sd*s.tanh(z)); V=R*(sd*sig/s.cosh(z)+cd*s.tanh(z)); L=R*q*sig/s.cosh(z)
dU=s.diff(U,z)*kappa; dV=s.diff(V,z)*kappa
for sgn in (-1,1):
 checks.append((s.simplify((dU+L*V/C).subs(kappa,R*q/C).subs(sig,sgn).subs(cd**2,1-sd**2)),f"tanh branch u sigma={sgn}"))
 checks.append((s.simplify((dV-L*U/C).subs(kappa,R*q/C).subs(sig,sgn).subs(cd**2,1-sd**2)),f"tanh branch v sigma={sgn}"))
checks.append((s.simplify(s.tanh(z)**2+1/s.cosh(z)**2-1),"branch circle"))
# Endpoint nonzero eigenvalue equals divergence and its square is kappa^2.
c2=2*H/(I1*b**2+I2*a**2); q2=a**2/I1+b**2/I2; k2=2*H*q2/(I1*I2)
checks.append((s.factor(c2*q2**2-k2),"endpoint exponent squared"))
speed2=c2*(a**2+b**2)
checks.append((s.simplify((4/speed2)*speed2-4),"period coefficient"))
checks.append((s.simplify((-ell/(I1*I2)).subs({a:0,b:0})),"principal bracket"))
for value,label in checks:
 value=s.trigsimp(s.simplify(value))
 if value!=0: raise AssertionError(f"{label}: {value}")
print(f"C255_SYMPY_PASS ({len(checks)} symbolic identities; reduction, explicit branches, Poisson measure and reconstruction scales)")
