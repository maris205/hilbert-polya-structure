# P179 improvement log

## Round 0 → Round 1

Hostile Review A found no Critical or Major defect and requested two boundary
clarifications.  The model now fixes `n>=1` before defining the operator
`P=(1/n) sum_i E_i`.  The contribution boundary now explicitly subtracts
P169's deterministic block-number-preserving successor transfer and P110's
cyclic shift--join coarsening; shared carrier and generic refinement/spectral
shells receive zero credit.

No theorem formula or author-control expectation changed.  The author
verifier still makes 125,118 exact assertions and replays byte-identically.
Round-1 PDF SHA-256:
`9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d`.

## Round 1 → Round 2

A late final science audit found one localized mismatch in the support
lemma's prose: it retained the residual block only at size at least two,
whereas the literal update, all downstream formulas, and the verifier correctly
retain every nonempty residual, including a singleton.  The lemma and proof
are corrected.  An exhaustive formula-versus-literal support oracle through
`n=7` adds 127,202 assertions, raising the author total from 125,118 to
252,320.

The original Reviewer A and Reviewer B then re-entered on the exact new
Round-2 source, replayed 120,977 and 209,583 independent assertions, and
closed with zero open findings.  Two fresh source-only cold builds reproduce
the Round-2/live PDF byte for byte, and all 3 rasterized pages pass visual QA.
Round-2 PDF SHA-256:
`6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`.
External status remains `HOLD_EXTERNAL`.
