#!/usr/bin/env python3
"""Build the five Round-10 Stage-2 PDFs in isolation and publish atomically."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-09-02T13:29:43Z"
PAPERS = {
    "P29": "29-bianchi-ideal-owner-refinement",
    "P30": "30-three-disk-nonconstant-roof-determinant",
    "P31": "31-level11-conjugacy-owner-ledger",
    "P32": "32-homology-cover-renormalization-uniformity",
    "P33": "33-bolza-control-matched-census",
}
CHAIN = (
    ("lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=paper", "manuscript.tex"),
    ("bibtex", "paper"),
    ("lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=paper", "manuscript.tex"),
    ("lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=paper", "manuscript.tex"),
)
FATAL_PATTERNS = (
    "undefined citations",
    "citation `",
    "undefined references",
    "reference `",
    "missing character:",
    "overfull \\hbox",
    "there were undefined",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: tuple[str, ...], cwd: Path) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        tail = "\n".join(result.stdout.splitlines()[-120:])
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(command)}\n{tail}")
    return result.stdout


def pdf_pages(path: Path) -> int:
    result = subprocess.run(("pdfinfo", str(path)), text=True, stdout=subprocess.PIPE, check=True)
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"pdfinfo did not report pages for {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--paper",
        default="all",
        help="comma-separated P29--P33 selection; default: all",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    requested = set(PAPERS) if args.paper == "all" else {value.strip().upper() for value in args.paper.split(",") if value.strip()}
    unknown = requested - set(PAPERS)
    if unknown:
        raise SystemExit(f"unknown paper(s): {', '.join(sorted(unknown))}")
    selected = {code: slug for code, slug in PAPERS.items() if code in requested}
    staged: dict[str, dict[str, object]] = {}
    with tempfile.TemporaryDirectory(prefix="round10-stage2-build-") as tmp_name:
        tmp_root = Path(tmp_name)
        for code, slug in selected.items():
            source = ROOT / "papers" / slug / "paper"
            work = tmp_root / code
            work.mkdir()
            for name in ("manuscript.tex", "references.bib"):
                shutil.copy2(source / name, work / name)
            outputs: list[str] = []
            for command in CHAIN:
                outputs.append(run(command, work))
            # Undefined citations are expected in the first LaTeX pass before
            # BibTeX.  Publication safety is decided from the final engine
            # output and final log, after the complete four-command chain.
            final_log = (work / "paper.log").read_text(encoding="utf-8", errors="replace")
            low = (outputs[-1] + "\n" + final_log).lower()
            fatals = sorted({pattern for pattern in FATAL_PATTERNS if pattern in low})
            if fatals:
                raise RuntimeError(f"{code}: fatal log patterns: {', '.join(fatals)}")
            pdf = work / "paper.pdf"
            if not pdf.read_bytes().startswith(b"%PDF-"):
                raise RuntimeError(f"{code}: invalid PDF header")
            text_path = work / "paper.txt"
            subprocess.run(("pdftotext", str(pdf), str(text_path)), check=True)
            staged[code] = {
                "slug": slug,
                "work_pdf": pdf,
                "manuscript_sha256": sha(source / "manuscript.tex"),
                "bibliography_sha256": sha(source / "references.bib"),
                "pdf_sha256": sha(pdf),
                "pdf_text_sha256": sha(text_path),
                "pdf_pages": pdf_pages(pdf),
                "pdf_bytes": pdf.stat().st_size,
                "underfull_box_warnings": low.count("underfull \\hbox") + low.count("underfull \\vbox"),
                "log_scan": {
                    "fatal_error": 0,
                    "undefined_citation": 0,
                    "undefined_reference": 0,
                    "missing_glyph": 0,
                    "overfull_box": 0,
                },
            }

        for code, row in staged.items():
            paper = ROOT / "papers" / str(row["slug"])
            target_pdf = paper / "paper" / "paper.pdf"
            shutil.copy2(Path(row["work_pdf"]), target_pdf)
            receipt = {
                "schema": "round10-stage2-build-receipt/1.0",
                "paper": code,
                "built_at": STAMP,
                "build_isolation": "temporary-directory; canonical PDF published only after every selected build passed",
                "engine_chain": [" ".join(command) for command in CHAIN],
                "manuscript_sha256": row["manuscript_sha256"],
                "bibliography_sha256": row["bibliography_sha256"],
                "pdf_sha256": row["pdf_sha256"],
                "pdf_text_sha256": row["pdf_text_sha256"],
                "pdf_pages": row["pdf_pages"],
                "pdf_bytes": row["pdf_bytes"],
                "underfull_box_warnings": row["underfull_box_warnings"],
                "log_scan": row["log_scan"],
                "verdict": "PASS",
            }
            receipt_path = paper / "notes" / "stage2_build_receipt.json"
            receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
            print(
                f"{code} PASS pages={row['pdf_pages']} bytes={row['pdf_bytes']} "
                f"pdf_sha256={row['pdf_sha256']}"
            )


if __name__ == "__main__":
    main()
