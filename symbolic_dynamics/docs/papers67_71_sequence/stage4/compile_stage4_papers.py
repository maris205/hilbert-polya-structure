#!/usr/bin/env python3
"""Compile the five Stage-4 LaTeX papers and persist one exact trace each."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPERS = (
    "67-multiplicative-plaquette-matroid-complexity",
    "68-complete-bipartite-homshift-conjugacies",
    "69-orientation-sensitive-surface-flat-sft",
    "70-weighted-heisenberg-congruence-nullities",
    "71-zip-shift-degree-pressure",
)


def run(command: list[str], cwd: Path) -> tuple[int, str]:
    completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    rendered = "$ " + " ".join(command) + "\n"
    rendered += completed.stdout
    if completed.stderr:
        rendered += "\n[stderr]\n" + completed.stderr
    rendered += f"\n[exit {completed.returncode}]\n"
    return completed.returncode, rendered


def main() -> None:
    latexmk = shutil.which("latexmk")
    for slug in PAPERS:
        paper = ROOT / "papers" / slug
        traces = []
        if latexmk:
            commands = [
                [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
            ]
        else:
            commands = [
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                ["bibtex", "main"],
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
            ]
            traces.append("latexmk: unavailable; using documented fallback chain\n")
        for command in commands:
            code, trace = run(command, paper)
            traces.append(trace)
            if code != 0:
                out = paper / "stage4" / "FINAL_COMPILE_TRACE.txt"
                out.write_text("\n".join(traces), encoding="utf-8")
                raise SystemExit(f"{slug}: compile command failed: {command}")
        if not (paper / "main.pdf").is_file():
            raise SystemExit(f"{slug}: compiler returned success without main.pdf")
        out = paper / "stage4" / "FINAL_COMPILE_TRACE.txt"
        out.write_text("\n".join(traces), encoding="utf-8")
        print(f"{slug}: PASS")


if __name__ == "__main__":
    main()
