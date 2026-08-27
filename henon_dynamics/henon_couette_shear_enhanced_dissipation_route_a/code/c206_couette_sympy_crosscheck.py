#!/usr/bin/env python3
"""Independent symbolic reconstruction for HCS-C206."""
import json
from pathlib import Path
import sympy as sp


def significant_digits(value: str) -> int:
    mantissa = value.lower().split("e", 1)[0].lstrip("+-").replace(".", "")
    significant = mantissa.lstrip("0")
    return len(significant) if significant else 1


def main():
    a,k,eta,t,s,nu = sp.symbols("a k eta t s nu", real=True)
    g = sp.Function("g")
    checks = 0
    def zero(expr, label):
        nonlocal checks; checks += 1
        if sp.simplify(sp.expand(expr)) != 0: raise AssertionError(label)
    def expect(condition, label):
        nonlocal checks; checks += 1
        if not condition: raise AssertionError(label)
    integral = eta**2*t + a*k*eta*t**2 + a**2*k**2*t**3/sp.Integer(3)
    square = t*(eta+a*k*t/2)**2 + a**2*k**2*t**3/sp.Integer(12)
    zero(integral-square, "complete square")
    D = k**2*t + integral
    h = sp.exp(-nu*D)*g(eta+a*k*t)
    zero(sp.diff(h,t)-a*k*sp.diff(h,eta)+nu*(k**2+eta**2)*h, "Fourier PDE")
    def d(time, freq):
        return k**2*time+freq**2*time+a*k*freq*time**2+a**2*k**2*time**3/sp.Integer(3)
    zero(d(t,eta)+d(s,eta+a*k*t)-d(t+s,eta), "semigroup exponent")
    zero(sp.diff(D,eta,2)-2*t, "strict quadratic curvature for positive time")
    zero(sp.diff(D,eta).subs(eta,-a*k*t/2), "minimizer")
    zero(D.subs(eta,-a*k*t/2)-(k**2*t+a**2*k**2*t**3/12), "minimum")
    zero(D.subs(t,0), "t0")
    zero((D-k**2*t-eta**2*t).subs(a,0), "a0")
    zero((D-eta**2*t).subs(k,0), "k0")
    zero((sp.exp(-nu*D)-1).subs(nu,0), "nu0")
    evidence = json.loads((Path(__file__).resolve().parents[1]/"results/c206_couette_evidence.json").read_text())
    summary = evidence["summary"]
    expect(summary["working_decimal_digits"] == 100, "working precision contract")
    expect(summary["serialized_significant_digits"] == 82, "serialization precision contract")
    expect(summary["serialized_decimal_fields"] == 1350, "serialized field count")
    for row in evidence["regression"]["fourier_cells"]:
        vals={a:sp.Rational(row["a"]),k:sp.Rational(row["k"]),eta:sp.Rational(row["eta"]),t:sp.Rational(row["t"])}
        zero(integral.subs(vals)-sp.Rational(row["integrated_vertical_frequency"]), "row integral")
        zero(square.subs(vals)-sp.Rational(row["completed_square"]), "row square")
        expect(significant_digits(row["multiplier"]) == 82, "multiplier serialized digits")
        expect(significant_digits(row["sector_norm"]) == 82, "norm serialized digits")
    print(json.dumps({"status":"C206_SYMPY_PASS","checks":checks,"symbolic_fourier_cells":len(evidence["regression"]["fourier_cells"])},sort_keys=True))


if __name__ == "__main__": main()
