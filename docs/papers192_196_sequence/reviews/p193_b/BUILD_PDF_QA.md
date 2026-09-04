# P193 Review-B build and PDF QA

## Bound artifact

- path: `papers/193-mutual-best-block-refinement/main_round1.pdf`
- SHA-256: `b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9`
- bytes: `390196`
- pages: `5`
- page box: `595.276 x 841.89 pts (A4)`
- PDF version: `1.5`

## Source-only cold build

Review B copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  The build
completed without LaTeX/package warnings, unresolved citations/references,
rerun requests, bad boxes, or BibTeX warnings.  The rebuilt PDF SHA-256 is the
same value above and is byte-identical to the frozen Round-1 PDF.

## Static and visual checks

- metadata title/author/subject/keywords/creator/producer are blank;
- no metadata stream, form, JavaScript, or encryption;
- all `29/29` fonts are embedded, subsetted, and Unicode mapped;
- extracted text is `418` lines / `16524` bytes and contains the definition,
  all theorem anchors, the `n=8` depth row, `OWNER_AMBER/HOLD_EXTERNAL`, and
  references;
- all five pages were separately rasterized and visually inspected.

No blank page, clipping, overlap, broken display, split theorem heading,
truncated table, or damaged reference was found.  This QA concerns only the
bound artifact and does not certify novelty, ownership, or release readiness.
