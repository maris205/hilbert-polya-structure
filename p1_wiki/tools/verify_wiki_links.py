#!/usr/bin/env python3
"""Verify local Markdown link destinations in the P1 Wiki.

The reader corpus deliberately links back to original source packages outside
``p1_wiki``.  This checker therefore verifies any local relative destination
against the repository filesystem, while leaving HTTP(S), mailto, data, and
fragment-only links alone.  It does not attempt to judge external URLs or
whether a rendered Markdown heading has a particular GitHub anchor slug.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


WIKI_ROOT = Path(__file__).resolve().parents[1]
INLINE_LINK = re.compile(r"\[[^\]]*\]\((?P<target><[^>]+>|[^)\s]+(?:\s+['\"][^)]*['\"])?)(?:\s+['\"][^)]*['\"])?\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(?P<target><[^>]+>|\S+)")
REMOTE_OR_SCHEME = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.IGNORECASE)


def unfenced_text(path: Path) -> str:
    """Return Markdown text excluding fenced code blocks.

    A literal URL-shaped string in a fenced example is not an active Markdown
    link, so excluding it avoids false failures in source-transcription pages.
    """

    lines: list[str] = []
    delimiter: str | None = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.lstrip()
        if delimiter is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            delimiter = stripped[:3]
            continue
        if delimiter is not None:
            if stripped.startswith(delimiter):
                delimiter = None
            continue
        lines.append(line)
    text = "\n".join(lines)
    # Pandoc's LaTeX reader writes display and inline math in Markdown math
    # delimiters.  Constructions such as ``[x^d](1-x^m)`` inside a formula
    # are coefficients, not Markdown links.
    text = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", "", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\\\[.*?(?<!\\)\\\]", "", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\$(?!\$)(?:\\.|[^$\n])*(?<!\\)\$", "", text)
    return text


def normalise_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    else:
        # An optional Markdown title follows whitespace.  This corpus uses
        # angle brackets for paths that may contain spaces, so this split is
        # safe for the non-angle form.
        raw = raw.split(maxsplit=1)[0]
    return unquote(raw.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0])


def candidates(text: str) -> list[str]:
    found = [match.group("target") for match in INLINE_LINK.finditer(text)]
    found.extend(match.group("target") for match in REFERENCE_LINK.finditer(text))
    return found


def main() -> int:
    files = sorted(WIKI_ROOT.rglob("*.md"))
    checked = 0
    failures: list[tuple[Path, str, Path]] = []
    for source in files:
        for raw in candidates(unfenced_text(source)):
            target = normalise_target(raw)
            if not target or target.startswith("#") or REMOTE_OR_SCHEME.match(target):
                continue
            destination = (source.parent / target).resolve()
            checked += 1
            if not destination.exists():
                failures.append((source, raw, destination))

    if failures:
        for source, raw, destination in failures:
            print(f"BROKEN: {source.relative_to(WIKI_ROOT)} -> {raw!r} ({destination})")
        print(f"P1 wiki link check: FAIL ({len(failures)} broken of {checked} local links in {len(files)} files)")
        return 1
    print(f"P1 wiki link check: PASS ({checked} local links in {len(files)} Markdown files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
