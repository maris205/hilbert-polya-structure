# Compilation Report

## Final build

- Status: **SUCCESS**
- Date: 2026-08-13
- PDF: main.pdf
- Total pages: 13
- Main body through conclusion: 10 pages
- References start: page 11
- Appendix starts: page 11
- PDF size: 545,643 bytes
- PDF SHA256:
  8b241df97895016fc70db56f9180f492f92d4bc87654ecca91e4a157b9b31270
- Page format: A4
- Encryption: none
- Embedded/subset fonts: all

## Build sequence

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

## Checks

- LaTeX errors: 0
- Undefined references: 0
- Undefined citations: 0
- Overfull boxes: 0
- Underfull boxes: 0
- Remaining LaTeX/package warnings: 0
- TODO/FIXME/VERIFY markers in PDF text: 0
- Visual inspection: title/abstract/status box and full-width hero figure
  checked at rendered size
- Local source control-byte scan: PASS

## Experiment verification

~~~text
test_finite_dual_identities       PASS
test_full_frozen_run              PASS
test_hand_complexes               PASS
test_poset_mobius_prefix          PASS
test_schatten_domain_diagnostics  PASS
~~~

The five tests completed successfully. The experiment uses only the Python
standard library.

## Review policy

No automatic review or paper-improvement loop was run. This follows the
project directive for rapid exploratory papers: exact formula checks,
source-lock checks, deterministic tests, and a clean PDF build are the
release gates.
