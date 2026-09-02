# P162 final QA — Random Translation Intersection

**Decision:** `PASS_INTERNAL / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Mathematical and review closure

- The author verifier replay matches `code/CANONICAL.txt` byte for byte and
  reports **1,712,974** exact assertions; transcript SHA-256 is
  `c31ec0a098bab52241eb2765bd6fef0669fdacdb4486ca69bea9dfc56fbab62b`.
- Hostile Review A returned `0 Critical / 0 Major / 1 minor`; the abstract's
  missing non-full-source qualifier was repaired without changing the
  theorem or verifier.
- Independent Hostile Review B ran **2,275,862** assertions and returned
  `0 Critical / 0 Major / 0 minor`.  No finding remains open.

## Frozen artifact

- Round 0 SHA-256:
  `e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46`.
- Round 1, Round 2, and current SHA-256:
  `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62`.
- The final artifact is four A4 pages, 399,828 bytes, with 30/30 font rows
  embedded, subsetted, and Unicode mapped.

Two final source-only builds reproduced the current PDF byte for byte.  The
settled logs and BibTeX output contain no genuine warning, error, undefined
reference/citation, rerun request, or bad box.  Metadata is non-identifying,
the byline is anonymous, `HOLD_EXTERNAL` is visible, and all pages passed
144-dpi visual inspection.

During batch closure, the two retained cold-log filenames were found to
contain a stale pre-repair byte count.  Both builds were rerun from the final
source, reproduced the final PDF exactly, and the two logs were replaced.
This was an evidence-ledger repair only; no source, theorem, verifier, or PDF
changed.
