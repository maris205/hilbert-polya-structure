# P25 Stage 3 — Editorial Synthesis and Decision

Date: **2026-08-29**  
Mode: **ARS `reviewer_full` under `reviewer/reviewer_full/v2`**  
Decision authority: **mechanical Schema 13.2 sprint-contract synthesis**  
Calibration status: **`NOT_CALIBRATED`**

## Scope, panel, criteria binding, and immutable route boundary

Five usable Phase-2 cards are present for the fixed roles `eic`,
`methodology`, `domain`, `perspective`, and `da`; panel cardinality is 5/5.
The Phase-0 record supplies no author-confirmed venue, track, article type,
ReviewTargetContext, or bound target criteria. This synthesis therefore
carries the exact unbound state:

criteria_binding_unavailable

This is a field-general scientific assessment. It makes **no venue-fit,
venue-alignment, or submission-readiness claim**. D6 is used only as the
Journal-Fit card's general contribution-positioning assessment; it is not a
claim about any named or inferred venue.

The review, decision letter, ledger, and every proposed response preserve the
frozen object and route boundary exactly:

- the unit-roof symbolic control remains
  `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` with
  `ROUTE_A_REJECTED`;
- the physical three-disk-flow tuple remains **unassigned** because scalar
  clock transfer is disproved;
- symbolic A1/A2 credit does **not** transfer to the physical flow; and
- Route B is not invoked: no Route-B operator or spectral realization is
  supplied or implied.

The manuscript and five reviewer cards are immutable, read-only inputs. This
document does not amend them and does not authorize manuscript revision.

## Machine audit receipt

```text
dimension_verdicts: [D1=warn, D2=warn, D3=warn, D4=pass, D5=pass, D6=warn]
fired_conditions: [F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision
```

The DA CRITICAL table is empty. There are no `C<n>` IDs to adjudicate, no
rejection-rationale line to supply, and no DA-critical-versus-accept marker.
The DA's two MAJOR rows remain decision-relevant review findings and are
carried separately as SC-09 and SC-10 below.

## Role-scoped scoring matrix

Only assessed scores from contract-eligible roles enter the matrix.
Ineligible `not_assessed` rows are structural exclusions, not votes or
abstentions. The audit verdict is the worst assessed eligible score and is
distinct from each failure condition's cross-reviewer quantifier.

| Dimension | Priority | Eligible role(s) | Assessed eligible scores parsed from cards | Assessed n | Audit verdict |
|---|---|---|---|---:|---|
| D1 `methodology_rigor` | mandatory | methodology | methodology=`warn` | 1 | `warn` |
| D2 `domain_accuracy` | mandatory | domain | domain=`warn` | 1 | `warn` |
| D3 `argumentative_coherence` | mandatory | da, methodology | da=`warn`; methodology=`pass` | 2 | `warn` |
| D4 `cross_disciplinary_relevance` | high | perspective | perspective=`pass` | 1 | `pass` |
| D5 `writing_and_structure` | normal | eic | eic=`pass` | 1 | `pass` |
| D6 `venue_fit_and_contribution` | mandatory | eic | eic=`warn` | 1 | `warn` |

No dimension is unassessed. No eligible role issued a `block`, and no fatal
block exists.

### Five-card scoring profiles

These five categorical profiles are parsed from the cards rather than
assumed. Sprint cards do not contain per-seat editorial recommendations, so
none is inferred.

| Source card | Verbatim assessed profile | Strengths recorded | Weaknesses carried forward |
|---|---|---:|---:|
| Journal-Fit Reviewer (`EIC`) | D5=`pass`; D6=`warn` | 4 | 3 |
| Methodology / certificate (`R1`) | D1=`warn`; D3=`pass` | 4 | 3 |
| Domain / theorem (`R2`) | D2=`warn` | 5 | 1 |
| Quantum-scattering / operator perspective (`R3`) | D4=`pass` | 3 | 1 |
| Devil's Advocate (`DA`) | D3=`warn` | narrative scope-pressure assessment | 0 CRITICAL; 2 MAJOR |

## Failure-condition receipt

The contract's cross-reviewer quantifier is applied within each selected
dimension first; the expression's dimension quantifier is applied second.
For a one-seat dimension, `majority` is the owner seat. For D3's two eligible
seats, `majority` requires both seats.

| Condition | Severity | Mechanical evaluation | Fired |
|---|---:|---|---|
| F1 — any mandatory dimension has a fatal block (`any`) | 95 | D1, D2, D3, and D6 have no fatal block. | false |
| F2 — any mandatory dimension scores `block` (`any`) | 90 | No assessed eligible mandatory score is `block`. | false |
| F3 — two or more mandatory dimensions score `warn` or worse (`majority`) | 70 | D1: true (1/1); D2: true (1/1); D3: false (1/2, while 2/2 are required); D6: true (1/1). Three mandatory dimensions pass the per-dimension test, so the two-or-more test is met. | **true** |
| F4 — any high-priority dimension scores `block` (`any`) | 60 | D4 is the only high-priority dimension and scores `pass`. | false |
| F5 — any dimension scores `warn` or worse (`any`) | 40 | D1, D2, D3, and D6 each contain at least one eligible `warn`. | **true** |
| F0 — every dimension scores `pass` (`all`) | 10 | D1, D2, D3, and D6 do not score uniformly `pass`; the universal condition fails. | false |

F3 and F5 fire. F3 has the higher severity and supplies the binding action.
No confidence value, qualitative recommendation matrix, venue inference, or
post-hoc appraisal may soften or harden that action.

## Part 1 — Editorial decision letter

Dear Author,

Thank you for submitting *Why a Unit-Roof Symbolic Determinant Does Not
Transfer to the Physical Three-Disk Flow* for field-general scholarly review.
The manuscript was evaluated through five role-separated review seats under
the fixed Schema 13.2 sprint contract. I write to convey the resulting
editorial action: **Major Revision**.

The panel found a sound and useful mathematical core. The period-two and
period-three witnesses give an exact positive roof gap and a sufficient
obstruction to constant cohomology and owner-preserving scalar transfer. The
unit-roof determinant family and local half-density factorization are kept in
their proper symbolic and stability types. The finite replay is explicitly
downstream of the proof, retains conditioned rows, and does not transfer its
certificate into a physical-flow determinant. The manuscript's most
important strength is this unusually disciplined separation of symbolic,
physical, semiclassical, and exact-scattering objects.

The Major Revision action is nevertheless mechanically required. The owner
seats warn three mandatory dimensions under F3: methodology rigor (D1), domain
accuracy (D2), and general contribution positioning (D6). The revision must
therefore make the computational provenance self-contained, repair the stale
hash trail and early receipt bindings, position the result against established
open-billiard transfer-operator and zeta literature, and state more precisely
what is new. It must also clarify what marginal scientific quantity the
2,241-row replay contributes after the exact two-witness proof, or demote it
unambiguously to solver/reproducibility verification. The exposition can be
improved by consolidating the four-object map and reducing repeated boundary
statements without weakening any scope guard.

This is a revision action, not a rejection: no card records a block or fatal
block, the DA records no CRITICAL item, and all five cards preserve the exact
scalar-clock obstruction and route boundary. It is also not a venue-fit or
submission-readiness assessment, because no venue or criteria binding exists.
Every requested response must leave the symbolic tuple rejected, the physical
tuple unassigned, symbolic A1/A2 credit nontransferable, and Route B closed.

Sincerely,  
Editorial Synthesizer

## Decision basis: cross-card convergence and divergence

Silence is neither agreement nor opposition. Confidence values are
self-reported competence/scope disclosures only; they do not weight findings,
alter severity, change consensus counts, or resolve disagreement.

### Convergence

1. **Core proof and typing boundary.** All five cards preserve the exact
   two-witness obstruction and the symbolic/physical separation. No card
   transfers symbolic credit, assigns the physical tuple, or invokes Route B.
2. **Originality and prior-work positioning require repair.** EIC-W1, R2-W1,
   and DA-M1 converge on a missing direct comparison with the closest
   nonconstant-roof, open-billiard transfer-operator, and dynamical-zeta
   literature. Across the four non-DA seats this is a corroborated 2/4 finding
   (EIC and R2), not `CONSENSUS-3` or `CONSENSUS-4`; the DA challenge is tracked
   outside that denominator.
3. **Replay purpose and reader payoff need a sharper contract.** EIC-W3 and
   DA-M2 agree that the finite replay's role after the exact proof is not yet
   sufficiently concrete. They do not dispute the replay tallies or proof.
4. **Consolidation can improve rather than relax the scope boundary.** EIC-W2
   and R3-W1 point in a compatible direction: a compact four-object map can
   replace distributed repetition while retaining the same clock, state-space,
   determinant, and route distinctions.
5. **Reproducibility gaps are localized.** R1's three findings concern a
   missing complete environment lock, a stale advertised bibliography hash,
   and incomplete early-round receipt binding. The analytic theorem and frozen
   replay counts are not challenged by those findings.

### Divergence and editorial adjudication

| Issue | Card positions | Editorial resolution |
|---|---|---|
| D3 eligible-seat score difference | R1 passes D3 because the exact proof chain is coherent; DA warns D3 because novelty and replay-value inferences remain under-supported. | Preserve both. The D3 audit verdict is `warn`, F5 sees the DA warning, but F3's D3 majority predicate is false because only 1/2 eligible seats warns. D3 is not informally upgraded into an F3 driver. |
| Replay remedy direction | EIC-W3 asks for a compact worked downstream implication if warranted, or a conceptual-ownership framing; DA-M2 asks for a distinct replay estimand or strict demotion to implementation verification. | Require the author to state and support the replay's distinct estimand, or label it strictly as solver/reproducibility evidence. A schematic implication is optional only if it follows from existing results and is explicitly not a new physical determinant, pressure, resonance, operator, or spectral result. |
| Prior-work correction versus novelty allocation | R2-W1 identifies concrete established open-billiard operator/zeta results and an overbroad “remain open” sentence; EIC-W1 and DA-M1 focus on what increment is actually new. | Apply one shared literature-and-claim-allocation operation, while responding to each source separately. Replace field-level open-status language with manuscript-scoped language and distinguish any new theorem, equilateral witness calculation, minimax result, certificate, or synthesis from established frameworks. |
| Boundary repetition versus accessibility | EIC-W2 asks to reduce repeated disclaimers; R3-W1 asks for a consolidated four-object comparison. | These are compatible, not a split. Consolidate the comparison near the first object-typing discussion, then retain only the boundary statements needed at theorem interpretation and conclusion. |
| Uncontradicted methodology findings | R1-W1, R1-W2, and R1-W3 are not discussed by the other cards. | Retain each as a single-reviewer finding. Non-mention does not turn any one into consensus, opposition, or a removable concern. |

No weakness sub-claim has an explicit disputing position from another non-DA
reviewer, so no formal `[SPLIT]` finding is created. The adjudications above
resolve differences in focus, remedy direction, or eligible-seat scoring
without inventing peer positions.

## Source-ordered, non-ranking revision-response ledger

The immutable source order is EIC → R1 → R2 → R3 → DA. `SC-01` through
`SC-10` are stable trace keys, **not priorities or a work order**. Every actual
weakness from every card appears once, including both DA MAJOR rows. The author
must answer every row separately even where one roadmap operation addresses
corroborating findings together.

| Trace key | Source finding | Transported severity | Confidence | Actual weakness and typed evidence anchor | Required point-by-point response | Roadmap |
|---|---|---|---|---|---|---|
| SC-01 | EIC-W1 | Major | 4/5 | Originality is not positioned against the closest roof literature. `absence: Related work, background, and three distinct objects — expected a direct comparison with prior roof-noncohomology or non-lattice results for open billiards and an explicit novelty statement; checked Introduction, Related work, Physical roof obstruction, and bibliography` | Add a verified closest-work comparison and allocate novelty among the equilateral two-witness calculation, owner-preserving scalar-transfer formulation, minimax bound, finite certificate, and their synthesis; narrow any claim that the comparison does not support. | REV-01 |
| SC-02 | EIC-W2 | Minor | 5/5 | Repeated boundary statements slow the middle and final sections. `text: Introduction and Conclusion — “The distinction between exact, semiclassical, and symbolic objects is mathematical, not terminological.” and “The next viable physical step is a genuinely nonconstant-roof operator with explicit ownership and analytic control”` | Consolidate the route/object boundary near the definitions and at final interpretation, remove avoidable repetition, and preserve every substantive scope guard. | REV-02 |
| SC-03 | EIC-W3 | Minor | 4/5 | Practical reader value remains one step removed from the proved obstruction. `absence: Consequences for products and repetitions — expected a compact worked example of how scalar-clock substitution changes one downstream physical-flow quantity; checked Consequences for products and repetitions, Locked physical-orbit replay, Robustness interpretation, and Conclusion` | Provide a tightly scoped schematic implication if existing results warrant it; otherwise explicitly frame the significance as a conceptual clock-ownership theorem without implying demonstrated downstream physical or spectral impact. | REV-03 |
| SC-04 | R1-W1 | Minor | 5/5 | The computational environment is recorded but not reproducibly pinned. `absence: Round-2--8 computational package — expected a pinned Python, NumPy, SciPy, mpmath, and platform environment; checked source programs, tests, validation notes, receipts, and reproduction scripts` | Add a machine-readable dependency lock or container specification and document the platform needed for the high-precision and compiled numerical paths. | REV-04 |
| SC-05 | R1-W2 | Minor | 5/5 | The data-and-code statement points to a stale bibliography hash in `paper/stage2_manuscript_audit.md`: `acec8403...` rather than the current frozen `de776cc0...`. `dataset: paper/stage2_manuscript_audit.md, Deliverables and integrity table, compared with notes/stage2_5_integrity_report.md, Outcome table` | Update the advertised audit path to a current immutable manifest or otherwise make the reader-facing verification path resolve to the current frozen bibliography hash. | REV-05 |
| SC-06 | R1-W3 | Minor | 5/5 | Early-round receipts do not fully bind the source and tests they summarize. `dataset: experiments/round2_receipt.json through experiments/round5_reproducibility_receipt.json, source/test binding fields` | Extend the receipt bindings retrospectively or provide one frozen manifest that binds every Round-2--8 source, test, input, output, and command. | REV-06 |
| SC-07 | R2-W1 | Major | 5/5 | Established open-billiard transfer and zeta theory is under-positioned, and “remain open” reads as a field-level claim. `text: Limitations, first paragraph — “Its functional setting, analytic continuation, and relation to physical or semiclassical quantities remain open.”` | Replace the field-level wording with manuscript-scoped wording; add a focused, verified account of established open-billiard Ruelle operators, weighted zeta functions, meromorphic continuation, and direct coding; state exactly what this manuscript does not construct or compare. | REV-01 |
| SC-08 | R3-W1 | Minor | 4/5 | The four-object map is distributed rather than consolidated. `absence: Related-work and object-typing discussion — expected one compact four-object comparison of state space, clock or weight, determinant status, and relation type; checked physical-flow, unit-roof, semiclassical, exact-scattering, Route-A, and limitations surfaces` | Add a compact four-row comparison that keeps the unit-roof symbolic determinant, prospective physical nonconstant-roof object, semiclassical construction, and exact boundary-channel determinant distinct. | REV-02 |
| SC-09 | DA-M1 | Major | 4/5 | Novelty is asserted more strongly than demonstrated; the classical determinant identity and necessary periodic-sum test are acknowledged, but no focused comparison identifies the specific three-disk increment. `text: Related work and physical-roof obstruction — “The reciprocal-determinant form of a finite-type shift zeta function is classical” and “We use only the necessary telescoping direction”` | Support the stronger novelty claim through verified prior-art comparison, or frame the contribution as a typed negative-control synthesis and reusable exact exposition. | REV-01 |
| SC-10 | DA-M2 | Major | 5/5 | The 2,241-row replay has under-specified marginal scientific value after the exact two-witness proof. `table: Table 1, locked scalar-clock replay counts at all three geometries` | Define and report a distinct replay estimand, or label the ledger strictly as reproducibility and solver-validation evidence; do not present its scale as additional proof of noncohomology. | REV-03 |

## Non-ranking revision roadmap

The roadmap follows the first occurrence of each source finding. It groups
SC-01/SC-07/SC-09 because they share one literature-positioning and
novelty-allocation operation, SC-02/SC-08 because consolidation is their
shared exposition operation, and SC-03/SC-10 because both require an explicit
contract for replay significance. Every transported severity remains visible;
grouping does not average, re-rate, rank, or merge the required source-by-source
responses.

| Roadmap ref | Source trace(s) and transported severity | Obligation class | Revision operation | Cost scope | Bounded consequence if unresolved |
|---|---|---|---|---|---|
| REV-01 | SC-01 Major; SC-07 Major; SC-09 Major | `must_fix` | Build a verified closest-work comparison, replace field-level open-status wording with manuscript-scoped wording, and allocate or narrow novelty across the exact witnesses, scalar-transfer formulation, minimax bound, finite certificate, and negative-control synthesis. | `section`: Introduction, Related work, physical-roof obstruction, Limitations, Conclusion, bibliography | `evidence_gap_remains` / `claim_scope_unsupported`: the D2 and D6 positioning concerns remain open. |
| REV-02 | SC-02 Minor; SC-08 Minor | `should_fix` | Add one compact four-object comparison and use it to consolidate repeated boundary language while retaining the necessary theorem-interpretation and final-scope guards. | `section`: first object-typing discussion plus organization pass | `reader_traceability_reduced`: object distinctions remain distributed and repetitive. |
| REV-03 | SC-03 Minor; SC-10 Major | `must_fix` | State a distinct scientific estimand for the replay and report only what supports it, or demote the ledger consistently to solver/reproducibility verification; calibrate practical-significance language to that choice. | `section` + `table`: Introduction, Locked physical-orbit replay, Table 1, Robustness interpretation, Conclusion | `interpretive_ambiguity_remains`: replay scale remains liable to be mistaken for additional proof or demonstrated downstream physical impact. |
| REV-04 | SC-04 Minor | `should_fix` | Add a machine-readable dependency lock or container/platform specification for the computational paths used by the certificate. | `other` `reproducibility_environment`: computational package and data/code availability surface | `method_reproducibility_unresolved`: the frozen run remains environment-dependent. |
| REV-05 | SC-05 Minor | `should_fix` | Repair the reader-facing hash trail so the cited audit or replacement manifest reports the current frozen bibliography digest. | `sentence` + `other` `integrity_manifest`: Data and code availability plus current audit pointer | `reader_traceability_reduced`: the advertised integrity check continues to fail on the frozen submission. |
| REV-06 | SC-06 Minor | `should_fix` | Supply a frozen manifest or retrospective receipt extension that binds every Round-2--8 source, test, input, output, and command. | `other` `provenance_manifest`: Round-2--8 receipt package | `method_reproducibility_unresolved`: early-round summaries remain incompletely source/test bound. |

Revision completion criteria, still stated in source-derived rather than work
order:

- **REV-01 acceptance criterion:** verified adjacent work is cited and compared
  accurately; “open” language is explicitly scoped to what this manuscript
  does not construct; every novelty statement identifies its precise increment
  without changing the frozen route boundary.
- **REV-02 acceptance criterion:** a reader can identify the state space,
  clock/weight, determinant status, and permitted relations of all four objects
  in one place, and repeated disclaimers are reduced without losing scope.
- **REV-03 acceptance criterion:** the replay has one explicitly stated
  estimand supported by its recorded outputs, or is consistently labeled only
  as implementation/reproducibility verification; nowhere is row count treated
  as a second proof or new determinant/spectral evidence.
- **REV-04 acceptance criterion:** a clean environment can be instantiated from
  machine-readable pinned dependencies or a container/platform specification
  covering Python, NumPy, SciPy, mpmath, and compiled paths.
- **REV-05 acceptance criterion:** the data/code statement's audit pointer
  resolves to a current frozen manifest whose bibliography digest matches the
  Stage-2.5 record.
- **REV-06 acceptance criterion:** one immutable provenance surface binds every
  named Round-2--8 program, test, input, output, validation command, and receipt.

No author triage, preferred display order, work order, permission to group
responses, claim-strength authorization, collateral authorization, or
manuscript-block write authority is inferred. The response letter must cite
each `SC-nn` row, state the author's disposition, describe the change or reason
for declining, and point to exact revised locations and evidence.

## Review panel provenance (#540/#740)

The provenance artifact replay-validates. Its observations are rendered
separately and are not reduced to a binary or numeric independence claim.

Artifact: `review-panel-provenance/1.0`  
Artifact raw SHA-256:
`374910c33588fb80bc1c8556ea4e3fc5101b843e71c4b7ace6a27a7d7f948a20`  
Panel ID: `p25-stage3-round1-2026-08-29`  
Contract ID: `reviewer/reviewer_full/v2`  
Contract SHA-256:
`e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`  
Normalized manifest SHA-256:
`8128deb65934ea7e55255e34463e0269021b0fff26daff9d9e84276f0f541abe`  
Execution topology SHA-256:
`a1f8e1998cabc29c3dff3c103f2a38a00a0fb2a020fba5816012bf1ab240cb4d`  
Fresh-context scope: `within_panel_attempt_only`

| Provenance axis | Recorded value | Meaning retained in this synthesis |
|---|---|---|
| `blind_to_peer_outputs` | `true` | No seat saw peer outputs before committing. |
| `fresh_context` | `true` | Contexts were distinct within this panel attempt only; this says nothing about retries or later-round history. |
| `human_distinct` | `false` | The five seats were model-executed, with no distinct accountable human reviewer identities. |
| `model_family_distinct` | `false` | Every seat used the `gpt-5` model family. |
| `provider_distinct` | `false` | Every seat used the `openai` provider. |
| `role_separated` | `true` | The five seats had distinct review roles. |

**Correlated-error disclosure:** All model-executed review seats used one
model family; role separation does not remove correlated-error risk.

Persona and role separation do not establish independent error processes. No
cross-family aggregate, same-model majority, or independence score is
computed.

## Mandatory scholar checkpoint

**Revision execution is not authorized until the scholar completes this
checkpoint.** The scholar must explicitly:

1. confirm or amend the Phase-0 field-general panel framing, while retaining
   `criteria_binding_unavailable` unless an author-confirmed ReviewTargetContext
   and resolved criteria binding are separately supplied;
2. adjudicate **each of SC-01 through SC-10 separately** as `will_address`,
   `wont_address`, or `not_on_point`, with a reason and the chosen minimum
   remedy or stronger evidence path;
3. confirm whether the proposed shared-operation groups
   SC-01/SC-07/SC-09, SC-02/SC-08, and SC-03/SC-10 may be implemented together
   while retaining separate point-by-point responses;
4. confirm that every revision will preserve the exact symbolic tuple
   `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` with
   `ROUTE_A_REJECTED`, leave the physical-flow tuple unassigned, transfer no
   symbolic A1/A2 credit, and invoke no Route B; and
5. authorize the exact manuscript or provenance blocks to be changed and the
   completion evidence for each accepted `REV-nn` item.

Until that explicit record exists, the roadmap is a reviewer-owned,
non-ranking proposal rather than an author decision. After any authorized
revision, the next substantive gate is a separate evidence-based re-review of
every ledger row. This synthesis does not revise the manuscript, authorize
Route advancement, or pre-judge a later re-review outcome.
