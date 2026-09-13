# Score History

The review evidence supplied to this workflow contains candidate-gate scores,
not a complete seven-axis venue review.  Missing values are left missing
rather than reconstructed.

| Stage | Novelty / 10 | Standalone size / 10 | Proof-completion confidence | Verdict | Provenance |
|---|---:|---:|---:|---|---|
| Initial embedded-formal proposal | not supplied | not supplied | not supplied | REVISE | defects reconstructed in `round-1-review.md` |
| Strengthened normalized-cover proposal, majority | 6.8 | 7.4 | 0.74 | GO | supplied final gate evidence |
| Strengthened normalized-cover proposal, dissent | 4.5 | 3.9 | not supplied | STOP / MERGE concern | supplied dissent; preserved separately |
| Independent source R1 after direct-prior correction | 4.8--5.5 | 4.5--5.5 | theorem audit found no blocker | REPAIR_REQUIRED; leans dissent | immutable R1 review, SHA-256 `d9ba3def010fea36bf8d0613ad6ca2d66cb2c4f00e412bf582d069a023acbc06` |

The first three rows are historical records and remain unchanged.  The R1
ranges are a conservative, provisional, author-side/R1-informed rescore after
disclosing Morton's direct scalar \(\rho\) generator for every \(d,n\), his
scalar \(\tau\) generator for \(d=2\), and Cantat--Dujardin's formal
trace-spectrum adjacency.  They are not a consensus, an average, or a
replacement verdict.  The normative lifecycle is `SOURCE_LOCKED_V2 /
PENDING_INDEPENDENT_R2 / NO_CODE / NO_RESULTS`.

`criteria_binding_unavailable`: no target venue was supplied, so no numerical
venue-readiness score is inferred.  The majority and dissent are not averaged.
All review roles available in this refinement used the same model family; the
scores therefore carry a correlated-error limitation.  Fresh independent R2
must review the corrected, hash-bound v2 package before any implementation.
