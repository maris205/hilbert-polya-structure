# Paper12 Compilation Report

- Candidate: `SD-C14`
- Compiled: 2026-08-13 (UTC)
- Engine: `pdfTeX` / `pdflatex`
- Bibliography: `BibTeX` with `plainnat`; every entry in `references.bib` is
  cited in the manuscript.
- Build sequence:

  ```text
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  bibtex main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  ```

- Output: `main.pdf`
- Format: A4, 9 pages, PDF 1.5
- Size: 352620 bytes
- SHA-256:
  `6a30f34dc6a1174ccac73323f8c5e56791a8612e43686bd6366b10dfb35e2cf7`
- Final-log audit: no undefined references or citations, LaTeX/package
  warnings, overfull boxes, or underfull boxes.
- Font audit: all fonts reported by `pdffonts` are embedded and subsetted.
- Content audit: the exact cyclic, density-perturbation,
  Fuglede--Kadison-residual, and nine matched-inventory control results are
  integrated without target-zero or fitted-parameter claims.
- Scope audit: Symbolic Dynamics is the only primary family; Route B remains
  locked and cross-family ideas occur only in `ROUND2_CLUES.md`.

LaTeX intermediates were removed after this report was recorded; the PDF and
human-editable sources are retained.
