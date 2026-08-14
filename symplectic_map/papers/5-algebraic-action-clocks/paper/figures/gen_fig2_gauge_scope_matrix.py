"""Figure 2: exact gauge formula and source-locked scope matrix."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from frozen_data import FIGURE_DIR, load_frozen_package
from paper_plot_style import COLORS, apply_style, save_figure
from scope_matrix_ledger import COLUMNS, STATUS_CODES, derive_scope_rows, write_scope_provenance


def main() -> None:
    data = load_frozen_package()
    control = data["control"]
    telescope = control["symbolic_telescope"]
    if telescope["general_residual"] != "0" or telescope["compatible_residual"] != "0":
        raise RuntimeError("the exact telescope control changed")
    rows = derive_scope_rows(data)
    write_scope_provenance(rows, FIGURE_DIR / "fig2_scope_matrix_provenance.json")
    matrix = np.array(
        [[STATUS_CODES[cell.status] for cell in row.cells] for row in rows],
        dtype=int,
    )
    cmap = ListedColormap([COLORS["red"], COLORS["orange"], COLORS["green"]])
    cell_text = {0: "STOP/OUT", 1: "EDGE", 2: "CERTIFIED"}

    apply_style()
    fig = plt.figure(figsize=(7.15, 5.05))
    grid = fig.add_gridspec(2, 1, height_ratios=[0.86, 3.4], hspace=0.22)
    ax_formula = fig.add_subplot(grid[0])
    ax_formula.axis("off")
    formula = (
        r"$\mathcal{A}' - \mathcal{A}"
        r"=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1} C_j$"
    )
    ax_formula.text(0.5, 0.69, formula, ha="center", va="center", fontsize=12.0)
    ax_formula.text(
        0.5,
        0.24,
        "Cells: frozen-JSON predicates + explicit theorem-defined scope ledger.",
        ha="center",
        va="center",
        fontsize=8.0,
        color=COLORS["muted"],
    )

    ax = fig.add_subplot(grid[1])
    ax.imshow(matrix, aspect="auto", cmap=cmap, vmin=0, vmax=2)
    ax.set_xticks(range(3), COLUMNS)
    ax.set_yticks(range(len(rows)), [row.label for row in rows])
    ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False, length=0)
    ax.tick_params(axis="y", length=0)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            code = int(matrix[i, j])
            color = "white" if code in (0, 2) else COLORS["ink"]
            ax.text(j, i, cell_text[code], ha="center", va="center", fontsize=6.7, color=color, weight="bold")
    ax.set_xticks(np.arange(-0.5, 3, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.4)
    ax.tick_params(which="minor", bottom=False, left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    save_figure(fig, FIGURE_DIR / "fig2_gauge_scope_matrix")
    plt.close(fig)


if __name__ == "__main__":
    main()
