#!/usr/bin/env bash
set -euo pipefail

overlay_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
if [[ $# -ne 1 ]]; then
  echo "usage: $0 EMPTY_OUTPUT_DIRECTORY" >&2
  exit 2
fi
output_dir=$1
if [[ -L "$output_dir" ]]; then
  echo "output directory must not be a symlink" >&2
  exit 2
fi
if [[ -e "$output_dir" && ! -d "$output_dir" ]]; then
  echo "output path exists and is not a directory" >&2
  exit 2
fi
mkdir -p -- "$output_dir"
if find "$output_dir" -mindepth 1 -print -quit | grep -q .; then
  echo "output directory must be empty" >&2
  exit 2
fi

export SOURCE_DATE_EPOCH=1787270400
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C

cd "$overlay_root/paper"
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory="$output_dir" main.tex
(
  cd "$output_dir"
  BIBINPUTS="$overlay_root/paper:" bibtex main
)
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory="$output_dir" main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory="$output_dir" main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory="$output_dir" main.tex

pdf_sha=$(sha256sum "$output_dir/main.pdf" | awk '{print $1}')
source_sha=$(
  cd "$overlay_root"
  find paper figures inputs \
    -type f \( -name '*.tex' -o -name '*.tikz' -o -name '*.bib' -o -name '*.csv' -o -name '*.json' \) \
    -printf '%p\0' | LC_ALL=C sort -z | \
    while IFS= read -r -d '' path; do
      printf '%s  %s\n' "$(sha256sum "$path" | awk '{print $1}')" "$path"
    done | sha256sum | awk '{print $1}'
)
page_count=$(pdfinfo "$output_dir/main.pdf" | awk '/^Pages:/ {print $2}')
warning_count=$(grep -Ec 'LaTeX Warning|Package .* Warning|Overfull|Underfull' "$output_dir/main.log" || true)
pdflatex_version=$(pdflatex --version | sed -n '1p')
bibtex_version=$(bibtex --version | sed -n '1p')

{
  echo "schema=p49-final-writer-overlay-build-v1"
  echo "source_date_epoch=1787270400"
  echo "source_tree_digest=$source_sha"
  echo "pdf_sha256=$pdf_sha"
  echo "pages=$page_count"
  echo "warning_lines=$warning_count"
  echo "pdflatex=$pdflatex_version"
  echo "bibtex=$bibtex_version"
} > "$output_dir/BUILD_RECEIPT.txt"

if [[ "$pdf_sha" != "aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4" ]]; then
  echo "active PDF byte mismatch: $pdf_sha" >&2
  exit 1
fi
if [[ "$page_count" != "19" || "$warning_count" != "0" ]]; then
  echo "build QA failure: pages=$page_count warnings=$warning_count" >&2
  exit 1
fi
echo "BUILD_OK pages=$page_count pdf_sha256=$pdf_sha warnings=$warning_count"
