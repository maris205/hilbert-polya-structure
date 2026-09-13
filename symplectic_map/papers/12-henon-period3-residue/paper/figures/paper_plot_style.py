"""Deterministic, grayscale-safe publication style for Paper 12 figures."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DPI = 300
FONT_SIZE = 8.0
FIXED_DATE = datetime(2026, 8, 16, tzinfo=timezone.utc)

# Okabe--Ito colors. Every claim-bearing distinction is also encoded by
# wording, border style, shape, or hatch so the diagrams remain legible in
# grayscale and for common color-vision deficiencies.
BLUE = "#0072B2"
SKY = "#56B4E9"
GREEN = "#009E73"
ORANGE = "#E69F00"
VERMILLION = "#D55E00"
PURPLE = "#CC79A7"
BLACK = "#202124"
MID_GRAY = "#6F7377"
LIGHT_GRAY = "#E8EAED"
PALE_BLUE = "#E8F2F8"
PALE_GREEN = "#E5F4EF"
PALE_ORANGE = "#FFF1D6"
PALE_RED = "#FBE9E5"
PALE_PURPLE = "#F7EAF2"
WHITE = "#FFFFFF"

matplotlib.rcParams.update(
    {
        "font.size": FONT_SIZE,
        "font.family": "serif",
        "font.serif": ["DejaVu Serif"],
        "mathtext.fontset": "dejavuserif",
        "axes.labelsize": FONT_SIZE,
        "axes.titlesize": FONT_SIZE,
        "xtick.labelsize": FONT_SIZE - 0.4,
        "ytick.labelsize": FONT_SIZE - 0.4,
        "legend.fontsize": FONT_SIZE - 0.6,
        "figure.dpi": DPI,
        "savefig.dpi": DPI,
        "savefig.facecolor": WHITE,
        "savefig.edgecolor": WHITE,
        "figure.facecolor": WHITE,
        "axes.facecolor": WHITE,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.unicode_minus": False,
        "lines.linewidth": 1.1,
        "patch.linewidth": 0.85,
        "path.simplify": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "svg.hashsalt": "paper12-henon-period3-proof-only-v1",
        "text.usetex": False,
    }
)


def clean_axis(ax) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def panel_marker(ax, x: float, y: float, label: str) -> None:
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=FONT_SIZE + 1.0,
        fontweight="bold",
        color=BLACK,
        zorder=10,
    )


def rounded_box(
    ax,
    x: float,
    y: float,
    width: float,
    height: float,
    text: str,
    *,
    facecolor: str = WHITE,
    edgecolor: str = BLACK,
    textcolor: str = BLACK,
    fontsize: float = FONT_SIZE,
    linewidth: float = 0.9,
    linestyle: str = "-",
    hatch: str | None = None,
    radius: float = 0.018,
    zorder: int = 2,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle=f"round,pad=0.010,rounding_size={radius}",
        transform=ax.transAxes,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        linestyle=linestyle,
        hatch=hatch,
        zorder=zorder,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=textcolor,
        linespacing=1.16,
        zorder=zorder + 1,
    )
    return patch


def arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = MID_GRAY,
    linewidth: float = 1.0,
    linestyle: str = "-",
    mutation_scale: float = 8.0,
    connectionstyle: str = "arc3",
    zorder: int = 1,
) -> FancyArrowPatch:
    item = FancyArrowPatch(
        start,
        end,
        transform=ax.transAxes,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=linewidth,
        linestyle=linestyle,
        color=color,
        connectionstyle=connectionstyle,
        shrinkA=1.5,
        shrinkB=1.5,
        zorder=zorder,
    )
    ax.add_patch(item)
    return item


def cross_out(ax, x: float, y: float, width: float, height: float) -> None:
    for x0, y0, x1, y1 in (
        (x + 0.02 * width, y + 0.04 * height, x + 0.98 * width, y + 0.96 * height),
        (x + 0.02 * width, y + 0.96 * height, x + 0.98 * width, y + 0.04 * height),
    ):
        ax.add_line(
            Line2D(
                [x0, x1],
                [y0, y1],
                transform=ax.transAxes,
                color=VERMILLION,
                linewidth=1.35,
                alpha=0.88,
                zorder=6,
            )
        )


def save_figure(fig, output_dir: Path, stem: str, description: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_metadata = {
        "Title": f"Paper 12 {stem}",
        "Author": "Anonymous asset author",
        "Subject": description,
        "Keywords": "Henon map, formal period three, residue, proof-only",
        "Creator": "Matplotlib deterministic publication generator",
        "Producer": "Matplotlib",
        "CreationDate": FIXED_DATE,
        "ModDate": FIXED_DATE,
    }
    svg_metadata = {
        "Title": f"Paper 12 {stem}",
        "Creator": "Matplotlib deterministic publication generator",
        "Date": "2026-08-16",
        "Description": description,
    }
    png_metadata = {
        "Title": f"Paper 12 {stem}",
        "Author": "Anonymous asset author",
        "Description": description,
        "Software": "Matplotlib deterministic publication generator",
    }
    fig.savefig(
        output_dir / f"{stem}.pdf",
        format="pdf",
        dpi=DPI,
        metadata=pdf_metadata,
        bbox_inches=None,
    )
    fig.savefig(
        output_dir / f"{stem}.svg",
        format="svg",
        dpi=DPI,
        metadata=svg_metadata,
        bbox_inches=None,
    )
    fig.savefig(
        output_dir / f"{stem}.png",
        format="png",
        dpi=DPI,
        metadata=png_metadata,
        bbox_inches=None,
    )
    plt.close(fig)
