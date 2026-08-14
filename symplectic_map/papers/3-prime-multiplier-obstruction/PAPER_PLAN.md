# Paper Plan

**Working title:** *Derivative Content Excludes Raw Rational-Prime Multipliers: An
Exact Audit of a Frozen PCF Quadratic*  
**One-sentence contribution:** For a monic algebraic-integer polynomial with
formal derivative (F'=mH), every rational multiplier at a point fixed by
(F^n) lies in (m^n\mathbb Z); at the inherited PCF quadratic this excludes
raw rational-prime multipliers at every period, while exact computations
through period four audit the implementation and a cotangent construction
transports the same obstruction only on regular symplectic branches.  
**Paper type:** theory + exact certification note  
**Target:** specialist arithmetic/complex/nonlinear-dynamics note, using the
Session's article format rather than an ML conference template  
**Date:** 2026-08-13  
**Main-text target:** 8--10 pages before references; proofs and complete
machine certificates may continue in appendices.

## Claims--Evidence Matrix

| Claim | Evidence | Status | Planned location |
|---|---|---|---|
| C1. If (F\in\mathcal O_K[X]) is monic and (F'=mH), then a rational multiplier of (F^n) belongs to (m^n\mathbb Z). | Self-contained integrality and chain-rule proof in `notes/PROOF_PACKAGE.md`; twelve proof-boundary gates in `results/proof_audit.json`. | Proved all-period | Sec. 3 |
| C2. The frozen (g(z)=z^2-u), and hence (f_u(x)=1-ux^2), has no raw rational-prime multiplier at any period. | C1; exact exclusion of the fixed multipliers (pm2); conjugacy audit. | Proved all-period | Sec. 4 |
| C3. Odd rational exponent-prime bases are excluded, while base (2) at periods (n\ge2) remains open. | Exact 2-adic argument and frozen negative-result ledger. | Proved boundary / open residue | Secs. 4 and 7 |
| C4. Periods (1\le n\le4) have the declared exact multiplier polynomials and no rational roots. | Independent dynatomic/resultant/quotient-ring pipelines; `results/exact_polynomials.json`; coordinate-conjugacy duplication in `results/conjugacy_audit.json`. | Exactly audited at cutoff | Sec. 5 |
| C5. The computation can detect positive cases and assumption failures. | Controls (z^2,z^2-2,z^2-3/4), including raw prime (3), Chebyshev values, and saturated formal-period contamination. | Exactly audited | Sec. 5 |
| C6. The cotangent formula is exact symplectic only on (q\ne0) branches and carries return eigenvalues ((\lambda,\lambda^{-1})). | One-form/determinant identities and computed singular/noncompact/overlap witnesses in `results/symplectic_bridge_audit.json`. | Proved with strict boundary | Sec. 6 |
| C7. The experiment used no external prime/zero table, floating recognition, or post-hoc high-period search. | Source-lock hash, static isolation scan, command manifest, final artifact manifest, 37-test XML. | Verified | Sec. 5 and Appendix C |

## Narrative and contribution boundary

The paper tells one story: replacing a finite-memory clock by the genuine
nonlinear derivative does not rescue the frozen arithmetic candidate, because
algebraic integrality imposes an even sharper exact obstruction.  The general
divisibility lemma is elementary and receives no priority claim.  The paper's
defensible contribution is the complete certificate chain for one inherited
candidate: all-period theorem, exact low-period audit, adversarial controls,
coordinate duplication, and a convention-safe symplectic bridge.

The manuscript must never claim:

- absence of every rational multiplier;
- absence of (|\lambda|=2^n) for (n\ge2);
- a theorem about complex modulus without rationality of (lambda);
- a global, compact, everywhere-defined symplectic lift;
- novelty for dynatomic polynomials, multiplier integrality, or cotangent
  constructions;
- evidence for a prime-orbit correspondence, Riemann determinant,
  quantization, or Route B.

## Section plan

### Abstract (170--210 words)

- Lead with the exact all-period divisibility theorem and frozen consequence.
- Explain that finite orbit searches cannot establish the result and are used
  only as implementation audits.
- Report the concrete audit: four exact periods, four empty rational-root
  sets, three controls, 37 passing tests.
- State the open boundary (p=2,n\ge2) for rational exponent-prime targets.
- End with the branchwise, singular cotangent-lift limitation.

### 1. Introduction

- Motivate intrinsic prime clocks: primitive repetitions require an exact
  arithmetic clock, not a merely chaotic orbit ledger.
- Attribute the frozen PCF parameter and prime-symbolic motivation to the
  author's earlier Logistic-map work, without importing its data or claims.
- Explain why Paper 1's finite-rank obstruction does not cover the
  point-dependent nonlinear derivative.
- State the one-sentence contribution before technical background.
- Give three falsifiable contributions: theorem/corollary, exact audit with
  controls, and strict symplectic-bridge boundary.
- Preview the all-period negative result and the base-2 open residue.
- Place Figure 1 here.

### 2. Prior work and claim boundary

- Arithmetic dynamics, dynatomic polynomials, and multiplier polynomials:
  Morton--Silverman; Silverman; Murakami--Sano--Takehira; Huguin.
- Global rational/integer multiplier rigidity versus the present sparse-value
  question: Huguin; Buff--Gauthier--Huguin--Raissy; Ji--Xie.
- Infinite-dimensional characteristic-exponent span as the boundary against
  a finite-rank nonlinear claim: Ji--Xie--Zhang.
- Logistic/one-dimensional symplectic-extension precedent: Fogedby--Jensen;
  Demaeyer--Gaspard.
- Explicitly rate the result as a narrow design certificate, not a new general
  multiplier theory.

### 3. Derivative-content divisibility

- Define finite fixed-by-(F^n) points and rational multipliers.
- State Theorem A over a number field.
- Prove: monic fixed equation gives algebraic-integral orbit; chain rule gives
  (m^n\beta); a rational algebraic integer is an integer.
- Include an assumption/scope table: monicity, algebraic-integer
  coefficients, derivative content, rational multiplier, finite point.
- Discuss sharpness using (z^2), which realizes (2^n).

### 4. Frozen PCF specialization

- Isolate the unique real root of (u^3-2u^2+2u-2) and note integrality.
- Give the exact conjugacy (\phi(x)=-ux) from (f_u) to (g(z)=z^2-u).
- Prove raw-prime exclusion for (n\ge2) by divisibility.
- Close (n=1): multipliers (pm2) force (u=0) or (u=2), both excluded.
- Separate raw-prime and exponent-prime definitions in a boxed comparison.
- Prove odd exponent-prime exclusion and label the base-2 higher-period case
  `OPEN`.

### 5. Exact audit and controls

- State before the table that computation audits implementation but carries
  no all-period inference.
- Describe formal dynatomic versus exact period, repeated saturation at
  root-of-unity collisions, point resultants, cycle grouping, quotient-ring
  annihilation, and exact rational-root classification in (1,u,u^2).
- Table 1: period, formal/exact degree, cycles, multiplier polynomial,
  rational roots.
- Table 2: three controls and what failure mode each detects.
- Report the independent (f_u/g) agreement, 37 tests, runtime/memory as
  engineering diagnostics only, and zero external target access.
- Place Figure 2 here.

### 6. What the symplectic bridge does—and does not do

- Define (\widehat g(q,p)=(q^2-u,p/(2q))) for (q\ne0).
- Prove exact preservation of (p\,dq).
- For zero-section periodic orbits contained in the regular locus \(q\ne0\),
  derive reciprocal return eigenvalues \((\lambda,\lambda^{-1})\).
- Record four obstructions: singular critical line, two-to-one/overlapping
  branch images, noncompactness, no lift of a critical zero multiplier.
- Place Figure 3 here.

### 7. Discussion and stopping decision

- The genuine nonlinear derivative escapes the finite-rank theorem but fails
  for a different arithmetic reason.
- State the candidate-specific Route-A outcome: raw-prime A0 failure; no
  determinant fitting, zero comparison, or quantization.
- Explain why more finite-period sampling cannot strengthen the all-period raw
  result and cannot close the base-2 exponent residue.
- List the two legitimate next questions: all-period unit-product analysis for
  the base-2 residue, or a separately source-locked global symplectic carrier.

### Appendices

- A. Full proof dependency ledger and theorem variants.
- B. Exact multiplier-polynomial derivation and complete period 1--4
  certificates.
- C. Source lock, command manifest, code-review closure, environment, hashes,
  and reproduction command.
- D. Control saturation details and symplectic symbolic identities.

## Figure and table plan

| ID | Type | Description | Frozen data source | Priority |
|---|---|---|---|---|
| Figure 1 | Three-panel hero certificate | (a) integrality/divisibility proof chain, (b) frozen raw rational-prime gate closes at all periods while the rational \(p=2\) exponent-prime gate stays open, (c) the local cotangent bridge preserves reciprocal multipliers only for regular zero-section cycles and fails globality at \(q=0\). | `experiments/source_lock.json`, `results/proof_audit.json`, `results/negative_result_ledger.json`, `results/symplectic_bridge_audit.json` | High |
| Figure 2 | Exact audit/control panel | Candidate period 1--4 exact degrees and empty rational-root counts beside control detections \(2^n\), Chebyshev signs, raw prime \(3\), and complete removal of the formal period-2 contamination for \(z^2-3/4\); visually distinguish theorem from cutoff audit. | `results/candidate_multiplier_audit.json`, `results/control_audit.json`, `results/exact_polynomials.json`, `results/conjugacy_audit.json` | High |
| Figure 3 | Symplectic scope schematic | Two regular cotangent branches, singular critical line, overlapping base images, zero section, and reciprocal return spectrum; every annotation pulled from the frozen bridge audit. | `results/symplectic_bridge_audit.json` | Medium |
| Table 1 | Exact candidate ledger | Four exact cycle multiplier polynomials and rational-root verdicts. | `results/exact_polynomials.json` | High |
| Table 2 | Matched controls | Assumption status, exact multipliers by period, and diagnostic role. | `results/control_audit.json` | High |
| Table 3 | Claim/prior boundary | General result versus closest established machinery and explicit nonclaim. | `notes/NOVELTY_AUDIT.md` plus verified bibliography | Medium |

All plot scripts must read these JSON files rather than hardcode scientific
values.  Outputs must include vector PDF and a 300-dpi PNG preview, with a
shared style module and a generated `latex_includes.tex`.

## Citation plan

- Introduction: Wang (2026), DOI `10.1080/27684830.2026.2684334`, for
  genealogy; Berry--Keating only as historical
  clock motivation if the claim remains narrowly phrased.
- Arithmetic multiplier rigidity: Huguin (2021, 2022, 2023), Ji--Xie (2023),
  Ji--Xie--Zhang (2026), Buff et al. (2026).
- Dynatomic/multiplier machinery: Morton--Silverman (1994), Silverman (2007),
  Murakami--Sano--Takehira (2024), Huguin (2024), Levin (2009).
- Symplectic-extension precedent: Fogedby--Jensen (2005),
  Demaeyer--Gaspard (2009).

Every entry must be copied from an existing audited record or fetched from a
publisher/DOI endpoint.  No BibTeX record may be synthesized from memory.

## Plan-review checklist

- The all-period theorem, not the cutoff, carries C1--C3.
- The title says “raw prime multipliers” or defines the rationality condition
  immediately; it must not imply a modulus-only theorem.
- Figure 1 distinguishes raw and exponent targets at a glance.
- Controls include both theorem-compatible positive multipliers and the
  nonintegral raw-prime counterexample.
- The cotangent map is never called a global symplectomorphism.
- The conclusion stops downstream Route-A stages for this candidate.
