"""Generate Figure 2: exact proof and outside-valuation flow."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from data_loader import FigureData, load_figure_data
from paper_plot_style import COLORS, add_arrow, add_box, panel_label, save_figure, status_badge, wrapped


def _step_box(ax, claim: dict, text: str, x: float, y: float, *, highlighted: bool = False) -> None:
    edge = COLORS["vermillion"] if highlighted else COLORS["blue"]
    face = "#FDEDE7" if highlighted else COLORS["pale_blue"]
    add_box(ax, (x, y), 0.275, 0.18, facecolor=face, edgecolor=edge, linewidth=1.25)
    ax.text(
        x + 0.016,
        y + 0.149,
        claim["id"],
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=8.1,
        fontweight="bold",
        color=edge,
    )
    ax.text(
        x + 0.016,
        y + 0.078,
        text,
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=6.4,
        color=COLORS["ink"],
        linespacing=1.18,
    )
    status_badge(ax, x + 0.242, y + 0.153, text=claim["status"], color=COLORS["green"])


def build_figure(data: FigureData):
    fig, ax = plt.subplots(figsize=(7.2, 4.65))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panel_label(ax, "a  Locked prerequisites", 0.012, 0.988)
    prerequisite_ids = ("T002", "T003", "T004")
    prerequisite_text = {
        "T002": "one certificate per distinct prime;\nrepeats collapse",
        "T003": "$S$-unit status survives extension,\nproduct, and inverse",
        "T004": "rational log sums close to $\\log q$;\n$q^2$ remains an $S$-unit",
    }
    prerequisite_colors = (COLORS["pale_gray"], COLORS["pale_green"], COLORS["pale_orange"])
    prerequisite_edges = (COLORS["muted"], COLORS["green"], COLORS["orange"])
    for index, (claim_id, pale, edge) in enumerate(zip(prerequisite_ids, prerequisite_colors, prerequisite_edges)):
        claim = data.proof_claims[claim_id]
        x = 0.025 + 0.325 * index
        add_box(ax, (x, 0.835), 0.30, 0.10, facecolor=pale, edgecolor=edge, linewidth=0.95)
        ax.text(
            x + 0.012,
            0.885,
            f"{claim_id}  {prerequisite_text[claim_id]}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=5.85,
            color=COLORS["ink"],
            linespacing=1.13,
        )

    panel_label(ax, "b  Relation-to-capacity proof spine", 0.012, 0.79)
    positions = {
        "T005": (0.025, 0.525),
        "T006": (0.3625, 0.525),
        "T007": (0.70, 0.525),
        "T008": (0.70, 0.285),
        "T009": (0.3625, 0.285),
        "T010": (0.025, 0.285),
    }
    summaries = {
        "T005": "rational relation in $\\{v_p\\}$\n$\\Longrightarrow$ integer coefficients $m_p$",
        "T006": "substitute the hits:\n$\\log R=\\beta$, with $R>0$ and\n$R,\\beta$ algebraic",
        "T007": "Hermite--Lindemann:\n$\\beta=0$ and $R=1$",
        "T008": "square in one number field:\n$\\prod p^{2m_p}=\\prod(q_p^2)^{m_p}$",
        "T009": "at $w\\mid p$, $p\\notin S$:\n$2m_pv_w(p)=0\\Longrightarrow m_p=0$",
        "T010": "$\\{v_p:p\\notin S\\}$ is independent\n$\\Longrightarrow |P_{\\rm hit}|\\leq\\dim V+|S|$",
    }
    for claim in data.proof_flow:
        x, y = positions[claim["id"]]
        _step_box(ax, claim, summaries[claim["id"]], x, y, highlighted=claim["id"] == "T009")

    sequential = tuple(claim["id"] for claim in data.proof_flow)
    for left, right in zip(sequential, sequential[1:]):
        x1, y1 = positions[left]
        x2, y2 = positions[right]
        if abs(y1 - y2) < 0.01 and x2 > x1:
            start, end = (x1 + 0.275, y1 + 0.09), (x2, y2 + 0.09)
        elif abs(y1 - y2) < 0.01 and x2 < x1:
            start, end = (x1, y1 + 0.09), (x2 + 0.275, y2 + 0.09)
        else:
            start, end = (x1 + 0.138, y1), (x2 + 0.138, y2 + 0.18)
        add_arrow(
            ax,
            start,
            end,
            color=COLORS["vermillion"] if right == "T009" else COLORS["muted"],
            linewidth=1.25,
        )

    # Dashed provenance arrows show where the source-locked lemmas enter.
    ax.annotate(
        "",
        xy=(0.505, 0.705),
        xytext=(0.505, 0.835),
        xycoords=ax.transAxes,
        textcoords=ax.transAxes,
        arrowprops={"arrowstyle": "-|>", "color": COLORS["line"], "lw": 0.85, "linestyle": "--"},
    )
    ax.annotate(
        "",
        xy=(0.84, 0.465),
        xytext=(0.84, 0.835),
        xycoords=ax.transAxes,
        textcoords=ax.transAxes,
        arrowprops={"arrowstyle": "-|>", "color": COLORS["line"], "lw": 0.85, "linestyle": "--"},
    )

    metrics = data.audit_metrics
    add_box(ax, (0.025, 0.065), 0.95, 0.12, facecolor=COLORS["panel"], edgecolor=COLORS["line"], linewidth=0.9)
    ax.text(
        0.045,
        0.145,
        "Machine ledger",
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=7.4,
        fontweight="bold",
        color=COLORS["ink"],
    )
    metric_strings = (
        f"proof IDs {metrics['proof_ids']}",
        f"dependency cycles {metrics['proof_cycles']}",
        f"controls {metrics['controls']}",
        f"target matches {metrics['target_matches']}",
    )
    for index, text in enumerate(metric_strings):
        x = 0.22 + index * 0.185
        ax.text(
            x,
            0.122,
            text,
            transform=ax.transAxes,
            ha="center",
            va="center",
            fontsize=7.1,
            color=COLORS["ink"],
            bbox={"boxstyle": "round,pad=0.28", "facecolor": COLORS["paper"], "edgecolor": COLORS["line"], "linewidth": 0.7},
        )
    ax.text(
        0.5,
        0.025,
        "Highlighted valuation isolation is the arithmetic step that eliminates every nonzero outside-prime coefficient.",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.5,
        color=COLORS["muted"],
    )
    return fig


def generate(output_dir: Path | None = None) -> dict[str, Path]:
    data = load_figure_data()
    destination = output_dir or Path(__file__).resolve().parent
    return save_figure(
        build_figure(data),
        destination,
        "fig2_proof_flow",
        description="Official proof-ledger rendering of the Hermite-Lindemann and valuation proof flow.",
    )


if __name__ == "__main__":
    generate()
