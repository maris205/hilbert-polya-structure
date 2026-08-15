"""Generate Figure 2 from the registered exact-period result ledger."""

from __future__ import annotations

import textwrap

import numpy as np
from matplotlib.patches import Patch, Rectangle

from figure_contract import load_frozen_inputs, require
from paper_plot_style import COLORS, plt, save_all


def main() -> None:
    source, result = load_frozen_inputs()
    records = result.get("period_records")
    require(isinstance(records, list) and records, "period records are absent")

    periods = [record["period"] for record in records]
    degrees = [record["exact_set_degree"] for record in records]
    cycle_counts = [record["exact_cycle_count"] for record in records]
    require(periods == result["periods_executed"], "record and execution periods differ")
    require(
        periods == source["registered_exact_audit"]["periods"],
        "record periods differ from the source-locked set",
    )
    require(
        periods == result["development_seen_periods"],
        "registered periods lost the development-seen disclosure",
    )
    require(result["new_blind_periods"] == [], "unexpected blind period in result")
    require(
        all(degree == period * cycles for degree, period, cycles in zip(degrees, periods, cycle_counts)),
        "degree/cycle-count relation failed",
    )

    target_order = [target["target"] for target in records[0]["targets"]]
    require(set(target_order) == {"1", "-1"}, "target set is not {+1,-1}")
    certificates = {}
    for record in records:
        row_targets = {target["target"]: target for target in record["targets"]}
        require(set(row_targets) == set(target_order), "period target set changed")
        for target_name in target_order:
            target = row_targets[target_name]
            passed = (
                target["gcd_degree"] == 0
                and target["field_norm_nonzero"] is True
                and target["gcd_resultant_norm_agree"] is True
                and target["hit"] is False
            )
            require(passed, f"target certificate failed at n={record['period']}")
            certificates[(target_name, record["period"])] = target

    x = np.arange(len(periods), dtype=float)
    fig = plt.figure(figsize=(7.25, 5.70))
    grid = fig.add_gridspec(2, 1, height_ratios=[2.65, 1.60], hspace=0.38)

    ax = fig.add_subplot(grid[0])
    bars = ax.bar(
        x,
        degrees,
        width=0.60,
        color=COLORS["blue"],
        edgecolor=COLORS["dark"],
        linewidth=0.6,
        label=r"exact-set degree $D_n$",
        zorder=2,
    )
    ax.set_xticks(x, [str(period) for period in periods])
    ax.set_xlabel(r"Exact period $n$")
    ax.set_ylabel(r"$D_n=\deg(\Psi_n^{\mathrm{set}})$", color=COLORS["blue"])
    ax.tick_params(axis="y", labelcolor=COLORS["blue"])
    ax.set_ylim(0, max(degrees) * 1.29)
    ax.spines["top"].set_visible(False)
    ax.grid(axis="y", color="#D9DEE3", linewidth=0.55, zorder=0)
    for bar, value in zip(bars, degrees):
        inside = value >= max(degrees) * 0.09
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() - max(degrees) * 0.035
            if inside
            else bar.get_height() + max(degrees) * 0.022,
            str(value),
            ha="center",
            va="top" if inside else "bottom",
            fontsize=7.7,
            color=COLORS["white"] if inside else COLORS["blue"],
            fontweight="bold" if inside else "normal",
        )

    ax_cycles = ax.twinx()
    line = ax_cycles.plot(
        x,
        cycle_counts,
        color=COLORS["orange"],
        marker="o",
        markerfacecolor=COLORS["white"],
        markeredgewidth=1.4,
        label=r"exact cycles $D_n/n$",
        zorder=3,
    )[0]
    ax_cycles.set_ylabel(r"Exact-cycle count $D_n/n$", color=COLORS["orange"])
    ax_cycles.tick_params(axis="y", labelcolor=COLORS["orange"])
    ax_cycles.set_ylim(0, max(cycle_counts) * 1.29)
    ax_cycles.spines["top"].set_visible(False)
    for xpos, value in zip(x, cycle_counts):
        ax_cycles.annotate(
            str(value),
            (xpos, value),
            xytext=(0, 7),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=7.7,
            color=COLORS["orange"],
        )

    ax.legend(
        [bars, line],
        [r"exact-set degree $D_n$", r"exact cycles $D_n/n$"],
        frameon=False,
        loc="upper left",
    )
    ax.text(
        0.70,
        0.955,
        "DEVELOPMENT-SEEN\nREPRODUCTION",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=7.2,
        fontweight="bold",
        color=COLORS["vermillion"],
        bbox={
            "boxstyle": "round,pad=0.25",
            "facecolor": COLORS["light_orange"],
            "edgecolor": COLORS["orange"],
            "linewidth": 0.8,
            "hatch": "///",
        },
    )
    ax.text(-0.075, 1.04, "(a)", transform=ax.transAxes, fontweight="bold", fontsize=10)

    ax_cert = fig.add_subplot(grid[1])
    ax_cert.set_xlim(-0.5, len(periods) - 0.5)
    ax_cert.set_ylim(-0.58, len(target_order) - 0.42)
    ax_cert.set_xticks(x, [str(period) for period in periods])
    ax_cert.set_xlabel(r"Exact period $n$")
    y_positions = list(reversed(range(len(target_order))))
    ax_cert.set_yticks(
        y_positions,
        [rf"$B_n={target}$" for target in target_order],
    )
    for spine in ax_cert.spines.values():
        spine.set_visible(False)
    ax_cert.tick_params(length=0)

    for target_name, ypos in zip(target_order, y_positions):
        for xpos, period in enumerate(periods):
            target = certificates[(target_name, period)]
            cell = Rectangle(
                (xpos - 0.43, ypos - 0.36),
                0.86,
                0.72,
                facecolor=COLORS["light_green"],
                edgecolor=COLORS["green"],
                linewidth=0.9,
                hatch="///",
            )
            ax_cert.add_patch(cell)
            norm_mark = r"$N\ne0$" if target["field_norm_nonzero"] else r"$N=0$"
            agree_mark = "agree" if target["gcd_resultant_norm_agree"] else "disagree"
            ax_cert.text(
                xpos,
                ypos,
                rf"$\deg\gcd={target['gcd_degree']}$" + "\n" + norm_mark + " · " + agree_mark,
                ha="center",
                va="center",
                fontsize=7.1,
                color=COLORS["dark"],
                linespacing=1.15,
            )
    ax_cert.text(
        -0.075,
        1.08,
        "(b)",
        transform=ax_cert.transAxes,
        fontweight="bold",
        fontsize=10,
    )
    legend_patch = Patch(
        facecolor=COLORS["light_green"],
        edgecolor=COLORS["green"],
        hatch="///",
        label="no target hit; exact engines agree",
    )
    ax_cert.legend(handles=[legend_patch], frameon=False, loc="upper right", bbox_to_anchor=(1.0, 1.16))

    open_status = result["all_period_equality_status"]
    open_status = open_status.replace("OPEN_FOR_N_GE_", "open for n ≥ ")
    footer = (
        "development-seen reproduction; "
        f"new blind periods: {len(result['new_blind_periods'])}; "
        f"all-period equality: {open_status}"
    )
    fig.text(
        0.5,
        0.018,
        textwrap.fill(footer, width=95),
        ha="center",
        va="bottom",
        fontsize=6.9,
        color=COLORS["gray"],
    )
    fig.subplots_adjust(left=0.105, right=0.895, top=0.97, bottom=0.155)
    save_all(fig, "fig2_registered_ledger")


if __name__ == "__main__":
    main()
