#!/usr/bin/env bash
# Scoped modular-paper adapter; a build is not a visual or mathematical review.
# Derived from the prior batch's source-only shell sequence. No old file changes.
set -euo pipefail
source_dir="${1:?absolute source directory}"
build_dir="${2:?absolute NEW build directory}"
expected_pdf="${3:-}"
test -d "$source_dir/sections"
test -f "$source_dir/main.tex"
test -f "$source_dir/math_commands.tex"
test -f "$source_dir/references.bib"
test ! -e "$build_dir"
build_parent="$(dirname "$build_dir")"
mkdir -p "$build_parent"
build_stage="$(mktemp -d "$build_parent/.build.XXXXXX")"
cp "$source_dir/main.tex" "$source_dir/math_commands.tex" \
   "$source_dir/references.bib" "$build_stage/"
cp -R "$source_dir/sections" "$build_stage/sections"
export SOURCE_DATE_EPOCH=1704067200 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
(
  cd "$build_stage"
  sha256sum main.tex math_commands.tex references.bib sections/*.tex > SOURCE_INPUTS.sha256
  pdflatex --version > ENGINE.txt
  bibtex --version > BIBTEX_ENGINE.txt
  printf '%s\n' 'SOURCE_DATE_EPOCH=1704067200' 'FORCE_SOURCE_DATE=1' \
     'TZ=UTC' 'LC_ALL=C' > BUILD_ENVIRONMENT.txt
  pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass1.stdout
  bibtex main > bibtex.stdout
  pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass2.stdout
  pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass3.stdout
  pdfinfo main.pdf > PDFINFO.txt
  pdffonts main.pdf > FONTS.txt
  pdftotext main.pdf main.txt
  if rg 'undefined|Overfull|Warning' main.log > DIAGNOSTICS.txt; then
    printf '%s\n' 'Final log contains diagnostics; inspect DIAGNOSTICS.txt.' >&2
  fi
  sha256sum main.pdf > PDF.sha256
)
if [[ -n "$expected_pdf" ]]; then
  cmp "$build_stage/main.pdf" "$expected_pdf"
fi
mv "$build_stage" "$build_dir"
printf 'SOURCE_ONLY_BUILD_COMPLETE %s\n' "$build_dir"
sha256sum "$build_dir/main.pdf"
