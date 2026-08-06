# Route B Round 2 Idea Report

**Direction:** analytic Hilbert--Pólya deformations of the fixed
\(a=51/50\) Hénon programme  
**Date:** 2026-08-06  
**Pipeline:** literature/death-log audit → candidate generation → novelty
check → independent review → fatal pilots → focused refinement

## Problem anchor

Find a fixed, zero-input Hénon-based quantum construction that satisfies more
than a visually or numerically fitted subset of the Hilbert--Pólya
requirements.  Partial progress is acceptable, but each passed gate must be
analytic and each unpassed arithmetic gate must remain explicit.

## Scoring rule

Candidates are ranked by information gain, not spectacle:

1. the object and its Hilbert space are fixed before testing;
2. it advances a named Q/W/S/P/Z gate by an exact identity or theorem;
3. the Hénon dependence is not a trivial direct sum or unitary relabelling;
4. no zero or prime list is used before P;
5. a fatal test fits within two CPU hours;
6. known death-log counterexamples do not already apply.

## Ranked candidates

### 1. Relative heat-trace activation of the clock-preserving Hénon warp — RECOMMENDED

- **Fixed object:** the already defined pair
  \[
  \mathcal H_a=-\tfrac12\Delta+2\pi e^{\pi|\widetilde H_a(q)|^2},
  \qquad
  \mathcal H_0=-\tfrac12\Delta+2\pi e^{\pi|q|^2}
  \]
  on \(L^2(\mathbb R^2)\), at \(a=51/50\).
- **Gate target:** upgrade S from sampled activity to analytic spectral
  activity while retaining the proved Q and W results.
- **Core mechanism:** area preservation makes the classical heat integrals
  identical.  A partially resummed heat-kernel expansion contains a quantum
  gradient invariant.  For one centered Hénon iterate its angular average is
  explicitly nonzero.  A Brascamp--Lieb--Luttinger rearrangement argument also
  supplies a natural global sign relative to the radial equimeasurable
  potential.
- **Provisional analytic signal:** with
  \(L=\log(1/(2\pi t))\), the first-gradient calculation predicts
  \[
  \operatorname{Tr}(e^{-t\mathcal H_a})-
  \operatorname{Tr}(e^{-t\mathcal H_0})
  =-\frac{a^2}{24\pi}L^2+O(L)
  \]
  if the noncompact resummed remainder is uniform.
- **Fatal pilot R300:** independently derive the coefficient, evaluate the
  exact one-dimensional gradient integral over a logarithmic time grid, and
  audit whether all omitted heat invariants are \(o(L^2)\).
- **Kill condition:** cancellation of the coefficient; a same-order
  uncontrolled remainder; or an equality case showing the warp can be
  spectrally invisible.
- **Closest prior work:** classical rearrangement inequalities and general
  resummed heat expansions.  The proposed novelty is the explicit
  equimeasurable Hénon/RvM-clock application, not those general tools.
- **Current verdict:** highest information gain and smallest mechanism.

### 2. Transverse homoclinic certificate and local Hénon generalized primes — BACKUP

- **Fixed object:** the real polynomial automorphism
  \(H_{51/50}(x,y)=(1-(51/50)x^2-y,x)\), restricted only after a proved
  local hyperbolic invariant set is identified.
- **Gate target:** a clearly renamed generalized-prime gate \(P^*\), not P.
- **Core mechanism:** a transverse homoclinic point for the negative
  hyperbolic fixed point implies a horseshoe for an iterate.  Primitive cycles
  with unstable-Jacobian lengths \(\ell_\gamma\) give
  \[
  Z_H(s)=\prod_\gamma(1-e^{-s\ell_\gamma})^{-1},\qquad
  -\frac{Z_H'}{Z_H}(s)
  =\sum_{\gamma,r\ge1}\ell_\gamma e^{-sr\ell_\gamma}.
  \]
- **Fatal pilot R301:** reproduce a transverse symmetry-line crossing with
  adaptive manifold subdivision, calculate a nonzero crossing angle, and
  repeat with an independent parameterization.
- **Kill condition:** the crossing collapses under refinement, lies at the
  numerical tangency scale, or no compact local rectangle can isolate it.
- **Closest prior work:** Birkhoff--Smale horseshoes, Ruelle zeta functions,
  and general Hénon hyperbolicity.  Novelty can only be parameter-specific
  certification and its use as a module in this exact programme.
- **Boundary:** even success does not couple these cycles to the
  Schrödinger wave trace and does not produce rational primes.

### 3. Adelic periodic-point schemes for \(H_{51/50}\) — HIGH-RISK EXPLORATION

- **Fixed object:** the rational Hénon automorphism together with its good
  reductions outside the bad places of an explicitly chosen integral model.
- **Gate target:** an actual arithmetic carrier indexed by prime places, but
  neither Q nor P is obtained automatically.
- **Core mechanism:** study the finite fixed-point schemes
  \(\operatorname{Fix}(H^n)\) and local dynamical factors assembled from
  their reductions.
- **Fatal paper test:** determine the good-place set and whether the local
  fixed-point counts admit a cohomological normalization with a stable global
  Euler product.
- **Kill condition:** normalization is arbitrary, the product diverges with
  the wrong degree, or the construction merely restates a standard
  Hasse--Weil/dynamical zeta.
- **Closest prior work:** arithmetic Hénon heights, non-Archimedean Hénon
  horseshoes, and Roberts--Vivaldi finite-field cycles.
- **Boundary:** this route is arithmetic rather than prime-free and is not yet
  a self-adjoint Hilbert--Pólya operator.

### 4. Energy-localized relative wave trace for the Paper 7 pair — CONDITIONAL

- **Fixed object:** the same radial/Hénon Schrödinger pair and its canonical
  discrete relative counting shift.
- **Gate target:** the shortest conceivable bridge from the existing relative
  container C toward P.
- **Core mechanism:** prove an energy-localized relative trace formula whose
  singular support is generated by actual periodic trajectories of the
  continuous Hamiltonian flow.
- **Fatal paper test:** show that the relevant orbit-time family can remain at
  fixed nonzero times at high energy.
- **Kill condition:** the existing fixed-complexity periods shrink to zero
  without a structural growing-complexity family.
- **Verdict:** mathematically central but currently blocked; do not launch a
  large computation.

### 5. Hénon deformation of a scaling/zeta spectral triple — NOVELTY RISK

- **Fixed object:** a Connes-style scaling spectral triple with a proposed
  Hénon-induced automorphism or cocycle.
- **Gate target:** Q/W and possibly an arithmetic trace inherited from the
  backbone.
- **Fatal paper test:** prove that the Hénon action changes a spectral or
  K-homological invariant rather than being inner, unitary, or decoupled.
- **Kill condition:** the prime structure remains entirely in the original
  scaling triple and the Hénon factor is cosmetic.
- **Closest prior work:** Bost--Connes, endomotives, zeta-cycles, and recent
  zeta spectral triples.

### 6. Hénon subshift/Cuntz--Krieger spectral triple — PRIOR COLLISION

- **Fixed object:** a spectral triple for a proved subshift coding a local
  Hénon horseshoe.
- **Gate target:** Q and S on a noncommutative symbolic space.
- **Fatal paper test:** calculate its eigenvalue counting law and compare it
  analytically with W.
- **Kill condition:** the word-length/entropy dimension gives the standard
  exponential or power clock rather than \(T\log T\).
- **Verdict:** useful language, but not a new HP mechanism by itself.

### 7. Renormalized Hénon Markov quantum-graph tower — ENGINEERING RISK

- **Fixed object:** a tower of finite metric graphs derived from successive
  Hénon Markov refinements, with a single self-adjoint graph Laplacian/Dirac
  operator on the completed tower.
- **Gate target:** combine Q, W, and a graph periodic-orbit trace.
- **Fatal toy test:** prove compact resolvent and calculate the second counting
  term for a two-shift tower before using Hénon data.
- **Kill condition:** infinite zero multiplicity, an essential spectrum, or
  order-\(T\) log-periodic oscillations that destroy W.
- **Verdict:** bold but likely engineered; held behind R300/R301.

### 8. Koopman/Cayley suspension of the Hénon natural extension — KILLED

- **Fixed object:** the unitary Koopman operator of a Hénon-invariant measure
  and its Cayley transform or suspension generator.
- **Apparent benefit:** self-adjointness follows from unitarity.
- **Fatal defect:** mixing symbolic suspensions normally have continuous
  spectrum; compact resolvent and the RvM count are absent.
- **Verdict:** eliminated before pilot.

### 9. Transfer-operator Hermitization or de Branges pencil — KILLED

- **Fixed object:** block Hermitization of \(I-\mathcal L_s\), or a
  parameter-dependent canonical system built from a Ruelle determinant.
- **Apparent benefit:** formally self-adjoint matrices or real spectra.
- **Fatal defect:** Hermitization records singular values, not the zeros of
  the transfer determinant; a parameterized pencil is not one fixed HP
  operator.
- **Verdict:** eliminated by operator identity failure.

### 10. Growing-iterate direct-sum clock — KILLED

- **Fixed object:** a multiscale direct sum of Hénon iterates chosen so that
  aggregate multiplicities mimic \(T\log T\).
- **Apparent benefit:** Q/W can be manufactured.
- **Fatal defect:** the clock is inserted by block weights and the Hénon
  action is non-identifying; fixed-iterate W estimates do not justify an
  energy-dependent iterate.
- **Verdict:** eliminated as an engineered clock.

## Phase-2 selection

The selected order is:

1. **R300** — relative heat-trace activity;
2. **R301** — local transverse-homoclinic precheck if R300 remains viable;
3. keep the adelic route as a written high-risk branch, not a current compute
   job.

This ranking deliberately accepts a modest but real analytic advance through
S before attempting the much harder rational-prime P gate.

## Pilot status

| Pilot | Status | Result | Claim effect |
|---|---|---|---|
| R300 | `PARTIAL_PASS` | exact carrier and coefficient pass; uniform heat remainder open | exact analytic carrier; S theorem awaits proof review/remainder |
| R301 | queued | pending | at most supports local \(P^*\) |
| R302 | paper-only | not launched | none |
