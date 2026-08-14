from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyBboxPatch


FIG_DIR = Path(__file__).resolve().parent
DPI = 300

OKABE_ITO = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
    "yellow": "#F0E442",
    "sky": "#56B4E9",
    "black": "#000000",
    "gray": "#7A7A7A",
    "light_gray": "#E5E5E5",
    "soft_green": "#D9F0E3",
    "soft_orange": "#FCE5CD",
    "soft_blue": "#DDEBF7",
    "soft_red": "#F8D7DA",
    "soft_yellow": "#FFF3CD",
}

rcParams.update(
    {
        "font.size": 9.5,
        "font.family": "serif",
        "font.serif": ["DejaVu Serif", "Times New Roman", "Times"],
        "axes.labelsize": 9.5,
        "axes.titlesize": 10.5,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.fontsize": 8.5,
        "figure.dpi": DPI,
        "savefig.dpi": DPI,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
        "axes.grid": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "mathtext.fontset": "stix",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)


def save_fig(fig: plt.Figure, stem: str) -> tuple[Path, Path]:
    pdf_path = FIG_DIR / f"{stem}.pdf"
    png_path = FIG_DIR / f"{stem}.png"
    fig.savefig(pdf_path, format="pdf")
    fig.savefig(png_path, format="png", dpi=DPI)
    return pdf_path, png_path


def add_panel_tag(ax, tag: str) -> None:
    ax.text(
        0.0,
        1.02,
        tag,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color=OKABE_ITO["black"],
    )


def rounded_box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    facecolor: str,
    edgecolor: str,
    linewidth: float = 1.0,
    rounding: float = 0.02,
    **kwargs,
):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.01,rounding_size={rounding}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        **kwargs,
    )
    ax.add_patch(patch)
    return patch


def status_color(status: str) -> tuple[str, str]:
    status = status.upper()
    if "PASS" in status or "ABSENT_BY_THEOREM" in status or status == "ABSENT":
        return OKABE_ITO["soft_green"], OKABE_ITO["green"]
    if "OPEN" in status:
        return OKABE_ITO["soft_yellow"], OKABE_ITO["orange"]
    if "OUTSIDE" in status or "DISABLED" in status:
        return OKABE_ITO["light_gray"], OKABE_ITO["gray"]
    return OKABE_ITO["soft_red"], OKABE_ITO["vermillion"]

