#!/usr/bin/env bash
# One fresh source-only build for a manuscript review; never terminal QA.
set -euo pipefail
source_dir="${1:?absolute frozen source directory}"
target_pdf="${2:?absolute frozen PDF}"
review_dir="${3:?absolute review directory}"
test -f "$source_dir/main.tex"
test -f "$source_dir/references.bib"
test -f "$target_pdf"
test ! -e "$review_dir/cold_build"
mkdir -p "$review_dir"
review_stage="$(mktemp -d "$review_dir/.review_build.XXXXXX")"
cp "$source_dir/main.tex" "$review_stage/main.tex"
cp "$source_dir/references.bib" "$review_stage/references.bib"
export SOURCE_DATE_EPOCH=1704067200 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
(
  cd "$review_stage"
  pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass1.stdout
  bibtex main > bibtex.stdout
  pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass2.stdout
  pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass3.stdout
)
cmp "$review_stage/main.pdf" "$target_pdf"
mv "$review_stage" "$review_dir/cold_build"
mkdir "$review_dir/visual"
pdftoppm -r 120 -png "$target_pdf" "$review_dir/visual/page"
pdfinfo "$target_pdf"
pdffonts "$target_pdf"
