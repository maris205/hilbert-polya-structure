#!/usr/bin/env python3
"""Read-only final PDF quality checks for the P47 writer candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET


def run(*args: str) -> bytes:
    completed = subprocess.run(
        args,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.stderr:
        raise SystemExit(f"STDERR:{args[0]}:{completed.stderr.decode('utf-8', 'replace')}")
    return completed.stdout


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def text_metrics(raw: bytes) -> dict[str, int]:
    text = raw.decode("utf-8", "strict")
    illegal = [
        ord(character)
        for character in text
        if (
            (ord(character) < 32 and character not in "\t\n\r\f")
            or ord(character) == 127
            or 128 <= ord(character) <= 159
        )
    ]
    forbidden = re.findall(r"\?\?|\[\?\]|VERIFY|TODO|FIXME", text)
    return {
        "character_count": len(text),
        "form_feed_page_separators": text.count("\f"),
        "forbidden_marker_count": len(forbidden),
        "illegal_c0_del_c1_count": len(illegal),
        "replacement_character_count": text.count("\ufffd"),
    }


def bbox_metrics(raw: bytes) -> dict[str, int]:
    root = ET.fromstring(raw.decode("utf-8", "strict"))
    pages = [element for element in root.iter() if element.tag.endswith("page")]
    words = [element for element in root.iter() if element.tag.endswith("word")]
    bad = 0
    for page in pages:
        width = float(page.attrib["width"])
        height = float(page.attrib["height"])
        for word in page.iter():
            if not word.tag.endswith("word"):
                continue
            x_min = float(word.attrib["xMin"])
            y_min = float(word.attrib["yMin"])
            x_max = float(word.attrib["xMax"])
            y_max = float(word.attrib["yMax"])
            if (
                x_min < -0.01
                or y_min < -0.01
                or x_max > width + 0.01
                or y_max > height + 0.01
                or x_max < x_min
                or y_max < y_min
            ):
                bad += 1
    return {
        "out_of_page_word_count": bad,
        "page_count": len(pages),
        "word_count": len(words),
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    if not root.is_absolute() or root.is_symlink() or root.resolve(strict=True) != root:
        raise SystemExit("ROOT_NOT_CANONICAL")
    pdf = root / "main.pdf"
    round2 = root / "main_round2.pdf"
    compile_log = root / "evidence" / "FINAL_COMPILE.log"
    if not pdf.is_file() or not round2.is_file() or pdf.read_bytes() != round2.read_bytes():
        raise SystemExit("FINAL_PDF_IDENTITY")

    info = run("pdfinfo", str(pdf)).decode("utf-8", "strict")
    if "Pages:           14" not in info or "Page size:       595.276 x 841.89 pts (A4)" not in info:
        raise SystemExit("PDFINFO")

    fonts = run("pdffonts", str(pdf)).decode("utf-8", "strict").splitlines()[2:]
    font_flags = []
    for line in fonts:
        match = re.search(r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", line)
        if match is None:
            raise SystemExit("PDF_FONTS_PARSE")
        font_flags.append(match.groups())
    if not fonts or any(flags != ("yes", "yes", "yes") for flags in font_flags):
        raise SystemExit("PDF_FONT_FLAGS")
    if any("Type 3" in line for line in fonts):
        raise SystemExit("TYPE3_FONT")

    text = {
        "default": text_metrics(run("pdftotext", str(pdf), "-")),
        "layout": text_metrics(run("pdftotext", "-layout", str(pdf), "-")),
        "raw": text_metrics(run("pdftotext", "-raw", str(pdf), "-")),
    }
    for metrics in text.values():
        if (
            metrics["illegal_c0_del_c1_count"]
            or metrics["replacement_character_count"]
            or metrics["forbidden_marker_count"]
        ):
            raise SystemExit("PDF_TEXT")

    bbox = {
        "bbox": bbox_metrics(run("pdftotext", "-bbox", str(pdf), "-")),
        "bbox_layout": bbox_metrics(run("pdftotext", "-bbox-layout", str(pdf), "-")),
    }
    for metrics in bbox.values():
        if metrics["page_count"] != 14 or metrics["out_of_page_word_count"]:
            raise SystemExit("PDF_BBOX")

    log_text = compile_log.read_text("utf-8")
    warning_pattern = re.compile(
        r"LaTeX Warning|Package\s+\S+\s+Warning|"
        r"Overfull \\hbox|Underfull \\hbox|"
        r"undefined references|undefined citations",
        re.IGNORECASE,
    )
    if warning_pattern.search(log_text):
        raise SystemExit("COMPILE_WARNING")

    result = {
        "bbox": bbox,
        "font_count": len(fonts),
        "fonts_embedded_subset_unicode": True,
        "main_pdf_sha256": sha256(pdf),
        "page_count": 14,
        "page_size": "A4_595.276x841.89pt",
        "schema": "paper47.writer-pdf-qa.v1",
        "status": "PASS",
        "text": text,
        "type3_font_count": 0,
    }
    print(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
