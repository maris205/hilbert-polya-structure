#!/usr/bin/env bash
set -euo pipefail

paper_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$paper_dir"

export SOURCE_DATE_EPOCH=1786752000
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C

rm -f manuscript.aux manuscript.bbl manuscript.blg manuscript.log \
  manuscript.out manuscript.fdb_latexmk manuscript.fls manuscript.toc \
  manuscript.synctex.gz manuscript.pdf

pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
