# C152 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `10ace603f2a1a7cdd9c10a6ee73b7950e5dcde6dc6f4459d6ce6a3559e84d68a`
- PDF: `paper/main.pdf`
- PDF SHA-256: `d028843b5606cec8609f37c616584731637f7bff42df0bb06c4ae6fe48cd2b68`
- Pages: 1
- File size: 264,054 bytes
- Engine: pdfTeX 1.40.22
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`

## Retained revisions

- Round 0: `6a72aaedde76f9fa328523816fc0c4a72f20e51c36591150edbf93f24ac34c33`
- Round 1: `f2941ac7a65689a651e2764747b5cc6dd4240c993eee89478399c57b23de0c6d`
- Round 2/final: `d028843b5606cec8609f37c616584731637f7bff42df0bb06c4ae6fe48cd2b68`

## Verification

Two fresh isolated fixed-epoch builds both produced the final hash above and
were byte-identical to `main.pdf` and `main_round2.pdf`.  Their logs contain no
warning, overfull/underfull box, badness, undefined reference/citation, or
multiply-defined label.  Every font is embedded; `pdfinfo` and `pdftotext`
succeed without unresolved markers.

The one-page artifact was rendered at 140 dpi and visually inspected.  The
title, factorization, asymptotic derivation, exact-validation paragraph, scope
boundary, and footer are fully visible with no collision, clipping,
truncation, or unreadable text.
