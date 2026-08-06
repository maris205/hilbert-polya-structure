#!/usr/bin/env python3
"""Generate reproducible Paper 3 figures from frozen and read-only audits."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Rectangle


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = PROJECT_ROOT / "results" / "common_coarsen_r061_analysis.json"
LOCALIZATION_AUDIT = PROJECT_ROOT / "results" / "localization_interpretation_audit_r061.json"
CYCLE_AUDIT = PROJECT_ROOT / "results" / "certified_domain_r059.json"
OUT = Path(__file__).resolve().parent

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 9,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
        "pdf.fonttype": 42,
    }
)
COLORS = {"blue": "#0072B2", "orange": "#D55E00", "green": "#009E73", "purple": "#7B2CBF", "gray": "#555555"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(OUT / name, format="pdf")
    plt.close(fig)


def symmetric_jitter(n: int, half_width: float = 0.12) -> np.ndarray:
    """Deterministic offsets that expose coincident seed-level points."""
    if n <= 1:
        return np.zeros(n)
    order = [0]
    for k in range(1, n):
        step = (k + 1) // 2
        order.append(step if k % 2 == 0 else -step)
    offsets = np.asarray(order, dtype=float)
    return half_width * offsets / np.max(np.abs(offsets))


def draw_distribution_summary(ax: plt.Axes, x: float, values: np.ndarray, color: str) -> None:
    """Overlay an IQR segment and median diamond on raw observations."""
    q1, median, q3 = np.percentile(values, [25, 50, 75])
    ax.vlines(x, q1, q3, color=color, linewidth=4.2, zorder=4)
    ax.scatter(
        [x],
        [median],
        marker="D",
        s=31,
        facecolor="white",
        edgecolor=color,
        linewidth=1.2,
        zorder=5,
    )


def cycle_convergence(data: dict) -> None:
    rows = data["cycle_cutoffs"]
    cutoffs = np.asarray([int(row["cutoff"]) for row in rows])
    beta_half = np.asarray([float(row["euler"]["0.5"]["leading_resonance"][0]) for row in rows])
    beta_one = np.asarray([float(row["euler"]["1.0"]["leading_resonance"][0]) for row in rows])
    flat = np.asarray([float(row["fredholm_resonance"][0]) for row in rows])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={"width_ratios": [1.05, 1]})
    ax1.plot(cutoffs, beta_half, marker="o", markersize=3, color=COLORS["purple"], label=r"Euler $\beta=1/2$")
    ax1.plot(cutoffs, beta_one, marker="s", markersize=3, color=COLORS["blue"], label=r"Euler $\beta=1$")
    ax1.plot(cutoffs, flat, marker="^", markersize=3, color=COLORS["orange"], label="Flat determinant")
    ax1.set_xlabel("Period cutoff $N$")
    ax1.set_ylabel("Leading modulus")
    ax1.set_xticks([1, 3, 5, 7, 9, 11, 12])
    ax1.legend(frameon=False, loc="lower right")

    mask = cutoffs >= 5
    ax2.plot(cutoffs[mask], beta_one[mask], marker="s", markersize=3, color=COLORS["blue"], label=r"Euler $\beta=1$")
    ax2.plot(cutoffs[mask], flat[mask], marker="^", markersize=3, color=COLORS["orange"], label="Flat determinant")
    ax2.axhline(beta_one[-1], color=COLORS["gray"], linestyle="--", linewidth=0.8)
    ax2.set_xlabel("Period cutoff $N$")
    ax2.set_ylabel("Leading modulus (zoom)")
    ax2.set_xticks(cutoffs[mask])
    ax2.ticklabel_format(axis="y", style="plain", useOffset=False)
    ax2.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    save(fig, "r059_cycle_convergence.pdf")


def gaps(data: dict) -> None:
    rows = data["sobol_groups"]
    chains = ["chain_24_48_96", "chain_32_64_128"]
    panel_labels = [r"(a) parent $M=96$", r"(b) parent $M=128$"]
    panel_colors = [COLORS["blue"], COLORS["orange"]]
    all_values = [
        100.0 * float(seed_row["relative_gap"])
        for row in rows
        for seed_row in row["seed_values"]
    ]
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0), sharey=True)

    for ax, chain, panel_label, color in zip(axes, chains, panel_labels, panel_colors):
        panel_rows = sorted(
            (row for row in rows if row["chain"] == chain),
            key=lambda row: (int(row["samples_per_cell"]), int(row["target_grid"])),
        )
        xpos = np.arange(len(panel_rows))
        for i, row in enumerate(panel_rows):
            seed_rows = sorted(row["seed_values"], key=lambda item: int(item["seed"]))
            values = np.asarray([100.0 * float(item["relative_gap"]) for item in seed_rows])
            jitter = symmetric_jitter(len(values), half_width=0.13)
            ax.scatter(
                i + jitter,
                values,
                s=19,
                color=color,
                edgecolor="white",
                linewidth=0.35,
                alpha=0.82,
                zorder=3,
            )
            draw_distribution_summary(ax, i, values, color)

        labels = [
            rf"$m={int(row['target_grid'])}$" + "\n" + rf"$s={int(row['samples_per_cell'])}$"
            for row in panel_rows
        ]
        ax.axhline(2.0, color=COLORS["gray"], linestyle="--", linewidth=1.0, zorder=1)
        ax.text(0.02, 0.96, panel_label, transform=ax.transAxes, ha="left", va="top")
        ax.set_xticks(xpos, labels)
        ax.set_xlim(-0.48, len(panel_rows) - 0.52)
        ax.set_ylim(-0.08, max(all_values) * 1.09)

    axes[0].set_ylabel("Direct/common relative gap (%)")
    legend_handles = [
        Line2D([], [], marker="o", linestyle="none", markersize=4.5, color=COLORS["gray"], label="seed"),
        Line2D([], [], linewidth=4.0, color=COLORS["gray"], label="IQR"),
        Line2D([], [], marker="D", markerfacecolor="white", markeredgecolor=COLORS["gray"], linestyle="none", markersize=4.5, label="median"),
        Line2D([], [], linestyle="--", linewidth=1.0, color=COLORS["gray"], label="2% gate"),
    ]
    axes[1].legend(handles=legend_handles, frameon=False, ncol=2, loc="upper right", handlelength=1.4, columnspacing=0.9)
    fig.tight_layout()
    save(fig, "r061_gaps.pdf")


def dyadic(data: dict) -> None:
    summaries = sorted(
        data["dyadic_groups"],
        key=lambda row: (row["chain"], int(row["samples_per_cell"])),
    )
    per_seed = data["dyadic_per_seed"]
    labels = [
        (r"$M=96$" if row["chain"] == "chain_24_48_96" else r"$M=128$")
        + "\n"
        + rf"$s={int(row['samples_per_cell'])}$"
        for row in summaries
    ]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.25), gridspec_kw={"width_ratios": [1.25, 1.0]})
    direct_color = COLORS["blue"]
    common_color = COLORS["orange"]

    all_signed: list[float] = []
    all_abs_differences: list[float] = []
    median_ratios: list[float] = []
    for i, summary in enumerate(summaries):
        group = sorted(
            (
                row
                for row in per_seed
                if row["chain"] == summary["chain"]
                and int(row["samples_per_cell"]) == int(summary["samples_per_cell"])
            ),
            key=lambda row: int(row["seed"]),
        )
        direct = 100.0 * np.asarray([float(row["direct_D"]) for row in group])
        common = 100.0 * np.asarray([float(row["common_D"]) for row in group])
        abs_difference = np.abs(common) - np.abs(direct)
        all_signed.extend(direct.tolist())
        all_signed.extend(common.tolist())
        all_abs_differences.extend(abs_difference.tolist())
        median_ratios.append(float(summary["abs_D_ratio"]["median"]))

        jitter = symmetric_jitter(len(group), half_width=0.055)
        direct_x = i - 0.17 + jitter
        common_x = i + 0.17 + jitter
        for x0, x1, y0, y1 in zip(direct_x, common_x, direct, common):
            ax1.plot([x0, x1], [y0, y1], color="#B5B5B5", linewidth=0.55, alpha=0.58, zorder=1)
        ax1.scatter(direct_x, direct, s=15, color=direct_color, alpha=0.78, zorder=2)
        ax1.scatter(common_x, common, s=15, color=common_color, alpha=0.78, zorder=2)
        draw_distribution_summary(ax1, i - 0.17, direct, direct_color)
        draw_distribution_summary(ax1, i + 0.17, common, common_color)

        difference_x = i + symmetric_jitter(len(group), half_width=0.12)
        ax2.scatter(
            difference_x,
            abs_difference,
            s=18,
            color=COLORS["purple"],
            edgecolor="white",
            linewidth=0.3,
            alpha=0.82,
            zorder=3,
        )
        draw_distribution_summary(ax2, i, abs_difference, COLORS["purple"])

    signed_span = max(abs(min(all_signed)), abs(max(all_signed))) * 1.10
    diff_span = max(abs(min(all_abs_differences)), abs(max(all_abs_differences))) * 1.12
    xpos = np.arange(len(summaries))
    ax1.axhline(0.0, color=COLORS["gray"], linewidth=0.8, zorder=0)
    ax1.set_ylim(-signed_span, signed_span)
    ax1.set_ylabel(r"Signed $D=\Delta_f-\Delta_i$ (percentage points)")
    ax1.set_xticks(xpos, labels)
    ax1.text(0.02, 0.97, "(a) paired seed values", transform=ax1.transAxes, ha="left", va="top")
    ax1.legend(
        handles=[
            Line2D([], [], marker="o", linestyle="none", color=direct_color, markersize=4.5, label="direct"),
            Line2D([], [], marker="o", linestyle="none", color=common_color, markersize=4.5, label="common cloud"),
        ],
        frameon=False,
        ncol=2,
        loc="lower left",
    )

    ax2.axhline(0.0, color=COLORS["gray"], linewidth=0.8, zorder=0)
    ax2.set_ylim(-diff_span, diff_span)
    ax2.set_ylabel(r"$|D_c|-|D_d|$ (percentage points)")
    ax2.set_xticks(xpos, labels)
    ax2.text(0.02, 0.97, "(b) paired absolute-contrast difference", transform=ax2.transAxes, ha="left", va="top")
    for i, ratio in enumerate(median_ratios):
        ax2.text(
            i,
            1.015,
            rf"$\widetilde{{r}}={ratio:.2f}$",
            transform=ax2.get_xaxis_transform(),
            ha="center",
            va="bottom",
            color=COLORS["green"] if ratio <= 0.8 else COLORS["gray"],
            fontsize=6.8,
        )
    fig.tight_layout()
    save(fig, "r061_dyadic.pdf")


def geometry_adjacency() -> None:
    """Draw the exact four state rectangles and the six allowed transitions."""
    x_minus = (-5.0 / 8.0, -1.0 / 3.0)
    x_plus = (1.0 / 3.0, 5.0 / 8.0)
    y_minus = (-81.0 / 128.0, -5.0 / 16.0)
    y_plus = (5.0 / 16.0, 81.0 / 128.0)
    states = [
        ("--", x_minus, y_minus, COLORS["blue"]),
        ("-+", x_minus, y_plus, COLORS["green"]),
        ("+-", x_plus, y_minus, COLORS["orange"]),
        ("++", x_plus, y_plus, COLORS["purple"]),
    ]

    fig, (ax_rect, ax_graph) = plt.subplots(1, 2, figsize=(7.0, 3.25), gridspec_kw={"width_ratios": [1.05, 1.0]})
    for label, xb, yb, color in states:
        patch = Rectangle(
            (xb[0], yb[0]),
            xb[1] - xb[0],
            yb[1] - yb[0],
            facecolor=color,
            edgecolor=color,
            linewidth=1.4,
            alpha=0.22,
        )
        ax_rect.add_patch(patch)
        ax_rect.text(
            0.5 * (xb[0] + xb[1]),
            0.5 * (yb[0] + yb[1]),
            rf"$N_{{{label}}}$",
            ha="center",
            va="center",
            color=color,
            fontsize=10,
        )
    ax_rect.axhline(0.0, color="#BBBBBB", linewidth=0.7, zorder=0)
    ax_rect.axvline(0.0, color="#BBBBBB", linewidth=0.7, zorder=0)
    ax_rect.set_xlim(-0.72, 0.72)
    ax_rect.set_ylim(-0.72, 0.72)
    ax_rect.set_aspect("equal")
    ax_rect.set_xlabel("$x$")
    ax_rect.set_ylabel("$y$")
    ax_rect.set_xticks(
        [-5 / 8, -1 / 3, 1 / 3, 5 / 8],
        [r"$-5/8$", r"$-1/3$", r"$1/3$", r"$5/8$"],
    )
    ax_rect.set_yticks(
        [-81 / 128, -5 / 16, 5 / 16, 81 / 128],
        [r"$-81/128$", r"$-5/16$", r"$5/16$", r"$81/128$"],
    )
    ax_rect.text(0.02, 0.98, "(a) state rectangles", transform=ax_rect.transAxes, ha="left", va="top")

    node_positions = {
        "--": (-0.68, -0.52),
        "-+": (-0.68, 0.52),
        "+-": (0.68, -0.52),
        "++": (0.68, 0.52),
    }
    state_colors = {label: color for label, _, _, color in states}

    def edge(source: str, target: str, rad: float = 0.0) -> None:
        arrow = FancyArrowPatch(
            node_positions[source],
            node_positions[target],
            arrowstyle="-|>",
            mutation_scale=10,
            connectionstyle=f"arc3,rad={rad}",
            color=COLORS["gray"],
            linewidth=1.15,
            shrinkA=15,
            shrinkB=15,
            zorder=1,
        )
        ax_graph.add_patch(arrow)

    edge("--", "+-", rad=0.0)
    edge("-+", "--", rad=0.0)
    edge("+-", "-+", rad=0.08)
    edge("+-", "++", rad=0.0)
    edge("++", "-+", rad=0.0)
    loop = FancyArrowPatch(
        (-0.77, -0.61),
        (-0.77, -0.43),
        arrowstyle="-|>",
        mutation_scale=10,
        connectionstyle="arc3,rad=-2.2",
        color=COLORS["gray"],
        linewidth=1.15,
        zorder=1,
    )
    ax_graph.add_patch(loop)

    for label, (x, y) in node_positions.items():
        ax_graph.scatter(
            [x],
            [y],
            s=660,
            facecolor="white",
            edgecolor=state_colors[label],
            linewidth=2.0,
            zorder=3,
        )
        ax_graph.text(
            x,
            y,
            rf"$\mathtt{{{label}}}$",
            ha="center",
            va="center",
            color=state_colors[label],
            fontsize=11,
            zorder=4,
        )

    ax_graph.set_xlim(-1.07, 1.07)
    ax_graph.set_ylim(-0.93, 0.93)
    ax_graph.set_aspect("equal")
    ax_graph.axis("off")
    ax_graph.text(0.02, 0.98, "(b) six allowed transitions", transform=ax_graph.transAxes, ha="left", va="top")
    ax_graph.text(
        0.5,
        0.02,
        r"state order $(\mathtt{--},\mathtt{-+},\mathtt{+-},\mathtt{++})$"
        "\nrow = source, column = target",
        transform=ax_graph.transAxes,
        ha="center",
        va="bottom",
        fontsize=7.6,
    )
    fig.tight_layout(w_pad=2.0)
    save(fig, "r059_geometry_adjacency.pdf")


def localization(data: dict, audit: dict) -> None:
    rows = data["localization_groups"]
    labels = [
        (r"$M=96$" if x["chain"] == "chain_24_48_96" else r"$M=128$")
        + "\n"
        + rf"$s={int(x['samples_per_cell'])},m={int(x['target_grid'])}$"
        for x in rows
    ]
    audit_map = {
        (x["chain"], int(x["samples_per_cell"]), int(x["target_grid"])): x
        for x in audit["group_summaries"]
    }
    sensitivity = [audit_map[(x["chain"], int(x["samples_per_cell"]), int(x["target_grid"]))] for x in rows]
    rho_support = np.array([100.0 * float(x["cell_rho"]["mean"]) for x in rows])
    rho_125 = np.array([100.0 * float(x["rho_tau_0.125"]["mean"]) for x in sensitivity])
    rho_25 = np.array([100.0 * float(x["rho_tau_0.25"]["mean"]) for x in sensitivity])
    top_125 = np.array([100.0 * float(x["top25_tau_0.125"]["mean"]) for x in sensitivity])
    top_25 = np.array([100.0 * float(x["top25_tau_0.25"]["mean"]) for x in sensitivity])
    x = np.arange(len(rows))
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(7.3, 2.75), gridspec_kw={"width_ratios": [0.85, 1.2, 1.2]})
    width = 0.36
    ax1.bar(x, rho_support, color=COLORS["purple"], width=0.65)
    ax1.set_title("(a) Formal gate")
    ax1.set_ylabel(r"Support Spearman $\rho$ (%)")
    ax1.set_xticks(x, labels, rotation=55, ha="right")
    ax1.set_ylim(0, 105)

    ax2.bar(x - width / 2, rho_125, width, color=COLORS["blue"], label=r"$\tau=.125$")
    ax2.bar(x + width / 2, rho_25, width, color=COLORS["orange"], label=r"$\tau=.25$")
    ax2.axhline(0.0, color=COLORS["gray"], linewidth=0.8)
    ax2.set_title("(b) Conditional correlation")
    ax2.set_ylabel(r"Conditional Spearman $\rho$ (%)")
    ax2.set_xticks(x, labels, rotation=55, ha="right")
    ax2.set_ylim(-38, 14)
    ax2.legend(frameon=False, loc="lower right")

    ax3.bar(x - width / 2, top_125, width, color=COLORS["blue"], label=r"$\tau=.125$")
    ax3.bar(x + width / 2, top_25, width, color=COLORS["orange"], label=r"$\tau=.25$")
    ax3.axhline(25.0, color=COLORS["gray"], linestyle="--", linewidth=0.8)
    ax3.text(0.02, 0.94, "25% row share", transform=ax3.transAxes, ha="left", va="top", fontsize=7)
    ax3.set_title("(c) Conditional concentration")
    ax3.set_ylabel("Top-quartile energy (%)")
    ax3.set_xticks(x, labels, rotation=55, ha="right")
    ax3.set_ylim(0, 30)
    fig.tight_layout()
    save(fig, "r061_localization.pdf")


def quadrature(data: dict) -> None:
    rows = data["gauss_gaps"]
    targets = [str(x["target_grid"]) for x in rows]
    values = [100.0 * float(x["q8_q12_gap"]) for x in rows]
    fig, ax = plt.subplots(figsize=(4.1, 2.55))
    x = np.arange(len(rows))
    baseline = 0.05
    ax.vlines(x, baseline, values, color=COLORS["green"], linewidth=2.2)
    ax.scatter(x, values, color=COLORS["green"], s=30, zorder=3)
    ax.axhline(1.0, color=COLORS["gray"], linestyle="--", linewidth=1.0, label="1% gate")
    for xi, value in zip(x, values):
        ax.annotate(f"{value:.3f}", (xi, value), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom", fontsize=7)
    ax.set_yscale("log")
    ax.set_ylabel(r"Relative $q=8$/$q=12$ gap (%)")
    ax.set_xlabel("Target grid")
    ax.set_xticks(x, targets)
    ax.set_ylim(baseline, 1.23)
    ax.set_yticks([0.05, 0.1, 0.2, 0.5, 1.0], ["0.05", "0.1", "0.2", "0.5", "1.0"])
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    save(fig, "r061_quadrature.pdf")


def main() -> None:
    data = load(ANALYSIS)
    localization_audit = load(LOCALIZATION_AUDIT)
    cycle_audit = load(CYCLE_AUDIT)
    if data.get("run_id") != "R061_COMMON_CLOUD_ANALYSIS":
        raise RuntimeError(f"unexpected R061 input: {data.get('run_id')!r}")
    if cycle_audit.get("run_id") != "R059_CERTIFIED_DOMAIN_SYMBOLIC_CYCLE":
        raise RuntimeError(f"unexpected R059 input: {cycle_audit.get('run_id')!r}")
    OUT.mkdir(parents=True, exist_ok=True)
    geometry_adjacency()
    cycle_convergence(cycle_audit)
    gaps(data)
    dyadic(data)
    localization(data, localization_audit)
    quadrature(data)
    generated = sorted(OUT.glob("r059_*.pdf")) + sorted(OUT.glob("r061_*.pdf"))
    print("generated", ", ".join(str(p.name) for p in generated))


if __name__ == "__main__":
    main()
