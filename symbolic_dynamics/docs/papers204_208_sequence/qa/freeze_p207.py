#!/usr/bin/env python3
"""Physical no-overwrite P207 freeze with its complete author evidence tree.

Disclosed schema adapter: the existing generic freeze_paper.py is unchanged.
P207 has a finite proof certificate and nested author execution provenance;
freeze its recorder, receipt, seal, original streams and source snapshots too.
Review acceptance remains an external lifecycle gate, not this tool's verdict.
"""
import argparse
from hashlib import sha256
from pathlib import Path
import shutil


REQUIRED = (
    "main.tex", "math_commands.tex", "references.bib", "main.pdf",
    "PROOF_PACKAGE.md", "verify.py", "CANONICAL.json", "record_author.py",
    "PAPER_PLAN.md", "NARRATIVE_REPORT.md", "CLAIMS_EVIDENCE.md",
    "SOURCE_AUDIT.md", "README.md", "AUTHOR_EXECUTION.md", "AUTHOR_REPLAY.md",
    "ROUND0_BUILD_REPORT.md", "INTEGRITY_REVIEW.md",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper", type=Path)
    parser.add_argument("round", type=int, choices=(0, 1, 2))
    args = parser.parse_args()
    paper = args.paper.resolve(strict=True)
    if paper.name != "207-upper-neighbor-rank-dynamics":
        raise SystemExit("adapter is scoped to P207")
    target = paper / f"frozen_round{args.round}"
    if target.exists():
        raise SystemExit("refusing existing physical freeze")
    if args.round and not (paper / f"frozen_round{args.round - 1}/SHA256SUMS").is_file():
        raise SystemExit("prior freeze absent")
    sources = [paper / name for name in REQUIRED]
    sources += sorted((paper / "sections").glob("*.tex"))
    sources += sorted(path for path in (paper / "author_replay").rglob("*") if path.is_file())
    if len(sources) != len(set(sources)):
        raise SystemExit("duplicate freeze input")
    for path in sources:
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"missing/nonregular input: {path}")
    if not all((paper / f"author_replay/{label}.stdout").is_file() for label in ("run1", "run2")):
        raise SystemExit("flat canonical pair absent")
    original = {path.relative_to(paper).as_posix(): sha256(path.read_bytes()).hexdigest() for path in sources}
    target.mkdir()
    for source in sources:
        dest = target / source.relative_to(paper)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
    copied = {path.relative_to(target).as_posix(): sha256(path.read_bytes()).hexdigest()
              for path in target.rglob("*") if path.is_file()}
    if copied != original:
        raise SystemExit("physical freeze byte mismatch; preserve failed copy")
    (target / "SHA256SUMS").write_text("".join(f"{digest}  {relative}\n" for relative, digest in sorted(copied.items())))
    print(f"FROZEN {target} files={len(copied)}; review acceptance is not granted by this copy tool")


if __name__ == "__main__":
    main()
