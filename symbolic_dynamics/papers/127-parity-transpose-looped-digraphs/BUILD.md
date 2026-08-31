# Build protocol — P127

From this directory, the settled manuscript build is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Final QA must also repeat these four stages in an isolated temporary
directory containing only `main.tex` and `references.bib`, check the log for
errors, warnings, undefined citations/references, box warnings, and rerun
requests, inspect every rasterized page, audit embedded fonts and anonymous
metadata, and verify a fresh canonical byte match.

## Round-one repair build

- Hostile Review A repair date: 2026-08-31 UTC.
- Fresh canonical verifier: byte-identical, **1,271,047 assertions**.
- Isolated four-stage build from only `main.tex` and `references.bib`: PASS;
  the isolated PDF is byte-identical to the working PDF.
- Settled errors, warnings, undefined citations/references, bad boxes, and
  actionable rerun requests: zero.
- `main.pdf` and `main_round1.pdf`: byte-identical, **3 A4 pages, 328,070
  bytes**, SHA-256
  `107d6baa4063d747799f26710bc1de0bc0eb8a7460509e9d8beafe570f760f0d`.
- All 26 font rows are embedded, subsetted, and Unicode-mapped; Author,
  Title, Subject, and Keywords metadata are blank; no form, JavaScript, or
  encryption is present.
- All three pages were rasterized and inspected after repair.  The former
  visible `qquad` defect is absent; no clipping, collision, blank page, or
  malformed display was found.

Independent Review B repeated these checks and returned zero findings.
`main_round2.pdf` is byte-identical to `main_round1.pdf` and `main.pdf`, with
SHA-256
`107d6baa4063d747799f26710bc1de0bc0eb8a7460509e9d8beafe570f760f0d`.

## Paper-local final QA

Final QA on 2026-08-31 UTC reran the canonical verifier and obtained a
byte-identical 738-byte transcript with **1,271,047 assertions**.  A fresh
isolated four-stage build from only `main.tex` and `references.bib`
reproduced `main.pdf` byte for byte; its settled log and BLG have no error,
warning, undefined item, bad box, or actionable rerun request, and all 7
bibliography items close.

The final `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` remain
byte-identical at 3 A4 pages and 328,070 bytes.  The reviewed PDF hash is
unchanged, so the all-page visual, 26-font, and anonymous-metadata evidence
from the two independent reviews applies exactly to the frozen artifact.
`FINAL_QA.md` records the terminal checks and `SHA256SUMS` freezes the
paper-local package.  Internal status is `GO_INTERNAL`; external status is
`HOLD_EXTERNAL`.
