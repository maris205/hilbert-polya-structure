# Final mechanical QA — P92

Audit date: 2026-08-28 UTC  
Disposition: **internal GO / external HOLD**

This is the final mechanical audit of the frozen internal package. It does
not replace specialist peer review or establish novelty or priority.

## Exact-control rerun

From the paper directory,

```text
python3 code/verify_primitive_avoidance.py
```

completed with exit status zero and reported `PASS: 258 exact assertions`.
All five registered lanes passed: `(2,2)`, `(3,2)`, `(3,3)`, `(4,2)`, and
`(5,2)`, including the independent nonprime `F_4` lane and the negative
binary mixing boundary.

## Four-stage build and log audit

The complete sequence

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

completed with exit status zero at every stage. The final `main.log` and
`main.blg` contain zero undefined citations, zero undefined references, zero
LaTeX or package warnings, zero overfull boxes, zero underfull boxes, and no
fatal error marker.

## PDF and extracted-text audit

`pdfinfo` reports a six-page, unencrypted A4 PDF with zero rotation, no
JavaScript, no forms, and no suspect objects. The final artifact is 325,223
bytes. `pdffonts` reports 24 font rows; every font is embedded, subset, and
Unicode-mapped. `pdftotext -layout` completed successfully, retained the
title, formulas, section order, table, citations, and references, and exposed
no unresolved editorial or cross-reference marker.

Canonical PDF SHA-256:

```text
a120a809a8e1f444563fbc9ca1e7432ffeda2836d14ab89297f5c360dabb0092  main.pdf
```

## Page-by-page visual audit

Every page was rasterized at 144 dpi and inspected individually.

1. Title, abstract, principal determinant/zeta display, introduction, and
   contribution list are complete and unclipped.
2. Ownership boundary, state model, matrix display, definition, and affine
   skew-product proposition are aligned and legible.
3. Fourier-compression lemma, boxed characteristic polynomial, and proof
   displays remain within the text block.
4. Complete periodic-data formulas, recovery corollary, and the opening of
   the mixing theorem have no collisions or broken symbols.
5. Mixing and binary-boundary proofs, control discussion, and the five-lane
   table are complete with no split-row or margin defect.
6. Nonprime-lane witness, scope boundary, and all four references are present;
   there is no unintended blank page.

No clipping, overlap, malformed glyph, broken hyperlink coloring, or layout
defect was found.

## Seal

`SHA256SUMS` covers the evidence-bearing source, control, review, build, QA,
and PDF files and passes `sha256sum -c SHA256SUMS`. Public posting,
submission, author contact, and venue or priority claims remain **HOLD**.
