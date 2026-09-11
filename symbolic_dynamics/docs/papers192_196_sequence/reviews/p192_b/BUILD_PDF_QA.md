# P192 Review-B build and PDF QA

## Bound artifact

- path: `papers/192-first-collision-hurwitz/main_round1.pdf`
- SHA-256: `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57`
- bytes: `323972`
- pages: `4`
- page box: `595.276 x 841.89 pts (A4)`
- PDF version: `1.5`

## Source-only cold build

Review B copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  The build had
no LaTeX/package warning, unresolved citation/reference, rerun request, bad
box, or BibTeX warning.  The resulting PDF is byte-identical to the frozen
Round-1 artifact.

## Static and visual checks

- metadata title/author/subject/keywords/creator/producer are blank;
- no metadata stream, form, JavaScript, or encryption;
- all `25/25` fonts are embedded, subsetted, and Unicode mapped;
- extracted text is `218` lines / `11502` bytes and contains the exact owner
  gate, Campion Loth--Rattan subtraction, `n=2` cases, Theorem 4.1, Conjecture
  5.1, limitations, and all six references;
- all four pages were separately rasterized and visually inspected.

No blank page, clipping, overlap, malformed display, broken theorem heading,
or truncated reference was found.  Artifact QA makes no ownership or release
claim.
