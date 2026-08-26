#!/usr/bin/env python3
"""Prepare a citation-preserving Markdown audit view from ordered LaTeX sections.

This is a derived integrity artifact only.  It replaces natbib commands by
Pandoc citation markers before Pandoc converts the surrounding LaTeX.  The
canonical paper source and PDF are never modified.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CITE_RE = re.compile(r"\\cite(?:t|p)?\{([^}]*)\}", re.DOTALL)


def replace_citation(match: re.Match[str]) -> str:
    keys = [key.strip() for key in match.group(1).split(",") if key.strip()]
    return "[" + "; ".join(f"@{key}" for key in keys) + "]"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: prepare_claim_draft.py SECTION.tex [...]", file=sys.stderr)
        return 2
    chunks: list[str] = []
    for raw_path in sys.argv[1:]:
        chunks.append(Path(raw_path).read_text(encoding="utf-8"))
    source = "\n\n".join(chunks)
    sys.stdout.write(CITE_RE.sub(replace_citation, source))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
