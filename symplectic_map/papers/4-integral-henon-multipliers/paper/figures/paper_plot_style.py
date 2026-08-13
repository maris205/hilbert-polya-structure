"""Shared publication style for the frozen Hénon audit figures."""

from __future__ import annotations

from datetime import datetime, timezone

import matplotlib as mpl


COLORS = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "sky": "#56B4E9",
    "yellow": "#F0E442",
    "ink": "#20242A",
    "muted": "#667085",
    "grid": "#D7DCE2",
    "paper": "#FFFFFF",
    "wash": "#F5F7FA",
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
            "svg.hashsalt": "integral-henon-multipliers-paper-v1",
            "savefig.facecolor": COLORS["paper"],
            "savefig.edgecolor": COLORS["paper"],
        }
    )


def save_figure(fig, stem) -> None:
    """Save vector masters and a review PNG from one Matplotlib figure."""

    frozen_time = datetime(2026, 8, 14, 0, 0, 0, tzinfo=timezone.utc)
    fig.savefig(
        stem.with_suffix(".pdf"),
        bbox_inches="tight",
        metadata={"CreationDate": frozen_time, "ModDate": frozen_time},
    )
    fig.savefig(
        stem.with_suffix(".svg"),
        bbox_inches="tight",
        metadata={"Date": "2026-08-14"},
    )
    fig.savefig(stem.with_suffix(".png"), dpi=240, bbox_inches="tight")
