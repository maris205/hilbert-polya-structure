## Contract Paraphrase

D1 concerns whether the mathematical method is adequate for the stated theorem-level aims: constructions must be well-defined, hypotheses must be carried through correctly, proof dependencies must be explicit, and descent, sheafification, and categorical arguments must be detailed enough for independent verification.

D2 concerns whether specialized assertions, terminology, and uses of established results are mathematically accurate, since a proof cannot be sound when it relies on misstated theorems, incompatible definitions, or erroneous domain facts.

D3 concerns the validity of the inferential chain from definitions and premises through intermediate lemmas to the principal conclusions, including the handling of quantifiers, cases, functoriality, counterexamples, and possible circularity.

D4 concerns whether definitions, categorical transitions, and claimed implications are explained with enough precision for mathematically adjacent readers, and whether connections beyond the immediate specialty are supported by actual arguments rather than suggestive terminology.

D5 concerns whether the ordering of definitions, statements, proofs, diagrams, and equations makes the reasoning auditable, with notation and cross-references clear enough that structural presentation does not conceal assumptions or proof dependencies.

D6 concerns whether the stated contribution is demonstrably original and mathematically significant for its intended readership; this requires a defensible account of what is new and why it matters, considered separately from any unavailable target-criteria binding.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Verify that every central construction is well-typed, all hypotheses propagate correctly, descent and sheafification steps invoke applicable results, and proofs expose enough intermediate reasoning to be independently audited.
what_triggers_block: A central result depends on a substantive but potentially repairable proof gap, ill-defined construction, or unjustified descent step that prevents verification.
what_triggers_warn: The principal proof architecture remains viable, but a localized dependency, hypothesis transfer, or reproducibility detail requires clarification.
what_triggers_fatal: A foundational construction is incoherent or a decisive counterexample invalidates the central theorem in a way that cannot be repaired within the stated framework.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Trace each claimed implication through its lemmas, checking logical direction, quantifier scope, case coverage, compatibility of statements, and engagement with boundary cases or counterexamples.
what_triggers_block: The main conclusion relies on circular reasoning, a missing essential implication, or incompatible intermediate claims and therefore requires major reconstruction.
what_triggers_warn: The overall inference chain is supportable, but a local quantifier transition, case split, or link between propositions is insufficiently explained.
what_triggers_fatal: The core thesis entails an unavoidable contradiction or is defeated by a counterexample for which no consistent reformulation preserves the claimed result.

criteria_binding_unavailable
[CONTRACT-ACKNOWLEDGED]
