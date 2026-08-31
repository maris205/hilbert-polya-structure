# Build record

## Round0 isolated build

Date: 2026-08-31 UTC.

The source pair `main.tex` and `references.bib` was copied into a fresh
`mktemp -d` directory and built in four stages:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

| stage | status |
|---|---:|
| pdflatex 1 | 0 |
| bibtex | 0 |
| pdflatex 2 | 0 |
| pdflatex 3 | 0 |

Final-log scan found no `Warning`, `Overfull`, `Underfull`, undefined
citation/reference, or multiply-defined-label line.

## PDF audit

```text
pages=4
page_size=A4 (595.276 x 841.89 pt)
file_size=362516 bytes
pdf_sha256=e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667
round0_sha256=e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667
main_vs_round0_cmp=0
```

All four pages were rasterized at 130 dpi and visually inspected.  No
clipping, collision, bad line break, orphan reference page, or malformed
formula was found.  The six references fit on page 4 with readable type.

`pdfinfo` reports blank Title, Subject, Keywords, and Author metadata.
`pdffonts` reports `emb=yes` for every font row.  The visible author is
`Anonymous`.

## Reproducibility controls

```text
main.tex
be420329b9b14f489536f808448e8c2729462310dac786abbf500a366bddabae

references.bib
32c4d786ead0bd833713fa1609a76abdd612829c7739ccf088d90a7d8079328c

main.pdf = main_round0_original.pdf
e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667
```

Round0 is frozen and must not be overwritten.  Subsequent successful review
repairs will create `main_round1.pdf` and `main_round2.pdf`.

External status: `HOLD_EXTERNAL`.

## Round1 isolated build

Date: 2026-08-31 UTC.  After implementing the three MINOR repairs in
`HOSTILE_REVIEW_A.md`, the final source pair was copied into the fresh
directory `/tmp/p128-round1-final2-YzXGL0` and built through the same four
stages.  The stage statuses were `0,0,0,0`.  The final log has no LaTeX or
package warning, overfull/underfull box, undefined citation/reference,
rerun request, or multiply-defined label.

```text
pages=4
page_size=A4 (595.276 x 841.89 pt)
file_size=386639 bytes
main_tex_sha256=fa1c10facf18dbb215896da5d4e6b36af446ce60f85208c1a632159f4d0ee1c7
references_sha256=32c4d786ead0bd833713fa1609a76abdd612829c7739ccf088d90a7d8079328c
pdf_sha256=f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439
main_vs_round1_cmp=0
round0_sha256=e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667
```

All four final pages were rasterized at 130 dpi and visually inspected.
The fixed-cut sentence and the new transfer-matrix control are visible; no
clipping, collision, malformed formula, bad break, or orphan reference page
was found.  `pdffonts` reports every font embedded.  `pdfinfo` reports blank
Title, Subject, Keywords, and Author metadata, while the visible author is
`Anonymous`.  `main.pdf` and `main_round1.pdf` are byte-identical;
`main_round0_original.pdf` remains unchanged and distinct.

Independent Review B repeated the canonical, isolated-build, four-page
visual, 28-font, and anonymous-metadata checks and returned zero findings.
`main_round2.pdf` is byte-identical to `main_round1.pdf` and `main.pdf`, with
SHA-256
`f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439`.
External status remains `HOLD_EXTERNAL`.

## Paper-local final QA

Final QA on 2026-08-31 UTC reran the canonical verifier and obtained a
byte-identical 1,712-byte transcript with **180,453 assertions**.  A fresh
isolated four-stage build from only `main.tex` and `references.bib`
reproduced `main.pdf` byte for byte; its settled log and BLG have no error,
warning, undefined item, bad box, or actionable rerun request, and all 6
bibliography items close.

The final `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` remain
byte-identical at 4 A4 pages and 386,639 bytes.  The reviewed PDF hash is
unchanged, so the all-page visual, 28-font, and anonymous-metadata evidence
from the two independent reviews applies exactly to the frozen artifact.
`FINAL_QA.md` records the terminal checks and `SHA256SUMS` freezes the
paper-local package.  Internal status is `GO_INTERNAL`; external status is
`HOLD_EXTERNAL`.
