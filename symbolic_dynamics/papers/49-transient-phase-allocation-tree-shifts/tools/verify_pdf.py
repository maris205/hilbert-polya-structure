#!/usr/bin/env python3
"""Independent fail-closed PDF hard gate for the frozen Paper 49 candidate."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import fitz


ALLOWED_C0 = {0x09, 0x0A, 0x0D}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_bytes(args: list[str], *, input_bytes: bytes | None = None) -> bytes:
    return subprocess.run(args, input=input_bytes, check=True, capture_output=True).stdout


def scan(label: str, payload: bytes) -> tuple[str, dict[str, object]]:
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"{label}: invalid UTF-8: {exc}") from exc
    counts = Counter(map(ord, text))
    illegal_c0 = {
        f"U+{cp:04X}": counts[cp]
        for cp in range(0x20)
        if cp not in ALLOWED_C0 and counts[cp]
    }
    pua = sum(
        count
        for cp, count in counts.items()
        if (0xE000 <= cp <= 0xF8FF)
        or (0xF0000 <= cp <= 0xFFFFD)
        or (0x100000 <= cp <= 0x10FFFD)
    )
    violations = {
        "illegal_c0": illegal_c0,
        "del": counts[0x7F],
        "c1": sum(counts[cp] for cp in range(0x80, 0xA0)),
        "replacement": counts[0xFFFD],
        "pua": pua,
    }
    if illegal_c0 or any(violations[key] for key in ("del", "c1", "replacement", "pua")):
        raise SystemExit(f"{label}: forbidden codepoint(s): {violations}")
    return text, {
        "bytes": len(payload),
        "characters": len(text),
        "sha256": sha256(payload),
        "violations": violations,
    }


def parse_bbox(label: str, payload: bytes, path: Path) -> dict[str, object]:
    # The exact bytes sent by Poppler are persisted before either parser runs.
    path.write_bytes(payload)
    text, result = scan(label, payload)
    if path.read_bytes() != payload:
        raise SystemExit(f"{label}: stored stream is not byte-exact")
    try:
        root = ET.fromstring(payload)
    except ET.ParseError as exc:
        raise SystemExit(f"{label}: ElementTree strict XML failure: {exc}") from exc
    subprocess.run(
        ["xmllint", "--nonet", "--noout", "-"],
        input=payload,
        check=True,
        capture_output=True,
    )
    pages = root.findall(".//{*}page")
    outside: list[dict[str, object]] = []
    malformed: list[dict[str, object]] = []
    words = 0
    for page_number, page in enumerate(pages, start=1):
        width = float(page.attrib["width"])
        height = float(page.attrib["height"])
        if abs(width - 595.276) > 0.02 or abs(height - 841.89) > 0.02:
            raise SystemExit(f"{label}: non-A4 XML page {page_number}: {width}x{height}")
        for word in page.findall(".//{*}word"):
            words += 1
            x0 = float(word.attrib["xMin"])
            y0 = float(word.attrib["yMin"])
            x1 = float(word.attrib["xMax"])
            y1 = float(word.attrib["yMax"])
            if x1 < x0 or y1 < y0:
                malformed.append({"page": page_number, "word": word.text, "box": [x0, y0, x1, y1]})
            if x0 < -0.25 or y0 < -0.25 or x1 > width + 0.25 or y1 > height + 0.25:
                outside.append({"page": page_number, "word": word.text, "box": [x0, y0, x1, y1]})
    if len(pages) != 19 or words < 7000 or malformed or outside:
        raise SystemExit(
            f"{label}: geometry failure pages={len(pages)} words={words} "
            f"malformed={malformed[:2]} outside={outside[:2]}"
        )
    result.update(
        {
            "elementtree_strict_xml": "PASS",
            "xmllint_nonet_strict_xml": "PASS",
            "stored_raw_stream_sha256": sha256(path.read_bytes()),
            "pages": len(pages),
            "words": words,
            "malformed_boxes": 0,
            "outside_page_words": 0,
        }
    )
    # Retain this binding to make explicit that no decoded/sanitized proxy was parsed.
    assert text.encode("utf-8") == payload
    return result


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit("usage: pdf_hardgate.py INPUT.pdf EVIDENCE_DIR OUTPUT.json")
    pdf = Path(sys.argv[1]).resolve()
    evidence = Path(sys.argv[2])
    output = Path(sys.argv[3])
    evidence.mkdir(parents=True, exist_ok=True)
    payload = pdf.read_bytes()
    if b"/ID [" in payload:
        raise SystemExit("PDF contains a run-dependent trailer /ID")

    info_payload = run_bytes(["pdfinfo", str(pdf)])
    info_text, info_scan = scan("pdfinfo", info_payload)
    info = {}
    for line in info_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    if info.get("Pages") != "19" or info.get("Page size") != "595.276 x 841.89 pts (A4)":
        raise SystemExit(f"pdfinfo page/A4 failure: {info}")

    font_payload = run_bytes(["pdffonts", str(pdf)])
    font_text, font_scan = scan("pdffonts", font_payload)
    font_lines = [line for line in font_text.splitlines()[2:] if line.strip()]
    if len(font_lines) != 33:
        raise SystemExit(f"expected 33 font rows, found {len(font_lines)}")
    bad_fonts = []
    for line in font_lines:
        match = re.search(r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", line)
        if match is None or match.groups() != ("yes", "yes", "yes") or "Type 3" in line:
            bad_fonts.append(line)
    if bad_fonts:
        raise SystemExit(f"unembedded/Type3/no-ToUnicode font rows: {bad_fonts}")

    commands = {
        "default": ["pdftotext", "-nopgbrk", "-enc", "UTF-8", str(pdf), "-"],
        "layout": ["pdftotext", "-layout", "-nopgbrk", "-enc", "UTF-8", str(pdf), "-"],
        "raw": ["pdftotext", "-raw", "-nopgbrk", "-enc", "UTF-8", str(pdf), "-"],
        "bbox": ["pdftotext", "-bbox", "-enc", "UTF-8", str(pdf), "-"],
        "bbox_layout": ["pdftotext", "-bbox-layout", "-enc", "UTF-8", str(pdf), "-"],
    }
    streams = {name: run_bytes(command) for name, command in commands.items()}
    scans: dict[str, dict[str, object]] = {}
    for name in ("default", "layout", "raw"):
        _, scans[name] = scan(f"pdftotext-{name}", streams[name])
    scans["bbox"] = parse_bbox("pdftotext-bbox", streams["bbox"], evidence / "bbox.xml")
    scans["bbox_layout"] = parse_bbox(
        "pdftotext-bbox-layout", streams["bbox_layout"], evidence / "bbox_layout.xml"
    )

    document = fitz.open(pdf)
    if document.page_count != 19:
        raise SystemExit(f"PyMuPDF page count is {document.page_count}")
    pymupdf_payload = "".join(page.get_text("text") for page in document).encode("utf-8")
    _, scans["pymupdf"] = scan("pymupdf", pymupdf_payload)
    fitz_oob: list[dict[str, object]] = []
    for page_index, page in enumerate(document):
        page_rect = page.rect
        if abs(page_rect.width - 595.276) > 0.02 or abs(page_rect.height - 841.89) > 0.02:
            raise SystemExit(f"PyMuPDF non-A4 page {page_index + 1}: {page_rect}")
        expanded = fitz.Rect(-0.25, -0.25, page_rect.width + 0.25, page_rect.height + 0.25)
        for word in page.get_text("words"):
            rect = fitz.Rect(word[:4])
            if rect.is_empty or not expanded.contains(rect):
                fitz_oob.append({"page": page_index + 1, "text": word[4], "box": list(rect)})
        for link in page.get_links():
            rect = fitz.Rect(link.get("from", fitz.Rect()))
            if not rect.is_empty and not expanded.contains(rect):
                fitz_oob.append({"page": page_index + 1, "link": True, "box": list(rect)})
    if fitz_oob:
        raise SystemExit(f"PyMuPDF out-of-bounds object(s): {fitz_oob[:3]}")

    default_text = streams["default"].decode("utf-8")
    required = [
        "Hausdorff Dimension for Complete Cyclic Markov Hom",
        "Anonymous Authors",
        "Theorem 4.3",
        "Theorem 5.3",
        "Theorem 7.2",
        "Corollary 8.1",
        "References",
    ]
    missing = [fragment for fragment in required if fragment not in default_text]
    forbidden = [token for token in ("[VERIFY]", "[?]", "??", "qquad") if token in default_text]
    if missing or forbidden:
        raise SystemExit(f"text sentinel failure missing={missing} forbidden={forbidden}")

    result = {
        "schema": "p49-fresh-independent-pdf-hardgate-v1",
        "status": "PASS",
        "pdf": str(pdf),
        "pdf_sha256": sha256(payload),
        "pages": 19,
        "a4": True,
        "trailer_id_present": False,
        "fonts": {
            "rows": len(font_lines),
            "embedded": len(font_lines),
            "to_unicode": len(font_lines),
            "type3": 0,
            "pdffonts_scan": font_scan,
        },
        "extractors": scans,
        "strict_xml": {"bbox": "PASS", "bbox_layout": "PASS", "sanitization": "NONE"},
        "bbox_outside_words": 0,
        "pymupdf_outside_words_or_links": 0,
        "pdfinfo": info,
        "pdfinfo_scan": info_scan,
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "PDF_HARDGATE_PASS pages=19 fonts=33 extractors=6 "
        f"bbox_words={scans['bbox']['words']} sha256={result['pdf_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
