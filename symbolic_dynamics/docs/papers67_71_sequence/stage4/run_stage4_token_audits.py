#!/usr/bin/env python3
"""Persist canonical advisory token-conservation reports for Stage 4."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.27/"
    "skills/academic-research-suite/ars"
)
PAPERS = (
    "67-multiplicative-plaquette-matroid-complexity",
    "68-complete-bipartite-homshift-conjugacies",
    "69-orientation-sensitive-surface-flat-sft",
    "70-weighted-heisenberg-congruence-nullities",
    "71-zip-shift-degree-pressure",
)


def main() -> None:
    checker = ARS / "scripts" / "check_revision_token_conservation.py"
    for slug in PAPERS:
        paper = ROOT / "papers" / slug
        command = [
            "python",
            str(checker),
            "patch",
            "--patch",
            str(paper / "stage4" / "REVISION_PATCH.json"),
            "--base",
            str(paper / "stage3" / "ANCHORED_REVIEW_DRAFT.md"),
        ]
        result = subprocess.run(command, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(
                f"{slug}: token audit failed with exit {result.returncode}: {result.stderr}"
            )
        out = paper / "stage4" / "TOKEN_CONSERVATION.json"
        out.write_text(result.stdout, encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
