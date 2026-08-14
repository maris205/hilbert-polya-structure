# Paper Plan

**Working title:** *Normalized Algebraic Periodic Actions versus Prime
Logarithms: A Hénon Design Certificate*  
**One-sentence contribution:** A periodic action obtained by regular
evaluation of a frozen algebraic exact potential on an algebraic orbit is
algebraic and therefore cannot equal a logarithm of a nontrivial algebraic
target; an exact gauge ledger, a sharp transcendental-normalization control,
and an algebraic Hénon specialization make the scope of this all-period
certificate explicit.  
**Format:** anonymous specialist mathematical-dynamics note, 11 pt,
author--year references  
**Type:** theorem plus source-locked exact static implementation audit  
**Date:** 2026-08-14  
**Target length:** 10--12 pages through the conclusion, followed by references
and two appendices  
**Section count:** eight main sections plus two appendices

The paper tells one narrow story.  Absolute periodic action depends on a
choice of exact potential and additive normalization.  Once that choice is
frozen over $\overline{\mathbb Q}$, algebraic evaluation puts the action on
the algebraic side of the Hermite--Lindemann boundary and excludes exact
$\log p$.  The result is a provenance filter for one proposed clock, not a
universal obstruction to symplectic or arithmetic dynamics.

## Claims--Evidence Matrix

| Claim | Evidence | Status | Planned location |
|---|---|---|---|
| C1. A finite, pole-free sum of a single-valued $\overline{\mathbb Q}$-rational potential over an algebraic period-$n$ orbit lies in $\overline{\mathbb Q}$. | `notes/PROOF_PACKAGE.md`, Theorem A and Step 1; exact dependency IDs in `results/proof_audit.json`. | Proved all periods | Sec. 3 |
| C2. Such an action cannot be any complex logarithm of a nontrivial algebraic number, hence cannot equal positive $\log p$; algebraic scales, averages, repetitions, real/imaginary parts, and modulus retain the exclusion. | Hermite--Lindemann implication in `notes/PROOF_PACKAGE.md`; beta-zero/one controls in `results/control_audit.json`; Baker citation as classical background. | Proved all periods | Sec. 3 |
| C3. A single-valued algebraic exact gauge changes a stepwise action by $\chi_n(P_n)-\chi_0(P_0)+\sum_j C_j$; endpoint compatibility deletes only the endpoint term. | Proposition C and Step 4 in `notes/PROOF_PACKAGE.md`; exact telescope and endpoint controls in `results/control_audit.json`. | Proved exactly | Sec. 4 |
| C4. The map alone cannot determine an arithmetic absolute action: an identity map with constant potential labelled $\log 2$ is a symbolic counterexample when transcendental normalization is allowed. | Frozen negative control in `results/control_audit.json`; source-lock stop rules. | Verified symbolic control | Sec. 4 |
| C5. For $H_a(q,p)=(q^2-a-p,q)$, $G=2q^3/3-pq$ satisfies $H_a^*\theta-\theta=dG$, while $L_a=q^3/3-aq-qQ$ equals $-G$ on the graph. | Theorem D and Step 5; zero residuals in `results/henon_static_audit.json`. | Proved/verified exact identities | Sec. 5 |
| C6. Every finite periodic point of algebraic $H_a$ is algebraic; for $a\in\mathcal O_{K_0,S_0}$ and an orbit field $K/K_0$, only $3\mathcal A_G\in\mathcal O_{K,S}$ is certified in general. | Projective no-infinity proof, cyclic valuation proof, and Corollary E; R021--R023 static ledgers; exact $-1/3$ sharpness control. | Proved all periods | Sec. 5, App. A |
| C7. The source-locked software faithfully implements the proof dependencies and scope gates without candidate parameter substitution, periodic-point solving, candidate action evaluation, prime tables, or zero data. | Seven official JSON records, 82-test JUnit, independent Round-3 deployment review, and final result manifest. | Verified static implementation audit | Sec. 6, App. B |
| C8. The correct route decision is to close only the frozen normalized algebraic action as an exact prime-logarithm clock; $\log|\mathcal A|$, multiplier/return-time clocks, multivalued or closed-nonexact primitives, transcendental normalization, and approximate targets remain outside the theorem. | Source-lock nonclaims, `EXPERIMENT_RESULTS.md`, `NOVELTY_AUDIT.md`. | Formal scoped decision | Secs. 7--8 |

## Evidence Boundaries

- The all-period conclusion is deductive.  Static JSON records validate
  formulas, proof contracts, and software ordering; they do not supply
  empirical evidence for the theorem.
- The candidate parameter is never substituted, no candidate periodic point
  is solved, and no candidate action is evaluated.
- `LOG_OF_TARGET_TWO` is a symbolic provenance label in a negative control,
  not a numeric logarithm or imported target datum.
- Algebraicity covers $\mathcal A$, $\operatorname{Re}\mathcal A$,
  $\operatorname{Im}\mathcal A$, and $|\mathcal A|$; it does not transfer to
  $\arg\mathcal A$ or $\log|\mathcal A|$.
- Exact single-valued algebraic gauges are not interchangeable with closed
  non-exact changes or multivalued gauges carrying monodromy.
- The Hénon refinement certifies $3\mathcal A_G$ as $S$-integral, not
  $\mathcal A_G$ at places above 3.
- The paper makes no historical-first claim.  The argument may be
  folklore-level; its value is the complete normalization-aware design
  certificate.

## Structure

### Abstract (180--220 words)

- State the conditional all-period certificate in the first sentence.
- Explain why additive normalization is the central validity gate.
- Name the exact Hénon specialization and denominator-three boundary.
- Report the concrete audit count: eight registered stages and 82 passing
  tests, with zero candidate orbit/action computations.
- End with the narrow route conclusion and strongest nonclaim.

### 1. Introduction (1.2--1.5 pages)

- Motivate $\log p$ as a proposed intrinsic periodic clock, not as imported
  zero data.
- Distinguish absolute action values from action differences and from other
  periodic observables.
- State the one-sentence contribution before the literature discussion.
- Give four falsifiable contributions matching C1--C7.
- Place Figure 1 immediately after the contribution list.
- State at once that the theorem does not concern $\log|\mathcal A|$,
  multiplier logs, return times, or arbitrary transcendental constants.

### 2. Exact symplectic action and arithmetic context (1.0--1.3 pages)

Organize by question rather than paper chronology:

1. periodic generating actions and variational symplectic maps;
2. exact potentials and additive normalization;
3. action/average-action spectra under iteration;
4. Hénon and quadratic symplectic maps;
5. transcendence and prime-logarithm motivation.

The section credits every classical ingredient and frames the paper-specific
delta as a source-locked provenance certificate.

### 3. Algebraic-action certificate (1.6--1.9 pages)

- Define the algebraic variety, rational map, orbit, primitive, potential,
  regularity conditions, and action.
- State and prove the finite-evaluation theorem.
- State the Hermite--Lindemann corollary, including beta zero and the unique
  algebraic beta-one exception.
- Prove the algebraic scale, average, repetition, real, imaginary, and modulus
  extensions.
- Use a boxed nonclaim to separate $|A|$ from $\log|A|$.

### 4. Gauge ledger and normalization counterexamples (1.3--1.6 pages)

- Derive the autonomous gauge formula and $nC$ shift.
- Derive the full time-dependent/stepwise endpoint formula.
- Separate value invariance ($C=0$) from algebraicity invariance
  ($C\in\overline{\mathbb Q}$).
- Present Figure 2 and the compatible/mismatch controls.
- Give the symbolic identity-map/transcendental-constant counterexample and
  list the precise stop conditions for poles, monodromy, and target injection.

### 5. Algebraic Hénon certificate (1.8--2.2 pages)

- Define $H_a$, its inverse, Jacobian, $\theta=p\,dq$, $G$, and $L_a$.
- Verify $H_a^*\theta-\theta=dG$ and $L_a=-G$ on the graph.
- Prove algebraicity of every finite periodic orbit using the cyclic
  recurrence and no-point-at-infinity argument.
- Prove the orbit-field $S$-integrality statement by a cyclic non-Archimedean
  maximum, tracking the factor 3 exactly.
- Present the $a=-1$, $(q,p)=(1,1)$ sharpness control with action $-1/3$.
- Place Figure 3 after the theorem/corollary pair.

### 6. Source-locked static implementation audit (1.1--1.4 pages)

- Explain the pre-execution source lock and independent deployment reviews.
- Give the controls-first registry order and exact pass matrix.
- State that R020--R023 are symbolic identity/proof-implementation audits,
  not candidate computations.
- Report 82 passing tests, exact manifest closure, software version, no GPU or
  target access, and the zero candidate counters.

### 7. Interpretation, route decision, and limitations (0.9--1.2 pages)

- State `GO_AS_NARROW_DESIGN_CERTIFICATE` and
  `MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED`.
- Close only the normalized algebraic absolute-action prime-log route.
- Discuss why normalization is both the obstruction's strength and its limit.
- List every surviving route and forbid universal no-go language.

### 8. Conclusion (0.4--0.6 pages)

- Rephrase the certificate as a provenance test rather than a new
  transcendence theorem.
- Retain the Hénon case and the sharp denominator-three boundary.
- Name one admissible next direction: a separately source-locked intrinsic
  nonalgebraic/multivalued clock with a complete branch ledger.

### Appendix A. Full Hénon geometry and valuation details

- Low-period multiplicity at $n=1,2$.
- Projective no-infinity/dimension argument.
- Orbit-field and extended-place bookkeeping.
- Denominator-three sharpness.

### Appendix B. Static-audit and reproducibility record

- Commands, versions, hashes, registry, and 82-test JUnit record.
- Figure generation commands and frozen JSON provenance.
- Forbidden-data and zero-execution declaration.

## Figure and Table Plan

| ID | Type | Description | Frozen data source | Priority |
|---|---|---|---|---|
| Figure 1 | Hero implication/boundary diagram | Left-to-right chain: regular algebraic orbit/potential $\to$ algebraic action $\to$ Hermite--Lindemann exclusion; lower band contrasts admitted algebraic normalizations with the symbolic transcendental target-injection control and lists surviving observables. | `source_lock_validation.json`, `proof_audit.json`, `control_audit.json`, `run_summary.json` | HIGH |
| Figure 2 | Gauge and scope matrix | Exact compatible, endpoint-mismatch, uniform-constant, pole, multivalued, beta-zero/one, and $\log|A|$ controls, with the full telescope formula and categorical outcomes. | `control_audit.json` | HIGH |
| Figure 3 | Hénon static certificate matrix | Exact residual zeros, determinant one, periods 1/2 multiplicity, no-infinity records, $3A$ denominator ledger, and the formal route boundary. | `henon_static_audit.json`, `run_summary.json`, `command_environment_manifest.json` | HIGH |
| Table 1 | Literature/claim-boundary comparison | Generating action, normalization, action spectra, Hénon background, transcendence, and the present arithmetic provenance question. | verified bibliography and `notes/CITATION_VERIFICATION.md` | HIGH |
| Table 2 | Official static registry | R000 through R023, proof versus implementation role, and pass state. | `run_summary.json` and official JSON artifacts | MEDIUM |

**Figure 1 draft caption.** The theorem is a conditional provenance chain,
not a universal no-go statement.  Regular evaluation of frozen algebraic
data gives an algebraic action; Hermite--Lindemann then excludes every
nontrivial algebraic logarithmic target.  Algebraic gauge/constant changes
remain inside the certificate, while a transcendental constant can inject a
target and therefore lies outside it.  Multiplier, return-time, multivalued,
and logarithmic-modulus clocks remain open.

## Citation Plan

- **Introduction / prime-log motivation:** Berry--Keating (1999), used only
  for the hypothetical periodic-orbit period scale.
- **Periodic generating action:** Kook--Meiss (1989),
  MacKay--Meiss--Percival (1984), Meiss (1992), Bialy--Tsodikovich (2023).
- **Exact potentials and normalization:** Delshams--Ramírez-Ros (1997).
- **Action and average-action spectra:** Ginzburg--Gürel (2009),
  Mazzucchelli (2013).
- **Hénon/quadratic symplectic context:** Friedland--Milnor (1989), Moser
  (1994), the collective-author open-problem survey by Julia Xénelkis de
  Hénon (2024), and Kim--Krieger--Postolache--Szeto (2024 preprint).
- **Transcendence:** Baker (2022) as an authoritative book source; the paper
  states Hermite--Lindemann as classical and proves only its elementary
  corollary in the present setup.
- No citation is used to assert the paper-specific combined certificate or a
  priority claim.  DOI/arXiv metadata and safe-use boundaries are recorded in
  `notes/PAPER_CITATION_AUDIT.md`.

## Author Plan Self-Review

- **Logical flow:** one dependency chain, followed by the normalization
  boundary, exact Hénon instantiation, and implementation audit.
- **Claim/evidence alignment:** every mathematical claim maps to the proof
  package; every software statement maps to frozen JSON/JUnit/manifest data.
- **Missing experiments:** none within scope.  Candidate orbit/action
  computation is forbidden and cannot strengthen the all-period theorem.
- **Positioning:** every ingredient is credited as classical or elementary;
  novelty is claimed only for the complete design-certificate packaging.
- **Length feasibility:** full Hénon geometry and reproducibility details can
  move to appendices without weakening the main proof.
- **Front matter:** title, abstract plan, contribution bullets, and Figure 1
  all expose both the theorem and its central limitation before Section 3.
- **Independent review:** deliberately deferred; this deliverable stops at a
  compiled, integrity-checked pre-review snapshot.

## Production Checklist

- [x] Generate three reproducible PDF/SVG vector figures and PNG review copies.
- [x] Write a verified, cited-only bibliography.
- [x] Draft the complete anonymous LaTeX manuscript.
- [x] Compile without undefined references/citations or material box warnings.
- [x] Create `CLAIM_MANIFEST.json`, `EXPERIMENT_PASSPORT.json`,
  `FIGURE_PACKAGE.json`, `PAPER_CONFIGURATION.md`, `PIPELINE_STATE.json`, and
  `INTEGRITY_PRE_REVIEW.md`.
- [x] Freeze `paper_pre_review.pdf` and report pages/hash/path.
