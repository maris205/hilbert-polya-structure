#!/usr/bin/env python3
"""Fresh SymPy derivation for HCS-C254."""
import sympy as s
S,X,D,Sin,mumax,K,Y,x,xs=s.symbols("S X D S_in mu_max K Y x x_star", positive=True)
mu=lambda z:mumax*z/(K+z)
Sd=D*(Sin-S)-mu(S)*X/Y; Xd=(mu(S)-D)*X; Q=S+X/Y
Sstar=D*K/(mumax-D); xstar=Sin-Sstar; A=mumax-D
checks=[]
checks.append((s.simplify(Sd+Xd/Y-D*(Sin-Q)),"total nutrient"))
checks.append((s.factor(mu(Sin)-D-(mumax*Sin-D*(K+Sin))/(K+Sin)),"threshold"))
checks.append((s.factor(mu(Sstar)-D),"break even"))
checks.append((s.simplify(Y*(Sin-Sstar)-Y*xstar),"positive equilibrium"))
checks.append((s.simplify(s.diff(mu(S),S)-mumax*K/(K+S)**2),"Monod derivative"))
J0=s.Matrix([[s.diff(Sd,S),s.diff(Sd,X)],[s.diff(Xd,S),s.diff(Xd,X)]]).subs({S:Sin,X:0})
z=s.symbols("z")
checks.append((s.factor(J0.charpoly(z).as_expr()-(z+D)*(z-(mu(Sin)-D))),"washout spectrum"))
rate=xstar*mumax*K/(K+Sstar)**2
Jqx=s.Matrix([[-D,0],[xstar*mumax*K/(K+Sstar)**2,-rate]])
checks.append((s.factor(Jqx.charpoly(z).as_expr()-(z+D)*(z+rate)),"survival spectrum"))
leaf=A*x*(xs-x)/(K+Sin-x); c=(K+Sin)/xs; d=(K+Sin-xs)/xs
primitive=c*s.log(x)-d*s.log(xs-x)
checks.append((s.simplify(s.diff(primitive,x)*leaf-A),"leaf logarithmic law"))
critical=-A*x**2/(K+Sin-x); crit=(K+Sin)/x+s.log(x)
checks.append((s.simplify(s.diff(crit,x)*critical-A),"critical law"))
checks.append((s.simplify((K+Sin)/A-1/(mumax*K/(K+Sin)**2)).subs(D,mumax*Sin/(K+Sin)),"critical coefficient"))
checks.append((s.simplify(mu(0)),"zero substrate"))
checks.append((s.simplify(Sd.subs(S,0)-D*Sin),"substrate boundary"))
checks.append((s.simplify(Xd.subs(X,0)),"biomass boundary"))
checks.append((s.factor(s.diff(mu(S),S,2)+2*mumax*K/(K+S)**3),"concavity formula"))
for value,label in checks:
 if s.simplify(value)!=0: raise AssertionError(f"{label}: {s.simplify(value)}")
print(f"C254_SYMPY_PASS ({len(checks)} symbolic identities; reduction, threshold, spectra and exact transients)")
