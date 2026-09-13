#!/usr/bin/env bash
# Reproducible build for the generic single-column research record.
# Requires: LuaLaTeX, BibTeX, pdfinfo.
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"
mkdir -p build

lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=build manuscript.tex
BIBINPUTS="$script_dir:" bibtex build/manuscript
lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=build manuscript.tex
lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=build manuscript.tex

cp build/manuscript.pdf manuscript.pdf
pdfinfo manuscript.pdf
