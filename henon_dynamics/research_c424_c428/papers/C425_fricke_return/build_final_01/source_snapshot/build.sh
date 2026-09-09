#!/usr/bin/env bash
# A manuscript build, not a mathematical-program execution.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
c425_build_dir=${1:-build_initial_01}
case "$c425_build_dir" in
  build_[a-zA-Z0-9_]*) ;;
  *) printf '%s\n' 'Build directory must be a simple build_* name.' >&2; exit 2 ;;
esac
if [[ "$c425_build_dir" == */* || "$c425_build_dir" == *..* ]]; then
  printf '%s\n' 'Nested or parent-relative build paths are not allowed.' >&2
  exit 2
fi
if [[ -e "$c425_build_dir" ]]; then
  printf '%s\n' 'Build directory already exists; choose a fresh name.' >&2
  exit 2
fi
mkdir -- "$c425_build_dir"
export SOURCE_DATE_EPOCH=1788912000
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$c425_build_dir" main.tex 2>&1 | tee "$c425_build_dir/compile.log"
