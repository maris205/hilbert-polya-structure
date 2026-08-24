# Compile report — C123

- Engine: `pdflatex` through `latexmk`.
- Environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`.
- Final PDF: 2 pages, SHA-256
  `2ec52ecdc8829e5b131ec44e7c7f286fcb54df2e9fb45e5d1f1546c365225700`.
- Two fresh isolated builds are byte-identical to one another and to the
  package PDF.
- Every font is embedded.
- Final logs contain no LaTeX/package warning, overfull/underfull box,
  undefined reference, multiply-defined label, or citation warning.
- Round-named PDFs are final-build release snapshots because internal semantic
  revisions preceded compilation; `../PAPER_IMPROVEMENT_LOG.md` records this
  honestly without an external-review claim.
