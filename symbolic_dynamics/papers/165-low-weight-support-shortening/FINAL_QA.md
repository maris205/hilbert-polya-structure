# P165 final QA — Iterated Low-Weight Support Shortening

**Decision:** `PASS_INTERNAL / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Mathematical and review closure

- The author verifier replay matches `code/CANONICAL.txt` byte for byte and
  reports **605,733** exact assertions; transcript SHA-256 is
  `0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd`.
- Hostile Reviews A and B both returned
  `0 Critical / 0 Major / 0 minor` after **1,574,098** and **1,220,460**
  independent assertions.  No repair or finding remains open.

## Frozen artifact

Round 0, Round 1, Round 2, and current PDFs are byte-identical at SHA-256
`f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`.
The final artifact is four A4 pages, 288,837 bytes, with 23/23 font rows
embedded, subsetted, and Unicode mapped.

Two final source-only builds reproduced the current PDF byte for byte.  The
settled logs and BibTeX output contain no genuine warning, error, undefined
reference/citation, rerun request, or bad box.  Metadata is non-identifying,
the byline is anonymous, `HOLD_EXTERNAL` is visible, and all pages passed
144-dpi visual inspection.  Final closure also normalized five stale
Round-0 labels in supporting ledgers; no source, proof, verifier, or PDF was
changed.
