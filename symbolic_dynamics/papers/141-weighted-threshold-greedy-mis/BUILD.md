# P141 Round-A build and artifact record

## Status

`ROUND1_REVIEW_A_PASS / NO_SOURCE_CHANGE / ISOLATED_REPRODUCIBILITY_PASS / HOLD_EXTERNAL`

Build date: 2026-09-01 UTC. Hostile review A returned PASS with no repair
item. The unchanged manuscript was nevertheless rebuilt using the P132
four-stage protocol:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All stages exited zero. The settled `main.log` and `main.blg` contain no
LaTeX/package warning, error, undefined citation/reference, overfull or
underfull box, or rerun request.

## Artifact identity

| artifact | bytes | SHA-256 |
|---|---:|---|
| `main.pdf` | 254,394 | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round0_original.pdf` | 254,394 | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round1.pdf` | 254,394 | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |

All three PDFs compare byte for byte. Round A records a PASS freeze; it does
not imply a source repair.

## Unchanged source and controls

| artifact | SHA-256 |
|---|---|
| `main.tex` | `b312ca8becfcc405de8276195058b9876c8631ae0119b882a5bf4973db2d7f6e` |
| `references.bib` | `7a9bad554745322727fac587e773a862622e7f35d5e486bbf3e6f216376f1286` |
| `code/verify.py` | `25c3a0ba8d9f8134aeee42dd98176faedc84c5d7de8852afa527df8ae3b2b5e6` |
| `code/verification_output.txt` | `bcb2e2f68121a3c13e79e0987fcd1ee5e985b225f4a948357424ed70ee695502` |

## Isolated reproduction and PDF QA

The four stages were repeated in the initially empty directory
`/tmp/p141-roundA-iso.k1KfE6`. The isolated PDF is byte-identical to all three
paper-local PDFs; its settled logs are warning-free.

- Canonical verifier replay: `cmp=0`, 750,181 exact assertions PASS.
- Four pages, A4 (`595.276 x 841.89 pt`), PDF 1.5, unencrypted.
- Blank identifying metadata; no custom metadata stream, form, or JavaScript.
- All 20 font rows are embedded, subsetted, and Unicode-mapped.
- `pdftotext` returns 346 lines, 1,875 words, and 10,965 bytes.
- Since the current, Round-0, and Round-1 PDFs are byte-identical, the hostile
  review's 150-dpi four-page visual audit applies exactly to the frozen
  Round-1 bytes; fresh automated metadata/font/text checks also pass.

The environment does not provide `latexmk`; the explicit protocol above is
canonical. External status remains on hold.
