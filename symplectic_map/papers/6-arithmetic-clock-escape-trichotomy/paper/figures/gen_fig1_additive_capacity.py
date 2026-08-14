"""Generate Figure 1: additive certificate, capacity conclusion, and boundaries."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from data_loader import FigureData, load_figure_data
from paper_plot_style import COLORS, add_arrow, add_box, panel_label, save_figure, status_badge, wrapped


def _source_box(ax, source: dict, x: float, y: float, color: str, pale: str) -> None:
    summaries = {
        "L": "finite memory $\\longrightarrow$ edge sums in $V$",
        "M": "$q^2=\\lambda\\bar\\lambda$ is an $S$-unit",
        "A": "regular action $\\longrightarrow\\alpha\\in\\overline{\\mathbb{Q}}\\cap\\mathbb{R}$",
    }
    id_text = (
        f"{source['ids'][0]}--{source['ids'][-1]}"
        if source["count"] > 2
        else ", ".join(source["ids"])
    )
    add_box(ax, (x, y), 0.285, 0.125, facecolor=pale, edgecolor=color, linewidth=1.15)
    ax.text(
        x + 0.014,
        y + 0.093,
        f"Class {source['prefix']}  |  {source['label']}",
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=7.6,
        fontweight="bold",
        color=COLORS["ink"],
    )
    ax.text(
        x + 0.014,
        y + 0.061,
        f"{source['count']} proved: {id_text}",
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=6.2,
        color=color,
    )
    ax.text(
        x + 0.014,
        y + 0.027,
        summaries[source["prefix"]],
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=6.15,
        color=COLORS["ink"],
        linespacing=1.1,
    )


def build_figure(data: FigureData):
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panel_label(ax, "a  Certified sources", 0.012, 0.985)
    source_colors = (
        (COLORS["blue"], COLORS["pale_blue"]),
        (COLORS["orange"], COLORS["pale_orange"]),
        (COLORS["purple"], COLORS["pale_purple"]),
    )
    source_y = (0.715, 0.555, 0.395)
    target_y = (0.70, 0.62, 0.54)
    for source, y, (color, pale), endpoint_y in zip(data.source_classes, source_y, source_colors, target_y):
        _source_box(ax, source, 0.025, y, color, pale)
        add_arrow(ax, (0.31, y + 0.062), (0.375, endpoint_y), color=color, linewidth=1.05)

    panel_label(ax, "b  Additive form", 0.355, 0.985)
    add_box(
        ax,
        (0.375, 0.475),
        0.30,
        0.285,
        facecolor=COLORS["pale_green"],
        edgecolor=COLORS["green"],
        linewidth=1.35,
    )
    ax.text(
        0.525,
        0.690,
        r"$L=v+\log q+\alpha$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=12.0,
        fontweight="bold",
        color=COLORS["ink"],
    )
    ax.text(
        0.525,
        0.615,
        r"$v\in V$, $\dim_{\mathbb{Q}}V<\infty$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.2,
        color=COLORS["ink"],
        linespacing=1.2,
    )
    ax.text(
        0.525,
        0.555,
        r"$q>0$ algebraic; $q^2$ is an $S$-unit",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.8,
        color=COLORS["ink"],
        linespacing=1.15,
    )
    ax.text(
        0.525,
        0.500,
        r"$\alpha\in\overline{\mathbb{Q}}\cap\mathbb{R}$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.8,
        color=COLORS["ink"],
    )
    status_badge(ax, 0.642, 0.724)

    add_arrow(ax, (0.675, 0.617), (0.715, 0.617), color=COLORS["green"], linewidth=1.45)
    panel_label(ax, "c  Capacity", 0.705, 0.985)
    add_box(
        ax,
        (0.72, 0.475),
        0.255,
        0.285,
        facecolor=COLORS["pale_blue"],
        edgecolor=COLORS["blue"],
        linewidth=1.4,
    )
    ax.text(
        0.8475,
        0.650,
        "outside-support $v_p$ terms\nare $\\mathbb{Q}$-independent",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.3,
        fontweight="bold",
        color=COLORS["ink"],
        linespacing=1.25,
    )
    ax.text(
        0.8475,
        0.555,
        r"$|P_{\rm hit}|\leq\dim_{\mathbb{Q}}V+|S|$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=8.6,
        color=COLORS["blue"],
        fontweight="bold",
    )
    ax.text(
        0.8475,
        0.505,
        "CAPACITY BOUND CERTIFIED",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.1,
        color=COLORS["blue"],
        fontweight="bold",
    )
    status_badge(ax, 0.947, 0.724, text="EXACT")

    panel_label(ax, "d  Exact controls and scoped escape", 0.012, 0.315)
    control_specs = (
        (
            data.controls["K001"],
            COLORS["pale_blue"],
            COLORS["blue"],
            lambda record: (
                f"{record['control_id']}  formal rank attainment\n"
                f"labels = rank = {record['rank']}\n"
                "target injection: yes"
            ),
        ),
        (
            data.controls["K002"],
            COLORS["pale_orange"],
            COLORS["orange"],
            lambda record: (
                f"{record['control_id']}  bad-support edge\n"
                f"a={record['parameter']}; fixed point (5/4, 5/4)\n"
                "multipliers 2 and 1/2"
            ),
        ),
        (
            data.controls["K003"],
            COLORS["pale_purple"],
            COLORS["purple"],
            lambda record: (
                f"{record['control_id']}  injected normalization\n"
                "identity map; symbolic log 2\n"
                "potential is not Qbar-rational"
            ),
        ),
    )
    for index, (record, pale, edge, formatter) in enumerate(control_specs):
        x = 0.025 + 0.325 * index
        add_box(ax, (x, 0.105), 0.30, 0.145, facecolor=pale, edgecolor=edge, linewidth=1.0)
        ax.text(
            x + 0.015,
            0.178,
            formatter(record),
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=6.25,
            color=COLORS["ink"],
            linespacing=1.25,
        )

    escape = data.escape_semantics
    escape_line = "certificate failures are necessary only: not exclusive, exhaustive, or sufficient"
    ax.text(
        0.5,
        0.035,
        escape_line,
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
        "fig1_additive_capacity",
        description="Official-source rendering of the additive capacity certificate and its exact boundaries.",
    )


if __name__ == "__main__":
    generate()
