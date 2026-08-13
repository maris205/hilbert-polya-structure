"""Figure 1: proof certificate and the sharp bad-prime control."""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from frozen_data import FIGURE_DIR, load_frozen_package
from paper_plot_style import COLORS, apply_style, save_figure


def _box(ax, x, y, w, h, text, color, fontsize=8.0, linewidth=1.0):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.018,rounding_size=0.025",
        facecolor=color + "18",
        edgecolor=color,
        linewidth=linewidth,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize)


def _arrow(ax, x0, y0, x1, y1, color=COLORS["muted"]):
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="-|>",
            mutation_scale=10,
            linewidth=1.0,
            color=color,
        )
    )


def main() -> None:
    data = load_frozen_package()
    proof = data["proof"]
    chain = proof["mathematical_dependency_chain"]
    frozen = data["candidate"]["classification"]
    control = data["control"]["planted_bad_prime_positive"]

    apply_style()
    fig, ax = plt.subplots(figsize=(7.15, 4.25))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    colors = [COLORS["blue"], COLORS["sky"], COLORS["green"], COLORS["purple"], COLORS["orange"]]
    if len(chain) != 5:
        raise RuntimeError("the frozen proof dependency chain changed")
    labels = [
        "Algebraic cycles\nno point at infinity\nin projective closure",
        "S-integral coordinates\ncyclic ultrametric\nmaximum",
        "Integral monodromy\nin $\\mathrm{SL}_2$\nboth eigenvalues S-units",
        "Galois closure\nall places over $S_{\\mathbf{Q}}$\nconjugation-stable",
        "$q^2=\\lambda\\bar\\lambda$\n$q\\in\\mathbf{Q}_{>0}$\n$\\Rightarrow q$ is an $S_{\\mathbf{Q}}$-unit",
    ]
    x_positions = [0.015, 0.215, 0.415, 0.615, 0.815]
    for index, (x, label, color) in enumerate(zip(x_positions, labels, colors)):
        _box(ax, x, 0.55, 0.17, 0.35, label, color, fontsize=7.0)
        if index < 4:
            _arrow(ax, x + 0.17, 0.725, x_positions[index + 1], 0.725)

    ax.text(0.015, 0.95, "Deductive all-period certificate", fontsize=9.2, weight="bold", color=COLORS["ink"])
    ax.text(
        0.985,
        0.95,
        "finite-period ledger is not a proof",
        ha="right",
        fontsize=7.6,
        color=COLORS["muted"],
    )

    frozen_bad = data["scope"]["bad_set_provenance"]["candidate"]
    frozen_values = ", ".join(frozen["exact_rational_modulus_set"])
    planted_bad = control["expected_bad_support"]
    planted_values = ", ".join(control["multiplier_moduli"])
    bottom = [
        (
            0.08,
            COLORS["green"],
            "Frozen integral map",
            f"predeclared bad support = {frozen_bad}\nexact rational moduli = {frozen_values}\nA0: no rational-prime modulus",
        ),
        (
            0.55,
            COLORS["orange"],
            f"Sharp control  a = {control['parameter']}",
            f"fixed point = ({', '.join(control['fixed_point'])})\npredeclared bad support = {planted_bad}\nexact rational moduli = {planted_values}",
        ),
    ]
    for x, color, heading, detail in bottom:
        _box(ax, x, 0.08, 0.37, 0.27, detail, color, fontsize=7.4)
        ax.text(x + 0.185, 0.38, heading, ha="center", va="bottom", fontsize=8.5, weight="bold", color=color)
        _arrow(ax, 0.9, 0.55, x + 0.185, 0.38, color=color)

    save_figure(fig, FIGURE_DIR / "fig1_good_reduction_certificate")
    plt.close(fig)


if __name__ == "__main__":
    main()
