# Final cold QA — P158 CIC

**Date:** 2026-09-02 UTC  
**Result:** `PASS / ROUND-2 CANONICAL / HOLD_EXTERNAL`

No manuscript source, PDF, verifier, frozen transcript, or review artifact was
modified during this audit.

## Author verifier

- Command: `PYTHONDONTWRITEBYTECODE=1 python3 -B verify_p158.py`.
- Fresh replays: 2/2 byte-identical to `verification_output.txt` and to one
  another.
- Exact assertions: **77,530**; terminal status: `STATUS=PASS`.
- Verifier SHA-256:
  `a1b20733927f31c417d475ec7566050ef812d17be123a7306b7587a6a453c44a`.
- Transcript SHA-256:
  `3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d`.

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
  `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5`.
- Pages / bytes / format: **4 / 371,703 / A4**.
- PDF metadata fields `Title`, `Author`, `Subject`, and `Keywords` are blank.
- Encryption / forms / JavaScript: `no / none / no`.
- `pdffonts`: 28 rows; all 28 embedded, subsetted, and Unicode mapped.
- `pdftotext`: anonymous label present; zero `??`, `[?]`, `TODO`, `FIXME`,
  `XXX`, `[VERIFY]`, draft-watermark, remove-before, or placeholder markers.
- All four pages were rasterized at 144 dpi (`1191 x 1684` pixels each) and
  visually inspected.  The mandatory `r=R,z>0` zero-fibre boundary, theorem,
  proofs, exact-control table, declarations, and references are legible with
  no clipping, overlap, broken glyph, missing object, or page-boundary defect.

## Manifest gate

`SHA256SUMS` is regenerated after this report, excludes only itself, and
covers every other retained regular file in this paper directory.  A final
`sha256sum -c SHA256SUMS` must report every entry `OK`.
