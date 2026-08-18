#!/usr/bin/env python3
"""Generate Paper 48's data-driven publication assets deterministically.

The script consumes only the frozen canonical summary.  It recomputes the
continuous critical curves from the exact digit singular-value formula and
uses frozen census fields for the validation table.  It does not infer an
infinite theorem from finite controls.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "figures" / "data" / "canonical_summary.json"
OUT_DIR = ROOT / "figures" / "generated"
TABLE_DIR = ROOT / "figures" / "tables"
DIGEST_PATH = ROOT / "figures" / "data" / "ASSET_DIGESTS.json"

EXPECTED_BINDINGS = {
    "integration_candidate_seal_sha256":
        "2726c5eac3ef0aed1e67158912b58ae1a8f98339573b683ba348bdf72171d02d",
    "state_a_tree_sha256":
        "c23b59034303af74f2a9433b92f9f5c1e1cce4510bd8032ef1214372390bda58",
    "state_b_tree_sha256":
        "3fc18f7f6122fb91d8c418a6a9da497c29253407b52db6ecad156e3a29b22a48",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def digit_singular_values(b: int) -> np.ndarray:
    j = np.arange(1, b + 1, dtype=float)
    return 1.0 / (2.0 * np.sin((2.0 * j - 1.0) * math.pi / (4.0 * b + 2.0)))


def kappa(values: np.ndarray, q: np.ndarray) -> np.ndarray:
    # Stable enough in the displayed range q in [1, 4].
    return np.sum(values[:, None] ** q[None, :], axis=0) ** (1.0 / q)


def validate_summary(summary: dict) -> None:
    bindings = summary["input_bindings"]
    for key, expected in EXPECTED_BINDINGS.items():
        actual = bindings.get(key)
        if actual != expected:
            raise ValueError(f"{key}: expected {expected}, got {actual}")

    for row in summary["theoretical_digit_data"]:
        b = int(row["b"])
        formula = digit_singular_values(b)
        frozen = np.array([float(x) for x in row["singular_values"]])
        if not np.allclose(formula, frozen, rtol=0.0, atol=5e-12):
            raise ValueError(f"digit spectrum mismatch for b={b}")
        for q_text, q_row in row["schatten_norms"].items():
            q = int(q_text)
            norm = float(np.sum(formula ** q) ** (1.0 / q))
            if abs(norm - float(q_row["kappa"])) > 5e-12:
                raise ValueError(f"kappa mismatch for b={b}, q={q}")

    finite = summary["finite_control_census"]
    hostile = summary["hostile_control_census"]
    if finite["finite_rows_per_lane"] != 1965:
        raise ValueError("unexpected finite row count")
    if finite["exact_field_mismatches"] != 0:
        raise ValueError("canonical exact-field mismatches are nonzero")
    if hostile["survivors"] != 0:
        raise ValueError("canonical hostile survivors are nonzero")
    if summary["evidence_boundary"]["finite_controls_are_proof"] is not False:
        raise ValueError("finite-proof firewall is not closed")


def generate_phase_diagram(summary: dict) -> list[Path]:
    q = np.linspace(1.0, 4.0, 361)
    colors = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"]
    styles = ["-", "--", "-.", ":"]
    markers = ["o", "s", "^", "D"]

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 8.5,
        "axes.labelsize": 9,
        "axes.linewidth": 0.7,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
    })

    fig, ax = plt.subplots(figsize=(6.65, 3.35))
    for idx, b in enumerate((2, 3, 4, 5)):
        values = digit_singular_values(b)
        log_wall = np.log(kappa(values, q)) / math.log(b)
        critical = np.maximum(1.0, log_wall)
        ax.plot(
            q,
            critical,
            color=colors[idx],
            linestyle=styles[idx],
            linewidth=1.55,
            marker=markers[idx],
            markevery=[0, 60, 120, 180, 240, 300, 360],
            markersize=3.0,
            markerfacecolor="white",
            markeredgewidth=0.8,
            label=rf"$b={b}$",
            zorder=3,
        )

    ax.axhline(
        1.0,
        color="#4D4D4D",
        linewidth=0.9,
        linestyle=(0, (4, 3)),
        label=r"universal wall $\sigma=1$",
        zorder=2,
    )
    ax.set_xlim(1.0, 4.0)
    ax.set_ylim(0.992, 1.18)
    ax.set_xlabel(r"Schatten index $q$")
    ax.set_ylabel(r"critical abscissa $\sigma_c(q)$")
    ax.set_xticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    ax.grid(axis="both", color="#D9D9D9", linewidth=0.45, alpha=0.75)
    ax.legend(loc="upper right", ncol=2, frameon=True, framealpha=0.96)
    ax.annotate(
        "trace-class points",
        xy=(1.0, 1.161),
        xytext=(1.32, 1.147),
        arrowprops={"arrowstyle": "->", "linewidth": 0.7, "color": "#333333"},
        fontsize=7.5,
        color="#333333",
    )
    fig.tight_layout(pad=0.25)

    fixed_time = datetime(2026, 8, 18, tzinfo=timezone.utc)
    pdf_path = OUT_DIR / "critical_surfaces.pdf"
    png_path = OUT_DIR / "critical_surfaces.png"
    fig.savefig(
        pdf_path,
        metadata={
            "Title": "Exact critical Schatten surfaces",
            "Author": "Anonymous",
            "Subject": "Deterministic evaluation of the exact digit formula",
            "Keywords": "carry-free radix operator, Schatten threshold",
            "Creator": "generate_paper_assets.py",
            "Producer": "Matplotlib",
            "CreationDate": fixed_time,
            "ModDate": fixed_time,
        },
    )
    fig.savefig(
        png_path,
        dpi=240,
        metadata={
            "Title": "Exact critical Schatten surfaces",
            "Software": "generate_paper_assets.py",
            "Creation Time": "2026-08-18T00:00:00Z",
        },
    )
    plt.close(fig)
    return [pdf_path, png_path]


def generate_threshold_table(summary: dict) -> Path:
    lines = [
        "% Generated by scripts/generate_paper_assets.py; do not edit by hand.",
        r"\begin{tabular}{@{}rrrrrr@{}}",
        r"\toprule",
        r"$b$ & $\tau_b$ & $\alpha_b$ & $\kappa_{b,2}$"
        r" & $\log_b\kappa_{b,2}$ & $\sigma_c(q{=}2)$ \\",
        r"\midrule",
    ]
    for row in summary["theoretical_digit_data"]:
        b = int(row["b"])
        q2 = row["schatten_norms"]["2"]
        lines.append(
            f"{b} & {float(row['tau_b']):.6f} & "
            f"{float(row['alpha_b']):.6f} & "
            f"{float(q2['kappa']):.6f} & "
            f"{float(q2['log_b_kappa']):.6f} & "
            f"{float(q2['critical_sigma']):.6f} " + r"\\"
        )
    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    path = TABLE_DIR / "thresholds.tex"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def generate_validation_table(summary: dict) -> Path:
    finite = summary["finite_control_census"]
    hostile = summary["hostile_control_census"]
    rows = [
        ("Finite rows", f"{finite['finite_rows_per_lane']:,} per lane",
         "two independently constructed lanes"),
        ("Digit intervals", f"{finite['digit_interval_comparisons']:,}",
         "overlapping enclosures"),
        ("Shell envelopes", f"{finite['shell_envelope_rows']:,}",
         "direct values inside exact bounds"),
        ("Exact-field discrepancies", f"{finite['exact_field_mismatches']}",
         "finite consistency check"),
        ("Atomic mutations", f"{hostile['mutation_instances']}",
         f"{hostile['designated_rejections']} designated rejections"),
        ("Nondesignated acceptances", f"{hostile['nondesignated_acceptances']}",
         "expected consumer isolation"),
        ("Physical/adversarial cases", f"{hostile['physical_instances']}",
         "normal and hostile replay inputs"),
        ("Survivors", f"{hostile['survivors']}",
         "no detected hostile survivor"),
    ]
    lines = [
        "% Generated by scripts/generate_paper_assets.py; do not edit by hand.",
        r"\begin{tabular}{@{}lrl@{}}",
        r"\toprule",
        r"Finite/audit item & Count & Interpretation \\",
        r"\midrule",
    ]
    for label, count, interpretation in rows:
        lines.append(f"{label} & {count} & {interpretation} " + r"\\")
    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    path = TABLE_DIR / "validation_census.tex"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    validate_summary(summary)

    outputs = []
    outputs.extend(generate_phase_diagram(summary))
    outputs.append(generate_threshold_table(summary))
    outputs.append(generate_validation_table(summary))

    digest_record = {
        "generator": "scripts/generate_paper_assets.py",
        "source_date_epoch": 1787011200,
        "input": {
            str(SUMMARY_PATH.relative_to(ROOT)): sha256(SUMMARY_PATH),
        },
        "outputs": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in sorted(outputs)
        },
        "evidence_ceiling": (
            "Plots and tables evaluate exact formulas or report frozen finite "
            "controls; finite controls are not proofs of infinite claims."
        ),
    }
    DIGEST_PATH.write_text(
        json.dumps(digest_record, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(digest_record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
