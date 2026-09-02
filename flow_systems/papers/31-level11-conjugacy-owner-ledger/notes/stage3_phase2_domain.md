criteria_binding_unavailable
contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "A localized terminology gap or insufficiently explicit convention involving trace, inversion, repetition, conjugacy, or ledger level while the configured dynamical owner remains recoverable."

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

The paper correctly centers an oriented primitive Gamma_0(11) conjugacy invariant rather than treating 138 instances, 55 groups, or 9,453 pairs as owners. Its G/I/C separation is mathematically useful, and its novelty positioning is appropriately bounded. D2 remains recoverable but needs two local formal repairs: the domain of the canonical byte map conflicts with the preceding partial-root definition, and the categorical inverse-separation rule needs an explicit group-theoretic justification or self-reciprocal branch.

### S1: Input occurrences are separated from dynamical owners

The manuscript explicitly prevents row, group, and coarse-invariant equality from substituting for exact oriented subgroup conjugacy and maximal-root resolution.

**Evidence Anchor**: text: §1 Introduction "the dynamical owner is not an input row"

### S2: The canonicalization target has the right logical shape

Both directions of byte equality versus owner equality, together with soundness, completeness, determinism, and totality, are made explicit rather than hidden behind a generic normal-form claim.

**Evidence Anchor**: text: §4.1 Primary target "a total, sound, complete, deterministic owner map"

### S3: G, I, and C retain different information

The incidence relation preserves occurrence-level provenance, while the global and cell-local projections do not pretend to reconstruct information they discard.

**Evidence Anchor**: text: §4.4 Distinct estimands "a complete I can induce G and C by the stated projections"

### S4: Citation closure is not promoted to theorem verification

The source discussion consistently marks exact theorem transfer as unresolved, which is preferable to treating DOI closure as evidence of applicability.

**Evidence Anchor**: text: §3.1 Closed-corpus synthesis "That check does not validate a theorem passage."

### W1: The declared canonical map has an inconsistent domain

**Problem**: The text first makes root(x) partial, with a typed not-evaluable outcome, and then displays kappa as a total map from all X to OwnerBytes while saying it is defined only on successfully resolved inputs.

**Evidence Anchor**: equation: §4.1 — kappa: X -> OwnerBytes following the partial root(x) definition

**Why it matters**: The biconditional and totality claims are ambiguous unless unresolved inputs are either outside the map's domain or represented in a distinct sum type that cannot collide with owner bytes.

**Suggestion**: Define X_res explicitly and type kappa: X_res -> OwnerBytes, or define a disjoint OwnerBytes-or-Unresolved codomain and state which subset the biconditional quantifies over.

**Severity**: Minor

**Confidence**: 5 — direct formal-domain inconsistency in the displayed contract

### W2: Inverse separation needs a self-reciprocity disposition

**Problem**: The biconditional defines owners by Gamma_0(11) conjugacy, yet the map is categorically forbidden to identify an owner with its inverse. The manuscript does not bind a lemma excluding conjugacy to the inverse in the exact group, nor does this contract specify the behavior if such a class occurs.

**Evidence Anchor**: text: §4.1 Primary target "The map must not identify an owner with its inverse"

**Why it matters**: If an inverse-related representative lies in the same subgroup conjugacy class, forced byte separation would contradict the reverse direction of the proposed canonicalization theorem.

**Suggestion**: Bind the exact group-theoretic result that makes inverse classes distinct here, or add a typed self-reciprocal case and allow the inverse link to point to the same owner bytes when proved.

**Severity**: Minor

**Confidence**: 4 — core expertise: oriented hyperbolic conjugacy; exact project theorem binding remains absent
