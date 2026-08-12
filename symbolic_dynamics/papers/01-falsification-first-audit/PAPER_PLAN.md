# Paper Plan

**Title:** Falsification-First Symbolic Dynamics for Arithmetic Determinants: Six Audits and Seven Scoped Obstructions
**One-sentence contribution:** We source-lock and adversarially audit six symbolic-dynamics constructions against five same-object obligations, prove seven scoped obstructions, and find that no frozen candidate unlocks the operator route.
**Format:** anonymous shareable preprint (`article`, not an ICLR submission)
**Type:** theory + reproducible diagnostic audit
**Date:** 2026-08-12
**Target length:** approximately 12--16 pages including references and appendices
**Section count:** 8 numbered main sections plus appendix

## Claims--Evidence Matrix

| Claim | Exact evidence | Numerical/certificate evidence | Status | Main location |
|---|---|---|---|---|
| C1. The protocol is source-locked, object-local, and falsification-first. | `SESSION4_PREREGISTRATION.md`; `docs/METHODOLOGY.md`; six Route-A YAML source locks | frozen manifests and complete seed ledgers | Supported as a protocol fact | Sections 1 and 3 |
| C2. Seven recurring failure modes admit scoped proofs. | `docs/obstruction_registry.md`; four proof packages | finite checks are illustrative only | Proved under stated hypotheses | Section 4 and Appendix A |
| C3. No one of the six frozen objects passes A0--A4; Route B remains locked. | six Route-A YAML records | none required | Proved by inspection of frozen evaluations; not a universal no-go theorem | Sections 5 and 6 |
| C4. Exact and finite audits distinguish implementation validity from target validity. | exact identities embedded in JSON/CSV and proof packages | 29 tests; Gauss, wheel, renewal, and Knauf diagnostics | Supported within finite cutoffs | Section 6 |

### Evidence accounting rules

- Each theorem is cited to its proof artifact and restated with its assumptions.
- Each number in the prose is sourced from an existing JSON/CSV/YAML artifact.
- No cell from one candidate supplies a missing gate for another candidate.
- `NUMERICAL_OBSERVATION` never becomes `PROVED` in the paper.
- `route_b_invocation_allowed: false` is reported for all six records.

## Structure

### Abstract

- State the six-object scope in the first sentence.
- Explain the same-object A0--A4 requirement.
- State the strongest exact result: seven scoped obstructions.
- Give concrete finite-audit scale: 63,319 Gauss necklaces, 98,460 wheel vertices, and $2^{22}$ Knauf states.
- End with the negative but bounded conclusion; no citations.

### 1. Introduction

- Motivate why determinant resemblance without source discipline is non-identifying.
- State the five obligations and the no-coordinate-mixing rule.
- Preview the result matrix (Figure 1).
- Give four falsifiable contributions matching C1--C4.
- Explicitly state nonclaims: no exhaustive search, no RH proof, no Route B.

### 2. Context and Related Work

- Periodic-point and transfer-operator determinants: Artin--Mazur, Bowen--Lanford, Ruelle, Pollicott.
- Countable/renewal systems: Sarig and the distinction between flexibility and arithmetic identification.
- Arithmetic symbolic systems: squarefree/ℒ-free work.
- Natural analytic benchmarks: Mayer and Knauf.
- Position the paper as an obligation audit rather than a new determinant construction.

### 3. Audit Protocol

- Formalize the source lock $C=(X,T,\tau,\phi,\mathcal B,D)$.
- Define A0 arithmetic origin, A1 orbit ledger, A2 determinant, A3 global structure, A4 lift.
- Separate exact theorem, finite certificate, numerical observation, modeling choice, open claim.
- Describe controls, forbidden data, stop rules, and Route-B lock.
- State that no Riemann-zero data were loaded.

### 4. Scoped Obstructions

- Theorem 1: finite-memory divisor obstruction, with main-body proof.
- Proposition 2: squarefree periodic collapse.
- Proposition 3: renewal inverse design.
- Proposition 4: mixed primitive words and finite-unitary non-erasure.
- Proposition 5: unary regular/context-free prime-length obstruction.
- Proposition 6: wheel prime induction and acyclicity.
- Put fuller proof details and edge cases in Appendix A.

### 5. The Six Frozen Objects

- One subsection per candidate, each with: source definition, best supported coordinate, blocking gate, and claim boundary.
- For `SD-C04`, distinguish finite word enumeration from Mayer's infinite-dimensional determinant theorem.
- For `SD-C06`, distinguish source-proved unsigned limit from the open signed region and from any periodic-orbit determinant.

### 6. Reproducible Finite Audits

- Explain commands, seeds, precision, and test counts.
- Insert Figure 2 with the Gauss, wheel, and Knauf panels.
- Report renewal on/off-circle reconstruction as a negative identifiability control.
- Discuss finite-cutoff and precision boundaries.
- Insert YAML-derived Table 1 if space permits.

### 7. What the Negative Result Does and Does Not Say

- Explain the empty row-wise intersection of A0--A4.
- Prohibit coordinatewise synthesis of `SD-C04`, `SD-C05`, and `SD-C06`.
- Enumerate escape classes not covered by the no-go theorems.
- Record later-family ideas only as out-of-scope clues, without development.

### 8. Conclusion

- Rephrase the audit contribution.
- State the reusable stop rules.
- Give the next admissible step: source-lock a new same-family object and restart at A0.

### Appendix A. Proof Details

- Full assumptions and proofs for the seven obstructions.
- Explain why zero-free entire factors cannot repair divisor growth.
- Preserve renewal and wheel edge cases.

### Appendix B. Reproducibility and Evidence Ledger

- Commands, data paths, fixed seeds, cutoffs, precision, and artifact roles.
- Claims-to-artifact table.
- Figure regeneration command.

## Figure and Table Plan

| ID | Type | Content | Data source | Script | Priority |
|---|---|---|---|---|---|
| Figure 1 | categorical matrix | A0--A4 verdicts for all six rows, with a separate Route-B lock marker | `evaluations/route_a/*/*.yaml` | `figures/gen_fig1_route_a_matrix.py` | High |
| Figure 2 | three-panel diagnostic | Gauss primitive/collision counts by cutoff; wheel unit-set Jaccard by control and level; Knauf absolute benchmark error versus $\Re(s)$, separated by theorem-domain status | existing CSV files; JSON summaries used for consistency assertions | `figures/gen_fig2_finite_audits.py` | High |
| Table 1 | generated LaTeX table | exact candidate verdict tuple and overall status | six Route-A YAML records | `figures/gen_table1_candidate_matrix.py` | High |

### Figure 1 caption intent

“Each row is one frozen object; cells are not composable across rows. No row reaches the complete A0--A4 chain, and every Route-B flag is false.” The figure should let a skim reader recover the paper's result without reading candidate details.

### Figure 2 caption intent

“Finite computations validate obligation-specific behavior rather than the Riemann divisor.” Panel (a) exposes both the exact Gauss ledger and noninjective trace labels. Panel (b) separates the arithmetic wheel deletion from matched controls while showing that every construction remains acyclic. Panel (c) distinguishes values inside the source-proved Knauf region from continuation benchmarks outside it.

## Citation Plan

- Introduction: Artin--Mazur; Bowen--Lanford; Ruelle.
- Related work: Pollicott; Sarig; Cellarosi--Sinai; El Abdalaoui et al.; Mayer 1990/1991; Knauf 1998 + erratum; Esparza et al.
- Theory: NIST DLMF for Riemann--von Mangoldt; Esparza et al. for unary semilinearity.
- Candidate sections: Mayer and Knauf primary records only where their source theorems are used.
- Bibliography entries must be derived from the locally audited DOI/arXiv records and contain no uncited entries.

## Internal Review Before Compilation

- Does every abstract/introduction claim appear in the matrix above?
- Is each negative theorem explicitly scoped?
- Is any numerical trend described as convergence outside a proved domain? If yes, weaken it.
- Does any sentence combine candidate strengths? If yes, rewrite it as a contrast.
- Are all plot values loaded from source artifacts rather than typed into plotting scripts?
- Are all references/citations defined and locally verified?
- Is the author block anonymous and free of repository-identifying links?

## Pipeline State

- [x] Phase 1: narrative report and paper plan
- [ ] Phase 2: reproducible figures and generated table
- [ ] Phase 3: complete modular LaTeX draft
- [ ] Phase 4: compilation and PDF checks
- [ ] Phase 5: intentionally deferred for unified external review
