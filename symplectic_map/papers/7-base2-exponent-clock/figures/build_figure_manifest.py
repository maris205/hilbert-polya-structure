"""Build the deterministic Paper 7 figure manifest and provenance note."""

from __future__ import annotations

import json
import platform
from pathlib import Path

import matplotlib
import paper_plot_style as _paper_plot_style  # noqa: F401  (applies frozen rcParams)

from figure_contract import (
    EXPECTED_SOURCE_LOCK_SHA256,
    PAPER_ROOT,
    load_frozen_inputs,
    load_json,
    require,
    sha256_file,
)


FIG_DIR = Path(__file__).resolve().parent
INPUTS = [
    "PAPER_PLAN.md",
    "experiments/source_lock.json",
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md",
    "experiments/OFFICIAL_VALIDATION_REPORT.md",
    "notes/PROOF_PACKAGE.md",
    "results/PRE_EXECUTION_AUDIT.json",
    "results/EXPERIMENT_RESULTS.json",
    "results/result_manifest.json",
    "notes/INDEPENDENT_RESULT_INTEGRITY.md",
    "notes/CITATION_VERIFICATION.md",
    "notes/CITATION_PLAN_AUDIT.md",
    "paper/references.bib",
]
ARTIFACTS = [
    "README.md",
    "paper_plot_style.py",
    "figure_contract.py",
    "gen_fig1_boundary_map.py",
    "gen_fig2_registered_ledger.py",
    "gen_fig3_frobenius_filter.py",
    "verify_figure_determinism.py",
    "build_figure_manifest.py",
    "latex_includes.tex",
    "FIGURE_QA.md",
    "DETERMINISM_AUDIT.json",
    "fig1_boundary_map.pdf",
    "fig1_boundary_map.svg",
    "fig1_boundary_map.png",
    "fig2_registered_ledger.pdf",
    "fig2_registered_ledger.svg",
    "fig2_registered_ledger.png",
    "fig3_frobenius_filter.pdf",
    "fig3_frobenius_filter.svg",
    "fig3_frobenius_filter.png",
]


def record(path: Path, label: str) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"expected regular nonsymlink file: {path}")
    return {"path": label, "bytes": path.stat().st_size, "sha256": sha256_file(path)}


def main() -> None:
    source, result = load_frozen_inputs()
    determinism = load_json(FIG_DIR / "DETERMINISM_AUDIT.json")
    require(determinism.get("pass") is True, "figure determinism audit failed")
    require(
        determinism.get("byte_identical_outputs") is True,
        "figure outputs were not byte-identical on regeneration",
    )
    input_records = [record(PAPER_ROOT / rel, rel) for rel in INPUTS]
    artifact_records = [record(FIG_DIR / rel, f"figures/{rel}") for rel in ARTIFACTS]
    manifest = {
        "schema": "BASE2_FIGURE_MANIFEST_V1",
        "candidate_id": source["candidate_id"],
        "source_lock_sha256": EXPECTED_SOURCE_LOCK_SHA256,
        "registered_result_sha256": sha256_file(PAPER_ROOT / "results/EXPERIMENT_RESULTS.json"),
        "result_classification": result["classification"],
        "all_period_equality_status": result["all_period_equality_status"],
        "inputs": input_records,
        "artifacts": artifact_records,
        "renderer": {
            "python": platform.python_version(),
            "matplotlib": matplotlib.__version__,
            "backend": matplotlib.get_backend(),
            "pdf_fonttype": matplotlib.rcParams["pdf.fonttype"],
            "svg_fonttype": matplotlib.rcParams["svg.fonttype"],
        },
        "determinism": {
            "audit_path": "figures/DETERMINISM_AUDIT.json",
            "audit_sha256": sha256_file(FIG_DIR / "DETERMINISM_AUDIT.json"),
            "regeneration_count": determinism["regeneration_count"],
            "byte_identical_outputs": determinism["byte_identical_outputs"],
        },
        "forbidden_sources_used": [],
        "pass": True,
    }
    manifest_path = FIG_DIR / "figure_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    manifest_sha = sha256_file(manifest_path)

    lines = [
        "# Figure Provenance",
        "",
        "Status: `PASS`",
        "",
        f"Candidate: `{source['candidate_id']}`",
        "",
        f"Figure manifest SHA-256: `{manifest_sha}`",
        "",
        "The package is bound to the frozen source lock and the sole registered",
        "exact-symbolic result.  Every plot value, target decision, theorem status,",
        "irreducible-polynomial row, and control outcome is read from the listed",
        "inputs.  No network resource, external prime table, Riemann-zero data,",
        "numerical orbit match, or post-null period was used.",
        "",
        "## Input bindings",
        "",
        "| Path | Bytes | SHA-256 |",
        "|---|---:|---|",
    ]
    lines.extend(
        f"| `{item['path']}` | {item['bytes']} | `{item['sha256']}` |"
        for item in input_records
    )
    lines.extend(
        [
            "",
            "## Figure package",
            "",
            "| Path | Bytes | SHA-256 |",
            "|---|---:|---|",
        ]
    )
    lines.extend(
        f"| `{item['path']}` | {item['bytes']} | `{item['sha256']}` |"
        for item in artifact_records
    )
    lines.extend(
        [
            "",
            "## Determinism and rendering checks",
            "",
            f"- Regeneration count: `{determinism['regeneration_count']}`.",
            f"- Byte-identical PDF/SVG/PNG outputs: `{str(determinism['byte_identical_outputs']).lower()}`.",
            f"- Python: `{platform.python_version()}`; Matplotlib: `{matplotlib.__version__}`.",
            "- PDF and SVG are vector masters; PNG files are 300 dpi review previews.",
            "- Embedded-font, vector-content, SVG-parse, DPI, and visual checks are",
            "  recorded in `figures/FIGURE_QA.md`; the hashes above bind that audit",
            "  and the inspected files.",
            "",
            "## Evidence boundary",
            "",
            f"- Finite registered label: `{result['classification']}`.",
            f"- All-period rational equality: `{result['all_period_equality_status']}`.",
            "- Figure 2 is a development-seen reproduction ledger, not theorem evidence.",
            "- The degree-four witness in Figure 3 passes a necessary coefficient filter",
            "  only; it is not an equality cycle and does not prove sufficiency.",
            "",
        ]
    )
    (FIG_DIR / "FIGURE_PROVENANCE.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
