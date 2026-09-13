# Round 10 Papers 29--33 — Stage 4.5 Round 2 final-integrity report

Date: **2026-09-05**  
ARS mode: **Stage 4.5 / Mode 2 final verification**  
Batch scientific-integrity verdict: **0/5 PASS; five fail-closed correction checkpoints**  
Audit-package replay: **PASS (89/89 checks)**  
Stage 5: **not started and not authorized**

## Outcome

The audit packages are structurally coherent and independently replayable, but none of the five
papers is eligible to enter Stage 5.  `PASS` here applies only to the audit machinery; the controlling
per-paper decisions remain `FAIL` or `FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED`.  These findings do not
say the underlying mathematics is false.  They identify unsupported, contradictory, or
same-lineage-evidence surfaces that must be corrected first.

| Paper | Refs / contexts | Claims (V/U/MD) | Evidence rows (V/U/MD) | Main blocker | Verdict |
|---|---:|---:|---:|---|---|
| P29 | 22 / 22 | 67/20/2 | 153/106/9 | translated status contradiction; 20 compound claims with missing raw components | FAIL |
| P30 | 28 / 30 | 96/4/7 | 457/17/68 | wrong correction relation; false review-role enumeration; Livsic passage; stale search/rerun status; AI metadata | FAIL |
| P31 | 24 / 26 | 119/6/2 | 2007/361/102 | P31-S23/S24 passages; overbroad literature negative; stale reader manifest; AI metadata | FAIL |
| P32 | 30 / 30 | 90/6/2 | 236/36/2 | translated status; five local raw gaps; CW01--CW04 excerpt binding | FAIL |
| P33 | 22 / 48 | 314/62/0 | 314/85/0 | 48 passage gaps; same-lineage synthetic oracle/harness | FAIL |

Totals: **126 references, 156 citation contexts,
797 registered claims, and 3,953 shared
evidence rows**.  Claim-level outcomes are
**686 VERIFIED /
98 UNVERIFIABLE /
13 MAJOR_DISTORTION**;
shared EVRs are **3167/605/181**.  For P29--P32,
3502 dependency components were independently cataloged:
**3408/68/26**.
Component, claim, and shared-EVR denominators are deliberately distinct:
Schema-5 propagates a compound claim's weakest verdict to every row sharing its claim ID without
reclassifying every supported component as defective.

The originality pass records
**269/371**
successful body-paragraph searches and
**206/206** changed
paragraphs covered.  These are audit/bookkeeping totals, not pooled scientific samples or new
experiments.  Preview-page and E6-operation totals are intentionally omitted from this batch
summary because they are not scientific outcomes and are already preserved in their per-paper receipts.

## Paper-level correction direction

- **P29:** correct B0006's translated locator-status sentence; conservatively narrow the unsupported
  components in the 20 affected compound claims.  The earlier fixed-preamble persistence defect is
  corrected in the audit artifacts; no claim was promoted merely because an audit report described it.
- **P30:** bind P30-S02 to correction DOI `10.1063/1.457672`, preserve the separate C01/C02
  relations, correct B0061's role enumeration against the actual review records, narrow the
  unsupported Livsic attribution in B0004/B0057/B0096, reconcile B0108 with the already frozen
  dated search replay, narrow B0124 to locked AI metadata, and correct B0125's now-false statement
  that this exact Round-3 draft has not received Stage 4.5 replay.
- **P31:** treat P31-S23/P31-S24 as metadata-only wherever no original passage is bound, narrowing
  four affected prose blocks; narrow the overbroad literature-negative claim to the admitted
  project-use boundary; correct B0079/B0105's reliance on a stale reader manifest; and narrow the
  AI-history disclosure to locked metadata.
- **P32:** correct B0007's translated status, keep CW01--CW04 explicitly unverifiable, and narrow
  the five local compound claims whose raw activity/author/provenance component is absent.
- **P33:** narrow all 48 source-dependent contexts that lack passage evidence.  For Mode 4, take the
  no-new-execution branch and remove evidentiary interpretation of the same-lineage 14/14 synthetic
  harness while preserving it as a diagnostic record.

The exact next-scope request is [BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.md](BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.md); its machine form binds 66
normalized blocks plus the single P30-S02 Bib entry by full SHA-256.  No repair has yet been applied.

## Route-A correspondence and frozen systems

Stage 4.5 is an integrity gate, not a Route-A coordinate.  Under
[`skills/route-a-evaluator.md`](skills/route-a-evaluator.md), formal Route-A tuples remain **0/5**,
positive-arithmetic A2 remains **0/5**, and A3/A4 remain **0/5**.  Under
[`skills/route-b-evaluator.md`](skills/route-b-evaluator.md), Route-B invocations remain **0/5**.

The five initial systems remain frozen: the level-(3) Gaussian Bianchi flow; the physical
three-disk flow at `d=6a` plus its separate symbolic calibrator; the positive Level-11 time change;
the pure genus-two homology-cover tower; and the Bolza `b=1/2` magnetic precursor with geodesic
control.  This audit makes no new dynamical-system test and changes no initial restriction.

## Independent replay and boundaries

[`tools/audit_round10_stage4_5_round2.rb`](tools/audit_round10_stage4_5_round2.rb) recomputed the
119 locked file bindings, 15 science-tree hashes, all registered claim spans, official coverage,
evidence and Schema-12 checks, catalog-to-EVR joins, raw UTF-8 spans, transitive lock chains, P30's
fresh authorized Crossref provenance, per-paper FAIL blockers, Route state, and Stage-5 closure.

```text
Checks passed: 89
ROUND10_STAGE4_5_ROUND2_AUDIT_PASS
```

The machine-readable batch audit is `BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_AUDIT.json`.  Manuscripts, bibliographies,
canonical PDFs, code/experiments/results, Route evaluators, initial-system definitions,
README/status files, and Git were not changed by this closeout.
