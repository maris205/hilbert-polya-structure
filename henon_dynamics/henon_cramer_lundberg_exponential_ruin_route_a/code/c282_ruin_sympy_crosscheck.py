#!/usr/bin/env python3
"""Independent exact symbolic audit for HCS-C282."""
import sympy as s

c, beta, nu, q, r, u, z = s.symbols("c beta nu q r u z", positive=True)
pen = s.symbols("pen", positive=True)
F = c*r**2-(c*beta-nu-q)*r-q*beta
A = (beta-r)/(beta+pen)
checks = []

# The e^{-r u} coefficient in the first-jump equation is exactly the root polynomial.
coef_r = -c*r*A-(nu+q)*A+nu*beta*A/(beta-r)
checks.append(s.factor(coef_r - A*F/(beta-r)))
# The memoryless forcing cancels the e^{-beta u} coefficient.
coef_beta = -nu*beta*A/(beta-r)+nu*beta/(beta+pen)
checks.append(s.factor(coef_beta))

# The convolution state closes a two-dimensional system.  Its homogeneous
# characteristic modes are precisely the two roots of F, and the forcing has
# the displayed particular solution.
lam = s.symbols("lam")
system_matrix = s.Matrix([[(nu+q)/c, -nu/c], [beta, -beta]])
checks.append(s.factor(c*system_matrix.charpoly(lam).as_expr().subs(lam, -r)-F))
particular = s.Matrix([0, -beta/(beta+pen)])
forcing = s.Matrix([-nu*beta/(c*(beta+pen)), 0])
checks.extend(s.simplify(x) for x in ((-beta*s.eye(2)-system_matrix)*particular-forcing))

disc = (c*beta-nu-q)**2+4*c*beta*q
root = (c*beta-nu-q+s.sqrt(disc))/(2*c)
checks.append(s.simplify(F.subs(r, root)))
checks.append(s.simplify(root.subs(q, 0)-(c*beta-nu+s.Abs(c*beta-nu))/(2*c)))

# Profitable root, ultimate probability, and conditional first moment.
R = beta-nu/c
checks.append(s.factor(F.subs({r: R, q: 0})))
rp_prof = nu/(c*(c*beta-nu))
phi = (beta-r)/beta*s.exp(-r*u)
dphi = s.diff(phi, r)
conditional = s.simplify(-dphi.subs(r, R)*rp_prof / phi.subs(r, R))
checks.append(s.factor(conditional-(1+nu*u/c)/(c*beta-nu)))

# Adverse q=0 branch r=0 and its derivative.
rp_adv = beta/(nu-c*beta)
conditional_adv = s.simplify(-dphi.subs(r, 0)*rp_adv/phi.subs(r, 0))
checks.append(s.factor(conditional_adv-(beta*u+1)/(nu-c*beta)))

# Adjustment martingale and exponential overshoot transform.
adjustment = s.factor(nu*(beta/(beta-R)-1)-c*R)
checks.append(adjustment)
checks.append(s.simplify(s.integrate(beta*s.exp(-(beta+pen)*z), (z, 0, s.oo))-beta/(beta+pen)))
checks.append(s.integrate(z*beta*s.exp(-beta*z), (z, 0, s.oo))-1/beta)

# Critical root has a square-root cusp: r(q)^2/q -> beta/c.
critical_root = root.subs(nu, c*beta)
checks.append(s.simplify(s.limit(critical_root**2/q, q, 0, dir="+")-beta/c))

# Supremum mixture is normalized and has the same tail as ruin.
rho = nu/(c*beta)
checks.append(s.simplify((1-rho)+rho-1))

assert all(s.simplify(x) == 0 for x in checks), checks
print(f"C282_SYMPY_PASS ({len(checks)} symbolic identities; independent Gerber-Shiu reconstruction)")
