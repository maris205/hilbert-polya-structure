# Build record

## Environment and commands

The verifier requires Python 3 and only the standard library. The manuscript
uses `amsart`, BibTeX, and standard TeX Live packages.

Run from `papers/113-principal-hook-partition-dynamics/`:

```bash
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Exact-verifier record

- Exhaustive range: every partition for `1<=n<=40`.
- Exact assertion count: **10,110,035**.
- Result: **PASS**.
- Stored transcript: `code/verification_output.txt`.
- Post-review fresh run: `python3 -B code/verify.py` exited `0` in 11.438 s.
- Fresh stdout: 45 lines, 6,053 bytes.
- Byte comparison with the stored transcript: `cmp` exit `0` (**MATCH**).
- The verifier and canonical transcript were unchanged by the review repair.

## PDF record

- PDF: `main.pdf`
- Pages: **4**
- PDF size: **325,001 bytes**
- Page geometry: A4 (`595.276 x 841.89 pt`)
- Four-stage exits (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`):
  **0 / 0 / 0 / 0**
- LaTeX warnings: **0**
- Overfull boxes: **0**
- Underfull boxes: **0**
- Undefined references/citations: **0**
- Multiply defined labels: **0**
- BibTeX warnings: **0**
- Fonts: **23/23 embedded, 23/23 subsetted, 23/23 with Unicode maps**
- Visual inspection: all four pages rendered at 140 dpi and checked; no
  clipping, collision, margin escape, missing glyph, broken rule, or
  unreadable formula was found.

## Deterministic metadata and font controls

The source now sets, before package loading:

```tex
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\usepackage[T1]{fontenc}
\usepackage{lmodern}
```

Settled `pdfinfo` reports no creation or modification date, PDF 1.5, A4, and
four pages. Latin Modern Type 1 fonts are embedded/subsetted with Unicode
maps. The settled `main.log`/`main.blg` scan found no package/class/font
warning, undefined control/reference/citation, multiply defined label,
overfull/underfull box, TeX error, or BibTeX `Warning--` line.

## Source conventions

- Anonymous author line.
- Positive weights only (`n>=1`); the empty partition is outside the system.
- Empty products equal one; empty layer sums equal zero.
- External dissemination, novelty, and priority: **HOLD**.
- `HOSTILE_REVIEW.md` is a repair-resolution ledger, not final QA.
- No final hash, batch QA, Git operation, or release clearance was performed.
