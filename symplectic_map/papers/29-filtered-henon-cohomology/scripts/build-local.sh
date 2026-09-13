#!/usr/bin/env bash
# One ordinary local build; the caller seals the complete source first.
# Usage: bash scripts/build-local.sh SOURCE_DIRECTORY NEW_BUILD_DIRECTORY
set -euo pipefail

if [[ $# != 2 ]]; then
  printf 'Usage: %s SOURCE_DIRECTORY NEW_BUILD_DIRECTORY\n' "$0" >&2
  exit 2
fi
paper_source=$(realpath -e -- "$1")
paper_build=$(realpath -m -- "$2")
paper_project=$(realpath -e -- "$(dirname -- "$0")/..")
case "$paper_source" in
  "$paper_project"/paper|"$paper_project"/paper-successor-*) ;;
  *) printf 'Source is outside the current project source convention.\n' >&2; exit 2 ;;
esac
case "$paper_build" in
  "$paper_project"/build/*) ;;
  *) printf 'Build directory must be a fresh child under this project build/.\n' >&2; exit 2 ;;
esac
if [[ -e "$paper_build" || -L "$paper_build" ]]; then
  printf 'Refusing to reuse an existing build directory: %s\n' "$paper_build" >&2
  exit 2
fi
test -f "$paper_source/main.tex"
test -f "$paper_source/references.bib"
mkdir -p -- "$(dirname -- "$paper_build")"
mkdir -- "$paper_build"
mkdir -- "$paper_build/work"
cp -a -- "$paper_source/." "$paper_build/work/"
export SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
cd -- "$paper_build/work"

tex_pass() {
  local pass_name=$1
  local pass_code
  if pdflatex -file-line-error -recorder -interaction=nonstopmode \
      -halt-on-error main.tex >"../${pass_name}.stdout.log" 2>&1; then
    pass_code=0
  else
    pass_code=$?
  fi
  [[ ! -f main.log ]] || cp -- main.log "../${pass_name}.tex.log"
  [[ ! -f main.fls ]] || cp -- main.fls "../${pass_name}.inputs.fls"
  printf '%s exit_code=%s\n' "$pass_name" "$pass_code" >>../stages.log
  return "$pass_code"
}

tex_pass pass1
if bibtex main >../bibtex.stdout.log 2>&1; then
  bibtex_code=0
else
  bibtex_code=$?
fi
[[ ! -f main.blg ]] || cp -- main.blg ../bibtex.blg
printf 'bibtex exit_code=%s\n' "$bibtex_code" >>../stages.log
if [[ "$bibtex_code" != 0 ]]; then exit "$bibtex_code"; fi
tex_pass pass2
tex_pass pass3
printf 'BUILD_COMPLETE %s/work/main.pdf\n' "$paper_build"
