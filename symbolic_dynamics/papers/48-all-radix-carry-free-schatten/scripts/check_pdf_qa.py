#!/usr/bin/env python3
"""Run deterministic writer-side QA on the final Paper 48 PDF.

This checker operates on the PDF bytes themselves.  In particular, text is
tested exactly as emitted by Poppler and PyMuPDF; no extraction output is
sanitized before the Unicode and XML checks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import fitz


EXPECTED_PDF = "5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573"
WITHDRAWN_PDF = "daaf6435625c6f1206f3e1faaec090619f2bc2750be5e1b4ca2cf748c0063867"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv: list[str]) -> str:
    return subprocess.run(argv, check=True, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def bad_unicode(text: str) -> dict[str, int]:
    return {
        "illegal_c0": sum(ord(c) < 32 and c not in "\t\n\r" for c in text),
        "del": text.count("\x7f"),
        "c1": sum(0x80 <= ord(c) <= 0x9F for c in text),
        "replacement": text.count("\ufffd"),
        "private_use": sum(
            0xE000 <= ord(c) <= 0xF8FF
            or 0xF0000 <= ord(c) <= 0xFFFFD
            or 0x100000 <= ord(c) <= 0x10FFFD
            for c in text
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--aux", type=Path, required=True)
    parser.add_argument("--bbl", type=Path, required=True)
    parser.add_argument("--lane-a", type=Path, required=True)
    parser.add_argument("--lane-b", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    pdf = args.pdf.resolve(strict=True)
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    digest = sha(pdf)
    if digest != EXPECTED_PDF or digest == WITHDRAWN_PDF:
        raise ValueError(f"final PDF digest: {digest}")
    lane_hashes = [sha(args.lane_a), sha(args.lane_b)]
    if lane_hashes != [digest, digest]:
        raise ValueError(f"fixed-epoch lane mismatch: {lane_hashes}")

    extraction: dict[str, dict[str, int]] = {}
    for mode, option in (("default", None), ("layout", "-layout"),
                         ("raw", "-raw")):
        target = out / f"poppler_{mode}.txt"
        argv = ["pdftotext", "-enc", "UTF-8", "-nopgbrk"]
        if option:
            argv.append(option)
        argv.extend([str(pdf), str(target)])
        subprocess.run(argv, check=True)
        text = target.read_text("utf-8")
        extraction[f"poppler_{mode}"] = bad_unicode(text)

    bbox = out / "poppler_raw_bbox.xhtml"
    subprocess.run(["pdftotext", "-enc", "UTF-8", "-nopgbrk", "-raw",
                    "-bbox", str(pdf), str(bbox)], check=True)
    bbox_text = bbox.read_text("utf-8")
    bbox_bad = bad_unicode(bbox_text)
    ET.parse(bbox)

    doc = fitz.open(pdf)
    page_text = [page.get_text("text") for page in doc]
    pymupdf_text = "\n".join(page_text)
    (out / "pymupdf.txt").write_text(pymupdf_text, encoding="utf-8", newline="\n")
    extraction["pymupdf"] = bad_unicode(pymupdf_text)
    page_counts = [sum(not char.isspace() for char in text) for text in page_text]
    if len(page_counts) != 16 or min(page_counts) != 1180 \
            or page_counts.index(min(page_counts)) + 1 != 7:
        raise ValueError(f"Unicode page census changed: {page_counts}")

    for name, counts in extraction.items():
        if any(counts.values()):
            raise ValueError(f"illegal extracted Unicode in {name}: {counts}")
    if any(bbox_bad.values()):
        raise ValueError(f"illegal bbox Unicode: {bbox_bad}")

    fonts_text = run(["pdffonts", str(pdf)])
    (out / "pdffonts.txt").write_text(fonts_text, encoding="utf-8", newline="\n")
    font_rows = [line.split() for line in fonts_text.splitlines()[2:] if line.strip()]
    if len(font_rows) != 33 or any(row[-5:-2] != ["yes", "yes", "yes"] for row in font_rows):
        raise ValueError("font embedding/subsetting/ToUnicode census")

    info_text = run(["pdfinfo", str(pdf)])
    (out / "pdfinfo.txt").write_text(info_text, encoding="utf-8", newline="\n")
    info = dict(line.split(":", 1) for line in info_text.splitlines() if ":" in line)
    if info.get("Pages", "").strip() != "16" \
            or info.get("Page size", "").strip() != "595.276 x 841.89 pts (A4)" \
            or info.get("Encrypted", "").strip() != "no" \
            or info.get("JavaScript", "").strip() != "no" \
            or info.get("Page rot", "").strip() != "0":
        raise ValueError("PDF structural metadata")

    log_text = args.log.read_text("utf-8", errors="strict")
    issue_pattern = re.compile(
        r"LaTeX Warning|Package .* Warning|undefined references?|Citation .* undefined|"
        r"Reference .* undefined|Overfull|Underfull|^! ", re.MULTILINE
    )
    issues = issue_pattern.findall(log_text)
    if issues:
        raise ValueError(f"final LaTeX log issues: {issues[:5]}")

    aux_text = args.aux.read_text("utf-8")
    bbl_text = args.bbl.read_text("utf-8")
    cited: set[str] = set()
    for group in re.findall(r"\\citation\{([^}]*)\}", aux_text):
        cited.update(key for key in group.split(",") if key)
    bibitems = set(re.findall(r"\\bibitem\{([^}]*)\}", bbl_text))
    if len(cited) != 9 or cited != bibitems:
        raise ValueError(f"citation closure: cited={sorted(cited)} bbl={sorted(bibitems)}")

    report = {
        "artifact": {
            "pages": 16,
            "pdf_sha256": digest,
            "withdrawn_predecessor_sha256": WITHDRAWN_PDF,
        },
        "bbox": {
            "direct_xml_parse": True,
            "illegal_unicode": bbox_bad,
            "sha256": sha(bbox),
        },
        "citations": {"bibitems": len(bibitems), "cited_keys": len(cited), "closed": True},
        "compilation": {"final_log_issues": 0, "fixed_epoch": 1787011200},
        "extractions": extraction,
        "fonts": {"all_embedded_subset_tounicode": True, "rows": len(font_rows)},
        "page_unicode_nonwhitespace": {
            "counts": page_counts,
            "minimum_page": 7,
            "minimum_value": 1180,
            "metric": "Unicode code points c for which str.isspace(c) is false",
        },
        "reproducibility": {
            "fresh_lane_a_pdf_sha256": lane_hashes[0],
            "fresh_lane_b_pdf_sha256": lane_hashes[1],
            "named_pdf_byte_identical": True,
        },
        "schema": "paper48.writer-pdf-qa.v1",
        "status": "PASS",
        "visual_nonregression": {
            "basis": "fresh PDF is byte-identical to the previously inspected 16-page PDF",
            "pages": 16,
        },
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8", newline="\n")
    print(f"PASS pdf_sha256={digest} report_sha256={sha(args.report)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
