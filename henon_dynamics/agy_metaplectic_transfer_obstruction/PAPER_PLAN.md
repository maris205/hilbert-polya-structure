# C25 paper plan

## Material Passport

- Origin Skill: `paper-plan`
- Origin Mode: `claims-evidence planning`
- Origin Date: `2026-08-10T00:00:00Z`
- Verification Status: `VERIFIED`
- Version Label: `c25_paper_plan_v2`

**Final title:** *Rauzy path decoding and an infinite-fibre
noncompactness obstruction for an AGY induced transfer operator*
**One-sentence contribution:** For every AGY induced model covered by the
stated hypotheses, the unsmoothed oscillator twist is noncompact on the
vector-valued extension of AGY's published (C_b^1) realization; the
normalized (L^2) model is already noncompact at scalar level, while an
all-length Rauzy decoder rules out equal-matrix branch cancellation.
**Format:** self-contained mathematical research note
**Date:** 2026-08-10
**Main-text budget:** 16 pages, with proof and certificate details allowed in
an appendix.

## Claims--evidence matrix

| Claim | Evidence | Final status | Location |
|---|---|---|---|
| The project-chosen four-letter class contains a neat strongly-positive AGY-admissible section | Eight-complete `gamma_star=t^64(tbttbtbb)^8`, exact graph, matrix, positivity, no-border, and state-frame checks | Verified independently | Sections 2 and 6 |
| A fixed-start Rauzy path is uniquely determined by its chronological matrix | Winner-row dominance, exact row subtraction, strict entry-sum descent, induction | Proved; checker replay passed | Section 3 |
| The vector-valued AGY raw (C_b^1) branch sum is bounded and noncompact for (Re s>-sigma_0) | Absolute branch-norm sum plus bump/evaluation compression to a nonzero infinite-dimensional unitary | Proved; source and theorem audits passed | Section 4 |
| The normalized (L^2(mu)) transfer is contractive but noncompact, and is a coisometry on (s=it) | Bochner convergence, Jensen/disintegration, nonatomic scalar branch essential norm, twisted Koopman adjoint | Proved; scalar obstruction holds throughout (Re s>=0) | Section 5 |
| Ordinary Fredholm determinants fail on both tested spaces | Nuclear/trace-class operators are compact; exact branch compressions are noncompact | Proved consequence | Sections 4--5 |
| The result does not close holomorphic or generalized traces | Branch localizers need not exist there; no cross-space compactness inference is valid | Verified scope/nonclaim | Section 7 |

## Structure

### Abstract

- Open with the concrete negative theorem, not general Hilbert--Pólya history.
- Explain why scalar AGY quasicompactness does not survive an unsmoothed
  infinite-dimensional unitary fibre.
- State the two exact mechanisms: branch localization and path decoding.
- Include the quantitative facts `d=4`, eight complete blocks, length 128,
  and essential norm one on the unitary axis.
- End with the precise surviving holomorphic/generalized-trace boundary.

### 1. Introduction

- Motivate the need to test an actual published transfer space after C24's
  abstract obstruction.
- Distinguish scalar quasicompactness from compactness of a vector-valued
  extension.
- State three falsifiable contributions: all-length decoder, raw (C^1)
  obstruction, normalized (L^2) obstruction.
- Preview the negative Route-A decision and the exact escape hatch.

### 2. The source-locked AGY return model

- Define labeled Rauzy arrows, later-on-left cocycle, strong positivity,
  neatness, full inverse branches, roof, and inverse Jacobian.
- Present the deterministic four-letter section witness.
- State which ingredients are sourced from AGY and which are project
  deductions.
- Include a compact comparison table: scalar AGY (C^1), twisted (C^1_F),
  normalized (L^2_F), and untested holomorphic/an-isotropic spaces.

### 3. An all-length matrix decoder

- State the decoder for arbitrary alphabet size and a fixed start.
- Prove unique row dominance, exact peeling, strict descent, termination, and
  injectivity.
- Explain why the theorem preserves genuine chronology and eliminates the
  same-matrix/opposite-central-sign escape for return branches.
- Put finite stress tests in Section 6; do not use them as proof.

### 4. The raw vector-valued (C_b^1) obstruction

- Prove uniform branch distortion and absolute operator-norm summability.
- State the bump/evaluation compression theorem.
- Derive positive essential norm and nonnuclearity.
- Explain why discontinuous cylinder indicators are unnecessary on (C^1).

### 5. The normalized Hilbert companion

- Derive branch probabilities from the invariant density.
- Prove the (L^2) contraction and exact branch norm.
- Prove noncompactness throughout (Re sge0).
- Identify the twisted Koopman adjoint and essential norm one on (s=it).
- Record the absolute atomic threshold (Re sge d/2=2) and the independent
  noncancellation proof.

### 6. Exact certificate and independent checks

- Give the seven-state reconstruction and exact section matrix.
- Describe the producer/checker independence rule and Material Passports.
- Report decoder stress-test counts and all registered mutations.
- Separate exact symbolic facts from finite mutation coverage.

### 7. Route-A decision and conclusion

- Report `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
- State that the ordinary determinant fails on the two tested source-standard
  spaces; do not claim `I-zL` is never Fredholm.
- Leave holomorphic/no-localizer, flat/distributional, semifinite, and
  geometrically forced continuous smoothing as distinct candidates.
- Authorize a large system-space switch, not a longer periodic cutoff.

### Appendix

- Full source-numbering crosswalk.
- Complete decoder pseudocode and proof details.
- Essential-norm lemmas and density/disintegration calculations.
- Exact witness tokens and mutation table.

## Table and algorithm plan

| ID | Type | Purpose | Data source | Priority |
|---|---|---|---|---|
| Table 1 | Assumption/result comparison | Show exactly which scalar, (C^1_F), (L^2_F), and holomorphic claims pass or remain open | `SOURCE_AUDIT.md`, `THEOREM_PACKAGE.md` | High |
| Algorithm 1 | Rauzy matrix decoder | Make the all-length chronology recovery reproducible | theorem proof and producer | High |
| Table 2 | Exact source-lock certificate | Report state, word length, completeness, matrix determinant/positivity, and checker status | `results/c25_certificate.json` | High |

A decorative figure is unnecessary.  The comparison table and decoder
algorithm expose the two logical doors more clearly than a schematic image.

## Citation plan

- AGY published article and official preprint: source of the induced map,
  roof, Jacobian, bumps, and scalar transfer space.
- Aimino--Nicol--Todd: quasi-Hölder boundary only; no unconditional branch
  projector claim.
- Kerckhoff: classical simplicial-cylinder geometry behind the decoder; the
  row-subtraction result is presented as a self-contained algorithmic
  restatement, not a blanket novelty claim.
- Bonet--Gómez-Collado--Jornet--Wolf: prior art for compactness forcing
  compact point weights in a single operator-weighted composition map.
- Magee--Naud: arbitrary-Hilbert twisted norm estimates versus
  finite-dimensional trace-class/Fredholm theory.
- C24 repository note: local tensor-essential-norm and discrete-atom lemmas,
  cited as predecessor infrastructure rather than external authority.

Every bibliography record must come from the published source, arXiv
metadata, DOI, or the existing verified C24 bibliography.  No citation is to
be generated from memory.

## Final checks

- [x] Independent certificate passes: 11/11 gates.
- [x] Regression/mutation suite passes: 14/14 tests.
- [x] Independent theorem review reports CRITICAL=0 and MAJOR=0.
- [x] Every claim in the introduction maps to a theorem or certificate.
- [x] Source-derived and project-derived claims are labeled.
- [x] The decoder is positioned conservatively after a primary-source
  literature lock; no absence-of-search-result novelty claim is made.
- [x] No `TODO`, undefined reference, or uncited BibTeX entry remains.
- [x] LaTeX builds from a clean tree.
