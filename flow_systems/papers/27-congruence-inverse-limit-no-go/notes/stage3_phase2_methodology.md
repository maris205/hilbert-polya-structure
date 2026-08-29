criteria_binding_unavailable
contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "A localized methodological omission or clarity gap reduces auditability or confidence but does not materially undermine any core result."

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

The methodology audit covered the written proof chain and the eligible Round 2, 4, 5, 7, and 8 execution surfaces. It separately checked exact quotient-order computation, cocompact lower-bound semantics, owner-indexed coefficient escape, the changed-clock finite calibrator, source and input locks, deterministic rendering, and the stated exclusions from infinite-product, growing-panel, uncomputed full-core, and Route-B claims. The 47 eligible unit tests passed in this review context. Round 3 and Round 6 receive no experiment credit.

### S1: The two candidates retain distinct owners, towers, clocks, and tuples

**Evidence Anchor**: text: paper/manuscript.tex, Limitations and open obligations — "$Q_{11}$ does not restore periodic points to $M_\infty$."

**Confidence**: 5 — direct examination of the definitions, proofs, limitations, and Route analysis.

**Rationale**: The residual inverse-limit owner remains governed by the common physical clock and the tuple `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`. The homology calibrator instead declares the nonresidual tower, the `1/N` clock, the `1/N^3` logarithmic normalization, and the distinct tuple `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)`. The paper never lets the finite $Q_{11}$ identity rescue residual-owner periodicity or Route credit, and Route B remains closed.

### S2: Quotient orders and bonding checks are exact on the registered congruence population

**Evidence Anchor**: dataset: results/round2/round2_metrics.json#/orders_by_element, /independent_order_crosschecks_passed, and /bonding_transition_checks_passed

**Confidence**: 5 — direct source, ledger, hash, and test replay.

**Rationale**: Sequential multiplication and finite-group-bound factor reduction agree on all 24 owner-level rows; the three displayed eight-level order sequences match the manuscript; and all 21 noninitial bonding and order-divisibility transitions pass. Arithmetic for the orders is integer-exact, the quotient test treats both scalar signs as projectively trivial, and every row forbids inverse-limit periodic-orbit credit. The source and ledger also preserve `gamma3_class_primitivity: OPEN`, so these rows support whole-loop closing orders rather than an unproved full conjugacy-primitivity claim.

### S3: The cocompact control preserves lower-bound rather than fabricated full-order semantics

**Evidence Anchor**: dataset: results/round5_cocompact_homology_escape_validation.json#/checks and /lower_bounds_by_owner

**Confidence**: 5 — exact ledger and proof-boundary inspection.

**Rationale**: All 24 cocompact owner-level rows have content-one homology and the certified sequence `1,2,6,24,120,720,5040,40320`. Every row reports `NOT_ENUMERATED_LOWER_BOUND_ONLY` for the residual-core quotient order, while primitive homology supplies the base-primitivity certificate. This supports the factorial minimal-period lower bounds without claiming that the residual cores or their full quotient orders were computed.

### S4: The four-quadrant replay is complete, exact, and bounded to a finite panel

**Evidence Anchor**: dataset: results/round8_homology_renormalization_summary.json#/exact_structure, /quadrant_conclusions, /quadrant_rows, and /coefficient_rows

**Confidence**: 5 — direct comparison of theorem formulas, builder logic, and unique serialized rows.

**Rationale**: The replay contains 96 unique owner-level-quadrant rows and 1,248 unique coefficient rows through degree 12. It uses exact `math.comb` arithmetic and preserves degree `N` under the physical clock, coefficient `N^3` after clock-only rescaling, degree `N` after normalization-only intervention, and exact factor `(1-x_g)^{-1}` only in $Q_{11}$. The 24 $Q_{11}$ rows explicitly state that they are not the Round-7 owner. The manuscript correctly leaves infinite products, growing panels, uniformity, full primitive censuses, global determinants, and uncomputed residual-core orders outside this finite replay.

### S5: Hash locks and deterministic rebuild checks bind the central finite artifacts

**Evidence Anchor**: dataset: experiments/round8_reproducibility_receipt.json#/core_sha256, /locked_inputs, /source_bindings, and /execution

**Confidence**: 5 — current hashes match the receipts and all 47 eligible tests pass.

**Rationale**: The Round-8 freeze hash, locked Round-5 ledger and validation hashes, three result hashes, validation binding, and source/test/reproducer bindings match the current files. Round 7 similarly binds four upstream inputs and its rendering sources, while Round 2 binds its source files in the manifest. The eligible test suites verify source drift detection, row cardinalities, exact coefficient formulas, owner separation, lower-bound semantics, Route boundaries, byte determinism, and receipt identity.

### S6: Experiment credit excludes research-only positioning rounds

**Evidence Anchor**: dataset: notes/stage2_5_experiment_provenance_source_map.json#/experiments

**Confidence**: 5 — exact inspection of the five-entry provenance population.

**Rationale**: The provenance population contains only Rounds 2, 4, 5, 7, and 8. Round 3 literature work and Round 6 source positioning are absent from experiment provenance and receive no computational support credit. The retrospective-transcription notice is retained, so the Stage-2.5 map is not misrepresented as a pre-writing intent record.

### W1: The negative projective-sign branch is not exercised by the frozen diagnostics

**Severity**: Minor

**Evidence Anchor**: dataset: results/round2/congruence_reduction_order_ledger.csv, terminal_scalar_sign column and all 24 data rows

**Confidence**: 5 — direct enumeration of the ledger plus inspection of both order algorithms and their tests.

**Rationale**: All 24 first scalar returns terminate at `+1`. The implementation correctly recognizes both `+I` and `-I`, but the frozen population and unit tests contain no case whose first projective return is `-I`. Both order strategies also share the same `scalar_sign` routine and matrix-multiplication kernel. Their agreement strongly checks the registered orders but does not independently exercise the negative-sign branch, so the statement that the finite table tests the projective-sign convention is slightly broader than the adversarial coverage actually delivered. This does not weaken the written projective-sign intersection proof or any displayed order sequence.

**Actionable Remedy**: Add a unit fixture that sends `-I` modulo an eligible modulus through `scalar_sign` and, preferably, a matrix whose first projective return is `-I`; either give the second checker an independently implemented arithmetic/sign kernel or describe the pair as distinct order-reduction strategies sharing common primitives.

## Arithmetic Receipts
no_recomputable_statistics: Checked the manuscript, tables, exact ledgers, and computational summaries; they report group orders, deterministic row counts, hashes, and exact formal coefficients, but no t, z, F, chi-square, rounded mean/SD, or df/N statistic covered by p_from_test_statistic, GRIM, GRIMMER, or n_from_df.
