#!/usr/bin/env python3
"""Build a deterministic machine-readable manifest for Paper 8 figures."""

from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import matplotlib
from PIL import Image

from figure_data import EXPECTED_HASHES, sha256_file, validate_source_hashes


HERE = Path(__file__).resolve().parent
FIGURES = {
    "fig1_carrier_bridge": "gen_fig1_carrier_bridge.py",
    "fig2_standard_cat_boundary": "gen_fig2_standard_cat_boundary.py",
    "fig3_capacity_specificity": "gen_fig3_capacity_specificity.py",
}
FORMATS = ("pdf", "svg", "png")
GENERATOR_FILES = (
    "paper_plot_style.py",
    "figure_data.py",
    "gen_fig1_carrier_bridge.py",
    "gen_fig2_standard_cat_boundary.py",
    "gen_fig3_capacity_specificity.py",
    "generate_all.py",
    "build_figure_manifest.py",
    "latex_includes.tex",
)


def run_checked(command: list[str]) -> str:
    completed = subprocess.run(
        command,
        cwd=HERE,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def pdf_quality(path: Path) -> dict[str, Any]:
    font_output = run_checked(["pdffonts", str(path)])
    font_rows = []
    for line in font_output.splitlines()[2:]:
        fields = line.split()
        if not fields:
            continue
        if len(fields) < 8:
            raise RuntimeError(f"unparseable pdffonts row for {path.name}: {line}")
        font_rows.append(
            {
                "name": fields[0],
                "type": " ".join(fields[1:-6]),
                "encoding": fields[-6],
                "embedded": fields[-5],
                "subset": fields[-4],
                "unicode": fields[-3],
            }
        )
    if not font_rows or any(row["embedded"] != "yes" for row in font_rows):
        raise RuntimeError(f"PDF fonts are not fully embedded: {path.name}")

    image_output = run_checked(["pdfimages", "-list", str(path)])
    raster_rows = [
        line
        for line in image_output.splitlines()
        if re.match(r"^\s*\d+\s+\d+\s+\S+", line)
    ]
    if raster_rows:
        raise RuntimeError(f"unexpected raster image object in {path.name}")

    info_output = run_checked(["pdfinfo", str(path)])
    pages_match = re.search(r"^Pages:\s+(\d+)\s*$", info_output, re.MULTILINE)
    page_match = re.search(r"^Page size:\s+(.+)$", info_output, re.MULTILINE)
    if pages_match is None or int(pages_match.group(1)) != 1:
        raise RuntimeError(f"expected one-page PDF: {path.name}")
    return {
        "one_page": True,
        "page_size": page_match.group(1).strip() if page_match else "unknown",
        "font_count": len(font_rows),
        "fonts": font_rows,
        "all_fonts_embedded": True,
        "raster_image_objects": 0,
        "vector_only": True,
    }


def svg_quality(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    counts = {"text": 0, "path": 0, "image": 0}
    for element in root.iter():
        local_name = element.tag.rsplit("}", 1)[-1]
        if local_name in counts:
            counts[local_name] += 1
    if counts["text"] == 0:
        raise RuntimeError(f"SVG has no selectable text nodes: {path.name}")
    if counts["image"] != 0:
        raise RuntimeError(f"SVG contains a raster image node: {path.name}")
    return {
        "xml_parse": "PASS",
        "selectable_text_nodes": counts["text"],
        "vector_path_nodes": counts["path"],
        "raster_image_nodes": counts["image"],
        "vector_only": True,
    }


def png_quality(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        width, height = image.size
        dpi = image.info.get("dpi")
        mode = image.mode
    if width < 2000 or height < 1000:
        raise RuntimeError(f"PNG fallback is below intended publication scale: {path.name}")
    if dpi is None or min(float(dpi[0]), float(dpi[1])) < 299.0:
        raise RuntimeError(f"PNG fallback is below 300 dpi tolerance: {path.name}")
    return {
        "pixel_dimensions": [width, height],
        "dpi": [round(float(dpi[0]), 4), round(float(dpi[1]), 4)],
        "dpi_300_tolerance": "PASS",
        "mode": mode,
    }


def write_manifest(
    run_one: dict[str, str],
    run_two: dict[str, str],
    output_path: Path,
) -> dict[str, Any]:
    source_hashes = validate_source_hashes()
    if run_one != run_two:
        differing = sorted(key for key in run_one if run_one.get(key) != run_two.get(key))
        raise RuntimeError(f"two-run byte determinism failed: {differing}")

    expected_names = {
        f"{stem}.{extension}" for stem in FIGURES for extension in FORMATS
    }
    if set(run_two) != expected_names:
        raise RuntimeError("two-run hash inventory does not match the nine expected outputs")

    outputs: dict[str, Any] = {}
    for stem, generator in FIGURES.items():
        files: dict[str, Any] = {}
        for extension in FORMATS:
            name = f"{stem}.{extension}"
            path = HERE / name
            actual_hash = sha256_file(path)
            if actual_hash != run_two[name]:
                raise RuntimeError(f"post-run output changed before manifest build: {name}")
            quality: dict[str, Any]
            if extension == "pdf":
                quality = pdf_quality(path)
            elif extension == "svg":
                quality = svg_quality(path)
            else:
                quality = png_quality(path)
            files[extension] = {
                "path": name,
                "sha256": actual_hash,
                "bytes": path.stat().st_size,
                "quality": quality,
            }
        outputs[stem] = {
            "generator": generator,
            "generator_sha256": sha256_file(HERE / generator),
            "files": files,
        }

    generator_hashes = {
        name: sha256_file(HERE / name) for name in GENERATOR_FILES
    }
    manifest = {
        "schema": "paper8.figure_manifest.v1",
        "generated_utc": "2026-08-14T00:00:00Z",
        "status": "PASS",
        "scientific_scope": {
            "classification": "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH",
            "computed_periods": list(range(1, 13)),
            "theorem_only_range": "all integers n > 12",
            "tail_periods_computed": [],
            "candidate_rerun": False,
            "new_scientific_result": False,
        },
        "source_hashes": source_hashes,
        "result_manifest": {
            "path": "results/result_manifest.json",
            "status": "PASS",
            "sha256": EXPECTED_HASHES["results/result_manifest.json"],
        },
        "determinism": {
            "status": "PASS",
            "runs": 2,
            "byte_identical": True,
            "run_one_sha256": run_one,
            "run_two_sha256": run_two,
            "python_hash_seed": "0",
            "source_date_epoch": "1471132800",
            "bytecode_writes_disabled": True,
        },
        "environment": {
            "python": platform.python_version(),
            "matplotlib": matplotlib.__version__,
            "pillow": Image.__version__,
            "platform": platform.platform(),
        },
        "generator_hashes": generator_hashes,
        "outputs": outputs,
        "quality_summary": {
            "pdf_fonts_embedded": "PASS",
            "pdf_vector_only": "PASS",
            "svg_selectable_text": "PASS",
            "svg_vector_only": "PASS",
            "png_300_dpi": "PASS",
            "original_resolution_visual_qa": "documented in PROVENANCE.md",
        },
    }
    output_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-one", required=True, type=Path)
    parser.add_argument("--run-two", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=HERE / "FIGURE_MANIFEST.json")
    args = parser.parse_args()
    run_one = json.loads(args.run_one.read_text())
    run_two = json.loads(args.run_two.read_text())
    write_manifest(run_one, run_two, args.output.resolve())


if __name__ == "__main__":
    main()
