# C151 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `c7159a7c6a322e04d1be2f340359fc1b04a9aa79424c8f1d338e42f8628d10bc`
- PDF: `paper/main.pdf`
- PDF SHA-256: `e2aed63c9da2e5af6fc5be41f8b618db19289c7355b2b269542cfef5ff25802e`
- Pages: 1
- File size: 270,624 bytes
- Engine: pdfTeX 1.40.22
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`

## Retained revisions

- Round 0: `61ee31892def787f5c577c0de77835e0847011ec22bc7ebcbbde9c0c254b6ce6`
- Round 1: `31386a49bd17e7255b2e9e6369e732ac58e3a7f80e2a7a4cba5d2be27f407929`
- Round 2/final: `e2aed63c9da2e5af6fc5be41f8b618db19289c7355b2b269542cfef5ff25802e`

## Verification

Two fresh isolated fixed-epoch builds both produced the final hash above and
were byte-identical to `main.pdf` and `main_round2.pdf`.  Their logs contain no
warning, overfull/underfull box, badness, undefined reference/citation, or
multiply-defined label.  `pdffonts` reports `emb=yes` for every font;
`pdfinfo` and `pdftotext` succeed without unresolved markers.

The one-page artifact was rendered at 140 dpi and visually inspected.  The
title, abstract, equations, exact table, scope boundary, and footer are fully
visible with no collision, clipping, truncation, or unreadable text.
