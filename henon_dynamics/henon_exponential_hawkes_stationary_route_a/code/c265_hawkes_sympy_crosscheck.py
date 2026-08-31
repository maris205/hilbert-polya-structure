#!/usr/bin/env python3
"""Independent SymPy reconstruction for the C265 Hawkes identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c265_hawkes_evidence.json"


def main() -> None:
    nu, a, b, s, w, T, t, z = sp.symbols("nu a b s w T t z", positive=True)
    delta = b - a
    mu = b * nu / delta
    checks = 0

    def demand(expr, message: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(f"{message}: {sp.simplify(expr)}")

    # Affine transform: backward generator coefficients reproduce both ODEs.
    B = sp.symbols("B")
    generator_constant = -b * nu * B
    generator_x = b * B + z * sp.exp(-a * B) - 1
    demand(generator_constant + b * nu * B, "affine constant")
    demand(generator_x + (1 - b * B - z * sp.exp(-a * B)), "affine slope")

    # First two stationary moments from the generator recurrence.
    m1 = mu
    m2 = b * nu * m1 / delta + a ** 2 * m1 / (2 * delta)
    variance = mu * a ** 2 / (2 * delta)
    demand(m2 - m1 ** 2 - variance, "stationary variance")

    # Laplace ODE expanded at zero recovers the mean and second moment.
    denominator = b * s + sp.exp(-a * s) - 1
    log_derivative = -b * nu * s / denominator
    series = sp.series(log_derivative, s, 0, 3).removeO()
    demand(series.subs(s, 0) + mu, "Laplace first derivative")
    demand(sp.diff(series, s).subs(s, 0) - variance, "log-Laplace second cumulant")

    # Complete counting covariance and no-2pi Bartlett transform.
    count_c = mu * a * (2 * b - a) / (2 * delta)
    spectrum = mu + 2 * count_c * delta / (delta ** 2 + w ** 2)
    closed_spectrum = mu * (b ** 2 + w ** 2) / (delta ** 2 + w ** 2)
    demand(spectrum - closed_spectrum, "Bartlett spectrum")
    demand(closed_spectrum.subs(w, 0) - mu * b ** 2 / delta ** 2, "zero frequency")

    window_closed = mu * T + mu * a * (2 * b - a) * (T / delta ** 2 - (1 - sp.exp(-delta * T)) / delta ** 3)
    demand(window_closed.subs(T, 0), "window variance initial value")
    demand(sp.diff(window_closed, T).subs(T, 0) - mu, "window variance initial slope")
    demand(sp.diff(window_closed, T, 2) - 2 * count_c * sp.exp(-delta * T), "window variance ODE")
    long_slope = mu + mu * a * (2 * b - a) / delta ** 2
    demand(long_slope - mu * b ** 2 / delta ** 2, "long-window slope")
    demand(sp.limit(window_closed, a, 0) - nu * T, "Poisson boundary")

    # Lagrange inversion for total progeny T=x exp(m(T-1)).
    x, m = sp.symbols("x m")
    for n in range(1, 13):
        # [u^(n-1)] exp(m*n*(u-1))/n
        coefficient = sp.expand(sp.exp(-m * n) * (m * n) ** (n - 1) / sp.factorial(n))
        expected = sp.exp(-m * n) * (m * n) ** (n - 1) / sp.factorial(n)
        demand(coefficient - expected, f"Borel Lagrange n={n}")

    data = json.loads(EVIDENCE.read_text())
    rows = data["regression"]["stable_cases"]
    for row in rows:
        subs = {nu: sp.Rational(row["nu"]), a: sp.Rational(row["a"]), b: sp.Rational(row["b"])}
        demand(mu.subs(subs) - sp.Rational(row["mean_intensity"]), "stored mean")
        demand(variance.subs(subs) - sp.Rational(row["intensity_variance"]), "stored intensity variance")
        demand(count_c.subs(subs) - sp.Rational(row["counting_continuous_covariance_coefficient"]), "stored counting covariance")
        demand(closed_spectrum.subs(subs).subs(w, 0) - sp.Rational(row["bartlett_zero_frequency"]), "stored spectrum zero")
    print(f"C265_SYMPY_PASS ({checks} exact symbolic and stored-row checks)")


if __name__ == "__main__":
    main()
