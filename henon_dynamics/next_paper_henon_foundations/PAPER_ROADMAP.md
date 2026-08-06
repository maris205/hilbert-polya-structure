# Paper roadmap

> Priority note (2026-08-05): this is a candidate-specific plan, not a fixed
> N+2 schedule. Promotion is governed by
> `../next_paper_henon_candidate_search/SEARCH_PROTOCOL.md`.

Priority status: **candidate lane**. This roadmap may proceed only after the
expanded G0 novelty audit and breadth-first promotion gates pass.

## Working title

**Which Spectrum Belongs to the Area-Preserving Hénon Map? A Weyl-Law
Obstruction for Quartic Surrogates and a Local Trace Formula for a Specified
Natural Quantization on a Certified Survivor**

## Intended paper type

A rigorous mathematical-physics foundations paper with a reproducible
computer-assisted component. The contribution is an obstruction plus a
replacement mechanism. It is not an empirical Riemann-zero modeling paper.

## Abstract-level story

1. Start from exactly the recurrence used in Paper 5.
2. Show that its continuum quartic surrogate has the wrong asymptotic spectral
   counting law.
3. Recall and rederive, in the current convention, the natural exact quantum
   Hénon map already known in the literature.
4. Localize it to the certified four-state \(H_6\) survivor.
5. Prove and numerically certify a periodic-orbit trace formula.
6. Identify the prior instability roof as the trace amplitude and the exact
   generating-function action as the trace phase.
7. Close with a precise Route-A result and a precise Hilbert--Pólya
   obstruction.

## Main claims in publication order

### Claim A: the legacy quartic spectrum has the wrong Weyl law

This is a theorem, not an empirical fit. It immediately explains why a
finite-range visual agreement cannot establish the required global mean
density.

### Claim B: one specified natural quantum object is a unitary Floquet map

This construction is credited to prior work. The paper's role is to state one
operator with exact signs, action gauge, subprincipal/global phase, domain,
normalization, and canonical relation for the Paper-5 coordinates. The
classical map does not choose a unique quantum spectrum.

### Claim C: the certified local dynamics controls localized quantum traces

This is the new constructive result. It must include chronological symbolic
localization and explicit orbit data, not an averaged transition matrix.

### Claim D: instability roof and action are complementary, not competing

The instability roof determines the stability amplitude. The action
determines the oscillatory phase. The period-four zero-action orbit is thereby
nonproblematic for quantum traces even though it failed as a positive
suspension clock.

### Claim E: no Hilbert--Pólya operator has yet been obtained

The full-plane quantum map is unitary but noncompact; the localized map is open
and generally nonunitary. Neither automatically supplies an ordered real
discrete energy spectrum, an arithmetic trace identity, a functional equation,
or the Riemann zeros.

## Proposed manuscript structure

### 1. Introduction: the spectral-object problem

- State Paper 5's motivating question fairly.
- Separate exact map, continuum surrogate, and finite Floquet matrix.
- State the new obstruction and local trace theorem.
- Declare all non-claims on page 1.

### 2. What survives from the original Hénon model

- Exact map, symplectic form, reversor, fixed points.
- Linear conjugacy to the standard conservative parameter convention.
- Exact elliptic fixed-point check at \(a=1.02\).
- Short reproducible explanation of why the old distance minimization does not
  certify tangency.
- Explain why the proof regime is the certified local survivor at \(a=6\),
  while \(a=1.02\) is only a mixed-phase negative control.

### 3. Weyl-law obstruction for the quartic surrogate

- State the static operator and its domain.
- Derive the phase-space volume.
- Evaluate the beta-function constant.
- Compare exponents with Riemann--von Mangoldt.
- Generalize to \(V(q)\sim\lambda|q|^d\).
- Delimit the theorem: no claim about every possible nonlocal/noncompact
  operator.

### 4. Exact discrete action and quantized Hénon map

- Derive \(S_a(q,Q)\).
- Factor the kernel into Fourier and cubic-phase operators.
- Prove unitarity and the canonical relation.
- Compare conventions with Fornæss--Weickert.
- Separate the frozen global/subprincipal phase convention from facts forced
  by the classical canonical relation; do not claim uniqueness of quantization.
- Discuss reversibility/antiunitary symmetry.
- Explain why a unitary quasienergy phase is not a canonically unwrapped
  self-adjoint energy.

### 5. Certified local survivor and chronological localization

- State only the R058/R059 results actually used.
- Distinguish \(\Lambda_*\) from the full bounded repeller.
- Define the four-state direct-sum operator and smooth cutoffs.
- Prove that closed symbolic paths correspond to the included stationary
  points.
- Prove trace class for the chosen localized blocks and certify that cutoff
  support introduces no additional stationary paths.

### 6. Local periodic-orbit trace theorem

- Write the \(n\)-step phase \(\Phi_n\).
- Derive the exact recurrence from stationarity.
- Prove
  \(\det D^2\Phi_n=(-1)^{n-1}\det(I-DH_6^n)\), treating \(n=1,2\)
  separately, and fix the Maslov phase from the frozen Fourier branch.
- Apply stationary phase with an explicit remainder.
- State the period range/uniformity honestly.

### 7. Instability amplitudes and the semiclassical determinant

- Prove the repeated-orbit amplitude identity in terms of \(T_p\).
- Insert discrete actions and instability times into the formal determinant.
- Treat the zero-action period-four orbit correctly.
- Include a determinant only if the fixed-contour gate passes.

### 8. Reproducible numerical validation

- Frozen protocol and independence of orbit/quantum implementations.
- Trace convergence versus \(\hbar\).
- Quadrature and cutoff controls.
- Wrong-adjacency, shuffled-action, and wrong-amplitude ablations.
- Boundary-artifact comparison with periodic FFT compactification.
- No Riemann data.

### 9. Route-A evaluation and Hilbert--Pólya boundary

- A1--A4 table.
- What has become natural/canonical.
- What remains local, open, cutoff dependent, or non-arithmetic.
- Why Route B is still unauthorized.

### 10. Conclusions

- The quartic fit is not the Hénon spectrum.
- A target-free periodic-orbit quantum bridge is possible locally.
- State exactly which theorem should be next: classical transfer-operator
  limit or a certified global horseshoe boundary.

### Appendices

- A. Coordinate and Fourier conventions.
- B. Weyl constant calculation.
- C. Hessian--monodromy determinant identity.
- D. Certified orbit/action/Maslov tables.
- E. Numerical error and cutoff definitions.
- F. Legacy tangency-algorithm audit.

## Figure and table plan

Only figures that answer a claim are allowed.

1. **Object diagram:** exact Hénon map versus quartic surrogate versus exact
   quantum map, showing which arrows are derived and which are not.
2. **Counting-law figure:** local slope of the quartic counting function
   tending to \(3/4\), with the analytic law overlaid; no fitted zero data.
3. **Certified localization figure:** the four rectangles and a few closed
   itineraries, clearly labeled as the local survivor.
4. **Trace convergence figure:** complex trace discrepancy versus \(\hbar\)
   for frozen periods.
5. **Mechanism-control figure:** correct formula against action/amplitude/
   adjacency ablations.
6. **Route-A table:** achieved and missing criteria.

No “quantum levels versus Riemann zeros” figure will appear.

## Milestones and calendar

### Weeks 1--2: foundations freeze

- Complete full-text audit of Fornæss--Weickert and trace-formula prior art.
- Complete the Helleman, Weickert, and Shudo--Ikeda comparison before any
  pilot code is authorized.
- Check all coordinate/Fourier conventions independently.
- Write T1--T3 proofs.
- Freeze the exact scope of the Weyl no-go.
- Run R010 and R020 as audits, not headline experiments.

Exit gate: two independent derivations agree on the Weyl constant, map
orientation, kernel phase, and reversor.

### Weeks 3--5: local quantum operator and orbit bridge

- Implement chronological direct-sum kernel.
- Import and independently validate local certified cycles.
- Compute actions, Hessians, signatures, and multipliers.
- Prove the Hessian--monodromy identity.
- Only if G0 passes, finish R000 and freeze R001.

Exit gate: all period-1--12 orbit identities pass, with no quantum data used
to repair orbit labels.

### Weeks 6--8: main trace experiment

- Run R050, R051, and R060.
- Complete mechanism ablations R070.
- Establish or falsify the semiclassical error trend.
- Convert numerical constants into rigorous/computer-assisted enclosures where
  feasible.

Exit gate: the preregistered trace criterion passes across cutoffs and
quadratures. If it fails, choose the appropriate negative-results paper.

### Weeks 9--10: theorem strengthening

- Attempt a useful uniform period range.
- Decide whether R080 determinant work is justified.
- Do not add determinant zeros without a contour/tail theorem.

Exit gate: freeze the exact main theorem and remove every stronger sentence.

### Weeks 11--12: manuscript and independent reproduction

- Draft paper in dependency order.
- Run R090 from a clean environment/separate implementation.
- Complete Route-A review.
- Compile, artifact-check, and produce repository update.

### Weeks 13--16, optional

- Log-time trace estimates or fixed-contour determinant certification.
- If these remain incomplete, defer them; do not delay a correct fixed-time
  paper indefinitely.

## Decision gates

### Gate G0: novelty

Read Tabor (1983), Helleman (1988), Fornæss--Weickert (2000), Weickert (2004),
Shudo--Ikeda (2008), and Shudo--Ikeda (2016), then perform a targeted primary-source search
for Hénon-specific localized trace/determinant results. Verify whether
Weickert's purely continuous-spectrum parameter regime includes the present
operator after exact coordinate/Fourier conjugacy. If the intended T4--T5
package is not materially stronger than this prior art, keep the project
deferred and use the classical Ruelle-operator route.

### Gate G1: analytic correctness

- Weyl coefficient independently checked.
- Fourier/global phase fixed.
- Generating function produces the correct, not inverse, map.
- Exact scope of unitarity and canonical relation stated.

### Gate G2: classical completeness

- Every included fixed point belongs to the certified local survivor.
- No claim of full-repeller completeness.
- R059 adjacency and orbit counts reproduced independently.

### Gate G3: numerical convergence

- Quadrature error subordinate to semiclassical error.
- Error decreases with \(\hbar\) on the frozen period set.
- Results persist across cutoff families.

### Gate G4: mechanism specificity

- Correct actions, amplitudes, and adjacency outperform all frozen ablations.
- No fitted phase, scale, or branch index is introduced.

### Gate G5: determinant honesty

- Either prove a determinant/tail result or omit infinite-determinant claims.

### Gate G6: Hilbert--Pólya firewall

- No Riemann-zero table is read by the code.
- No arithmetic interpretation is promoted beyond evidence.
- Route B evaluator must return “unauthorized/not reached.”

## Risk register

| Risk | Likelihood | Impact | Mitigation / pivot |
|---|---:|---:|---|
| Fixed-time trace theorem judged standard | Medium | High | Add explicit certified constants, useful period range, or contour control |
| Cutoff localization creates extra stationary points | Medium | High | Use state-indexed chronological cutoffs and certify stationary support |
| Full-plane spectrum is not discrete | High | Expected | Make this part of the obstruction, not a surprise |
| Open resonances drift with cutoff | Medium | High | Claim fixed-time microlocal traces only; publish drift as negative if robust |
| Maslov/Fourier sign error | Medium | High | Two independent symbolic/numerical derivations; period-1 analytic control |
| Existing orbit catalogue mistaken for full horseshoe | Medium | High | Repeat “local survivor” in theorem statements and artifact schemas |
| Semiclassical cancellation makes relative error unstable | High | Medium | Use amplitude-normalized error and separate phase/magnitude metrics |
| Determinant tail cannot be bounded | High | Medium | Stop at trace theorem; no zero claim |
| Arithmetic temptation after a visually suggestive root | Medium | High | Frozen no-target protocol and Route-A review |

## Publication fallback ladder

1. **Best case:** Weyl no-go + controlled local trace + determinant contour.
2. **Minimal positive paper:** Weyl no-go + explicit fixed-time certified trace
   theorem and strong mechanism controls.
3. **Negative foundations paper:** Weyl no-go + reproducible proof that every
   natural localization tested is cutoff/boundary dependent.
4. **Pivot:** if the trace contribution is not novel or not robust, move to a
   Ruelle-operator approximation theorem for the instability suspension.

## Deliberately separate future papers

### Classical global-threshold paper

Computer-assisted certification of the conservative horseshoe-closing
homoclinic tangency near \(a\simeq5.699310787\), including quadratic tangency,
generic unfolding, branch ordering, and full-repeller versus local-survivor
distinction.

### Historical N+1 classical operator-limit plan

Construction of a specified Ruelle operator for the non-lattice instability
roof, finite-memory approximation, and a fixed-contour determinant/tail bound.
This project is retained at `../next_paper_henon_ruelle_operator/` as
foundation, control, and fallback. It is no longer preselected.

### Any later arithmetic paper

Allowed only after an intrinsic arithmetic mechanism is found. It must not be
obtained by fitting actions, clocks, cutoffs, \(\hbar\), or phase-unwrapping
branches to zero ordinates.
