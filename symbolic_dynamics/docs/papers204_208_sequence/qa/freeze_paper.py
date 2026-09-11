#!/usr/bin/env python3
"""Physical, no-overwrite freeze of this batch's documented paper inputs."""
import argparse
import hashlib
from pathlib import Path
import shutil


REQUIRED = (
    "main.tex", "math_commands.tex", "references.bib", "main.pdf",
    "PROOF_PACKAGE.md", "verify.py", "CANONICAL.json", "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md", "CLAIMS_EVIDENCE.md", "SOURCE_AUDIT.md", "README.md",
    "AUTHOR_REPLAY.md", "ROUND0_BUILD_REPORT.md", "INTEGRITY_REVIEW.md",
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paper", type=Path)
    parser.add_argument("round", type=int, choices=(0, 1, 2))
    args = parser.parse_args()
    paper = args.paper.resolve(strict=True)
    target = paper / f"frozen_round{args.round}"
    if target.exists():
        raise SystemExit(f"Refusing existing freeze: {target}")
    sources = [paper / name for name in REQUIRED]
    sources += sorted((paper / "sections").glob("*.tex"))
    sources += sorted((paper / "author_replay").glob("*.stdout"))
    if not (paper / "sections/00_abstract.tex").is_file():
        raise SystemExit("Missing modular sections")
    if len(list((paper / "author_replay").glob("*.stdout"))) != 2:
        raise SystemExit("Expected exactly two complete author replay outputs")
    for source in sources:
        if not source.is_file() or source.is_symlink():
            raise SystemExit(f"Missing/nonregular source: {source}")
    if args.round and not (paper / f"frozen_round{args.round - 1}").is_dir():
        raise SystemExit("Prior freeze absent; review delta remains required separately")
    target.mkdir()
    for source in sources:
        dest = target / source.relative_to(paper)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
    paths = sorted(p for p in target.rglob("*") if p.is_file())
    lines = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(target).as_posix()}\n" for p in paths]
    (target / "SHA256SUMS").write_text("".join(lines), encoding="utf-8")
    print(f"FROZEN {target} files={len(paths)}")
    print("Review acceptance is checked separately; this command does not grant it.")


if __name__ == "__main__":
    main()
