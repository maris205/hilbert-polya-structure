"""Figure 1: the all-period implication and its normalization boundary."""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from frozen_data import FIGURE_DIR, load_frozen_package
from paper_plot_style import COLORS, apply_style, save_figure


def box(ax, x, y, w, h, text, color, fontsize=8.0, dashed=False):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.018,rounding_size=0.025",
            facecolor=color + "18",
            edgecolor=color,
            linewidth=1.0,
            linestyle="--" if dashed else "-",
        )
    )
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize)


def arrow(ax, x0, y0, x1, y1, color=COLORS["muted"]):
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
    control = data["control"]
    if not all(proof["dependency_checks"].values()):
        raise RuntimeError("the frozen proof-dependency contract changed")
    identity = control["identity_transcendental_constant"]
    if not identity["pass"] or identity["numeric_logarithm_evaluated"]:
        raise RuntimeError("identity-map symbolic control changed")
    if identity["classification"] != "COUNTEREXAMPLE_TO_MAP_ONLY_CLAIM_OUTSIDE_QBAR_POTENTIAL_HYPOTHESIS":
        raise RuntimeError("identity-map scope classification changed")

    apply_style()
    fig, ax = plt.subplots(figsize=(7.15, 4.25))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.02, 0.95, "All-period deductive certificate", fontsize=9.4, weight="bold")
    ax.text(
        0.98,
        0.95,
        "static JSON audits implementation, not the theorem",
        ha="right",
        fontsize=7.4,
        color=COLORS["muted"],
    )

    boxes = [
        (0.02, COLORS["blue"], "Regular algebraic orbit\n frozen single-valued\n$\\overline{\\mathbf{Q}}$-rational $G$"),
        (0.365, COLORS["green"], "Finite evaluation\n$\\mathcal{A}_G=\\sum_jG(P_j)$\n$\\in\\overline{\\mathbf{Q}}$"),
        (0.71, COLORS["purple"], "Hermite--Lindemann\n$\\mathcal{A}_G\\ne\\log\\beta$\n$\\beta\\in\\overline{\\mathbf{Q}}^*\\!\\setminus\\{1\\}$"),
    ]
    for index, (x, color, label) in enumerate(boxes):
        box(ax, x, 0.56, 0.27, 0.30, label, color, fontsize=8.2)
        if index < 2:
            arrow(ax, x + 0.27, 0.71, boxes[index + 1][0], 0.71)

    ax.text(0.02, 0.46, "Normalization ledger", fontsize=8.8, weight="bold")
    box(
        ax,
        0.02,
        0.12,
        0.29,
        0.25,
        "Inside certificate\nalgebraic gauges and constants\nfull endpoint term retained",
        COLORS["green"],
        fontsize=7.7,
    )
    box(
        ax,
        0.355,
        0.12,
        0.29,
        0.25,
        "Sharp outside control\nidentity map, $G\\equiv\\log 2$\nsymbolic; no numeric logarithm",
        COLORS["orange"],
        fontsize=7.7,
        dashed=True,
    )
    box(
        ax,
        0.69,
        0.12,
        0.29,
        0.25,
        "Not decided\n$\\log|\\mathcal{A}|$, multipliers, return times\nmultivalued/closed non-exact clocks",
        COLORS["sky"],
        fontsize=7.5,
        dashed=True,
    )
    arrow(ax, 0.50, 0.56, 0.50, 0.39, color=COLORS["orange"])
    ax.text(
        0.50,
        0.395,
        "Map-only countercontrol:\ntranscendental normalization",
        ha="center",
        va="bottom",
        fontsize=7.2,
        color=COLORS["orange"],
        linespacing=1.15,
    )

    save_figure(fig, FIGURE_DIR / "fig1_action_certificate")
    plt.close(fig)


if __name__ == "__main__":
    main()
