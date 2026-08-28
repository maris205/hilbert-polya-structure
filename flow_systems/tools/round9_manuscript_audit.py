#!/usr/bin/env python3
"""Deterministic structural audit for the five Round-9 manuscript packages.

The audit is deliberately narrower than scientific peer review.  It checks the
frozen package anatomy, citation-key closure, the requested plainnat numerical
style, author/declaration surfaces, PDF readability, and claim-boundary guard
strings.  It never upgrades a theorem, a numerical certificate, or a Route-A
verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


PAPERS = (
    "24-bianchi-holonomy-flow",
    "25-three-disk-scattering-flow",
    "26-level11-newform-time-change",
    "27-congruence-inverse-limit-no-go",
    "28-bolza-magnetic-flow",
)

CITE_RE = re.compile(
    r"\\cite(?:alp|alt|author|year|yearpar|num|p|t)?\*?"
    r"\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}",
    re.MULTILINE,
)
BIB_RE = re.compile(r"@(?:article|book|incollection|inproceedings|misc|phdthesis|techreport)"
                    r"\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
WORD_RE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")


@dataclass
class PaperAudit:
    paper: str
    passed: bool
    errors: list[str]
    warnings: list[str]
    tex_sha256: str | None
    bib_sha256: str | None
    pdf_sha256: str | None
    body_word_count: int
    citation_key_count: int
    bibliography_entry_count: int
    pdf_pages: int | None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def strip_comments(tex: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in tex.splitlines())


def body_word_count(tex: str) -> int:
    text = strip_comments(tex)
    begin = re.search(r"\\section\*?\{Introduction[^}]*\}", text, re.IGNORECASE)
    if begin:
        text = text[begin.start():]
    bibliography = re.search(r"\\bibliography\s*\{", text, re.IGNORECASE)
    if bibliography:
        text = text[:bibliography.start()]
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"\$[^$]*\$", " ", text)
    text = re.sub(r"\\\([^)]*\\\)|\\\[[^]]*\\\]", " ", text, flags=re.DOTALL)
    return len(WORD_RE.findall(text))


def pdf_page_count(path: Path) -> tuple[int | None, str | None]:
    try:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        return None, f"pdfinfo failed: {exc}"
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if not match:
        return None, "pdfinfo did not report a page count"
    return int(match.group(1)), None


def require_any(tex: str, label: str, patterns: tuple[str, ...], errors: list[str]) -> None:
    if not any(re.search(pattern, tex, re.IGNORECASE | re.DOTALL) for pattern in patterns):
        errors.append(f"missing required surface: {label}")


def audit_paper(root: Path, paper: str) -> PaperAudit:
    paper_dir = root / "papers" / paper / "paper"
    tex_path = paper_dir / "manuscript.tex"
    bib_path = paper_dir / "references.bib"
    pdf_path = paper_dir / "paper.pdf"
    report_path = paper_dir / "stage2_manuscript_audit.md"
    errors: list[str] = []
    warnings: list[str] = []

    for required in (tex_path, bib_path, pdf_path, report_path):
        if not required.is_file():
            errors.append(f"missing file: {required.relative_to(root)}")

    if not tex_path.is_file() or not bib_path.is_file():
        return PaperAudit(
            paper=paper,
            passed=False,
            errors=errors,
            warnings=warnings,
            tex_sha256=sha256(tex_path) if tex_path.is_file() else None,
            bib_sha256=sha256(bib_path) if bib_path.is_file() else None,
            pdf_sha256=sha256(pdf_path) if pdf_path.is_file() else None,
            body_word_count=0,
            citation_key_count=0,
            bibliography_entry_count=0,
            pdf_pages=None,
        )

    tex = tex_path.read_text(encoding="utf-8")
    bib = bib_path.read_text(encoding="utf-8")
    tex_no_comments = strip_comments(tex)

    required_surfaces = {
        "English abstract": (r"\\begin\{abstract\}",),
        "Traditional-Chinese abstract": (r"Chinese Abstract", r"中文摘要", r"繁體中文摘要"),
        "keywords": (r"Keywords", r"關鍵詞", r"關鍵字"),
        "introduction": (r"\\section\*?\{Introduction",),
        "background or related work": (
            r"\\section\*?\{[^}]*(?:Background|Related|Prior[ -]Work|Prior work)",
        ),
        "theorem statement": (r"\\begin\{theorem\}", r"\\begin\{proposition\}"),
        "proof": (r"\\begin\{proof\}",),
        "computational/certificate method": (
            r"\\section\*?\{[^}]*(?:Comput|Certificate|Reproducibility|Exact Enumeration)",
        ),
        "Route-A interpretation": (r"Route[-~ ]A",),
        "limitations": (r"\\section\*?\{[^}]*Limitations",),
        "conclusion": (r"\\section\*?\{Conclusion",),
        "data/code availability": (r"Data (?:and|\&) Code Availability", r"Data Availability"),
        "ethics declaration": (r"Ethics Declaration", r"Ethics Statement"),
        "author contributions": (r"Author Contributions", r"CRediT"),
        "conflict of interest": (r"Conflict of Interest", r"Competing Interests"),
        "funding": (r"Funding",),
        "AI disclosure": (r"AI[- ]Assisted Research Disclosure", r"AI Disclosure"),
    }
    for label, patterns in required_surfaces.items():
        require_any(tex_no_comments, label, patterns, errors)

    for literal, label in (
        ("Liang Wang", "author name"),
        ("wangliang.f@gmail.com", "contact email"),
        ("Huazhong University of Science and Technology", "affiliation"),
    ):
        if literal not in tex:
            errors.append(f"missing {label}: {literal}")

    if not re.search(r"\\usepackage(?:\[[^]]*\])?\{natbib\}", tex):
        errors.append("natbib is not loaded")
    if not re.search(r"\\bibliographystyle\{plainnat\}", tex):
        errors.append("bibliography style is not plainnat")
    if not re.search(r"\\bibliography\{references\}", tex):
        errors.append("bibliography does not point to references.bib")

    cited_keys = {
        key.strip()
        for match in CITE_RE.finditer(tex_no_comments)
        for key in match.group(1).split(",")
        if key.strip() and key.strip() != "*"
    }
    bib_keys = {match.group(1).strip() for match in BIB_RE.finditer(bib)}
    missing_bib = sorted(cited_keys - bib_keys)
    orphan_bib = sorted(bib_keys - cited_keys)
    if missing_bib:
        errors.append("citation keys missing from bibliography: " + ", ".join(missing_bib))
    if orphan_bib:
        errors.append("orphan bibliography entries: " + ", ".join(orphan_bib))
    if len(cited_keys) < 4:
        warnings.append(f"small cited-source set: {len(cited_keys)} keys")

    words = body_word_count(tex)
    if words < 3500:
        errors.append(f"body word count below manuscript floor: {words} < 3500")
    if words > 8000:
        warnings.append(f"body word count exceeds preferred ceiling: {words} > 8000")

    lowered = tex.lower()
    forbidden = (
        "hilbert_polya_realization",
        "hilbert--pólya realization is established",
        "route b is ready",
        "route-b ready",
        "route_b_invocation_allowed: true",
    )
    for phrase in forbidden:
        if phrase in lowered:
            errors.append(f"forbidden Route-B promotion phrase: {phrase}")

    pages: int | None = None
    if pdf_path.is_file():
        if pdf_path.stat().st_size < 1024 or not pdf_path.read_bytes().startswith(b"%PDF"):
            errors.append("paper.pdf is missing a valid PDF header or is too small")
        else:
            pages, pdf_error = pdf_page_count(pdf_path)
            if pdf_error:
                errors.append(pdf_error)
            elif pages is not None and pages < 8:
                warnings.append(f"short compiled manuscript: {pages} pages")

    return PaperAudit(
        paper=paper,
        passed=not errors,
        errors=errors,
        warnings=warnings,
        tex_sha256=sha256(tex_path),
        bib_sha256=sha256(bib_path),
        pdf_sha256=sha256(pdf_path) if pdf_path.is_file() else None,
        body_word_count=words,
        citation_key_count=len(cited_keys),
        bibliography_entry_count=len(bib_keys),
        pdf_pages=pages,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    audits = [audit_paper(root, paper) for paper in PAPERS]
    payload = {
        "schema": "flow-systems-round9-manuscript-audit/1.0",
        "root": str(root),
        "passed": all(audit.passed for audit in audits),
        "papers": [asdict(audit) for audit in audits],
    }
    print(json.dumps(payload, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
