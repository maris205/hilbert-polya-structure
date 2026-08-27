#!/usr/bin/env python3
"""Separate SymPy reconstruction of finite laws and all C208 limit regimes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c208_branching_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(expression, message):
        nonlocal checks
        checks += 1
        if sp.simplify(sp.cancel(expression)) != 0:
            raise AssertionError(message)

    s = sp.symbols("s")
    lam, mu, delta = sp.symbols("lambda mu delta", positive=True)
    rate = lam - mu
    p0 = mu * (1 - delta) / (lam - mu * delta)
    beta = lam * (1 - delta) / (lam - mu * delta)
    finite = p0 + (1 - p0) * (1 - beta) * s / (1 - beta * s)
    raw = (mu * (1 - s) - delta * (mu - lam * s)) / (
        lam * (1 - s) - delta * (mu - lam * s)
    )
    check(finite - raw, "off-critical zero-modified geometric form")
    check(finite.subs(s, 0) - p0, "extinction probability")
    check(finite.subs(s, 1) - 1, "PGF normalization")
    check(finite.subs(delta, 1) - s, "off-critical t=0")
    check(-rate * delta * sp.diff(finite, delta) - (finite - 1) * (lam * finite - mu),
          "off-critical backward equation")
    d1, d2 = sp.symbols("delta_1 delta_2", positive=True)
    f1 = raw.subs(delta, d1)
    f2 = raw.subs(delta, d2)
    check(f1.subs(s, f2) - raw.subs(delta, d1 * d2), "off-critical semigroup")
    mean = sp.diff(finite, s).subs(s, 1)
    factorial_second = sp.diff(finite, s, 2).subs(s, 1)
    variance = factorial_second + mean - mean ** 2
    check(mean - 1 / delta, "off-critical mean")
    check(variance - (lam + mu) / rate / delta * (1 / delta - 1), "off-critical variance")
    check(raw.subs(mu, 0) - delta * s / (1 - (1 - delta) * s), "pure birth")
    check(raw.subs(lam, 0) - (1 - 1 / delta + s / delta), "pure death")

    tau, c = sp.symbols("tau c", positive=True)
    critical = (tau + (1 - tau) * s) / (1 + tau - tau * s)
    critical_p = tau / (1 + tau)
    critical_mixture = critical_p + (1 - critical_p) ** 2 * s / (1 - critical_p * s)
    check(critical - critical_mixture, "critical zero-modified geometric form")
    check(critical.subs(tau, 0) - s, "critical t=0")
    check(critical.subs(s, 1) - 1, "critical normalization")
    check(c * sp.diff(critical, tau) - c * (critical - 1) ** 2, "critical backward equation")
    u, v = sp.symbols("tau_1 tau_2", positive=True)
    check(critical.subs(tau, u).subs(s, critical.subs(tau, v)) - critical.subs(tau, u + v),
          "critical semigroup")
    critical_mean = sp.diff(critical, s).subs(s, 1)
    critical_second = sp.diff(critical, s, 2).subs(s, 1)
    check(critical_mean - 1, "critical mean")
    check(critical_second + critical_mean - critical_mean ** 2 - 2 * tau, "critical variance")

    eps, time = sp.symbols("epsilon time", positive=True)
    near_critical = raw.subs({lam: c + eps, mu: c, delta: sp.exp(-eps * time)})
    check(sp.limit(near_critical, eps, 0, dir="+") - critical.subs(tau, c * time),
          "critical limit of off-critical Mobius law")

    rho, horizon, theta = sp.symbols("rho horizon theta", positive=True)
    beta_sub = rho * (1 - horizon) / (rho - horizon)
    conditional_sub = (1 - beta_sub) * s / (1 - beta_sub * s)
    check(sp.limit(conditional_sub, horizon, sp.oo) - (1 - rho) * s / (1 - rho * s),
          "subcritical quasi-stationary PGF")
    qsd_pgf = (1 - rho) * s / (1 - rho * s)
    subcritical_finite = raw.subs({lam: rho, mu: 1, delta: horizon})
    subcritical_extinction = subcritical_finite.subs(s, 0)
    conditioned_qsd = (
        qsd_pgf.subs(s, subcritical_finite) - qsd_pgf.subs(s, subcritical_extinction)
    ) / (1 - qsd_pgf.subs(s, subcritical_extinction))
    check(conditioned_qsd - qsd_pgf, "subcritical QSD conditional-semigroup invariance")

    scaled_s_critical = sp.exp(-theta / tau)
    conditional_critical = ((1 - critical_p) * scaled_s_critical /
                            (1 - critical_p * scaled_s_critical))
    check(sp.limit(conditional_critical, tau, sp.oo) - 1 / (1 + theta),
          "critical Yaglom Laplace transform")
    for z in range(1, 5):
        critical_z = ((critical.subs(s, scaled_s_critical) ** z - critical_p ** z) /
                      (1 - critical_p ** z))
        check(sp.limit(critical_z, tau, sp.oo) - 1 / (1 + theta),
              f"critical Yaglom transform z={z}")

    scaled_s_super = sp.exp(-theta * delta)
    super_limit = sp.limit(raw.subs(s, scaled_s_super), delta, 0, dir="+")
    expected_super = mu / lam + rate ** 2 / (lam * (rate + lam * theta))
    check(super_limit - expected_super, "supercritical one-ancestor martingale limit")
    q = rate / lam
    check(expected_super - (mu / lam + q * q / (q + theta)), "atom plus exponential")
    for z in range(5):
        mixture = sum(sp.binomial(z, k) * (mu / lam) ** (z - k) * q ** k *
                      (q / (q + theta)) ** k for k in range(z + 1))
        check(expected_super ** z - mixture, f"binomial-gamma mixture z={z}")
    check(sp.limit(delta * (1 / delta), delta, 0) - 1, "scaled mean")
    check(sp.limit(delta ** 2 * (lam + mu) / rate / delta * (1 / delta - 1),
                   delta, 0, dir="+") - (lam + mu) / rate, "scaled variance")

    generic_checks = checks
    evidence_coefficients = 0
    evidence_moments = 0
    for case in data["regression"]["parameter_cases"]:
        p = sp.Rational(case["p0"])
        b = sp.Rational(case["beta"])
        one = p + (1 - p) * (1 - b) * s / (1 - b * s)
        for population in case["population_rows"]:
            z = population["initial_population"]
            series = sp.series(one ** z, s, 0, 13).removeO().expand()
            for n, value in enumerate(population["transition_probabilities_n_0_to_12"]):
                check(series.coeff(s, n) - sp.Rational(value), "evidence transition coefficient")
                evidence_coefficients += 1
            evidence_mean = sp.diff(one ** z, s).subs(s, 1)
            evidence_factorial_second = sp.diff(one ** z, s, 2).subs(s, 1)
            evidence_variance = evidence_factorial_second + evidence_mean - evidence_mean ** 2
            check(evidence_mean - sp.Rational(population["mean"]), "evidence mean")
            check(evidence_variance - sp.Rational(population["variance"]), "evidence variance")
            evidence_moments += 2
    print(json.dumps({
        "status": "C208_SYMPY_PASS",
        "checks": checks,
        "generic_symbolic_checks": generic_checks,
        "evidence_coefficient_checks": evidence_coefficients,
        "evidence_moment_checks": evidence_moments,
        "long_time_regimes": 3,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
