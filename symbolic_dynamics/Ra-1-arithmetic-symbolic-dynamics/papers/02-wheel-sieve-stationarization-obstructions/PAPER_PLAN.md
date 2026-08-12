# Paper Plan

**Title**: Scoped Obstructions to Stationarizing a Graded Wheel-Sieve
Symbolic System

**One-sentence contribution**: We give three precisely delimited
obstructions to adding periodic dynamics without losing the endogenous wheel
clock, and retain an as-yet undefined infinite observational recoding as a
project branch rather than a validated candidate.

**Format**: anonymous shareable theory preprint (not yet targeted to a
specific venue)

**Date**: 2026-08-12

**Evidence policy**: theorem-only; no numerical experiment, external dataset,
or empirical figure

**Target length**: 7--10 pages including appendices

## Claims--Evidence Matrix

| ID | Claim | Evidence | Boundary stated in paper | Section |
|---|---|---|---|---|
| C1 | Every periodic point under a strict equivariant extension map would project to a periodic point of the strictly graded wheel shift; hence none exists.  Independently, the graded source's full-backward-orbit inverse limit is empty. | Complete equivariance and backward-level proofs | New factors/recodings are not strict extensions | §3 |
| C2 | A strong forward-bisimulation quotient of a graph with no infinite forward path is acyclic; the finite-DAG case is a corollary. | Complete cycle-lifting proof | Infinite ray counterexample; arbitrary simulations/homomorphic images excluded | §4 |
| C2b | A quotient with one state-class decoder exact for every representative inherits an acyclic grading. | Complete quotient-grading proof; exact (q_{k+1}) corollary | Edge/path decoders that distinguish representatives are outside the result | §4 |
| C3 | A finite-alphabet fixed-finite-window decoder has finite image and cannot output an infinite exact wheel clock range. | Codomain-independent finite-domain/finite-image proof | Countable alphabet, infinite memory, and other unbounded inputs are not covered | §5 |
| C4 | A fully specified infinite observational recoding could be tested for arithmetic fidelity and compatible periodic words. | None yet: source lock incomplete | Must remain `NOT_TESTABLE` | §6 |

Every supported claim is backed by a formal proof.  C4 is included only as a
status statement and receives no evidentiary credit.

## Structure

### Abstract (170--220 words)

- Open with the specific graded wheel-sieve problem.
- State all three scoped obstructions.
- Give the two crucial non-coverage statements:
  - forward-well-founded strong bisimulation does not settle an infinite DAG
    with an infinite forward path;
  - finite-local decoding does not settle countable alphabets or infinite
    memory.
- End with the externally legible status: the observational recoding remains
  undefined/not testable, no determinant is defined, and analytic comparison
  is outside scope.

### §1 Introduction (1--1.5 pages)

- Explain why adding periodic orbits while preserving an endogenous,
  unbounded arithmetic clock is not a generic “make it stationary” task.
- Present the one-sentence contribution before technical detail.
- List three falsifiable theorem contributions and one non-result.
- Place Figure 1 after the contribution list.
- State explicitly that the paper contains no numerical experiments.

### §2 Graded wheel setup and category discipline (1 page)

- Define and prove the wheel recurrence, then define
  \(X=\bigsqcup X_k\), strict level growth, distinct unbounded
  \(q_{k+1}\), and \(\tau_k=\log q_{k+1}\).
- Define the project-specific level-blind stationarization convention.
- Define periodic points, strict extension, strong forward bisimulation,
  quotient edge, and finite local decoder.
- Include a scope table pairing each theorem with its assumptions and
  non-coverage class.

### §3 Strict extensions and natural extensions (1 page)

- State and prove the periodic-point projection theorem.
- State and prove emptiness of the full-backward-orbit inverse limit; prove the
  image-intersection statement separately.
- Interpret the result only for strict extensions of the frozen wheel shift.

### §4 Strong-bisimulation quotients (1.5 pages)

- State and prove forward-well-founded quotient acyclicity and derive the
  finite-DAG corollary.
- Give the infinite-ray counterexample immediately after the corollary.
- State and prove the level-injective-label proposition without a finiteness
  assumption.
- Derive the representative-exact next-prime state-decoder corollary.
- Separate strong bisimulation from one-way simulation, bounded-radius
  observational equivalence, and arbitrary graph homomorphism.

### §5 Exact-clock locality obstruction (0.75--1 page)

- State and prove the finite-image theorem.
- Identify countable alphabet and infinite memory as excluded from the
  theorem's scope, not as successful constructions.
- Distinguish mathematical escape from scope-compliant endogenous recovery.

### §6 The surviving class and research status (1 page)

- Give the minimum source-lock obligations for one infinite observational
  recoding.
- Explain representative compatibility/path lifting.
- Provide a plain-language status table separating excluded hypothesis
  classes from the undefined/not-testable branch.
- State that no numerical run is authorized and no candidate ID is assigned.

### §7 Conclusion and limitations (0.5 page)

- Rephrase the three obstruction results.
- Emphasize that they are not a universal no-go theorem.
- Name source-lock completion, not experiment execution, as the next step.
- Reaffirm that no determinant is defined and analytic comparison is outside
  scope.

### Appendix A: Proof-dependency and boundary audit

- Map each conclusion to the assumptions actually used.
- Record the infinite-ray counterexample in full.
- Record why finite-cutoff partition stability cannot substitute for an
  infinite consistency theorem.

### Appendix B: Source-lock readiness checklist

- Reproduce the minimum mathematical fields without filling them in.
- Mark every unresolved field as pending.
- Record project governance: no Stage-02 numerics, no new candidate identifier,
  and analytic comparison locked.

## Figure Plan

| ID | Type | Description | Source | Priority |
|---|---|---|---|---|
| Fig. 1 | Parallel theorem relationship map | The graded wheel system branches in parallel into three theorem-closed hypothesis classes and one dashed unresolved infinite-recoding project branch.  It is explicitly not a yes/no exhaustive tree. | Pure TikZ in `figures/obstruction_map.tex`; no data | High |

### Figure 1 caption draft

“The obstruction map is hypothesis-sensitive and parallel rather than
exhaustive.  Strict equivariant extensions, forward-well-founded
strong-bisimulation quotients, and finite-alphabet fixed-window decoders are
closed by distinct arguments.  The dashed infinite observational-recoding
branch is retained for further definition by this project; it is unresolved,
not validated.”

The diagram is the hero figure because a skim reader can recover both the
three results and their two essential scope boundaries before reading the
proofs.

## Citation Plan

No external citation will be included in this initial stage paper.  All
mathematical arguments are proved in full, and all project-status statements
are traceable to the frozen Stage-02 artifacts.  This avoids introducing
unverified bibliography entries.  A later literature-positioning revision
may add references only after metadata is checked against the shared local
corpus or a primary source.

## Anonymity and sharing checks

- Author block: `Anonymous Authors`.
- No personal names, affiliations, grant identifiers, or repository URLs.
- No claim of venue submission or acceptance.
- No external or private data.
- No generated empirical result.

## Phase checkpoints

- [x] Narrative report and claims--evidence matrix.
- [x] Structural plan and scope guardrails.
- [x] Pure TikZ theorem relationship figure.
- [x] Complete modular LaTeX manuscript.
- [x] Successful PDF compilation with reference and font checks.
- [x] Unified review/improvement Round 1.
- [ ] Unified review/improvement Round 2.

The initial paper contains no external citations, so the citation check is
vacuous and references.bib is intentionally empty.
