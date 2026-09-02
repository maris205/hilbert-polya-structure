# P31 Stage 2.5 E6 manual semantic comparison advisory

Date: 2026-09-03 UTC  
Frozen manuscript SHA-256:
`6023a33a4679a79c7c6cc8be8cf4345813a564b2fd420770618e7afa9547206a`  
Current manuscript SHA-256:
`f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a`

## Formal E6 status

The official ARS carrier remains
`stage2_5_claim_strength_drift_findings.json` with
`status=skipped_no_revision_evidence`,
`revision_evidence_bundle_sha256=null`, and an empty findings array. No
Revision-Evidence Bundle was supplied or constructed. This advisory is a
project-local human-readable comparison and is **not** an ARS
Revision-Evidence Bundle, detector result, or replacement for the official
carrier.

## Honest comparison of the authorized changes

| Surface | Frozen meaning | Current meaning | Strength assessment |
|---|---|---|---|
| `P31-E1-056` reconstructability | Said publishing any one of `G`, `I`, or `C` destroys information needed to reconstruct the other two, an overbroad symmetric assertion. | Says `G` alone or `C` alone cannot reconstruct occurrence-level `I`; a complete `I` can induce `G` and `C` under the stated projections, while separate materializations improve auditability. | **Narrowed and corrected.** This removes an unsupported universal claim and adds no scientific outcome. |
| `P31-E1-078` originality/novelty boundary | Said originality remained unassessed. | Reports only that a bounded Stage-2.5 textual screen found no exact match within its declared samples and corpora; scientific contribution novelty remains unassessed. | **Bounded workflow claim added after the declared screen; novelty is not strengthened.** The fresh 21/67 search plus mandatory review of both repaired paragraphs and declared local/public-corpus checks supports this limited wording. |

The bibliography is byte-identical to the frozen bibliography and the
manuscript diff contains no third hunk. Neither change reports a theorem,
experiment, owner partition, pair decision, `G/I/C` output, Route-A
promotion, or Route-B invocation.

## Recommendation

Keep the official E6 carrier in its current skipped state unless a genuine,
schema-valid ARS Revision-Evidence Bundle is independently supplied. If formal
claim-strength drift adjudication is required later, build that bundle from the
frozen and current byte spans, authorization receipt, and independently
adjudicated support artifacts, then rerun the official detector. Until then,
use this comparison only as advisory repair lineage and preserve the current
bounded originality-versus-novelty wording.
