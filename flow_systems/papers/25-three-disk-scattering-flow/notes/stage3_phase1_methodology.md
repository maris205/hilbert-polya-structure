## Contract Paraphrase

D1 requires the methodology seat to judge whether the research design, treatment of evidence or data, analytical procedures, quantitative reporting where applicable, and reproducibility information collectively satisfy a defensible peer-review standard.

D2 requires domain-facing claims, terminology, representations of prior work, and reported results to be factually dependable; from a methodology perspective, that accuracy is a prerequisite for interpreting whether an analysis addresses the intended objects and questions.

D3 requires the central line of reasoning to connect premises, methods, evidence, and conclusions without contradictions or inference failures that undermine the thesis; methodology review will focus on whether the evidentiary chain licenses the claims made.

D4 requires the framing, definitions, and implications to be intelligible beyond the immediate specialty and any interdisciplinary reach to be supported; methodologically, readers in neighboring fields should be able to understand the basis and limits of the inferences.

D5 requires clear organization, readable exposition, effective figures or tables, and compliance with the applicable presentation conventions; methodology-relevant procedures and results should therefore be communicated in an auditable form.

D6 establishes a separate requirement that the contribution be original, consequential, and appropriate for the intended readership under the configured review target; the methodology seat does not score that requirement.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Whether the stated question, research design, evidence or data handling, analytical chain, reporting, robustness checks, and reproducibility affordances form a valid and auditable method.
what_triggers_block: A central result depends on a materially invalid design, analysis, or evidence-handling step that cannot be repaired without substantial re-analysis.
what_triggers_warn: The methods are broadly suitable, but important reporting, robustness, or reproducibility details are incomplete enough to reduce confidence without invalidating the core analysis.
what_triggers_fatal: The core conclusion is methodologically uninterpretable because the design or analytical procedure cannot answer the stated question and no valid evidentiary path remains.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Whether each central claim follows from explicit premises and appropriately analyzed evidence, with assumptions, alternatives, counterexamples, and scope limits handled consistently.
what_triggers_block: A central conclusion rests on a decisive logical gap or evidentiary mismatch that requires substantial reconstruction of the argument.
what_triggers_warn: The main inferential chain remains viable, but one or more assumptions, intermediate steps, or scope limits need clearer support.
what_triggers_fatal: The core thesis follows from neither its premises nor its evidence, so the central argument collapses even if local statements are repaired.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
