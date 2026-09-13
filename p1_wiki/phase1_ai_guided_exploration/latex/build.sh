#!/usr/bin/env bash
# Build the formal PDF deterministically from the tracked TeX sources.
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"
mkdir -p build

lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=build manuscript.tex
lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=build manuscript.tex

cp build/manuscript.pdf manuscript.pdf
pdfinfo manuscript.pdf
