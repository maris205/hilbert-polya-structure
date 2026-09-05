#!/usr/bin/env bash
# Deterministic, source-only author build into a new explicit output directory.
set -euo pipefail
paper_source="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
paper_output="${1:?usage: BUILD.sh NEW_ABSOLUTE_OUTPUT_DIRECTORY}"
case "$paper_output" in /*) ;; *) exit 2 ;; esac
test ! -e "$paper_output"
mkdir -p "$paper_output"
cp "$paper_source/main.tex" "$paper_output/main.tex"
cp "$paper_source/references.bib" "$paper_output/references.bib"
export SOURCE_DATE_EPOCH=1704067200 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
cd "$paper_output"
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass1.stdout
bibtex main > bibtex.stdout
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass2.stdout
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass3.stdout
pdfinfo main.pdf
pdffonts main.pdf
