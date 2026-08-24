# Compile report — C122

- Engine: `pdflatex` through `latexmk`.
- Environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`.
- Final artifact: `main.pdf`, 2 pages.
- SHA-256: `eb23aed0cd77147f1d24dae91e7023d2c85345580b3fb58f9a75200ca32d754b`.
- Two fresh isolated builds are byte-identical to each other and to the
  checked-in PDF.
- Every font reported by `pdffonts` is embedded.
- Final logs contain no LaTeX/package warning, overfull/underfull box,
  undefined reference, multiply-defined label, or citation warning.
- The three round-named release snapshots are byte-identical because the two
  semantic revisions were applied before the frozen build; this is disclosed
  in `../PAPER_IMPROVEMENT_LOG.md` and is not an external-review claim.
