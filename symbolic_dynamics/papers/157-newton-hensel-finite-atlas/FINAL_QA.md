# Final cold QA — P157 NHI

**Date:** 2026-09-02 UTC  
**Result:** `PASS / ROUND-2 CANONICAL / HOLD_EXTERNAL`

No manuscript source, PDF, verifier, frozen transcript, or review artifact was
modified during this audit.

## Author verifier

- Command: `PYTHONDONTWRITEBYTECODE=1 python3 -B verify_p157.py`.
- Fresh replays: 2/2 byte-identical to `verification_output.txt` and to one
  another.
- Exact assertions: **2,563,880**; terminal status: `STATUS=PASS`.
- Verifier SHA-256:
  `9e259f6f6de3bb8a0ad5aae13e1c73f73c49d4cb4f62943e81e5ec1fe52950b9`.
- Transcript SHA-256:
  `f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.

## Two source-only cold builds

Two independent temporary directories received only `main.tex` and
`references.bib`.  Each ran

```text
pdflatex; bibtex; pdflatex; pdflatex; pdflatex
```

with halt-on-error.  Within each build, the third and fourth LaTeX passes
were byte-identical, establishing settlement.  Both cold PDFs were
byte-identical to each other and to canonical `main.pdf`.

For both cold builds and the canonical settled log:

```text
actual warnings=0  bad boxes=0  undefined=0  rerun requests=0
```

Canonical `main.pdf` is also byte-identical to `main_round2.pdf`.

## PDF and visual gate

- Canonical SHA-256:
  `6b0c1fb81c065a9213df4cb4af7b731e25e02e3306e6220a154899166e9129dd`.
- Pages / bytes / format: **4 / 349,380 / A4**.
- PDF metadata fields `Title`, `Author`, `Subject`, and `Keywords` are blank.
- Encryption / forms / JavaScript: `no / none / no`.
- `pdffonts`: 26 rows; all 26 embedded, subsetted, and Unicode mapped.
- `pdftotext`: anonymous label present; zero `??`, `[?]`, `TODO`, `FIXME`,
  `XXX`, `[VERIFY]`, draft-watermark, remove-before, or placeholder markers.
- All four pages were rasterized at 144 dpi (`1191 x 1684` pixels each) and
  visually inspected.  Title, theorem statements, tables, displayed formulas,
  proofs, declarations, and reference are legible with no clipping, overlap,
  broken glyph, missing object, or page-boundary defect.

## Manifest gate

`SHA256SUMS` is regenerated after this report, excludes only itself, and
covers every other retained regular file in this paper directory.  A final
`sha256sum -c SHA256SUMS` must report every entry `OK`.
