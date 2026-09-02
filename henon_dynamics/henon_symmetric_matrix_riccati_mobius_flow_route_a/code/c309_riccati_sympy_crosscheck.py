#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C309."""
import sympy as sp


def main():
    x, s, t = sp.symbols("x s t", real=True)
    checks = 0
    def zero(expr, label):
        nonlocal checks
        if sp.simplify(sp.trigsimp(expr).rewrite(sp.exp)) != 0: raise AssertionError(label)
        checks += 1
    def f(z, u):
        return (z*sp.cosh(u)+sp.sinh(u))/(sp.cosh(u)+z*sp.sinh(u))
    zero(sp.diff(f(x,t),t) - (1-f(x,t)**2), "ODE")
    zero(f(x,0)-x, "initial")
    zero(f(f(x,s),t)-f(x,s+t), "group law")
    zero(sp.diff(f(x,t),x)-1/(sp.cosh(t)+x*sp.sinh(t))**2, "derivative")
    y = sp.symbols("y", real=True)
    zero((f(x,t)-f(y,t))/(x-y)-1/((sp.cosh(t)+x*sp.sinh(t))*(sp.cosh(t)+y*sp.sinh(t))), "divided difference")
    zero(f(1,t)-1, "plus equilibrium")
    zero(f(-1,t)+1, "minus equilibrium")
    phi = x**3/sp.Integer(3)-x
    zero(sp.diff(phi,x)*(1-x**2)+(1-x**2)**2, "gradient law")
    asym = 2*(x-1)*sp.exp(-2*t)/((1+x)+(1-x)*sp.exp(-2*t))
    zero(f(x,t)-1-asym, "exact forward remainder")
    # Linearization dimensions close the ambient symmetric dimension.
    for n in range(1, 11):
        for p in range(n+1):
            q=n-p
            zero(sp.Rational(p*(p+1),2)+sp.Rational(q*(q+1),2)+p*q-sp.Rational(n*(n+1),2), "dimension partition")
    print(f"C309 SymPy cross-check: PASS ({checks} identities)")


if __name__ == "__main__": main()
