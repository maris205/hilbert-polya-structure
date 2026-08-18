#!/usr/bin/env bash
set -euo pipefail

paper_root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)"
cd "$paper_root"

export SOURCE_DATE_EPOCH=1787011200
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C

clean_aux() {
  rm -f -- main.aux main.bbl main.blg main.log main.out main.toc \
    main.fdb_latexmk main.fls main.synctex.gz
}

if [[ "${1:-}" == "--clean" ]]; then
  clean_aux
  rm -f -- main.pdf
  exit 0
fi
if [[ $# -ne 0 ]]; then
  printf '%s\n' 'usage: scripts/build_paper.sh [--clean]' >&2
  exit 64
fi

clean_aux
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex

test -s main.pdf
printf 'BUILT %s\n' "$paper_root/main.pdf"
