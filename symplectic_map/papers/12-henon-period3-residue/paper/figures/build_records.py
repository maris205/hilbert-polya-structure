#!/usr/bin/env python3
"""Build deterministic QA, trace, manifest, and asset-tree records."""

from __future__ import annotations

import json
import platform
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import matplotlib
from PIL import Image, __version__ as pillow_version

from figure_data import load_contract, sha256_file


HERE = Path(__file__).resolve().parent
PAPER_ROOT = HERE.parent.parent
PROJECT_ROOT = PAPER_ROOT
FORMATS = ("pdf", "png", "svg")
FIGURE_SCRIPTS = {
    "fig1_theorem_architecture": "gen_fig1_theorem_architecture.py",
    "fig2_weighted_two_term_law": "gen_fig2_weighted_two_term_law.py",
    "fig3_step9_certificate_pipeline": "gen_fig3_step9_certificate_pipeline.py",
}


def canonical_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def write_json(path: Path, payload: Any) -> None:
    path.write_bytes(canonical_bytes(payload))


def command_output(*args: str) -> str:
    return subprocess.run(
        args,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout


def pdf_quality(path: Path) -> dict[str, Any]:
    info_text = command_output("pdfinfo", str(path))
    info: dict[str, str] = {}
    for line in info_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    fonts_text = command_output("pdffonts", str(path))
    font_rows = [
        line.strip()
        for line in fonts_text.splitlines()[2:]
        if line.strip()
    ]
    images_text = command_output("pdfimages", "-list", str(path))
    image_lines = images_text.splitlines()
    separator_index = next(
        (index for index, line in enumerate(image_lines) if line.startswith("---")),
        len(image_lines),
    )
    image_rows = [line for line in image_lines[separator_index + 1 :] if line.strip()]
    all_embedded = bool(font_rows) and all(" yes " in f" {line} " for line in font_rows)
    type3_count = sum("Type 3" in line or "Type3" in line for line in font_rows)
    return {
        "all_fonts_embedded": all_embedded,
        "font_count": len(font_rows),
        "font_rows": font_rows,
        "one_page": info.get("Pages") == "1",
        "page_size": info.get("Page size"),
        "pdf_version": info.get("PDF version"),
        "raster_image_objects": len(image_rows),
        "type3_fonts": type3_count,
        "vector_only": len(image_rows) == 0,
    }


def svg_quality(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    elements = list(root.iter())
    count = lambda suffix: sum(element.tag.endswith(suffix) for element in elements)
    return {
        "raster_image_nodes": count("image"),
        "selectable_text_nodes": count("text"),
        "vector_path_nodes": count("path"),
        "vector_only": count("image") == 0,
        "xml_parse": "PASS",
    }


def png_quality(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        dpi = image.info.get("dpi", (0.0, 0.0))
        return {
            "dpi": [float(dpi[0]), float(dpi[1])],
            "dpi_300_tolerance": (
                "PASS"
                if abs(float(dpi[0]) - 300.0) < 0.01
                and abs(float(dpi[1]) - 300.0) < 0.01
                else "FAIL"
            ),
            "mode": image.mode,
            "pixel_dimensions": list(image.size),
        }


def output_record(path: Path) -> dict[str, Any]:
    if path.suffix == ".pdf":
        quality = pdf_quality(path)
    elif path.suffix == ".svg":
        quality = svg_quality(path)
    elif path.suffix == ".png":
        quality = png_quality(path)
    else:
        raise RuntimeError(f"unsupported output format: {path}")
    return {
        "bytes": path.stat().st_size,
        "path": path.name,
        "quality": quality,
        "sha256": sha256_file(path),
    }


def validate_caption_label_contract(contract: dict[str, Any]) -> None:
    latex = (HERE / "latex_includes.tex").read_text(encoding="utf-8")
    pairs = re.findall(
        r"\\caption\{(.*?)\}\s*\\label\{([^}]+)\}",
        latex,
        flags=re.DOTALL,
    )
    if len(pairs) != 3:
        raise RuntimeError("latex_includes.tex must contain exactly three caption-label pairs")
    normalize = lambda value: " ".join(value.split())
    expected = [
        (normalize(item["caption_contract"]), item["label"])
        for item in contract["figures"]
    ]
    observed = [(normalize(caption), label) for caption, label in pairs]
    if observed != expected:
        raise RuntimeError("LaTeX caption/label contract differs from figure_contract.json")

    plan = (PROJECT_ROOT / "PAPER_PLAN.md").read_text(encoding="utf-8")
    planned_captions = re.findall(
        r"\*\*Exact caption:\*\*\s*\n\s*>\s*(.+)",
        plan,
    )
    if [normalize(caption) for caption in planned_captions] != [
        caption for caption, _label in expected
    ]:
        raise RuntimeError("PAPER_PLAN.md exact captions differ from figure_contract.json")
    planned_labels = re.findall(
        r"\| Fig\. \d \| `[^`]+`, `([^`]+)` \|",
        plan,
    )
    if planned_labels != [label for _caption, label in expected]:
        raise RuntimeError("PAPER_PLAN.md labels differ from figure_contract.json")


def extract_manuscript_citation_keys(path: Path) -> list[str]:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError("paper/manuscript.tex must be a nonsymlink ordinary file")
    uncommented = "\n".join(
        re.sub(r"(?<!\\)%.*$", "", line)
        for line in path.read_text(encoding="utf-8").splitlines()
    )
    citation_pattern = re.compile(
        r"\\cite[a-zA-Z]*\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]*)\}"
    )
    calls = citation_pattern.findall(uncommented)
    starts = re.findall(r"\\cite[a-zA-Z]*\*?", uncommented)
    if len(calls) != len(starts):
        raise RuntimeError(
            "unparsed manuscript citation command; citation-domain validation fails closed"
        )
    keys: set[str] = set()
    for call in calls:
        call_keys = [key.strip() for key in call.split(",")]
        if not call_keys or any(not key for key in call_keys):
            raise RuntimeError("empty manuscript citation key")
        keys.update(call_keys)
    if not keys:
        raise RuntimeError("no manuscript citation keys found")
    return sorted(keys)


def validate_citations() -> dict[str, Any]:
    bibliography = HERE.parent / "references.bib"
    key_contract_path = HERE.parent / "CITATION_KEY_CONTRACT.json"
    manuscript = HERE.parent / "manuscript.tex"
    key_contract = json.loads(key_contract_path.read_text(encoding="utf-8"))
    observed = sorted(
        re.findall(
            r"^@(?:article|incollection|misc)\{([^,]+),",
            bibliography.read_text(encoding="utf-8"),
            flags=re.MULTILINE,
        )
    )
    expected = sorted(key_contract["canonical_keys"])
    if observed != expected:
        raise RuntimeError(f"bibliography keys differ: observed={observed}, expected={expected}")
    if sha256_file(bibliography) != key_contract["canonical_bibliography_sha256"]:
        raise RuntimeError("bibliography hash differs from citation-key contract")
    placeholder_map = key_contract["frozen_draft_placeholder_map"]
    manuscript_keys = extract_manuscript_citation_keys(manuscript)
    map_domain = sorted(placeholder_map)
    missing_from_map = sorted(set(manuscript_keys) - set(map_domain))
    extra_in_map = sorted(set(map_domain) - set(manuscript_keys))
    if missing_from_map or extra_in_map:
        raise RuntimeError(
            "manuscript citation domain differs from frozen placeholder map: "
            f"missing_from_map={missing_from_map}, extra_in_map={extra_in_map}"
        )
    map_targets = list(placeholder_map.values())
    optional_key = key_contract["optional_unmapped_key"]
    expected_targets = sorted(set(expected) - {optional_key})
    if len(map_targets) != len(set(map_targets)):
        raise RuntimeError("citation placeholder map targets must be unique")
    if sorted(map_targets) != expected_targets:
        raise RuntimeError(
            "citation placeholder targets must equal canonical keys minus optional key"
        )
    return {
        "canonical_key_count": len(observed),
        "canonical_keys": observed,
        "frozen_placeholder_map_count": len(placeholder_map),
        "frozen_placeholder_map_domain": map_domain,
        "key_contract_path": "paper/CITATION_KEY_CONTRACT.json",
        "key_contract_sha256": sha256_file(key_contract_path),
        "manuscript_citation_domain_exact_match": True,
        "manuscript_citation_keys": manuscript_keys,
        "manuscript_citation_keys_extra_in_map": extra_in_map,
        "manuscript_citation_keys_missing_from_map": missing_from_map,
        "manuscript_path": "paper/manuscript.tex",
        "manuscript_sha256": sha256_file(manuscript),
        "references_path": "paper/references.bib",
        "references_sha256": sha256_file(bibliography),
    }


def build_trace(contract: dict[str, Any], outputs: dict[str, Any]) -> dict[str, Any]:
    transformations = {
        "fig1_theorem_architecture": (
            "Arrange the source-proved formal period-one, exact-period-two, epsilon-one "
            "period-three, and quartic statements above a proof-only evidence firewall. "
            "The failed audit is confined to a dashed provenance branch with no theorem arrow."
        ),
        "fig2_weighted_two_term_law": (
            "Map the four solutions of the weight equation to two surviving and two "
            "crossed-out supports; attach each elimination proof, then show the two-term law, "
            "odd-m parity, quartic identity, and open universal-nonvanishing boundary."
        ),
        "fig3_step9_certificate_pipeline": (
            "Map the mandated Step-9 order into seven numbered stages, keeping local identity "
            "(9.14), incoming transfers, and the separate j=0 classification explicit before "
            "the finite H/A/D certificate and open nonvanishing box."
        ),
    }
    locations = {
        "fig1_theorem_architecture": "Sections 1--2, immediately after contribution bullets",
        "fig2_weighted_two_term_law": "Section 4, after weighted-support enumeration",
        "fig3_step9_certificate_pipeline": "Section 5, before the full Step-9 derivation",
    }
    trace_figures = []
    for item in contract["figures"]:
        stem = item["stem"]
        trace_figures.append(
            {
                "caption_contract": item["caption_contract"],
                "generator": {
                    "path": FIGURE_SCRIPTS[stem],
                    "sha256": sha256_file(HERE / FIGURE_SCRIPTS[stem]),
                },
                "label": item["label"],
                "number": item["number"],
                "outputs": {
                    extension: outputs[stem]["files"][extension]["sha256"]
                    for extension in FORMATS
                },
                "planned_location": locations[stem],
                "registered_evidence_used": False,
                "stem": stem,
                "supported_claims": item["supported_claims"],
                "transformation": transformations[stem],
            }
        )
    return {
        "candidate_id": contract["candidate_id"],
        "evidence_mode": contract["evidence_mode"],
        "figures": trace_figures,
        "forbidden_roots_read_or_used": [],
        "generated_utc": "2026-08-16T00:00:00Z",
        "input_bindings": contract["input_bindings"],
        "nonclaims": contract["nonclaims"],
        "schema": "paper12.figure_trace.v1",
        "status": "PASS_PENDING_INDEPENDENT_ASSET_REVIEW",
    }


def publication_asset_paths() -> list[Path]:
    paths = [
        HERE.parent / "CITATION_KEY_CONTRACT.json",
        HERE.parent / "references.bib",
        PROJECT_ROOT / "PAPER_PLAN.md",
        PROJECT_ROOT / "notes" / "CITATION_VERIFICATION.md",
    ]
    paths.extend(
        path
        for path in sorted(HERE.iterdir())
        if path.is_file() and path.name != "ASSET_TREE.json"
    )
    return sorted(set(paths), key=lambda item: str(item))


def relative_asset_path(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def main() -> None:
    contract = load_contract()
    validate_caption_label_contract(contract)
    citation_record = validate_citations()

    outputs: dict[str, Any] = {}
    for stem, generator in FIGURE_SCRIPTS.items():
        files = {
            extension: output_record(HERE / f"{stem}.{extension}")
            for extension in FORMATS
        }
        outputs[stem] = {
            "files": files,
            "generator": generator,
            "generator_sha256": sha256_file(HERE / generator),
        }

    trace = build_trace(contract, outputs)
    write_json(HERE / "FIGURE_TRACE.json", trace)

    generator_names = [
        "build_records.py",
        "figure_data.py",
        "generate_all.py",
        "gen_fig1_theorem_architecture.py",
        "gen_fig2_weighted_two_term_law.py",
        "gen_fig3_step9_certificate_pipeline.py",
        "paper_plot_style.py",
    ]
    documentation_names = [
        "FIGURE_QA.md",
        "PROVENANCE.md",
        "figure_contract.json",
        "latex_includes.tex",
    ]
    manifest = {
        "candidate_id": contract["candidate_id"],
        "caption_label_contract_pass": True,
        "citation_contract": citation_record,
        "determinism": {
            "audit_path": "DETERMINISM_AUDIT.json",
            "audit_sha256": sha256_file(HERE / "DETERMINISM_AUDIT.json"),
            "byte_identical_media_outputs": True,
            "isolated_generation_trees": 2,
        },
        "documentation_hashes": {
            name: sha256_file(HERE / name) for name in documentation_names
        },
        "environment": {
            "matplotlib": matplotlib.__version__,
            "pillow": pillow_version,
            "platform": platform.platform(),
            "python": platform.python_version(),
        },
        "generated_utc": "2026-08-16T00:00:00Z",
        "generator_hashes": {
            name: sha256_file(HERE / name) for name in generator_names
        },
        "independent_asset_pass": False,
        "input_bindings": contract["input_bindings"],
        "outputs": outputs,
        "registered_evidence_used": False,
        "schema": "paper12.figure_manifest.v1",
        "status": "FROZEN_PENDING_INDEPENDENT_ASSET_REVIEW",
        "trace": {
            "path": "FIGURE_TRACE.json",
            "sha256": sha256_file(HERE / "FIGURE_TRACE.json"),
        },
    }
    write_json(HERE / "FIGURE_MANIFEST.json", manifest)

    asset_paths = publication_asset_paths()
    tree = {
        "asset_root": "papers/12-henon-period3-residue",
        "assets": {
            relative_asset_path(path): {
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
            for path in asset_paths
        },
        "excluded_by_design": [
            "paper/manuscript.tex (not edited by the asset author)",
            "paper/figures/ASSET_TREE.json (self)",
            "future independent asset-review files",
            "all code/, preexecution/, results/, and runtime/ trees",
            "all nonallowlisted historical design files",
        ],
        "figure_stems": sorted(FIGURE_SCRIPTS),
        "generated_utc": "2026-08-16T00:00:00Z",
        "included_asset_count": len(asset_paths),
        "independent_asset_pass": False,
        "publication_layer_only": True,
        "registered_evidence_used": False,
        "schema": "paper12.asset_tree.v1",
        "status": "FROZEN_PENDING_INDEPENDENT_ASSET_REVIEW",
    }
    write_json(HERE / "ASSET_TREE.json", tree)

    failures = []
    for stem, record in outputs.items():
        pdf = record["files"]["pdf"]["quality"]
        svg = record["files"]["svg"]["quality"]
        png = record["files"]["png"]["quality"]
        if not (pdf["one_page"] and pdf["vector_only"] and pdf["all_fonts_embedded"]):
            failures.append(f"{stem}: PDF QA")
        if pdf["type3_fonts"] != 0:
            failures.append(f"{stem}: Type 3 font")
        if not (svg["vector_only"] and svg["selectable_text_nodes"] > 0):
            failures.append(f"{stem}: SVG QA")
        if png["dpi_300_tolerance"] != "PASS":
            failures.append(f"{stem}: PNG DPI")
    if failures:
        raise RuntimeError(f"publication QA failure: {failures}")

    print("Paper 12 publication records: PASS_PENDING_INDEPENDENT_ASSET_REVIEW")
    print(f"manifest: {sha256_file(HERE / 'FIGURE_MANIFEST.json')}")
    print(f"trace: {sha256_file(HERE / 'FIGURE_TRACE.json')}")
    print(f"asset tree: {sha256_file(HERE / 'ASSET_TREE.json')}")


if __name__ == "__main__":
    main()
