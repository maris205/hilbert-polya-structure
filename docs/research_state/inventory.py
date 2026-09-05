#!/usr/bin/env python3
"""Read-only artifact inventory. Presence and hashes are not proof/review verdicts."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("mirror", type=Path)
    args = parser.parse_args()
    workspace, mirror = args.workspace.resolve(), args.mirror.resolve()
    tracked = set(subprocess.check_output(
        ["git", "-C", str(mirror), "ls-files", "-z"]
    ).decode().split("\0"))
    rows = []
    for directory in (workspace / "papers").iterdir():
        match = re.match(r"^(\d+)-", directory.name)
        if not directory.is_dir() or not match:
            continue
        relative = directory.relative_to(workspace)
        copies = []
        for prefix in (Path("symbolic_dynamics"), Path(".")):
            candidate = prefix / relative
            if any(p.startswith(candidate.as_posix() + "/") for p in tracked):
                copies.append(candidate.as_posix())
        primary_pdfs = [directory / "main.pdf"]
        if not primary_pdfs[0].is_file():
            primary_pdfs = sorted(directory.glob("paper/*.pdf"))
        primary_pdfs = [p for p in primary_pdfs if p.is_file()]
        rows.append({
            "paper_number": int(match.group(1)),
            "workspace_path": relative.as_posix(),
            "readme_present": (directory / "README.md").is_file(),
            "main_tex_present": (directory / "main.tex").is_file(),
            "primary_pdf_candidates": [{
                "workspace_path": pdf.relative_to(workspace).as_posix(),
                "sha256": digest(pdf),
                "matching_tracked_mirror_paths": [
                    (Path(copy) / pdf.relative_to(directory)).as_posix()
                    for copy in copies
                    if (Path(copy) / pdf.relative_to(directory)).as_posix() in tracked
                    and (mirror / copy / pdf.relative_to(directory)).is_file()
                    and digest(mirror / copy / pdf.relative_to(directory)) == digest(pdf)
                ],
            } for pdf in primary_pdfs],
            "tracked_mirror_directories": copies,
        })
    rows.sort(key=lambda row: (row["paper_number"], row["workspace_path"]))
    counts = Counter(row["paper_number"] for row in rows)
    current = workspace / "docs/papers197_201_sequence"
    files = sorted(p for p in current.rglob("*") if p.is_file()
                   and "__pycache__" not in p.parts and p.suffix != ".pyc")
    result = {
        "schema": "artifact-presence-v1",
        "meaning": "Read-only presence/hash census; not a completed-paper or validated-subclass count.",
        "workspace": str(workspace), "mirror": str(mirror),
        "git_baseline": subprocess.check_output(
            ["git", "-C", str(mirror), "rev-parse", "HEAD"]
        ).decode().strip(),
        "numbered_directory_count": len(rows),
        "distinct_paper_numbers": len(counts),
        "highest_number": max(counts),
        "missing_numbers_through_highest": [n for n in range(1, max(counts) + 1) if n not in counts],
        "duplicate_numbers": {str(n): count for n, count in sorted(counts.items()) if count > 1},
        "directories_with_primary_pdf_candidates": sum(bool(row["primary_pdf_candidates"]) for row in rows),
        "papers": rows,
        "current_batch_file_count": len(files),
        "current_batch_files": [{"path": p.relative_to(workspace).as_posix(),
                                 "sha256": digest(p)} for p in files],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
