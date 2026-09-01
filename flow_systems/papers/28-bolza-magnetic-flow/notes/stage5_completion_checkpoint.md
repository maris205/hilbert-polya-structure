# Paper 28 Stage-5 FULL completion checkpoint

Project: `28-bolza-magnetic-flow`  
Checkpoint type: `FULL`  
Date: `2026-09-01`  
Stage verdict: **PASS WITH DISCLOSED FONT-ACCESSIBILITY ADVISORY — final paper delivered**  
Pipeline state at checkpoint issuance: **Stage 5 complete; Stage 6 pending and not entered**  
Current terminal state: **Stage 6 skipped; pipeline completed**

## Stage result

The scholar-confirmed Stage-4.5 content was not changed.  Stage 5 produced a
byte-reproducible 14-page final PDF from the exact locked LaTeX and BibTeX
inputs, verified its extracted-text equivalence to the accepted content proof,
visually inspected every page, and completed the official package audit under
the advisory policy.

## Completion metrics

| Metric | Result |
|---|---:|
| Final PDF | 14 A4 pages; SHA-256 `be156f76...633cc9` |
| Independent deterministic builds | 2/2 byte-identical |
| Final/proof `pdftotext -layout` | byte-identical; SHA-256 `2e7c0210...f1ff` |
| Visual render inspection | 14/14 pages |
| Fonts embedded / subsetted | 17/17 / 17/17 |
| Explicit ToUnicode maps | 5/17; 12 legacy math fonts `uni=no`, same as accepted proof |
| Citation commands / unique keys / BibTeX entries | 9 / 6 / 6 |
| Missing / orphan / duplicate BibTeX keys | 0 / 0 / 0 |
| Fatal / undefined citation / undefined ref / overfull / missing glyph | 0 / 0 / 0 / 0 / 0 |
| BibTeX warnings | 0 |
| Stage-4.5 integrity authority | PASS; refs 6/6; contexts 9/9; claims 95/95; tuples 104/104 |
| Package verifier | pass 2; not-applicable 7; not-checked 5; warn 0; fail 0 |
| Verifier freshness | `report fresh (policy=advisory)`; no terminal token |
| Final-manifest hash replay | 17/17 rows match |

## Primary deliverables

- Final paper: `../stage5_finalization/paper.pdf`.
- Locked LaTeX: `../stage5_finalization/manuscript.tex`.
- Locked BibTeX: `../stage5_finalization/references.bib`.
- Accepted proof: `../stage5_finalization/content_proof.pdf`.
- Provenance/advisory carrier:
  `../stage5_finalization/provenance_summary.md`.
- Package verifier report:
  `../stage5_finalization/submission_verification_report.json`.
- Finalization report: `stage5_finalization_report.md`.
- Final manifest: `stage5_final_manifest.json`, SHA-256
  `6d5505a5cfda8f6810089e01f8884a7c9dadc6e1c64eac2be95187e8c63b1903`.
- Reproducible-build receipt:
  `stage5_build_artifacts/reproducible_build_receipt.json`.
- Collaboration Depth advisory:
  `stage5_collaboration_depth_advisory.md`.

## Significant scientific progress and Route correspondence

Paper 28 lands a substantive positive control: exact nonarithmeticity, a
finite completeness certificate below the frozen cutoff, and an exact systole
chain with primitive witness.  This removes a control-side ambiguity from the
Route-A programme.  It does not claim or execute the later
magnetic/arithmetic transfer.

Accordingly:

- Route A position: early control-infrastructure layer; formal P28 tuple still
  `UNASSIGNED`; no Stage-5 gate credit.
- Batch positive-arithmetic A2: `0/5`.
- Route-B invocations: `0/5`.
- Recorded model instances: 19; they are not independent statistical samples.
- Route evaluator hashes: unchanged.
- This integrity/formatting PASS is not a Route promotion.

## Required caveats

- #660 is still `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
  SNAPSHOT_NOT_PROVIDED`; no clean certificate exists.
- #672 is still
  `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`; no agreement or clean result
  exists.
- B1--B5 are `not_checked` because no venue profile is declared.  No venue
  compliance, venue fit, or submission readiness is claimed.
- Twelve legacy Computer Modern math fonts lack explicit ToUnicode maps in
  both final and accepted proof; full per-font ToUnicode coverage is not
  claimed, although embedding and accepted-proof text equivalence pass.
- Pandoc output is withheld because the preflight recorded material loss.
- No manuscript/declaration/bibliography/canonical-result/Route/subtype change,
  submission, release, external upload/contact, Git action, or
  corresponding-author designation occurred.

## Collaboration Depth observer

The observer window contains only two Stage-5 scholar turns.  The short-stage
guard therefore records Zone, Delegation Intensity, Cognitive Vigilance, and
Cognitive Reallocation as `insufficient_evidence`, without numeric scores.
This advisory is nonblocking and makes no inference about scholar ability.

## Post-checkpoint terminal disposition

On 2026-09-01 UTC the scholar answered the immediately preceding optional
Stage-6 decision with the exact response:

> 跳过，继续下一批

Under the ARS `checkpoint -> completed` transition, Stage 6 is `skipped` with
reason `user declined Stage 6`, and the pipeline global state is `completed`.
Stage 6 did not run, no Process Record was generated, no terminal
acknowledgement is required, and there is no next required ARS event. This
terminal decision does not change any Stage-5 deliverable, scientific content,
dynamical restriction, Route state, submission authority, or release boundary.

```text
Pipeline: [v]RES -> [v]WRT -> [v]INT -> [v]REV -> [v]REVISE -> [v]RE-REV -> [v]F-INT -> [v]FIN -> [-]SUMMARY (skipped) -> [v]COMPLETED
```
