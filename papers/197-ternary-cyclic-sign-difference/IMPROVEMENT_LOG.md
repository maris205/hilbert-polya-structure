# P197 improvement log

## Before Round0

- Replaced implicit fibre gap-merging with an explicit rank-one product and
  a global Fibonacci bound; no merge-by-merge strictness claim remains.
- Expanded the four-phase sharp trajectory and no-early-entry coordinates.
- Qualified the n2,3 sharp witness to 0^(n-1)1; retained counterexamples to
  the overly general historical witness assertion in a separate erratum.
- Added an all81-coefficient Newton certificate for the core characteristic
  polynomial rather than only checking a fitted recurrence on small n.
- Preserved exact P164 projection, bounded Fuks nonassociativity comparison,
  source-access limits, no external novelty clearance and HOLD_EXTERNAL.

## Review A / Round1

The independent review at docs/papers197_201_sequence/reviews/p197_a/
accepted the frozen manuscript without changes. Root read its full evidence,
checked all pins/manifests and independently replayed4,814,623assertions,
including a fresh byte comparison. See ROUND1_RECEIPT.md. No new defects or
author edits were invented to satisfy a repair quota.

Round1 is byte-identical to Round0. The two small-boundary concerns above
were fixed BEFORE Round0 and do not count as review-induced repairs.
Review B and terminal QA remain outstanding; no final completion is claimed.

## Review B / Round2

The separate B process used radix-3/binary lifting, source/sink inverse
levels and an SCC/Bareiss polynomial certificate. It accepted no change,
C0/M0/m0. Root read all evidence, checked pins/manifests and freshly replayed
4,833,354 assertions byte-identically. ROUND2_RECEIPT.md records the new
physical unchanged freeze. Terminal double builds, final views and manifests
are pending; the earlier pending sentence describes the Round1 checkpoint.
