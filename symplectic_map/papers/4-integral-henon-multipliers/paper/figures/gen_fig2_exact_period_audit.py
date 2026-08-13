"""Figure 2: exact period ledger and selected-embedding classifications."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from frozen_data import FIGURE_DIR, audited_period_rows, cycle_class_counts, load_frozen_package
from paper_plot_style import COLORS, apply_style, save_figure


def main() -> None:
    data = load_frozen_package()
    rows = audited_period_rows(data)
    classes = cycle_class_counts(data)
    cutoff = data["periods"]["cutoff"]

    apply_style()
    fig = plt.figure(figsize=(7.15, 4.35))
    grid = fig.add_gridspec(2, 2, width_ratios=[1.6, 1], height_ratios=[1, 1], wspace=0.3, hspace=0.48)
    ax_counts = fig.add_subplot(grid[0, 0])
    ax_matrix = fig.add_subplot(grid[1, 0])
    ax_class = fig.add_subplot(grid[:, 1])

    periods = np.array([row["period"] for row in rows])
    points = np.array([row["points"] for row in rows])
    cycles = np.array([row["cycles"] for row in rows])
    width = 0.34
    ax_counts.bar(periods - width / 2, points, width, color=COLORS["blue"], label="exact points")
    ax_counts.bar(periods + width / 2, cycles, width, color=COLORS["orange"], label="exact cycles")
    ax_counts.set_xticks(periods)
    ax_counts.set_xlabel("exact period")
    ax_counts.set_ylabel("count")
    ax_counts.set_ylim(0, max(points) + 1.1)
    ax_counts.legend(frameon=False, ncol=2, loc="upper left")
    ax_counts.grid(axis="y", color=COLORS["grid"], linewidth=0.6)
    ax_counts.spines[["top", "right"]].set_visible(False)

    checks = ["branch pass", "det = 1", "unit polynomial", "no rational roots"]
    matrix = []
    for row in rows:
        matrix.append(
            [
                int(row["pass"]),
                int(row["determinant_pass"]),
                int(row["unit_pass"]),
                int(row["rational_roots"] == 0),
            ]
        )
    matrix_array = np.asarray(matrix)
    cmap = plt.matplotlib.colors.ListedColormap([COLORS["red"], COLORS["green"]])
    ax_matrix.imshow(matrix_array, aspect="auto", vmin=0, vmax=1, cmap=cmap)
    ax_matrix.set_xticks(range(len(checks)), labels=checks, rotation=20, ha="right")
    ax_matrix.set_yticks(range(len(rows)), labels=[f"n={row['period']}" for row in rows])
    ax_matrix.tick_params(length=0)
    for i in range(len(rows)):
        for j in range(len(checks)):
            ax_matrix.text(j, i, "PASS" if matrix_array[i, j] else "FAIL", ha="center", va="center", color="white", fontsize=6.8, weight="bold")
    for spine in ax_matrix.spines.values():
        spine.set_visible(False)

    class_labels = list(classes)
    class_values = [classes[label] for label in class_labels]
    wedges, _ = ax_class.pie(
        class_values,
        colors=[COLORS["green"], COLORS["purple"]],
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.42, "edgecolor": "white"},
    )
    ax_class.text(0, 0.06, str(sum(class_values)), ha="center", va="center", fontsize=19, weight="bold")
    ax_class.text(0, -0.17, "cycles", ha="center", va="center", fontsize=8, color=COLORS["muted"])
    legend_labels = [f"{label}: {value}" for label, value in zip(class_labels, class_values)]
    ax_class.legend(wedges, legend_labels, loc="lower center", bbox_to_anchor=(0.5, -0.07), frameon=False)
    ax_class.text(0, 1.23, "selected real embedding", ha="center", fontsize=8.5, weight="bold")
    ax_class.text(0, 1.08, "exact modulus classification", ha="center", fontsize=7.4, color=COLORS["muted"])

    fig.text(0.01, 0.985, f"Finite exact implementation audit through n = {cutoff}", va="top", fontsize=9.2, weight="bold")
    fig.text(
        0.99,
        0.985,
        data["periods"]["finite_ledger_role"],
        va="top",
        ha="right",
        fontsize=7.5,
        color=COLORS["muted"],
    )
    save_figure(fig, FIGURE_DIR / "fig2_exact_period_audit")
    plt.close(fig)


if __name__ == "__main__":
    main()
