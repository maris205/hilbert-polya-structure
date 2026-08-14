from __future__ import annotations

import textwrap

import matplotlib.pyplot as plt

from frozen_data import load_core, require
from paper_plot_style import OKABE_ITO, add_panel_tag, rounded_box, save_fig


def wrap(text: str, width: int) -> str:
    return textwrap.fill(text, width=width)


def main() -> None:
    bridge = load_core()["bridge_audit"]
    require(bridge["status"] == "PASS", "bridge audit must PASS")
    for key, value in bridge["checks"].items():
        require(value is True, f"bridge check {key} failed")
    require(bridge["critical_denominator"] == "2*q", "critical denominator changed")
    require(len(bridge["return_products"]) == 4, "unexpected number of return products")

    fig = plt.figure(figsize=(13.6, 5.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.06, 0.94], wspace=0.18)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])

    add_panel_tag(ax_a, "(a)")
    ax_a.set_xlim(-3.2, 3.2)
    ax_a.set_ylim(-1.9, 1.9)
    ax_a.axvspan(-3.2, -0.18, color=OKABE_ITO["soft_green"], alpha=0.85)
    ax_a.axvspan(0.18, 3.2, color=OKABE_ITO["soft_green"], alpha=0.85)
    ax_a.axvspan(-0.18, 0.18, color=OKABE_ITO["soft_red"], alpha=0.65)
    ax_a.axhline(0.0, color=OKABE_ITO["black"], lw=1.1)
    ax_a.axvline(0.0, color=OKABE_ITO["vermillion"], lw=1.4, linestyle="--")
    ax_a.set_xlabel("$q$")
    ax_a.set_ylabel("$p$")
    ax_a.text(-1.75, 1.72, bridge["domain"][0], ha="center", va="center", fontsize=8.9)
    ax_a.text(1.75, 1.72, bridge["domain"][1], ha="center", va="center", fontsize=8.9)
    ax_a.text(0.0, 1.72, "$q=0$", ha="center", va="center", fontsize=8.8, color=OKABE_ITO["vermillion"])
    ax_a.text(-2.9, 0.12, "zero section  $p=0$", ha="left", va="bottom", fontsize=8.1)
    ax_a.scatter([-1.35, 1.35], [0.0, 0.0], color=OKABE_ITO["blue"], s=24, zorder=3)
    ax_a.annotate(
        r"regular return  $\mapsto\,(\lambda,\lambda^{-1})$",
        xy=(1.35, 0.0),
        xytext=(1.0, 0.9),
        arrowprops=dict(arrowstyle="->", lw=1.1, color=OKABE_ITO["blue"]),
        fontsize=8.4,
        color=OKABE_ITO["blue"],
    )
    ax_a.scatter([-1.0, 1.0], [1.1, -1.1], color=OKABE_ITO["purple"], s=20, zorder=3)
    ax_a.annotate(
        wrap(
            f"{bridge['branch_overlap_witness']['inputs'][0]} and "
            f"{bridge['branch_overlap_witness']['inputs'][1]} map to "
            f"({bridge['branch_overlap_witness']['common_output'][0]}, "
            f"{bridge['branch_overlap_witness']['common_output'][1]})",
            26,
        ),
        xy=(1.0, -1.1),
        xytext=(0.95, -1.60),
        textcoords="data",
        fontsize=7.7,
        arrowprops=dict(arrowstyle="->", lw=1.0, color=OKABE_ITO["purple"]),
        color=OKABE_ITO["black"],
    )
    rounded_box(ax_a, 0.05, 0.78, 0.44, 0.12, OKABE_ITO["soft_blue"], OKABE_ITO["blue"], linewidth=0.95, transform=ax_a.transAxes)
    ax_a.text(
        0.07,
        0.84,
        wrap(bridge["map"], 36),
        transform=ax_a.transAxes,
        ha="left",
        va="center",
        fontsize=7.8,
    )
    rounded_box(ax_a, 0.53, 0.78, 0.40, 0.12, OKABE_ITO["soft_blue"], OKABE_ITO["blue"], linewidth=0.95, transform=ax_a.transAxes)
    ax_a.text(
        0.55,
        0.84,
        r"$\widehat g^*(P\,dQ)-p\,dq = "
        + bridge["canonical_one_form_residual"]
        + r"$"
        + "\n"
        + r"$\det D\widehat g - 1 = "
        + bridge["jacobian_determinant_residual"]
        + r"$",
        transform=ax_a.transAxes,
        ha="left",
        va="center",
        fontsize=7.8,
    )

    ax_b.set_axis_off()
    ax_b.set_xlim(0, 1)
    ax_b.set_ylim(0, 1)
    add_panel_tag(ax_b, "(b)")

    rounded_box(ax_b, 0.02, 0.68, 0.96, 0.27, OKABE_ITO["light_gray"], OKABE_ITO["gray"], linewidth=0.9)
    ax_b.text(0.05, 0.90, "period", fontweight="bold", fontsize=8.5)
    ax_b.text(0.22, 0.90, r"$\lambda$ expression", fontweight="bold", fontsize=8.5)
    ax_b.text(0.78, 0.90, "check", fontweight="bold", fontsize=8.5)
    y = 0.84
    for item in bridge["return_products"]:
        ax_b.text(0.07, y, str(item["period"]), ha="left", va="center", fontsize=8.1)
        ax_b.text(0.22, y, item["lambda_expression"], ha="left", va="center", fontsize=8.0, family="monospace")
        ax_b.text(0.79, y, item["reciprocal_pair_identity"], ha="left", va="center", fontsize=8.0, color=OKABE_ITO["green"])
        y -= 0.045

    rounded_box(ax_b, 0.02, 0.34, 0.96, 0.27, OKABE_ITO["soft_yellow"], OKABE_ITO["orange"], linewidth=0.95)
    ax_b.text(0.05, 0.58, "\n".join(f"• {item}" for item in bridge["mandatory_limitations"]), ha="left", va="top", fontsize=7.6, linespacing=1.20)

    rounded_box(ax_b, 0.02, 0.14, 0.96, 0.13, OKABE_ITO["soft_red"], OKABE_ITO["vermillion"], linewidth=0.95)
    ax_b.text(
        0.05,
        0.205,
        wrap(
            f"critical denominator {bridge['critical_denominator']} becomes "
            f"{bridge['critical_denominator_at_q_zero']} at q=0; "
            f"{bridge['noncompactness_witness']}",
            62,
        ),
        ha="left",
        va="center",
        fontsize=7.7,
    )

    save_fig(fig, "fig3_symplectic_scope")
    plt.close(fig)


if __name__ == "__main__":
    main()
