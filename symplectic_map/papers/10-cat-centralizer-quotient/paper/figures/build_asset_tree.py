#!/usr/bin/env python3
"""Frame and hash the Paper 10 asset tree without touching frozen evidence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from figure_data import EXPECTED_HASHES, PAPER_ROOT, sha256_file


HERE = Path(__file__).resolve().parent
ASSET_RELATIVE_PATHS = (
    "PAPER_PLAN.md",
    "notes/CITATION_VERIFICATION.md",
    "paper/references.bib",
    "paper/figures/figure_data.py",
    "paper/figures/paper_plot_style.py",
    "paper/figures/gen_fig1_quotient_layers.py",
    "paper/figures/gen_fig2_nine_modulus_ledger.py",
    "paper/figures/gen_fig3_clock_semantics.py",
    "paper/figures/generate_all.py",
    "paper/figures/build_figure_manifest.py",
    "paper/figures/build_asset_tree.py",
    "paper/figures/latex_includes.tex",
    "paper/figures/PROVENANCE.md",
    "paper/figures/FIGURE_QA.md",
    "paper/figures/FIGURE_TRACE.json",
    "paper/figures/DETERMINISM_AUDIT.json",
    "paper/figures/fig1_quotient_layers.pdf",
    "paper/figures/fig1_quotient_layers.svg",
    "paper/figures/fig1_quotient_layers.png",
    "paper/figures/fig2_nine_modulus_ledger.pdf",
    "paper/figures/fig2_nine_modulus_ledger.svg",
    "paper/figures/fig2_nine_modulus_ledger.png",
    "paper/figures/fig3_clock_semantics.pdf",
    "paper/figures/fig3_clock_semantics.svg",
    "paper/figures/fig3_clock_semantics.png",
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
        "schema": "paper10.asset_tree.v1",
        "generated_utc": "2026-08-15T00:00:00Z",
        "status": "PASS",
        "frame": {
            "asset_root": "papers/10-cat-centralizer-quotient",
            "included_asset_count": len(assets),
            "exactly_three_figure_stems": [
                "fig1_quotient_layers",
                "fig2_nine_modulus_ledger",
                "fig3_clock_semantics",
            ],
            "excluded_by_design": [
                "paper/manuscript.tex",
                "paper/figures/FIGURE_MANIFEST.json (hashes this tree)",
                "paper/figures/ASSET_TREE.json (self)",
                "notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md (post-freeze review)",
                "all code/, experiments/, results/, and frozen source/proof files",
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
    manifest = write_asset_tree()
    print(
        f"Paper 10 asset tree: {manifest['status']} "
        f"({manifest['frame']['included_asset_count']} files)"
    )
