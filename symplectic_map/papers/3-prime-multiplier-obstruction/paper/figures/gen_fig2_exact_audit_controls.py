from __future__ import annotations

import textwrap

import matplotlib.pyplot as plt
import numpy as np

from frozen_data import load_core, require
from paper_plot_style import OKABE_ITO, add_panel_tag, rounded_box, save_fig


def wrap(text: str, width: int) -> str:
    return textwrap.fill(text, width=width)


def format_candidate_list(values: list[str]) -> str:
    if not values:
        return "none"
    if len(values) == 1:
        return values[0]
    return "{" + ", ".join(values) + "}"


def main() -> None:
    core = load_core()
    candidate = core["candidate_audit"]
    controls = core["control_audit"]
    exact = core["exact_polynomials"]
    conjugacy = core["conjugacy_audit"]

    require(candidate["status"] == "PASS", "candidate audit must PASS")
    require(controls["status"] == "PASS", "control audit must PASS")
    require(conjugacy["status"] == "PASS", "conjugacy audit must PASS")
    require(candidate["period_cutoff"] == [1, 2, 3, 4], "unexpected candidate cutoff")
    require(candidate["checks"]["formal_degrees_match_freeze"], "formal degree freeze changed")
    require(candidate["checks"]["exact_degrees_equal_formal_degrees"], "exact degrees changed")
    require(candidate["checks"]["no_low_period_raw_rational_prime"], "candidate raw-prime finding changed")
    require(candidate["checks"]["all_rational_candidates_divisible_by_2_power_n"], "candidate divisibility changed")
    for period_record in conjugacy["periods"]:
        for key, value in period_record["checks"].items():
            require(value is True, f"conjugacy check {period_record['period']}:{key} failed")

    contamination = None
    control_rows = {}
    for control in controls["controls"]:
        control_rows[control["control_id"]] = control
        if control["control_id"] == "c_minus_3_over_4":
            contamination = control["periods"][1]
    require(contamination is not None, "missing c=-3/4 control")
    require(contamination["formal_period_contamination"] is True, "contamination witness changed")
    require(contamination["formal_degree"] == 2, "formal contamination degree changed")
    require(contamination["exact_period_degree"] == 0, "exact period removal changed")
    require(contamination["removed_factor_degrees"] == [1, 1], "removed factor degrees changed")

    periods = [record["period"] for record in candidate["periods"]]
    formal_degrees = [record["formal_degree"] for record in candidate["periods"]]
    exact_degrees = [record["exact_period_degree"] for record in candidate["periods"]]
    cycle_counts = [record["exact_cycle_count"] for record in candidate["periods"]]
    poly_rows = [
        exact["candidate_g"][str(period)]["cycle_multiplier_polynomial"]["expression"] for period in periods
    ]

    fig = plt.figure(figsize=(14.4, 7.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.28], height_ratios=[0.92, 1.08], hspace=0.18, wspace=0.16)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[1, 0])
    ax_c = fig.add_subplot(gs[:, 1])

    # (a) Candidate exact-audit chart
    add_panel_tag(ax_a, "(a)")
    x = np.arange(len(periods))
    bars = ax_a.bar(x, exact_degrees, width=0.55, color=OKABE_ITO["soft_blue"], edgecolor=OKABE_ITO["blue"], linewidth=1.1, label="exact degree")
    ax_a.plot(x, formal_degrees, color=OKABE_ITO["black"], marker="o", markersize=4.5, linewidth=1.1, markerfacecolor="white", label="formal degree")
    for idx, bar in enumerate(bars):
        ax_a.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.35,
            f"cycles={cycle_counts[idx]}\nroots=none",
            ha="center",
            va="bottom",
            fontsize=7.7,
        )
    ax_a.set_xticks(x, [str(p) for p in periods])
    ax_a.set_xlabel("exact period $n$")
    ax_a.set_ylabel("degree / count")
    ax_a.set_ylim(0, 13.5)
    ax_a.legend(frameon=False, loc="upper left")
    rounded_box(ax_a, 0.57, 0.06, 0.38, 0.12, OKABE_ITO["soft_yellow"], OKABE_ITO["orange"], transform=ax_a.transAxes)
    ax_a.text(
        0.59,
        0.12,
        "cutoff audit only\nall-period claim comes from the theorem",
        transform=ax_a.transAxes,
        ha="left",
        va="center",
        fontsize=7.8,
    )

    # (b) Candidate multiplier-polynomial ledger
    ax_b.set_axis_off()
    ax_b.set_xlim(0, 1)
    ax_b.set_ylim(0, 1)
    add_panel_tag(ax_b, "(b)")
    rounded_box(ax_b, 0.02, 0.02, 0.96, 0.92, "white", OKABE_ITO["gray"], linewidth=0.9)
    ax_b.text(0.04, 0.90, r"$n$", fontweight="bold", fontsize=8.6)
    ax_b.text(0.12, 0.90, r"$M_n(L)$", fontweight="bold", fontsize=8.6)
    row_y = 0.80
    for period, expr in zip(periods, poly_rows):
        rounded_box(
            ax_b,
            0.035,
            row_y - 0.095,
            0.93,
            0.11,
            OKABE_ITO["light_gray"] if period % 2 == 0 else "white",
            edgecolor="none",
            linewidth=0.0,
        )
        ax_b.text(0.05, row_y, str(period), ha="left", va="center", fontsize=8.3)
        ax_b.text(
            0.12,
            row_y,
            wrap(expr, 52),
            ha="left",
            va="center",
            fontsize=7.5,
            family="monospace",
            linespacing=1.18,
        )
        row_y -= 0.19

    # (c) Control evidence matrix
    ax_c.set_axis_off()
    ax_c.set_xlim(0, 1)
    ax_c.set_ylim(0, 1)
    add_panel_tag(ax_c, "(c)")
    cols = ["assumption", "1", "2", "3", "4"]
    col_x = [0.02, 0.34, 0.50, 0.66, 0.82]
    col_w = [0.30, 0.14, 0.14, 0.14, 0.14]
    for label, x0, w in zip(cols, col_x, col_w):
        rounded_box(ax_c, x0, 0.88, w, 0.08, OKABE_ITO["light_gray"], OKABE_ITO["gray"], linewidth=0.8)
        ax_c.text(x0 + w / 2, 0.92, f"period {label}" if label.isdigit() else label, ha="center", va="center", fontsize=8.2, fontweight="bold")

    row_specs = [
        ("c_zero", r"$z^2$", 0.68),
        ("c_minus_2", r"$z^2-2$", 0.45),
        ("c_minus_3_over_4", r"$z^2-3/4$", 0.22),
    ]
    for control_id, label, y0 in row_specs:
        control = control_rows[control_id]
        violated = not control["algebraic_integer_coefficients"]
        face = OKABE_ITO["soft_red"] if violated else OKABE_ITO["soft_green"]
        edge = OKABE_ITO["vermillion"] if violated else OKABE_ITO["green"]
        rounded_box(ax_c, col_x[0], y0, col_w[0], 0.16, face, edge, linewidth=1.0)
        assumption_text = "assumptions violated" if violated else "assumptions satisfied"
        ax_c.text(col_x[0] + 0.02, y0 + 0.11, label, ha="left", va="center", fontsize=8.7, fontweight="bold")
        ax_c.text(col_x[0] + 0.02, y0 + 0.065, assumption_text, ha="left", va="center", fontsize=7.8)
        ax_c.text(col_x[0] + 0.02, y0 + 0.025, wrap(control["role"], 28), ha="left", va="center", fontsize=7.2)

        for idx, period_record in enumerate(control["periods"]):
            x0 = col_x[idx + 1]
            content = format_candidate_list(period_record["rational_candidates"])
            cell_face = OKABE_ITO["soft_blue"]
            cell_edge = OKABE_ITO["blue"]
            if period_record["formal_period_contamination"]:
                content = (
                    f"formal {period_record['formal_degree']}\n"
                    f"exact {period_record['exact_period_degree']}\n"
                    f"removed {period_record['removed_factor_degrees']}"
                )
                cell_face = OKABE_ITO["soft_yellow"]
                cell_edge = OKABE_ITO["orange"]
            elif control_id == "c_minus_2" and idx == 0:
                cell_face = OKABE_ITO["soft_orange"]
                cell_edge = OKABE_ITO["orange"]
            elif violated and idx == 0:
                cell_face = OKABE_ITO["soft_red"]
                cell_edge = OKABE_ITO["vermillion"]
            rounded_box(ax_c, x0, y0, col_w[idx + 1], 0.16, cell_face, cell_edge, linewidth=0.95)
            ax_c.text(
                x0 + col_w[idx + 1] / 2,
                y0 + 0.08,
                wrap(content, 13),
                ha="center",
                va="center",
                fontsize=6.5 if period_record["formal_period_contamination"] else 7.5,
                family="monospace" if control_id == "c_minus_3_over_4" and idx == 1 else None,
                linespacing=1.2,
            )

    rounded_box(ax_c, 0.02, 0.04, 0.94, 0.10, OKABE_ITO["soft_blue"], OKABE_ITO["blue"], linewidth=0.95)
    ax_c.text(
        0.04,
        0.09,
        wrap(
            "independent duplication PASS: all n=1..4 checks agree under z=-u x "
            "(cycle polynomials, point resultants, exact-period components, rational candidate lists)",
            92,
        ),
        ha="left",
        va="center",
        fontsize=7.8,
    )

    save_fig(fig, "fig2_exact_audit_controls")
    plt.close(fig)


if __name__ == "__main__":
    main()
