#!/usr/bin/env python3
"""Independent SymPy formula, branch, and shell checks for HCS-C157."""
from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / "results/c157_abel_trace_evidence.json").read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not bool(condition):
            raise AssertionError(message)

    # The radial Fourier constant follows by differentiating the Laplace--
    # Bessel transform int exp(-a r) J_0(b r) dr=(a^2+b^2)^(-1/2).
    a, b, s, radius = sp.symbols("a b s radius", positive=True)
    laplace_bessel = 1 / sp.sqrt(a*a+b*b)
    radial_first_moment = -sp.diff(laplace_bessel, a)
    check(sp.simplify(radial_first_moment-a/(a*a+b*b)**sp.Rational(3, 2)) == 0,
          "Laplace-Bessel derivative")
    scaled = sp.simplify(2*sp.pi*radial_first_moment.subs({a: sp.pi*s, b: 2*sp.pi*radius}))
    expected = 2*s/(sp.pi*(s*s+4*radius*radius)**sp.Rational(3, 2))
    check(sp.simplify(scaled-expected) == 0, "2D Fourier constant")

    full, axis, quadrant = sp.symbols("S A W")
    check(sp.solve(sp.Eq(full, 1+4*axis+4*quadrant), quadrant)[0] ==
          full/4-axis-sp.Rational(1, 4), "quadrant decomposition")
    check(data["poisson_theorem"]["radial_transform"] ==
          "Fourier[exp(-pi*s*|x|)](m)=2*s/(pi*(s^2+4*|m|^2)^(3/2))",
          "frozen transform")

    # The principal branch is unambiguous on Re(s)>0.
    sigma, tau, R = sp.symbols("sigma tau R", positive=True, real=True)
    complex_s = sigma + sp.I*tau
    argument = sp.expand(complex_s**2+R**2)
    check(sp.im(argument) == 2*sigma*tau, "branch imaginary part")
    check(sp.re((sigma+sp.I*0)**2+R**2) == sigma**2+R**2, "real-axis positivity")
    epsilon = sp.symbols("epsilon", positive=True)
    modulus_factor = (epsilon*sp.sqrt(epsilon**2+4*R**2))**(-sp.Rational(3, 2))
    branch_scale = sp.limit(epsilon**sp.Rational(3, 2)*modulus_factor, epsilon, 0, dir="+")
    check(sp.simplify(branch_scale-(2*R)**(-sp.Rational(3, 2))) == 0,
          "minus-three-halves branch scaling")
    zeta_var, radial_var = sp.symbols("zeta_var radial_var", positive=True)
    g = (4*radial_var**2+zeta_var)**(-sp.Rational(3, 2))
    check(sp.diff(g, zeta_var, 2) ==
          sp.Rational(15, 4)*(4*radial_var**2+zeta_var)**(-sp.Rational(7, 2)),
          "complex Taylor second derivative")
    k, M = sp.symbols("k M", positive=True)
    check(sp.integrate(k**-6, (k, M, sp.oo)) == 1/(5*M**5),
          "square-shell tail integral")
    check(sp.simplify(sp.Rational(15, 8)*8*sp.Rational(1, 5)/3**sp.Rational(7, 2)
                      -1/3**sp.Rational(5, 2)) == 0, "dual tail constant")
    z = sp.symbols("z")
    pole = 2*sp.I
    residue = sp.limit((z-pole)*(-1/(sp.exp(sp.pi*z)-1)), z, pole)
    check(sp.simplify(residue+1/sp.pi) == 0, "boundary subtraction simple pole")
    singularity = data["boundary_singularity_theorem"]
    check(singularity["branch_locations_exhaust_all_boundary_singularities"] is False,
          "branch list not exhaustive")
    check("singularity types differ" in singularity["overlap_boundary"],
          "branch-pole noncancellation")

    # Rebuild every exact shell by solving a^2+b^2=N, a,b>0.
    primitive_lookup = {row["primitive_squared_norm"]: row
                        for row in data["primitive_direction_ledger"]}
    shell_lookup = {row["dual_squared_norm"]: row for row in data["dual_shell_ledger"]}
    for squared_norm in range(2, 501):
        solutions = []
        for first in range(1, isqrt(squared_norm)+1):
            remainder = squared_norm-first*first
            if remainder > 0 and isqrt(remainder)**2 == remainder:
                solutions.append((first, isqrt(remainder)))
        if not solutions:
            check(squared_norm not in shell_lookup, f"empty shell {squared_norm}")
            continue
        frozen_shell = shell_lookup[squared_norm]
        check(frozen_shell["ordered_positive_vector_count"] == len(solutions),
              f"shell count {squared_norm}")
        check(frozen_shell["sign_lifted_dual_multiplicity"] == 4*len(solutions),
              f"sign lifts {squared_norm}")
        expected_decomposition = {}
        for first, second in solutions:
            repetition = gcd(first, second)
            base_norm = squared_norm//(repetition*repetition)
            expected_decomposition[(base_norm, repetition)] = (
                expected_decomposition.get((base_norm, repetition), 0)+1)
        frozen_decomposition = {
            (row["primitive_squared_norm"], row["repetition"]):
                row["primitive_ordered_multiplicity"]
            for row in frozen_shell["primitive_repetition_decomposition"]
        }
        check(expected_decomposition == frozen_decomposition,
              f"primitive repetition {squared_norm}")
        primitive = [[first, second] for first, second in solutions if gcd(first, second) == 1]
        if primitive:
            frozen_primitive = primitive_lookup[squared_norm]
            check(frozen_primitive["directions"] == primitive, f"primitive directions {squared_norm}")
            check(frozen_primitive["ordered_positive_direction_count"] == len(primitive),
                  f"primitive multiplicity {squared_norm}")
            check(frozen_primitive["length_symbol"] == f"2*sqrt({squared_norm})",
                  f"length symbol {squared_norm}")
        else:
            check(squared_norm not in primitive_lookup, f"nonprimitive shell {squared_norm}")

    collision = data["collision_sentinel"]
    check(collision["first_fourfold_ordered_primitive_squared_norm"] == 65, "collision norm")
    check(collision["directions"] == [[1, 8], [4, 7], [7, 4], [8, 1]], "collision directions")
    check(collision["sign_lifted_multiplicity"] == 16, "collision sign lifts")
    check(data["geometric_decomposition"]["isolated_orbit_determinant"] is False,
          "no isolated determinant")
    check(data["formal_lift"]["target_operator_claimed"] is False, "no target operator")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B disabled")
    check(all(value is False for value in data["claim_boundary"].values()), "claim boundary")
    print(json.dumps({"status": "C157_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
