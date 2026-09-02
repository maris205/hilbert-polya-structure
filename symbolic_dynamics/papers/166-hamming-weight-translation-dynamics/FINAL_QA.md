# P166 final QA — Hamming-Weight Translation Dynamics

**Decision:** `PASS_INTERNAL / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Mathematical and review closure

- The author verifier replay matches `code/CANONICAL.txt` byte for byte and
  reports **17,017,929** exact assertions; transcript SHA-256 is
  `7ef213d9334acc39c835f9c9da4b52f4581b423e76de82406d65ece73c55cc06`.
- Hostile Reviews A and B both returned
  `0 Critical / 0 Major / 0 minor` after **11,795,304** and **14,005,344**
  independent assertions.  Review B independently resolved the phase-anchor
  factor, the all-zero fibre correction, and the sharp triangular boundary.
  No repair or finding remains open.

## Frozen artifact

Round 0, Round 1, Round 2, and current PDFs are byte-identical at SHA-256
`f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`.
The final artifact is four A4 pages, 294,007 bytes, with 24/24 font rows
embedded, subsetted, and Unicode mapped.

Two final source-only builds reproduced the current PDF byte for byte.  The
settled logs and BibTeX output contain no genuine warning, error, undefined
reference/citation, rerun request, or bad box.  Metadata is non-identifying,
the byline is anonymous, `HOLD_EXTERNAL` is visible, and all pages passed
144-dpi visual inspection.
