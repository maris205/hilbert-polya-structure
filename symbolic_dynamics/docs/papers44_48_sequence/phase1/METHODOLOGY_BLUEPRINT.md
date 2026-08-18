# Methodology Blueprint — Papers 44–48

## Research Design

**Paradigm:** Formal-deductive realism with falsification-first empirical
software checks. Mathematical objects and implications are treated as
objective; computational artifacts certify bounded instances and provenance,
not universal theorems.

**Approach:** Sequential multi-case design. First perform an exhaustive
repository census and primary-literature collision audit; then admit only
candidate-specific theorem packages that pass typed ownership and
independence gates. Downstream exact computation is confirmatory with respect
to a byte-frozen contract, but the overall candidate selection is explicitly
exploratory and retrospective.

**Method:** Secondary-document analysis, formal proof construction, exact
symbolic computation, independently implemented evaluators, adversarial
mutation testing, and content-addressed provenance auditing.

**Justification:** The primary RQ asks whether a finite sequence of exact
mathematical units exists. A formal and documentary census can refute
eligibility or duplication; proof plus exact computation can establish the
surviving bounded claims. Statistical inference or qualitative interviews
cannot answer this RQ.

## Data Strategy

**Data Type:** Secondary mathematical documents and deterministic generated
artifacts; no human-subject or personal data.

**Sources:**

- all regular files in the accepted P1–P43 authority trees and root README;
- immutable Route cards, source locks, proof packages, experiment ledgers,
  manifests, Git objects, and plain-mirror copies;
- primary journal, publisher, DOI, arXiv, and institutional sources retrieved
  in Phase 2;
- candidate-specific exact finite fixtures generated only after a source and
  experiment contract is frozen.

**Sampling:** Internal evidence is a census, not a sample. External sources
use criterion-based retrieval with forward/backward citation checking and an
exact claim-to-source ledger. Candidate directions are exhaustively compared
within the declared universe; additions require a dated universe amendment.

**Time Frame:** Internal baseline through commit `6e565864...`; external
literature search cutoff 2026-08-17 for the first freeze, with a final update
search immediately before publication.

## Candidate-Universe Protocol

1. Separate three states: historical registry membership, commissioned
   working remainder, and newly proposed source universe. Never collapse them.
2. Encode every proposal by the signature
   `(object, dynamics, primitive type, repetition law, arithmetic source,
   clock, marker, operator owner, determinant owner, claim quantifiers)`.
3. Compare that signature against all P1–P43 signatures before theorem work.
4. Require a one-sentence theorem, proof dependency graph, positive control,
   at least three non-prime/adversarial controls, and an explicit failure
   outcome before admission.
5. Apply the primary-literature collision gate in Phase 2. An exact collision
   yields `STOP_DUPLICATE`; a partial collision narrows the claim and novelty
   ceiling.
6. Freeze the ordered sequence only after each unit passes the preceding
   gates. A dependency paper cannot be counted separately if its theorem is
   only a lemma needed by the next unit.

## Analytical Framework

**Technique:** Typed claim–evidence matrix plus theorem-proving and exact
counterexample analysis.

**Steps:**

1. Recompute the accepted baseline, repository/mirror identity, and historical
   chronology.
2. Build the residual/open-boundary matrix and classify every direction as
   `CONSUMABLE`, `NEW_SOURCE_LOCK_REQUIRED`, `DUPLICATE`, `OUT_OF_SCOPE`, or
   `UNRESOLVED_LITERATURE`.
3. Search primary literature for each exact theorem signature, not only broad
   topic keywords; verify metadata and claim scope.
4. For each survivor, independently derive the theorem and attack all
   quantifiers, edge cases, object resets, and ownership relations.
5. Score independence: a paper must have a theorem that remains meaningful if
   the next paper is deleted, while preserving a non-overlapping principal
   claim.
6. Freeze per-paper source locks and preregister exact computational
   projections, controls, mutation classes, rejection envelopes, and Route
   expectations.
7. Implement two mathematically independent evaluators. Compare normalized
   science projections by strict type and canonical bytes.
8. Run transactional empty-to-materialized-to-idempotent workflows only in
   disposable clones before any authority materialization.
9. Subject every proposed publication unit to independent theorem,
   literature, experiment, Route, PDF, provenance, Git, and mirror audits.
10. Merge adjacent units or stop below five whenever the independence gate
    fails.

**Tools:** `rg`, Git object inspection, exact rational/integer arithmetic,
Python 3 isolated execution, duplicate-safe YAML/strict JSON parsing, LaTeX
fixed-epoch builds, primary-source web retrieval in Phase 2, and independent
read-only subagent audits. No target-zero data or cross-model content
transport is authorized.

## Validity Criteria

| Criterion | Strategy to Ensure |
|---|---|
| Construct validity | Freeze typed object/clock/marker/operator/determinant contracts; reject coordinate mixing and unannounced object resets. |
| Internal validity | Complete proofs own universal statements; exact controls delete one hypothesis at a time; two independent evaluators and strict recursive type equality cover bounded artifacts. |
| External validity | State source- and quantifier-specific boundaries; do not generalize from one symbolic family to all symbolic dynamics. |
| Reliability | Content-address every input/output; use isolated deterministic runs, exact rejection envelopes, cold relocation, and zero-write idempotence. |
| Source validity | Cite only verified primary sources for theorem/priority claims; unresolved metadata or claim scope fails closed. |
| Sequence validity | Require a distinct principal theorem and standalone significance for each unit; use merge/stop rather than paper-count padding. |
| Chronology validity | Record what was known at each freeze; label exploratory, retrospective, and post-output actions exactly. |

## Limitations (By Design)

- Phase 1 cannot establish novelty; primary-source verification is deliberately
  deferred to Phase 2 and can delete any candidate.
- The five-paper cardinality creates salami-slicing pressure. The fixed
  mitigation is an independence test plus `STOP_AT_k` for `k<5`.
- Program-internal typed closure may be rigorous yet have low standalone
  novelty; both values will be reported separately.
- Exact finite computation cannot prove infinite theorems; it is used only for
  formula checks, controls, implementation integrity, and reproducibility.
- A newly opened source universe is not evidence that the historical C03/C05
  remainder was consumed.

## Ethical Considerations

- No human subjects, personal data, recruitment, or intervention are involved.
- Attribution, exact quotation limits, source provenance, and AI-assistance
  disclosure are mandatory.
- Negative or low-novelty outcomes will not be rewritten as positive Route
  results.
- No manuscript, source package, or unpublished full text will be sent to an
  external model without separate user consent; none is planned here.

## Reporting Standard

- Recommended guideline: Other — theorem/provenance audit with a
  claim–evidence–scope matrix, exact computational reproducibility appendix,
  and explicit AI-use disclosure.

## Preregistration

- Recommended: Yes, per candidate after literature clearance and before
  canonical experiment outcomes.
- Platform: N/A — content-addressed repository source lock and experiment
  contract are the governing mechanism.
- Status: Planned.
- Completed artifact declaration: not_provided.
- Companion handle: none.
- Sidecar ownership: dispatching/integration layer only.

## Design-Freeze Checkpoint Audit

- Primary decision: `sound` — drivers: the method directly answers the
  existence/selection RQ; exact novelty and duplication are hard-gated; the
  five-count pressure is neutralized by merge/stop.
- Cross-model decision: `unavailable` — drivers: none — confidence: N/A.
- Outcome: `unavailable — no consented external transport; single-model only`.
