# Round 9 Papers 24--28 — fresh Stage 4.5 Round 2 final-integrity report

Date: **2026-08-31**  
ARS mode: **Stage 4.5 / Mode 2 final verification**  
Batch verdict: **5/5 PASS**  
Next pipeline state: **Stage 5 not started; mandatory author confirmation required**

## 1. Outcome

Papers 24--28 have completed a fresh, from-scratch Stage 4.5 audit against the
exact derived drafts, bibliographies, original revision-evidence authorities,
canonical trees, result trees, Route evaluators, and experiment declarations
bound by
[`BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json`](BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json)
(SHA-256
`bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30`).

All five final Schema-5 handoffs have `verdict=PASS`, zero SERIOUS/MEDIUM/MINOR
issues, complete Phase-A--E populations, empty E6 finding sets, and all seven
ARS AI-research failure modes recorded under the exact taxonomy as `CLEAR`.
The batch audit does not promote any canonical manuscript, bibliography, PDF,
result, Route tuple, or initial dynamical object.

| Paper | References / contexts | Registry / evidence tuples | Originality / changed paragraphs | Fresh execution evidence | Verdict |
|---|---:|---:|---:|---|---|
| P24 Bianchi holonomy | 7/7 / 9/9 | 98 / 107, 0 anchorless | 45/85 / 35/35 | 81/81 unit tests; 10/10 derivative replay; 15-page preview | PASS |
| P25 three-disk scattering | 8/8 / 13/13 | 114 / 127, 0 anchorless | 45/74 / 17/17 | 75/75 environment-locked tests; 68-file inventory; two 2,241-row replays; 13-page preview | PASS |
| P26 Level-11 time change | 7/7 / 8/8 | 93 / 97, 0 anchorless | 47/89 / 39/39 | 84/84 unit tests; 18/18 Round-8 and 10/10 support replay; 16-page preview | PASS |
| P27 inverse-limit no-go | 5/5 / 5/5 | 87 / 87, 0 anchorless | 39/78 / 20/20 | 61/61 unit tests; 12/12 Round-8 replay; 13-page preview | PASS |
| P28 Bolza/magnetic precursor | 6/6 / 9/9 | 95 / 104, 0 anchorless | 44/77 / 5/5 | 108/108 unit tests; Round-3--8 two-run replay; 14-page preview | PASS |

Batch denominators are **33 references**, **44 citation contexts**, **487
registered claims**, and **522 persisted source-bound evidence rows**. The
originality searches succeeded on **220/403** body paragraphs, with every
Stage-4/4-prime new or materially changed paragraph covered (**116/116**).
These aggregate counts are bookkeeping totals, not pooled statistical samples.

## 2. Phase results

### Phase A — references

All 33 registered references have fresh A0 Semantic Scholar records and fresh
A1/A2 query/URL/result trails. The Tier-0 outcomes were 23 `S2_VERIFIED`, two
`S2_NOT_FOUND`, and eight `S2_API_UNAVAILABLE`; every not-found/unavailable row
was downgraded to DOI, arXiv, publisher, database, or other authoritative
existence and metadata review. No DOI-title mismatch remained.

P25's fresh check surfaced the linked erratum to
`GaspardRice1989Exact` (DOI `10.1063/1.457670`). Its corrections were compared
against both P25 contexts: they concern Equation (5.4), appendix notation, and
typography, not the abstract/Sections II--III multiple-scattering determinant
claims used at manuscript lines 75 and 160. The impact assessment is preserved
in P25's
[`stage4_5_round2_reference_citation_audit.md`](papers/25-three-disk-scattering-flow/notes/stage4_5_round2_reference_citation_audit.md).

### Phase B — citation contexts

All 44 current citation commands were checked against their registered sources
and locators. All bibliography keys resolve, no ghost or dangling citation
remains, and the current `plainnat` numeric convention is unchanged.

### Phase C — data and experiment provenance

Every registered statistical/data/result surface and every experiment-backed
claim was checked against the scholar-declared provenance. The exact mandatory
boundary is retained in every paper:

> This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

The audit replays claims against existing code, manifests, results, tests, and
receipts. It does not recast ARS as the scientific experimenter or silently
refresh canonical results.

### Phase D — originality and failure modes

Each counted paragraph has an 8--12-word quoted search and an unquoted
supplementary/paraphrase search with accessible, reviewable result titles,
URLs, and snippets. HTTP 429, HTTP 202 with no result cards, and other access
limitations do not count as successful searches. All changed paragraphs are
covered. The same-author bounded check includes Liang Wang's identified
searchable works, but no professional similarity system such as iThenticate or
Turnitin was available; therefore no global plagiarism percentage or universal
originality certificate is claimed.

The seven exact ARS classes are all `CLEAR` on the recorded surfaces:

1. Implementation bug passing AI self-review.
2. Hallucinated citation.
3. Hallucinated experimental result.
4. Shortcut reliance.
5. Implementation bug reframed as novel insight.
6. Methodology fabrication.
7. Frame-lock at early pipeline stage.

### Phase E — claims and E6

The official claim-registry coverage replay reports zero mechanically detected
unregistered candidates for every draft, while retaining
`semantic_extraction_coverage=not_machine_detectable`. Every selected
`(claim_id, ref_slug, anchor)` tuple has one official `evidence-row/1.0` row,
all 522 rows are source-bound `agent_extracted`, and no anchorless promotion is
used. Each current Schema-5 report embeds its complete evidence-row array.

E6 is bound to each original authorized revision-evidence bundle, not to a
substitute auxiliary bundle. All five finding sets are empty, with the exact
limitation **“none detected by the recorded model-mediated semantic review”**;
this is not a deterministic proof that semantic drift is impossible.

## 3. Intermediate QA defects that were not allowed to pass

The final PASS follows correction and full replay of the audit artifacts. It is
not the first generated label.

- P24 initially had seven mechanically detected unregistered candidates; all
  seven were added as exact byte-span registry claims before the final
  zero-gap replay.
- Early evidence artifacts collapsed some claims into ref-less rows or used a
  wrapper where the official source-map command required a pure
  `ref_slug -> session source string` map. The final tuple populations are
  exact and the required source maps pass the official validator.
- P27 initially counted one quoted search with HTTP 202 and zero result cards.
  That row was downgraded, a fresh successful dual-lane paragraph was added,
  and the final valid numerator is 39/78.
- Early originality/failure-mode summaries used custom status labels. The
  final artifacts use only the exact seven ARS names and the closed status
  `CLEAR`.
- Schema-5 reports that initially summarized evidence by count/hash were
  rejected. The final reports embed the complete evidence arrays as required.

## 4. Independent batch replay

[`tools/audit_round9_stage4_5_round2.rb`](tools/audit_round9_stage4_5_round2.rb)
reopened the input lock, recomputed canonical/result-tree hashes, replayed the
official registry and evidence validators, checked all claim spans and tuples,
validated E6 and Compliance Schema 12, checked originality denominators and
the exact seven-mode taxonomy, inspected Schema-5 handoffs/passports/build
receipts, and enforced the Stage-5 and Route boundaries.

For Git-clean reproducibility, the validator also binds the exact SHA-256
values of the thirteen LaTeX intermediates that were present when the input
lock was created but are intentionally excluded by the repository's
`.gitignore`. If one is present its bytes must match; if it is absent, only its
locked hash row is projected when reconstructing the original canonical-tree
commitment. No log or build intermediate is committed. Both the original
workspace and a clean Git clone independently pass the same 397 checks.

Final result:

```text
Checks passed: 397
ROUND9_STAGE4_5_ROUND2_AUDIT_PASS
```

The five direct unit suites were also independently rerun in the final
workspace: **409/409 tests passed**. P25 first failed exactly as designed when
its locked process environment was absent, then passed 75/75 under the required
`LC_ALL=C`, `TZ=UTC`, `PYTHONHASHSEED=0`, and
`PYTHONDONTWRITEBYTECODE=1` environment.

## 5. Route-A correspondence and frozen dynamical systems

Stage 4.5 is an academic-integrity checkpoint, not a Route-A coordinate. Under
[`skills/route-a-evaluator.md`](skills/route-a-evaluator.md), no positive
arithmetic candidate reached A2: **positive-arithmetic A2 remains 0/5**. P25's
`A2_ANALYTIC_DETERMINANT` belongs only to the explicitly nonarithmetic
unit-roof symbolic calibrator and transfers no credit to the physical
three-disk flow. Under
[`skills/route-b-evaluator.md`](skills/route-b-evaluator.md), **Route-B
invocations remain 0/5**.

The initial object restrictions remain:

- P24: a cusped finite-volume Bianchi 3-flow marked-word proxy; the full flow
  tuple remains unassigned.
- P25: a physical no-eclipse three-disk scattering flow and a separate
  unit-roof symbolic calibrator.
- P26: a positive Level-11 newform time change of the modular geodesic flow.
- P27: distinct residual inverse-limit and homology-cover geodesic candidates.
- P28: the frozen Bolza `b=1/2` magnetic precursor and its nonarithmetic
  genus-two geodesic control.

The batch still contains 12 frozen geometry/physics parameter instances plus
seven `q`-symbol calibrators, for 19 bookkeeping instances. They are structured
stress tests, not 19 statistically independent samples.

## 6. Frozen outputs and next checkpoint

All audit-draft, bibliography, original E6-authority, Route-evaluator,
canonical manuscript/PDF/bibliography, and result-tree bindings in the input
lock remain unchanged. The five isolated previews are diagnostic Stage-4.5
outputs only and were not promoted to `paper/paper.pdf`.

The only next pipeline action is the **mandatory explicit author confirmation
for Stage 5**. Until that confirmation is recorded, Stage 5, canonical
promotion, finalization, submission, Route B, and a new scientific round remain
closed.

Per-paper final reports:

- [P24](papers/24-bianchi-holonomy-flow/notes/stage4_5_round2_final_integrity_report.md)
- [P25](papers/25-three-disk-scattering-flow/notes/stage4_5_round2_final_integrity_report.md)
- [P26](papers/26-level11-newform-time-change/notes/stage4_5_round2_final_integrity_report.md)
- [P27](papers/27-congruence-inverse-limit-no-go/notes/stage4_5_round2_final_integrity_report.md)
- [P28](papers/28-bolza-magnetic-flow/notes/stage4_5_round2_final_integrity_report.md)
