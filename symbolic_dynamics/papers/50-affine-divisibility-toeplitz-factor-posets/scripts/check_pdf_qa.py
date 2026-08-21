#!/usr/bin/env python3
"""Fail-closed raw PDF text, XML, Unicode, page, and bbox audit."""

from __future__ import annotations

from collections import Counter
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "paper" / "main.pdf"
EXPECTED_PAGES = 17
A4_WIDTH = 595.276
A4_HEIGHT = 841.89
PAGE_TOLERANCE = 0.05
BBOX_TOLERANCE = 0.25


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def illegal_codepoints(text: str, *, allow_form_feed: bool) -> dict[str, object]:
    allowed_c0 = {0x09, 0x0A, 0x0D}
    if allow_form_feed:
        allowed_c0.add(0x0C)
    counts = Counter()
    categories = Counter()
    for character in text:
        value = ord(character)
        category = None
        if value < 0x20 and value not in allowed_c0:
            category = "C0"
        elif value == 0x7F:
            category = "DEL"
        elif 0x80 <= value <= 0x9F:
            category = "C1"
        elif value == 0xFFFD:
            category = "replacement"
        elif (
            0xE000 <= value <= 0xF8FF
            or 0xF0000 <= value <= 0xFFFFD
            or 0x100000 <= value <= 0x10FFFD
        ):
            category = "PUA"
        if category is not None:
            counts[value] += 1
            categories[category] += 1
    return {
        "by_category": dict(sorted(categories.items())),
        "by_codepoint": {
            f"U+{value:04X}": count for value, count in sorted(counts.items())
        },
        "total": sum(counts.values()),
    }


def run_pdftotext(output: Path, options: list[str]) -> tuple[bytes, str]:
    completed = subprocess.run(
        ["pdftotext", *options, "-enc", "UTF-8", str(PDF), str(output)],
        check=True,
        capture_output=True,
        text=True,
    )
    if completed.stderr:
        raise RuntimeError({"pdftotext_options": options, "stderr": completed.stderr})
    payload = output.read_bytes()
    return payload, payload.decode("utf-8", errors="strict")


def plain_record(payload: bytes, text: str, mode: str) -> dict[str, object]:
    controls = illegal_codepoints(text, allow_form_feed=True)
    form_feeds = text.count("\f")
    forbidden_tokens = {
        "double_question_mark": text.count("??"),
        "verify_placeholder": text.count("[VERIFY]"),
    }
    if controls["total"] or form_feeds != EXPECTED_PAGES or any(forbidden_tokens.values()):
        raise RuntimeError({
            "mode": mode,
            "illegal": controls,
            "form_feeds": form_feeds,
            "forbidden_tokens": forbidden_tokens,
        })
    return {
        "form_feed_page_separators": form_feeds,
        "illegal": controls,
        "sha256": digest(payload),
        "size": len(payload),
    }


def xml_record(payload: bytes, output: Path, mode: str) -> dict[str, object]:
    text = payload.decode("utf-8", errors="strict")
    controls = illegal_codepoints(text, allow_form_feed=False)
    if controls["total"]:
        raise RuntimeError({"mode": mode, "illegal": controls})

    # Parse the untouched bytes.  No replacement, filtering, regex cleanup, or
    # error-tolerant decode is permitted before either strict parser.
    root = ET.fromstring(payload)
    xmllint = subprocess.run(
        ["xmllint", "--nonet", "--noout", str(output)],
        capture_output=True,
        text=True,
    )
    if xmllint.returncode != 0 or xmllint.stderr:
        raise RuntimeError({
            "mode": mode,
            "xmllint_exit": xmllint.returncode,
            "xmllint_stderr": xmllint.stderr,
        })

    pages = [element for element in root.iter() if local_name(element.tag) == "page"]
    if len(pages) != EXPECTED_PAGES:
        raise RuntimeError({"mode": mode, "page_count": len(pages)})
    violations = []
    word_count = 0
    page_sizes = []
    for page_index, page in enumerate(pages, start=1):
        width = float(page.attrib["width"])
        height = float(page.attrib["height"])
        page_sizes.append([width, height])
        if abs(width - A4_WIDTH) > PAGE_TOLERANCE or abs(height - A4_HEIGHT) > PAGE_TOLERANCE:
            violations.append({"page": page_index, "page_size": [width, height], "kind": "not_A4"})
        for word in page.iter():
            if local_name(word.tag) != "word":
                continue
            word_count += 1
            box = [float(word.attrib[key]) for key in ("xMin", "yMin", "xMax", "yMax")]
            x_min, y_min, x_max, y_max = box
            if not (
                -BBOX_TOLERANCE <= x_min <= x_max <= width + BBOX_TOLERANCE
                and -BBOX_TOLERANCE <= y_min <= y_max <= height + BBOX_TOLERANCE
            ):
                violations.append({"page": page_index, "box": box, "page_size": [width, height], "kind": "bbox"})
    if violations:
        raise RuntimeError({"mode": mode, "violations": violations})
    return {
        "bbox_violation_count": 0,
        "illegal": controls,
        "page_count": len(pages),
        "page_size": "A4",
        "raw_xml_sanitized": False,
        "sha256": digest(payload),
        "size": len(payload),
        "strict_elementtree_parse": True,
        "strict_xmllint_parse": True,
        "word_count": word_count,
    }


def run() -> dict[str, object]:
    if not PDF.is_file():
        raise RuntimeError(f"missing PDF: {PDF}")
    records: dict[str, object] = {}
    with tempfile.TemporaryDirectory(prefix="p50_pdf_raw_qa_") as temporary:
        directory = Path(temporary)
        for mode, options in (
            ("default", []),
            ("layout", ["-layout"]),
            ("raw", ["-raw"]),
        ):
            payload, text = run_pdftotext(directory / f"{mode}.txt", options)
            records[mode] = plain_record(payload, text, mode)
        for mode, options in (
            ("bbox", ["-bbox"]),
            ("bbox_layout", ["-bbox-layout"]),
        ):
            output = directory / f"{mode}.html"
            payload, _ = run_pdftotext(output, options)
            records[mode] = xml_record(payload, output, mode)

    try:
        import fitz
    except Exception as exc:  # fail closed if the independent backend vanishes
        raise RuntimeError("PyMuPDF/fitz unavailable") from exc
    document = fitz.open(PDF)
    pymupdf_text = "\n".join(page.get_text("text") for page in document)
    pymupdf_controls = illegal_codepoints(pymupdf_text, allow_form_feed=False)
    if document.page_count != EXPECTED_PAGES or pymupdf_controls["total"]:
        raise RuntimeError({
            "mode": "pymupdf",
            "page_count": document.page_count,
            "illegal": pymupdf_controls,
        })
    records["pymupdf"] = {
        "illegal": pymupdf_controls,
        "page_count": document.page_count,
        "sha256": digest(pymupdf_text.encode("utf-8")),
        "version": getattr(fitz, "VersionBind", "unknown"),
    }
    return {
        "bbox_tolerance_points": BBOX_TOLERANCE,
        "extractors": records,
        "page_count": EXPECTED_PAGES,
        "pdf_sha256": digest(PDF.read_bytes()),
        "raw_xml_sanitization": "forbidden",
        "status": "PASS",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.record and args.check:
        raise SystemExit("choose at most one action")
    raw = (json.dumps(run(), indent=2, sort_keys=True) + "\n").encode("ascii")
    target = ROOT / "evidence/PDF_QA.json"
    if args.record:
        if os.path.lexists(target):
            raise SystemExit("PDF_QA_EXISTS")
        descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o644)
        try:
            os.fchmod(descriptor, 0o644)
            offset = 0
            while offset < len(raw):
                offset += os.write(descriptor, raw[offset:])
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        print(f"RECORDED pdf_qa_sha256={hashlib.sha256(raw).hexdigest()}")
    elif args.check:
        if target.is_symlink() or not target.is_file() or target.read_bytes() != raw:
            raise SystemExit("PDF_QA_MISMATCH")
        print(f"PASS pdf_qa_sha256={hashlib.sha256(raw).hexdigest()}")
    else:
        sys.stdout.buffer.write(raw)
