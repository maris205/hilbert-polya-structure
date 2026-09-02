#!/usr/bin/env python3
"""Build exact-draft Stage-2.5 claim artifacts for Round-10 Papers 29--33.

This is a thin configuration wrapper around the already validated Round-9
mechanical builder. It changes only the paper population, identifiers,
selection salt, and provenance label. Manuscripts and bibliographies remain
read-only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "tools" / "round9_stage2_5_build_claim_artifacts.py"


def load_base():
    spec = importlib.util.spec_from_file_location("round10_stage2_5_claim_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {BASE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PAPERS = {
    "29-bianchi-ideal-owner-refinement": {
        "prefix": "P29",
        "headline_markers": ["Gate M", "Gate Q", "S_H"],
    },
    "30-three-disk-nonconstant-roof-determinant": {
        "prefix": "P30",
        "headline_markers": ["Gate 4", "Gate 5", "Gate 6"],
    },
    "31-level11-conjugacy-owner-ledger": {
        "prefix": "P31",
        "headline_markers": ["canonicalization biconditional", "9,453"],
    },
    "32-homology-cover-renormalization-uniformity": {
        "prefix": "P32",
        "headline_markers": ["higher-content", "zero-content", "content one"],
    },
    "33-bolza-control-matched-census": {
        "prefix": "P33",
        "headline_markers": ["P33-RC-1", "common semantic owner-certificate schema"],
    },
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", choices=["all", *PAPERS], default="all")
    args = parser.parse_args()

    base = load_base()
    base.PAPERS = PAPERS
    base.SELECTION_SALT = "round10-stage2.5"
    base.DETECTOR_ID = "ars-codex-academic-pipeline-stage2.5-first-pass-round10"
    evidence_rows = base.load_module(base.EVIDENCE_ROWS_MODULE, "round10_ars_evidence_rows")
    selected = PAPERS if args.paper == "all" else {args.paper: PAPERS[args.paper]}
    summary = [
        base.build_one(paper, config, evidence_rows)
        for paper, config in selected.items()
    ]
    print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
