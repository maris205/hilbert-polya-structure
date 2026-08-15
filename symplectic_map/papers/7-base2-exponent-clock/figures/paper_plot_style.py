"""Shared deterministic publication style for Paper 7 figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams.update(
    {
        "font.family": "serif",
        "font.serif": ["DejaVu Serif"],
        "font.size": 9.5,
        "axes.labelsize": 9.5,
        "axes.titlesize": 10.0,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.fontsize": 8.5,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.6,
        "lines.markersize": 5.0,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "svg.hashsalt": "paper7-base2-exponent-clock-v1",
        "mathtext.fontset": "dejavuserif",
        "axes.unicode_minus": False,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
        "figure.dpi": 150,
        "savefig.dpi": 300,
    }
)

import matplotlib.pyplot as plt  # noqa: E402


FIG_DIR = Path(__file__).resolve().parent

# Okabe--Ito-inspired, print-friendly palette.
COLORS = {
    "blue": "#0072B2",
    "sky": "#56B4E9",
    "orange": "#E69F00",
    "green": "#009E73",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
    "gray": "#6C757D",
    "dark": "#23303F",
    "light_blue": "#E6F2F8",
    "light_green": "#E3F4EE",
    "light_orange": "#FFF2D6",
    "light_gray": "#F0F2F4",
    "white": "#FFFFFF",
}


def save_all(fig: matplotlib.figure.Figure, stem: str) -> None:
    """Save deterministic PDF/SVG masters plus a 300 dpi PNG preview."""

    pdf_metadata = {
        "Creator": "Paper 7 deterministic figure pipeline",
        "Producer": "Matplotlib",
        "CreationDate": None,
        "ModDate": None,
    }
    svg_metadata = {
        "Creator": "Paper 7 deterministic figure pipeline",
        "Date": None,
    }
    png_metadata = {"Software": "Paper 7 deterministic figure pipeline"}
    fig.savefig(FIG_DIR / f"{stem}.pdf", format="pdf", metadata=pdf_metadata)
    fig.savefig(FIG_DIR / f"{stem}.svg", format="svg", metadata=svg_metadata)
    fig.savefig(FIG_DIR / f"{stem}.png", format="png", metadata=png_metadata)
    plt.close(fig)

