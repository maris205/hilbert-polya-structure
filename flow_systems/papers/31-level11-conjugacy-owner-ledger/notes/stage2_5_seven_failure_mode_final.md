# Paper 31 Stage 2.5 seven-failure-mode final sidecar

Audit date: `2026-09-03 UTC`  
Frozen manuscript SHA-256:
`f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a`

## Decision

The seven-mode checklist finds **no `SUSPECTED` or `INSUFFICIENT EVIDENCE`
failure mode** within the declared P31 scope. This checklist therefore adds no
independent block. The authorized `P31-E1-056` and `P31-E1-078` repairs
were separately re-audited against the current registry and now pass Phase E.
This checklist still does not certify that the unimplemented canonicalization
theorem or certificate system is correct.

| Failure mode | Verdict | Evidence and explicit boundary |
|---|---|---|
| 1. Implementation bug passing self-review | CLEAR | P31 contains no implemented canonicalizer, producer, verifier, fixture run, owner partition, all-pairs result, or `G/I/C` output. The only arithmetic surface checked here, `binom(138,2)=9,453`, is exact. `code/`, `results/`, and `experiments/` contain no P31 scientific execution artifact. This does not certify the absence of an ordinary prose, definition, or future implementation error. |
| 2. Hallucinated citation | CLEAR | Phase A verified existence and metadata for 22/22 references; the deterministic Phase-B sample checked 7/22 broad citation contexts with 7 `ACCURATE_WITH_BOUNDARY` verdicts. The remaining contexts preserve Stage-1 source-fitness limits. All 22 citations remain `anchor:none`, so this verdict is bounded to nonfabrication and broad claim fitness and does not claim complete theorem-passage validation. |
| 3. Hallucinated experimental result | CLEAR | The manuscript repeatedly states `NOT_EXECUTED` and reports no run-derived scientific result, dataset metric, solver output, owner decision, theorem computation, or estimand table. Workflow/corpus counts are traceable to named Stage-1 artifacts and are not labeled experiments. |
| 4. Shortcut reliance | CLEAR | There is no trained model, predictive dataset, or executed solver whose performance could rest on a shortcut. The prospective design explicitly requires target-blind fixtures, exact subgroup/orientation/root checks, an independent verifier, and full 138-instance replay before population claims. This does not validate a future implementation. |
| 5. Bug reframed as a novel insight | CLEAR | No anomaly, failed run, implementation behavior, or numerical surprise is narrated as a discovery. The article types its contribution as review-informed certificate architecture, and the repaired conclusion limits its originality statement to the bounded textual screen while leaving scientific contribution novelty unassessed. |
| 6. Methodology fabrication | CLEAR | The only executed method claimed is closed-corpus literature synthesis plus documented review/adjudication; the corpus, source verification, four Phase-5 reviews, manifest, revision log, and rechecks exist. Canonicalization, certificate production, verification, fixtures, pair audit, and census are consistently prospective or absent. |
| 7. Early frame-lock | CLEAR | Phase-5 adversarial review explicitly challenged the earlier assumption that 9,453 bespoke pair certificates were foundational, and Revision 1 adopted a canonicalization-first design while retaining the pair table as a derived audit. The current manuscript preserves alternative implementation routes and fail-closed endpoints. The historical frame-lock signal was therefore surfaced and resolved rather than concealed. |

## Boundary notes

- The citation verdict does not change any evidence row: all 89 persisted rows
  remain `anchor.kind=none` and `anchorless`; exact claim-to-passage
  faithfulness remains unresolved beyond the bounded Phase-B review.
- Semantic extraction coverage remains `not_machine_detectable`; the checklist
  cannot prove that no unregistered semantic claim exists.
- The completed originality screen is a deterministic public-Web/local-corpus
  heuristic, not Turnitin or iThenticate. It found no exact-match signal within
  its declared samples and corpora but does not assess scientific contribution
  novelty or inaccessible/unindexed material.
- No manuscript, bibliography, PDF, registry, evidence-row, state, README,
  scientific artifact, or Route file was edited or evaluated by this sidecar.

## Aggregate disposition

| Verdict class | Count |
|---|---:|
| CLEAR | 7 |
| SUSPECTED | 0 |
| INSUFFICIENT EVIDENCE | 0 |

Seven-mode status: **CLEAR within the declared non-execution and anchorless
evidence boundaries.** The fresh Phase-E review passes all 71 selected claims,
including the two authorized repair surfaces.
