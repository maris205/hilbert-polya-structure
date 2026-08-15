#!/usr/bin/env python3
"""Frame and hash the Paper 11 publication-asset tree."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from figure_data import EXPECTED_HASHES, PAPER_ROOT, sha256_file


HERE = Path(__file__).resolve().parent
FIGURE_STEMS = (
    "fig1_retention_hierarchy",
    "fig2_nine_row_retention",
    "fig3_effectivity_counterexamples",
)
ASSET_RELATIVE_PATHS = (
    "PAPER_PLAN.md",
    "paper/CITATION_VERIFICATION.md",
    "paper/references.bib",
    "paper/figures/figure_data.py",
    "paper/figures/paper_plot_style.py",
    "paper/figures/gen_fig1_retention_hierarchy.py",
    "paper/figures/gen_fig2_nine_row_retention.py",
    "paper/figures/gen_fig3_effectivity_counterexamples.py",
    "paper/figures/generate_all.py",
    "paper/figures/build_figure_manifest.py",
    "paper/figures/build_asset_tree.py",
    "paper/figures/latex_includes.tex",
    "paper/figures/PROVENANCE.md",
    "paper/figures/FIGURE_QA.md",
    "paper/figures/FIGURE_TRACE.json",
    "paper/figures/DETERMINISM_AUDIT.json",
    "paper/figures/fig1_retention_hierarchy.pdf",
    "paper/figures/fig1_retention_hierarchy.svg",
    "paper/figures/fig1_retention_hierarchy.png",
    "paper/figures/fig2_nine_row_retention.pdf",
    "paper/figures/fig2_nine_row_retention.svg",
    "paper/figures/fig2_nine_row_retention.png",
    "paper/figures/fig3_effectivity_counterexamples.pdf",
    "paper/figures/fig3_effectivity_counterexamples.svg",
    "paper/figures/fig3_effectivity_counterexamples.png",
)


def write_asset_tree(output_path: Path = HERE / "ASSET_TREE.json") -> dict[str, Any]:
    assets: dict[str, Any] = {}
    for relative in ASSET_RELATIVE_PATHS:
        path = PAPER_ROOT / relative
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"asset is absent, non-regular, or symlinked: {relative}")
        assets[relative] = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }

    tree = {
        "schema": "paper11.asset_tree.v1",
        "generated_utc": "2026-08-15T00:00:00Z",
        "status": "PASS",
        "frame": {
            "asset_root": "papers/11-cat-equivariant-clock",
            "included_asset_count": len(assets),
            "exactly_three_figure_stems": list(FIGURE_STEMS),
            "publication_layer_only": True,
            "excluded_by_design": [
                "paper/manuscript.tex",
                "paper/math_commands.tex",
                "paper/figures/FIGURE_MANIFEST.json (hashes this tree)",
                "paper/figures/ASSET_TREE.json (self)",
                "notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md (post-freeze review)",
                "notes/INDEPENDENT_PLAN_FIGURE_REVIEW_R2.md (if needed)",
                "all code/, postrun_analyzer/, experiments/, results/, and frozen notes",
            ],
        },
        "external_frozen_evidence": dict(sorted(EXPECTED_HASHES.items())),
        "assets": assets,
    }
    output_path.write_text(
        json.dumps(tree, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return tree


if __name__ == "__main__":
    result = write_asset_tree()
    print(
        f"Paper 11 asset tree: {result['status']} "
        f"({result['frame']['included_asset_count']} files)"
    )
