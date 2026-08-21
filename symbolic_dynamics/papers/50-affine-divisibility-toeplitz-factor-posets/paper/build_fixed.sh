#!/usr/bin/env bash
set -euo pipefail

export SOURCE_DATE_EPOCH=1787270400
export FORCE_SOURCE_DATE=1
export TZ=UTC

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
