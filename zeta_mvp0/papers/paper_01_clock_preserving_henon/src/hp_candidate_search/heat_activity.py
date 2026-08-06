"""Deterministic R300 calculations for the Hénon relative heat carrier.

The functions in this module evaluate the exact first-gradient carrier.  The
separate R300-P1 Brownian-bridge proof certifies that the omitted relative
heat-trace terms are ``O(t log(1/t)^4)``; this module remains a calculator for
the exact carrier rather than a numerical evaluator of the full heat trace.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import exp, log, pi, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import digamma


@dataclass(frozen=True)
class HeatActivityRecord:
    t: float
    lam: float
    log_clock: float
    a1: float
    a2: float
    exact_bracket: float
    raw_polar_bracket: float
    identity_relative_error: float
    asymptotic_bracket: float
    bracket_over_log_squared: float
    formal_relative_heat_carrier: float

    def to_dict(self) -> dict[str, float]:
        return asdict(self)


def centered_fixed_point(a: float) -> float:
    """Return r_a used by the centered one-step Hénon warp."""

    if a <= -1.0:
        raise ValueError("a must exceed -1")
    return 1.0 / (1.0 + sqrt(1.0 + float(a)))


def euler_gamma() -> float:
    """Return Euler's constant without depending on a platform constant."""

    return float(-digamma(1.0))


def asymptotic_constants(a: float) -> dict[str, float]:
    """Return the frozen coefficient, beta, and kappa for R300."""

    a = float(a)
    r = centered_fixed_point(a)
    gamma = euler_gamma()
    coefficient = -(a * a) / (24.0 * pi)
    beta = 2.0 * (1.0 - gamma) + 4.0 * pi * r * r
    kappa = (
        pi * pi / 6.0
        - 2.0 * gamma
        + gamma * gamma
        + 4.0 * pi * r * r * (1.0 - gamma)
    )
    return {
        "a": a,
        "r_a": r,
        "euler_gamma": gamma,
        "coefficient": coefficient,
        "beta": beta,
        "kappa": kappa,
    }


def logarithmic_moment(t: float, order: int) -> float:
    """Evaluate A_order(lambda) by one-dimensional adaptive quadrature."""

    t = float(t)
    if t <= 0.0:
        raise ValueError("t must be positive")
    if order not in (1, 2):
        raise ValueError("R300 uses only moments one and two")
    lam = 2.0 * pi * t
    log_clock = log(1.0 / lam)

    def integrand(w: float) -> float:
        return w * exp(-w) * (log_clock + log(w)) ** order

    value, error = quad(
        integrand,
        lam,
        np.inf,
        epsabs=2.0e-12,
        epsrel=2.0e-13,
        limit=300,
    )
    if not np.isfinite(value) or error > 5.0e-10 * max(1.0, abs(value)):
        raise RuntimeError(f"adaptive moment quadrature failed: value={value}, error={error}")
    return float(value)


def exact_bracket(t: float, a: float) -> tuple[float, float, float]:
    """Return A1, A2, and A2+4*pi*r_a^2*A1."""

    a1 = logarithmic_moment(t, 1)
    a2 = logarithmic_moment(t, 2)
    r = centered_fixed_point(a)
    return a1, a2, float(a2 + 4.0 * pi * r * r * a1)


def raw_polar_bracket(t: float, a: float, theta_order: int = 96) -> float:
    """Evaluate t^2(I_a-I_0)/(2a^2) before angular cancellation.

    The integral retains the full matrix action D Psi_a^T z.  Gauss--Legendre
    nodes integrate the angular variable, while scipy.quad integrates
    zeta=pi*rho^2.  This is intentionally distinct from ``exact_bracket``.
    """

    t = float(t)
    a = float(a)
    if t <= 0.0:
        raise ValueError("t must be positive")
    if a == 0.0:
        raise ValueError("raw relative bracket is normalized by a^2")
    if theta_order < 16:
        raise ValueError("theta_order must be at least 16")

    r = centered_fixed_point(a)
    lam = 2.0 * pi * t
    log_clock = log(1.0 / lam)
    nodes, weights = leggauss(theta_order)
    theta = pi * (nodes + 1.0)
    theta_weights = pi * weights
    cosine = np.cos(theta)
    sine = np.sin(theta)
    log_prefactor = log(4.0 * pi**3 / (a * a)) + 2.0 * log(t)

    def radial_integrand(zeta: float) -> float:
        rho = sqrt(max(0.0, zeta) / pi)
        u = rho * cosine
        v = rho * sine
        derivative = -2.0 * a * (r + v)
        transformed_first = derivative * u + v
        transformed_second = -u
        delta = (
            transformed_first * transformed_first
            + transformed_second * transformed_second
            - u * u
            - v * v
        )
        angular_integral = float(np.dot(theta_weights, delta))
        exponential_argument = (
            log_prefactor + 2.0 * zeta - lam * exp(min(zeta, 700.0))
        )
        if exponential_argument < -745.0:
            return 0.0
        return exp(exponential_argument) * angular_integral

    upper = max(40.0, log_clock + 35.0)
    points = sorted({0.0, max(0.0, log_clock), max(0.0, log_clock + log(2.0)), upper})
    total = 0.0
    total_error = 0.0
    for left, right in zip(points[:-1], points[1:]):
        if right <= left:
            continue
        value, error = quad(
            radial_integrand,
            left,
            right,
            epsabs=2.0e-11,
            epsrel=2.0e-11,
            limit=250,
        )
        total += value
        total_error += error
    if not np.isfinite(total) or total_error > 2.0e-8 * max(1.0, abs(total)):
        raise RuntimeError(f"raw polar quadrature failed: value={total}, error={total_error}")
    return float(total)


def evaluate_record(t: float, a: float = 51.0 / 50.0) -> HeatActivityRecord:
    """Evaluate one frozen R300 time cell."""

    a1, a2, bracket = exact_bracket(t, a)
    raw = raw_polar_bracket(t, a)
    relative_error = abs(raw - bracket) / abs(bracket)
    constants = asymptotic_constants(a)
    lam = 2.0 * pi * float(t)
    log_clock = log(1.0 / lam)
    asymptotic = log_clock**2 + constants["beta"] * log_clock + constants["kappa"]
    carrier = constants["coefficient"] * bracket
    return HeatActivityRecord(
        t=float(t),
        lam=lam,
        log_clock=log_clock,
        a1=a1,
        a2=a2,
        exact_bracket=bracket,
        raw_polar_bracket=raw,
        identity_relative_error=relative_error,
        asymptotic_bracket=asymptotic,
        bracket_over_log_squared=bracket / (log_clock * log_clock),
        formal_relative_heat_carrier=carrier,
    )
