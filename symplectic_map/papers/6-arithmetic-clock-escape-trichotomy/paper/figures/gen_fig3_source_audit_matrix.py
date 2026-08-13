"""Generate Figure 3: source certificates and registered audit closure matrix."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from data_loader import FigureData, load_figure_data
from paper_plot_style import COLORS, add_box, panel_label, save_figure, status_badge, wrapped


def _matrix_cell(ax, x: float, y: float, width: float, height: float, passed: bool) -> None:
    face = COLORS["pale_green"] if passed else "#FDEDE7"
    edge = COLORS["green"] if passed else COLORS["vermillion"]
    ax.add_patch(
        Rectangle(
            (x, y),
            width,
            height,
            transform=ax.transAxes,
            facecolor=face,
            edgecolor=COLORS["paper"],
            linewidth=1.2,
            zorder=2,
        )
    )
    ax.text(
        x + width / 2,
        y + height / 2,
        "✓" if passed else "×",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=edge,
        fontfamily="DejaVu Sans",
        zorder=3,
    )


def build_figure(data: FigureData):
    fig, ax = plt.subplots(figsize=(7.2, 4.65))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panel_label(ax, "a  Source-class certificate ledger", 0.012, 0.985)
    source_colors = (
        (COLORS["blue"], COLORS["pale_blue"]),
        (COLORS["orange"], COLORS["pale_orange"]),
        (COLORS["purple"], COLORS["pale_purple"]),
    )
    y_rows = (0.675, 0.43, 0.185)
    source_summaries = {
        "L": "fixed finite memory becomes finitely many edge readouts in $V$",
        "M": "$q^2=\\lambda\\bar\\lambda$ is a fixed-support $S$-unit",
        "A": "regular algebraic action and endpoint shifts stay algebraic",
    }
    for source, y, (edge, pale) in zip(data.source_classes, y_rows, source_colors):
        add_box(ax, (0.025, y), 0.445, 0.195, facecolor=pale, edgecolor=edge, linewidth=1.05)
        ax.text(
            0.043,
            y + 0.158,
            f"Class {source['prefix']}  |  {source['label']}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=8.2,
            fontweight="bold",
            color=COLORS["ink"],
        )
        ax.text(
            0.043,
            y + 0.124,
            f"proved IDs: {', '.join(source['ids'])}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=6.4,
            color=edge,
        )
        ax.text(
            0.043,
            y + 0.067,
            wrapped(source_summaries[source["prefix"]], 54),
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=6.4,
            color=COLORS["ink"],
            linespacing=1.18,
        )
        status_badge(ax, 0.435, y + 0.16, text=f"{source['count']}/{source['count']}", color=COLORS["green"])

    panel_label(ax, "b  Terminal upstream closure", 0.505, 0.985)
    matrix_x = 0.700
    matrix_y = 0.700
    cell_w = 0.066
    cell_h = 0.066
    columns = ("Frozen", "Manifest", "Pipeline", "Record")
    for col_index, label in enumerate(columns):
        ax.text(
            matrix_x + col_index * cell_w + cell_w / 2,
            matrix_y + 2 * cell_h + 0.025,
            label,
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=5.7,
            color=COLORS["muted"],
            rotation=20,
        )
    for row_index, row in enumerate(data.upstream_rows):
        y = matrix_y + (1 - row_index) * cell_h
        compact_label = row["id"].replace("PAPER3_INTEGRAL_HENON_MULTIPLIERS", "Paper 3: multiplier").replace(
            "PAPER4_ALGEBRAIC_ACTION_CLOCKS", "Paper 4: action"
        )
        ax.text(
            0.515,
            y + cell_h / 2,
            compact_label,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=6.25,
            color=COLORS["ink"],
        )
        for col_index, key in enumerate(("frozen", "manifest", "pipeline", "pass")):
            _matrix_cell(ax, matrix_x + col_index * cell_w, y, cell_w, cell_h, row[key])

    panel_label(ax, "c  Registered gates (9/9)", 0.505, 0.625)
    gate_labels = {
        "escape_semantics": "Escape semantics",
        "source_lock": "Source lock",
        "independent_code_review": "Independent review",
        "proof_ledger": "Proof ledger",
        "scope_ledger": "Scope ledger",
        "exact_controls": "Exact controls",
        "executable_isolation": "Executable isolation",
        "upstream_bindings": "Upstream bindings",
        "output_scope": "Output scope",
    }
    for row_index, row in enumerate(data.gate_rows):
        column = 0 if row_index < 5 else 1
        local_index = row_index if column == 0 else row_index - 5
        x = 0.515 + 0.235 * column
        y = 0.555 - 0.055 * local_index
        ax.text(
            x,
            y,
            gate_labels[row["id"]],
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=5.8,
            color=COLORS["ink"],
        )
        _matrix_cell(ax, x + 0.155, y - 0.019, 0.032, 0.038, row["pass"])
        ax.text(
            x + 0.195,
            y,
            "PASS" if row["pass"] else "FAIL",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=5.4,
            fontweight="bold",
            color=COLORS["green"] if row["pass"] else COLORS["vermillion"],
        )

    metrics = data.audit_metrics
    add_box(ax, (0.505, 0.07), 0.47, 0.14, facecolor=COLORS["panel"], edgecolor=COLORS["line"], linewidth=0.85)
    metric_items = (
        f"Proof: {metrics['proof_ids']} IDs / {metrics['proof_cycles']} cycles",
        f"Scope: {metrics['admitted_operations']} in / {metrics['excluded_operations']} out",
        f"Controls: {metrics['controls']} pass",
        f"Isolation: {metrics['scanned_files']} files / {metrics['scanner_findings']} findings",
    )
    for index, value in enumerate(metric_items):
        x = 0.525 + (index % 2) * 0.225
        y = 0.158 - (index // 2) * 0.060
        ax.text(
            x,
            y,
            value,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=5.9,
            fontweight="bold",
            color=COLORS["ink"],
        )

    ax.text(
        0.5,
        0.022,
        f"registered classification: {data.classification.replace('_', ' ')}   |   target matches: {metrics['target_matches']}",
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
        "fig3_source_audit_matrix",
        description="Official proof-ledger, upstream-binding, and registered-gate closure matrix.",
    )


if __name__ == "__main__":
    generate()
