# Stage 2.5 final seven-mode failure audit — P67–P71

Date: `2026-08-26`  
Scope: corrected Round-1 manuscripts and their local provenance artifacts  
Posture: author-side internal audit, not external specialist or peer review  
External release: **HOLD**

The individual `INTEGRITY_AND_PRIORITY_AUDIT.md` files preserve the immutable
Round-0 findings.  Several Round-0 rows were correctly marked `FAIL` or
`SUSPECTED`; this file records the separate post-correction disposition.

| Failure mode | Final evidence after correction round 1 | Disposition |
|---|---|---|
| 1. Invalid proof or computation hidden by fluent presentation | theorem/proof chains checked in each paper; five deterministic controls replay exactly; finite controls are explicitly separated from infinite proofs | **CLEAR** |
| 2. Hallucinated, miscited, ghost, or dangling source | 38/38 final records field-verified; 72/72 contexts checked; zero ghost, dangling, or undefined keys; every registered metadata defect corrected | **CLEAR** |
| 3. Fabricated, misreported, or irreproducible experiment | no experiments or empirical datasets are declared; all scripts are finite proof-regression controls with frozen outputs | **CLEAR** |
| 4. Finite check promoted to an infinite proof | every paper states the control boundary; arbitrary-size results have manuscript proofs independent of the scripts | **CLEAR** |
| 5. Bug or convention mismatch reframed as an insight | formulas, tables, code branches, group/action conventions, and stored outputs reconcile; no unresolved discrepancy remains | **CLEAR** |
| 6. Method/result fabrication through unsupported provenance | 140 selected claims expand to 152 exact tuples: 47 source-bound rows, 105 explicit anchorless rows, zero manuscript-self sources; semantic extraction completeness remains non-machine-detectable | **CLEAR** |
| 7. Frame-lock or ignored neighboring terminology | alternate-term searches found omitted neighbors in P67, P69, P70, and P71; all were integrated or explicitly delimited in Round 1 | **CLEAR** |

The same seven checks are recorded paper-by-paper, yielding 35/35 `CLEAR`
rows.  No final row remains `SUSPECTED` or `INSUFFICIENT EVIDENCE` for the
internal content gate.  `CLEAR` is limited to the evidence and mechanism named
in each row; it does not convert bounded search into priority clearance.
Residual collision risks remain P67 `MEDIUM`, P68 `MEDIUM`, P69 `MEDIUM`, P70
`MEDIUM-HIGH`, and P71 `HIGH` for the pressure portion.

The required protocol boundary is retained verbatim:

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

For this theoretical batch, “experiment” in that sentence has no manuscript
referent.  It does not reclassify the deterministic controls as experiments.

Administrative declarations remain unresolved because responsible human
author identities and approvals were not supplied: author order and
contributions, funding, competing interests, venue-specific AI disclosure,
and final release authorization.  The author-overlap component of the
self-plagiarism screen is therefore
`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.  These are release blockers, not
content defects to be filled by inference.
