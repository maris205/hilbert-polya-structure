# Paper 7 Plan

**Working title:** Clock-Preserving Hénon Warps of an Exponential
Schrödinger Operator: Two Growing Riemann--von Mangoldt Terms and
Finite-Window Diagnostics

**One-sentence contribution:** We construct a zero-input self-adjoint family
in which area-preserving Hénon warps and fixed magnetic fields change the
classical geometry and antiunitary symmetry while preserving, analytically,
the two growing Riemann--von Mangoldt mean-counting terms.

**Paper type:** mathematical physics, theory plus reproducible numerical
experiments.

**Target format:** standard journal article; approximately 22--28 pages of
main text plus technical and reproducibility appendices.

**Date:** 2026-08-05.

## Problem anchor and scope

- **Bottom-line problem:** Find a genuine self-adjoint dynamical construction
  that satisfies several necessary Hilbert--Pólya requirements without
  fitting a finite list of zeta zeros.
- **Bottleneck addressed here:** Mean-count engineering is usually either
  dynamically inert or detached from symmetry control.  We ask whether the
  Riemann--von Mangoldt mean clock can be held fixed while nonlinear dynamics
  and time-reversal structure are activated independently.
- **Non-goals:** This paper does not derive a prime-power trace formula,
  identify individual zeta zeros, prove GUE universality, prove
  positive-measure chaos, or prove RH.
- **Success condition for Paper 7:** Q and W are theorems; the Hénon and
  magnetic deformations are shown to be nontrivial; the corresponding S and
  symmetry-statistics signals survive frozen controls and numerical audits;
  the missing P bridge is stated without concealment.

## Claims--evidence matrix

| ID | Claim | Evidence | Status | Main location |
|---|---|---|---|---|
| M1 | Every proper area-preserving configuration warp preserves the exact classical clock (E(2\pi)^{-1}\log(E/2\pi)-E(2\pi)^{-1}+1); a fixed magnetic field preserves it as well. | Exact configuration change of variables and momentum-fiber translation in `DERIVATION_PACKAGE.md` and `MAGNETIC_EXTENSION.md`. | **Theorem** | Sections 3--4 |
| M2 | For every fixed Hénon iterate and fixed constant field, the Friedrichs operator is self-adjoint with compact resolvent and its quantum count has the same two growing terms with an explicit (o(E)) remainder. | Dirichlet--Neumann bracketing, first-exit polynomial bounds, local magnetic gauge, and independent mathematical audit. | **Theorem** | Section 4; Appendices A--C |
| M3 | The Hénon warp is not a spectrally irrelevant relabelling: in radial coordinates it moves into a determinant-one variable kinetic metric; for centered (a\ne0,n=1,2), the magnetic core has no standard orientation-reversing Euclidean repair of time reversal. | Unitary coordinate identity and symmetry lemma. | **Proved identity / lemma** | Section 5; Appendix D |
| M4 | The legacy, prior-frozen (a=1.02) member has stable sampled chaotic diagnostics distinct from the radial control, and the signal persists at (B=1). | R000--R001 FTLE/SALI; R106 independent DOP853 replication; energy-drift and time-step/time-length checks. | **Sampled numerical support at four frozen states** | Section 6 |
| M5 | In the tested finite spectral window, (B=0) is GOE-like and fixed nonzero fields drive a stable response toward the unitary class without changing the proved mean clock. | R100--R105 grid sequence, fourth-grid and (h^2) extrapolation, ratio CDFs, gauge and (B\leftrightarrow-B) audits; R107A supplies a gauge-covariant fourth-order cross-stencil check with converged Ritz residuals. | **Converged finite-window numerical support** | Section 7 |
| M6 | The construction is an HP-motivated mean-count/symmetry testbed, not a prime/zero mechanism. | Q/W/S/R/C/P/Z ledger, zero/prime input audit, explicit P-gate death conditions. | **Scope statement** | Sections 1 and 8 |

The dominant paper claim is M1--M2: two independent deformations preserve the
same analytic clock.  M3--M5 show that these deformations are active rather
than decorative.  M6 prevents the supporting experiments from being promoted
into arithmetic claims.

## Structure and page budget

### Abstract (180--230 words)

- Start with the constructed operator, not generic RH background.
- State the exact classical count and the quantum (o(E)) theorem.
- Explain the two clock-preserving deformations: Hénon geometry and magnetic
  symmetry.
- Report the strongest frozen numbers: (a=1.02) adaptive FTLE/SALI at
  (B=0,1), and mean adjacent ratios (0.52983\to0.58727).
- End by naming the missing endogenous prime-power trace gate.

### 1. Introduction: preserving the clock while changing the mechanism

**Target:** 2.5--3 pages.

- Open with the Hilbert--Pólya distinction between a real self-adjoint
  spectral object, its mean clock, and the arithmetic fluctuation.
- Explain why a smooth count alone is weak evidence, using inverse spectral
  and (xp)/Morse precedents.
- Present the breadth-first framework in one paragraph: the already explored
  family is retrospectively organized as a Route-B survivor, while the paper
  prospectively illustrates how Route A closes Q/W and exposes P as the next
  bridge.  Do not present the post hoc protocol as selection history.
- Introduce
  
  \[
  \mathcal H_{a,n,B}=\frac12(-i\nabla-A_B)^2+
  2\pi e^{\pi|\widetilde H_a^n(q)|^2}.
  \]
- State the central invariant: Hénon warping preserves configuration sublevel
  area; magnetic coupling preserves momentum-fiber area.
- Give four falsifiable contribution bullets matching M1--M5.
- Include the Q/W/S/R/C/P/Z ledger early; R and C are side diagnostics.
- Explain that (a=1.02) is prior-frozen from an RH-motivated, zero-exposed
  lineage.  The current runs are zero-input, but the parameter provenance is
  not statistically blinded and was not selected by the present theorem.

**Key citations:** `Riemann1859`, `TitchmarshHeathBrown1986`,
`BerryKeating1999`, `Connes1999`, `Lagarias2009` [verified metadata to add],
`Wang2026PrimeChaos`, `Wang2026HenonPreprint`.

### 2. Closest work and novelty boundary

**Target:** 2.5--3 pages.

Organize by question rather than paper:

1. Hilbert--Pólya, (xp), Morse, inverse-potential, and quantum-graph models.
2. Global and magnetic Weyl laws for confining Schrödinger operators.
3. Area-preserving maps and Hénon quantization versus a Hénon-warped static
   scalar potential.
4. Quantum-chaos symmetry classes and orthogonal--unitary crossover.
5. Equimeasurable/isospectral deformations and why “same clock” is weaker
   than “same spectrum.”

End with a precise novelty paragraph: phase-volume invariance is elementary
and general; the contribution is the explicit Riemann clock family, the
fixed-iterate two-term quantum theorem including constant magnetic fields,
and the controlled realization of active Hénon/magnetic dynamics within that
family.

### 3. Centered Hénon warps and exact classical clock

**Target:** 3 pages.

- Define the area-preserving Hénon map, its positive fixed point, the centered
  conjugate, inverse, determinant, properness, and degree (D=2^n).
- Explain the roles of (a=0), (1.02), and (6).
- State and prove the general proper determinant-one warp theorem.
- Evaluate the radial integral exactly.
- State the magnetic extension and make clear that the momentum translation
  is a measure argument, not necessarily a global canonical transformation.
- Separate the classical (+1) from any claim about the quantum constant
  term.

### 4. Quantum two-term Weyl law with fixed magnetic field

**Target:** 4--5 pages plus appendices.

- Define the closed quadratic form and Friedrichs operator.
- Prove compact resolvent from confinement, local Rellich compactness, and
  tail control.
- State the main theorem with
  
  \[
  O_{a,n,B}\!\left(E^{3/4}(\log E)^{1+2^{n-1}}\right).
  \]
- Give the main proof skeleton:
  1. (E^{-1/4}) square bracketing;
  2. polynomial preimage/first-exit geometry;
  3. upper/lower Riemann-sum control;
  4. local gauge removal of (A_B(c_Q));
  5. aggregation of lattice and potential-oscillation errors.
- Keep full constants and the first-exit bootstrap in Appendices A--C.
- State explicitly that the remainder preserves two growing terms but is far
  too large for the (7/8) constant or (S(T))-scale oscillation.

### 5. Why the deformations are active

**Target:** 2--2.5 pages.

- Under (u=\Psi(q)), derive the determinant-one variable metric in the
  kinetic term; contrast classical equimeasurability with quantum
  isospectrality.
- Audit antiunitary symmetry:
  (\mathcal C\mathcal H_{B}\mathcal C=\mathcal H_{-B}).
- At (B=0), identify (T^2=+1); at fixed (B\ne0), distinguish bare
  conjugation from a possible reflected-conjugation symmetry.
- State the centered (n=1,2) no-orientation-reversing-Euclidean-symmetry
  lemma, with the exact boundary that arbitrary nonlocal antiunitaries are not
  excluded.
- Clarify that a scalar magnetic model is an orthogonal-to-unitary laboratory,
  not a (T^2=-1) symplectic/GSE construction.

### 6. Zero-input sampled classical dynamics

**Target:** 3 pages.

- Give the natural time scale, deterministic microcanonical Sobol seeding,
  velocity-Verlet variational map, FTLE and SALI definitions, and frozen joint
  decision rule.
- Present R000 and the failure-first high-distortion controls.
- Use R001 to distinguish radial finite-time shear from nonlinear plateaus.
- Present R106 as an independent DOP853 physical-velocity audit at (B=0,1).
- Report seed count, energy, integration times, tolerances, and maximum drift.
- Avoid “ergodic,” “mixing,” “positive-measure,” and global-chaos claims.

### 7. Quantum spectra and magnetic crossover

**Target:** 4 pages.

- Define the gauge-covariant Peierls finite-difference operator, domain
  truncation, deterministic Lanczos solve, edge discard, smooth-clock
  unfolding, and adjacent-gap ratio.
- Tell the failed (h=0.04\to0.03) story before the successful refinements.
- Present the (a=1.02) fourth grid and (h^2) extrapolation.
- Compare empirical ratio CDFs descriptively with GOE/GUE surmises; do not use
  i.i.d. p-values.
- Present the preregistered (B) grid as a crossover, not a fitted optimum.
- Explain radial angular-momentum doublets and retain (a=6) as a failed
  high-distortion spectral control.
- Include R105 residual, orthogonality, gauge-equivalence,
  (B\leftrightarrow-B), and deterministic-rerun checks.
- Present R107A as an independent-order, gauge-covariant cross-stencil check:
  median level changes are about (0.041\%), fourth-order/extrapolated
  ratio differences are below (0.005), and retained Ritz residuals are
  below (7\times10^{-10}).
- State the remaining boundary precisely: both stencils share the Cartesian
  box, Peierls links, point-sampled potential, and Lanczos eigensolver. A
  magnetic finite-element or sine-Galerkin family and a 600--1000-level
  window remain the decisive submission-grade extension.

### 8. Hilbert--Pólya gate ledger and missing arithmetic bridge

**Target:** 2.5--3 pages.

- Summarize \(Q\) and \(W\) as proved, \(S\) as sampled numerical support,
  \(R\) as a finite-window symmetry diagnostic, and \(C\) as relative-
  container admissibility; \(P\) remains open and \(Z\) is untested.
- Explain why GOE/GUE agreement cannot manufacture the explicit formula.
- State the endogenous target:
  periods (r\log p) and amplitudes of von-Mangoldt type.
- Develop the relative spectral-shift route only to the extent justified by
  the completed trace-class audit. The first-resolvent route is not
  established and is disfavored; powers (m\ge2), the canonically normalized
  signed staircase, the relative heat trace, and the distributional wave
  trace provide rigorous containers:
  
  \[
  \operatorname{Tr}(f(H_1)-f(H_0))
  =\int f'(E)\xi(E)\,dE.
  \]
- Give death conditions: no prime table, no zero fitting before P, no
  eigenvalue-dependent operator, no RMT-to-arithmetic inference.
- Re-emphasize that an HP-motivated mean-count/symmetry testbed is useful
  because it isolates the genuinely arithmetic obstruction.

### 9. Conclusion

**Target:** 1 page.

- Restate the clock-preserving deformation principle.
- Separate theorem, numerical evidence, and open bridge in three sentences.
- Give two concrete next steps: (i) genuinely independent finite-element or
  Galerkin/high-window quantum validation and broader classical phase-space
  census; (ii) R200 energy-localized relative-trace diagnostics followed by
  an endogenous prime-power carrier via a relative trace or symbolic cocycle.

### Appendices

- **A.** Polynomial geometry, properness, and first-exit bounds.
- **B.** Nonmagnetic Dirichlet--Neumann bracketing.
- **C.** Local magnetic gauge and covariant Neumann bracketing.
- **D.** Coordinate metric identity and centered reflection audit.
- **E.** Classical protocols, variational equations, and per-seed tables.
- **F.** Quantum discretization, gauge covariance, convergence, and audit.
- **G.** Breadth-first candidate protocol, promotion log, hardware, software,
  source hashes, and zero/prime access statement.

## Figure and table plan

| ID | Type | Content | Source | Priority |
|---|---|---|---|---|
| Fig. 1 | Hero schematic | Radial exponential clock (\to) area-preserving Hénon warp (\to) fixed magnetic field. Show the invariant areas with Q/W/S/R/C/P/Z status below. | Analytic/manual vector figure | High |
| Fig. 2 | Geometry | Equal-energy potential contours for (a=0), centered (a=1.02,n=1), and high-distortion (a=6,n=1), drawn at identical sublevel area. | `warped_henon.py` | High |
| Fig. 3 | Classical convergence | Median FTLE versus natural time with SALI at the same checkpoints for radial, (a=1.02,n=1,2), and (a=6); inset R106 (B=0,1) independent-solver comparison. | R001 CSV; R106 JSON | High |
| Fig. 4 | Quantum convergence | Mean ratio and median relative level change across grid refinements; visually retain the failed first comparison and the failed (a=6) extrapolation. Add the R107A fourth-order points or report them in Table 4. | R100--R102 and R107A NPZ/JSON; `QUANTUM_WINDOW_AUDIT.json` | High |
| Fig. 5 | Ratio distributions | Empirical adjacent-ratio CDFs for (a=1.02,B=0,1) against GOE/GUE surmises; include sample size and descriptive sup distances. | R102 NPZ | High |
| Fig. 6 | Magnetic response | Mean adjacent ratio versus the frozen (B=(0,0.25,0.5,1,2,4)) grid with GOE/GUE reference lines and convergence annotations. | R103--R104 JSON/NPZ | High |
| Fig. 7 | Smooth clock check | Quantum staircase transformed by the exact classical clock, plus local mean unfolded spacing for the core cells.  This is a mean-density diagnostic, not a zero comparison. | R102 spectra | Medium |
| Table 1 | Gate ledger | Q/W/S/R/C/P/Z status, evidence type, and excluded inference. | `CLAIM_LEDGER.md` | High |
| Table 2 | Prior-positioning matrix | Mean-count engineering, Hénon quantization, magnetic Weyl law, equimeasurable/isospectral work, and this construction. | Verified literature audit | High |
| Table 3 | Classical results | R001 time convergence and R106 adaptive magnetic audit. | Frozen result reports | High |
| Table 4 | Quantum results | Fourth-grid/extrapolated ratios, CDF distances, residuals, gauge checks, field scan, and R107A cross-stencil values. | R102--R107A | High |

**Hero-caption draft:** Area-preserving Hénon warping changes the potential
geometry while preserving every configuration-sublevel area, and a fixed
magnetic field changes the antiunitary symmetry while preserving every
momentum-fiber area.  Consequently both deformations retain the same two-term
Riemann--von Mangoldt mean clock.  The paper proves the Q/W statements and
tests S and the side diagnostic R without loading prime or zero arrays; C is
admissible, P remains open, and Z is not tested before P.

## Citation scaffold

All final BibTeX will be copied from verified publisher/DOI metadata or from
the already audited Paper 6 bibliography; no entry will be generated from
memory.

- **Riemann--von Mangoldt and statistics:** `Riemann1859`,
  `TitchmarshHeathBrown1986`, `Montgomery1973`, `Odlyzko1987`,
  `RudnickSarnak1996`, `KatzSarnak1999Zeros`, `KatzSarnak1999`,
  `KeatingSnaith2000`.
- **Hilbert--Pólya and engineered spectra:** `BerryKeating1999`,
  `Connes1999`, `Sierra2008`, `SierraTownsend2008`,
  `SierraRodriguezLaguna2011`, `EndresSteiner2010`,
  `Yakaboylu2024`, `WuSprung1993`, `KuipersHummelRichter2014`, plus
  verified Lagarias, Rahm, and Crehan entries.
- **Weyl and magnetic operator theory:** `Rozenblum1974`, `Tachizawa1992`,
  `HelfferRobert1982`, `LeinfelderSimader1981`,
  `BravermanMilatovicShubin2002`, `Kato1995`, `MazyaShubin2005`,
  `Ivrii2016`, plus verified Avron--Herbst--Simon, Tamura, Matsumoto, and
  Dimassi--Duong entries.
- **Hénon and quantization:** `Henon1969`, `Henon1976`,
  `DevaneyNitecki1979`, `FornaessWeickert2000`, `BerryQuantumMaps1979`
  [to verify/add], and the author's prior Hénon manuscript.
- **Quantum chaos and symmetry:** `Dyson1962`,
  `BohigasGiannoniSchmit1984`, `Berry1985`, `BerryTabor1977`,
  `Gutzwiller1971`, `Gutzwiller1990`, `Haake2010`,
  `PandeyMehta1983`, `BerryRobnik1986`, `SaitoEtAl2009`, and a verified
  adjacent-gap-ratio reference.
- **Equimeasurable/isospectral boundary:** verified Gordon--Schueth and
  Dhar--Rao--Shankar--Sridhar entries.
- **Author programme:** `Wang2026PrimeChaos` and
  `Wang2026HenonPreprint`; related Papers 3--6 will be cited only where
  their actual public/preprint status permits.

The target is 40--50 genuinely used references, with at least 30 in the final
manuscript.

## Review risks and minimum fixes

1. **“The mean clock is designed.”**  Agree explicitly; emphasize controlled
   deformation and the isolation of the P obstruction.
2. **“Any area-preserving warp works, so Hénon is decorative.”**  Prove the
   general theorem, then use radial, linear/equimeasurable, (a=1.02), and
   (a=6) controls to show what is and is not Hénon-specific.
3. **“Map chaos does not imply Hamiltonian chaos.”**  Use only the new
   Hamiltonian-flow FTLE/SALI results and state their finite-sample boundary.
4. **“GOE/GUE crossover is known.”**  Claim only its realization in this
   exact-clock family; cite the established crossover literature.
5. **“Finite differences may manufacture the effect.”**  Require the
   independent higher-order or finite-element audit and higher-window check
   before submission; until then label M5 finite-window evidence.
6. **“Same phase volume means isospectral.”**  Explicitly deny this and show
   the variable kinetic metric after coordinate change.
7. **“This is a Hilbert--Pólya candidate/solution.”**  Use “HP-motivated
   mean-count/symmetry testbed”
   and keep P open in the title, abstract, figures, and conclusion.

## Immediate execution order

1. Freeze the literature/newness audit and import verified entries.
2. Generate Figs. 1--7 and Tables 1--4 from frozen result files.
3. Draft Sections 3--5 and proof appendices before rhetorical front matter.
4. Draft Sections 6--7 from the protocol/result chain, retaining failed runs.
5. Write Sections 1--2 and Abstract last, once claim boundaries are stable.
6. Compile, inspect every page, run citation/data integrity checks, obtain an
   independent skeptical review, revise, and recompile.
