# P140 Round-A build and artifact record

## Status

`ROUND1_COMPILE_PASS / REVIEW_A_REPAIR_CLOSED / ISOLATED_REPRODUCIBILITY_PASS / HOLD_EXTERNAL`

Build date: 2026-09-01 UTC. After the `n=1` scope repair, the manuscript was
rebuilt with pdfTeX from TeX Live 2022 using the P132 four-stage protocol:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages exited zero. The settled `main.log` and `main.blg` contain no
LaTeX/package warning, error, undefined citation/reference, overfull or
underfull box, or rerun request.

## Round artifacts

| artifact | bytes | SHA-256 | role |
|---|---:|---|---|
| `main_round0_original.pdf` | 259,329 | `2b151d0916d8d43d26988f3f70a25885fdf8e71255657dc1486bc300e070aa99` | preserved pre-review freeze |
| `main.pdf` | 260,643 | `a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18` | repaired current PDF |
| `main_round1.pdf` | 260,643 | `a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18` | Round-A repaired freeze |

The current PDF is byte-identical to `main_round1.pdf` and deliberately differs
from the preserved Round-0 artifact. `main_round0_original.pdf` retains its
audited pre-review hash.

## Current source and control hashes

| artifact | SHA-256 |
|---|---|
| `main.tex` | `1e10db2a0bedadc9c35df6265867264813bf165298b83c16cc60434dcb158473` |
| `references.bib` | `ac64e59d8708acc0c757a7a2f6c49420c983a886dc3bf6672c70d1cae99b27a7` |
| `code/verify.py` | `3b66cd33bca07d3ea7ac2739eb226adb3b50204755596c561aa2885cd282a331` |
| `code/verification_output.txt` | `c23afcaf89ee9bf9ac5c2cd43ee72d6599155b9930215bf0dba0b4c328087ec8` |

Only `main.tex` changed among these four inputs. The bibliography, verifier,
and canonical transcript retain their Round-0 hashes.

## Isolated reproduction

The four stages were repeated in the initially empty directory
`/tmp/p140-roundA-iso.nka80e`, using the paper directory only through TeX and
BibTeX search paths. The isolated PDF compares byte for byte with the repaired
current `main.pdf` and has SHA-256
`a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18`.
Its settled logs are warning-free.

## Verifier and PDF checks

- Canonical verifier replay: `cmp=0`, 190,740 exact assertions PASS.
- Four pages, A4 (`595.276 x 841.89 pt`), PDF 1.5, unencrypted.
- Title, author, subject, and keyword metadata fields are blank; no custom
  metadata stream, form, or JavaScript.
- All 22 font rows are embedded, subsetted, and Unicode-mapped.
- `pdftotext` succeeds and returns 369 lines, 2,160 words, and 12,080 bytes.
- All four repaired pages were rendered at 150 dpi and inspected; the `n=1`
  boundary, `m>=1` Beta scope, Gamma-limit scope, equations, table, and
  references are legible without clipping or overlap.

The environment does not provide `latexmk`; the explicit four-stage protocol
above remains canonical. External status is unchanged.
