#!/usr/bin/env bash
set -euo pipefail

c420_package_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
c420_build_label="${1:-baseline}"
if [[ ! "$c420_build_label" =~ ^[A-Za-z0-9_-]+$ ]]; then
  printf 'Invalid build label: use letters, digits, underscores or hyphens.\n' >&2
  exit 64
fi
c420_build_dir="$c420_package_dir/builds/$c420_build_label"
if [[ -e "$c420_build_dir" ]]; then
  printf 'Build directory already exists; choose a fresh label: %s\n' "$c420_build_dir" >&2
  exit 65
fi
mkdir -p -- "$c420_build_dir"
cp -a -- "$c420_package_dir/paper" "$c420_build_dir/source_snapshot"

export SOURCE_DATE_EPOCH=1788825600
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C
{
  date -u '+Build started: %Y-%m-%d %H:%M:%S UTC'
  uname -srm
  printf 'SOURCE_DATE_EPOCH=%s\nFORCE_SOURCE_DATE=%s\nTZ=%s\nLC_ALL=%s\n' \
    "$SOURCE_DATE_EPOCH" "$FORCE_SOURCE_DATE" "$TZ" "$LC_ALL"
  pdflatex --version
  latexmk -v
  bibtex --version
  pdfinfo -v 2>&1
} > "$c420_build_dir/environment.txt"
(
  cd -- "$c420_package_dir"
  rg --files -0 -g '*.tex' -g '*.bib' paper |
    sort -z | xargs -0 sha256sum
) > "$c420_build_dir/source_inputs.sha256"

cd -- "$c420_package_dir/paper"
set +e
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$c420_build_dir" main.tex 2>&1 |
  tee "$c420_build_dir/compile.stdout.log"
c420_latexmk_status=${PIPESTATUS[0]}
set -e
printf '%s\n' "$c420_latexmk_status" > "$c420_build_dir/latexmk_exit_code.txt"
if [[ "$c420_latexmk_status" -ne 0 ]]; then
  exit "$c420_latexmk_status"
fi
pdfinfo "$c420_build_dir/main.pdf" > "$c420_build_dir/pdfinfo.txt"
pdffonts "$c420_build_dir/main.pdf" > "$c420_build_dir/pdffonts.txt"
pdftotext -layout "$c420_build_dir/main.pdf" "$c420_build_dir/main.txt"
sha256sum "$c420_build_dir/main.pdf" > "$c420_build_dir/pdf.sha256"
printf 'Successful build: %s\n' "$c420_build_dir/main.pdf"
