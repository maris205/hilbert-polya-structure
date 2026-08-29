criteria_binding_unavailable
contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "The core methodological route remains credible, but limited omissions in justification, reporting, robustness checks, or reproducibility detail require clarification."

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: pass

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

The theorem-proof and exact-computation design is fit for the stated finite research question. The analytic chain separates cycle-pushforward ownership, branch-cycle degree, primitive-root exponent, and zeta repetition before deriving the all-parameter quadratic moment criterion. The finite certificate then reconstructs every locked owner, works over integer and rational arithmetic for all decisions, and relegates binary64 values to diagnostics. Across the authorized evidence, the denominators remain stable at 11 sources, five primes, 55 source/prime groups, 138 owner instances, and 165 group/law rows. The declared 17/17 experiment-backed claim alignments are traceability evidence only: their audit expressly identifies the mapping as retrospective and declines to certify design, execution, or reproducibility.

The non-deduplicated boundary is methodologically explicit. The taxonomy is exhaustive for the registered output multiset, not for globally distinct conjugacy classes or all primitive classes of $\Gamma_0(11)$; the manuscript consistently preserves that finite/global distinction. The current package also records deterministic two-build agreement, tests, artifact hashes, and fail-closed checks. One minor provenance-closure omission prevents an unqualified pass on D1, but it does not undermine the present exact results. No target criteria are bound, and this report makes no venue-alignment or submission-readiness claim.

### S1: The analytic criterion is necessary and sufficient on the declared finite object
**Evidence Anchor**: equation: manuscript.tex:253-271 (quadratic degree-moment criterion and coefficient/Mobius-inversion proof)
**Rationale**: The proof moves from equality for all sufficiently large $s$ to coefficient equality and then separates every branch-degree moment. This supplies the logical bridge needed to interpret the exact finite ledger without treating a few sampled $s$ values as proof.

### S2: Frozen denominators and owner reconstruction are carried consistently
**Evidence Anchor**: dataset: results/round8_summary.json#/instances and #/groups
**Rationale**: The summary records 138 mutually classified instances, 55 word/prime groups, and 165 group/law rows, while the implementation rebuilds each owner from its source, prime, branch cycle, and degree and checks determinant, subgroup membership, and exact primitivity. The primary laws each yield four survivors and 51 failures; the control yields 55 failures.

### S3: Exact arithmetic has authority over floating diagnostics
**Evidence Anchor**: dataset: results/round8_summary.json#/instances/floating_point_zero_decisions and #/theorem/numerical_smallness_used_as_proof
**Rationale**: Kernel status and normalized moments come from rational homology coordinates and sums of rational squares. The summary records zero floating-point zero decisions and explicitly denies using numerical smallness as proof; all 165 floating cross-check verdicts agree only after the exact decisions are formed.

### S4: The reproducibility package supplies deterministic and tamper-sensitive checks
**Evidence Anchor**: dataset: experiments/round8_reproducibility_receipt.json#/execution and #/unit_tests
**Rationale**: The receipt records two byte-identical isolated builds with tree hash `cc36c1f952c9ce89050996f4bb4c9905571f9ef09a0d7115be8a985e02a5621d` and 18/18 passing Round-8 tests. The inspected tests cover locked input hashes, exact owner replay, full denominator counts, exact moment identities, taxonomy counts, tampering, route boundaries, and deterministic in-memory reconstruction.

### S5: Experiment-claim provenance is reported with the correct epistemic limit
**Evidence Anchor**: text: stage2_5_experiment_claim_alignment_audit.md:4 "Decision: 17/17 directly experiment-backed selected registry spans ALIGNED"
**Rationale**: The audit identifies 17 direct experiment-backed spans, seven provenance entries, and 17 registry-to-manifest-to-experiment crosswalk rows, while explicitly describing the manifest as gate-time reconstruction and withholding credit from proof, citation, interpretation, limitation, and heavily mixed spans. It therefore supports traceability without being misused as prospective registration or methodological validation.

### S6: The multiset theorem is not promoted into a global census
**Evidence Anchor**: text: manuscript.tex:451-453 "The taxonomy is complete only for the frozen output multiset."
**Rationale**: The manuscript repeatedly states that cross-instance $\Gamma_0(11)$ conjugacy deduplication and complete primitive enumeration were not performed. It preserves correspondence multiplicities for the finite theorem and names exact cross-instance canonicalization as the next finite task, so the 138-instance denominator is not presented as 138 globally distinct primitive owners.

### W1: The final certificate manifest is not closed over transitive source dependencies
**Severity**: Minor
**Evidence Anchor**: dataset: results/round8_artifact_manifest.json#/sources (dependency imports at code/round8_exact_taxonomy.py:152-154 and code/round7_exact_survivors.py:123-124)
**Confidence**: 5 — direct comparison of the recorded source list with the inspected import graph
**Rationale**: The Round-8 manifest and receipt bind the top-level builder, its test, the reproduction wrapper, freeze notes, and two input ledgers, but the builder imports `round7_exact_survivors.py`, which in turn imports `round2_experiment.py` and `round4_hecke_correspondence.py`; those transitive code files are absent from the final Round-8 source list. Earlier round receipts bind the omitted files and their current hashes match those records, so this is an auditability defect rather than evidence of a wrong result. Nevertheless, the final certificate alone does not enumerate every source byte used by its rebuild.
**Actionable Remedy**: Regenerate the Round-8 artifact manifest and reproducibility receipt with a dependency-closed source list that includes `round7_exact_survivors.py`, `round4_hecke_correspondence.py`, `round2_experiment.py`, and any further imported project module, then add a fail-closed test that verifies every recorded dependency hash before building and confirms the checked-in output tree remains unchanged.

## Arithmetic Receipts
no_recomputable_statistics: Checked the reported finite counts, exact rational moments, homology ranks, hashes, and floating diagnostic residuals; none is a p_from_test_statistic, GRIM, GRIMMER, or n_from_df claim.
