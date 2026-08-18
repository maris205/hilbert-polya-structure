#!/usr/bin/env bash
set -eu

# Fixed build epoch: 2026-08-18 00:00:00 UTC.
export SOURCE_DATE_EPOCH=1787011200
export FORCE_SOURCE_DATE=1
export TZ=UTC

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
