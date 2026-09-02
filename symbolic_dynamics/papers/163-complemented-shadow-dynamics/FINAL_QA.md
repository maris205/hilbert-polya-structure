# P163 final QA — Complemented-Shadow Dynamics

**Decision:** `PASS_INTERNAL / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Mathematical and review closure

- The author verifier replay matches `code/CANONICAL.txt` byte for byte and
  reports **1,430,898** exact assertions; transcript SHA-256 is
  `21d2dc8e66580e7b78ef9c4bd2bda3eaa393757ee466497a62defb0f15700434`.
- Hostile Reviews A and B both returned
  `0 Critical / 0 Major / 0 minor` after **356,948** and **1,041,401**
  independent assertions.  No repair or finding remains open.

## Frozen artifact

Round 0, Round 1, Round 2, and current PDFs are byte-identical at SHA-256
`899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`.
The final artifact is five A4 pages, 424,998 bytes, with 32/32 font rows
embedded, subsetted, and Unicode mapped.

Two final source-only builds reproduced the current PDF byte for byte.  The
settled logs and BibTeX output contain no genuine warning, error, undefined
reference/citation, rerun request, or bad box.  Metadata is non-identifying,
the byline is anonymous, `HOLD_EXTERNAL` is visible, and all pages passed
144-dpi visual inspection.
