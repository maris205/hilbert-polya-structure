#!/usr/bin/env python3
"""Generate the Route-A result matrix directly from frozen YAML records."""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import yaml
from matplotlib.colors import ListedColormap

from paper_plot_style import COLORS, save_figure


PAPER_ROOT = Path(__file__).resolve().parents[1]
EVALUATION_ROOT = PAPER_ROOT / "evaluations" / "route_a"
GATES = ("a0", "a1", "a2", "a3", "a4")
GATE_LABELS = ("A0\narithmetic", "A1\norbits", "A2\ndeterminant", "A3\nglobal", "A4\nlift", "Route B")

SUPPORTED = {
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A0_ANALYTIC_ARITHMETIC_ORIGIN",
    "A1_PASS_ANALYTIC",
    "A2_ANALYTIC_DETERMINANT",
}
PARTIAL = {
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_WEAK",
    "A3_PARTIAL_ANALYTIC_STRUCTURE",
    "A4_FORMAL_HINT",
}
FAILED = {"A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"}


def classify(verdict: str) -> tuple[int, str]:
    """Map evaluator vocabulary to a display category without changing verdicts."""

    if verdict in FAILED:
        return 0, "F"
    if verdict in PARTIAL:
        return 1, "P"
    if verdict in SUPPORTED:
        return 2, "S"
    raise ValueError(f"unrecognized evaluator verdict: {verdict!r}")


def load_records() -> list[dict]:
    records = []
    for path in sorted(EVALUATION_ROOT.glob("SD-C*/*.yaml")):
        with path.open(encoding="utf-8") as handle:
            record = yaml.safe_load(handle)
        record["_path"] = str(path.relative_to(PAPER_ROOT))
        records.append(record)
    if len(records) != 6:
        raise RuntimeError(f"expected six Route-A records, found {len(records)}")
    return records


def main() -> None:
    records = load_records()
    values = np.zeros((len(records), len(GATES) + 1), dtype=int)
    text = np.empty(values.shape, dtype=object)

    for row, record in enumerate(records):
        for col, gate in enumerate(GATES):
            values[row, col], text[row, col] = classify(record[gate]["verdict"])
        allowed = bool(record["route_b_invocation_allowed"])
        values[row, -1] = 2 if allowed else 3
        text[row, -1] = "OPEN" if allowed else "LOCK"

    cmap = ListedColormap(
        [COLORS["light_gray"], COLORS["orange"], COLORS["blue"], COLORS["gray"]]
    )
    fig, ax = plt.subplots(figsize=(7.15, 3.15), constrained_layout=True)
    ax.imshow(values, aspect="auto", interpolation="none", cmap=cmap, vmin=-0.5, vmax=3.5)

    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            color = "white" if values[row, col] == 3 else "black"
            ax.text(col, row, text[row, col], ha="center", va="center", color=color, fontweight="bold")

    ax.set_xticks(range(len(GATE_LABELS)), GATE_LABELS)
    ax.set_yticks(range(len(records)), [r["candidate_id"] for r in records])
    ax.set_xticks(np.arange(-0.5, len(GATE_LABELS), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(records), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.tick_params(axis="x", length=0)
    ax.tick_params(axis="y", length=0)

    legend = [
        mpatches.Patch(color=COLORS["blue"], label="S: local structural support"),
        mpatches.Patch(color=COLORS["orange"], label="P: weak/partial/formal"),
        mpatches.Patch(color=COLORS["light_gray"], label="F: failed/not testable"),
        mpatches.Patch(color=COLORS["gray"], label="LOCK: Route B disabled"),
    ]
    ax.legend(handles=legend, ncol=2, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.16))
    save_figure(fig, "fig1_route_a_matrix")


if __name__ == "__main__":
    main()
