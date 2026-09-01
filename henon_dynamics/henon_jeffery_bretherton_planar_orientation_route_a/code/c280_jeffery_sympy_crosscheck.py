#!/usr/bin/env python3
"""Independent exact symbolic audit for HCS-C280."""
import sympy as s

a, b, c, lam, t, z, r, gamma = s.symbols("a b c lambda t z r gamma", nonzero=True)
k = (b-c)/2
h = (b+c)/2
B = s.Matrix([[lam*a, k+lam*h], [-k+lam*h, -lam*a]])
delta = s.factor(lam**2*(a**2+h**2)-k**2)
I = s.eye(2)
checks = []
checks.extend(list(B*B-delta*I))
checks.append(s.factor(B.det()+delta))
checks.append(s.factor(B.trace()))
checks.append(s.factor((z*s.eye(2)-B).det()-(z**2-delta)))

# Cayley--Hamilton exponentials satisfy X'=BX and X(0)=I.
rho = s.symbols("rho", positive=True)
Xh = s.cosh(rho*t)*I+s.sinh(rho*t)/rho*B
checks.extend(list(s.diff(Xh, t)-B*Xh-s.sinh(rho*t)/rho*(rho**2-delta)*I))
checks.extend(list(Xh.subs(t, 0)-I))
omega = s.symbols("omega", positive=True)
Xe = s.cos(omega*t)*I+s.sin(omega*t)/omega*B
checks.extend(list(s.diff(Xe, t)-B*Xe+s.sin(omega*t)/omega*(omega**2+delta)*I))
checks.extend(list(Xe.subs(t, 0)-I))
Xn = I+t*B
checks.extend(list(s.diff(Xn, t)-B*Xn+t*delta*I))

# Simple shear and aspect-ratio identities.
ls = (r**2-1)/(r**2+1)
Bs = B.subs({a: 0, b: gamma, c: 0, lam: ls})
deltas = s.factor(delta.subs({a: 0, b: gamma, c: 0, lam: ls}))
checks.append(s.factor(deltas + gamma**2*r**2/(r**2+1)**2))
checks.extend(list(s.simplify(Bs*Bs-deltas*I)))
checks.append(s.simplify(s.pi/(gamma*r/(r**2+1))-s.pi*(r+1/r)/gamma))

# Frozen nilpotent representative and the projective normalization identity.
Bn = B.subs({a: 0, b: 8, c: 2, lam: s.Rational(3, 5)})
checks.extend(list(Bn**2))
checks.append(Bn.rank()-1)
q1, q2, q3 = s.symbols("q1 q2 q3", real=True)
B3 = s.diag(1, 1, 0)
B3[:2, :2] = B
q = s.Matrix([q1, q2, q3])
v = s.Function("v")
# Algebraic tangent identity: p dot (Bp-(p^T Bp)p)=0 for p^Tp=1.
p1, p2, p3 = s.symbols("p1 p2 p3", real=True)
p = s.Matrix([p1, p2, p3])
rhs = B3*p-(p.T*B3*p)[0]*p
quadratic = (p.T*B3*p)[0]
checks.append(s.factor((p.T*rhs)[0]-quadratic*(1-(p.T*p)[0])))

assert all(s.simplify(x) == 0 for x in checks), [x for x in checks if s.simplify(x) != 0]
print(f"C280_SYMPY_PASS ({len(checks)} symbolic identities; independent Cayley-Hamilton reconstruction)")
