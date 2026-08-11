# Compilation report

## Build status

- Status: **PASS**
- Final build: 2026-08-11 10:55:44 UTC
- Entry point: **main.tex**
- Command:

  ~~~bash
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
  ~~~

- Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- Driver: latexmk 4.76
- Bibliography: BibTeX with plainnat; 11 primary-source records
- Output: **main.pdf**
- Pages: 18
- Page size: US Letter, 612 x 792 pt
- PDF version: 1.5
- PDF size: 355,576 bytes

## Final hashes

~~~text
8c1f8a8443a35a3e80468700146a5806e2de034608e5c1f6ccc638a759d84c96  main.pdf
0c26819fe4482bedf6e062f91e66329af193e67405f57dca543fc34c306734ed  main.tex
055f0b9f247154b536cc1b1d636e01e7753c9120a82012d31b05548da2aa86b5  references.bib
~~~

## Log audit

The converged **main.log** was searched for:

~~~text
LaTeX Warning
Package ... Warning
undefined
multiply defined
Overfull
Underfull
Error
~~~

Final counts are all zero:

- TeX errors: 0
- undefined citations: 0
- undefined references: 0
- multiply-defined labels: 0
- package/LaTeX warnings: 0
- overfull boxes: 0
- underfull boxes: 0

The Appendix B longtable uses ragged-right paragraph columns so its scope
ledger compiles without box warnings.

## Source and PDF semantic audit

- A byte-level scan of **main.tex**, all 11 section files,
  **references.bib**, and **README.md** found no C0 control characters,
  carriage returns, or accidental tab escapes.
- Inline mathematics uses explicit dollar delimiters; the earlier
  parenthesized pseudo-math failure mode is absent.
- The output of **pdftotext -layout main.pdf** was inspected around the
  groupoid cocycle, projective normalizer, finite group trace, normalized
  determinant root, Farkas certificate table, and Route-A decision.
- The extracted PDF correctly renders the groupoid arrows, Greek symbols,
  the $B^{-\mathsf T}$/$B^{\mathsf T}$ distinction, the C26
  15-nonpositive/9-positive-dependence census for each action, and the
  “promotion rejected” boundary.
- No literal source placeholders such as (cG...), (rho_p), (tau...), (p), or
  (p^2) remain in the extracted paper text.

## Artifact boundary

Only files under this **paper/** directory were authored or modified for the
paper package. The project code, project-level documentation, results, and
release manifest were not edited.
