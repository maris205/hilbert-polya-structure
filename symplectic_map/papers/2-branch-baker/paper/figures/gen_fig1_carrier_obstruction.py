#!/usr/bin/env python3
"""Generate the Markov-factor, branch-carrier, and clock-obstruction hero figure.

Scientific inputs are read only from experiments/source_lock.json and
results/analysis_test.json.  Coordinates below specify layout, not data.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from paper_plot_style import COLORS, panel_label, save_figure


FIGURE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = FIGURE_DIR.parents[1]


def load_json(relative: str) -> dict:
    return json.loads((PROJECT_ROOT / relative).read_text(encoding="utf-8"))


def draw_edge(ax, start, end, sign: int, curvature: float, label_xy) -> None:
    color = COLORS["blue"] if sign > 0 else COLORS["orange"]
    linestyle = "-" if sign > 0 else (0, (3, 2))
    edge = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=8,
        connectionstyle=f"arc3,rad={curvature}",
        shrinkA=14,
        shrinkB=14,
        linewidth=1.1,
        linestyle=linestyle,
        color=color,
        zorder=1,
    )
    ax.add_patch(edge)
    ax.text(
        *label_xy,
        "+" if sign > 0 else r"$-$",
        color=color,
        fontsize=8,
        ha="center",
        va="center",
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.25},
        zorder=4,
    )


def main() -> None:
    lock = load_json("experiments/source_lock.json")
    analysis = load_json("results/analysis_test.json")
    adjacency = lock["markov_factor"]["adjacency"]
    signs = lock["markov_factor"]["factor_orientation_weights"]
    areas = [float(Fraction(value)) for value in lock["phase_space"]["rectangle_areas"]]

    assert adjacency == [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
    assert areas == [0.25, 0.25, 0.5]
    assert lock["phase_space"]["pf_eigenvalue"] == "sqrt(2)"
    assert lock["phase_space"]["branch_derivative"] == (
        "diag(sigma_ij*sqrt(2),sigma_ij/sqrt(2))"
    )
    assert lock["pretest_exact_predictions"]["all_unquotiented_SFT_baker_periods_even"]
    assert "2^k" in lock["clocks"]["frozen_locally_constant_prediction"]
    assert analysis["route_a_status"] == "A0_FAIL / STRUCTURAL_ONLY"
    assert analysis["pre_a0_status"] == "PRE_A0_STRUCTURAL_PASS"

    fig = plt.figure(figsize=(7.05, 2.72))
    grid = fig.add_gridspec(1, 3, width_ratios=(1.03, 1.48, 1.30), wspace=0.24)

    # (a) Exact three-state Markov graph.  Edge signs are inherited
    # one-dimensional factor orientations, not symplectic orientations.
    ax_graph = fig.add_subplot(grid[0, 0])
    ax_graph.set_xlim(0, 1)
    ax_graph.set_ylim(0, 1)
    ax_graph.axis("off")
    positions = {0: (0.22, 0.72), 1: (0.22, 0.28), 2: (0.78, 0.50)}
    node_colors = {0: COLORS["sky"], 1: COLORS["yellow"], 2: COLORS["green"]}
    for state, (x, y) in positions.items():
        ax_graph.scatter(
            [x], [y], s=650, facecolor=node_colors[state], edgecolor="white",
            linewidth=1.2, zorder=3,
        )
        ax_graph.text(x, y, rf"$I_{state}$", ha="center", va="center", zorder=4)

    edge_specs = {
        (0, 2): (0.13, (0.51, 0.68)),
        (2, 0): (0.13, (0.51, 0.82)),
        (1, 2): (-0.13, (0.51, 0.32)),
        (2, 1): (-0.13, (0.51, 0.18)),
    }
    for (source, target), (curve, label_xy) in edge_specs.items():
        assert adjacency[source][target] == 1
        draw_edge(
            ax_graph,
            positions[source],
            positions[target],
            signs[source][target],
            curve,
            label_xy,
        )
    ax_graph.plot([], [], color=COLORS["blue"], label="factor sign $+1$")
    ax_graph.plot([], [], color=COLORS["orange"], linestyle=(0, (3, 2)),
                  label="factor sign $-1$")
    ax_graph.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.50, -0.02),
                    handlelength=1.7, labelspacing=0.25)
    panel_label(ax_graph, "a")

    # (b) Labeled disjoint union of rectangles.  Heights visualize the exact
    # area ratios; vertical subdivisions are source strips ordered by target.
    ax_carrier = fig.add_subplot(grid[0, 1])
    ax_carrier.set_xlim(0, 3.55)
    ax_carrier.set_ylim(0, 1.72)
    ax_carrier.axis("off")
    x0 = [0.13, 1.23, 2.33]
    width = 0.83
    max_height = 0.95
    edge_colors = {(0, 2): COLORS["green"], (1, 2): COLORS["green"],
                   (2, 0): COLORS["sky"], (2, 1): COLORS["yellow"]}
    for state, (x, area) in enumerate(zip(x0, areas)):
        height = max_height * area / max(areas)
        y = 0.43 + (max_height - height) / 2
        targets = [j for j, present in enumerate(adjacency[state]) if present]
        strip_width = width / len(targets)
        for index, target in enumerate(targets):
            ax_carrier.add_patch(
                Rectangle(
                    (x + index * strip_width, y), strip_width, height,
                    facecolor=edge_colors[(state, target)], alpha=0.38,
                    edgecolor=COLORS["black"], linewidth=0.8,
                )
            )
            ax_carrier.text(
                x + (index + 0.5) * strip_width,
                y + 0.5 * height,
                rf"${state}\!\to\!{target}$",
                ha="center", va="center", fontsize=7.5,
            )
        area_fraction = Fraction(area).limit_denominator()
        ax_carrier.text(
            x + width / 2,
            y + height + 0.055,
            rf"$R_{state}$" + "\n"
            + rf"area $={area_fraction.numerator}/{area_fraction.denominator}$",
            ha="center", va="bottom", fontsize=7.1, linespacing=0.95,
        )
    ax_carrier.text(
        1.77, 0.34,
        r"$J_{ij}=\mathrm{diag}(\sigma_{ij}\sqrt{2},\,\sigma_{ij}/\sqrt{2})$"
        "\n" r"$J_{ij}^{\mathsf{T}}\Omega J_{ij}=\Omega,\qquad \det J_{ij}=1$",
        ha="center", va="top", fontsize=7.4,
    )
    ax_carrier.text(
        1.77, 0.012, analysis["pre_a0_status"].replace("_", " "),
        ha="center", va="bottom", fontsize=6.7, color=COLORS["green"],
        fontweight="bold",
    )
    panel_label(ax_carrier, "b")

    # (c) The candidate clock is a one-dimensional lattice.  The displayed
    # general implication is the finite-memory theorem frozen in the lock.
    ax_clock = fig.add_subplot(grid[0, 2])
    ax_clock.set_xlim(0, 1)
    ax_clock.set_ylim(0, 1)
    ax_clock.axis("off")
    ax_clock.annotate(
        "", xy=(0.92, 0.70), xytext=(0.10, 0.70),
        arrowprops={"arrowstyle": "->", "color": COLORS["black"], "lw": 0.8},
    )
    for k in range(1, 6):
        x = 0.10 + 0.15 * k
        ax_clock.plot(x, 0.70, "o", ms=4.2, color=COLORS["blue"])
        ax_clock.text(x, 0.625, rf"$k={k}$", ha="center", va="top", fontsize=6.7)
    ax_clock.text(
        0.50, 0.86, r"period $2k$:  $|\Lambda_u|=2^k$",
        ha="center", va="center", fontsize=8.5,
    )
    ax_clock.text(
        0.50, 0.45,
        r"finite local weights $\Longrightarrow$"
        "\n" r"$\dim_{\mathbf{Q}}\operatorname{span}\{\ell_\gamma\}<\infty$",
        ha="center", va="center", fontsize=8.2,
        bbox={"boxstyle": "round,pad=0.28", "facecolor": "white",
              "edgecolor": COLORS["gray"], "linewidth": 0.7},
    )
    ax_clock.text(
        0.50, 0.25,
        r"candidate: $\ell_\gamma\in\mathbf{Q}\log 2$"
        "\n" r"$\{\log p:p\ \mathrm{prime}\}\nsubseteq\mathbf{Q}\log 2$",
        ha="center", va="center", fontsize=8.0,
    )
    ax_clock.text(
        0.50, 0.055, analysis["route_a_status"].replace("_", " "),
        ha="center", va="center", fontsize=8.0, color=COLORS["orange"],
        fontweight="bold",
        bbox={"boxstyle": "round,pad=0.22", "facecolor": "#FFF4EC",
              "edgecolor": COLORS["orange"], "linewidth": 0.8},
    )
    panel_label(ax_clock, "c")

    # Process arrows are deliberately neutral: the carrier passes structurally,
    # while its frozen scalar clock is what fails the arithmetic gate.
    for start, end in [((0.307, 0.51), (0.334, 0.51)), ((0.675, 0.62), (0.702, 0.62))]:
        fig.add_artist(
            FancyArrowPatch(
                start, end, transform=fig.transFigure, arrowstyle="-|>",
                mutation_scale=9, linewidth=0.8, color=COLORS["gray"],
            )
        )

    save_figure(fig, "fig1_carrier_obstruction")


if __name__ == "__main__":
    main()
