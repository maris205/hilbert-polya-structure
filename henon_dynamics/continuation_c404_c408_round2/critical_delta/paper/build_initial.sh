#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
export SOURCE_DATE_EPOCH=1788652800
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C

attempt="${1:-01}"
if [[ ! "$attempt" =~ ^[0-9][0-9]$ ]]; then
  printf '%s\n' 'The attempt identifier must contain exactly two digits.' >&2
  exit 2
fi
mkdir -p initial_build
build_log="initial_build/compile_attempt_${attempt}.stdout.log"
if [[ -e "$build_log" ]]; then
  printf '%s\n' "Refusing to overwrite the recorded build log: $build_log" >&2
  exit 2
fi

latexmk -pdf -recorder -interaction=nonstopmode -halt-on-error \
  -file-line-error -outdir=initial_build main.tex 2>&1 | tee "$build_log"
pdfinfo initial_build/main.pdf | tee initial_build/pdfinfo.txt
pdffonts initial_build/main.pdf | tee initial_build/pdffonts.txt
pdftotext -layout initial_build/main.pdf initial_build/main.txt
cp initial_build/main.pdf main.pdf
