criteria_binding_unavailable

contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "The canonicalization method would remain viable, but important edge cases, witness formats, termination arguments, collision handling, or cross-implementation replay details would be underspecified."

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "The central reasoning would remain defensible, but one or more implication directions, representation qualifications, evidence-status distinctions, or limitations would need explicit clarification."

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

The revised architecture improves the evidence hierarchy by making a two-direction canonicalization theorem the primary proof object and the 9,453 unordered pairs a derived regression surface. It also correctly keeps global owners, occurrence-level incidence, and within-cell deduplication as distinct conditional estimands. No canonicalizer, theorem, owner partition, pair audit, or G/I/C table was executed, and the manuscript does not award scientific or Route credit for its design. D1 warns because the proof schema, theorem binding, negative evidence, serializer, fixtures, producer, and independent verifier remain uninstantiated. D3 also warns: the displayed type of kappa conflicts with its stated resolved-only domain, and the proposed unordered-pair expansion cannot by itself test all the equivalence properties attributed to it. Both issues are repairable without abandoning the certificate-first architecture, but they need explicit formal correction before a scientific freeze.

### S1: The biconditional is the correct primary invariant
Making equality of deterministic owner bytes equivalent in both directions to oriented primitive-owner identity is methodologically stronger than treating thousands of pair decisions as unrelated authorities.
**Evidence Anchor**: equation: §4.1 — canonicalization biconditional relating kappa byte equality to the same oriented primitive Gamma_0(11) owner

### S2: G, I, and C are not conflated
The conditional definitions preserve global identity, every input occurrence, and cell-local no-double-credit information without pretending that one projection reconstructs all three surfaces.
**Evidence Anchor**: text: §4.4 — "The three estimands answer noninterchangeable questions."

### S3: Target-blind fixtures precede population execution
The proposed fixtures include same-owner representations, inverse relations, powers, malformed inputs, coarse-invariant collisions, and unresolved theorem bindings, with expected outcomes fixed before producer access.
**Evidence Anchor**: text: §4.2 — "Expected outputs must be registered before the producer sees them."

### W1: The canonical map has inconsistent domain and totality semantics
**Problem**: The manuscript displays kappa as a map from all of X to OwnerBytes, then defines it only on successfully resolved inputs, while later describing the primary invariant as total and requiring zero unresolved rows before complete estimands.
**Evidence Anchor**: text: §4.1 — "kappa: X -> OwnerBytes"; "on every successfully resolved input"
**Why it matters**: The biconditional, byte partition, pair audit, and G/I/C materialization have different truth conditions depending on whether unresolved inputs are outside the map, mapped to a typed non-owner state, or invalidate the batch. The current statement cannot support a single totality proof.
**Suggestion**: Define a resolved domain and a separate total disposition map explicitly, state that any unresolved disposition blocks complete kappa-based materialization, and restate both directions of the biconditional with precise quantifiers over the resolved domain.
**Severity**: Major
**Confidence**: 5 — core expertise: exact canonicalization contracts

### W2: The unordered pair table cannot independently test every claimed equivalence property
**Problem**: The paper says the derived table can test symmetry and transitivity consequences, yet it contains only unordered pairs of distinct inputs. Such rows omit self-pairs, direction reversal, and explicit triples or class-level closure checks.
**Evidence Anchor**: text: §4.3 — "It can test symmetry, transitivity consequences"; "all unordered cross-input comparisons"
**Why it matters**: Reflexivity and directional symmetry are structurally absent from this table, while transitivity requires checking compatible triples or grouped equivalence classes. Treating byte equality as already proving these properties would make the audit dependent on the canonicalizer it is meant to challenge.
**Suggestion**: Specify separate audit predicates: self-fixtures for reflexivity, ordered conjugacy-route reversals for symmetry, class/triple closure checks for transitivity, and pairwise byte/direct-solver disagreement rows. State which predicates test the canonicalizer versus merely expand its output.
**Severity**: Major
**Confidence**: 5 — core expertise: adversarial equivalence-class testing

### W3: The certificate and verifier contract remains non-executable
**Problem**: Required fields and failure semantics are described, but no closed byte schema, theorem registry, proof payload grammar, fixture bytes, producer, reference verifier, or build manifest exists.
**Evidence Anchor**: text: §4.2 — "No such schema, theorem binding, fixture set, producer, or verifier was implemented"
**Why it matters**: Two implementations could satisfy the prose using incompatible orientation, root, negative-proof, or serialization semantics. Independent replay cannot be assessed without an external consumer and frozen expected outcomes.
**Suggestion**: Publish a versioned schema and theorem/proof-type registry; specify rejection rules and canonical bytes; provide positive, negative, inverse, power, malformed, collision, and unresolved fixtures; and require a separately implemented verifier before exposing the 138 inputs.
**Severity**: Major
**Confidence**: 5 — core expertise: proof-carrying group computation

### W4: The executed evidence synthesis is not independently reproducible at claim level
**Problem**: Aggregate corpus counts and citation closure are reported, but the manuscript provides neither exact search queries and complete screening decisions nor theorem/page locators for the component claims used to motivate the canonicalization design.
**Evidence Anchor**: absence: Executed Methodology and Reproducibility sections — expected exact queries, a complete screening ledger, and claim-level theorem locators; checked §§3.1, 6, 8, and references.bib
**Why it matters**: The only executed research method cannot be replayed from retrieval through claim assignment, and the exact hypotheses of candidate conjugacy, root, and subgroup methods remain unverified.
**Suggestion**: Add a hash-bound search and screening supplement and a source-finalization table linking each proposed subroutine to exact passages, hypotheses, representation constraints, and prohibited transfers.
**Severity**: Major
**Confidence**: 4 — adjacent expertise: reproducible mathematical evidence synthesis

## Arithmetic Receipts
no_recomputable_statistics: Checked the reported 138 instances, 55 groups, 2/2/134 diagnostic split, 44 captured records, nine duplicates, 35 screened records, 13 exclusions, 22 retained sources, 22-of-22 identity closure, 19 peer-reviewed rows, 138-row incidence relation, and the exact combinatorial identity binom(138,2)=9,453; these are design, inventory, or set-count quantities rather than reported test statistics, discrete means/SDs, or df-based sample claims covered by p_from_test_statistic, grim, grimmer, or n_from_df.
