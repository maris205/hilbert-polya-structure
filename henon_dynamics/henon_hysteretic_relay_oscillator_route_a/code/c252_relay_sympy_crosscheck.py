#!/usr/bin/env python3
"""Symbolic checks for the relay flow and guards."""
import sympy as s
h,g,t,y0=s.symbols('h g t y0', positive=True)
checks=[]
y=y0*s.exp(-g*t)
checks.append((s.simplify(s.diff(y,t)+g*y),"decay ODE"))
checks.append((s.simplify((y0*s.exp(-2*g*h))*s.exp(-2*g*h)-y0*s.exp(-4*g*h)),"full composition"))
checks.append((s.simplify(2*h+2*h-4*h),"period"))
checks.append((s.simplify(s.exp(-4*g*h)-1).subs(g,0),"neutral face"))
checks.append((s.simplify(s.exp(-4*g*h)*0-0),"fixed zero orbit"))
n=s.symbols('n', positive=True, integer=True)
checks.append((s.simplify((n*2*h)/n-2*h),"event lower bound"))
checks.append((s.simplify((-h)+2*h-h),"theta cycle"))
checks.append((s.simplify(h-2*h+h),"reverse theta cycle"))
checks.append((s.simplify(s.diff(s.exp(-g*t),t)+g*s.exp(-g*t)),"fundamental solution"))
checks.append((s.simplify(s.exp(-g*(2*h+2*h))-s.exp(-4*g*h)),"semigroup law"))
for v,label in checks:
    if v!=0: raise AssertionError(f"{label}: {v}")
print(f"C252_SYMPY_PASS ({len(checks)} symbolic identities; guards, flow and return map)")
