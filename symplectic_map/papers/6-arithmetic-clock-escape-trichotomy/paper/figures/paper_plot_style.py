"""Shared deterministic publication style for all Paper-5 figures."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from textwrap import fill

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DPI = 300
SVG_HASH_SALT = "paper5-additive-capacity-2026-08-14"
FIXED_DATE = datetime(2026, 8, 14, tzinfo=timezone.utc)

# Okabe--Ito colors, augmented with neutral ink and paper tones.
COLORS = {
    "blue": "#0072B2",
    "sky": "#56B4E9",
    "green": "#009E73",
    "orange": "#E69F00",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
    "yellow": "#F0E442",
    "ink": "#17212B",
    "muted": "#5E6A73",
    "line": "#AAB4BC",
    "paper": "#FFFFFF",
    "panel": "#F6F8FA",
    "pale_blue": "#E9F3F9",
    "pale_green": "#E6F4EF",
    "pale_orange": "#FFF3D9",
    "pale_purple": "#F5EAF1",
    "pale_gray": "#EEF1F3",
}


def configure_style() -> None:
    """Apply a print-safe, deterministic Matplotlib configuration."""

    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["DejaVu Serif"],
            "font.sans-serif": ["DejaVu Sans"],
            "mathtext.fontset": "dejavuserif",
            "font.size": 8.5,
            "axes.labelsize": 8.5,
            "axes.titlesize": 9.5,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "legend.fontsize": 7.5,
            "figure.dpi": DPI,
            "savefig.dpi": DPI,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.04,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "svg.hashsalt": SVG_HASH_SALT,
            "text.usetex": False,
            "axes.unicode_minus": False,
            "figure.facecolor": COLORS["paper"],
            "axes.facecolor": COLORS["paper"],
        }
    )


def wrapped(text: str, width: int) -> str:
    return fill(text, width=width, break_long_words=False, break_on_hyphens=False)


def add_box(
    ax,
    xy: tuple[float, float],
    width: float,
    height: float,
    *,
    facecolor: str = COLORS["panel"],
    edgecolor: str = COLORS["line"],
    linewidth: float = 1.0,
    radius: float = 0.015,
    zorder: int = 2,
) -> FancyBboxPatch:
    box = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle=f"round,pad=0.008,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        transform=ax.transAxes,
        clip_on=False,
        zorder=zorder,
    )
    ax.add_patch(box)
    return box


def add_arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = COLORS["muted"],
    connectionstyle: str = "arc3,rad=0",
    linewidth: float = 1.15,
    mutation_scale: float = 10,
    zorder: int = 1,
) -> FancyArrowPatch:
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=linewidth,
        color=color,
        connectionstyle=connectionstyle,
        transform=ax.transAxes,
        clip_on=False,
        zorder=zorder,
    )
    ax.add_patch(arrow)
    return arrow


def panel_label(ax, label: str, x: float, y: float) -> None:
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=9.5,
        fontweight="bold",
        color=COLORS["ink"],
        zorder=5,
    )


def status_badge(ax, x: float, y: float, text: str = "PASS", *, color: str = COLORS["green"]) -> None:
    ax.text(
        x,
        y,
        text,
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.8,
        fontweight="bold",
        color=COLORS["paper"],
        bbox={"boxstyle": "round,pad=0.25", "facecolor": color, "edgecolor": color, "linewidth": 0.6},
        zorder=6,
    )


def save_figure(fig, output_dir: Path, stem: str, *, description: str) -> dict[str, Path]:
    """Save deterministic PDF/SVG masters and a 300-dpi review PNG."""

    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {extension: output_dir / f"{stem}.{extension}" for extension in ("pdf", "svg", "png")}
    common_title = stem.replace("_", " ")
    fig.savefig(
        outputs["pdf"],
        format="pdf",
        metadata={
            "Title": common_title,
            "Author": "Paper 5 reproducible figure pipeline",
            "Subject": description,
            "Keywords": "additive arithmetic capacity, exact audit",
            "Creator": "Matplotlib deterministic Paper-5 pipeline",
            "Producer": "Matplotlib deterministic Paper-5 pipeline",
            "CreationDate": FIXED_DATE,
            "ModDate": FIXED_DATE,
        },
    )
    fig.savefig(
        outputs["svg"],
        format="svg",
        metadata={
            "Title": common_title,
            "Description": description,
            "Creator": "Matplotlib deterministic Paper-5 pipeline",
            "Date": "2026-08-14",
        },
    )
    fig.savefig(
        outputs["png"],
        format="png",
        dpi=DPI,
        metadata={
            "Software": "Matplotlib deterministic Paper-5 pipeline",
            "Title": common_title,
            "Description": description,
            "Creation Time": "2026-08-14T00:00:00Z",
        },
    )
    plt.close(fig)
    return outputs


configure_style()
