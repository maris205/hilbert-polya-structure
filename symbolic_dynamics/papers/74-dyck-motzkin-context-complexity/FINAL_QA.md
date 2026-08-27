# Final QA — P74

Checkpoint: 2026-08-27 UTC
Disposition: **PASS; INTERNAL FREEZE; EXTERNAL HOLD**

- Canonical artifact: `main.pdf` (4 pages), newer than the final source and
  bibliography.
- Build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, all exit zero.
- Log: no LaTeX/BibTeX warning, undefined reference/citation, overfull box, or
  underfull box.
- Fonts: every font reported by `pdffonts` is embedded.
- Control replay: `python3 code/verify_context_complexity.py` exits zero and
  its output is byte-for-byte equal to `code/verify_context_complexity.out`.
- Reverse reading: the deterministic normal form, prolongability, empty
  context, `M=1` degeneracy, direct bounded context signatures, and the
  rejected histogram shortcut were checked again.
- Visual inspection: first and last pages are complete, legible, and free of
  clipping or malformed equations.

This is an internal QA record, not priority clearance or permission to
circulate.
