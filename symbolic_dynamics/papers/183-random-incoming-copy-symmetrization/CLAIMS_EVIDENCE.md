# Claims-to-evidence ledger — P183 final freeze

| claim | deductive location | exact author-side pressure |
|---|---|---|
| conflict-star deletion, idempotence, and recurrence | Lemma 2.1 and Corollary 2.2; Proof Package Steps 1–2 | every state/action through `n=4` |
| independent-set absorption CDF | Theorem 3.2; Proof Package Step 3 | every conflict graph through `n=4`, every history length `0<=t<=n` |
| first-occurrence-order endpoint kernel | Theorem 4.1; Proof Package Step 4 | every conflict graph through `n=4`, all support/order classes and literal histories through `t=n` |
| labelled predecessor/action count | Theorem 5.1; Proof Package Step 5 | every target through `n=4` |
| distinct predecessor-state count | Theorem 5.1; Proof Package Step 6 | every target through `n=4` |
| `n=1`, `t=0`, symmetric-source and zero-fibre boundaries | statements and proofs throughout | explicit exhaustive inclusion |

The proof establishes the all-parameter claims.  `code/verify_p183.py` is
author-side regression code derived from the theorem specification; it is not
itself an independent review and is not novelty evidence.  Two fresh runs each
completed 47,033 assertions and matched `code/CANONICAL.txt` byte for byte.
Two process-separated hostile controls later rechecked the claim set through
different state representations and closed with zero findings.

Shared reciprocity, semigroup, coupon, Stirling, independence-polynomial, and
finite-graph vocabulary receives zero contribution credit.  The exact internal
subtraction against P145, P159, P177, and P179 is stated in Section 1.
