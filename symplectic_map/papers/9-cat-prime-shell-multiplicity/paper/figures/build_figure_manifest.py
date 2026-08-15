#!/usr/bin/env python3
"""Build the deterministic machine-readable Paper 9 figure manifest."""

from __future__ import annotations

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

from figure_data import EXPECTED_HASHES, PAPER_ROOT, sha256_file, validate_source_hashes


HERE = Path(__file__).resolve().parent
FIGURES = {
    "fig1_shell_profiles": "gen_fig1_shell_profiles.py",
    "fig2_product_semantics": "gen_fig2_product_semantics.py",
    "fig3_mechanism_boundary": "gen_fig3_mechanism_boundary.py",
}
FORMATS = ("pdf", "svg", "png")
GENERATOR_FILES = (
    "figure_data.py",
    "paper_plot_style.py",
    "gen_fig1_shell_profiles.py",
    "gen_fig2_product_semantics.py",
    "gen_fig3_mechanism_boundary.py",
    "generate_all.py",
    "build_figure_manifest.py",
    "latex_includes.tex",
)
PLANNING_FILES = (
    "PAPER_PLAN.md",
    "notes/CITATION_VERIFICATION.md",
    "paper/references.bib",
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
        if len(fields) < 9:
            raise RuntimeError(f"unparseable pdffonts row for {path.name}: {line}")
        record = {
            "name": fields[0],
            "type": " ".join(fields[1:-6]),
            "encoding": fields[-6],
            "embedded": fields[-5],
            "subset": fields[-4],
            "unicode": fields[-3],
        }
        font_rows.append(record)
    if not font_rows:
        raise RuntimeError(f"no fonts detected in {path.name}")
    if any(row["embedded"] != "yes" for row in font_rows):
        raise RuntimeError(f"unembedded font in {path.name}")
    if any(row["subset"] != "yes" for row in font_rows):
        raise RuntimeError(f"unsubsetted font in {path.name}")
    if any(row["unicode"] != "yes" for row in font_rows):
        raise RuntimeError(f"font lacks Unicode map in {path.name}")
    if any("Type 3" in row["type"] for row in font_rows):
        raise RuntimeError(f"Type-3 font in {path.name}")

    image_output = run_checked(["pdfimages", "-list", str(path)])
    raster_rows = [
        line
        for line in image_output.splitlines()
        if re.match(r"^\s*\d+\s+\d+\s+\S+", line)
    ]
    if raster_rows:
        raise RuntimeError(f"unexpected raster object in {path.name}")

    info_output = run_checked(["pdfinfo", str(path)])
    pages_match = re.search(r"^Pages:\s+(\d+)\s*$", info_output, re.MULTILINE)
    size_match = re.search(r"^Page size:\s+(.+)$", info_output, re.MULTILINE)
    if pages_match is None or int(pages_match.group(1)) != 1:
        raise RuntimeError(f"expected a one-page PDF: {path.name}")
    return {
        "one_page": True,
        "page_size": size_match.group(1).strip() if size_match else "unknown",
        "font_count": len(font_rows),
        "fonts": font_rows,
        "all_fonts_embedded_subset_unicode": True,
        "type3_fonts": 0,
        "raster_image_objects": 0,
        "vector_only": True,
    }


def svg_quality(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    counts = {"text": 0, "path": 0, "image": 0}
    for element in root.iter():
        name = element.tag.rsplit("}", 1)[-1]
        if name in counts:
            counts[name] += 1
    if counts["text"] == 0:
        raise RuntimeError(f"SVG has no selectable text: {path.name}")
    if counts["image"] != 0:
        raise RuntimeError(f"SVG contains a raster image: {path.name}")
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
        raise RuntimeError(f"PNG below publication scale: {path.name}")
    if dpi is None or min(float(dpi[0]), float(dpi[1])) < 299.0:
        raise RuntimeError(f"PNG below 300 dpi tolerance: {path.name}")
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
    expected_outputs = {
        f"{stem}.{extension}" for stem in FIGURES for extension in FORMATS
    }
    if set(run_two) != expected_outputs:
        raise RuntimeError("two-run output inventory is not exactly nine files")

    outputs: dict[str, Any] = {}
    for stem, generator in FIGURES.items():
        files: dict[str, Any] = {}
        for extension in FORMATS:
            name = f"{stem}.{extension}"
            path = HERE / name
            actual = sha256_file(path)
            if actual != run_two[name]:
                raise RuntimeError(f"output changed before manifest build: {name}")
            if extension == "pdf":
                quality = pdf_quality(path)
            elif extension == "svg":
                quality = svg_quality(path)
            else:
                quality = png_quality(path)
            files[extension] = {
                "path": name,
                "sha256": actual,
                "bytes": path.stat().st_size,
                "quality": quality,
            }
        outputs[stem] = {
            "generator": generator,
            "generator_sha256": sha256_file(HERE / generator),
            "files": files,
        }

    planning_hashes = {
        name: sha256_file(PAPER_ROOT / name) for name in PLANNING_FILES
    }
    generator_hashes = {name: sha256_file(HERE / name) for name in GENERATOR_FILES}
    determinism_path = HERE / "DETERMINISM_AUDIT.json"
    if not determinism_path.is_file() or determinism_path.is_symlink():
        raise RuntimeError("determinism audit is absent or not a regular file")

    manifest = {
        "schema": "paper9.figure_manifest.v1",
        "generated_utc": "2026-08-14T00:00:00Z",
        "status": "PASS",
        "scientific_scope": {
            "classification": (
                "PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED / "
                "A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED"
            ),
            "fixed_development_seen_primes": [2, 3, 5, 7, 11],
            "all_prime_claims": "proof only",
            "global_convergence_claims": "proof only",
            "candidate_rerun": False,
            "new_prime_or_modulus_scan": False,
            "numeric_s_or_log_evaluation": False,
            "centralizer_computation": False,
            "new_scientific_result": False,
        },
        "source_hashes": source_hashes,
        "result_manifest": {
            "path": "results/result_manifest.json",
            "status": "PASS",
            "sha256": EXPECTED_HASHES["results/result_manifest.json"],
        },
        "planning_artifact_hashes": planning_hashes,
        "generator_hashes": generator_hashes,
        "determinism": {
            "status": "PASS",
            "runs": 2,
            "byte_identical": True,
            "run_one_sha256": run_one,
            "run_two_sha256": run_two,
            "audit_path": "DETERMINISM_AUDIT.json",
            "audit_sha256": sha256_file(determinism_path),
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
        "outputs": outputs,
        "quality_summary": {
            "pdf_fonts_embedded_subset_unicode": "PASS",
            "pdf_no_type3": "PASS",
            "pdf_vector_only": "PASS",
            "svg_selectable_text": "PASS",
            "svg_vector_only": "PASS",
            "png_300_dpi": "PASS",
            "original_resolution_visual_qa": "documented in FIGURE_QA.md",
        },
    }
    output_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


if __name__ == "__main__":
    raise SystemExit(
        "build_figure_manifest.py is called by generate_all.py with two in-memory runs"
    )

