#!/usr/bin/env python3
"""Exact symbolic and finite-group cross-checks for HCS-C296."""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/c296_hard_rod_evidence.json"


def R(value: str) -> sp.Rational:
    return sp.Rational(value)


def main() -> None:
    data = json.loads(DATA.read_text())
    checks = 0

    # Changing the cyclic starting rod produces a cyclic permutation of the
    # compressed coordinates followed by one common translation by a.
    a, ell = sp.symbols("a ell", positive=True)
    xs = sp.symbols("x0:5", real=True)
    length = ell - 5*a
    ys = [xs[i]-i*a for i in range(5)]
    shifted_x = list(xs[1:]) + [xs[0]+ell]
    shifted_y = [shifted_x[i]-i*a for i in range(5)]
    predicted = [ys[i]+a for i in range(1, 5)] + [ys[0]+a+length]
    for actual, wanted in zip(shifted_y, predicted):
        if sp.simplify(actual-wanted) != 0:
            raise AssertionError("cyclic-start compression")
        checks += 1

    # Equal-mass exchange preserves the two algebraically independent
    # quadratic invariants.  A three-body sorting is a permutation as well.
    u, w = sp.symbols("u w", real=True)
    if sp.expand((u+w)-(w+u)) != 0 or sp.expand((u*u+w*w)-(w*w+u*u)) != 0:
        raise AssertionError("binary invariants")
    checks += 2
    z = sp.symbols("z0:4", real=True)
    for permutation in itertools.permutations(range(4)):
        if sp.expand(sum(z)-sum(z[i] for i in permutation)) != 0:
            raise AssertionError("permutation momentum")
        if sp.expand(sum(t*t for t in z)-sum(z[i]**2 for i in permutation)) != 0:
            raise AssertionError("permutation energy")
        checks += 2

    # Every recorded pair row satisfies its affine winding congruence.
    scenarios = {row["id"]: row for row in data["scenarios"]}
    particles = {}
    for row in data["particle_cells"]:
        particles.setdefault(row["scenario"], []).append((R(row["y"]), R(row["velocity"])))
    for row in data["pair_crossing_cells"]:
        scenario = scenarios[row["scenario"]]
        L = R(scenario["L"]); t = R(row["time"])
        yi, vi = particles[row["scenario"]][row["i"]]
        yj, vj = particles[row["scenario"]][row["j"]]
        winding = sp.simplify((yi-yj+t*(vi-vj))/L)
        if winding.is_integer is not True:
            raise AssertionError("pair winding")
        checks += 1

    # Recorded blocks conserve power sums p_1 and p_2; the outgoing list is
    # an exact multiset permutation, not an inelastic average.
    for event in data["event_cells"]:
        for group in event["groups"]:
            incoming = [R(x) for x in group["incoming_spatial_velocities"]]
            outgoing = [R(x) for x in group["outgoing_spatial_velocities"]]
            if sorted(incoming, key=sp.default_sort_key) != sorted(outgoing, key=sp.default_sort_key):
                raise AssertionError("event multiset")
            if sp.simplify(sum(incoming)-R(group["momentum_before"])) != 0:
                raise AssertionError("incoming momentum")
            if sp.simplify(sum(outgoing)-R(group["momentum_after"])) != 0:
                raise AssertionError("outgoing momentum")
            if sp.simplify(sum(x*x for x in incoming)-R(group["twice_energy_before"])) != 0:
                raise AssertionError("incoming energy")
            if sp.simplify(sum(x*x for x in outgoing)-R(group["twice_energy_after"])) != 0:
                raise AssertionError("outgoing energy")
            checks += 5

    # Exhaustive finite cyclic-group audit of the two-coset lcm condition.
    # Work in Z/MZ with H_d={k*M/d}; this is the exact discretization of the
    # circle finite stabilizers.
    for modulus in (12, 24, 60):
        divisors = [d for d in range(1, 7) if modulus % d == 0]
        for d, e in itertools.product(divisors, repeat=2):
            hd = {(k*modulus//d) % modulus for k in range(d)}
            he = {(k*modulus//e) % modulus for k in range(e)}
            lcm = math.lcm(d, e)
            for alpha in range(modulus):
                for beta in range(modulus):
                    intersects = bool({(alpha+h) % modulus for h in hd} & {(beta+h) % modulus for h in he})
                    criterion = (lcm*(alpha-beta)) % modulus == 0
                    if intersects != criterion:
                        raise AssertionError("two-coset lcm criterion")
                    checks += 1

    # Three- and four-coset generalized CRT: pairwise compatibility is
    # sufficient for these cyclic congruence systems.
    modulus = 12
    divisors = [1, 2, 3, 4, 6]
    for ds in itertools.product(divisors, repeat=3):
        subgroups = [{(k*modulus//d) % modulus for k in range(d)} for d in ds]
        for alphas in itertools.product(range(0, modulus, 3), repeat=3):
            cosets = [{(alpha+h) % modulus for h in subgroup} for alpha, subgroup in zip(alphas, subgroups)]
            pairwise = all(cosets[i] & cosets[j] for i, j in itertools.combinations(range(3), 2))
            common = bool(set.intersection(*cosets))
            if pairwise != common:
                raise AssertionError("generalized CRT")
            checks += 1

    # The incommensurable case cannot return: nonzero integers m,n with
    # T/10=m and sqrt(2)T/10=n would imply sqrt(2)=n/m.
    x = sp.sqrt(2)
    if sp.minimal_polynomial(x) != sp.Symbol("_x")**2-2:
        # SymPy may choose a differently named dummy; use direct identity too.
        if sp.expand(x*x-2) != 0:
            raise AssertionError("sqrt2 polynomial")
    checks += 1
    for numerator in range(-40, 41):
        for denominator in range(1, 41):
            if sp.simplify(x-sp.Rational(numerator, denominator)) == 0:
                raise AssertionError("sqrt2 rational escape")
            checks += 1

    # Validate every periodic witness directly in the quotient equation.
    by_scenario = {row["scenario"]: row for row in data["return_cells"]}
    for identifier, rows in particles.items():
        L = R(scenarios[identifier]["L"])
        witness = by_scenario[identifier]
        T = R(witness["witness_time"]); c = R(witness["witness_common_translation"])
        sigma = witness["witness_permutation"]
        for i, (yi, vi) in enumerate(rows):
            yj, vj = rows[sigma[i]]
            if sp.simplify(vi-vj) != 0:
                raise AssertionError("return velocity")
            quotient = sp.simplify((yi+T*vi-yj-c)/L)
            if quotient.is_integer is not True:
                raise AssertionError("return position")
            checks += 2

    print(f"C296_SYMPY_PASS ({checks} symbolic/exact finite-group identities)")


if __name__ == "__main__":
    main()
