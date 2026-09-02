# Final cold QA — P159 OVP

**Date:** 2026-09-02 UTC  
**Result:** `PASS / ROUND-2 CANONICAL / HOLD_EXTERNAL`

No manuscript source, PDF, verifier, frozen transcript, or review artifact was
modified during this audit.

## Author verifier

- Command: `PYTHONDONTWRITEBYTECODE=1 python3 -B verify_p159.py`.
- Fresh replays: 2/2 byte-identical to `verification_output.txt` and to one
  another.
- Exact assertions: **3,167,525**; terminal status: `PASS`.
- Verifier SHA-256:
  `ffb7e464f665731a2dcb2dc3fabff724594d7420eea8edded64d33e13b413c5d`.
- Transcript SHA-256:
  `363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879`.

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
  `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d`.
- Pages / bytes / format: **5 / 363,444 / A4**.
- PDF metadata fields `Title`, `Author`, `Subject`, and `Keywords` are blank.
- Encryption / forms / JavaScript: `no / none / no`.
- `pdffonts`: 27 rows; all 27 embedded, subsetted, and Unicode mapped.
- `pdftotext`: anonymous label present; zero `??`, `[?]`, `TODO`, `FIXME`,
  `XXX`, `[VERIFY]`, draft-watermark, remove-before, or placeholder markers.
- All five pages were rasterized at 144 dpi (`1191 x 1684` pixels each) and
  visually inspected.  Transfer matrices, boundary formulas, exact-control
  table, declarations, and all six references are legible with no clipping,
  overlap, broken glyph, missing object, or page-boundary defect.

## Manifest gate

`SHA256SUMS` is regenerated after this report, excludes only itself, and
covers every other retained regular file in this paper directory.  A final
`sha256sum -c SHA256SUMS` must report every entry `OK`.
