"""Fixed test functions and eigenvalue-only trace evaluation for R401."""

from __future__ import annotations

from dataclasses import dataclass
from math import pi

import numpy as np

from .warped_henon import TWO_PI


@dataclass(frozen=True)
class TraceWindowSpec:
    """Frozen positive-time plateau and compact energy cutoff."""

    time_support_lower: float
    time_plateau_lower: float
    time_plateau_upper: float
    time_support_upper: float
    time_quadrature_order: int
    cutoff_support_lower: float
    cutoff_plateau_lower: float
    cutoff_plateau_upper: float
    cutoff_support_upper: float


def flat_step(values: np.ndarray) -> np.ndarray:
    """C-infinity transition from zero to one on the unit interval."""

    x = np.asarray(values, dtype=float)
    output = np.zeros_like(x)
    output[x >= 1.0] = 1.0
    interior = (x > 0.0) & (x < 1.0)
    left = np.exp(-1.0 / x[interior])
    right = np.exp(-1.0 / (1.0 - x[interior]))
    output[interior] = left / (left + right)
    return output


def energy_cutoff(values: np.ndarray, spec: TraceWindowSpec) -> np.ndarray:
    """Evaluate the fixed compactly supported cutoff chi."""

    energies = np.asarray(values, dtype=float)
    lower = flat_step(
        (energies - spec.cutoff_support_lower)
        / (spec.cutoff_plateau_lower - spec.cutoff_support_lower)
    )
    upper = flat_step(
        (spec.cutoff_support_upper - energies)
        / (spec.cutoff_support_upper - spec.cutoff_plateau_upper)
    )
    return lower * upper


def time_cutoff(values: np.ndarray, spec: TraceWindowSpec) -> np.ndarray:
    """Evaluate the frozen C-infinity positive-time cutoff hat(g)."""

    times = np.asarray(values, dtype=float)
    lower = flat_step(
        (times - spec.time_support_lower)
        / (spec.time_plateau_lower - spec.time_support_lower)
    )
    upper = flat_step(
        (spec.time_support_upper - times)
        / (spec.time_support_upper - spec.time_plateau_upper)
    )
    return lower * upper


def inverse_fourier_test_function(
    scaled_energies: np.ndarray,
    spec: TraceWindowSpec,
) -> np.ndarray:
    """Evaluate g(s)=(2*pi)^-1 int exp(i*t*s) hat(g)(t) dt."""

    if not (
        0.0
        < spec.time_support_lower
        < spec.time_plateau_lower
        <= spec.time_plateau_upper
        < spec.time_support_upper
        < 1.0
    ):
        raise ValueError("invalid positive-time support/plateau ordering")
    nodes, weights = np.polynomial.legendre.leggauss(spec.time_quadrature_order)
    midpoint = 0.5 * (spec.time_support_lower + spec.time_support_upper)
    half_width = 0.5 * (spec.time_support_upper - spec.time_support_lower)
    times = midpoint + half_width * nodes
    integration_weights = half_width * weights * time_cutoff(times, spec)
    phases = np.exp(
        1.0j * np.outer(times, np.asarray(scaled_energies, dtype=float))
    )
    return (integration_weights @ phases) / TWO_PI


def filtered_spectral_density(
    eigenvalues: np.ndarray,
    *,
    target_energy: float,
    hbar: float,
    window: TraceWindowSpec,
) -> complex:
    """Compute sum chi(lambda)^2 g((E-lambda)/hbar)."""

    values = np.asarray(eigenvalues, dtype=float)
    chi = energy_cutoff(values, window)
    active = chi > 0.0
    scaled = (target_energy - values[active]) / hbar
    g_values = inverse_fourier_test_function(scaled, window)
    return complex(np.sum(chi[active] ** 2 * g_values))


def predicted_fast_orbit_term(
    *,
    hbar: float,
    action: float,
    period: float,
    stability_determinant: float,
    transformed_test_value: float = 1.0,
) -> complex:
    """A4.10 positive-time term in the project's Fourier convention."""

    amplitude = (
        transformed_test_value
        * period
        / (TWO_PI * np.sqrt(stability_determinant))
    )
    return complex(1.0j * amplitude * np.exp(1.0j * action / hbar))


def ordered_spectrum_difference(
    reference: np.ndarray,
    comparison: np.ndarray,
    *,
    upper_energy: float,
) -> dict[str, float | int]:
    """Compare two sorted low spectra by index below a common ceiling."""

    first = np.asarray(reference, dtype=float)
    second = np.asarray(comparison, dtype=float)
    count = min(
        int(np.searchsorted(first, upper_energy, side="right")),
        int(np.searchsorted(second, upper_energy, side="right")),
    )
    if count == 0:
        raise ValueError("no ordered eigenvalues lie below upper_energy")
    differences = first[:count] - second[:count]
    return {
        "compared_eigenvalues": count,
        "max_absolute_difference": float(np.max(np.abs(differences))),
        "median_absolute_difference": float(np.median(np.abs(differences))),
        "signed_mean_difference": float(np.mean(differences)),
    }


def wrapped_phase(value: complex) -> float:
    """Return the principal argument in (-pi, pi]."""

    return float(np.angle(value))


def r401_window_delta_0p05(order: int = 512) -> TraceWindowSpec:
    """Return the exploratory delta=0.05 test data."""

    bottom = 2.0 * pi
    return TraceWindowSpec(
        time_support_lower=0.05,
        time_plateau_lower=0.15,
        time_plateau_upper=0.68,
        time_support_upper=0.745,
        time_quadrature_order=order,
        cutoff_support_lower=bottom + 0.020,
        cutoff_plateau_lower=bottom + 0.025,
        cutoff_plateau_upper=bottom + 0.075,
        cutoff_support_upper=bottom + 0.080,
    )


def r401_window_delta_0p01(order: int = 512) -> TraceWindowSpec:
    """Return the preregistered R401-SC delta=0.01 test data."""

    bottom = 2.0 * pi
    return TraceWindowSpec(
        time_support_lower=0.05,
        time_plateau_lower=0.15,
        time_plateau_upper=0.68,
        time_support_upper=0.745,
        time_quadrature_order=order,
        cutoff_support_lower=bottom + 0.002,
        cutoff_plateau_lower=bottom + 0.004,
        cutoff_plateau_upper=bottom + 0.016,
        cutoff_support_upper=bottom + 0.018,
    )
