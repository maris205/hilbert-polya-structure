# Paper 02 plan

**Working title:** A Local Relative Gutzwiller Trace and a Certified Fast
Branch for a Clock-Preserving Hénon Schrödinger Pair

**One-sentence contribution:** For an explicit Hénon-warped exponential
Schrödinger pair, we prove an eigenvalue-only one-orbit relative trace for
each sufficiently small fixed energy excess and, as a separate quantitative
result, certify the orbit's connected local branch and a uniform transverse
determinant gap on an explicit interval, and exclude every other reduced root
from one declared local box over that interval.

**Paper type:** mathematical physics; analysis plus computer-assisted proof.  
**Author:** Liang Wang, School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology, Wuhan 430074, P. R. China.  
**Target format:** full journal article, approximately 28--34 pages of main
text plus proof and reproducibility appendices.  
**Date:** 2026-08-09.

The paper tells one technical story: a clock-preserving operator family from
Paper 01 has a model-specific, eigenvalue-only local wave-trace term that can
be isolated analytically near the bottom, while its distinguished fast orbit
can be certified quantitatively on a nontrivial interval.  The analytic
trace theorem has a positive but presently nonquantitative energy threshold;
the explicit branch certificate does not promote that threshold.  The paper
does not turn the local term into an arithmetic prime trace.

## Claims--evidence matrix

| ID | Claim | Evidence | Planned status | Main section |
|---|---|---|---|---|
| C1 | The energy-localized relative propagator trace is an ordinary finite-rank spectral object and is determined by the two eigenvalue lists. | Exact cutoff/staircase identities and the fixed-energy semiclassical trace framework in the theorem package. | Identity / standard-theorem specialization | Sections 3 and 7 |
| C2 | At (a=1.02), the Hénon well has an explicitly split bottom normal form and a fast Lyapunov branch whose limiting period, action slope, determinant, and first nonlinear period coefficient are computable. | Exact singular-value normal form, Lyapunov-centre hypotheses, audited Poincaré--Lindstedt derivation, R400 controls. | Propositions plus reproducible numerical evaluation | Section 4 |
| C3 | For every sufficiently small fixed energy excess, a radial-free positive-time window isolates one primitive fast warped return and yields its explicit coefficient in an eigenvalue-only relative trace. | A4.8 whole-shell blow-up/Poincaré argument, A4.9 finite-time CRR hypothesis audit, and A4.10 phase calculation. | Analytic theorem for (0<\delta<\delta_{\rm tr}) with (\delta_{\rm tr}>0) nonquantitative | Section 5 |
| C4 | One primitive fast branch is real analytic and locally unique in explicitly displayed boxes for (0\leq\epsilon\leq0.101), where (\delta=\epsilon^2). | A4.12 / `R401-VAL-L1-V2`: 202 CAPD/MPFR jobs, 202 exact-rational Krawczyk replays, 3973 aggregate checks. | Computer-assisted theorem local to the frozen boxes; no complement exclusion | Section 6 |
| C5 | On that certified local branch, (\det(I-D\Pi_\epsilon)>3) uniformly. | A4.13 / `R401-VAL-L1-MG-V2`: invariant quotient identity, positive event slope, 202 determinant and 202 phase-slope replays, 8302 checks. | Analytic identity plus validated local-branch theorem; no promotion of (\delta_{\rm tr}) | Section 6 |
| C6 | At (\delta=0.01), the frozen eigenvalue-only statistic is numerically consistent with the A4.10 coefficient, with finest normalized value (1.0065230645+0.0133004473i). | `R401-SC`: preregistered eight-point (\hbar) ladder, integrity gates, and independent recomputation. | Numerical diagnostic; not evidence that (0.01<\delta_{\rm tr}) | Section 7 |
| C7 | The representative complement-tree implementation excludes three selected local complements at both precisions. | Accepted `R401-VAL-L2-S0`: 6/6 trees, 3,016 nodes, 89,962 independent exact-decimal checks, sealed postcheck/provenance. | Historical `PASS_IMPLEMENTATION_SMOKE`; superseded in coverage, not invalidated, by C8 | Reproducibility appendix |
| C8 | For every frozen slab and parameter value, the A4.12 root is the only reduced root in the declared local box. | Accepted `R401-VAL-L2-A1`: 102/102 trees, 52,790 nodes, 158,782 independent checks, sealed 19-role release. | `PASS_LOCAL_COMPLEMENT_ALL_SLABS`; local \(P_+=0\) reduced chart only | Sections 6 and 8; reproducibility appendix |
| C9 | None of C1--C8 supplies prime times, von-Mangoldt weights, a zeta-zero spectrum, or RH. | Explicit Q/W/(S_{\rm op})/(P^*_{\rm loc})/(P_0)/Z/RH ledger. | Scope theorem / non-implication statement | Introduction and Section 8 |

`R401-VAL-L2-S0` passed without weakening its frozen gates and remains the
representative implementation certificate.  The later `R401-VAL-L2-A1`
production closes the same complement problem on all 51 slabs at both
precisions.  C8 enters the local theorem chain only when combined with the
accepted A4.12 protected-box existence-and-uniqueness result.

## Front matter

### Abstract

Target: 190--230 words.

1. State the analytic one-orbit relative trace and the separate quantitative
   local-branch certificate in the first sentence.
2. Explain the difficulty: fixed-energy trace formulas are standard, but
   their use requires a complete, nondegenerate model-specific return audit.
3. Describe the analytic normal form, radial-free time window, and
   CAPD/MPFR branch certification.
4. Give the quantitative branch and local-complement results:
   (0\leq\epsilon\leq0.101), 202 validated jobs across two precisions, and
   (\det(I-D\Pi)>3), followed by the A4.15 total of 102 closed trees, 52,790
   nodes, and 158,782 zero-failure checks.  Do not assign this whole interval
   to the analytic trace theorem.
5. End with the exact boundary: (\delta_{\rm tr}>0) is not yet quantitative,
   the (\delta=0.01) spectral computation is a diagnostic, and an endogenous
   rational-prime trace remains open.

The abstract must not lead with RH background, call the term a prime trace,
or imply that local uniqueness has already become global uniqueness.

### Figure 1: the proof architecture

Use a vector flow diagram with a three-block analytic spine and a separate
quantitative sidecar:

1. the two eigenvalue lists and energy-localized relative trace;
2. bottom normal form plus whole-shell isolation for
   (0<\delta<\delta_{\rm tr}), with (\delta_{\rm tr}>0) nonquantitative;
3. the licensed one-orbit coefficient for the eigenvalue-only relative trace;
4. below blocks 2--3, the certified local branch and determinant gap for
   (0\leq\epsilon\leq0.101), followed separately by the R401-SC diagnostic.

Place the open phase/flow-box/global-cover gates between block 4 and any
claim of an explicit trace-theorem interval.  In particular, draw no closed
arrow that licenses the coefficient at (\delta=0.01).  Place the separate
(P_0) arithmetic gate below block 3.  Use different line styles for analytic
proof, computer-assisted proof, numerical diagnostic, and open arrows.  The
caption must state that the figure compares the closed nonquantitative local
spectral route with the quantitative local-branch sidecar and the still-open
global and arithmetic routes; it is not merely a workflow illustration.

## Main-text structure

### 1. Introduction — 3 pages

- Open with the distinction between an explicit self-adjoint spectrum, its
  mean counting law, and a nonzero-time periodic-orbit fluctuation.
- State why the local step is hard: one must exclude competing returns,
  control nondegeneracy, and remove dependence on eigenfunction observables.
- Introduce the pair
  
  \[
  P_{a,\hbar}=-\frac{\hbar^2}{2}\Delta+
  2\pi\exp\!\left(\pi|\Psi_a(q)|^2\right),
  \]
  
  together with its radial reference.
- State the one-sentence contribution before the end of page 1.
- Give six falsifiable theorem/certificate bullets corresponding to C1--C5
  and C8, then label C6 as a numerical diagnostic and C7 as the predecessor
  implementation smoke.
- Preview the strongest certified numbers and the exact local-box boundary;
  do not present (\delta=0.01) as lying in the trace-theorem domain.
- Show Figure 1 and the gate ledger early.

Key positioning citations, verified in the Route A4 audit or the existing
Paper 01 bibliography: Duistermaat--Guillemin (1975), Brummelhuis--Uribe
(1991), Combescure--Ralston--Robert (1999), Paul--Uribe (1995), and Wang
(2026).  Import the underlying audited records before drafting.

### 2. Related work and novelty boundary — 3 pages

Organize by question rather than paper:

1. wave traces, clean flows, and fixed-energy Schrödinger trace formulas;
2. Lyapunov families and nonlinear normal modes;
3. relative spectral-shift containers versus energy-localized finite-rank
   differences;
4. computer-assisted periodic-orbit continuation and uniqueness;
5. Hilbert--Pólya models and why a local orbit term is not an arithmetic
   explicit formula.

The novelty paragraph must say that fixed-energy trace formulas and Lyapunov
centre theory are prior tools.  The model-specific contribution is their
combination with the explicit equimeasurable Hénon pair, an analytic time
window, and a two-precision auditable branch/determinant certificate.  Avoid
an absolute priority claim; retain the scoped literature-search wording.

### 3. Model and exact relative spectral object — 3.5 pages

- Define the centered Hénon automorphism, its inverse, the radial reference,
  the two Hamiltonians, and the regular compact energy surfaces.
- Derive the common exact shell volume and explain why it cancels only the
  mean classical clock, not the spectra.
- Define the finite-rank energy cutoff and relative propagator trace.
- Prove the staircase identity and fix the Fourier convention.
- Explain how support away from (t=0) removes zero-time distributions.
- State the fixed-energy trace theorem being specialized and list every
  hypothesis that the later sections must discharge.

Keep the exact functional-calculus identities in the main text.  Put routine
compactness details in Appendix A.

### 4. Bottom normal form and the fast Lyapunov oracle — 4 pages

- Compute the exact Hessian from (D\Psi_a(0)^T D\Psi_a(0)).
- Derive singular values, normal frequencies, and limiting periods.
- Verify the fast-pair nonresonance required by the Lyapunov centre theorem.
- Derive the limiting transverse multipliers and determinant.
- Present the Poincaré--Lindstedt coefficient with enough proof intuition to
  show where the cubic/quartic tensors enter; move tensor expansions to
  Appendix B.
- At (a=1.02), report
  (T_+^0=0.6638439766792985) and
  (D_+^0=3.8627220445155035), with directed numerical provenance.
- Use R400 only as a consistency check, not as proof of continuation.

### 5. Analytic one-orbit theorem at nonquantitative small energy — 5 pages

- State the target time window ([0.60,0.75]).
- Prove the radial reference has no return in the window for sufficiently
  small energy, and state the separate quantitative A4.11a bound.
- Prove the warped short-period floor A4.11b, while saying explicitly that a
  period floor does not exclude additional returns in ([0.60,0.75]).
- Give a main-text proof sketch of A4.8: complete-shell blow-up, classification
  of limiting returns, Poincaré-map uniqueness, iterate exclusion, and
  globalization.  Put the full proof in Appendix D.
- State and justify the finite-time CRR corollary used by A4.9, map every
  trace-formula hypothesis to a proved result, and make the fixed-energy
  quantifier order explicit: first fix (0<\delta<\delta_{\rm tr}), then let
  (\hbar\downarrow0).
- Prove the A4.10 phase and normalization by the exact harmonic trace and
  nondegenerate continuation; relegate the full convention audit to
  Appendix A.
- State precisely where compactness/continuity supplies the unspecified
  positive threshold (\delta_{\rm tr}) and why A4.11a--A4.13 do not yet
  prove (\delta_{\rm tr}\geq0.010201).
- Give the positive-time complex Gutzwiller coefficient in the frozen Fourier
  convention, including primitive period, action, Maslov phase, and
  determinant.

### 6. Quantitative local branch and stability theorem — 5 pages

- Define the reduced return equations, omitted coordinate recovery, section,
  and energy scaling (epsilon).
- Explain the analytic anchor at (epsilon=0).
- State the interval Krawczyk theorem used for each primary slab and guarded
  bridge.
- Describe the 51 primary slabs plus 50 bridges and the two independent
  precision levels.
- Prove connectedness, local uniqueness, full-state return recovery, and
  primitivity within the certified boxes.
- Derive the invariant flag
  
  \[
  0\subset\operatorname{span}(X_K)\subset\ker(dK)\subset T_z\mathbb R^4
  \]
  
  and the quotient identity
  
  \[
  \chi_M(t)=(t-1)^2\chi_{D\Pi}(t),\qquad
  \det(I-D\Pi)=4-\operatorname{tr}M.
  \]
- State the uniform lower bound (>3), including the directed endpoints and
  the fact that no semisimplicity assumption is used.
- Separate theorem statements from implementation tables.
- End the section with a formal non-promotion clause: A4.15 closes the local
  reduced-box complement, while the phase/flow-box and global covers and an
  independent event-projected determinant check remain open.  Thus this
  section does not license A4.9 at (\delta=0.01).

### 7. Spectral coefficient and frozen numerical diagnostic — 3 pages

- Derive the coefficient in the analytic A4.9 domain from the one-orbit
  theorem; do not substitute the explicit-interval certificate as though it
  quantified that domain.
- Explain that the left-hand spectral statistic is determined by the two
  eigenvalue lists, whereas the asymptotic right-hand coefficient contains
  classical orbit data.
- Present the eight-point (hbar) ladder at (delta=0.01) and the finest
  normalized value (1.0065230645+0.0133004473i).
- Distinguish asymptotic consistency from fixed-(hbar) accuracy.
- Include deterministic rerun, phase-convention, and independent
  recomputation gates.
- State in the figure caption and closing paragraph that R401-SC is an
  A4.9-guided diagnostic, not a theorem-domain validation at (\delta=0.01).

### 8. What has and has not been built — 2 pages

- Present the gate status:
  (Q,W,S_{\rm op},P^*_{\rm loc}) closed at their stated analytic levels,
  with (P^*_{\rm loc,num}) passed only as a diagnostic at (\delta=0.01);
  (P_0), Z, and RH open or unauthorized.
- Explain why an isolated Gutzwiller orbit does not supply periods
  (r\log p), von-Mangoldt amplitudes, an Euler product, or zeta zeros.
- Record the accepted all-slab reduced-root complement, then list the
  remaining analytic work: local phase/flow-box cover, global shell cover,
  independent event-projected determinant, and a quantitative
  (delta_{\rm tr}).
- Present the complement-tree engine as a completed local certificate, not as
  evidence for a phase or global theorem.

### 9. Conclusion — 1 page

- Restate the local spectral contribution without repeating the abstract.
- Separate analytic theorem, computer-assisted theorem, and implementation
  smoke in three sentences.
- Name two concrete next steps: close the full local/global return cover, then
  search for an endogenous arithmetic carrier without zero fitting.

The section allocations sum to 29.5 pages
(3+3+3.5+4+5+5+3+2+1).  These budgets include Figures 1--5 and Tables 1--3;
the proof and reproducibility appendices are separate.  To remain below 34
main-text pages, move full certificate matrices and long directed endpoint
tables to Appendices E--G, but retain the A4.8 and invariant-quotient proof
sketches in the main text.

## Appendices

- **A.** Regularity, compactness, finite-rank functional calculus, and
  Fourier conventions.
- **B.** Normal-coordinate tensors and the audited nonlinear-period
  derivation.
- **C.** Radial period and warped short-time estimates.
- **D.** Full-shell blow-up and removal of the microlocal observable.
- **E.** CAPD equations, interval-Newton/Krawczyk lemmas, and exact-decimal
  proof objects.
- **F.** Invariant-quotient monodromy proof, including possible Jordan cases.
- **G.** Frozen protocols, failed/superseded attempts, dependency hashes, and
  complete reproduction commands.
- **H.** L2 complement evidence: representative A4.14 smoke followed by the
  independently accepted A4.15 all-slab production.

## Figure and table plan

| ID | Type | Content | Data source | Priority |
|---|---|---|---|---|
| Fig. 1 | Proof architecture | Nonquantitative analytic trace spine, quantitative local-branch/complement sidecar, and open phase/global/arithmetic gates | Manual vector source | High |
| Fig. 2 | Geometry/phase portrait | Radial family, fast Hénon orbit, section, and the radial-free time window | R400 orbit data plus analytic annotations | High |
| Fig. 3 | Branch enclosure | Period and selected state coordinates across 51 slabs; show 128/256 outward enclosures without implying statistical error bars | L1 `summary.json` | High |
| Fig. 4 | Stability bounds | Directed lower/upper envelopes for (4-\operatorname{tr}M), with the line (D=3) | MG-V2 `summary.json` | High |
| Fig. 5 | Semiclassical diagnostic | Real/imaginary normalized coefficient across the frozen (hbar) ladder; label (\delta=0.01) as outside the presently quantified theorem domain | R401 fixed-energy result | Medium |
| Fig. 6 | Complement tree | Representative shell/tree structure and all-slab terminal-exclusion mix | L2-S0 and L2-A1 results | Appendix |
| Table 1 | Theorem hypotheses | Standard fixed-energy trace assumption, model-specific discharge, evidence location, and authorized energy domain | Theorem package | High |
| Table 2 | Certificate matrix | 51 slabs, 50 bridges, two precisions, checks and minimum margins | L1 release/checker | High |
| Table 3 | Claim boundary | Proved, certified, smoke-only, and open statements | Global claim ledger | High |

All plots should be vector PDF, colorblind safe, and interpretable in
grayscale.  Enclosure widths are deterministic validated bounds, not
confidence intervals.

## Citation scaffold

Only verified metadata already present in the route literature audit or an
existing audited bibliography may enter the manuscript.

- **Sections 1--3:** Duistermaat--Guillemin (1975), Brummelhuis--Uribe
  (1991), Paul--Uribe (1995), Combescure--Ralston--Robert (1999).
- **Section 2 clean/symmetric flows:** Guillemin--Uribe (1989), Cassanas
  (2007).
- **Section 4:** Weinstein (1973), Alligood--Yorke (1986).
- **Relative spectral context:** Yafaev (2005), Frank--Pushnitski (2019).
- **High-energy contrast only:** Pushnitski--Sorrell (2006),
  Doll--Gannot--Wunsch (2018), Doll--Zelditch (2020).
- **Computer-assisted proof:** Krawczyk (1969), Zgliczyński (2002),
  Kapela--Mrozek--Wilczak--Zgliczyński (2021),
  Kapela--Wilczak--Zgliczyński (2022), and Wilczak--Barrio (2017), as
  bounded by `../research/CAP_LITERATURE_AUDIT.md`.
- **Programme provenance:** Wang (2026), and the named Hénon preprint with
  author/affiliation recorded in Paper 01.

The independently quality-reviewed computer-assisted-proof audit now covers
interval Newton/Krawczyk methods, validated ODE integration/CAPD, rigorous
Poincaré maps, and parameterized periodic-orbit continuation.  It establishes
prior-method and claim boundaries, not the validity of this project's proof
archive.  Import the exact audited records for Wang (2026) and the named
Hénon preprint from Paper 01 rather than citing this outline as metadata.

Before LaTeX drafting, copy the audited BibTeX records or verify each record
against its DOI landing page.  Do not synthesize citation metadata from this
outline.

## Release checklist before drafting

- [x] Import the complete Paper 02 source/results package into this directory.
- [x] Require `R401-VAL-L2-S0` producer, independent checker, postcheck, and
      release provenance to agree before including C7/Fig. 6/Appendix H.
- [x] Require `R401-VAL-L2-A1` producer, independent checker, postcheck, and
      19-role release provenance to agree before promoting C8.
- [x] Freeze a manuscript-level claim ledger separating local theorem,
      representative smoke, and open global cover.
- [ ] Generate Figures 1--5 from archived sources and proof objects.
- [ ] Assemble a verified `references.bib` from the literature audit.
- [x] Extend the literature audit with primary computer-assisted-proof
      sources before writing the certification novelty paragraph.
- [x] Obtain an independent structural review of this outline and record the
      minimum fixes; no unavailable external-model score was invented.
- [x] Draft section by section only after the imported hashes replay.

## Independent outline review

**Disposition (2026-08-06):** coherent after minimum boundary corrections;
no numerical score was assigned.  The viable single story is the analytic
near-bottom one-orbit trace, strengthened by a separate quantitative
certificate for its distinguished local branch.

The 2026-08-06 review corrected the only material claim--evidence mismatch
present at that time: A4.9 has a
positive but nonquantitative (\delta_{\rm tr}), whereas A4.12--A4.13 certify
only the selected branch on (\delta=\epsilon^2\leq0.010201).  R401-SC at
(\delta=0.01) and the then-available L2 complement trees were therefore
diagnostic/smoke layers, not theorem-domain promotion.  The subsequent A4.15
production promotes the reduced-box complement alone to an all-slab local
computer-assisted theorem; it does not quantify the A4.9 trace domain.  The
hero figure, claims matrix, and Sections 5--8 preserve this separation.

The proof architecture is adequate provided the manuscript includes the
main-text A4.8 and invariant-quotient proof sketches, a justified finite-time
CRR corollary, and the harmonic phase/normalization argument, with full
details in Appendices A and D--F.  The 29.5-page main-text budget is feasible
only if detailed certificate tables stay in the appendices.  At review time,
the citation scaffold lacked a verified computer-assisted-proof corpus; the
subsequent quality-reviewed CAP audit closes that gap.  Exact imported
metadata for the programme-provenance references remains required.
