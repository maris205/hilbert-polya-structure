criteria_binding_unavailable
contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "The core method remains usable, but important reporting, justification, robustness, or reproducibility details are incomplete or unclear."

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

The methodology is fit for the paper's deliberately narrow control-infrastructure theorem. The proof separates source-locked geometry, symbolic normal-form and sign arguments, exhaustive finite execution, and display-only decimals. The current verify-only replay passed all 24 Round-8 tests and produced two byte-identical artifact trees with the frozen tree digest. D1 is nevertheless a warn because one replay-sequencing sentence is inaccurate and the official test suite does not directly isolate several canonicalization and closure invariants. D3 passes: the finite computation is connected to the global systole claim by the axis-recentering and tile-chain completeness proof, and the conclusions remain within that chain's scope.

### S1: Exact canonical state identity and comparison predicates

The normal-form argument distinguishes denominator parity, proves uniqueness after common-Delta cancellation, fixes the remaining global projective sign, and uses the resulting tuple directly for dictionary/set deduplication. The implementation toggles parity and updates the integral Delta exponent on multiplication, repeatedly cancels common Delta factors, canonicalizes the first nonzero Gaussian coefficient, constructs inverse generators exactly, and serializes the canonical tuple deterministically. Exact generator/inverse and relator reductions pass; additional read-only diagnostics also confirmed two-sided inverse reduction, multi-factor cancellation, sign normalization, and normalization idempotence.

**Evidence Anchor**: equation: manuscript \eqref{eq:state-form}, Lemma \ref{lem:key}, and \eqref{eq:center-poly}/\eqref{eq:H}; builder lines 328–405 and 630–653

### S2: Geometric completeness is not replaced by a word cap

The axis-recentering and tile-chain argument places a representative of every class through the frozen cutoff in the identity-connected guarded component. The builder then starts from the identity, expands all eight exact right-neighbors of each included state, records distinct rejected endpoints without expanding them, fails on an unresolved sign or state-cap excess, retains first-discovery witness words, and hashes the sorted included and rejected streams. Queue exhaustion therefore implements the stated component contract, while the paper correctly disclaims global connectivity of the entire guard-induced subgraph.

**Evidence Anchor**: equation: manuscript \eqref{eq:chain-radius}–\eqref{eq:guard} and Theorem \ref{thm:complete}; builder lines 548–627 and 660–728

### S3: Exact decisions, reproducible execution, and hash interpretation are separated

All theorem-changing interval branches use integer and Fraction arithmetic; exact zero polynomials are recognized symbolically, unresolved nonzero signs raise an error, negative systole signs abort, and mpmath is confined to decimal rendering. The verify-only wrapper builds twice in fresh temporary directories, compares the complete trees, compares fresh artifacts and the receipt against checked-in bytes, and exposes refresh only through an explicit option. The manuscript also states correctly that hashes bind reviewed bytes but do not establish mathematical truth on their own.

**Evidence Anchor**: dataset: experiments/round8_reproducibility_receipt.json#/execution and results/round8_control_finite_ball_certificate.json#/proof_guards

### S4: The evidentiary scope is kept failure-closed

The artifacts and manuscript consistently classify this work as a control-side exact-systole and finite-completeness result only. The formal full Route-A tuple remains unassigned, and the historical bounded proxy remains unchanged at A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL. No matched census, Bolza or control census, conjugacy/owner classification of the 144 equality elements, magnetic comparison, determinant experiment, new A2 evaluation, A3/A4 promotion, or Route-B invocation receives credit here.

**Evidence Anchor**: dataset: results/round8_control_finite_ball_certificate.json#/execution and #/route_a

### W1: Replay-order prose does not match the executable order

The paper says that source and upstream locks are checked before reconstruction, but main calls finite_traversal before build_validation performs those lock checks. The verify-only wrapper remains safe because both builds occur in fresh temporary directories and no canonical refresh occurs unless the builder validates successfully, so this sequencing discrepancy does not alter the theorem values or byte-identical replay result.

**Severity**: Minor
**Evidence Anchor**: text: manuscript Independent replay obligations, lines 815–817: "The verifier first checks source and upstream digests, then reconstructs all canonical states in a fresh directory."
**Confidence**: 5 — direct comparison of manuscript wording, builder control flow, and a successful current verify-only replay
**Rationale**: The issue is a precise reproducibility-description error, not a defect in the exact traversal or its reported output, but it can mislead an independent implementer about when input locks become gating conditions.
**Actionable Remedy**: In the next authorized manuscript-revision stage, state that the builder reconstructs in an isolated output directory and then validates source/upstream locks before a PASS is emitted; alternatively, move the lock checks before finite_traversal if pre-reconstruction rejection is the intended executable contract.

### W2: Canonicalization and closure regression tests are mostly indirect

The 24 official tests lock inverse products, the relator, guards, counts, histograms, stream hashes, scope flags, and validation hashes, but they do not directly exercise multi-factor Delta cancellation, projective-sign idempotence, both inverse orders, or independently recompute the eight-transition closure of the included/rejected partition. Source inspection and the successful full replay provide substantial assurance, so this is test-localization and robustness debt rather than evidence that a reported state or sign is wrong.

**Severity**: Minor
**Evidence Anchor**: absence: code/test_round8_control_systole_certificate.py — expected direct regression tests for multi-factor Delta cancellation, projective-sign idempotence, two-sided inverse reduction, and transition-closure recomputation; checked all 24 Round-8 test methods and the corresponding builder functions
**Confidence**: 5 — complete inspection of the Round-8 builder and test module, supplemented by passing read-only canonicalization diagnostics and the full verify-only replay
**Rationale**: Frozen hashes make changes visible but can also preserve a shared implementation error; focused property tests and an independent closure assertion would make failures easier to localize and reduce reliance on the builder's own summary booleans.
**Actionable Remedy**: Add direct tests for repeated Delta cancellation, normalization idempotence under global negation, both generator/inverse multiplication orders, and sampled-state canonical collisions. For stronger assurance, add an independent verifier that reconstructs every stored witness and asserts that each of the eight outgoing transitions from every included state lands in the included or rejected set before accepting the closure flag.

## Arithmetic Receipts
no_recomputable_statistics: Checked the manuscript's exact counts, polynomial identities, rational interval bounds, and display decimals; it reports no claim covered by p_from_test_statistic, grim, grimmer, or n_from_df.
