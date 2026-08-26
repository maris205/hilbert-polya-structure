# Papers 67--71 Stage-4 bounded-revision checkpoint

Date: 2026-08-26 UTC  
Revision round: 1  
Authority: exact author-adjudicated Stage-3 roadmap items  
Release state: **HOLD**

## Outcome

Stage 4 is complete for all five papers. Sixteen author-authorized block
operations were applied against the immutable Stage-3 review surfaces. Every
operation passed its block/hash precondition and author-authorization witness;
all five revised mirrors replay through a valid Revision-Evidence Bundle. The
corresponding LaTeX sources were transported, all five deterministic controls
passed again, and all five papers compiled to final PDFs.

The round resolves 12 roadmap items. Three optional items are retained as
deliberate limitations, and five specialist exact-neighbour items remain
genuinely unresolvable inside an author-side internal round. No new reference
was added, no specialist or priority clearance is inferred, and external
release remains on hold.

| Paper | Concrete Stage-4 advance | Roadmap disposition (`resolved / limitation / unresolvable`) | Patch ops | Preserved blocks | Final PDF |
|---|---|---:|---:|---:|---|
| P67 | Defines total correlation before theorem use and adds an exact nonprime `F_4 = F_2[u]/(u^2+u+1)` control covering prefix ranks, all 4096 subsets of `[12]`, rectangles, and Haar forest/cycle counts. | 2 / 1 / 1 | 2 | 96/98 (0.9796) | 11 pages; `cee9a255bbb805601531855c38512bcb011868825786f4dd56747055ce432454` |
| P68 | Makes the classification-to-mechanism hierarchy explicit, supplies a statistical-mechanics dictionary for the two sectors, and hardens the boundary with the singleton `K_(1,1)` and `K_(1,6) <-> K_(2,3)` controls. | 3 / 0 / 1 | 3 | 58/60 (0.9667) | 7 pages; `a8e3491df2ce91ea43c5d1161c0300bb77209bd939f064c6dea20fdb2f8130e9` |
| P69 | Corrects the proof map to three stages and adds an exact two-degree mixed-indicator synthetic fixture that recovers total, self-dual, and signed multiplicities through the three Vandermonde systems. | 2 / 1 / 1 | 2 | 113/115 (0.9826) | 11 pages; `b45b6839b02cd7b285cab4b90753285d6c47f4b109a4461cce92bfc42b031b14` |
| P70 | Adds a five-row theorem-component owner comparison, a bounded code-dimension/zero-eigenspace bridge with explicit nonclaims, and an exact non-split `F_4` fixture for the ground-field gcd degree. | 3 / 0 / 1 | 5 | 68/71 (0.9577) | 8 pages; `3091437f38faa5ef271fb2185e1c6fa7760e0762a296948c4a2d64fa012e8f9d` |
| P71 | Narrows the headline to a ledger-supported residual package, adds a seven-row theorem-component comparison retaining HIGH collision risk, and verifies repeated endpoint fibres with masses 2 and 8 and limits `log 2`, `log 8`. | 2 / 1 / 1 | 4 | 68/71 (0.9577) | 10 pages; `a8c7555a8445b22d18f23cf191beb486eb41131a0218b80d4f8aea51564ee246` |

The marker-stripped revised mirrors add 1,054 whitespace-delimited words in
total: P67 `+59`, P68 `+151`, P69 `+51`, P70 `+372`, and P71 `+421`.

## Authority and evidence replay

| Check | Result |
|---|---:|
| Author-adjudication inputs and outputs | schema-valid 5/5 |
| Patch format and base/block preconditions | PASS 5/5 |
| Author-authorization witness | PASS 5/5 |
| Patch operations | 16/16 applied |
| Structural escalation flags | false 5/5 |
| Revision-Evidence Bundles | canonical replay PASS 5/5 |
| Frozen Stage-3 base/manifest/roadmap hashes | unchanged 15/15 |
| TeX transport receipts | PASS 5/5 |
| New bibliography entries | 0 |
| Deterministic controls, baseline and final | PASS 5/5 in both runs |

P70's replacement of `B0056` is attributed only to the EIC roadmap item and
uses the explicit collateral authorization
`COLLATERAL-AUTH-P70-EIC-over-R2-B0056`. It does not claim that the Domain
specialist item was resolved.

The five claim-surface manifests intentionally register no independently
authorized semantic claim surface. Consequently, every apply report records
`unregistered_claim_drift_review_required: true`. This is an honest handoff to
Stage 3-prime verification review, not evidence that drift is absent and not a
failure of the exact author-bound patch replay.

## Compile and PDF QA

`latexmk` was unavailable in the environment. The documented fallback chain
used `pdflatex`, `bibtex`, then two further `pdflatex` passes. All five builds
finished with exit code zero. Final log scans found no LaTeX error, undefined
reference/citation, multiply-defined label, overfull/underfull box, or fatal
warning. All listed PDF fonts are embedded and subsetted; `pdftotext` succeeds
for every paper.

Seventeen pages covering every modified presentation surface were rasterized
and visually inspected. No clipping, overflow, unreadable table, malformed
box, or broken page was observed. The exact page ledger is in
`stage4/VISUAL_QA_RECEIPT.md`.

## Response and release boundary

Every paper now has a complete Round-1 response, an operation-by-operation TeX
transport receipt, and a checksum manifest. The responses mark each external
specialist request `UNRESOLVABLE` rather than replacing independent expertise
with internal search or author self-certification. Optional application or
extension work in P67, P69, and P71 is recorded as a deliberate limitation.

No venue was supplied, so calibration remains `NOT_CALIBRATED` with
`criteria_binding_unavailable`. Public posting, submission, external
circulation, author/editor contact, and priority claims remain prohibited.

## Next internal stage

The next stage is **Stage 3-prime verification review**. It will verify the
registered and unregistered claim-strength delta, response-to-reviewer
coverage, deterministic-control receipts, and final PDF/source consistency.
It does not reopen Stage 4 or authorize external release.
