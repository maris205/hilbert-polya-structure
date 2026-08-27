# Final QA — P76

Checkpoint: 2026-08-27 UTC
Disposition: **PASS; INTERNAL FREEZE; EXTERNAL HOLD**

- Canonical artifact: `main.pdf` (5 pages), rebuilt after the last source
  correction.
- Build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, all exit zero.
- Log: no LaTeX/BibTeX warning, undefined reference/citation, overfull box, or
  underfull box.
- Fonts: every font reported by `pdffonts` is embedded.
- Control replay: `python3 code/verify_iet_fan.py` exits zero and its output is
  byte-for-byte equal to `code/verify_iet_fan.out`; the 18 language equalities
  cover 207 positive cylinders.
- Reverse reading: strict versus weak feasibility, the conditional closure
  equality, essential collapse wall, weak-only negative control, and the
  explicit hyperplane/chamber bound were checked again.
- Visual inspection: first and last pages are complete, legible, and free of
  clipping or malformed equations.

This is an internal QA record, not priority clearance or permission to
circulate.
