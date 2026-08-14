# HCS-C53 compilation report

Status: **PASS; DOCS_FINAL_NO_MORE_EDITS against RELEASE_CANDIDATE evidence**

## Build

- Engine: pdflatex through latexmk 4.76.
- Command:
  `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Exit status: zero.
- PDF: paper/main.pdf.
- Total pages: 13 A4 pages.
- Main text through Limitations and Reproducibility: page 11.
- Appendix begins on page 12; references begin on page 13.
- File size: 430815 bytes.
- PDF SHA-256:
  0fcae5c42fa5803749956bb62c56f0f25f0148aa1019704b2dc43dcc443a518f.

No conference page limit is asserted; the project uses the inherited
single-column mathematical-article format.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- LaTeX/package warnings after the final stabilized pass: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Rerun requests: 0.
- Stale section files: 0; every file in paper/sections/ is input by
  main.tex.
- Bibliography: eight entries, all cited; no uncited bibliography bloat.
- Text extraction: PASS.
- Residual TODO/FIXME/XXX/[VERIFY] markers in extracted PDF: 0.
- Literal ?? or [?] placeholders in extracted PDF: 0.

## Release-candidate evidence lock

- Certificate SHA-256:
  `f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79`.
- Payload SHA-256:
  `8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41`.
- Independent-check SHA-256:
  `0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67`.
- Code/results-manifest SHA-256:
  `b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480`.
- Read-only replay: 20/20 semantic gates, 63/63 targeted tests, and
  11/11 code/results-manifest entries pass.

## PDF checks

- All fonts are embedded and subsetted.
- No Type 3 fonts occur.
- PDF version: 1.5.
- The prior visual inspection of pages 1, 7, 10, 12, and 13 remains valid;
  the changed replay page 11 was re-rendered and inspected after the clean
  build.  The four evidence hashes are legible, unclipped, and contained
  within the text block.

## Scope checks visible in the paper

- Equation descent is all-\(n\); smooth/motive statements are restricted to
  certified \(n=2,3,4\).
- Reynolds averaging is order 24 with coefficient \(1/24\); quadratic
  transfer has coefficient \(1/2\).
- Frobenius is geometric, with \(F_p\mid\mathbf Q_\ell(-1)=p\).
- Raw integrality passes through the monic polynomial
  \(\det(U-F_p)\), then coefficient reversal; the Euler polynomial
  \(\det(1-F_pT)\) is not called monic.
- Fourth-row exponent clearing is good-split-local only.
- The inert identity, absent global half-root, and irreducibility/phantom
  scope are explicit.
- The \(p=7\) trace is labeled
  PRE_C53_RECONNAISSANCE_REGRESSION_ANCHOR_UNCERTIFIED, not an independently
  reconstructed point-count theorem; no C52 provenance is asserted.

This is the final paper-source/report freeze.  Full-project manifest creation
and implementation-provenance backfill must record these bytes without
reopening the paper.
