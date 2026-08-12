# Compilation report

- Status: PASS.
- Engine: pdfLaTeX through latexmk 4.76.
- PDF: `main.pdf`.
- PDF SHA-256:
  `0937b4b7be27978cbd7f7b2983cab1cce89f975e61afeabaacbfc783b7530716`.
- Format: A4, 7 pages, 346432 bytes.
- Final `main.log`: zero warnings, undefined references/citations,
  overfull boxes, underfull boxes, or LaTeX errors.
- Fonts: all 20 listed font subsets embedded with Unicode maps.
- Text audit: no `TODO`, `FIXME`, `VERIFY`, `PENDING`, unresolved-reference
  sentinels, or stale high-precision-only status.
- Section audit: every file in `paper/sections/` is included by `main.tex`.
- Main body: conclusion ends on page 6; references and appendix begin on
  page 6. The note is within a nine-page main-body budget.

The retained `main.pdf` is the release artifact. LaTeX auxiliary files and
`compile.log` are reproducible build products excluded from the manifest.
