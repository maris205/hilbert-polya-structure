# P209 claims and evidence roles

This matrix records author assertions and their proof/check roles. It is
not an independent review, completed execution receipt or paper acceptance.

| Claim | All-parameter proof | Fresh paper-local finite test | Scope boundary |
|---|---|---|---|
| Recurrent iff labelled cycle/unbranched-path geometry with final labels below cycle minimum | PROOF_PACKAGE Steps 1–4; manuscript Theorem 1 | `graph_data` predicate versus `whole_orbit` from the literal transition for every n=0,...,5 state | Does not prove an entrance-time bound |
| Exact period equals LCM only over cycles with attached paths | Step 4; Theorem 1 | Every recurrent state, full orbit and attachment-coordinate check | Pure cycles fixed; no quotient by unlabelled symmetry |
| Every one-step inverse fibre is the admissible increasing-path decoder | Step 5; Theorem 2 | Every target and every eligible subset; complete decoded set versus complete brute-force source set | No general-time inverse, product formula or counting-complexity result |
| Unique global maximum 2^(n-1) for n>=1 | Step 6; Theorem 3 | All target fibre sizes and entire maximizer list, including n=0/1 | Consequence of this inverse, not another theorem mechanism |
| All vertex-image sets are monotone and frozen on recurrent orbits | Steps 1–2 inside Theorem 1 | Every depth up to n+1 in each finite box; all recurrent orbit states | Supporting lemma, not a separate novelty claim |

`verify.py` is fresh author code and imports only standard-library modules.
It reads no canonical data or old/gate mathematical implementation. Complete
JSON stdout is the canonical payload; runtime observations and actual raw
comparisons belong to separate execution receipts. Finite enumeration covers
3,414 states across the six original boxes and cannot establish the
all-parameter theorems. Observed entrance indices carry no all-size claim.

[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records primary and internal subtraction.
No author-level run, root collaboration or candidate gate counts as either
of the two required process-separated nonauthor manuscript reviews.
