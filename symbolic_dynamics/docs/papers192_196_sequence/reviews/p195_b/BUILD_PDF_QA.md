# P195 Review-B build and PDF QA

## Bound artifact

- path: `papers/195-odd-side-least-neighbor-trees/main_round1.pdf`
- SHA-256: `d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a`
- bytes: `318096`
- pages: `3`
- page box: `595.276 x 841.89 pts (A4)`
- PDF version: `1.5`

## Source-only cold build

Review B copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  The build
completed without LaTeX/package warnings, unresolved citations/references,
rerun requests, bad boxes, or BibTeX warnings.  The rebuilt PDF is byte-
identical to the frozen Round-1 artifact.

## Static and visual checks

- metadata title/author/subject/keywords/creator/producer are blank;
- no metadata stream, form, JavaScript, or encryption;
- all `23/23` fonts are embedded, subsetted, and Unicode mapped;
- extracted text is `243` lines / `11077` bytes and contains all theorem and
  equation anchors, both recurrent-count rows, the nonuniqueness warning,
  `OWNER_AMBER/HOLD_EXTERNAL`, and references;
- all three pages were separately rasterized and visually inspected.

No blank page, clipped display, overlap, malformed fraction, broken theorem
heading, or truncated reference was found.  Artifact QA does not certify
novelty, ownership, or external-release readiness.
