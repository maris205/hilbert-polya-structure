#!/usr/bin/env python3
"""Finite, non-certified sanity checks for candidate B; prints canonical JSON.

No producer/imported evidence, target-zero input, or network access is used.
Exact SymPy constants, high-precision endpoint bounds, exact-propagation
shooting, and a separately assembled finite-element form have different roles.
Floating numerical agreement is not an interval certificate of infinite spectra.
"""

import json
import math

import mpmath as mp
import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def symbolic_constants():
    kap = sp.symbols("kappa", positive=True)
    d = sp.symbols("d", real=True, nonzero=True)
    c = kap * sp.exp(-sp.EulerGamma) / sp.pi
    ck = sp.log(4 * sp.pi / kap) + sp.EulerGamma - 2
    comparator = sp.expand_log(sp.log(4 / c) - 2 - ck, force=True)
    heat = sp.expand_log(sp.polygamma(0, sp.Rational(3, 2)) + ck
                         - sp.log(sp.pi / kap), force=True)
    principal = sp.expand((d + sp.Rational(1, 2)) / d**2
                          + (d + sp.Rational(1, 2)) * ck / d
                          - 1 / (2 * d**2) - (1 + ck / 2) / d - ck)
    results = [sp.simplify(x) for x in (comparator, heat, principal)]
    require(all(x == 0 for x in results), "Symbolic constant mismatch")
    return {"identities": 3, "remainders": [str(x) for x in results]}


def high_precision_bounds():
    mp.mp.dps = 70
    h = mp.mpf(0)
    maximum = mp.mpf(0)
    for n in range(1, 1001):
        left = mp.exp(h - mp.euler)
        h += mp.mpf(1) / n
        right = mp.exp(h - mp.euler)
        deviation = max(abs(n - left), abs(n - right))
        require(deviation < 1, "Harmonic endpoint bound fails")
        maximum = max(maximum, deviation)

    # f(x)=x exp(-a x) on [0, x_N]. The proof's global RHS is
    # 2*kappa*||f||*||f'||=kappa/(2*a^2). Integrals are evaluated by
    # an explicit antiderivative, not by the sampled endpoint sum.
    a, kap, count = mp.mpf("0.4"), mp.mpf("1.5"), 1200
    h, sampled, averaged = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    lam = 2 * a

    def antiderivative(x):
        return -mp.exp(-lam*x)*(x*x/lam+2*x/lam**2+2/lam**3)

    for n in range(1, count + 1):
        left = mp.pi * h
        h += mp.mpf(1) / n
        right = mp.pi * h
        sampled += kap * right**2 * mp.exp(-2*a*right)
        averaged += kap*n/mp.pi*(antiderivative(right)-antiderivative(left))
    error, bound = abs(sampled-averaged), kap/(2*a*a)
    require(error <= bound, "Finite sampling estimate fails")
    return {"decimal_digits": 70, "harmonic_endpoint_pairs": 1000,
            "max_endpoint_deviation": mp.nstr(maximum, 25),
            "sampling_cells": count,
            "sampling_absolute_difference": mp.nstr(error, 25),
            "sampling_global_bound": mp.nstr(bound, 25)}


def shooting_counts(kap, k, cells):
    """Exact free rotations and delta shears, rounded in binary64.

    y = r sin(theta), y'/k = r cos(theta). The right endpoint delta
    does not change a Dirichlet count, and its shear makes the Robin
    condition y'(X)+kappa*y(X)=0 into cos(theta)=0.
    """
    theta = 0.0
    for n in range(1, cells + 1):
        theta += k * math.pi / n
        sn, cs = math.sin(theta), math.cos(theta)
        change = math.atan2(sn, cs + kap / k * sn) - math.atan2(sn, cs)
        change = (change + math.pi) % (2 * math.pi) - math.pi
        theta += change
    fraction = theta / math.pi
    return {"dirichlet": math.floor(fraction),
            "robin": math.floor(fraction + 0.5),
            "end_phase_fraction": round(fraction % 1, 12)}


def finite_element_counts(kap, k, cells, phase_bound):
    """Independent form discretization, without transfer matrices or trig.

    Assemble the piecewise-linear stiffness and consistent mass matrices
    of the first `cells` intervals. A true vertex has the exact delta
    energy kappa*|f(vertex)|^2. Count negative LDL pivots of K-k^2*M.
    This approximates strict finite-interval counts; selected test energies
    are numerically separated from thresholds but not interval-certified.
    """
    lengths, penalties = [], [0.0]
    for n in range(1, cells + 1):
        subdivisions = max(1, math.ceil(k * math.pi / (n * phase_bound)))
        step = math.pi / (n * subdivisions)
        for j in range(subdivisions):
            lengths.append(step)
            penalties.append(kap if j + 1 == subdivisions else 0.0)

    total = len(lengths)

    def inertia(terminal_robin):
        last = total if terminal_robin else total - 1
        neg, previous, min_relative = 0, None, 1.0
        for node in range(1, last + 1):
            left = lengths[node - 1]
            if node < total:
                right = lengths[node]
                diagonal = 1/left+1/right-k*k*(left+right)/3+penalties[node]
            else:
                diagonal = 1/left-k*k*left/3+penalties[node]
            if previous is None:
                pivot = diagonal
            else:
                off = -1/left-k*k*left/6
                pivot = diagonal-off*off/previous
            require(math.isfinite(pivot) and pivot != 0, "Invalid LDL pivot")
            relative = abs(pivot) / max(1.0, abs(diagonal))
            min_relative = min(min_relative, relative)
            neg += pivot < 0
            previous = pivot
        return neg, min_relative

    dcount, dmargin = inertia(False)
    rcount, rmargin = inertia(True)
    return {"dirichlet": dcount, "robin": rcount,
            "elements": total, "max_free_phase": phase_bound,
            "min_relative_ldl_pivot": round(min(dmargin, rmargin), 12)}


def spectral_sanity():
    cases = []
    for kap in (0.5, 1.0, 2.0):
        for k in (10.0, 20.0, 40.0):
            cells = math.ceil(4*math.pi*(k*k+kap*kap+1)/kap)
            shoot = shooting_counts(kap, k, cells)
            doubled = shooting_counts(kap, k, 2*cells)
            fem = finite_element_counts(kap, k, cells, 0.08)
            refined = finite_element_counts(kap, k, cells, 0.04)
            fine = finite_element_counts(kap, k, cells, 0.02)
            finest = finite_element_counts(kap, k, cells, 0.01)
            counts = [(x["dirichlet"], x["robin"])
                      for x in (shoot, doubled, fine, finest)]
            require(len(set(counts)) == 1, "Independent finite counts disagree")
            require(shoot["dirichlet"] == shoot["robin"],
                    "Head boundary bracket not closed numerically")
            ck = math.log(4*math.pi/kap) + float(mp.euler) - 2
            predicted = 2*k*math.log(k)+ck*k
            # On the split tail the sampling estimate gives the rigorous
            # symbolic lower form bound kappa*(N+1)/pi-2*kappa^2.
            tail_lower = kap*(cells+1)/math.pi-2*kap*kap
            require(tail_lower > k*k, "Chosen tail cutoff too short")
            cases.append({"kappa": kap, "frequency": k, "cells": cells,
                          "tail_lower_over_energy": round(tail_lower/(k*k), 9),
                          "shooting": shoot, "shooting_double_cutoff": doubled,
                          "finite_elements": fem, "refined_finite_elements": refined,
                          "fine_finite_elements": fine, "finest_finite_elements": finest,
                          "coarse_levels_agree": all(
                              x["dirichlet"] == shoot["dirichlet"] and
                              x["robin"] == shoot["robin"] for x in (fem, refined)),
                          "two_term_prediction": round(predicted, 9),
                          "count_minus_prediction": round(shoot["dirichlet"]-predicted, 9)})
    return cases


def divisor_sanity():
    rows = []
    for k in (1, 2, 10, 100, 1000):
        direct = sum(k // n for n in range(1, k + 1))
        root = math.isqrt(k)
        hyperbola = 2*sum(k // n for n in range(1, root + 1))-root*root
        require(direct == hyperbola, "Exact divisor identity fails")
        rows.append({"integer_frequency": k, "pair_count": direct,
                     "hyperbola_count": hyperbola})
    return rows


def main():
    result = {"scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
              "status": "FINITE_SANITY_PASS_NOT_INTERVAL_CERTIFIED",
              "dependencies": {"sympy": sp.__version__, "mpmath": mp.__version__},
              "limitations": ["No infinite-spectrum numerical certificate.",
                              "No fitted theorem or target-zero data.",
                              "No global novelty certification.",
                              "All floating comparisons are finite sanity checks."],
              "symbolic_constants": symbolic_constants(),
              "high_precision_bounds": high_precision_bounds(),
              "spectral_cases": spectral_sanity(),
              "exact_divisor_cases": divisor_sanity()}
    print(json.dumps(result, sort_keys=True, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
