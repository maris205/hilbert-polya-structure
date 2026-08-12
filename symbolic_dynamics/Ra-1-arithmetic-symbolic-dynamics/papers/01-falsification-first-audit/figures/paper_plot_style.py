"""Shared publication plotting style for the Stage-01 paper."""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt


FIGURE_DIR = Path(__file__).resolve().parent

COLORS = {
    "blue": "#4C78A8",
    "orange": "#F58518",
    "green": "#54A24B",
    "red": "#E45756",
    "purple": "#B279A2",
    "gray": "#79706E",
    "light_gray": "#D9D9D9",
}

mpl.rcParams.update(
    {
        "font.size": 9,
        "font.family": "serif",
        "font.serif": ["DejaVu Serif"],
        "axes.labelsize": 9,
        "axes.titlesize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "figure.dpi": 160,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "mathtext.fontset": "stix",
    }
)


def save_figure(fig: plt.Figure, stem: str) -> None:
    """Save a vector PDF and a review PNG from one source figure."""

    fig.savefig(FIGURE_DIR / f"{stem}.pdf")
    fig.savefig(FIGURE_DIR / f"{stem}.png")
    plt.close(fig)
