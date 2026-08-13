#!/usr/bin/env python3
"""Generate primitive-count, multiplier-lattice, and boundary-quotient panels.

All plotted values come from results/ledger.json.  Frozen formula conventions
are cross-checked against experiments/source_lock.json before rendering.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from paper_plot_style import COLORS, panel_label, save_figure


FIGURE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = FIGURE_DIR.parents[1]


def load_json(relative: str) -> dict:
    return json.loads((PROJECT_ROOT / relative).read_text(encoding="utf-8"))


def main() -> None:
    ledger = load_json("results/ledger.json")
    lock = load_json("experiments/source_lock.json")
    rows = ledger["cycle_rows"]
    quotient = ledger["parent_boundary_quotient"]

    periods = np.array([row["period"] for row in rows], dtype=int)
    sft_counts = np.array(ledger["primitive_counts"], dtype=int)
    parent_counts = np.array(quotient["parent_primitive_orbit_counts"], dtype=int)
    delta = np.array(quotient["primitive_count_delta"], dtype=int)
    assert np.array_equal(sft_counts, np.array([row["primitive_count"] for row in rows]))
    assert np.array_equal(parent_counts - sft_counts, delta)
    assert np.flatnonzero(delta).tolist() == [0, 1]
    assert delta[:2].tolist() == [1, -1]
    assert ledger["ledger_scope"] == "unquotiented constant-slope SFT/baker"
    assert quotient["sole_declared_collapse_verified"]
    assert lock["pretest_exact_predictions"]["unsigned_zeta"] == "1/(1-2*z^2)"
    assert lock["pretest_exact_predictions"]["parent_core_zeta"] == "(1+z)/(1-2*z^2)"

    even_rows = [row for row in rows if row["unstable_multiplier_modulus"] is not None]
    even_periods = np.array([row["period"] for row in even_rows], dtype=int)
    unstable = np.array(
        [float(Fraction(row["unstable_multiplier_modulus"])) for row in even_rows]
    )
    stable = np.array(
        [float(Fraction(row["stable_multiplier_modulus"])) for row in even_rows]
    )
    assert np.all(even_periods % 2 == 0)
    assert np.allclose(stable * unstable, 1.0, rtol=0.0, atol=0.0)
    unstable_exponents = np.array([math.log2(value) for value in unstable])
    stable_exponents = np.array([math.log2(value) for value in stable])
    assert np.array_equal(unstable_exponents, even_periods / 2)
    assert np.array_equal(stable_exponents, -even_periods / 2)

    fig, axes = plt.subplots(
        1, 3, figsize=(7.05, 2.68),
        gridspec_kw={"width_ratios": (1.35, 1.10, 1.05)},
    )
    ax_counts, ax_lattice, ax_quotient = axes

    # (a) Discrete primitive-orbit counts, with small horizontal offsets so
    # coincident SFT and parent values remain visible.
    ax_counts.vlines(periods - 0.10, 0, sft_counts, color=COLORS["blue"],
                     linewidth=1.0, alpha=0.88)
    ax_counts.scatter(periods - 0.10, sft_counts, s=17, color=COLORS["blue"],
                      marker="o", label="SFT/baker", zorder=3)
    ax_counts.vlines(periods + 0.10, 0, parent_counts, color=COLORS["orange"],
                     linewidth=1.0, linestyle=(0, (2, 1)), alpha=0.88)
    ax_counts.scatter(periods + 0.10, parent_counts, s=21, facecolor="white",
                      edgecolor=COLORS["orange"], linewidth=1.0, marker="s",
                      label="parent quotient", zorder=4)
    ax_counts.set_yscale("symlog", linthresh=1, linscale=0.7, base=10)
    ax_counts.set_xlim(0.4, 20.6)
    ax_counts.set_ylim(-0.08, 150)
    ax_counts.set_xticks([1, 5, 10, 15, 20])
    ax_counts.set_yticks([0, 1, 2, 10, 100])
    ax_counts.set_yticklabels(["0", "1", "2", "10", "100"])
    ax_counts.set_xlabel("primitive period $n$")
    ax_counts.set_ylabel("primitive orbit count")
    ax_counts.legend(frameon=False, loc="upper left", handletextpad=0.35,
                     borderaxespad=0.4)
    panel_label(ax_counts, "a")

    # (b) Exact reciprocal multiplier lattice of the unquotiented carrier.
    ax_lattice.axhline(0, color=COLORS["light_gray"], linewidth=0.8)
    ax_lattice.plot(even_periods, unstable_exponents, color=COLORS["blue"],
                    marker="o", label="unstable")
    ax_lattice.plot(even_periods, stable_exponents, color=COLORS["orange"],
                    marker="^", linestyle=(0, (3, 2)), label="stable")
    for n, y_hi, y_lo in zip(even_periods, unstable_exponents, stable_exponents):
        ax_lattice.vlines(n, y_lo, y_hi, color=COLORS["light_gray"],
                          linewidth=0.45, zorder=0)
    ax_lattice.set_xlim(1, 21)
    ax_lattice.set_ylim(-11, 11)
    ax_lattice.set_xticks([2, 6, 10, 14, 18])
    ax_lattice.set_yticks([-10, -5, 0, 5, 10])
    ax_lattice.set_xlabel("SFT/baker period $n=2k$")
    ax_lattice.set_ylabel(r"$\log_2 |\Lambda|$")
    ax_lattice.text(
        0.50, 0.04, r"$\log_2|\Lambda_{u,s}|=\pm k$",
        transform=ax_lattice.transAxes, ha="center", va="bottom", fontsize=7.8,
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.3},
    )
    ax_lattice.legend(frameon=False, loc="upper left", handlelength=1.4,
                      labelspacing=0.25)
    panel_label(ax_lattice, "b")

    # (c) The quotient correction is a primitive-ledger delta, kept separate
    # from the SFT multiplier data in panel (b).
    ax_quotient.axhline(0, color=COLORS["black"], linewidth=0.7)
    nonzero = np.flatnonzero(delta)
    colors = [COLORS["green"] if delta[index] > 0 else COLORS["orange"]
              for index in nonzero]
    ax_quotient.vlines(periods[nonzero], 0, delta[nonzero], color=colors,
                       linewidth=1.5)
    ax_quotient.scatter(periods[nonzero], delta[nonzero], s=28, color=colors,
                        zorder=3)
    ax_quotient.scatter(periods[2:], delta[2:], s=8, color=COLORS["light_gray"],
                        zorder=2)
    ax_quotient.set_xlim(0.4, 20.6)
    ax_quotient.set_ylim(-1.45, 1.55)
    ax_quotient.set_xticks([1, 5, 10, 15, 20])
    ax_quotient.set_yticks([-1, 0, 1])
    ax_quotient.set_xlabel("period $n$")
    ax_quotient.set_ylabel(r"$P_n^{\rm parent}-P_n^{\rm SFT}$")
    removed = r"$%s\!\leftrightarrow\!%s$ ghost" % tuple(
        quotient["removed_symbolic_cycle"]
    )
    added = rf"$+\,{quotient['added_parent_fixed_label']}$ fixed point"
    ax_quotient.text(1.55, 1.03, added, color=COLORS["green"], fontsize=7.3,
                     ha="left", va="center")
    ax_quotient.text(2.55, -0.98, removed, color=COLORS["orange"], fontsize=7.3,
                     ha="left", va="center")
    ax_quotient.text(
        0.50, 0.61,
        r"$\zeta_{\rm SFT}(z)=\dfrac{1}{1-2z^2}$"
        "\n" r"$\zeta_{\rm parent}(z)=\dfrac{1+z}{1-2z^2}$",
        transform=ax_quotient.transAxes, ha="center", va="center", fontsize=8.0,
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white",
              "edgecolor": COLORS["gray"], "linewidth": 0.6},
    )
    panel_label(ax_quotient, "c")

    for ax in axes:
        ax.tick_params(direction="out", length=3, width=0.7)
    fig.subplots_adjust(wspace=0.38)
    save_figure(fig, "fig2_orbit_lattice")


if __name__ == "__main__":
    main()
