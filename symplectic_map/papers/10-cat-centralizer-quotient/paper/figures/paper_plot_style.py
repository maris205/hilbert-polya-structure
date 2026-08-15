"""Shared deterministic publication style for Paper 10 figures."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DPI = 300
FONT_SIZE = 8.2
FIXED_DATE = datetime(2026, 8, 15, tzinfo=timezone.utc)

# Okabe--Ito palette; every scientific status also has text/shape redundancy.
BLUE = "#0072B2"
SKY = "#56B4E9"
GREEN = "#009E73"
ORANGE = "#E69F00"
VERMILLION = "#D55E00"
PURPLE = "#CC79A7"
BLACK = "#202124"
MID_GRAY = "#73777B"
LIGHT_GRAY = "#E8EAED"
PALE_BLUE = "#E8F2F8"
PALE_GREEN = "#E5F4EF"
PALE_ORANGE = "#FFF1D6"
PALE_RED = "#FBE9E5"
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
        "legend.fontsize": FONT_SIZE - 0.7,
        "figure.dpi": DPI,
        "savefig.dpi": DPI,
        "savefig.facecolor": WHITE,
        "savefig.edgecolor": WHITE,
        "axes.facecolor": WHITE,
        "figure.facecolor": WHITE,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.7,
        "lines.linewidth": 1.2,
        "patch.linewidth": 0.8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "svg.hashsalt": "paper10-centralizer-quotient-v1",
        "text.usetex": False,
        "axes.unicode_minus": False,
        "path.simplify": False,
    }
)


def panel_label(ax, label: str, descriptor: str) -> None:
    ax.text(
        0.0,
        1.02,
        f"{label}  {descriptor}",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=FONT_SIZE + 0.35,
        fontweight="bold",
        color=BLACK,
        clip_on=False,
    )


def clean_axis(ax) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


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
    hatch: str | None = None,
    radius: float = 0.02,
    zorder: int = 2,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle=f"round,pad=0.012,rounding_size={radius}",
        transform=ax.transAxes,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
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
    mutation_scale: float = 8.0,
    connectionstyle: str = "arc3",
) -> FancyArrowPatch:
    item = FancyArrowPatch(
        start,
        end,
        transform=ax.transAxes,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=linewidth,
        color=color,
        connectionstyle=connectionstyle,
        shrinkA=1.5,
        shrinkB=1.5,
    )
    ax.add_patch(item)
    return item


def output_paths(output_dir: Path, stem: str) -> Iterable[Path]:
    for suffix in ("pdf", "svg", "png"):
        yield output_dir / f"{stem}.{suffix}"


def save_figure(fig, output_dir: Path, stem: str, *, metadata_title: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_metadata = {
        "Title": metadata_title,
        "Author": "Anonymous figure generator",
        "Subject": "Manifest-bound exact cat-map centralizer quotient audit",
        "Keywords": "cat map, centralizer, cyclic vectors, quotient dynamics, exact audit",
        "Creator": "Matplotlib deterministic publication generator",
        "Producer": "Matplotlib",
        "CreationDate": FIXED_DATE,
        "ModDate": FIXED_DATE,
    }
    svg_metadata = {
        "Title": metadata_title,
        "Creator": "Matplotlib deterministic publication generator",
        "Date": "2026-08-15",
        "Description": "Manifest-bound exact cat-map centralizer quotient audit",
    }
    png_metadata = {
        "Title": metadata_title,
        "Author": "Anonymous figure generator",
        "Description": "Manifest-bound exact cat-map centralizer quotient audit",
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
