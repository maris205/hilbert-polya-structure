# Final mechanical QA — P95

Audit date: 2026-08-28 UTC  
Disposition: **internal GO after direct-owner subtraction / external HOLD**

This is the final mechanical audit of the frozen internal package. It does
not replace specialist peer review or establish novelty or priority.

## Exact-control rerun

From the paper directory,

```text
python3 code/verify_no_repeat.py
```

completed with exit status zero and reported `5,031` exact assertions. The
separate literal route enumerated `99,058` cyclic words. The registered
state-graph, orientation, positive-reachability, trace, first-hit, rational
return, and full admissible two-gap grid checks all passed using exact
integer or `Fraction` arithmetic.

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

`pdfinfo` reports a four-page, unencrypted A4 PDF with zero rotation, no
JavaScript, no forms, and no suspect objects. The final artifact is 289,151
bytes. `pdffonts` reports 23 font rows; every font is embedded, subset, and
Unicode-mapped. `pdftotext -layout` completed successfully, retained the
title, formulas, section order, citations, and references, and exposed no
unresolved editorial or cross-reference marker.

Canonical PDF SHA-256:

```text
c783ead4bd43089c836079dcaf361c6ba0802ec2b084dfd14441db96f895823b  main.pdf
```

## Page-by-page visual audit

Every page was rasterized at 144 dpi and inspected individually.

1. Title, abstract, short-period formulas, introduction, ownership boundary,
   and initial definition are complete and unclipped.
2. Right-action Cayley presentation, mixing corollary, and initial-period
   theorem are aligned, legible, and inside the text block.
3. Desert proof and delayed-geometric return theorem, including the renewal
   and covariance displays, have no collisions or broken symbols.
4. Scope discussion, exact-control summary, and all four references are
   present; there is no unintended blank page.

No clipping, overlap, malformed glyph, broken hyperlink coloring, or layout
defect was found.

## Seal

`SHA256SUMS` covers the evidence-bearing source, control, review, build, QA,
and PDF files and passes `sha256sum -c SHA256SUMS`. Public posting,
submission, author contact, and venue or priority claims remain **HOLD**.
