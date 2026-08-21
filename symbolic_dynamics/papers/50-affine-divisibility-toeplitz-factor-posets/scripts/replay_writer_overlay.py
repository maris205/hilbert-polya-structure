#!/usr/bin/env python3
"""Read-only, two-lane fixed-epoch replay of the minimal P50 overlay."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


EXPECTED = {
    "pdf": "bf0c9ea39d55596fab6d873a4062a836451c0a65113d2d245b0a7d94e3243736",
    "log": "040ce1a1306948b86a5484760ef8c761ee6c8fcdecff21f8767963264bb27a93",
    "bbl": "c9325f05ff00a68e8522fdd841c055945e9087102a3f93552cefbf1ce5174dde",
    "table2": "73562e6763d2df25826aa3fea56f5d01402a5539c0570ca4887e1bb128b5ba5c",
    "preview_pdf": "520cb7814bc0bffab4b63f2800260998b9bcd843856cfeb599f7518369eee335",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_root(path: Path) -> Path:
    if not path.is_absolute() or path.is_symlink() or path.resolve(strict=True) != path or not path.is_dir():
        raise SystemExit("ROOT_INVALID")
    return path


def environment() -> dict[str, str]:
    return {
        "FORCE_SOURCE_DATE": "1",
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "SOURCE_DATE_EPOCH": "1787270400",
        "TZ": "UTC",
    }


def citations(lane: Path) -> dict[str, Any]:
    bib = (lane / "paper/references.bib").read_text(encoding="utf-8")
    aux = (lane / "paper/main.aux").read_text(encoding="utf-8")
    bbl = (lane / "paper/main.bbl").read_text(encoding="utf-8")
    bib_keys = set(re.findall(r"^@[A-Za-z]+\{([^,]+),", bib, re.M))
    cited = set()
    for group in re.findall(r"\\citation\{([^}]*)\}", aux):
        cited.update(key for key in group.split(",") if key)
    bbl_keys = set(re.findall(r"\\bibitem\[[^]]*\]\{([^}]+)\}", bbl))
    if not (bib_keys == cited == bbl_keys):
        raise SystemExit("CITATION_CLOSURE")
    return {"bib": len(bib_keys), "bbl": len(bbl_keys), "cited": len(cited), "keys": sorted(cited)}


def run_lane(source: Path, destination: Path) -> dict[str, Any]:
    shutil.copytree(source, destination, symlinks=True)
    for directory in [destination, *(path for path in destination.rglob("*") if path.is_dir())]:
        os.chmod(directory, 0o755)
    for path in (path for path in destination.rglob("*") if path.is_file() and not path.is_symlink()):
        os.chmod(path, 0o644)
    (destination / "paper/main.pdf").unlink()
    env = environment()
    table = subprocess.run(
        [os.sys.executable, "-I", "-B", str(destination / "figures/gen_diagnostic_table.py"),
         "--input", str(destination / "figures/diagnostic_receipt.json"),
         "--output", str(destination / "figures/table2_diagnostics.tex")],
        cwd="/", env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=60, check=False,
    )
    if table.returncode or table.stderr:
        raise SystemExit("TABLE_REPLAY")
    for _pass in range(2):
        preview = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "preview.tex"],
            cwd=destination / "figures", env=env, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, timeout=120, check=False,
        )
        if preview.returncode or preview.stderr:
            raise SystemExit("PREVIEW_REPLAY")
    build = subprocess.run(
        ["bash", "build_fixed.sh"], cwd=destination / "paper", env=env,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=300, check=False,
    )
    if build.returncode or build.stderr:
        raise SystemExit("BUILD_REPLAY")
    artifacts = {
        "pdf": sha(destination / "paper/main.pdf"),
        "log": sha(destination / "paper/main.log"),
        "bbl": sha(destination / "paper/main.bbl"),
        "table2": sha(destination / "figures/table2_diagnostics.tex"),
        "preview_pdf": sha(destination / "figures/preview.pdf"),
    }
    if artifacts != EXPECTED:
        raise SystemExit("ARTIFACT_HASH")
    log = (destination / "paper/main.log").read_text(encoding="utf-8", errors="strict")
    diagnostics = re.findall(r"(?:LaTeX Warning|Package .+ Warning|Class .+ Warning|Warning:|undefined|multiply defined|Overfull|Underfull|^!|error:)", log, re.I | re.M)
    if diagnostics:
        raise SystemExit("LOG_DIAGNOSTICS")
    preview_log = (destination / "figures/preview.log").read_text(encoding="utf-8", errors="strict")
    preview_diagnostics = re.findall(r"(?:LaTeX Warning|Package .+ Warning|Class .+ Warning|Warning:|undefined|multiply defined|Overfull|Underfull|^!|error:)", preview_log, re.I | re.M)
    if preview_diagnostics:
        raise SystemExit("PREVIEW_LOG_DIAGNOSTICS")
    pdf = subprocess.run(
        [os.sys.executable, "-I", "-B", str(destination / "scripts/check_pdf_qa.py")],
        cwd="/", env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=120, check=False,
    )
    if pdf.returncode or pdf.stderr:
        raise SystemExit("PDF_QA")
    pdf_qa = json.loads(pdf.stdout)
    if pdf_qa.get("status") != "PASS" or pdf_qa.get("pdf_sha256") != EXPECTED["pdf"] \
            or any(record["illegal"]["total"] for record in pdf_qa["extractors"].values()):
        raise SystemExit("PDF_QA_RESULT")
    c4 = subprocess.run(
        [os.sys.executable, "-I", "-B", str(destination / "scripts/check_c4_partitions.py")],
        cwd="/", env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=60, check=False,
    )
    if c4.returncode or c4.stderr or b'"status": "PASS"' not in c4.stdout:
        raise SystemExit("C4_REPLAY")
    caches = [path.relative_to(destination).as_posix() for path in destination.rglob("*") if path.name == "__pycache__" or path.suffix in {".pyc", ".pyo"}]
    if caches:
        raise SystemExit("CACHE_CREATED")
    return {
        "artifact_hashes": artifacts,
        "c4_stdout_sha256": hashlib.sha256(c4.stdout).hexdigest(),
        "citation_closure": citations(destination),
        "log_diagnostic_count": 0,
        "preview_log_diagnostic_count": 0,
        "pdf_qa_sha256": hashlib.sha256(canonical(pdf_qa)).hexdigest(),
        "six_extractor_illegal_count": 0,
        "strict_raw_bbox_xml": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True, type=Path)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--record", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = strict_root(args.root)
    if sha(root / "paper/main.pdf") != EXPECTED["pdf"]:
        raise SystemExit("ACTIVE_PDF")
    initial = json.loads((root / "evidence/FRESH_AB_REPLAY.json").read_text(encoding="ascii"))
    for relative, expected in initial["source_hashes"].items():
        if sha(root / relative) != expected:
            raise SystemExit(f"SOURCE_HASH:{relative}")
    with tempfile.TemporaryDirectory(prefix="p50_final_overlay_replay_") as temporary:
        base = Path(temporary)
        lanes = {label: run_lane(root, base / f"lane_{label}") for label in ("a", "b")}
    if lanes["a"] != lanes["b"]:
        raise SystemExit("LANE_MISMATCH")
    result = {
        "active_pdf_sha256": EXPECTED["pdf"],
        "evidence_boundary": "Finite build, extraction, and C4 checks are reproducibility controls, not proofs of the manuscript's infinite claims.",
        "fixed_source_date_epoch": 1787270400,
        "fresh_lane_count": 2,
        "lanes": lanes,
        "producer_role": "P50_WRITER_REPLAY",
        "schema": "paper50.final-writer-overlay-replay.v1",
        "source_file_count": len(initial["source_hashes"]),
        "status": "PASS",
    }
    raw = canonical(result)
    target = root / "evidence/FINAL_OVERLAY_REPLAY.json"
    if args.record:
        if os.path.lexists(target):
            raise SystemExit("REPLAY_RECEIPT_EXISTS")
        descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o644)
        try:
            os.fchmod(descriptor, 0o644)
            offset = 0
            while offset < len(raw):
                offset += os.write(descriptor, raw[offset:])
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        print(f"RECORDED replay_sha256={hashlib.sha256(raw).hexdigest()}")
    else:
        if target.is_symlink() or not target.is_file() or target.read_bytes() != raw:
            raise SystemExit("REPLAY_RECEIPT_MISMATCH")
        print(f"PASS replay_sha256={hashlib.sha256(raw).hexdigest()}")


if __name__ == "__main__":
    main()
