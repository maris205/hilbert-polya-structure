#!/usr/bin/env bash
set -euo pipefail

paper_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$paper_dir"

export SOURCE_DATE_EPOCH=1786665600
export FORCE_SOURCE_DATE=1
export TZ=UTC

if command -v latexmk >/dev/null 2>&1; then
  latexmk -C manuscript.tex
  latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error manuscript.tex
else
  rm -f manuscript.aux manuscript.bbl manuscript.blg manuscript.log \
    manuscript.out manuscript.fdb_latexmk manuscript.fls
  pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
  bibtex manuscript
  pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
  pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
fi
