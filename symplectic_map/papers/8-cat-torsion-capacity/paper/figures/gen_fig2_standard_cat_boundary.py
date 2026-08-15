#!/usr/bin/env python3
"""Generate Figure 2: exact standard-cat carrier boundary for n=1,...,12."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from figure_data import boundary_payload, ledger_payload, load_sources
from paper_plot_style import (
    BLACK,
    BLUE,
    GREEN,
    MID_GRAY,
    ORANGE,
    PALE_BLUE,
    PALE_GREEN,
    PALE_ORANGE,
    PALE_RED,
    VERMILLION,
    WHITE,
    panel_label,
    save_figure,
)


STEM = "fig2_standard_cat_boundary"


def factor_math(text: str) -> str:
    """Convert the frozen ASCII factorization to compact math text."""
    compact = text.replace("*", r"\,")
    compact = re.sub(r"\^(\d+)", r"^{\1}", compact)
    return f"${compact}$"


def build_figure():
    raw, _manifest, _proof = load_sources()
    ledger = ledger_payload(raw)
    boundary_data = boundary_payload(raw)
    boundary = boundary_data["boundary"]
    profiles = boundary_data["profiles"]
    exceptions = set(boundary["exception_set"])

    if not all(row["engines_agree"] and row["locked_record_matches"] for row in raw["ledger_records"]):
        raise RuntimeError("one or more exact ledger checks failed")

    fig = plt.figure(figsize=(7.2, 4.35), constrained_layout=False)
    grid = fig.add_gridspec(
        2,
        1,
        height_ratios=(1.48, 1.0),
        left=0.055,
        right=0.985,
        bottom=0.09,
        top=0.92,
        hspace=0.25,
    )

    # (a) Categorical ledger. Magnitude is deliberately not encoded.
    ax = fig.add_subplot(grid[0, 0])
    ax.set_xlim(0.5, 12.5)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    panel_label(ax, "a", "Exact determinant ledger and carrier mechanism")

    for row in ledger:
        n = row["period"]
        left = n - 0.46
        # Ledger tier.
        ax.add_patch(
            Rectangle(
                (left, 0.53),
                0.92,
                0.39,
                facecolor=WHITE,
                edgecolor=MID_GRAY,
                linewidth=0.65,
            )
        )
        ax.text(n, 0.87, rf"$n={n}$", ha="center", va="center", fontsize=6.7, fontweight="bold")
        ax.text(n, 0.73, factor_math(row["factorization_text"]), ha="center", va="center", fontsize=6.35)
        if row["selected_primitive_prime"] is None:
            divisor_label = "new $p$\nnone"
        else:
            divisor_label = "new " + rf"$p={row['selected_primitive_prime']}$"
        ax.text(n, 0.59, divisor_label, ha="center", va="center", fontsize=5.15, color=MID_GRAY, linespacing=1.0)

        mechanism = row["mechanism"]
        if mechanism == "primitive":
            face, edge, hatch = PALE_GREEN, GREEN, "///"
            status = r"$\bullet$" + "\n" + rf"$p={row['carrier_prime']}$"
        elif mechanism == "jordan":
            face, edge, hatch = PALE_ORANGE, ORANGE, "xx"
            status = (
                rf"$\diamond$ $p={row['carrier_prime']}$"
                + "\n"
                + f"{boundary['jordan_period_ten_points']} / "
                + f"{boundary['jordan_period_ten_cycles']}"
            )
        else:
            if n not in exceptions:
                raise RuntimeError("a nonexception was encoded as no carrier")
            face, edge, hatch = PALE_RED, VERMILLION, "\\\\"
            status = "$\\times$\nnone"
        ax.add_patch(
            Rectangle(
                (left, 0.07),
                0.92,
                0.38,
                facecolor=face,
                edgecolor=edge,
                linewidth=0.85,
                hatch=hatch,
            )
        )
        ax.text(
            n,
            0.26,
            status,
            ha="center",
            va="center",
            fontsize=6.25 if mechanism != "jordan" else 5.8,
            color=edge,
            linespacing=1.25,
            fontweight="bold",
        )

    # (b) Exact small-prime return profiles and excluded columns.
    ax = fig.add_subplot(grid[1, 0])
    ax.set_xlim(0.5, 12.5)
    ax.set_ylim(0.45, 3.55)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([str(i) for i in range(1, 13)])
    ax.set_xlabel("exact dynamical period")
    ax.set_yticks((1, 2, 3))
    ax.set_yticklabels((r"$p=2$", r"$p=3$", r"$p=5$"))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", color="#E8EAED", lw=0.5, zorder=0)
    panel_label(ax, "b", "Exact mod-$2,3,5$ profiles; shaded columns are excluded periods")

    for n in sorted(exceptions):
        ax.axvspan(n - 0.38, n + 0.38, color=PALE_RED, ec=VERMILLION, lw=0.55, hatch="\\\\", zorder=0)
        ax.text(n, 3.42, r"$\times$", ha="center", va="center", color=VERMILLION, fontsize=8.5)

    y_for_prime = {2: 1, 3: 2, 5: 3}
    color_for_prime = {2: BLUE, 3: GREEN, 5: ORANGE}
    marker_for_prime = {2: "o", 3: "s", 5: "D"}
    for prime in (2, 3, 5):
        for period, count in sorted(profiles[prime].items()):
            y = y_for_prime[prime]
            ax.scatter(
                [period],
                [y],
                s=52,
                marker=marker_for_prime[prime],
                facecolor=WHITE,
                edgecolor=color_for_prime[prime],
                linewidth=1.25,
                zorder=3,
            )
            suffix = " pts"
            label = f"{count}{suffix}"
            if prime == 5 and period == 10:
                label += f" / {boundary['jordan_period_ten_cycles']} cycles"
            ax.annotate(
                label,
                (period, y),
                xytext=(0, -12 if prime == 5 and period == 2 else 10),
                textcoords="offset points",
                ha="center",
                va="center",
                fontsize=6.4,
                color=color_for_prime[prime],
                fontweight="bold",
            )

    return fig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    save_figure(
        build_figure(),
        args.output_dir.resolve(),
        STEM,
        metadata_title="Exact standard-cat torsion-carrier boundary at periods one through twelve",
    )


if __name__ == "__main__":
    main()
