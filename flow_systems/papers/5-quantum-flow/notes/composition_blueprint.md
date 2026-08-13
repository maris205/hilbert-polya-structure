# Composition Blueprint — Paper 5

Date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2-KOOPMAN-P1`  
Status: proof-complete composition plan; not a manuscript

## 1. Proposed paper identity

**Working title**

> The Canonical Koopman Lift Is Too Large: Dense Rational Spectrum for a
> Frobenius Suspension

**Alternative title**

> From Frobenius Circles to a Self-Adjoint Obstruction

**Central thesis**

The constant-roof Frobenius suspension from Paper 4 possesses an entirely
natural, same-clock Koopman unitary group with a rigorously defined
self-adjoint Stone generator. Precisely because every closed-point degree
occurs, its Fourier frequencies fill
\((2\pi/\log2)\mathbb Q\), every point frequency is infinitely degenerate,
and the full and essential spectra are \(\mathbb R\). This exact positive
B1--B2 result is therefore an exact B3 obstruction, not a Hilbert--Pólya
candidate. The orbit Hasse--Weil product and the etale-cohomological
Frobenius determinant must remain distinct from the Koopman generator ledger.

**Paper type**

- theorem-and-obstruction operator paper;
- natural-lift audit of an already frozen classical object;
- exact spectral analysis, not numerical spectroscopy;
- Route A / A4 plus limited Route B / B1--B3;
- no physical-quantization, B4, B5, or Hilbert--Pólya claim.

**Recommended length**

Approximately 6,500--8,500 words, excluding appendices and bibliography.

## 2. Abstract logic

Use five or six sentences:

1. Recall the methodological question: when a classical arithmetic flow has
   an exact orbit zeta, does its most natural unitary lift have the spectral
   type needed for a determinant realization?
2. Name the fixed object: the constant-roof \(\log2\) suspension of Frobenius
   on the discrete geometric points of
   \(\mathbb P^1_{\mathbb F_2}\).
3. Define the canonical lift in one phrase: Koopman translations on the
   Hilbert direct sum of all closed-point suspension circles, with Stone
   generator \(\bigoplus_x(-i\,d/du)_{\rm per}\).
4. State the spectral theorem:
   \(\sigma_{\rm p}=(2\pi/\log2)\mathbb Q\), every point eigenvalue has
   countably infinite multiplicity, and
   \(\sigma=\sigma_{\rm ess}=\mathbb R\).
5. State the functional-analytic consequences: no compact resolvent, locally
   finite eigenvalue count, or trace-class heat; positive component weights
   cannot help because they are unitarily equivalent.
6. State the calibrated conclusion: the natural unitary lift passes B1--B2
   and proves B3 failure, while the Hasse--Weil cohomological determinant is a
   different operator ledger.

Do not mention target-zero computations, GUE statistics, or fitted spectra.

## 3. Main contribution package

### Theorem A — measure and unitary-equivalence class

For every family \(0<w_x<\infty\), the invariant measure
\(\mu_w|_{C_x}=w_xdu_x\) is sigma-finite, Radon, and full-support, and

\[
W_wf=(\sqrt{w_x}f_x)_x
\]

unitarily intertwines its Koopman group and generator with the canonical
\(w_x=1\) version.

### Theorem B — complete operator definition

\[
A_w=\bigoplus_x\left(-i\frac d{du}\right)_{\rm per}
\]

is self-adjoint on the componentwise periodic \(H^1\) domain with global
graph-norm square summability and is the unique Stone generator of
\(U_tf=f\circ\phi^{-t}\).

### Theorem C — spectral classification

\[
\sigma_{\rm p}(A_w)=\frac{2\pi}{\log2}\mathbb Q,
\qquad
\sigma(A_w)=\sigma_{\rm ess}(A_w)=\mathbb R,
\qquad
\sigma_{\rm disc}(A_w)=\varnothing.
\]

Every point eigenvalue has countably infinite multiplicity. The eigenvectors
form a complete pure-point basis, while irrational real numbers are
set-theoretic continuous-spectrum points.

### Corollary D — B3 obstruction

The resolvent is noncompact; every interval of positive width has an
infinite-rank spectral projection; \(e^{-tA_w^2}\) and \(e^{-t|A_w|}\) are not
trace class; these failures remain after zero-mode deletion.

### Proposition E — determinant ledger separation

The primitive-orbit Hasse--Weil product, the alternating finite-dimensional
etale Frobenius determinant, and the Koopman/Stone operator act on distinct
ledgers. Their shared arithmetic source supplies no determinant identity for
\(A_w\).

## 4. Recommended section architecture

### 1. Introduction

- Begin with the strongest outcome: the canonical operator exists and is
  self-adjoint, but exact spectral analysis rejects it as a spectral host.
- Explain why a negative B3 theorem is useful after an exact classical orbit
  zeta: it prevents operator-ledger substitution.
- State Theorems A--C and Corollary D.
- State the calibrated route tuple only for the invoked layers:
  A4 unitary candidate, B1 complete, B2 self-adjoint, B3 fail.
- Avoid presenting B4/B5 verdicts; say they are outside the limited audit.

### 2. The frozen Frobenius suspension

- Reproduce only the definitions needed from Paper 4.
- State the discrete topology as inherited `MODELING_CHOICE`.
- State the circle decomposition
  \(M_F=\coprod_x\mathbb R/(\deg x\log2)\mathbb Z\).
- Emphasize that no new roof, potential, phase, or component coupling is
  introduced.
- Cite Paper 4 for the orbit/Hasse--Weil identity rather than reproving the
  entire classical paper.

### 3. Closed-point degree support

- Cite Deligne for closed points as Frobenius orbits.
- Cite Niederreiter--Xing for the irreducible-polynomial count.
- Record \(a_1=3\) and the Möbius formula for \(d\ge2\).
- Prove \(a_d>0\) with the elementary domination bound.
- Explain the minimality result: one point per degree already forces the later
  infinite degeneracy.

### 4. Invariant measures and the canonical Hilbert class

- Define counting-times-flow-time measure first.
- Prove invariant, sigma-finite, Radon, and full-support properties.
- Introduce arbitrary positive component weights.
- Prove the \(W_w\) unitary intertwiner.
- Mention probability weights and normalized Haar as corollaries, not as
  separate candidates.
- State why a zero weight deletes arithmetic data and creates a new object.

### 5. Koopman group, domain, and self-adjointness

- Freeze \(U_tf=f\circ\phi^{-t}=f(u-t)\) and
  \(U_t=e^{-itA}\).
- Prove strong continuity by finite-component approximation.
- Give the full periodic Sobolev domain, not only the formal expression
  \(-i\,d/du\).
- Diagonalize each circle by Fourier series.
- Invoke the orthogonal-sum theorem.
- Check the sign of the generator explicitly.
- State B1 and B2 verdicts at the end of the section.

### 6. Exact point spectrum and degeneracies

- Derive \(2\pi n/(d\log2)\) on a degree-\(d\) component.
- Take the union over all degrees to obtain
  \((2\pi/\log2)\mathbb Q\).
- Prove the converse by restricting an eigenvector to a nonzero component.
- For \(q=a/b\), use degrees \(kb\), modes \(ka\), and distinct components.
- Treat \(q=0\) explicitly.
- State countably infinite, not merely infinite, multiplicity.

### 7. Full spectrum, essential spectrum, and terminology

- Apply the direct-sum spectrum theorem and rational density.
- Give the short infinite-rank-neighborhood proof of
  \(\sigma_{\rm ess}=\mathbb R\).
- Optionally include the explicit singular Weyl sequence as a second proof.
- Add a boxed terminology warning:
  complete pure-point eigenbasis does not imply discrete spectrum.
- Identify irrational reals as continuous-spectrum points without claiming
  continuous spectral measure.

### 8. Compactness, counting, and trace obstructions

- Use zero modes for the shortest noncompact-resolvent proof.
- Immediately add the nonzero rational-eigenspace control to show the result
  is not a removable-kernel artifact.
- State the correct interval quantifier: every interval of positive width,
  not every nonempty Borel set.
- Define \(N(E)\) and show it is infinite for every \(E\ge0\).
- Use \(e^{-tA^2}\) and \(e^{-t|A|}\), not \(e^{-tA}\).
- Conclude B3 fail.

### 9. Why the orbit zeta is not this spectral determinant

- Present a three-row operator ledger:
  Koopman/Stone, primitive-orbit/transfer, etale cohomology/Frobenius.
- Cite Bornemann only for the ordinary trace-class Fredholm determinant
  boundary.
- Cite Deligne equation (1.5.4) for the cohomological determinant.
- Invoke Paper 3 T0/T3/T5 same-object fields.
- Allow a carefully scoped sentence that relative or renormalized
  determinants may be new research objects after additional choices.

### 10. Koopman representation versus physical quantization

- Define what was actually constructed: unitary transport of observables.
- List the missing source-locked structure:
  symplectic/prequantum/polarization or another explicit quantization rule.
- Avoid the overly broad claim that no geometric quantization can exist.
- Assign `A4_UNITARY_OR_SCATTERING_CANDIDATE`, but not
  `A4_NATURAL_QUANTIZATION` or `A4_ROUTE_B_READY`.

### 11. Controls, limitations, and route verdict

- Present weight, one-point-per-degree, zero-removal, and finite-cutoff
  controls.
- State that coupling or potentials create new candidates.
- Give exactly the B1, B2, B3 enums.
- Explain that the Riemann-target Route-A rejection from Paper 4 remains
  unchanged.
- Conclude with the Paper 6 stop condition: no formal prime trace may be
  transplanted into \(A_w\) without a same-object bridge.

### Appendices

- Appendix A: count of closed points in every degree.
- Appendix B: Fourier and direct-sum domain details.
- Appendix C: singular Weyl sequences and spectral-type terminology.
- Appendix D: deterministic controls, hashes, and environment.

## 5. Proof ordering

The paper should not reveal the operator and postpone its domain. Use:

```text
frozen circles
  -> measure
  -> Hilbert direct sum
  -> Koopman group
  -> periodic domain
  -> self-adjoint generator
  -> Fourier spectra
  -> global/essential spectrum
  -> B3 consequences
  -> determinant-ledger separation
```

This ordering ensures B1 is complete before B2 and prevents a formal
Hamiltonian from appearing ahead of its mathematical object.

## 6. Source placement

| Claim location | Primary/authoritative source |
|---|---|
| closed points as Frobenius orbits | Deligne §1.4 |
| cohomological determinant | Deligne equation (1.5.4) |
| irreducible-polynomial count | Niederreiter--Xing Theorem 1.3.6 |
| Koopman definition/context | ter Elst--Lemańczyk Introduction |
| direct-sum self-adjointness/spectrum | Teschl Theorem 2.23 |
| Stone theorem | Teschl Theorems 5.1--5.2; historical Stone 1932 |
| compact/trace-class/essential definitions | Teschl §§6.2--6.4 |
| ordinary Fredholm determinant boundary | Bornemann §3 |
| same-object rule | Paper 3 same-object certificate T0--T7 |

Do not cite a source for a stronger claim than it proves. In particular:

- ter Elst--Lemańczyk does not compute this candidate's spectrum;
- Teschl does not prove that closed points occur in all degrees;
- Deligne does not identify etale Frobenius with the circle derivative;
- Bornemann does not rule out every conceivable regularized determinant.

## 7. Tables and displays

Recommended main-text tables:

1. frozen operator definition: space, measure, group, domain, action, clock;
2. theorem ledger: point spectrum, multiplicity, full/essential spectrum,
   resolvent, heat;
3. three distinct operator ledgers;
4. Route A4 and limited B1--B3 verdicts.

Recommended displays:

- the component decomposition;
- the weight intertwiner;
- the full generator domain;
- the normalized Fourier eigenvectors;
- the boxed spectrum theorem;
- the degree-\(kb\), mode-\(ka\) multiplicity witness;
- the noncompact-resolvent action on an orthonormal sequence.

No eigenvalue scatterplot is needed: the exact rational set and multiplicities
are clearer as formulas.

## 8. Deterministic-control placement

Code artifacts may verify:

- exact Möbius closed-point counts for finite degree ranges;
- positivity and fixed-point reconstruction;
- rational-frequency witnesses \((kb,ka)\);
- weight-norm and translation-intertwining identities on finite Fourier
  vectors;
- persistence of a nonzero infinite-multiplicity witness after deleting zero.

These are regression controls, not evidence for the infinite theorems. All
theorems must appear before finite outputs in the exposition.

## 9. Route-reporting block

Use this compact text in the paper:

```text
Route A / A4:
  A4_UNITARY_OR_SCATTERING_CANDIDATE (PROVED)
  not A4_NATURAL_QUANTIZATION
  not A4_ROUTE_B_READY

Limited Route B:
  B1_COMPLETE_OPERATOR_DEFINITION (PROVED)
  B2_SELF_ADJOINT (PROVED)
  B3_FAIL (PROVED)
  B4 and B5 not invoked

Scoped overall:
  ROUTE_B_REJECTED at Gate C
  hilbert_polya_claim_allowed: false
```

Do not serialize an invented “not invoked” value as a B4 or B5 layer enum.

## 10. Mandatory phrasing boundaries

Use:

- “canonical Koopman unitary lift”;
- “self-adjoint Stone generator”;
- “complete pure-point eigenbasis with dense point spectrum”;
- “irrational continuous-spectrum accumulation points”;
- “every interval of positive width has infinite projection rank”;
- “standard compact-resolvent/Fredholm determinant mechanisms fail”;
- “cohomological Frobenius acts on a different operator ledger”;
- “physical quantization is not supplied by the frozen data.”

Avoid:

- “quantum Hamiltonian” without qualification;
- “discrete spectrum”;
- “continuous spectral measure” for the irrational points;
- ambiguous nonempty-window wording that would include singleton sets;
- “heat kernel \(e^{-tA}\)”;
- “Deligne determinant of the Koopman generator”;
- “no determinant can ever be regularized”;
- “B4 fail” or “B5 fail” in this limited Phase 1 audit;
- any Riemann-zero language beyond the explicit claim boundary.

## 11. Anticipated referee objections

### “Positive weights could suppress high-degree circles.”

They suppress norms but not unitary equivalence: componentwise multiplication
by \(\sqrt{w_x}\) exactly intertwines the representations. Vanishing weights
would delete components and are excluded.

### “Infinite multiplicity is caused only by constant functions.”

No. For any nonzero \(a/b\), degrees \(kb\) and modes \(ka\) provide
infinitely many eigenvectors with that same nonzero frequency.

### “A complete eigenbasis contradicts continuous spectrum.”

No. Spectral measures can be atomic while the closed spectral set contains
non-eigenvalue accumulation points. State both notions and prove the irrational
range characterization.

### “A finite truncation has a determinant.”

Correct, but it is a different finite object. A convergence/renormalization
theorem would require an independently frozen scheme and cannot be inferred
from the cutoff.

### “The Hasse--Weil determinant already solves the operator problem.”

It solves a finite-dimensional etale-cohomological determinant problem. The
paper's point is that this operator is not the Koopman/Stone generator.

### “Koopman mechanics is a quantization.”

It is a useful Hilbert-space representation of classical dynamics. The Route
A evaluator's physical/natural-quantization label requires additional
source-derived structure that is not present here.

## 12. Final composition checklist

- [ ] candidate ID appears in title page metadata;
- [ ] Paper 4 object is quoted without silently changing topology or clock;
- [ ] canonical and weighted measures are both defined;
- [ ] \(W_w\) intertwines group, domain, and generator;
- [ ] the complete domain precedes the self-adjointness claim;
- [ ] the sign convention is checked;
- [ ] the count \(a_d>0\) is proved for all \(d\);
- [ ] point spectrum equality includes the converse;
- [ ] infinite multiplicity includes nonzero frequencies;
- [ ] pure-point measures and irrational continuous-spectrum points are
  distinguished;
- [ ] all interval claims say “positive width”;
- [ ] zero-mode deletion appears as a control;
- [ ] heat uses \(A^2\) or \(|A|\);
- [ ] determinant ledgers are in separate rows;
- [ ] A4 does not become a physical-quantization claim;
- [ ] B4/B5 receive no verdict;
- [ ] no target-zero or fitted data appear;
- [ ] limitations precede future-work speculation.

## 13. Closing paragraph logic

End with three calibrated sentences:

1. the Frobenius suspension does possess a fixed, natural self-adjoint Koopman
   generator;
2. its exact dense, infinitely degenerate spectrum proves that this generator
   cannot be the required locally finite determinant host;
3. any next-stage trace interface must identify a different source-derived
   operator and a rigorous same-object morphism, rather than transplant the
   Hasse--Weil ledger into \(A_K\).
