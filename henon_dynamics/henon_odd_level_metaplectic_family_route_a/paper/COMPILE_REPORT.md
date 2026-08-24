# Compile report

- Engine: pdfTeX 1.40.22 via latexmk 4.76
- Command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Source SHA-256: `4cadac9191ba6af8fb2a5d88e26fe166fc0e9ae1a5f32d9974c5b137697a55bc`
- Final PDF SHA-256: `ba2e47cbc73f27d5340d350fed108604a6bf3a55d717ac3784f1fd7f050acf88`
- Output: 3 US-letter pages, 220,942 bytes, PDF 1.5
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787529600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`

## Preserved rounds

| PDF | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `19eab41edc980f7fd0a8bbce5377fe84dba07dcc96e72fd0fed3133b76acf505` |
| `main_round1.pdf` | `740843eec7c22a6fa6c0740eea095068eeb39b09e37852fe4ffcd19387343e17` |
| `main_round2.pdf` | `ba2e47cbc73f27d5340d350fed108604a6bf3a55d717ac3784f1fd7f050acf88` |

`main.pdf` and `main_round2.pdf` are byte-identical.  The historical Round 0
and Round 1 files were not changed by the release-integrity reconciliation.

## Verification

- Two fresh isolated latexmk builds started from only `main.tex`; both output
  hashes equal the checked-in final PDF hash.
- Every font reported by `pdffonts` is embedded and subset.
- The final logs contain no warning, overfull/underfull box, undefined
  reference, multiply-defined label, or citation warning.
- All three pages were rendered at 150 dpi and visually inspected.  There is
  no clipping, collision, truncation, malformed formula, blank page, or broken
  table layout.
- Extracted text contains no unresolved `??`, `[?]`, `[VERIFY]`, `TODO`,
  `FIXME`, or `XXX` marker.

The frozen epoch removes creation-time metadata variance only and does not
alter mathematical content.
