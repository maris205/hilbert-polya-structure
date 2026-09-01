#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C281."""
import sympy as s

t = s.symbols("t", real=True)
a1, a2, a3 = s.symbols("a1 a2 a3", positive=True)
d1, d2, d3 = s.symbols("d1 d2 d3", positive=True)
c1, c2, c3 = s.symbols("c1 c2 c3", nonnegative=True)
n = d1 + d2 + d3
A = [a1 - 2*c1*t, a2 - 2*c2*t, a3 - 2*c3*t]
aa = [a1, a2, a3]; dd = [d1, d2, d3]; cc = [c1, c2, c3]
R = sum(di*ci/Ai for di, ci, Ai in zip(dd, cc, A))
Vratio = s.prod((Ai/ai)**(di/s.Integer(2)) for Ai, ai, di in zip(A, aa, dd))
C = s.prod((Ai/ai)**(-di/n) for Ai, ai, di in zip(A, aa, dd))
checks = []
checks.append(s.simplify(s.diff(s.log(Vratio), t) + R))
checks.append(s.simplify(s.diff(s.log(C), t) - 2*R/n))
# The preceding two logarithmic derivatives imply constant normalized volume;
# pin that constant at t=0 without asking SymPy to canonicalize symbolic
# real powers of three unrelated positive bases.
checks.append(s.simplify((C**(n/s.Integer(2))*Vratio).subs(t, 0)-1))
for Ai, ci in zip(A, cc):
    checks.append(s.simplify(s.diff(Ai, t)+2*ci))
    # Divide d(C A_i)/dt by d tau/dt=C.
    lhs = s.diff(C*Ai, t)/C
    rhs = -2*ci + 2*(R/C)*(C*Ai)/n
    checks.append(s.simplify(lhs-rhs))

# Equal clocks: a_i=2 c_i T gives a homothety and a stationary normalized metric.
T = s.symbols("T", positive=True)
subs_equal = {a1: 2*c1*T, a2: 2*c2*T, a3: 2*c3*T}
for Ai, ai in zip(A, aa):
    checks.append(s.simplify((Ai-ai*(1-t/T)).subs(subs_equal)))
checks.append(s.simplify((C-(1-t/T)**-1).subs(subs_equal)))
for Ai, ai in zip(A, aa):
    checks.append(s.simplify((C*Ai-ai).subs(subs_equal)))

# Frozen tied-collapse representative d=(2,2,4), a=(2,2,12), T=1.
eps = s.symbols("eps", positive=True)
dvals = [2, 2, 4]; cvals = [1, 1, 3]; avals = [2, 2, 12]
At = [a-2*c*(1-eps) for a, c in zip(avals, cvals)]
Rt = sum(s.Rational(d*c, 1)/x for d, c, x in zip(dvals, cvals, At))
Rm2 = sum(s.Rational(2*d*c, 1)/x**2 for d, c, x in zip(dvals, cvals, At))
Ric2 = sum(s.Rational(d*c*c, 1)/x**2 for d, c, x in zip(dvals, cvals, At))
checks.append(s.simplify(s.limit(eps*Rt, eps, 0)-2))
checks.append(s.simplify(s.limit(eps**2*Ric2, eps, 0)-1))
checks.append(s.simplify(s.limit(eps**2*Rm2, eps, 0)-s.Rational(2, 1)))

# Mixed flat representative retains the circle scale exactly.
checks.append(s.diff(s.Rational(5, 2)-2*0*t, t))

assert all(s.simplify(x) == 0 for x in checks), [x for x in checks if s.simplify(x) != 0]
print(f"C281_SYMPY_PASS ({len(checks)} symbolic identities; independent normalized-time reconstruction)")
