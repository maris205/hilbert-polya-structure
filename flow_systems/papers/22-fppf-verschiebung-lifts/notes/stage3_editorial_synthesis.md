# Stage 3 Editorial Synthesis

## Synthesis boundary

This document mechanically synthesizes the five committed `reviewer_full`
cards under contract `reviewer/reviewer_full/v2`. It is not a sixth review:
no finding below is introduced independently of the EIC, Methodology, Domain,
Perspective, or Devil's Advocate card. All five cards disclose
`criteria_binding_unavailable`; accordingly, this synthesis makes no
venue-alignment claim. The package remains `calibration_status:
NOT_CALIBRATED`.

## Mechanical audit

dimension_verdicts: [D1=pass, D2=warn, D3=pass, D4=warn, D5=pass, D6=warn]
fired_conditions: [F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

### Role-scoped dimension matrix

Only assessed scores from contract-eligible seats enter the matrix.
Ineligible `not_assessed` entries are excluded.

| Dimension | Priority | Assessed eligible seat(s) | Audit verdict |
|---|---|---|---|
| D1 methodology_rigor | mandatory | Methodology: `pass` | `pass` |
| D2 domain_accuracy | mandatory | Domain: `warn` | `warn` |
| D3 argumentative_coherence | mandatory | Methodology: `pass`; DA: `pass` | `pass` |
| D4 cross_disciplinary_relevance | high | Perspective: `warn` | `warn` |
| D5 writing_and_structure | normal | EIC: `pass` | `pass` |
| D6 venue_fit_and_contribution | mandatory | EIC: `warn` | `warn` |

No assessed eligible seat declared a `block` or fatal block. The EIC's D6
score is carried mechanically from its card; because the criteria binding is
unavailable, it is not converted into a claim that a named venue's criteria
were assessed.

### Failure-condition receipt

| Condition | Fired | Mechanical basis |
|---|---:|---|
| F1 | false | No mandatory dimension has a fatal block. |
| F2 | false | No mandatory dimension scores `block`. |
| F3 | true | D2 and D6 are two mandatory dimensions scoring `warn` or worse. Each has one assessed eligible owner seat, so that seat decides the per-dimension majority test. |
| F4 | false | The high-priority dimension D4 scores `warn`, not `block`. |
| F5 | true | D2, D4, and D6 score `warn` or worse. |
| F0 | false | Not every dimension scores `pass`. |

F3 has the highest severity among the fired conditions and mechanically sets
the decision to Major Revision. F5 is also retained in the audit rather than
being suppressed by the higher-severity action.

## Editorial decision

**Major Revision.** The decision is contract-derived. The cards support the
central proof's methodology and argumentative chain (D1 and D3 pass), and no
card reports a fatal or repairable block. At the same time, the contract treats
the simultaneous mandatory warnings on domain accuracy/context (D2) and
venue-fit/contribution framing (D6) as sufficient for Major Revision. The
cross-disciplinary warning on D4 independently contributes to F5. This
decision does not impose an author work order or predetermine author triage.

## Panel consensus and divergence

### Cross-card convergence

- The cards converge on the soundness and careful delimitation of the central
  nonlift argument. The EIC identifies a precise principal contribution and
  disciplined scope (EIC S1--S3); Methodology finds the categorical levels,
  two site-specific injectivity arguments, overlap detector, all-index
  construction, and Ext variance sound (Methodology S1--S5); Domain reaches
  the same favorable assessment of the arithmetic obstruction, site
  refinements, source correction, and Ext consequence (Domain S1--S4);
  Perspective finds the descent and categorical boundaries accessible
  (Perspective S1--S4); and the DA concludes that its strongest attacks do not
  prevail.
- The distinction among presheaf representatives, sheaf sections, and
  cover-local representatives is independently emphasized by EIC S2,
  Methodology S1, Perspective S1, and the DA's Genuine Strength.
- The extension-theoretic consequence is supported from complementary angles
  by Methodology S5, Domain S4, Perspective S2--S3, and the DA's Adversarial
  Disposition.
- Two issue families receive cross-card corroboration without being promoted
  to four-seat consensus: contribution/literature positioning appears in EIC
  W1 and Domain W1, while project-internal Route/Gate language appears in EIC
  W2 and Perspective W3. The two findings in each family remain separately
  traceable because their stated evidence and requested repairs are not
  identical.

These are descriptions of cross-card convergence, not formal
`CONSENSUS-3`/`CONSENSUS-4` labels. Sprint-contract arithmetic operates on
role-scoped dimensions, and silence by a card is not counted as agreement.

### Disagreement and arbitration

No reviewer card explicitly disputes another card's finding, severity, or
proposed response. The D2, D4, and D6 warnings concern different eligible
dimensions and therefore do not conflict with the D1, D3, and D5 passes.
There is consequently no card-versus-card split requiring editorial
arbitration. The DA's strongest counter-argument is resolved within the DA
card itself as unsuccessful and is not elevated into a new panel finding.

## Source-ordered, non-ranking revision-response ledger

The rows below preserve reviewer-card source order. Their order is neither a
priority ranking nor a proposed work sequence. The final column transports
the originating card's suggestion; it is not an inferred author decision,
and no schedule or time estimate is assigned.

| Source ref | Transported severity | Evidence anchor | Card finding | Card-proposed response |
|---|---|---|---|---|
| EIC-W1 | Major | `absence: Introduction and bibliography` | The originality and significance case is underdeveloped: the related-work record is too narrow to establish distinctiveness and broader significance confidently. | Expand the relevant comparison, record the search scope reproducibly, and state proposition by proposition what the result adds beyond the closest precedents. |
| EIC-W2 | Minor | `text: Section 7, “In the project's separate Route-A/Route-B roadmap...”` | An internal project-roadmap paragraph interrupts the scholarly conclusion. | Remove it from the public manuscript or relocate it to internal project documentation. |
| EIC-W3 | Minor | `text: Declarations, “AUTHOR TO CONFIRM...”` | Authorship, contributions, funding, and competing-interest metadata remain unresolved. | Resolve the placeholders, confirm provisional classification metadata, and obtain the stated human approvals before submission or public release. |
| Domain-W1 | Minor | `absence: Introduction literature-positioning paragraph following Corollary 1.3` | The dated bounded novelty screen is not auditable because its indexes, queries, inclusion bounds, and result ledger are absent. | Add a compact footnote or appendix with indexes, query clusters, cutoff date, and nearest-hit dispositions while retaining the bounded, non-priority wording. |
| Domain-W2 | Minor | `text: Corollary 1.3, “For N>1 and every endomorphism...”` | The extension class and related notation are not indexed by topology even though the two classes live in different abelian categories. | Quantify the topology and write topology-indexed forms such as `e_tau`, `K_tau`, and the corresponding category-qualified Ext group. |
| Perspective-W1 | Minor | `absence: Introduction and Section 2` | The finite-flat covering-family convention is not defined early. | State the convention at first use and identify the subcanonicity property used later. |
| Perspective-W2 | Minor | `absence: Introduction and conclusion` | The portable descent-obstruction template remains implicit rather than being separated from the Witt-specific inputs. | Add a short remark listing the abstract pattern and separately label the arithmetic and site-specific hypotheses used here. |
| Perspective-W3 | Minor | `text: Section 7, “It therefore assigns no Route coordinates and no Gate A--E credit...”` | Unexplained project-internal labels interrupt the standalone scope statement. | Remove the clause or replace it with a self-contained statement that the argument uses no dynamical or operator-theoretic structure while retaining the sheaf-theoretic meaning of “lift.” |

The Methodology card reports no weakness after its stated D1/D3 coverage
checks. The DA card contains no Critical or Major finding. Its two
Observations remain non-defects: the full big-Witt sheaf assertion is
compressed but not an inferential gap, and the word “refinement” is a reading
hazard rather than a mathematical defect. They are therefore not promoted
into the revision-response ledger.

## Devil's Advocate terminal gate

The DA `CRITICAL` table is empty, so there are no Critical IDs to validate,
reject, or leave unresolved. No phantom adjudication is introduced. The
mechanical decision is not Accept, and no DA-versus-Accept escalation marker
is applicable.

## Review Panel Provenance (#540/#740)

The supplied provenance artifact reports the following six axes without
collapsing them into an independence score or claim:

| Axis | Recorded value | Scope or implication |
|---|---:|---|
| `blind_to_peer_outputs` | `true` | The five seats did not receive peer outputs before commitment. |
| `fresh_context` | `true` | Limited to `within_panel_attempt_only`; it says nothing about retry or later-round freshness. |
| `human_distinct` | `false` | The seats are model-executed, not five distinct human reviewers. |
| `model_family_distinct` | `unknown` | Cross-family separation was not established. |
| `provider_distinct` | `unknown` | Cross-provider separation was not established. |
| `role_separated` | `true` | The EIC, Methodology, Domain, Perspective, and DA roles were separately committed. |

Model-family provenance is incomplete; cross-family separation is unknown,
so correlated-error risk cannot be ruled out. Persona and context separation
are not evidence of independent error processes.
