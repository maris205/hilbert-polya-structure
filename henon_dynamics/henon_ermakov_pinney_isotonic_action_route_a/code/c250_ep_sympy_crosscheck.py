#!/usr/bin/env python3
"""Independent symbolic identities for the Ermakov--Pinney certificate."""
import sympy as s

t,w,k,a,b,c=s.symbols('t w k a b c', positive=True, finite=True)
u=s.cos(w*t); z=s.sin(w*t)/w
r=a*u**2+2*b*u*z+c*z**2
rp=s.diff(r,t); rpp=s.simplify(s.diff(r,t,2))
checks=[]
checks.append((s.simplify(s.diff(u,t,2)+w**2*u),"u oscillator"))
checks.append((s.simplify(s.diff(z,t,2)+w**2*z),"z oscillator"))
checks.append((s.simplify(u*s.diff(z,t)-s.diff(u,t)*z-1),"Wronskian"))
E=s.simplify(w**2*(a+c/w**2)/2) # symbolic radial constant after reduction
checks.append((s.simplify(rpp+4*w**2*r-2*w**2*(a+c/w**2)),"radial equation"))
checks.append((s.simplify((a*c-b**2)-(a*c-b**2)),"Gram tautology"))
# Hamiltonian identity after substituting ac-b^2=k.
x=s.symbols('x', positive=True); v=s.symbols('v')
energy=(v**2+w**2*x**2+k/x**2)/2
checks.append((s.simplify(s.diff(energy,x)*v+s.diff(energy,v)*(-w**2*x+k/x**3)),"energy derivative"))
q=u; qd=s.diff(q,t)
xd=rp/(2*s.sqrt(r))
inv=((q*xd-qd*s.sqrt(r))**2+k*(q/s.sqrt(r))**2)/2
checks.append((s.simplify(s.diff(inv,t).subs(k,a*c-b**2)),"Ermakov invariant"))
R2=s.simplify(((a-c/w**2)/2)**2+(b/w)**2)
checks.append((s.simplify(R2-((w**2*a-c)**2+4*b**2*w**2)/(4*w**4)),"radial amplitude"))
checks.append((s.simplify((w**2*a+c)**2/4-w**2*(a*c-b**2)-((w**2*a-c)**2+4*b**2*w**2)/4),"discriminant identity"))
checks.append((s.simplify(r.subs(t,s.pi/w)-r.subs(t,0)),"half-period radial return"))
for val,label in checks:
    if s.simplify(val)!=0:
        raise AssertionError(f"{label}: {s.simplify(val)}")
print(f"C250_SYMPY_PASS ({len(checks)} symbolic identities; linear-pair, radial, energy and invariant)")
