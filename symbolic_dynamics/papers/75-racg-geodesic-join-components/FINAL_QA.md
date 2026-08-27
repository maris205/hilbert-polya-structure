# Final QA — P75

Checkpoint: 2026-08-27 UTC
Disposition: **PASS; INTERNAL FREEZE; EXTERNAL HOLD**

- Canonical artifact: `main.pdf` (5 pages), newer than the final source and
  bibliography.
- Build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, all exit zero.
- Log: no LaTeX/BibTeX warning, undefined reference/citation, overfull box, or
  underfull box.
- Fonts: every font reported by `pdffonts` is embedded.
- Control replay: `python3 code/verify_racg_join.py` exits zero and its output
  is byte-for-byte equal to `code/verify_racg_join.out`; 1,252 atlas
  matrix/count checks and 995 nontrivial local irreducibility checks pass.
- Reverse reading: every multiplicity and zeta statement is scoped to the
  state-decorated edge presentation; the bare label shift is only a factor,
  with the collapse example retained.
- Visual inspection: first and last pages are complete and legible; the final
  page is a short references continuation and contains no clipping.

This is an internal QA record, not priority clearance or permission to
circulate.
