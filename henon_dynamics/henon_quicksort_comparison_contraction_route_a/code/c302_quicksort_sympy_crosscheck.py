#!/usr/bin/env python3
"""Independent exact SymPy lane for the HCS-C302 formulas."""
from __future__ import annotations

import argparse
import itertools
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c302_quicksort_evidence.json"


def harmonic(n: int, power: int = 1) -> sp.Rational:
    return sum((sp.Rational(1, k**power) for k in range(1, n+1)), sp.Rational(0))


def mean(n: int) -> sp.Expr:
    return 2*(n+1)*harmonic(n)-4*n


def variance(n: int) -> sp.Expr:
    return 7*n*n-4*(n+1)**2*harmonic(n,2)-2*(n+1)*harmonic(n)+13*n


# A term is coefficient*u^a*(1-u)^b*log(u)^r*log(1-u)^s.
Term = tuple[sp.Expr, int, int, int, int]
A, B = sp.symbols("A B", positive=True)
BETA = sp.gamma(A+1)*sp.gamma(B+1)/sp.gamma(A+B+2)


@lru_cache(None)
def beta_log_integral(a: int, b: int, r: int, s: int) -> sp.Expr:
    derivative = sp.diff(BETA, A, r, B, s).subs({A: a, B: b}).doit()
    return sp.simplify(sp.expand_func(derivative))


def multiply(left: list[Term], right: list[Term]) -> list[Term]:
    return [
        (sp.expand(c*d), a+e, b+f, r+g, s+h)
        for c,a,b,r,s in left for d,e,f,g,h in right
    ]


def power(terms: list[Term], exponent: int) -> list[Term]:
    out: list[Term] = [(sp.Integer(1),0,0,0,0)]
    for _ in range(exponent):
        out = multiply(out, terms)
    return out


def integrate_terms(terms: list[Term]) -> sp.Expr:
    return sp.simplify(sum(c*beta_log_integral(a,b,r,s) for c,a,b,r,s in terms))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    evidence = json.loads(args.evidence.read_text())
    assert evidence["candidate_id"] == "HCS-C302"
    checks = 1
    z = sp.symbols("z")

    laws = [sp.Integer(1), sp.Integer(1)]
    for n in range(2,13):
        laws.append(sp.expand(z**(n-1)*sum(laws[j]*laws[n-1-j] for j in range(n))/n))

    for n,(poly,row) in enumerate(zip(laws,evidence["finite_pgf_regression"]["rows"])):
        archived = sum(
            sp.Rational(item["numerator"],item["denominator"])*z**item["comparisons"]
            for item in row["coefficients"]
        )
        assert sp.expand(poly-archived)==0
        checks += 1
        assert poly.subs(z,1)==1
        checks += 1
        distribution = sp.Poly(poly,z).terms()
        raw=[]
        for order in (1,2,3):
            moment=sum(coefficient*exponents[0]**order for exponents,coefficient in distribution)
            raw.append(sp.simplify(moment)); checks += 1
        var=sp.simplify(raw[1]-raw[0]**2)
        central3=sp.simplify(raw[2]-3*raw[0]*raw[1]+2*raw[0]**3)
        assert raw[0]==mean(n)
        assert var==variance(n)
        assert sp.Rational(row["raw_moment_3"])==raw[2]
        assert sp.Rational(row["third_centered_moment"])==central3
        checks += 4

    # Verify both all-n closed formulas against their unsimplified finite
    # recurrences for a much larger exact range than the PGF archive.
    for n in range(2,81):
        assert sp.simplify(mean(n)-(n-1)-sp.Rational(2,n)*sum(mean(j) for j in range(n)))==0
        conditional = [mean(j)+mean(n-1-j) for j in range(n)]
        average = sum(conditional)/n
        conditional_variance = sum((value-average)**2 for value in conditional)/n
        rhs = sp.Rational(2,n)*sum(variance(j) for j in range(n))+conditional_variance
        assert sp.simplify(variance(n)-rhs)==0
        checks += 2

    # Check the exact n+1 centering coefficients and zero-mean toll grids.
    for n,group in zip(range(2,33),evidence["centered_recursion_regression"]["groups"]):
        toll_sum=sp.Rational(0)
        for j,row in enumerate(group["rows"]):
            a=sp.Rational(j+1,n+1); b=sp.Rational(n-j,n+1)
            toll=sp.Rational(n-1+mean(j)+mean(n-1-j)-mean(n),n+1)
            assert sp.Rational(row["left_coefficient"])==a
            assert sp.Rational(row["right_coefficient"])==b
            assert a+b==1
            assert sp.Rational(row["centered_toll"])==toll
            toll_sum += toll
            checks += 4
        assert toll_sum==0
        checks += 1

    C: list[Term] = [
        (sp.Integer(1),0,0,0,0),
        (sp.Integer(2),1,0,1,0),
        (sp.Integer(2),0,1,0,1),
    ]
    branch: list[Term] = [
        (sp.Integer(1),2,0,0,0),
        (sp.Integer(1),0,2,0,0),
    ]
    int_c=integrate_terms(C)
    int_c2=integrate_terms(power(C,2))
    int_c_branch=integrate_terms(multiply(C,branch))
    int_c3=integrate_terms(power(C,3))
    int_branch=integrate_terms(branch)
    assert int_c==0
    assert int_c2==sp.Rational(7,3)-2*sp.pi**2/9
    assert int_c_branch==sp.Rational(1,18)
    assert int_c3==-sp.Rational(32,3)+sp.pi**2/9+8*sp.zeta(3)
    assert int_branch==sp.Rational(2,3)
    checks += 5

    m2=sp.simplify(int_c2/(1-int_branch))
    m3=sp.simplify((3*m2*int_c_branch+int_c3)/(1-sp.Rational(1,2)))
    assert m2==7-2*sp.pi**2/3
    assert m3==16*sp.zeta(3)-19
    checks += 2

    partial=sum(sp.Rational(1,k**3) for k in range(1,7))
    assert partial==sp.Rational(28567,24000)
    assert 16*partial-19==sp.Rational(67,1500)>0
    checks += 2

    print(f"C302 SymPy exact cross-check PASS ({checks} symbolic/cell assertions)")
    print("verified: PGFs, mean/variance recurrences, n+1 centering, contraction integral, beta derivatives, m3=16*zeta(3)-19")


if __name__ == "__main__":
    main()
