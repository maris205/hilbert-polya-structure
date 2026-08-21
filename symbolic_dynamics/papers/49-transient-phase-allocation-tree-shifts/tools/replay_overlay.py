#!/usr/bin/env python3
"""Rebuild the final Paper 49 overlay in two isolated lanes.

The overlay is never modified except for the five evidence files created by an
explicit first ``--write`` invocation.  ``--check`` only writes below the
caller-supplied scratch directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
from typing import Any


OVERLAY = Path(__file__).resolve().parents[1]
EVIDENCE = OVERLAY / "evidence"
ACTIVE_PDF_SHA = "aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4"
ACTIVE_BBL_SHA = "7b76b4191ede10ddabdf6cca40d0dfba2f2878557240f1896238a7cab6ff0bfc"
SOURCE_INPUT_SHA = "cf8ae3ee10fd798d937bed725b6a55ad0635e5dcdfdb29fb0c1070f2290a63f9"
FIGURE_FILES = [
    "figures/data/fig2_balanced.csv",
    "figures/data/fig2_exact.csv",
    "figures/data/fig3_p2.csv",
    "figures/data/figure_data_hashes.json",
    "figures/data/figure_provenance.json",
]
EVIDENCE_FILES = [
    "FINAL_BIBLIOGRAPHY.bbl",
    "FINAL_BUILD_RECEIPT.txt",
    "FINAL_COMPILE_NORMALIZED.log",
    "INDEPENDENT_REPLAY.json",
    "PDF_QA.json",
]
PYTHON = str(Path(sys.executable).resolve())
SAFE_PATH = os.pathsep.join(
    [
        str(Path(PYTHON).parent),
        "/usr/local/bin",
        "/usr/bin",
        "/bin",
    ]
)


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def file_sha(path: Path) -> str:
    return sha(path.read_bytes())


def assert_clean_tree(root: Path) -> None:
    root_info = os.lstat(root)
    if not stat.S_ISDIR(root_info.st_mode) or stat.S_ISLNK(root_info.st_mode):
        raise RuntimeError("unsafe overlay root")
    for path in sorted(root.rglob("*")):
        info = os.lstat(path)
        relative = path.relative_to(root).as_posix()
        if stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o755:
                raise RuntimeError(f"directory mode is not 0755: {relative}")
        elif stat.S_ISREG(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o644:
                raise RuntimeError(f"file mode is not 0644: {relative}")
            if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
                raise RuntimeError(f"cache file in overlay: {relative}")
            if path.suffix in {".aux", ".blg", ".out", ".toc", ".synctex"}:
                raise RuntimeError(f"temporary build artifact in overlay: {relative}")
            if path.suffix == ".log" and relative != "evidence/FINAL_COMPILE_NORMALIZED.log":
                raise RuntimeError(f"unapproved log artifact in overlay: {relative}")
        else:
            raise RuntimeError(f"nonregular overlay node: {relative}")


def copy_overlay(destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        raise RuntimeError(f"scratch lane already exists: {destination}")
    destination.mkdir(mode=0o755, parents=True)
    for path in sorted(OVERLAY.rglob("*")):
        relative = path.relative_to(OVERLAY)
        target = destination / relative
        info = os.lstat(path)
        if stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode):
            target.mkdir(mode=0o755)
        elif stat.S_ISREG(info.st_mode):
            shutil.copyfile(path, target, follow_symlinks=False)
            os.chmod(target, 0o644)
        else:
            raise RuntimeError(f"unsafe overlay node while copying: {relative}")


def run(args: list[str], *, cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(args, cwd=cwd, env=env, check=True, capture_output=True)


def neutral_pdf_receipt(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="ascii"))
    value.pop("pdf", None)
    if value.get("status") != "PASS" or value.get("pdf_sha256") != ACTIVE_PDF_SHA:
        raise RuntimeError("PDF hard-gate receipt mismatch")
    return value


def normalize_log(raw: bytes, lane: Path) -> bytes:
    text = raw.decode("utf-8", errors="strict")
    # TeX wraps long absolute paths according to their pre-normalization
    # length, and its terminal memory-use counters include those path lengths.
    # The diagnostic tail is not a build result.  Removing it and canonicalizing
    # whitespace yields a lane-neutral compile transcript while warnings,
    # errors, loaded files, page output, and PDF statistics remain bound.
    text = text.split("Here is how much of TeX's memory you used:", 1)[0]
    text = re.sub(r"\s+", "", text)
    text = text.replace(str(lane), "<LANE>")
    return (text + "\n").encode("utf-8")


def clean_lane_env(lane: Path, scratch: Path) -> dict[str, str]:
    """Return a deterministic child environment with no caller Python hooks."""
    lane_home = scratch / f"{lane.name}_home"
    lane_tmp = scratch / f"{lane.name}_tmp"
    lane_cache = lane_home / ".cache"
    lane_home.mkdir(mode=0o755)
    lane_tmp.mkdir(mode=0o755)
    lane_cache.mkdir(mode=0o755)
    env = {
        "FORCE_SOURCE_DATE": "1",
        "HOME": str(lane_home),
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": SAFE_PATH,
        "PYTHONDONTWRITEBYTECODE": "1",
        "SOURCE_DATE_EPOCH": "1787270400",
        "TMPDIR": str(lane_tmp),
        "TZ": "UTC",
        "XDG_CACHE_HOME": str(lane_cache),
    }
    # These are intentionally absent from the whitelist.  Keep the explicit
    # removals as an executable assertion of the hostile-environment contract.
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    return env


def build_lane(lane: Path, scratch: Path) -> dict[str, Any]:
    env = clean_lane_env(lane, scratch)
    run(
        [PYTHON, "-I", "-B", str(lane / "tools/generate_figure_data.py")],
        cwd=lane,
        env=env,
    )
    figure_verify = run(
        [PYTHON, "-I", "-B", str(lane / "tools/verify_figure_data.py")],
        cwd=lane,
        env=env,
    )
    if figure_verify.stdout != b"FIGURE_DATA_OK assertions=153\n":
        raise RuntimeError(f"figure verification mismatch: {figure_verify.stdout!r}")
    for relative in FIGURE_FILES:
        if (lane / relative).read_bytes() != (OVERLAY / relative).read_bytes():
            raise RuntimeError(f"regenerated figure evidence differs: {relative}")

    build = lane / "replay_build"
    build_result = run(
        ["/usr/bin/bash", str(lane / "tools/build_paper.sh"), str(build)],
        cwd=lane,
        env=env,
    )
    if b"BUILD_OK pages=19" not in build_result.stdout:
        raise RuntimeError("build success sentinel missing")
    pdf = build / "main.pdf"
    if file_sha(pdf) != ACTIVE_PDF_SHA or pdf.read_bytes() != (OVERLAY / "main.pdf").read_bytes():
        raise RuntimeError("rebuilt PDF differs from active PDF")
    bbl = build / "main.bbl"
    if file_sha(bbl) != ACTIVE_BBL_SHA:
        raise RuntimeError("bibliography output mismatch")
    receipt = (build / "BUILD_RECEIPT.txt").read_bytes()
    receipt_text = receipt.decode("ascii")
    if "pages=19\n" not in receipt_text or "warning_lines=0\n" not in receipt_text:
        raise RuntimeError("build receipt page/warning mismatch")

    streams = scratch / f"{lane.name}_pdf_streams"
    qa_path = scratch / f"{lane.name}_pdf_qa.json"
    qa_result = run(
        [
            PYTHON,
            "-I",
            "-B",
            str(lane / "tools/verify_pdf.py"),
            str(pdf),
            str(streams),
            str(qa_path),
        ],
        cwd=lane,
        env=env,
    )
    if b"PDF_HARDGATE_PASS pages=19 fonts=33 extractors=6" not in qa_result.stdout:
        raise RuntimeError("PDF hard-gate success sentinel missing")
    qa = neutral_pdf_receipt(qa_path)
    return {
        "bbl": bbl.read_bytes(),
        "build_receipt": receipt,
        "figure_assertions": 153,
        "figure_hashes": {relative: file_sha(lane / relative) for relative in FIGURE_FILES},
        "normalized_log": normalize_log((build / "main.log").read_bytes(), lane),
        "pdf_qa": qa,
        "pdf_sha256": file_sha(pdf),
        "source_input_sha256": file_sha(lane / "inputs/level_l.json"),
    }


def exclusive_write(path: Path, raw: bytes) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        os.write(descriptor, raw)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def expected_outputs(scratch: Path) -> dict[str, bytes]:
    if scratch.exists() or scratch.is_symlink():
        raise RuntimeError("scratch path must not exist")
    scratch.mkdir(mode=0o755, parents=True)
    lane_a = scratch / "lane_a"
    lane_b = scratch / "lane_b"
    copy_overlay(lane_a)
    copy_overlay(lane_b)
    a = build_lane(lane_a, scratch)
    b = build_lane(lane_b, scratch)
    for key in (
        "bbl",
        "build_receipt",
        "figure_assertions",
        "figure_hashes",
        "normalized_log",
        "pdf_qa",
        "pdf_sha256",
        "source_input_sha256",
    ):
        if a[key] != b[key]:
            raise RuntimeError(f"fresh lane mismatch: {key}")
    if a["source_input_sha256"] != SOURCE_INPUT_SHA:
        raise RuntimeError("bundled frozen input mismatch")
    if a["pdf_sha256"] != ACTIVE_PDF_SHA:
        raise RuntimeError("active PDF mismatch")

    qa = {
        "payload": a["pdf_qa"],
        "schema": "p49-final-writer-path-neutral-pdf-qa-v1",
        "status": "PASS",
    }
    replay = {
        "payload": {
            "active_pdf_sha256": ACTIVE_PDF_SHA,
            "bibliography_sha256": sha(a["bbl"]),
            "build_receipt_sha256": sha(a["build_receipt"]),
            "figure_assertions_per_lane": 153,
            "figure_hashes": a["figure_hashes"],
            "fresh_lane_count": 2,
            "fresh_lanes_byte_exact": True,
            "normalized_compile_log_sha256": sha(a["normalized_log"]),
            "pdf_qa_sha256": sha(canonical(qa)),
            "source_input_sha256": SOURCE_INPUT_SHA,
        },
        "schema": "p49-final-writer-independent-replay-v1",
        "status": "PASS",
    }
    return {
        "FINAL_BIBLIOGRAPHY.bbl": a["bbl"],
        "FINAL_BUILD_RECEIPT.txt": a["build_receipt"],
        "FINAL_COMPILE_NORMALIZED.log": a["normalized_log"],
        "INDEPENDENT_REPLAY.json": canonical(replay),
        "PDF_QA.json": canonical(qa),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    parser.add_argument("--scratch", type=Path, required=True)
    args = parser.parse_args()
    assert_clean_tree(OVERLAY)
    expected = expected_outputs(args.scratch)
    if args.write:
        for name in EVIDENCE_FILES:
            exclusive_write(EVIDENCE / name, expected[name])
    else:
        for name in EVIDENCE_FILES:
            if (EVIDENCE / name).read_bytes() != expected[name]:
                raise RuntimeError(f"replay evidence mismatch: {name}")
    print(
        "OVERLAY_REPLAY_PASS lanes=2 figures=153 pdf_pages=19 fonts=33 "
        f"pdf_sha256={ACTIVE_PDF_SHA}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
