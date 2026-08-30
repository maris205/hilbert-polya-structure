# Improvement log — P123

External status: **HOLD_EXTERNAL**.

## Review A to round 1

Review A returned `GO_INTERNAL` with no critical or major finding and two
minor support/control findings.

1. Replaced the claim of two *independent* proof routes by the exact claim
   that the pointwise and labelled-enumerative routes are complementary.  The
   EGF construction now explicitly says that it translates the already-proved
   pointwise depth recursion.
2. Corrected the claim ledger's theorem numbers.  Rather than merely narrow
   its evidence language, strengthened the paper-local verifier to assert,
   for every labelled graph through order six, component refinement, equality
   of literal orbit depth with the independently evaluated split clock, both
   fixed/recurrent iff criteria, and both literal censuses.  The canonical
   assertion count increased from 67,758 to 203,244.

No theorem statement or owner ceiling was relaxed.  The original PDF remains
frozen as `main_round0_original.pdf`; the rebuilt repaired manuscript is
`main_round1.pdf` pending Review B.

## Review B to round 2

Review B returned `GO_INTERNAL` with zero critical, zero major, and three
support-reporting minors.  Round two:

1. labels the live package as round two rather than round zero;
2. adds P122 to the collision register and zero-credits generic
   parity-selected-block/sharp-clock language; and
3. distinguishes statewise iff checks from per-order aggregate census checks,
   while documenting `connected[0]=1` as an unused empty-state print sentinel.

No manuscript, theorem, verifier, canonical transcript, bibliography, or PDF
changed.  `main_round2.pdf` is intentionally byte-identical to
`main_round1.pdf`; external status remains HOLD.
