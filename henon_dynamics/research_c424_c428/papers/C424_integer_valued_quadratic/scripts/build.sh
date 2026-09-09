#!/usr/bin/env bash
set -euo pipefail
paper_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
cd -- "$paper_dir"
build_dir=${1:-build/round0}
case "$build_dir" in
  build/*) ;;
  *) echo "Build output must be a named directory under build/." >&2; exit 2 ;;
esac
if [[ -e "$build_dir/latexmk.console.log" ]]; then
  echo "Refusing to overwrite a preserved build log: $build_dir" >&2
  exit 2
fi
mkdir -p -- "$build_dir"
export SOURCE_DATE_EPOCH=1788912000
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$build_dir" main.tex 2>&1 | tee "$build_dir/latexmk.console.log"
pdfinfo "$build_dir/main.pdf" | tee "$build_dir/pdfinfo.txt"
pdffonts "$build_dir/main.pdf" | tee "$build_dir/fonts.txt"
pdftotext -layout "$build_dir/main.pdf" "$build_dir/main.txt"
sha256sum "$build_dir/main.pdf" | tee "$build_dir/pdf.sha256"
