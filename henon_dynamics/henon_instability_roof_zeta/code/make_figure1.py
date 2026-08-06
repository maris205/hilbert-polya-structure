#!/usr/bin/env python3
"""Generate the research note's main diagnostic figure from persisted results."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT = PROJECT_ROOT / "results" / "analysis_summary.json"
OUTPUT_DIR = PROJECT_ROOT / "paper" / "figures"


def configure_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 9,
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.03,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "mathtext.fontset": "stix",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def main() -> None:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    root_rows = [row for row in payload["root_rows"] if row["sector"] == 0]
    cutoffs = np.asarray([row["cutoff"] for row in root_rows], dtype=int)
    roots = np.asarray([row["positive_real_root"] for row in root_rows], dtype=float)
    reference = float(payload["untwisted"]["h20_high_precision"])
    differences = np.maximum(np.abs(roots - reference), 1e-18)

    valid_random_names = {
        "positive_random_weights": "positive weights",
        "random_phases": "random phases",
        "same_density_random_lengths": "random lengths",
    }
    rows_by_name = {row["control"]: row for row in payload["control_rows"]}
    labels = ["constant roof", "Hénon"] + list(valid_random_names.values())
    ratios = [
        rows_by_name["constant_roof_parent"]["tail_ratio_vs_henon"],
        1.0,
        *[
            rows_by_name[name]["tail_ratio_vs_henon"]
            for name in valid_random_names
        ],
    ]

    configure_style()
    figure, axes = plt.subplots(1, 2, figsize=(7.1, 2.65))

    left = axes[0]
    left.semilogy(
        cutoffs,
        differences,
        color="#0072B2",
        marker="o",
        markersize=4,
        linewidth=1.4,
    )
    left.axhline(1e-12, color="#777777", linestyle="--", linewidth=0.8)
    left.text(7.2, 1.6e-12, "displayed-reference scale", fontsize=7, color="#555555")
    left.set_xlabel("cycle-section cutoff $N$")
    left.set_ylabel(r"$|h_N-h_{20}|$")
    left.set_xticks(cutoffs)
    left.grid(axis="y", which="both", linewidth=0.35, color="#dddddd")
    left.text(-0.14, 1.02, "(a)", transform=left.transAxes, fontweight="bold")

    right = axes[1]
    positions = np.arange(len(labels))
    colors = ["#CC79A7", "#0072B2", "#E69F00", "#009E73", "#56B4E9"]
    right.bar(positions, ratios, color=colors, width=0.72)
    right.axhline(1.0, color="#333333", linewidth=0.8, linestyle="--")
    right.set_yscale("log")
    right.set_ylabel("degree-9--16 tail / Hénon tail")
    right.set_xticks(positions)
    right.set_xticklabels(labels, rotation=27, ha="right")
    right.grid(axis="y", which="major", linewidth=0.35, color="#dddddd")
    right.text(-0.14, 1.02, "(b)", transform=right.transAxes, fontweight="bold")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    figure.tight_layout(w_pad=2.0)
    pdf_path = OUTPUT_DIR / "figure1_stability_controls.pdf"
    png_path = OUTPUT_DIR / "figure1_stability_controls.png"
    figure.savefig(pdf_path, metadata={"CreationDate": None, "ModDate": None})
    figure.savefig(png_path)
    plt.close(figure)
    print(pdf_path)
    print(png_path)


if __name__ == "__main__":
    main()
