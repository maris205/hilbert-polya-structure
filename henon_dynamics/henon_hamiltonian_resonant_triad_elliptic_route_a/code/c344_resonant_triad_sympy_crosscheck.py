#!/usr/bin/env python3
"""Independent symbolic Hamiltonian and elliptic checks for HCS-C344."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c344_resonant_triad_evidence.json"
CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def q(value: str) -> sp.Rational:
    item = Fraction(value)
    return sp.Rational(item.numerator, item.denominator)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C344 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    imaginary = sp.I
    z1, z2, z3, w1, w2, w3 = sp.symbols("z1 z2 z3 w1 w2 w3")
    zs, ws = (z1, z2, z3), (w1, w2, w3)
    hamiltonian = z1*z2*w3+w1*w2*z3

    def bracket(f, g):
        return sp.expand(-imaginary*sum(
            sp.diff(f, z)*sp.diff(g, w)-sp.diff(f, w)*sp.diff(g, z)
            for z, w in zip(zs, ws)))

    velocities = [bracket(z, hamiltonian) for z in zs]
    need(sp.simplify(imaginary*velocities[0]-w2*z3) == 0, "first Hamilton equation")
    need(sp.simplify(imaginary*velocities[1]-w1*z3) == 0, "second Hamilton equation")
    need(sp.simplify(imaginary*velocities[2]-z1*z2) == 0, "third Hamilton equation")
    n1 = z1*w1+z3*w3
    n2 = z2*w2+z3*w3
    for invariant, name in ((n1, "N1"), (n2, "N2"), (hamiltonian, "H")):
        need(bracket(invariant, hamiltonian) == 0, f"{name} conservation")
    need(bracket(n1, n2) == 0, "Manley-Rowe involution")
    need(bracket(n1, hamiltonian) == bracket(n2, hamiltonian) == 0, "Liouville involution")

    x = z3*w3
    xdot = bracket(x, hamiltonian)
    product = (z1*z2*w3)*(w1*w2*z3)
    need(sp.expand(xdot**2-(4*product-hamiltonian**2)) == 0, "scalar square identity")
    need(sp.expand(product-x*(n1-x)*(n2-x)) == 0, "intensity factorization")

    X, N1, N2, H2 = sp.symbols("X N1 N2 H2")
    polynomial = sp.expand(4*X*(N1-X)*(N2-X)-H2)
    r1, r2, r3 = sp.symbols("r1 r2 r3")
    factored = 4*(X-r1)*(X-r2)*(X-r3)
    expanded_difference = sp.Poly(sp.expand(factored-polynomial), X)
    coefficients = expanded_difference.all_coeffs()
    need(sp.expand(coefficients[0]-4*(N1+N2-r1-r2-r3)) == 0, "Vieta sum")
    need(sp.expand(coefficients[1]-4*(r1*r2+r1*r3+r2*r3-N1*N2)) == 0, "Vieta pair sum")
    need(sp.expand(coefficients[2]-(H2-4*r1*r2*r3)) == 0, "Vieta product")

    y, delta, gap = sp.symbols("y delta gap", positive=True)
    modulus = delta/gap
    ydot_squared = 4*gap*y*(1-y)*(1-modulus*y)
    Xy = r1+delta*y
    elliptic_rhs = 4*(Xy-r1)*(r1+delta-Xy)*(r1+gap-Xy)
    need(sp.expand(delta**2*ydot_squared-elliptic_rhs) == 0, "Jacobi sn-squared reduction")

    critical = sp.diff(X*(N1-X)*(N2-X), X)
    need(sp.expand(critical-(3*X**2-2*(N1+N2)*X+N1*N2)) == 0, "critical equation")
    phase_lock = sp.together(1/X-1/(N1-X)-1/(N2-X))
    need(sp.factor(sp.together(phase_lock).as_numer_denom()[0]-critical) == 0,
         "critical point equals phase lock")

    # The H=0 Jacobi orbit in the chamber N1=A^2 <= N2=B^2.
    A, B, sn, cn, dn = sp.symbols("A B sn cn dn", positive=True)
    derivatives = {sn: B*cn*dn, cn: -B*sn*dn, dn: -(A**2/B)*sn*cn}
    components = [A*cn, B*dn, -imaginary*A*sn]
    conjugates = [A*cn, B*dn, imaginary*A*sn]
    time_derivative = lambda expression: sp.expand(sum(
        sp.diff(expression, variable)*value for variable, value in derivatives.items()))
    rhs = [conjugates[1]*components[2], conjugates[0]*components[2], components[0]*components[1]]
    for index in range(3):
        need(sp.expand(imaginary*time_derivative(components[index])-rhs[index]) == 0,
             f"H-zero Jacobi component {index}")
    need(sp.expand(components[0]*components[1]*conjugates[2]
                   +conjugates[0]*conjugates[1]*components[2]) == 0,
         "H-zero Hamiltonian")
    need(sp.expand(components[0]*conjugates[0]+components[2]*conjugates[2]
                   -A**2*(cn**2+sn**2)) == 0, "first H-zero invariant")
    need(sp.expand(components[1]*conjugates[1]+components[2]*conjugates[2]
                   -(B**2*dn**2+A**2*sn**2)) == 0, "second H-zero invariant")

    # Evidence rows: exact cubic construction and Vieta coefficients.
    for row in data["regular_rows"]:
        aa, bb, level = q(row["n1"]), q(row["n2"]), q(row["level"])
        nminus = min(aa, bb)
        witness = nminus/2
        h2 = level*witness*(aa-witness)*(bb-witness)
        need(q(row["h_squared"]) == h2, "evidence H-squared")
        need(q(row["root_sum"]) == aa+bb, "evidence root sum")
        need(q(row["root_pair_sum"]) == aa*bb, "evidence root pair sum")
        need(q(row["root_product"]) == h2/4, "evidence root product")
        for interval in row["root_intervals"]:
            left, right = q(interval[0]), q(interval[1])
            pleft = 4*left*(aa-left)*(bb-left)-h2
            pright = 4*right*(aa-right)*(bb-right)-h2
            need(pleft*pright < 0, "evidence exact sign bracket")

    for row in data["zero_hamiltonian_rows"]:
        aa, bb = q(row["n1"]), q(row["n2"])
        if aa == bb:
            need(row["modulus_squared"] == "1" and row["intensity_period"] is None,
                 "evidence separatrix boundary")
        else:
            need(q(row["modulus_squared"]) == min(aa, bb)/max(aa, bb),
                 "evidence zero-H modulus")

    # Exact asymmetric rational-frequency relative equilibrium witnesses.
    for row in data["relative_equilibrium_rows"]:
        aa, bb = q(row["n1"]), q(row["n2"])
        if (aa, bb) in ((sp.Rational(5), sp.Rational(8)), (sp.Rational(8), sp.Rational(5))):
            need(sp.Rational(row["critical_x"]) == 2, "rational critical intensity")
            need(sp.Rational(row["maximum_abs_h"]) == 12, "rational maximal H")

    print(f"C344 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
