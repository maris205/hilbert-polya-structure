"""Generate Figure 1: theorem boundary and unresolved semantic branches."""

from __future__ import annotations

from matplotlib.patches import FancyBboxPatch

from figure_contract import load_frozen_inputs, proof_contract, require
from paper_plot_style import COLORS, plt, save_all


def box(ax, xy, wh, heading, body, face, edge, status=None, hatch=None):
    x, y = xy
    width, height = wh
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.015",
        linewidth=1.15,
        edgecolor=edge,
        facecolor=face,
        hatch=hatch,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height * 0.69,
        heading,
        ha="center",
        va="center",
        fontsize=9.1,
        fontweight="bold",
        color=COLORS["dark"],
        zorder=3,
    )
    ax.text(
        x + width / 2,
        y + height * 0.40,
        body,
        ha="center",
        va="center",
        fontsize=8.2,
        color=COLORS["dark"],
        linespacing=1.20,
        zorder=3,
    )
    if status:
        ax.text(
            x + width / 2,
            y + height * 0.10,
            status,
            ha="center",
            va="center",
            fontsize=6.8,
            fontweight="bold",
            color=edge,
            zorder=3,
        )


def arrow(ax, start, end):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={
            "arrowstyle": "-|>",
            "color": COLORS["gray"],
            "linewidth": 1.2,
            "shrinkA": 2,
            "shrinkB": 2,
        },
        zorder=1,
    )


def main() -> None:
    source, result = load_frozen_inputs()
    contract = proof_contract(result)
    claims = {entry.split(":", 1)[0]: entry for entry in source["frozen_theorem_claims"]}
    require(all(key in claims for key in ("T1", "T2", "T3")), "T1--T3 missing")

    boundary = contract["scientific_boundary"]
    require(
        boundary["exact_2adic_valuation_all_periods"] == "CERTIFIED_BY_PROOF",
        "all-period valuation is not proof-certified",
    )
    require(
        result["all_period_equality_status"]
        == source["open_claims_and_nonclaims"]["all_period_B_plus_or_minus_1"],
        "open equality status differs between lock and result",
    )
    require(
        source["open_claims_and_nonclaims"]["complex_modulus_only"]
        == "NOT_DECIDED",
        "complex-modulus status changed",
    )

    open_status = result["all_period_equality_status"].replace("_", " ")
    modulus_status = source["open_claims_and_nonclaims"]["complex_modulus_only"].replace(
        "_", " "
    )

    fig, ax = plt.subplots(figsize=(11.6, 4.25))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    chain_y, chain_h, chain_w = 0.355, 0.29, 0.155
    chain_x = [0.018, 0.206, 0.394, 0.582]
    box(
        ax,
        (chain_x[0], chain_y),
        (chain_w, chain_h),
        "Local lemma (T1)",
        "residue characteristic 2\n$0<|c|<1$, exact $n\\geq2$",
        COLORS["light_blue"],
        COLORS["blue"],
        "STANDARD ARGUMENT",
    )
    box(
        ax,
        (chain_x[1], chain_y),
        (chain_w, chain_h),
        "Unit-cycle boundary",
        "$|z_j|=1$ for every\npoint on the cycle",
        COLORS["light_blue"],
        COLORS["blue"],
        "ALL PERIODS",
    )
    box(
        ax,
        (chain_x[2], chain_y),
        (chain_w, chain_h),
        "Frozen valuation (T2)",
        "$w(\\Lambda_C)=n\\,w(2)$\nat every $w\\mid2$",
        COLORS["light_green"],
        COLORS["green"],
        boundary["exact_2adic_valuation_all_periods"].replace("_", " "),
    )
    box(
        ax,
        (chain_x[3], chain_y),
        (chain_w, chain_h),
        "Rational quotient (T3)",
        "$\\Lambda_C=2^n m$\n$m$ is an odd integer",
        COLORS["light_green"],
        COLORS["green"],
        "PROVED UNDER $\\Lambda_C\\in\\mathbb{Q}$",
    )
    for left, right in zip(chain_x[:-1], chain_x[1:]):
        arrow(ax, (left + chain_w, 0.50), (right, 0.50))

    branch_x, branch_w, branch_h = 0.805, 0.176, 0.205
    branch_ys = [0.715, 0.3975, 0.080]
    junction_x = 0.775
    ax.plot(
        [chain_x[-1] + chain_w, junction_x],
        [0.50, 0.50],
        color=COLORS["gray"],
        linewidth=1.2,
        zorder=1,
    )
    ax.plot(
        [junction_x, junction_x],
        [branch_ys[-1] + branch_h / 2, branch_ys[0] + branch_h / 2],
        color=COLORS["gray"],
        linewidth=1.2,
        zorder=1,
    )
    for y in branch_ys:
        arrow(ax, (junction_x, y + branch_h / 2), (branch_x, y + branch_h / 2))

    box(
        ax,
        (branch_x, branch_ys[0]),
        (branch_w, branch_h),
        "Rational equality",
        "$\\Lambda_C=\\pm2^n$\n(equivalently $B_C=\\pm1$)",
        COLORS["light_orange"],
        COLORS["orange"],
        open_status,
        hatch="///",
    )
    box(
        ax,
        (branch_x, branch_ys[1]),
        (branch_w, branch_h),
        "Complex modulus only",
        "$|\\Lambda_C|=2^n$\nwithout rationality",
        COLORS["light_gray"],
        COLORS["gray"],
        modulus_status,
    )
    box(
        ax,
        (branch_x, branch_ys[2]),
        (branch_w, branch_h),
        "Exponent equality",
        "$\\chi_C=\\log 2$\n(modulus-level statement)",
        COLORS["light_gray"],
        COLORS["gray"],
        modulus_status,
    )

    ax.text(0.006, 0.978, "(a)", ha="left", va="top", fontweight="bold", fontsize=10)
    ax.text(
        0.39,
        0.11,
        "2-adic theorem level",
        ha="center",
        va="center",
        color=COLORS["green"],
        fontsize=8.0,
        fontweight="bold",
    )
    ax.text(
        0.896,
        0.967,
        "semantic branches",
        ha="center",
        va="top",
        color=COLORS["gray"],
        fontsize=8.0,
        fontweight="bold",
    )
    save_all(fig, "fig1_boundary_map")


if __name__ == "__main__":
    main()

