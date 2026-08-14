#!/usr/bin/env python3
"""Generate split-scale, numerical-error, residual, and control audit panels.

The script reads the three frozen floating-stress JSON files, the independent
parent audit, the exact preflight, and the source lock.  No displayed metric is
recomputed from paper prose.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from paper_plot_style import COLORS, panel_label, save_figure


FIGURE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = FIGURE_DIR.parents[1]
SPLITS = ("development", "validation", "test")


def load_json(relative: str) -> dict:
    return json.loads((PROJECT_ROOT / relative).read_text(encoding="utf-8"))


def main() -> None:
    lock = load_json("experiments/source_lock.json")
    stresses = [load_json(f"results/float_stress_{split}.json") for split in SPLITS]
    parent = load_json("results/parent_audit.json")
    preflight = load_json("results/exact_preflight.json")

    assert [row["split"] for row in stresses] == list(SPLITS)
    assert all(row["passed"] and row["frozen_scale_executed"] for row in stresses)
    assert all(row["completed_checks"] == row["expected_checks"] for row in stresses)
    assert all(row["completed_checks"] == row["points"] * row["steps"] for row in stresses)
    assert all(row["boundary_failures"] == 0 and row["edge_mismatches"] == 0
               for row in stresses)
    assert parent["passed"] and parent["digits"] == lock["verification_protocol"][
        "independent_parent_audit_digits"
    ]
    assert preflight["controls"]["passed"]

    checks = np.array([row["completed_checks"] for row in stresses], dtype=int)
    errors = np.array([row["max_roundtrip_error"] for row in stresses], dtype=float)
    thresholds = np.array(
        [row["thresholds"]["max_roundtrip_error"] for row in stresses], dtype=float
    )
    assert np.all(thresholds == thresholds[0])

    residual_labels = ["parameter\npolynomial", "postcritical\nrelations",
                       "periodic\nfactor"]
    residuals = np.array(
        [
            float(parent["parameter"]["polynomial_residual"]),
            float(parent["postcritical"]["max_abs_residual"]),
            float(parent["periodic_factor"]["max_periodic_residual"]),
        ]
    )
    residual_target = float(parent["thresholds"]["residual_target"])
    assert np.all(residuals < residual_target)

    fig, axes = plt.subplots(2, 2, figsize=(7.05, 4.75))
    ax_checks, ax_error, ax_residual, ax_controls = axes.flat
    split_labels = ["development", "validation", "test"]
    split_colors = [COLORS["gray"], COLORS["sky"], COLORS["blue"]]

    # (a) Confirmatory work scale.  Bars are shown in millions solely to keep
    # the axis readable; exact integer counts are printed on each bar.
    y = np.arange(len(SPLITS))
    ax_checks.barh(y, checks / 1e6, color=split_colors, height=0.55)
    ax_checks.set_yticks(y, split_labels)
    ax_checks.invert_yaxis()
    ax_checks.set_xlim(0, 18.8)
    ax_checks.set_xlabel("per-step forward/inverse checks (millions)")
    for index, count in enumerate(checks):
        ax_checks.text(count / 1e6 - 0.25, index, f"{count:,}", ha="right",
                       va="center", color="white", fontsize=7.5,
                       fontweight="bold")
    points, steps = stresses[0]["points"], stresses[0]["steps"]
    ax_checks.text(
        0.98, 1.015, f"{points:,} points × {steps} steps; 0 boundary / edge failures",
        transform=ax_checks.transAxes, ha="right", va="bottom", fontsize=6.5,
        color=COLORS["gray"], clip_on=False,
    )
    panel_label(ax_checks, "a")

    # (b) Identified one-step inverse error, explicitly not a long-trajectory
    # reversal metric.
    x = np.arange(len(SPLITS))
    ax_error.axhline(thresholds[0], color=COLORS["orange"], linewidth=1.0,
                     linestyle=(0, (3, 2)), label="frozen threshold")
    ax_error.plot(x, errors, color=COLORS["blue"], marker="o",
                  label="maximum error")
    ax_error.set_yscale("log")
    ax_error.set_ylim(5e-17, 1e-12)
    ax_error.set_xticks(x, ["dev.", "validation", "test"])
    ax_error.set_ylabel("maximum roundtrip error")
    ax_error.text(
        0.50, 0.13, f"observed {errors.max():.3g}\nthreshold {thresholds[0]:.1g}",
        transform=ax_error.transAxes, ha="center", va="bottom", fontsize=7.5,
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.5},
    )
    ax_error.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.84),
                    handlelength=1.5, labelspacing=0.25, borderaxespad=0.0)
    panel_label(ax_error, "b")

    # (c) Independent high-precision parent consistency audit.
    residual_x = np.arange(len(residuals))
    ax_residual.axhline(residual_target, color=COLORS["orange"], linewidth=1.0,
                        linestyle=(0, (3, 2)))
    ax_residual.scatter(residual_x, residuals, s=30,
                        color=[COLORS["purple"], COLORS["green"], COLORS["blue"]],
                        zorder=3)
    ax_residual.vlines(residual_x, 1e-102, residuals,
                       color=COLORS["light_gray"], linewidth=0.8, zorder=1)
    ax_residual.set_yscale("log")
    ax_residual.set_ylim(5e-102, 1e-72)
    ax_residual.set_xticks(residual_x, residual_labels)
    ax_residual.set_ylabel("absolute residual")
    ax_residual.text(
        0.02, 0.82, f"{parent['digits']}-digit consistency audit",
        transform=ax_residual.transAxes, ha="left", va="top", fontsize=7.5,
        color=COLORS["gray"],
    )
    ax_residual.text(
        0.98, 0.98, "frozen target $10^{-75}$",
        transform=ax_residual.transAxes, ha="right", va="top", fontsize=6.9,
        color=COLORS["orange"],
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.25},
    )
    panel_label(ax_residual, "c")

    # (d) Six frozen controls.  Each row aggregates only the preregistered gates
    # belonging to that control; the quantitative determinant values are read
    # from exact_preflight.json.
    gates = preflight["controls"]["gates"]
    control_groups = [
        ("Dyadic", ("dyadic_ledger_total", "dyadic_symplectic")),
        ("Folded-tent", ("folded_branch_symplectic",)),
        ("Dissipative match", ("matched_dissipative_det_half",
                                  "matched_dissipative_non_surjective",
                                  "matched_dissipative_same_graph")),
        ("Label erasure", ("label_erasure_loses_past",)),
        ("Anti-symplectic", ("anti_symplectic_rejected_signature",)),
        ("All-positive null", ("all_positive_null_changes_signs",
                                    "all_positive_null_removes_nilpotent_cancellation",
                                    "all_positive_null_same_unsigned_graph",
                                    "all_positive_null_weight_matrix_is_A")),
    ]
    control_pass = [all(gates[key] for key in keys) for _, keys in control_groups]
    assert all(control_pass)

    dyadic_text = lock["controls"]["dyadic_baker"]
    dyadic_total_match = re.search(r"recover ([0-9,]+) primitive", dyadic_text)
    assert dyadic_total_match is not None
    dyadic_total = int(dyadic_total_match.group(1).replace(",", ""))
    dissipative_det = sorted(preflight["controls"]["dissipative_determinants"].values())[0]
    anti_min_det = min(preflight["controls"]["anti_symplectic_determinants"].values())
    detail = [
        f"{dyadic_total} cycles; det +1",
        "paired reversal",
        f"same graph; det {dissipative_det:g}",
        "unique past lost",
        f"det {anti_min_det:g} detected",
        "cancellation removed",
    ]

    ax_controls.set_xlim(0, 1)
    ax_controls.set_ylim(0, 1)
    ax_controls.axis("off")
    ax_controls.text(0.085, 0.94, "control", ha="left", va="center",
                     fontsize=6.5, color=COLORS["gray"])
    ax_controls.text(0.84, 0.94, "verified gate", ha="right", va="center",
                     fontsize=6.5, color=COLORS["gray"])
    ax_controls.text(0.98, 0.94, "status", ha="right", va="center",
                     fontsize=6.5, color=COLORS["gray"])
    ax_controls.plot([0.02, 0.98], [0.90, 0.90], color=COLORS["gray"],
                     linewidth=0.7)
    row_y = np.linspace(0.82, 0.12, len(control_groups))
    for index, ((name, _), passed, description) in enumerate(
        zip(control_groups, control_pass, detail)
    ):
        y_value = row_y[index]
        if index:
            ax_controls.plot([0.02, 0.98], [y_value + 0.065, y_value + 0.065],
                             color="#EEEEEE", linewidth=0.6)
        ax_controls.scatter([0.045], [y_value], s=18, color=COLORS["green"], zorder=3)
        ax_controls.text(0.085, y_value, name, ha="left", va="center", fontsize=6.6)
        ax_controls.text(0.84, y_value, description, ha="right", va="center",
                         fontsize=6.0, color=COLORS["gray"])
        ax_controls.text(0.99, y_value, "PASS" if passed else "FAIL", ha="right",
                         va="center", fontsize=6.2,
                         color=COLORS["green"] if passed else COLORS["orange"],
                         fontweight="bold")
    panel_label(ax_controls, "d")

    for ax in (ax_checks, ax_error, ax_residual):
        ax.tick_params(direction="out", length=3, width=0.7)
    fig.subplots_adjust(wspace=0.34, hspace=0.48)
    save_figure(fig, "fig3_audit_panel")


if __name__ == "__main__":
    main()
