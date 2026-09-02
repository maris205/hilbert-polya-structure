# Final cold QA — P161 ORT

**Date:** 2026-09-02 UTC  
**Result:** `PASS / ROUND-2 CANONICAL / HOLD_EXTERNAL`

No manuscript source, PDF, verifier, frozen transcript, or review artifact was
modified during this audit.

## Author verifier

- Command: `PYTHONDONTWRITEBYTECODE=1 python3 -B verify_p161.py`.
- Fresh replays: 2/2 byte-identical to `verification_output.txt` and to one
  another.
- Exact assertions: **1,317,843**; terminal status: `STATUS=PASS`.
- Verifier SHA-256:
  `0c5ac6d3303e19142569517f77e1ee1c9792e092e7dc7e309b80bb7c3f81330d`.
- Transcript SHA-256:
  `26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c`.

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
  `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214`.
- Pages / bytes / format: **4 / 304,462 / A4**.
- PDF metadata fields `Title`, `Author`, `Subject`, and `Keywords` are blank.
- Encryption / forms / JavaScript: `no / none / no`.
- `pdffonts`: 21 rows; all 21 embedded, subsetted, and Unicode mapped.
- `pdftotext`: anonymous label present; zero `??`, `[?]`, `TODO`, `FIXME`,
  `XXX`, `[VERIFY]`, draft-watermark, remove-before, or placeholder markers.
- All four pages were rasterized at 144 dpi (`1191 x 1684` pixels each) and
  visually inspected.  The theorem, singular strata, source-subtraction
  table, reverse-window proof, declarations, and references are legible with
  no clipping, overlap, broken glyph, missing object, or page-boundary defect.

## Manifest gate

`SHA256SUMS` is regenerated after this report, excludes only itself, and
covers every other retained regular file in this paper directory.  A final
`sha256sum -c SHA256SUMS` must report every entry `OK`.
