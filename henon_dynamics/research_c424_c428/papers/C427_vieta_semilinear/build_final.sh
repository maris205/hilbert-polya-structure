#!/usr/bin/env bash
# Typesetting only. Never invokes a mathematical certificate or atlas program.
set -euo pipefail
cd -- "$(dirname -- "$0")"
build_label=${1:?Use final_01 or final_02}
case "$build_label" in
  final_01|final_02) ;;
  *) printf 'Unsupported final build label: %s\n' "$build_label" >&2; exit 2 ;;
esac
build_dir="builds/$build_label"
if test -e "$build_dir"; then
  printf 'Refusing to reuse an existing final build directory: %s\n' "$build_dir" >&2
  exit 2
fi
sha256sum -c INPUT_MANIFEST.sha256
mkdir -p -- "$build_dir/pages"
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$build_dir/start_utc.txt"
cp INPUT_MANIFEST.sha256 "$build_dir/input_before.sha256"
env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$build_dir" main.tex 2>&1 | tee "$build_dir/compile.log"
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$build_dir/end_utc.txt"
sha256sum -c INPUT_MANIFEST.sha256
cp INPUT_MANIFEST.sha256 "$build_dir/input_after.sha256"
cmp "$build_dir/input_before.sha256" "$build_dir/input_after.sha256"
tar --sort=name --mtime='@1788912000' --owner=0 --group=0 --numeric-owner \
  -cf "$build_dir/source.tar" main.tex math_commands.tex references.bib \
  sections build_final.sh INPUT_MANIFEST.sha256
pdfinfo "$build_dir/main.pdf" > "$build_dir/pdfinfo.txt"
pdffonts "$build_dir/main.pdf" > "$build_dir/pdffonts.txt"
pdftotext -layout "$build_dir/main.pdf" "$build_dir/main.txt"
pdftoppm -r 85 -png "$build_dir/main.pdf" "$build_dir/pages/page"
if rg -n 'Warning|Error|Overfull|Underfull|undefined|^!' \
  "$build_dir/main.log" "$build_dir/main.blg"; then
  printf 'Final diagnostics require inspection; preserving all outputs.\n' >&2
  exit 3
else
  diagnostic_status=$?
  if test "$diagnostic_status" -ne 1; then exit "$diagnostic_status"; fi
fi
sha256sum "$build_dir/main.pdf" "$build_dir/source.tar"
