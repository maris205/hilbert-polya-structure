#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C345."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c345_fano_anderson_evidence.json"
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
        raise RuntimeError("C345 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())

    E, epsilon, J, g, s, V = sp.symbols("E epsilon J g s V", real=True)
    quartic = sp.expand((E-epsilon)**2*(E**2-4*J**2)-g**4)
    expected = E**4-2*epsilon*E**3+(epsilon**2-4*J**2)*E**2+8*epsilon*J**2*E-4*epsilon**2*J**2-g**4
    need(sp.expand(quartic-expected) == 0, "quartic expansion")

    upper = E-epsilon-g**2/sp.sqrt(E**2-4*J**2)
    lower = E-epsilon+g**2/sp.sqrt(E**2-4*J**2)
    need(sp.simplify(sp.diff(upper, E)-(1+g**2*E/(E**2-4*J**2)**sp.Rational(3, 2))) == 0,
         "upper monotonic derivative")
    need(sp.simplify(sp.diff(lower, E)-(1-g**2*E/(E**2-4*J**2)**sp.Rational(3, 2))) == 0,
         "lower monotonic derivative")
    need(sp.factor((E-epsilon)**2*(E**2-4*J**2)-g**4) == quartic,
         "branch equation squares to quartic")

    A = sp.symbols("A", real=True)
    radical = sp.symbols("radical", positive=True)
    boundary_resolvent = 1/(A+sp.I*g**2/radical)
    density = -sp.im(sp.expand_complex(boundary_resolvent))/sp.pi
    target_density = g**2*radical/(sp.pi*(A**2*radical**2+g**4))
    need(sp.simplify(density-target_density) == 0, "Stieltjes density boundary value")
    gamma = sp.symbols("gamma", positive=True)
    signed_boundary = 1/(A+sp.I*gamma)
    need(sp.simplify(sp.im(signed_boundary)+gamma/(A**2+gamma**2)) == 0,
         "Cauchy resolvent is anti-Herglotz on the upper boundary")
    sigma = sp.symbols("sigma", positive=True)
    edge_form = sigma/((E-epsilon)*sigma-g**2)
    need(sp.simplify(1/(E-epsilon-g**2/sigma)-edge_form) == 0,
         "edge-safe Schur rewrite")
    positive_g = sp.symbols("positive_g", positive=True)
    for edge in (-2*J, 2*J):
        edge_limit = sp.limit(
            sigma/((edge-epsilon)*sigma-positive_g**2), sigma, 0, dir="+"
        )
        need(edge_limit == 0, "vanishing edge resolvent and atom test")

    sine = sp.symbols("sine", positive=True, real=True)
    amplitude = 2*sp.I*J*sine/(2*sp.I*J*sine+V)
    reflection = -V/(2*sp.I*J*sine+V)
    transmission_probability = sp.simplify(amplitude*sp.conjugate(amplitude))
    reflection_probability = sp.simplify(reflection*sp.conjugate(reflection))
    need(sp.simplify(transmission_probability-4*J**2*sine**2/(4*J**2*sine**2+V**2)) == 0,
         "transmission amplitude")
    need(sp.simplify(reflection_probability-V**2/(4*J**2*sine**2+V**2)) == 0,
         "reflection amplitude")
    need(sp.simplify(transmission_probability+reflection_probability-1) == 0,
         "scattering unitarity")
    substituted = sp.factor(transmission_probability.subs(V, g**2/(E-epsilon)))
    expected_transmission = 4*J**2*sine**2*(E-epsilon)**2/(g**4+4*J**2*sine**2*(E-epsilon)**2)
    need(sp.simplify(substituted-expected_transmission) == 0, "Fano transmission formula")
    need(sp.simplify(expected_transmission.subs(E, epsilon)) == 0, "Fano zero")

    w = sp.symbols("w")
    m_series = w/sp.sqrt(1-4*J**2*w**2)
    G_series = 1/(1/w-epsilon-g**2*m_series)
    expansion = sp.series(G_series, w, 0, 5).removeO().expand()
    target_expansion = w+epsilon*w**2+(epsilon**2+g**2)*w**3+(epsilon**3+2*epsilon*g**2)*w**4
    need(sp.expand(expansion-target_expansion) == 0, "resolvent moments and total mass")

    block = sp.Matrix([[0, g], [g, epsilon]])
    need(sp.factor((E*sp.eye(2)-block).det()-(E**2-epsilon*E-g**2)) == 0,
         "J zero two-by-two block")
    for root in (epsilon/2-sp.sqrt(epsilon**2+4*g**2)/2,
                 epsilon/2+sp.sqrt(epsilon**2+4*g**2)/2):
        need(sp.simplify(root**2-epsilon*root-g**2) == 0, "J zero eigenvalue")

    for row in data["spectral_rows"]:
        jj, ee, gg = q(row["J"]), q(row["epsilon"]), q(row["g"])
        poly = sp.Poly((E-ee)**2*(E**2-4*jj**2)-gg**4, E, domain=sp.QQ)
        lower, upper = min(-2*jj, ee), max(2*jj, ee)
        need(poly.count_roots(-sp.oo, lower) == row["physical_lower_root_count"],
             "physical lower Sturm count")
        need(poly.count_roots(upper, sp.oo) == row["physical_upper_root_count"],
             "physical upper Sturm count")
        need(poly.count_roots(-2*jj, 2*jj) == row["band_root_count"],
             "band Sturm count")
        need(poly.count_roots(-sp.oo, sp.oo) == row["quartic_real_root_count"],
             "total real Sturm count")

    for row in data["scattering_rows"]:
        jj, ee, gg = q(row["J"]), q(row["epsilon"]), q(row["abs_g"])
        cosine = q(row["cos_k"])
        energy = 2*jj*cosine
        sine2 = 1-cosine**2
        exact_t = 4*jj**2*sine2*(energy-ee)**2/(gg**4+4*jj**2*sine2*(energy-ee)**2)
        need(q(row["transmission"]) == exact_t, "evidence transmission")
        need(q(row["reflection"]) == 1-exact_t, "evidence reflection")
        radical2 = 4*jj**2-energy**2
        density_denominator = (energy-ee)**2*radical2+gg**4
        need(q(row["pi_density_divided_by_radical"]) == gg**2/density_denominator,
             "evidence density factor")

    print(f"C345 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
