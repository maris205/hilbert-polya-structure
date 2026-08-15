#!/usr/bin/env python3
"""Build the deterministic machine-readable Paper 11 figure manifest."""

from __future__ import annotations

import json
import platform
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import matplotlib
from PIL import Image

from figure_data import (
    CLASSIFICATION,
    EXPECTED_HASHES,
    LOCKED_MODULI,
    PAPER_ROOT,
    sha256_file,
    validate_source_hashes,
)


HERE = Path(__file__).resolve().parent
FIGURES = {
    "fig1_retention_hierarchy": "gen_fig1_retention_hierarchy.py",
    "fig2_nine_row_retention": "gen_fig2_nine_row_retention.py",
    "fig3_effectivity_counterexamples": "gen_fig3_effectivity_counterexamples.py",
}
FORMATS = ("pdf", "svg", "png")
GENERATOR_FILES = (
    "figure_data.py",
    "paper_plot_style.py",
    "gen_fig1_retention_hierarchy.py",
    "gen_fig2_nine_row_retention.py",
    "gen_fig3_effectivity_counterexamples.py",
    "generate_all.py",
    "build_figure_manifest.py",
    "build_asset_tree.py",
    "latex_includes.tex",
)
PLANNING_FILES = (
    "PAPER_PLAN.md",
    "paper/CITATION_VERIFICATION.md",
    "paper/references.bib",
)
DOCUMENTATION_FILES = (
    "PROVENANCE.md",
    "FIGURE_QA.md",
    "FIGURE_TRACE.json",
    "ASSET_TREE.json",
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


def validate_publication_layer() -> dict[str, Any]:
    bibliography = (PAPER_ROOT / "paper/references.bib").read_text(encoding="utf-8")
    citation_note = (PAPER_ROOT / "paper/CITATION_VERIFICATION.md").read_text(encoding="utf-8")
    includes = (HERE / "latex_includes.tex").read_text(encoding="utf-8")
    if len(re.findall(r"(?m)^@", bibliography)) != 14:
        raise RuntimeError("publication bibliography does not contain exactly 14 entries")
    walton_markers = (
        "doi           = {10.1016/j.jnt.2018.03.023}",
        "volume        = {192}",
        "pages         = {386--405}",
    )
    if any(marker not in bibliography for marker in walton_markers):
        raise RuntimeError("DOI-authoritative Walton metadata is absent")
    if "historical bibliographic typo" not in citation_note:
        raise RuntimeError("Walton source-side typo provenance note is absent")
    if (
        "This correction changes\nno title, author, DOI, theorem, source formula, "
        "registered result, novelty\nscore, or scope conclusion" not in citation_note
    ):
        raise RuntimeError("publication-layer no-claim-change note is absent")
    if includes.count("\\begin{figure*}") != 3:
        raise RuntimeError("LaTeX contract does not contain exactly three figures")
    for label in (
        "fig:retention-hierarchy",
        "fig:nine-row-retention",
        "fig:effectivity-counterexamples",
    ):
        if includes.count(f"\\label{{{label}}}") != 1:
            raise RuntimeError(f"LaTeX figure-label contract changed: {label}")
    required_scope = (
        "sole locked exception",
        "family-uniform",
        "r_2=r_4=3",
        "There is no\n  family-uniform starred column",
    )
    if any(marker not in includes for marker in required_scope):
        raise RuntimeError("q=2 family-uniform caption scope changed")
    return {
        "bibliography_entries": 14,
        "walton_doi_authoritative_metadata": "JNT 192 (2018), 386--405",
        "historical_source_sidecar_typo_corrected_at_publication_layer": True,
        "scientific_claim_change": False,
        "latex_figure_count": 3,
    }


def write_manifest(
    run_one: dict[str, str],
    run_two: dict[str, str],
    output_path: Path,
) -> dict[str, Any]:
    source_hashes = validate_source_hashes()
    publication_layer = validate_publication_layer()
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
            quality = (
                pdf_quality(path)
                if extension == "pdf"
                else svg_quality(path)
                if extension == "svg"
                else png_quality(path)
            )
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
    documentation_hashes = {
        name: sha256_file(HERE / name) for name in DOCUMENTATION_FILES
    }
    determinism_path = HERE / "DETERMINISM_AUDIT.json"
    if not determinism_path.is_file() or determinism_path.is_symlink():
        raise RuntimeError("determinism audit is absent or not a regular file")

    manifest = {
        "schema": "paper11.figure_manifest.v1",
        "generated_utc": "2026-08-15T00:00:00Z",
        "status": "PASS",
        "scientific_scope": {
            "classification": CLASSIFICATION,
            "fixed_development_seen_moduli": list(LOCKED_MODULI),
            "all_q_claims": "proof only",
            "q2_point_cardinality_exception": True,
            "q2_pair": [3, 1],
            "family_uniform_nonattainment_only": True,
            "forbidden_per_row_none_claim": False,
            "q2_modulus_specific": False,
            "r2_equals_r4": 3,
            "candidate_rerun": False,
            "analyzer_rerun": False,
            "new_prime_or_modulus_scan": False,
            "numeric_s_or_log_evaluation": False,
            "numeric_q_to_minus_s_evaluation": False,
            "candidate_import_or_execution": False,
            "new_scientific_result": False,
            "novelty_score_out_of_10": 2,
        },
        "source_hashes": source_hashes,
        "scope_audit": {
            "path": "notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md",
            "verdict": "PASS_WITH_SCOPE_CORRECTION",
            "sha256": EXPECTED_HASHES["notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md"],
        },
        "result_manifest": {
            "path": "results/result_manifest.json",
            "status": "PASS",
            "sha256": EXPECTED_HASHES["results/result_manifest.json"],
        },
        "publication_layer": publication_layer,
        "planning_artifact_hashes": planning_hashes,
        "generator_hashes": generator_hashes,
        "documentation_hashes": documentation_hashes,
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
