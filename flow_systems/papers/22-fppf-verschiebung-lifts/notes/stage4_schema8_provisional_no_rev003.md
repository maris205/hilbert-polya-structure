# Stage 4 provisional Schema 8 companion — Round 1

> **SUPERSEDED.** This pre-apply five-item snapshot is retained as writer-side
> provenance.  The complete post-apply six-item artifacts are
> `stage4_response_to_reviewers_round1.json` and
> `stage4_response_to_reviewers_round1.md`.

**CANDIDATE_INCOMPLETE_PENDING_AUTHOR_FACTS**

This is a provisional writer-side companion, not a complete or final Schema 8
artifact.  The patch candidate has not been applied.  REV-003 is omitted
entirely because explicit byline, contribution, funding, and competing-interest
facts have not been supplied; its authorization scope does not authorize the
writer to invent those facts.

The five judgments below are conditional on successful deterministic apply of
stage4_revision_patch_candidate_no_rev003.json.  The orchestrator must populate
change_block_ids and the final change_location values from the apply report,
and must compute word_count_delta after apply.  Nothing below represents those
post-apply facts.

## Provisional response judgments

### REV-001

**Reviewer comment:** The manuscript does not yet support its originality and
broader significance with a sufficiently developed, reproducible comparison
to the closest relevant work.

**Provisional Schema 8 status judgment:** RESOLVED, conditional on successful
apply.

**Author response draft:** We have expanded the Introduction's
literature-positioning block with proposition-level comparisons to the exact
source, the nearest algebraic presentation result, and the general sheaf and
extension formalism already cited in the manuscript.  The revision also records
the 25 August 2026 search surfaces, query clusters, post-source date boundary,
inclusion rule, and nearest-hit dispositions.  It states only that no direct
post-source solution was located within that declared search and expressly
disclaims a global priority claim.  The candidate introduces no new BibTeX key.

**Intended target and operation:** B0022, replace_block.

**Mechanical fields:** change_block_ids and final change_location are pending
the orchestrator's apply report.

**Decline justification:** Not applicable.

### REV-002

**Reviewer comment:** The conclusion contains unexplained project-internal
Route and Gate terminology that interrupts the standalone mathematical scope
statement.

**Provisional Schema 8 status judgment:** RESOLVED, conditional on successful
apply.

**Author response draft:** We have removed the project-internal Route-A,
Route-B, Route-coordinate, and Gate A--E paragraph.  The surrounding public
mathematical scope statement and conclusion remain intact.

**Intended target and operation:** B0091, delete_block.

**Mechanical fields:** change_block_ids and final change_location are pending
the orchestrator's apply report.

**Decline justification:** Not applicable.

### REV-004

**Reviewer comment:** The extension class, kernel sheaf, and Ext group are
written without topology indices even though the fppf and finite-flat
statements live in different abelian categories.

**Provisional Schema 8 status judgment:** RESOLVED, conditional on successful
apply.

**Author response draft:** We have quantified
\(\tau\in\{\fppf,\ff\}\), introduced \(\Ksh_\tau\) and \(e_\tau\), and
placed each class in
\(\Ext^1_{\mathrm{Ab}(\mathscr C_\tau)}(\Wsh,\Ksh_\tau)\).  The
corollary, Section 5 setup, and proof now use the same topology-indexed
notation, with an explicit local abbreviation for the untouched continuation
of the proof.

**Intended targets and operations:** B0019, B0020, B0069, and B0073, each
replace_block.

**Mechanical fields:** change_block_ids and final change_location are pending
the orchestrator's apply report.

**Decline justification:** Not applicable.

### REV-005

**Reviewer comment:** The finite-flat covering-family convention is not
defined when that topology is introduced and contrasted with fppf.

**Provisional Schema 8 status judgment:** RESOLVED, conditional on successful
apply.

**Author response draft:** We have defined a finite-flat cover as a jointly
surjective family of finite flat morphisms, identified the corresponding
affine ring maps as finite locally free, and stated the subcanonicity property
used for the structure sheaf and descent.  The finite-flat theorem remains
logically separate from the fppf theorem.

**Intended target and operation:** B0016, replace_block.

**Mechanical fields:** change_block_ids and final change_location are pending
the orchestrator's apply report.

**Decline justification:** Not applicable.

### REV-006

**Reviewer comment:** The reusable categorical descent-obstruction pattern
remains implicit rather than being separated from the Witt-specific arithmetic
and site-dependent inputs.

**Provisional Schema 8 status judgment:** RESOLVED, conditional on successful
apply.

**Author response draft:** We have separated the conditional categorical
template from its arithmetic and site-specific instantiation.  The template
now fixes \(v\), a source section \(z_0\), and the selected target
\(w=v(p(z_0))\); it explains why an inducing-\((u,v)\) middle map would
supply the forbidden global preimage before invoking the
pushout--pullback criterion.  The conclusion states the theorem's exact
quantifier \(N>1\), lists Dedekind injectivity, rational-Witt sheaf,
finite-flat/subcanonical, big-Witt detector, and torsion-freeness inputs, and
describes the four finite-algebra calculations only as the explicit
computational core rather than as the entire verification.

**Intended targets and operations:** B0023 and B0092, each replace_block.

**Mechanical fields:** change_block_ids and final change_location are pending
the orchestrator's apply report.

**Decline justification:** Not applicable.

## Provisional subset summary

- Conditional resolved judgments: 5
- Conditional deliberate limitations: 0
- Conditional unresolvable judgments: 0
- Conditional reviewer disagreements: 0
- Provisional new references added: 0
- word_count_delta: PENDING_ORCHESTRATOR_APPLY_REPORT
- change_block_ids: PENDING_ORCHESTRATOR_APPLY_REPORT
- Final round summary: NOT AVAILABLE while REV-003 awaits explicit author
  facts and while the candidate remains unapplied.

The orchestrator must not promote these conditional judgments to a final
Response to Reviewers until the apply report verifies the landed operations
and supplies the mechanical fields.
