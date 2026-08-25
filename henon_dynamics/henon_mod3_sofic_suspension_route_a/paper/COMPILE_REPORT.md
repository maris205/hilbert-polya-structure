# C140 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `30e3d05952958a31e41d4496c00dd0ae5cbba308ca02bc1f9932931089dd8eeb`
- PDF: `paper/main.pdf`
- PDF SHA-256: `1e41191864c8a54e672116e181d8be2dc40c27a82db2fefc542ecfe7552ed513`
- Pages: 2
- File size: 323,796 bytes
- Engine: pdfTeX 1.40.22
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`

## Retained revisions

- Round 0: `1f0436449b859c3b7e74cf00e0867a1cd243e621b305a820fe96e9d16fca9f65`
- Round 1: `8b4d31942d872d8e93ea9f7c0cabf130128f76e7eb745f2ba637a195e81d19dc`
- Round 2/final: `1e41191864c8a54e672116e181d8be2dc40c27a82db2fefc542ecfe7552ed513`

## Verification

Two fresh isolated `latexmk` builds at the fixed epoch both produced
`1e41191864c8a54e672116e181d8be2dc40c27a82db2fefc542ecfe7552ed513`;
they are byte-identical to one another, `main_round2.pdf`, and `main.pdf`.
Both isolated logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference/citation, or multiply defined label.  `pdffonts` reports
`emb=yes` for every font.  `pdfinfo`, `pdftotext`, and `pdftoppm` read the
artifact successfully; no unresolved marker appears in extracted text.

Both pages were rendered at 120 dpi and visually inspected.  There is no
clipping, collision, truncation, broken equation layout, unintended blank
page, or unreadable text.  The round-0 4.88pt overfull box is absent.
