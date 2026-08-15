"""Generate Figure 3: Frobenius--Hensel norm and coefficient obstruction."""

from __future__ import annotations

from matplotlib.patches import FancyBboxPatch

from figure_contract import (
    controls_contract,
    load_frozen_inputs,
    proof_contract,
    require,
)
from paper_plot_style import COLORS, plt, save_all


def flow_box(ax, x, heading, body, face, edge):
    width, y, height = 0.174, 0.24, 0.53
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        linewidth=1.0,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height * 0.70,
        heading,
        ha="center",
        va="center",
        fontsize=8.5,
        fontweight="bold",
        color=COLORS["dark"],
    )
    ax.text(
        x + width / 2,
        y + height * 0.37,
        body,
        ha="center",
        va="center",
        fontsize=7.5,
        color=COLORS["dark"],
        linespacing=1.18,
    )
    return width, y, height


def main() -> None:
    source, result = load_frozen_inputs()
    contract = proof_contract(result)
    controls = controls_contract(result)
    claims = {entry.split(":", 1)[0]: entry for entry in source["frozen_theorem_claims"]}
    require("T4" in claims and "T5" in claims, "T4--T5 missing from source lock")

    norm_record = contract["records"]["frobenius_hensel_norm"]
    require(norm_record["pass"] is True, "Frobenius--Hensel contract failed")
    logic = norm_record["logic_checks"]
    require(all(logic.values()), "Frobenius--Hensel logic check failed")
    mod2_lift = norm_record["mod2_lift"]
    require(mod2_lift["pass"] is True, "mod-2 lift contract failed")
    coeff_filter = norm_record["two_coefficient_filter"]
    require(coeff_filter["pass"] is True, "two-coefficient filter contract failed")
    require(coeff_filter["n2_n3_obstructed"] is True, "n=2,3 obstruction absent")
    require(
        coeff_filter["degree_four_filter_insufficient"] is True,
        "degree-four insufficiency marker absent",
    )
    require(
        coeff_filter["all_period_inference_allowed"] is False,
        "unsafe all-period inference is marked as allowed",
    )

    irreducibles = coeff_filter["irreducibles"]
    degrees = sorted(int(key) for key in irreducibles)
    require({2, 3, 4}.issubset(degrees), "degree-2--4 irreducible ledger incomplete")
    table_rows = []
    passing_degrees = set()
    for degree in degrees:
        for record in irreducibles[str(degree)]:
            passed = record["two_coefficient_filter_passes"] is True
            if passed:
                passing_degrees.add(degree)
            table_rows.append(
                [
                    str(degree),
                    rf"${record['polynomial']}$",
                    str(record["coefficient_T"]),
                    str(record["coefficient_T2"]),
                    "PASS" if passed else "BLOCKED",
                    "necessary only" if passed else "obstructed",
                ]
            )
    excluded_degrees = [
        degree
        for degree in degrees
        if not any(row["two_coefficient_filter_passes"] for row in irreducibles[str(degree)])
    ]
    require(excluded_degrees[:2] == [2, 3], "finite obstruction ledger changed")
    require(4 in passing_degrees, "degree-four witness no longer passes the filter")

    control_records = {record["control_id"]: record for record in controls["records"]}
    require(
        {
            "power_map_and_negative_target",
            "chebyshev_signed_equality",
            "formal_period_pollution",
        }.issubset(control_records),
        "required control records are missing",
    )
    power = control_records["power_map_and_negative_target"]
    chebyshev = control_records["chebyshev_signed_equality"]
    pollution = control_records["formal_period_pollution"]
    control_badges = [
        (
            "$" + source["controls"]["power_map"]["map"] + "$ equality path",
            power["checks"]["positive_equality_hit"],
        ),
        (
            "$" + source["controls"]["chebyshev"]["map"] + "$ signed path",
            chebyshev["checks"]["negative_equality_hit"],
        ),
        (
            "$" + source["controls"]["negative_target"]["target"] + "$ negative target",
            power["checks"]["target_B_equals_2_absent"],
        ),
        (
            "$" + source["controls"]["formal_period_pollution"]["map"] + "$ saturation",
            pollution["checks"]["no_false_target_hit"],
        ),
    ]
    require(all(status is True for _, status in control_badges), "control badge failed")

    fig = plt.figure(figsize=(10.9, 6.6))
    grid = fig.add_gridspec(3, 1, height_ratios=[1.35, 2.75, 0.85], hspace=0.13)

    ax_flow = fig.add_subplot(grid[0])
    ax_flow.set_xlim(0, 1)
    ax_flow.set_ylim(0, 1)
    ax_flow.axis("off")
    ax_flow.text(0.001, 0.97, "(a)", ha="left", va="top", fontweight="bold", fontsize=10)

    x_positions = [0.018, 0.214, 0.410, 0.606, 0.802]
    lift_coefficients = mod2_lift["lift_coefficients_in_1_u_u2"]
    require(lift_coefficients == ["alpha", "1", "1"], "unexpected lift coefficients")
    flow_data = [
        (
            "Exact Frobenius orbit",
            r"$\alpha\in\mathbb{F}_{2^n}$" + "\nexact Frobenius degree $n$",
            COLORS["light_blue"],
            COLORS["blue"],
        ),
        (
            "Unique Hensel lift",
            r"$z_\alpha\equiv\alpha+u+u^2$" + "\n" + r"$(\mathrm{mod}\ 2)$",
            COLORS["light_blue"],
            COLORS["blue"],
        ),
        (
            "Dynamics = Frobenius",
            r"$\sigma(z_\alpha)=g(z_\alpha)$" + "\nexact period is preserved",
            COLORS["light_green"],
            COLORS["green"],
        ),
        (
            "Norm coordinate",
            r"$B_C=N_{K_{u,n}/K_u}(z_\alpha)$" + "\nunramified local norm",
            COLORS["light_green"],
            COLORS["green"],
        ),
        (
            "Necessary equality gate",
            r"$B_C=\pm1\Longrightarrow$" + "\n" + r"$e_{n-1}=e_{n-2}=0$",
            COLORS["light_orange"],
            COLORS["orange"],
        ),
    ]
    box_width = None
    for xpos, data in zip(x_positions, flow_data):
        box_width, _, _ = flow_box(ax_flow, xpos, *data)
    for left, right in zip(x_positions[:-1], x_positions[1:]):
        ax_flow.annotate(
            "",
            xy=(right, 0.505),
            xytext=(left + box_width, 0.505),
            arrowprops={
                "arrowstyle": "-|>",
                "color": COLORS["gray"],
                "linewidth": 1.15,
                "shrinkA": 2,
                "shrinkB": 2,
            },
        )

    ax_table = fig.add_subplot(grid[1])
    ax_table.axis("off")
    ax_table.text(0.001, 0.995, "(b)", ha="left", va="top", fontweight="bold", fontsize=10)
    columns = [r"degree $n$", r"irreducible over $\mathbb{F}_2$", r"$[T]$", r"$[T^2]$", "gate", "meaning"]
    table = ax_table.table(
        cellText=table_rows,
        colLabels=columns,
        cellLoc="center",
        colLoc="center",
        bbox=[0.035, 0.18, 0.93, 0.75],
        colWidths=[0.10, 0.31, 0.09, 0.09, 0.16, 0.20],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.0)
    table.scale(1.0, 1.32)
    for (row, col), cell in table.get_celld().items():
        cell.set_linewidth(0.55)
        cell.set_edgecolor("#AAB2BA")
        if row == 0:
            cell.set_facecolor(COLORS["dark"])
            cell.get_text().set_color(COLORS["white"])
            cell.get_text().set_fontweight("bold")
        else:
            passed = table_rows[row - 1][4] == "PASS"
            if col in (4, 5):
                cell.set_facecolor(COLORS["light_orange"] if passed else COLORS["light_gray"])
                cell.get_text().set_color(COLORS["vermillion"] if passed else COLORS["gray"])
                cell.get_text().set_fontweight("bold")
            else:
                cell.set_facecolor(COLORS["white"] if row % 2 else "#F8F9FA")

    excluded_text = ",".join(str(value) for value in excluded_degrees)
    passing_text = ",".join(str(value) for value in sorted(passing_degrees))
    ax_table.text(
        0.5,
        0.075,
        rf"degrees {excluded_text}: no irreducible passes $\Rightarrow B_C\ne\pm1$; "
        rf"degree {passing_text}: a witness passes a necessary filter; equality remains open",
        ha="center",
        va="center",
        fontsize=8.2,
        color=COLORS["dark"],
        bbox={
            "boxstyle": "round,pad=0.28",
            "facecolor": COLORS["light_orange"],
            "edgecolor": COLORS["orange"],
            "linewidth": 0.8,
        },
    )

    ax_controls = fig.add_subplot(grid[2])
    ax_controls.set_xlim(0, 1)
    ax_controls.set_ylim(0, 1)
    ax_controls.axis("off")
    ax_controls.text(0.001, 0.98, "(c)", ha="left", va="top", fontweight="bold", fontsize=10)
    badge_width = 0.222
    for index, (label, status) in enumerate(control_badges):
        xpos = 0.038 + index * 0.239
        patch = FancyBboxPatch(
            (xpos, 0.22),
            badge_width,
            0.55,
            boxstyle="round,pad=0.012,rounding_size=0.02",
            linewidth=0.85,
            edgecolor=COLORS["green"],
            facecolor=COLORS["light_green"],
            hatch="///",
        )
        ax_controls.add_patch(patch)
        ax_controls.text(
            xpos + badge_width / 2,
            0.55,
            label,
            ha="center",
            va="center",
            fontsize=7.4,
            color=COLORS["dark"],
        )
        ax_controls.text(
            xpos + badge_width / 2,
            0.34,
            "PASS" if status else "FAIL",
            ha="center",
            va="center",
            fontsize=7.0,
            fontweight="bold",
            color=COLORS["green"] if status else COLORS["vermillion"],
        )

    fig.subplots_adjust(left=0.025, right=0.985, top=0.98, bottom=0.035)
    save_all(fig, "fig3_frobenius_filter")


if __name__ == "__main__":
    main()
