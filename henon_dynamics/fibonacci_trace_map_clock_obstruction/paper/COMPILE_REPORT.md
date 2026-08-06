# Compile report

Date: 2026-08-06

## Outcome

- Status: PASS
- Output: main.pdf
- Pages: 12
- Size: 290393 bytes
- SHA-256: 5ca4ee4c469c5df2b38d63b389f6df6113f004eeb47d9ce1eb0ba90c39193bea
- PDF version: 1.5

## Build

The paper was built with:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Additional stabilization passes were run after the final Route-A and
terminology edits.  The persisted compile-pass1.log through compile-pass5.log
and compile-bibtex.log correspond to the final source.

## Verification

- no LaTeX errors or fatal stops;
- no undefined citations or references;
- no multiply defined labels;
- no overfull or underfull boxes in the final logs;
- no TODO, FIXME, undefined marker, double-question marker, stale limsup, or
  stale direct-variable-map language in extracted PDF text;
- all 19 PDF fonts are embedded;
- the PDF timestamp is later than every included TeX source;
- an independent adversarial source/PDF audit found no remaining
  release-blocking mathematical or scope inconsistency.
