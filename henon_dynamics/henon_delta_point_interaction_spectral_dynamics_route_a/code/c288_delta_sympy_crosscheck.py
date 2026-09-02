#!/usr/bin/env python3
"""Symbolic reconstruction for HCS-C288."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/c288_delta_evidence.json"


def main() -> None:
    data = json.loads(DATA.read_text())
    a, k, p = s.symbols("a k p", real=True)
    checks = []
    free = 1/(2*k)
    image = -a/(2*k*(2*k+a))
    value = s.simplify(free+image)
    checks.append(s.simplify(value-1/(2*k+a)) == 0)
    checks.append(s.simplify(a/(2*(2*k+a))-(-a/(2*(2*k+a)))-a*value) == 0)
    r = a/(2*s.I*p-a)
    t = 2*s.I*p/(2*s.I*p-a)
    checks.append(s.simplify(r*s.conjugate(r)+t*s.conjugate(t)-1) == 0)
    checks.append(s.simplify(t-r-1) == 0)
    even = s.simplify(t+r)
    checks.append(s.simplify(even-(2*s.I*p+a)/(2*s.I*p-a)) == 0)
    checks.append(s.simplify(even*s.conjugate(even)-1) == 0)
    energy = -a**2/4
    checks.append(s.simplify((-a/2)*(-2/a)-1) == 0)
    checks.append(s.simplify(2*(-a/2)+a) == 0)
    checks.append(s.simplify((2*k+a).subs(k, -a/2)) == 0)
    checks.append(s.simplify(energy-(-a/2)**2*(-1)) == 0)
    # Integral used for the relative trace, u=a*sqrt(t)/2.
    u = s.symbols("u", real=True)
    trace = (s.exp(u**2)*s.erfc(u)-1)/2
    checks.append(s.simplify(trace.subs(u, 0)) == 0)
    checks.append(s.simplify(s.diff(trace, u) - (u*s.exp(u**2)*s.erfc(u)-1/s.sqrt(s.pi))) == 0)
    for row in data["scattering_cells"]:
        rr = s.Rational(row["reflection_probability"])
        tt = s.Rational(row["transmission_probability"])
        checks.append(s.simplify(rr+tt-1) == 0)
    for row in data["bound_state_cells"]:
        aa = s.Rational(row["alpha"])
        checks.append(s.Rational(row["energy"]) == -aa**2/4)
        checks.append(s.Rational(row["normalization_squared"])*(-2/aa) == 1)
    assert all(checks)
    print(f"C288_SYMPY_PASS ({len(checks)} symbolic checks)")


if __name__ == "__main__":
    main()
