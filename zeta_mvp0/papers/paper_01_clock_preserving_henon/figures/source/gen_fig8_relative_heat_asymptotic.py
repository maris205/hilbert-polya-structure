#!/usr/bin/env python3
"""Generate the analytic relative-heat figure from the archived R300 table."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results" / "r300_heat_activity" / "records.csv"
OUTPUT_PDF = ROOT / "figures" / "fig8_relative_heat_asymptotic.pdf"
OUTPUT_PNG = ROOT / "figures" / "fig8_relative_heat_asymptotic.png"


def read_records() -> dict[str, np.ndarray]:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise RuntimeError(f"no records in {INPUT}")
    columns = {
        key: np.asarray([float(row[key]) for row in rows], dtype=float)
        for key in rows[0]
    }
    order = np.argsort(columns["log_clock"])
    return {key: value[order] for key, value in columns.items()}


def main() -> None:
    data = read_records()
    a = 51.0 / 50.0
    r_a = 1.0 / (1.0 + math.sqrt(1.0 + a))
    gamma = float(np.euler_gamma)
    beta = 2.0 * (1.0 - gamma) + 4.0 * math.pi * r_a**2
    kappa = (
        math.pi**2 / 6.0
        - 2.0 * gamma
        + gamma**2
        + 4.0 * math.pi * r_a**2 * (1.0 - gamma)
    )
    residual_limit = math.pi**2 * (4.0 * math.pi * r_a**2 - 1.0)

    clock = data["log_clock"]
    lam = data["lam"]
    exact = data["exact_bracket"]
    scaled_exact = exact / clock**2
    dense_clock = np.linspace(float(clock.min()), float(clock.max()), 400)
    dense_scaled_asymptotic = (
        dense_clock**2 + beta * dense_clock + kappa
    ) / dense_clock**2

    # Evaluate the O(t^2) lower-tail residual without subtracting two
    # O(L^2) floating-point numbers.  After w=lambda*u,
    # mathcal(B)_a-P_a=lambda^2[-I_2-4*pi*r_a^2*I_1], where
    # I_k=int_0^1 u*exp(-lambda*u)*(log u)^k du.
    scaled_residual_values = []
    for value in lam:
        i1 = quad(
            lambda u: u * math.exp(-value * u) * math.log(u) if u else 0.0,
            0.0,
            1.0,
            epsabs=2.0e-14,
            epsrel=2.0e-14,
            limit=200,
        )[0]
        i2 = quad(
            lambda u: u * math.exp(-value * u) * math.log(u) ** 2 if u else 0.0,
            0.0,
            1.0,
            epsabs=2.0e-14,
            epsrel=2.0e-14,
            limit=200,
        )[0]
        scaled_residual_values.append(
            4.0 * math.pi**2 * (-i2 - 4.0 * math.pi * r_a**2 * i1)
        )
    scaled_residual = np.asarray(scaled_residual_values)

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 9.4,
            "axes.labelsize": 10,
            "axes.titlesize": 10,
            "legend.fontsize": 8.4,
            "xtick.labelsize": 8.5,
            "ytick.labelsize": 8.5,
            "axes.linewidth": 0.8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    fig, axes = plt.subplots(1, 2, figsize=(7.25, 2.85))

    ax = axes[0]
    ax.plot(
        dense_clock,
        dense_scaled_asymptotic,
        color="#1f4e79",
        linewidth=1.8,
        label=r"$1+\beta_a/L+\kappa_a/L^2$",
        zorder=2,
    )
    ax.scatter(
        clock,
        scaled_exact,
        s=28,
        facecolor="#f28e2b",
        edgecolor="white",
        linewidth=0.55,
        label=r"exact $\mathcal{B}_a(t)/L^2$",
        zorder=3,
    )
    ax.axhline(1.0, color="0.35", linestyle="--", linewidth=1.0, label="limit 1")
    ax.set_xlabel(r"$L=\log(1/(2\pi t))$")
    ax.set_ylabel(r"normalized carrier $\mathcal{B}_a(t)/L^2$")
    ax.grid(alpha=0.22, linewidth=0.6)
    ax.legend(frameon=False, loc="upper left")
    ax.text(0.02, 0.04, "(a)", transform=ax.transAxes, fontweight="bold")

    ax = axes[1]
    ax.plot(
        clock,
        scaled_residual,
        marker="o",
        markersize=4.7,
        linewidth=1.6,
        color="#a23b72",
        label="exact scaled residual",
    )
    ax.axhline(
        residual_limit,
        color="0.35",
        linestyle="--",
        linewidth=1.0,
        label=r"$\pi^2(4\pi r_a^2-1)$",
    )
    ax.set_xlabel(r"$L=\log(1/(2\pi t))$")
    ax.set_ylabel(r"$[\mathcal{B}_a-(L^2+\beta_aL+\kappa_a)]/t^2$")
    ax.grid(alpha=0.22, linewidth=0.6)
    ax.legend(frameon=False, loc="lower right")
    ax.text(0.02, 0.04, "(b)", transform=ax.transAxes, fontweight="bold")

    fig.subplots_adjust(left=0.085, right=0.99, bottom=0.22, top=0.97, wspace=0.30)
    fig.savefig(OUTPUT_PDF, bbox_inches="tight")
    fig.savefig(OUTPUT_PNG, dpi=320, bbox_inches="tight")


if __name__ == "__main__":
    main()
