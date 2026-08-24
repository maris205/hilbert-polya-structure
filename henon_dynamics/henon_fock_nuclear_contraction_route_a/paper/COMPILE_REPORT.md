# Compile report — C119

- Engine: `pdflatex` through `latexmk`.
- Reproducibility environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`.
- Final artifact: `main.pdf`, 2 pages.
- SHA-256: `77aa108f6ccad9b3dd9db6d69c89116dfac788cb50c3d6d251d3926c7cce40c2`.
- Two clean isolated builds were byte-identical to one another and to the
  checked-in PDF.
- `pdffonts` reports every font as embedded.
- The final log contains no LaTeX/package warning, overfull/underfull box,
  undefined reference, multiply-defined label, or citation warning.
- `main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` are
  byte-identical release snapshots. The semantic internal prose progression is
  documented in `../PAPER_IMPROVEMENT_LOG.md`; no external review is implied.
