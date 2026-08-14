"""Shared deterministic publication style for Paper 4 figures."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import matplotlib as mpl


COLORS = {
    "blue": "#0072B2",
    "sky": "#56B4E9",
    "green": "#009E73",
    "orange": "#E69F00",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "ink": "#20242A",
    "muted": "#667085",
    "grid": "#D7DCE2",
    "wash": "#F5F7FA",
    "paper": "#FFFFFF",
}


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.2,
            "axes.labelsize": 8.2,
            "axes.titlesize": 9.0,
            "xtick.labelsize": 7.6,
            "ytick.labelsize": 7.6,
            "legend.fontsize": 7.5,
            "text.color": COLORS["ink"],
            "axes.labelcolor": COLORS["ink"],
            "axes.edgecolor": COLORS["muted"],
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "axes.linewidth": 0.7,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "svg.hashsalt": "algebraic-action-clocks-paper-v1",
            "savefig.facecolor": COLORS["paper"],
            "savefig.edgecolor": COLORS["paper"],
        }
    )


def save_figure(fig, stem: Path) -> None:
    """Write vector masters and a review PNG with fixed metadata."""

    frozen = datetime(2026, 8, 14, 0, 0, 0, tzinfo=timezone.utc)
    fig.savefig(
        stem.with_suffix(".pdf"),
        bbox_inches="tight",
        metadata={"CreationDate": frozen, "ModDate": frozen},
    )
    fig.savefig(
        stem.with_suffix(".svg"),
        bbox_inches="tight",
        metadata={"Date": "2026-08-14"},
    )
    fig.savefig(stem.with_suffix(".png"), dpi=240, bbox_inches="tight")
