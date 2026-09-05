#!/usr/bin/env bash
set -euo pipefail
review_dir="$(cd "$(dirname "$0")/.." && pwd)"
project_dir="$(cd "$review_dir/../../../.." && pwd)"
build_dir="$review_dir/qa/cold_source"
test -d "$build_dir"
test -z "$(find "$build_dir" -mindepth 1 -maxdepth 1 -print -quit)"
cp "$project_dir/papers/202-ternary-ordered-reset/frozen_round0/main.tex" "$build_dir/main.tex"
cp "$project_dir/papers/202-ternary-ordered-reset/frozen_round0/references.bib" "$build_dir/references.bib"
cd "$build_dir"
pdflatex -interaction=nonstopmode -halt-on-error main.tex > pdflatex1.stdout
bibtex main > bibtex.stdout
pdflatex -interaction=nonstopmode -halt-on-error main.tex > pdflatex2.stdout
pdflatex -interaction=nonstopmode -halt-on-error main.tex > pdflatex3.stdout
cmp main.pdf "$project_dir/papers/202-ternary-ordered-reset/frozen_round0/main.pdf"
pdfinfo main.pdf > pdfinfo.txt
pdffonts main.pdf > pdffonts.txt
pdftotext -layout main.pdf main.txt
pdftoppm -png -r 110 main.pdf page > pdftoppm.stdout 2> pdftoppm.stderr
sha256sum main.tex references.bib main.pdf
if rg -n 'Warning|Overfull|Underfull|undefined|Error|Citation' main.log main.blg; then
  exit 1
fi
