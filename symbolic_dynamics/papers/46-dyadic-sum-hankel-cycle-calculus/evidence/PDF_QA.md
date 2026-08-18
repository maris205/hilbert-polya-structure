# Final PDF QA after ToUnicode delimiter repair

Status: `PASS`

The pre-repair PDF with SHA-256
`db4edcb3c366736f1812948beca8472c13914e815815dd3f353b0c9771ccef3c`
is permanently withdrawn.  It must not be used in a writer manifest, writer
seal, publication manifest, or publication seal.

## Repair scope

The only manuscript-source changes in this repair replaced five uses of
extensible or enlarged parentheses with ordinary fixed parentheses:

- the partial-fraction display in `sections/05_ideal_thresholds.tex`;
- the determinant-overlap display in
  `sections/06_valuation_determinants.tex`;
- the compression-square estimate in `sections/07_cycle_solver.tex`;
- the cardinality display in `appendices/C_cycle_bookkeeping.tex`;
- both trace parentheses in equation (D.1) in
  `appendices/D_canonical_evidence.tex`.

The mathematical expressions are unchanged.  The repair removes the
unmapped extensible-delimiter glyph pieces that had been extracted as illegal
C0 characters.

## Reproducible build

Two clean, isolated builds were made from the same source bytes with
`SOURCE_DATE_EPOCH=1787011200`, `TZ=UTC`, and `LC_ALL=C`.  Each build ran
`pdflatex`, `bibtex`, and two further `pdflatex` passes.  Both builds exited
zero and produced byte-identical PDFs, logs, and bibliographies.

| Artifact | SHA-256 |
|---|---|
| `main.pdf` and `main_round2.pdf` | `8772e8c9649bea045bace7b369d446ff51f5c9a7eb95c7e1bc957a9ff2f02d6e` |
| `compile.log`, `main.log`, and `evidence/FINAL_COMPILE.log` | `e458745557941be7d04e4d9420a308d4eb6dcf0092cdba619007ca820a595cdd` |
| `main.bbl` and `evidence/FINAL_BIBLIOGRAPHY.bbl` | `2bd8b051f978b0124a143c8cdc064218a7e9ff4740990dc16df302554439c6f7` |

The final PDF is 461,757 bytes, PDF 1.5, unencrypted, and contains 16 A4
pages.  The main text, conclusion, and references end on page 12; appendices
occupy pages 13--16.

## Text and accessibility checks

Illegal C0/DEL means U+0000--U+0008, U+000B, U+000E--U+001F, or U+007F;
ordinary tab, line-feed, carriage-return, and form-feed separators are not
counted.  The complete document was checked in all three extraction modes.

| `pdftotext` mode | Extracted characters | Illegal C0/DEL | C1 controls | U+FFFD | Text SHA-256 |
|---|---:|---:|---:|---:|---|
| default | 38,627 | 0 | 0 | 0 | `0275ee0a91afff5ea2cbc413fad4ef758e77a375fe8a0a4e4ebeabc983f20e31` |
| `-layout` | 53,311 | 0 | 0 | 0 | `708138601967252e8f2508371c9066e1f2a54f859da4c4e7f7f4f7241a91ac82` |
| `-raw` | 38,003 | 0 | 0 | 0 | `70d2dcb62aa207531f4944a416b65dabfead2a8f7f3217b8195597698c5df78e` |

Both `pdftotext -bbox` and `pdftotext -bbox-layout` produced well-formed XML
with zero illegal C0/DEL characters and zero U+FFFD replacement characters.
The bbox-layout output has SHA-256
`f36b45dac3c087b868afa4e62d99576025a6b2aeb28469f9917f67b0dc0323f1`,
contains 7,634 words, and has zero word boxes outside their page bounds.  All
27 reported fonts are embedded, subset, and Unicode mapped.

## Compile and visual checks

The final log contains zero undefined citations, zero undefined references,
zero LaTeX/package warnings, zero overfull boxes, zero underfull boxes, and no
fatal error.  Extracted text contains no `??`, `[?]`, `[VERIFY]`, `TODO`, or
`FIXME` marker.

All 16 pages were rendered and inspected.  No clipping, overlap, overflow,
missing figure, blank page, or unreadable label was found.  Pages 6, 9, 10,
15, and 16 were additionally inspected at higher resolution around every
repaired display; the fixed parentheses are balanced, legible, and do not
alter the surrounding layout.
