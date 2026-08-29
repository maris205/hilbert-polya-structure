# Consolidated hostile review — P105

Audit date: 2026-08-29 UTC
Disposition: **GO for internal Stage 2 after evidence-language repair / external HOLD**

Two reviewers independent of the P105 author reconstructed the map in
sequence.  Their complete records remain in `HOSTILE_REVIEW_A.md` and
`HOSTILE_REVIEW_B.md`.

## Severity ledger

- unresolved mathematical CRITICAL: **0**;
- unresolved mathematical MAJOR: **0**;
- repaired evidence-semantics MINOR: **1**;
- unresolved release-only direct-owner gate: **1**.

Both reviews independently derived the exact iterate, longest-cycle depth,
restricted-cycle layers and recurrence, unique recurrent point, formal zeta,
and every factor in the label-sensitive one-step fibre formula.  In
particular, they rechecked the nested eligible-label factor `e_i-i+1`, the
`ell_i` cyclic insertion positions, the unmatched involution factor
`I_(f-r)`, the Garden-of-Eden threshold, and the `n=1,2,3` endpoints.

Review B repaired one evidence-label error.  The value 1,981,326 counts
nontrivial **trajectory-step evaluations over all starting permutations**;
the same functional-graph edge can be traversed repeatedly.  It is not a
count of distinct edges.  The verifier key, stored output, manuscript,
README, claims ledger, and control report now use that precise convention.
No theorem or assertion count changed.

## Final evidence gate

The verifier exhausts every permutation in `S_1` through `S_9`, follows all
409,113 starting states, compares the closed fibre formula with every literal
indegree, extends the restricted-cycle recurrence through `n=50`, and checks
the Möbius/zeta ledger through period 60.  A final replay reports
**17,219,241 exact assertions** and byte-identical stored output.  The
four-stage build passes and yields a clean **5-page A4 PDF of 331,334 bytes**;
24/24 font records are embedded, subsetted, and Unicode-mapped, and the
modified final page passed visual inspection.

Classical labelled-cycle enumeration, longest-cycle laws,
deletion-consistent structures, and Artin--Mazur bookkeeping are positively
attributed.  The bounded search did not locate the same simultaneous labelled
surgery and reverse-fibre theorem, but it cannot grant priority.  External
posting, submission, contact, venue choice, and novelty or priority language
remain **HOLD**.
