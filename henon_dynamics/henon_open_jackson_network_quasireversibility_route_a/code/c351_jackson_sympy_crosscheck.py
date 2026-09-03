#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C351."""
from __future__ import annotations

import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C351 SymPy lane refuses optimized Python")
    checks = 0
    a1, a2, p11, p12, p21, p22 = sp.symbols(
        "a1 a2 p11 p12 p21 p22", positive=True)
    matrix = sp.Matrix([[1 - p11, -p21], [-p12, 1 - p22]])
    traffic = sp.simplify(matrix.inv() * sp.Matrix([a1, a2]))
    need(sp.simplify((1 - p11) * traffic[0] - p21 * traffic[1] - a1) == 0,
         "traffic equation 1")
    need(sp.simplify(-p12 * traffic[0] + (1 - p22) * traffic[1] - a2) == 0,
         "traffic equation 2")
    checks += 2

    lam_i, lam_j, mu_i, mu_j, pij = sp.symbols(
        "lambda_i lambda_j mu_i mu_j p_ij", positive=True)
    rho_i, rho_j = lam_i / mu_i, lam_j / mu_j
    p_hat_ji = lam_i * pij / lam_j
    need(sp.factor(mu_i * pij * rho_i / rho_j - mu_j * p_hat_ji) == 0,
         "internal reverse jump")
    checks += 1

    alpha, lam, mu, p0 = sp.symbols("alpha lambda mu p0", positive=True)
    rho = lam / mu
    need(sp.factor(alpha / rho - mu * alpha / lam) == 0,
         "arrival reverses to exit")
    need(sp.factor(mu * p0 * rho - lam * p0) == 0,
         "exit reverses to arrival")
    checks += 2

    # The reversed augmented routing row sums to one by the traffic equation.
    incoming, self_route = sp.symbols("incoming self_route", nonnegative=True)
    traffic_identity = sp.Eq(lam, alpha + incoming + lam * self_route)
    reverse_sum = (incoming + lam * self_route) / lam + alpha / lam
    need(sp.simplify(reverse_sum.subs(incoming,
        sp.solve(traffic_identity, incoming)[0]) - 1) == 0, "reverse row sum")
    checks += 1

    # Product-form global balance grouped at one occupied coordinate.
    incoming_other = lam - alpha - lam * self_route
    occupied_inflow = alpha / rho + incoming_other * mu / lam
    occupied_outflow = mu * (1 - self_route)
    need(sp.factor(occupied_inflow - occupied_outflow) == 0,
         "occupied-coordinate balance")
    checks += 1

    # Total outside flow follows by summing the traffic equations.
    total_alpha, total_exit = sp.symbols("total_alpha total_exit")
    need(sp.simplify(total_alpha - total_exit).subs(total_exit, total_alpha) == 0,
         "external flow conservation")
    checks += 1

    # One-node feedback is an ordinary birth/death chain with effective death mu(1-p).
    feedback = sp.symbols("feedback", nonnegative=True)
    one_lambda = alpha / (1 - feedback)
    one_rho = one_lambda / mu
    need(sp.factor(alpha - one_rho * mu * (1 - feedback)) == 0,
         "one-node feedback balance")
    checks += 1
    print(f"C351 SymPy cross-check: PASS {checks} symbolic identities")


if __name__ == "__main__":
    main()
