# Compile report — C118

- Engine: `pdflatex` through `latexmk`.
- Reproducibility environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`.
- Final artifact: `main.pdf`, 2 pages.
- SHA-256: `c36c3371fe5aa608dc1e55f50ab5573dc51bb9d21bf49809720013c41f28b74a`.
- Two clean isolated builds were byte-identical to one another and to the
  checked-in PDF.
- `pdffonts` reports every font as embedded.
- The final log contains no LaTeX/package warning, overfull/underfull box,
  undefined reference, multiply-defined label, or citation warning.
- `main_round0.pdf`, `main_round1.pdf`, and `main_round2.pdf` are release
  snapshots of the same final build; the semantic prose progression is
  documented in `../PAPER_IMPROVEMENT_LOG.md` and is not presented as an
  external-review history.
